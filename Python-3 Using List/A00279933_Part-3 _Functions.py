"""

PART 3 ASSIGNMENT

A00279933- K R ROOPESH BHARATWAJ


"""
#import my_file from part-3assignment.py

from math import sqrt
import matplotlib.pyplot as plt
#import datetime

#import sys
# LIST

def get_file(File_name):
   # S_No=[]
    Observation_date =[]
    Province_State =[]
    Country_Region =[]
   # last_update =[]
    Confirmed =[]
    Death=[]
    # Recovered =[]
    # Active=[]
    country_region_bydeath = {} #Dictionary
   #format_str ="%m/%d/%y"
   
    try:
        with open((File_name),"r",  encoding=('utf-8')) as datafile: # FILE OPENING AND DEFINES UNPACKET FOR ENCODING
            i = 0  # since the header is string initilized value =0
            for line in datafile: # READING EACH LINE IN DATAFILE
                _,ObservationDate,province,country,_,confirmed_infect,death_rate,_,_= line.split(",",maxsplit=8) # APPEND EACH HEADER AND SPLIT WITH (",")
                
                try:
                    Province_State.append(province) # append string 
                    Country_Region.append(country) # append  string
                except ValueError:
                    print("The value cannot be converted to an integer. skip !!!!")
                
                i = i+1 # COUNT THE VALUE PLUS 1
                # if i==1000:
                #     break
                #if ObservationDate == '11/15/2020':   # TO GET THE UPDATED RECORD OF DATA 
                if i>1:  # IF THE VALUE IS >1 THEN IT START TO READ THE S.NO 
                # S_No.append(int(S_no))
                    Observation_date.append(ObservationDate)
                   # last_update.append(lastUpdate)
                    Confirmed.append(int(confirmed_infect)) 
                    Death.append(int(death_rate))
                    # Recovered.append(int(recovered))  
                    # Active.append(int(active_cases)) 
                  
                # if country not in country_region_bydeath:
                #         country_region_bydeath[country]= int(death_rate)
                # else:
                #         country_region_bydeath[country]+= int(death_rate)
                  
    except FileNotFoundError as fnf_error: # file not found message
        print("The file you're trying to open cannot be found !!!",fnf_error)
    except ValueError as value_error: #value error message
        print("The value is incorrect !!! ",value_error)
    except ZeroDivisionError as division_by_zero: # division by zero error message
        print("ZERO DIVISION ERROR !!!", division_by_zero)
        
    return Confirmed, Death, Province_State


def calc_general(values):
    """
    

    Parameters
    ----------
    values : List of numbers in the values

    Returns
    -------
    minimum : of the number
    maxamium : of the numberN.
    length : of the number
    """
    minimum = min(values)
    maxamium= max(values)
    length = len(values)
  
    return minimum, maxamium, length    
       
def calc_median(values: list):
    """
    

    Parameters
    ----------
    values : list of numbers
        to calculate the median of the values in  list

    Returns 
    -------
    median of the number
    """
    try:
        median = mid_index = int(len(values)/2)
        if len(values) % 2 == 1: 
               median = values[mid_index]
        else:
               median = sum(values[mid_index-1 : mid_index+1])/2
               
    except(ZeroDivisionError, TypeError):
        print("cannot be calculated -median")
    return median

def calc_mode(values: list):
    """
    

    Parameters
    ----------
    values : list of number in values
       To calculate the mode of the values in list

    Returns
    -------
    mode of the number
    """
    try:
        key = sorted(list(set(values))) #sorting 
        frequencies = [values.count(value) for value in key]
        mode_value = frequencies.index(max(frequencies)) #finding the maxamium repeted number_index
        mode = key[mode_value]
    except(ZeroDivisionError, TypeError):
        print("cannot be calculated-MODE")
    return mode

def calc_Range(values: list):
    """
    

    Parameters
    ----------
    values : list of numbers in values
       to calculate the range of the values in list
    Returns
    -------
    range of the number

    """
    try:
        Range = max(values)-min(values)
    except(ZeroDivisionError, TypeError):
        print("cannot be calculated-RANGE")    
    return Range 
   
def calc_standardDeviation(values: list):    
    """
    

    Parameters
    ----------
    values : list of numbers in values
    To calculate the standard deviation 

    Returns
    -------
    Standard Deviation
    """
    try:
        Death_mean = sum(values)/len(values) # sum of death to the length of death
        sqr_deviation = [pow (x-Death_mean,2)for x in values] # this is the squared deviation
        standard_deviation = sum(sqr_deviation)/ (len(values)-1) 
        standardDeviation = standard_deviation 
    except(ZeroDivisionError, TypeError):
        print("cannot be calculated-SD")    
    return standardDeviation

def calc_corr(values: list, values1: list)->float: # Additional Analysis 
    """
    Parameters
    ----------
    values : Values, Values1
    To calculate the correlation of values and values 1 

    Returns
    -------
    corellation of the number
    
    
    
    
    """# ADDITIONAL ANALYSIS CORELLATION
  
  
  # the both squared deviation of x and y values, and finally using the sum of x-y deviations 
  # and the sq. root of the y deviations correlation is calculated Below is the 
  # result of the Correlation between the death and the Confirmed case dataset variables. 
    
  
    
  
    
  
    
  
    try:
        mean1 = sum(values)/len(values) # MEAN1
        mean2 = sum(values1)/len(values1) # MEAN
        x_deviations = [ x - mean1 for x in values ] # FIRST OBSERVATION -MEAN1
        y_deviations = [ y - mean2 for y in values1  ] # FIRST OBSERVATION -MEAN2
        xy_deviations = [ x*y for (x,y) in zip(x_deviations,y_deviations)] # using the zip function to combine the two list (x,y deviations) 
        x_sqd_deviations = [ (x - mean1) ** 2 for x in values ]
  # the both squared deviation of x and y values, and finally using the sum of x-y deviations 
  # and the sq. root of the y deviations correlation is calculated Below is the 
  # result of the Correlation between the death and the Confirmed case dataset variables. 
        y_sqd_deviations = [ (y - mean2) ** 2 for y in values1 ]         
        corr = sum(xy_deviations)/(sqrt(sum(x_sqd_deviations))*(sqrt(sum(y_sqd_deviations)))) 
    except(ZeroDivisionError, TypeError):
        print("cannot be calculated-CORR")  
    return corr

def calc_varience(values:list):  # ADDITIONAL ANALYSIS VARIENCE 
    """
    Parameters
    ----------
    values :list of numbers in values
    to calculate the varience 

    Returns
    -------
    varience of the number
       
    """
    # ADDITIONAL ANALYSIS VARIENCE 
    try:
        #var=-1
        mean = sum(values) / len(values) #MEAN
        var = sum((x-mean)**2 for x in values) / (len(values)-1) # FIRST OBSERVATION -MEAN SQUARED OF THE VALUES IN X BY THE TOTOAL LENGTH MINUS 1
        varience=var
       
    except(ZeroDivisionError, TypeError):
            print("cannot be calculated-VAR")
    return varience

  
def calc_covar(values:list, values1:list):
    """
    Parameters
    ----------
    values : List of numbers in value and value 1
    to calculate the covarience 

    Returns
    -------
    covarience of the number
     
    """
    # ADDITIONAL ANALYSIS COVARENCE 
    covar = -2
    # try:
    mean1=sum(values)/len(values) # mEAN CALCULATION
    x_cov=[x-mean1 for x in values] # FIRST OBSERVATION-MEAN 
    mean2=sum(values1)/len(values1) # MEAN OF SECONF VALUE
    y_cov=[y-mean2 for y in values1] # FIRST OBSERVATION -MEAN2
    N= len(values)#+len(values1) # TOTOAL LENGTH OF THE VALUE
    summ=0
    for i in range(len(x_cov)): # LENGTH OF THE A VARIABLE SINCE BOTH VARIABLE HAS SAME LENGTH IN DATASET
        summ = summ + (x_cov[i]*y_cov[i])  # X COV OF  TIMES Y-COV OF 
    covar = summ /(N-1) 
    return covar

def calc_mean(values: list):

    """
    

    Parameters
    ----------
    values : List of numbers
    to calculate mean   

    Returns
    -------
    mean of the number

    """
   
    mean = sum(values)/len(values)
    
    return mean

        
def pie_chart(values: list, title:list):
    """
    

    Parameters
    ----------
    values : a list of numbers
        To Plot the Pie Chart

    Returns
    -------
    TYPE
       Pie Chart of the number

    """
    
    #pie chart
    try: 
            fig, axs = plt.subplots (figsize = (10,10))
            axs.set_title("Deaths")
            # Sets the title of the Pie chart
            # creates the pie chart using regions_data values as the variable and its keys as the labels keys
            axs.pie(values[0:1000], labels = title[0:1000]) # 1000 instances
            
    except:
               print("error in pie chart")
                
    return plt.show()  


def scatter_plot(x_list: list, y_list: list):
    """
    
    Parameters
    ----------
    x_list : Number in the list
        
    y_list :Number in the List 
    
        

    Returns
    -------
    Scatter Plot of the number

    """
    try:
        # SCATTER PLOT # entire dataset
        fig, axs = plt.subplots (figsize = (10,10))
        axs.set_title("Deaths vs Confirmed")
        axs.set_xlabel("Deaths")
        axs.set_ylabel("Confirmed")
        # Plots the scatter plot using the trolleys list as x axis and wards as y axis
        axs.scatter(x_list,y_list,marker = ".")
    except: 
           print("error in scatter plot")
    return plt.show()
    
    
def violin_plot(values:list):
    """

    

    Parameters
    ----------
    values : List of number in values
        Violin PLOT

    Returns
    -------
    vIOLIN plOT of the number

    """
    try:
    
        fig, axs = plt.subplots (figsize = (10,10))
        
        # VIOLIN PLOT
    
        axs.set_title("Violin Plot for Death Covid data")
        # set labels
        axs.violinplot(values[0:20])# for first 20 instances
    except:
        print("Error in Violin Plot")
    return plt.show()  



def box_plot(values: list):
    """
    

    Parameters
    ----------
    values : list
        A list of numbers.

    Returns
    -------
    TYPE
        A box plot of the numbers.

    """
    try:
        # BOX PLOT
        fig,axs=plt.subplots( figsize=(10,10))
        axs.boxplot(values[0:1000]) # for first 1000 instances
        axs.set_title("Box Plot for Death Covid data /n Box Plot for Confirmed Covid data ")
        
    except:
        print("Error in the Box plot ")
    return plt.show()



