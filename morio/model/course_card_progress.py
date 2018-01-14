from datetime import datetime

from sqlalchemy import Column, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy import Integer

from morio.model import db


class CourseCardProgress(db.Model):
    FEEL_EASY = 0
    FEEL_MEDIUM = 1
    FEEL_HARD = 2

    feels = [FEEL_EASY, FEEL_MEDIUM, FEEL_HARD]

    STATUS_TO_LEARN = 0
    STATUS_TO_REVIEW = 1
    STATUS_FINISHED = 2

    id = Column(Integer, primary_key=True, autoincrement=True)
    # 學習次數
    hits = Column(Integer, default=0, nullable=False)
    # 上一次掌握的時間
    last_time_grasped = Column(DateTime)
    # 今天的學習計劃
    # refresh every 12:00 am
    # todo: 記錄用戶時區來對應刷新時間
    today_status = Column(Integer)
    now_status = Column(Integer)
    last_feel = Column(Integer)

    # relationships
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    card_id = Column(Integer, ForeignKey('card.id'), nullable=False)

    __table_args__ = (
        UniqueConstraint('course_id', 'card_id', name='_course_id_card_id_uc'),
    )

    @staticmethod
    def record(course_id, card_id, feel):
        progress = CourseCardProgress.query \
            .filter_by(course_id=course_id, card_id=card_id).first()
        if not progress:
            return
        if feel == CourseCardProgress.FEEL_HARD:
            progress.now_status = CourseCardProgress.STATUS_TO_LEARN
        elif feel == CourseCardProgress.FEEL_EASY:
            progress.now_status = CourseCardProgress.STATUS_FINISHED
            progress.hits += 1
            progress.last_time_grasped = datetime.now()
        elif feel == CourseCardProgress.FEEL_MEDIUM:
            if progress.now_status == CourseCardProgress.STATUS_TO_REVIEW:
                progress.now_status = CourseCardProgress.STATUS_FINISHED
                progress.hits += 1
                progress.last_time_grasped = datetime.now()
            else:
                progress.now_status = CourseCardProgress.STATUS_TO_REVIEW
        progress.last_feel = feel
        with db.auto_commit():
            db.session.add(progress)
