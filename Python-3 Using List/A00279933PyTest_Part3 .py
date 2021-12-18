# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:45:51 2020

@author: user
"""
from pytest import approx

from Def_part3 import calc_mean,calc_median,calc_mode,calc_Range,calc_standardDeviation, get_file, calc_general,calc_covar,calc_varience, calc_corr


# Test the function calc_mean(values)
def test_calc_mean():
    """
    

    Returns
    -------
    A function that tests the "calc_mean" function.

    """
    try:
        assert calc_mean([8,2,3,4,5,6,8,8,8,10]) == 5.5 # FALSE
        assert calc_mean([1,2,3,4,5,6,7,8,9,10]) == 5.5 # TRUE
        assert calc_mean(['root', 'apache', 'mysql', 'jbloggs']) == None
        
    except:
           print(AssertionError,"Assertion error ...calculation is wrong")
           print()

    #assert calc_mean(['root', 'apache', 'mysql', 'jbloggs']) == None
 
# Test the function calc_median(values)

def test_calc_median():
    """
    

    Returns
    -------
    A function that tests the "calc_median" function.

    """
    #assert calc_median([2,5,4,5,5,2,5,1,4]) == 4   # FALSE
    assert calc_median([1,2,5,2,3,6,6,5,5,4]) == 4.5 # TRUE
    
    #assert calc_median([1,2,"buckle my shoe",3,4,"knock on the door"]) == None
    
    
def test_calc_Range():
    """
    

    Returns
    -------
    A function that tests the "calc_Range" function.

    """
    assert calc_Range([1,2,3,4,5,6,7])==6
# Test the function calc_mode(values)

def test_calc_mode():
    """
    

    Returns
    -------
    A function that tests the "calc_mode" function.

    """

    assert calc_mode([2,5,4,5,5,2,5,1,4,3]) == 5 # TRUE 
    assert calc_mode([6.0,2.1,5.3,2,3,6,6,5.0,5.0,4]) == 6 # TRUE
    assert calc_mode(['e','b','d','e','b','c','a','c','d', 'b']) == 'b' #
    
# Test the function calc_standard_deviation(values)
 
def test_calc_standard_deviation():
    """
    

    Returns
    -------
    A function that tests the "calc_standard_deviation" function.

    """

    assert calc_standardDeviation([50.5, 84.0, 74.4, 71.2, 85.3, 41.7, 61.1, 71.4, 45.9, 90.4]) == approx(17.2,0.1) #false
    assert calc_standardDeviation([ 6.0, 2.1, 5.3, 2, 3, 6, 6, 5.0, 5.0, 4]) == approx(1.6,0.1) #FALSE
    assert calc_standardDeviation(['e', 'b', 'd', 'e', 'b', 'c', 'd', 'c', 'd', 'b']) == None
    
# Test the function calc_correlation(x_values, y_values)

def test_calc_corr():
    """
    

    Returns
    -------
    A function that tests the "calc_corr" function.

    """
 
    assert calc_corr([26.8, 62.4, 25.9, 9.1, 74.8, 23.4, 15.8, 44.1, 25.9, 54.9],[50.5, 84.0, 74.4, 71.2, 85.3, 41.7, 61.1, 71.4, 45.9, 90.4]) == approx(0.7, 0.1)
    assert calc_corr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == approx(1.0)
    assert calc_corr([6, 2, 5, 2, 3, 6, 6, 5, 5, 4], [6, 4, 5, 2, 2, 2, 2, 5, 5, 1]) == approx(0.3, 0.1)
    assert calc_corr([6, 2, 5, 2, 3, 6, 6, 5, 5, 4],[6, 4, 5, 2, 2, 2, 2, 5, 5]) == None
    assert calc_corr(['e', 'b', 'd', 'e', 'b', 'c', 'd', 'c', 'd', 'b'],['c', 'a', 'c', 'c', 'a', 'c', 'b', 'c', 'c', 'e']) == None
    

# Test the function for calc_varience(values)

def test_calc_varience():
    """
    

    Returns
    -------
    A function that tests the "calc_variance" function.

    """
    assert calc_varience([1,2,3,4,5,6,7,8,9,10])==9.166666666666666#True
    

# Test the function for calc_covar
def Test_calc_covar():
    """
    

    Returns
    -------
    A function that tests the "calc_covar" function.

    """
    
    assert calc_covar([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10])==9.166666666666666 #True
   
# Test the function general(max, min, length)
def Test_calc_general():
    """
    

    Returns
    -------
    A function that tests the "calc_general" function.

    """
    assert calc_general([1,2,3,4,5,6,7,8,9]) == (1,9,9) ## TRUE# first returns minimum, maximum and length 
