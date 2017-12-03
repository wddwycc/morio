from fabric.api import env, cd, run, put, local

env.use_ssh_config = True
env.user = 'ubuntu'
env.hosts = ['duan-p0']


def update_flask():
    with cd('/code/morio'):
        run('git pull origin master')
        run('pipenv install')
        run('pipenv run python manage.py db upgrade')
        run('sudo systemctl restart morio.service')


def update_fn():
    local('npm run prod')
    put('dist/*', '/var/www/morio')


def deploy():
    update_fn()
    update_flask()
