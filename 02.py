#! /usr/bin/env python2

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from base import *  # stubs so that the code below works


# Algo mejor: con logging()

import time
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

class Cyborg(object):

    def __init__(self, name):
        logging.info("Creating new Cyborg (name=%s)", name)
        self.name = name
        self.weapon = DeathRay(ammunition=25)
        self.teleporter = TimeMachine()

    def travel(self, destination, year):
        logging.info("Travelling to %s and year %s", destination, year)
        self.teleporter.go(destination, year)
        time.sleep(0.25)  # not instant, but almost

    def attack(self, target):
        logging.info("Attacking %s", target)
        self.weapon.vaporize(target)

robot = Cyborg('T-1000')
robot.travel('Los Angeles', 1995)
robot.attack('Sarah Connor')
robot.attack('John Connor')
