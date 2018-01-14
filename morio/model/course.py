from datetime import datetime

import math
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func, or_, and_

from morio.model import db


def score_for_feel(feel):
    from morio.model import CourseCardProgress
    options = {
        CourseCardProgress.FEEL_EASY: 100,
        CourseCardProgress.FEEL_MEDIUM: 80,
        CourseCardProgress.FEEL_HARD: 0,
    }
    return options.get(feel)


def memory_stability(review_times):
    options = {
        0: 1,
        1: 1,
        2: 4,
        3: 7,
        4: 13,
        5: 30,
        6: 70,
    }
    return options.get(review_times, 150)


class Course(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    repository_id = Column(
        Integer, ForeignKey('repository.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    progresses = relationship('CourseCardProgress',
                              backref='course', lazy='dynamic')

    def to_dict(self):
        repo = self.repository
        return dict(
            id=self.id,
            repository=repo.to_dict(),
        )

    def next(self):
        from morio.model import CourseCardProgress

        options = [
            CourseCardProgress.STATUS_TO_LEARN,
            CourseCardProgress.STATUS_TO_REVIEW,
        ]
        progress = CourseCardProgress.query.filter_by(course_id=self.id) \
            .filter(CourseCardProgress.now_status.in_(options)) \
            .order_by(func.random()).first()
        if not progress:
            return None
        card = progress.card
        repo = card.repository
        to_learn = CourseCardProgress.query.filter_by(course_id=self.id) \
            .filter_by(now_status=CourseCardProgress.STATUS_TO_LEARN) \
            .count()
        to_review = CourseCardProgress.query.filter_by(course_id=self.id) \
            .filter_by(now_status=CourseCardProgress.STATUS_TO_REVIEW) \
            .count()
        summary = dict(to_learn=to_learn, to_review=to_review)
        return dict(
            data=dict(card=card, repo=repo),
            summary=summary,
        )

    def refresh_progress(self):
        from morio.model import CourseCardProgress
        # clear status
        with db.auto_commit():
            for row in CourseCardProgress.query.filter_by(course_id=self.id):
                row.today_status = None
                row.now_status = None
        # map hard feeling to last_time_grasped = None, hits = 0
        last_feeling_hard = CourseCardProgress.query \
            .filter_by(course_id=self.id, last_feel=CourseCardProgress.FEEL_HARD) \
            .all()
        with db.auto_commit():
            for item in last_feeling_hard:
                item.hits = 0
                item.last_time_grasped = None
                db.session.add(item)
        # to learn
        to_learn_max = 30
        progresses = CourseCardProgress.query \
            .filter_by(course_id=self.id, last_time_grasped=None) \
            .limit(to_learn_max)
        with db.auto_commit():
            for progress in progresses:
                progress.today_status = CourseCardProgress.STATUS_TO_LEARN
                progress.now_status = CourseCardProgress.STATUS_TO_LEARN
                db.session.add(progress)
        # to review
        to_review_max = to_learn_max * 6
        to_review = CourseCardProgress.query \
            .filter_by(course_id=self.id) \
            .filter(CourseCardProgress.last_time_grasped.isnot(None)) \
            .all()
        to_review_measurements = list()
        for item in to_review:
            delta_day = (datetime.now() - item.last_time_grasped).days
            m = score_for_feel(item.last_feel or CourseCardProgress.FEEL_HARD) * \
                math.exp(-delta_day / memory_stability(item.hits - 1))
            to_review_measurements.append((m, item))
        to_review_measurements.sort(key=lambda x: x[0])
        to_review = [x[1] for x in to_review_measurements if x[0] < 50]
        to_review = to_review[:to_review_max]
        for item in to_review:
            with db.auto_commit():
                item.today_status = CourseCardProgress.STATUS_TO_REVIEW
                item.now_status = CourseCardProgress.STATUS_TO_REVIEW
                db.session.add(item)
