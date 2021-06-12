# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 20:56:05 2021

@author: USER
"""

# the purpose of this is to answer  mcq

import src.energy
import src.time
test = src.energy.Energy()
test_time = src.time.Time()
print(test.kinetic(100,100))
print(test_time.days_to_seconds(1))
