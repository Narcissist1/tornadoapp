# coding: utf-8

from fabric.api import *
from fabric.decorators import hosts
from config import VPS_CONN

env.proj_dir = '/root/tornadoapp'
env.code_base = 'git@github.com:Narcissist1/tornadoapp.git'


@hosts(VPS_CONN)
def deploy():
	with cd(env.proj_dir):
		run('git pull --ff')
		run('systemctl restart tornado.service')