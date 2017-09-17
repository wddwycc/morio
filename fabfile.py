from fabric.api import env, cd, run, put, local

env.use_ssh_config = True
env.user = 'root'
env.hosts = ['duan-p0']


def update_flask():
    pass


def update_front():
    local('npm run prod')
    put('dist/*', '/var/www/morio.monk-studio.com')
