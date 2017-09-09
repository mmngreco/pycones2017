#! /usr/bin/env python2

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from base import *

# En vez de copia y pega: decorador de clases

import time
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

import functools

def log(func):
    @functools.wraps(func)
    def wrapped(*args):  # omit **kwargs for simplicity
        # args[1:] so that we don't print 'self'
        logging.info('Called %s%s', func.__name__, args[1:])
        return func(*args)
    return wrapped


class Cyborg(object):

    @log
    def __init__(self, name):
        self.name = name
        self.weapon = DeathRay(ammunition=25)
        self.teleporter = TimeMachine()

    @log
    def travel(self, destination, year):
        self.teleporter.go(destination, year)
        time.sleep(0.25)  # not instant, but almost

    @log
    def attack(self, target):
        self.weapon.vaporize(target)

robot = Cyborg('T-1000')
robot.travel(destination='Los Angeles', year=1995)
robot.attack('Sarah Connor')
robot.attack('John Connor')
