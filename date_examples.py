'''
Created on Dec 4, 2019

@author: jdeep
'''

import datetime


"""
datetime is a module
In the datetime module there are following classes
datetime
time
date
Each class(datetime,time,date) has both instance and class methods
As we know class methods are used to return objects(otherwise class methods are used as constructors)
"""

# Print the current date time

# class methods that returns date object
print(datetime.datetime.today())
print(datetime.datetime.now())
obj = datetime.datetime.now()
print(obj)
print(obj.strftime("%Y_%m_%d_%H_%M_%S"))



