#! /usr/bin/env python2

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from base import *

# Aún mejor: decorador de clases.

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

# Inspired from: https://stackoverflow.com/a/6307868
def decorate_all_methods(decorator):
    def wrapped(cls):
        for attr_name in cls.__dict__:
            attr = getattr(cls, attr_name)
            if callable(attr):
                # It's a function, decorate it
                setattr(cls, attr_name, decorator(attr))
        return cls
    return wrapped

@decorate_all_methods(log)
class Cyborg(object):

    def __init__(self, name):
        self.name = name
        self.weapon = DeathRay(ammunition=25)
        self.teleporter = TimeMachine()

    def travel(self, destination, year):
        self.teleporter.go(destination, year)
        time.sleep(0.25)  # not instant, but almost

    def attack(self, target):
        self.weapon.vaporize(target)

robot = Cyborg('T-1000')
robot.travel('Los Angeles', 1995)
robot.attack('Sarah Connor')
robot.attack('John Connor')
