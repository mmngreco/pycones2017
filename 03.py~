#! /usr/bin/env python2

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

# Stubs so the code below works
class DeathRay(object):
    def __init__(self, *args, **kwargs): pass
    def vaporize(self, *args, **kwargs): pass
class TimeMachine(object):
    def go(self, *args, **kwargs):
        pass


# Algo mejor: con logging()

import time
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

class Cyborg(object):

    def __init__(self, name):
        logging.info("Creating new Cyborg (name={})".format(name))
        self.name = name
        self.weapon = DeathRay(ammunition=25)
        self.teleporter = TimeMachine()

    def travel(self, destination, year):
        logging.info("Travelling to {} and year {}".format(destination, year))
        self.teleporter.go(destination, year)
        time.sleep(0.25)  # not instant, but almost

    def attack(self, target):
        logging.info("Attacking {}".format(target))
        self.weapon.vaporize(target)

robot = Cyborg('T-1000')
robot.travel(destination='Los Angeles', year=1995)
robot.attack('Sarah Connor')
robot.attack('John Connor')
