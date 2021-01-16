# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:21:03 2020

@author:  Roopesh bharatwaj K R
STUDENT ID- A00279933
"""


import numpy as np
#import matplotlib.pyplot as plt

def corr_calc (value , value1):
    """
    

    Calculate and return the correlation of a list of numbers
    This version uses NumPy
    
    numbers - an ndarray of numbers
    
    Returns the Correlationof the numbers

    """
    try:
        corr =np.corrcoef(value, value1)
        
    
    except(ZeroDivisionError, TypeError):
        print("Calculation cannot be done - correlation")
    return corr
def median_calc(value):
    """
    

    Calculate and return the median (middle value) of a list of numbers
    This version uses NumPy
    
    numbers - an ndarray of numbers
    
    Returns the median of the numbers
    """
    try:
        median = np.median(value)
    except(ZeroDivisionError, TypeError):
        print("cannot be calculated -median")
    return median
def range_calc(value):
    """
    Calculate and return the Range (Max-Min) of a list of numbers
    This version uses NumPy
    
    numbers - an ndarray of numbers
    
    Returns the Range of the numbers

    """
    try:
        Range= np.max(value)- np.min(value)
    except(ZeroDivisionError, TypeError):
        print("cannot be calculated-RANGE")    
    return Range

def calc_mode(value):
    """
    Calculate and return the mode (most frequent value) of a list of numbers
    This version uses NumPy
    
    numbers - an ndarray of numbers
    
    Returns the mode of the numbers
    """    
    try:
    # use np.unique to count the frequencies of each number
        values,frequencies = np.unique(value, return_counts=True)
    # return the value corresponding to the index wity the highest frequency
    except(ZeroDivisionError, TypeError):
        print("cannot be calculated-MODE")
    return values[np.argmax(frequencies)]


def var_calc(value):
    """
    Calculate and return the varience of a list of numbers
    This version uses NumPy
    
    numbers - an ndarray of numbers
    
    Returns the  varience of the numbers

    """
    try:
        var = np.var(value)
    except(ZeroDivisionError, TypeError):
            print("cannot be calculated-VAR")
    return var
def covar_calc(value, value1):
    """
    

    Calculate and return the covarience of a list of numbers
    This version uses NumPy
    
    numbers - an ndarray of numbers
    
    Returns the Covarience of the numbers

    """
    try:
        covar =np.cov(value, value1)
    except(ZeroDivisionError, TypeError):
        print("Calculation cannot be done - Covarience")
    return covar
def std_dev(value):
    """
    Calculate and return the Standard Deviation of a list of numbers
    This version uses NumPy
    
    numbers - an ndarray of numbers
    
    Returns the Std_dev of the numbers

    """
    try:
        std_dev =np.std(value)
    except(ZeroDivisionError, TypeError):
        print("cannot be calculated-SD")  
    return std_dev
 
def Linear_Regression(value, value1 ):
    """
    Calculate and return the Linear regressionof a list of numbers
    This version uses NumPy
    
    numbers - an ndarray of numbers
    
    Returns the inner_funct of the x
    """
    
    def inner_funct(x):
        """
        Calculate the inner_funct
    This version uses NumPy
    
    numbers - an ndarray of numbers
    
    Returns the formula slope*x+b
        """
        return slope*x+bias
    slope = (len(value) * np.sum(value*value1) - np.sum(value) * np.sum(value1)) / (len(value)*np.sum(value*value) - np.sum(value) ** 2)
    bias = (np.sum(value1) - slope *np.sum(value)) / len(value)
    
    return inner_funct

 #Additional Analysis##
 #https://medium.com/we-are-orb/linear-regression-in-python-without-scikit-learn-50aef4b8d122

# def calc_percentage(value, value1):
#     percentage = round(((sum(value/value1))*100),2)
#     return  percentage
    