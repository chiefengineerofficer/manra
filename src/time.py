# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 21:04:38 2021

@author: USER
"""
class Time():

    def __init__(self):
        self.real=True
        
    def days_to_seconds(self, days):
        return days *24*60*60
    def seconds_to_days(self,seconds):
        return seconds/(60*60*24)
        
