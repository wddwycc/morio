from fabric.api import env, cd, run, put, local

env.use_ssh_config = True
env.user = 'ubuntu'
env.hosts = ['duan-p0']


def update_flask():
    with cd('/code/morio'):
        run('git pull origin master')
        run('/var/venv/morio/bin/pip install -r requirements.txt')
        run('sudo systemctl stop morio.service')
        run('/var/venv/morio/bin/python manage.py db upgrade')
        run('sudo systemctl start morio.service')


def update_fn():
    local('npm run prod')
    put('dist/*', '/var/www/morio.monk-studio.com')


def publish():
    update_flask()
    update_fn()
