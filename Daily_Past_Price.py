# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 08:06:16 2026

@author: Owner
"""

# Description: Since the data provided is only monthly
# so it order to get daily price, linear interpolation
# is used since it is defensible, simple and consistent

# Interpolation for this case mean that it assumed the 
# best neutral guess for any date between 2 observed
# month-end prices is a straight line.