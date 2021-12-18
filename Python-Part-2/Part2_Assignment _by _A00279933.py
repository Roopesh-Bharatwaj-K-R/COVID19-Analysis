
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:55:00 2020

@author: Roopesh Bharatwaj K R
A00279933
PART -2 ASSIGNMENT 
"""
# =============================================================================
# In Part 2 of the Assignment, you must read in the data from the file(s), 
# analyse the data (number of values,
# maximum, minimum, mean, median, mode and standard deviation of one variable)
#  and display the results.
# 
# =============================================================================#
from math import sqrt
#import sys
# LIST
S_No=[]
Observation_date =[]
Province_State =[]
Country_Region =[]
last_update =[]
Confirmed =[]
Death=[]
Recovered =[]
Active=[]
try:
    with open("covid_19_data.csv","r",  encoding=('utf-8')) as datafile, open("Results.txt", "w") as outFile: # FILE OPENING AND DEFINES UNPACKET FOR ENCODING
    
        i = 0  # since the header is string initilized value =0
        for line in datafile: # READING EACH LINE IN DATAFILE
            S_no, ObservationDate,province,country,lastUpdate,confirmed_infect,death_rate,recovered,active_cases= line.split(",",maxsplit=8) # APPEND EACH HEADER AND SPLIT WITH (",")
            #print(S_no)
            try:
                Province_State.append(province) # append string 
                Country_Region.append(country) # append  string
                
            except ValueError:
                print("The value cannot be converted to an integer. skip !!!!")
                continue
            i = i+1 # COUNT THE VALUE PLUS 1
            #if ObservationDate == '11/15/2020':   # TO GET THE UPDATED RECORD OF DATA 
            if i>1:  # IF THE VALUE IS >1 THEN IT START TO READ THE S.NO 
                S_No.append(int(S_no))
                Observation_date.append(ObservationDate)
                last_update.append(lastUpdate)
                Confirmed.append(int(confirmed_infect)) 
                Death.append(int(death_rate))
                Recovered.append(int(recovered))  
                
                Active.append(int(active_cases))       #

    
    #WHILE LOOP TO PRINT THE REPORT 
        Choice1 = "y"
        while Choice1.lower() == "y":
             print() 
             print('-----------------------------------------------------------------------------------')  
             print("WELCOME TO WORLD COVID 2019 DATABASE From JANUARY 2020 TILL 15TH NOVEMBER 2020 !!! ")   
             print('-----------------------------------------------------------------------------------') 
             print()
             print()
             print("1. What is covid-19 ? ")
             print("2. World current data for Covid-19 Cases.")
             print("3. Death of Covid-19 case study. ")
             print("4. Statistical Data of Covid-19.")
             print("5. Top country affected by Covid-19.")
             print()
             print('***********************************************************************************')
             
             Choice = input("ENTER YOUR CHOICE (1-5) OR PRESS (0) TO EXIT:") # USER INPUT CHOICE 
             print('----------------------------------------------')
             print()
         # CHECK CONDITION IF THE WORD IS A APLHABET
             if  Choice.isalpha():
                 print("WARNING !!. Please Enter the choice correctly without any alphabet")
                 break
         # IF USER INPUT CHOICE EQUAL TO 0 -->END OF LOOP
             elif Choice == '0':
                print("THANK YOU AND WELCOME BACK AGAIN !!! ")   
                # BREAK THE  LOOP
                break
           
        
             elif Choice == '1':  # IF USER CHOICE IS 1 --> LOOP STARTS  
                 # PRINTING INFORMATION ABOUT COVID 
                 # WHAT IS CORONAVIRUS
                 
                 print("CORONAVIRUS: ")
                 print('-------------')
                 print("Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.Most people infected with  the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.")
                # PREVENSION  
                 print()
                 print("PREVENSION OF COVID: ")
                 print('---------------------')
                 print("The best way to prevent and slow down transmission is to be well informed about the COVID-19 virus, the disease it causes and how it spreads. Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face") 
                 print()
                 print('CAUSES !!')
                 print('---------')
                 print("The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important that you also practice respiratory etiquette (for example, by coughing into a flexed elbow).")
                 print()
                 print("Referenced and For more information please visit: https://www.who.int/health-topics/coronavirus#tab=tab_1")
                 print('=========================================================================================================')
                 
                 #PRINTING FUNCTION, ADDITIONAL WORK
                 outFile.write("\n")
                 outFile.write("\n")
                 outFile.write('-----------------------------------------------------------------------------------\n')  
                 outFile.write("WELCOME TO WORLD COVID 2019 DATABASE From JANUARY 2020 TILL 15TH NOVEMBER 2020 !!! \n")   
                 outFile.write('-----------------------------------------------------------------------------------\n') 
                 outFile.write("\n")
                 outFile.write("\n")
                 outFile.write(" What is covid-19 ? \n")
                 outFile.write("\n")
                 outFile.write(" CORONAVIRUS:\n")
                 outFile.write("-------------\n")
                 outFile.write("Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.Most people infected with  the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.\n")
                 outFile.write("\n")
                 outFile.write("PREVENSION OF COVID: \n")
                 outFile.write("---------------------\n")
                 outFile.write("The best way to prevent and slow down transmission is to be well informed about the COVID-19 virus, the disease it causes and how it spreads. Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face\n")
                 outFile.write("\n")
                 outFile.write("CAUSES !!\n")
                 outFile.write("---------\n")
                 outFile.write("The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important that you also practice respiratory etiquette (for example, by coughing into a flexed elbow).\n")
                 outFile.write("\n")
                 outFile.write("Referenced from WHO and For more information please visit: https://www.who.int/health-topics/coronavirus#tab=tab_1\n")
                 outFile.write("=======================================================================================================================================================================================================================\n")
                 
                 #break
                
                     
             elif Choice == '2':  # IF USER CHOICE IS 2 --> LOOP STARTS  
             
                # CALCULATION OF TOTAL DEATH, ACTIVE, RECOVERED, CONFIRMED CASES OF COVID
            
                    print(" COVID 2019 DATASET DEATILS"     )
                    print('--------------------------------')
                    print(" Total length of dead cases records in covid-19 dataset is :",len(Death))
                    
                    outFile.write(" COVID 2019 DATASET DEATILS\n")
                    outFile.write("----------------------------\n")
                    outFile.write(f"Total length of dead cases records in covid-19 dataset is : {len(Death)}\n")
                       
             elif Choice == '3': 
                 # IF USER CHOICE IS 3 --> LOOP STARTS  
             
             # CALCULATION OF MEAN , MINIMUM AND MAXAMIUM , PECRCENTAGE OF DEATH, ACTIVE, RECOVERED, CONFIRMED CASES OF COVID
                 print()
                 print("STUDY OF COVID-19, DEATH CASES OF COVID-19- AS ON 15TH NOVEMBER, 2020. WORLD WIDE ")
                 print('-----------------------------------------------------------------------------------')
                 print("MEAN :")
                 print('-------')#DEATH MEAN
                 print("The Average number of people died from covid-19 is : ", round(sum(Death)/len(Death))) 
                 print()
                 print("MINIMUM AND MAXAMIUM : ")
                 print('-------------------------')# MAX AND MIN OF DEATH VARIABLE
                 print("Maxamium death of covid cases recorded on a day is: ", max(Death))
                 print ("Least Recorded Death of Covid-19 on a day is :", min(Death))
                 print()
                 print("PERCENTAGE :") #Additional
                 print('-------------')
                 print("Percentage of covid-19 death is:", round(((sum(Death)/sum(Confirmed))*100),2),'%') #sum of death by the sum of confirmed times 100
                 # PRINTING THE RESULTS
                 outFile.write(" STUDY OF COVID-19, DEATH CASES OF COVID-19- AS ON 15TH NOVEMBER, 2020. WORLD WIDE \n")
                 outFile.write("-----------------------------------------------------------------------------------\n")
                 outFile.write(" MEAN\n")
                 outFile.write("------\n")
                 outFile.write(f"The Average number of people died from covid-19 is : {round(sum(Death)/len(Death))}\n")
                 outFile.write("\n")
                 outFile.write(" MINIMUM AND MAXAMIUM : \n")
                 outFile.write('-----------------------\n')# MAX AND MIN OF DEATH VARIABLE
                 outFile.write(f"Maxamium death of covid cases recorded on a day is: {max(Death)}\n")
                 outFile.write(f"Least Recorded Death of Covid-19 on a day is :{min(Death)}\n")
                 outFile.write("\n")
                 outFile.write("PERCENTAGE :\n") #Additional
                 outFile.write('-------------\n')
                 outFile.write(f"Percentage of covid-19 death is: {round(((sum(Death)/sum(Confirmed))*100),2)},'%'\n")
                 outFile.write("\n")
                 
                
                 
                 
                 
                 
                  
                
                 #    
             elif Choice == '4':
                 # IF USER CHOICE IS 4 --> LOOP STARTS  
             
             
                 # MODE , MEDIAN , RANGE AND STANDARD DEVIATION OF COVID DEATH
                 print()
                 print("STASTS OF COVID- 19 DEATH CASES")
                 print('-------------------------------')
                 # MODE 
                 print("DEATH CASES")
                 print('-----------')
                 
                  # STANDARD DEVIATION 
                 Death_mean = sum(Death)/len(Death) # sum of death to the length of death
                 sqr_deviation = [pow (x-Death_mean,2)for x in Death] # this is the squared deviation
                 standard_deviation = sum(sqr_deviation)/ (len(Death)-1)
                 print("The standard deviation of Death cases from covid-19 : ",round(standard_deviation, 2))
                 # MEDIAN
                 mid_index = int(len(Death)/2)
                 if len(Death) % 2 == 1: 
                        median = Death[mid_index]
                 else:
                        median = sum(Death[mid_index-1 : mid_index+1])/2
        
                 print("The Median of people Death from covid 19 :: ", round(median))
                 # RANGE        
                
                 print("The range of Death Cases as on date is : ", max(Death) - min(Death))
            
                 #mode finding the most frequent 
                 values = sorted(list(set(Death))) #sorting 
                 frequencies = [Death.count(value) for value in values]
                 mode_value = frequencies.index(max(frequencies)) #finding the maxamium repeted number_index
                 print("The Mode of death cases :", values[mode_value]) 
                 # prining the report
                 outFile.write("\n")
                 outFile.write(" STASTS OF COVID- 19 DEATH CASES  \n")
                 outFile.write("----------------------------------\n")
                 outFile.write(" DEATH CASES\n")
                 outFile.write("-------------\n")
                 outFile.write(f"he standard deviation of Death cases from covid-19 : {round(standard_deviation, 2)}\n")
                 outFile.write("\n")
                 outFile.write(f"\The Median of people Death from covid 19 :: {round(median)}\n")
                 outFile.write("\n")
                 outFile.write(f"The range of Death Cases as on date is : { max(Death) - min(Death)}\n")
                 outFile.write("\n")
                 outFile.write(f"The Mode of death cases :{ values[mode_value]}\n") #Additional
                 outFile.write("\n")
                 
                 
                 
                 
                 
                 
                 
                 
                 
                
             elif Choice == '5':  
                 for line in Country_Region :
                     
                     print('Top Death cases recorded on a country name on a single day as on 15, November 2020.' )
                     print("Death", "\t"  "Country" ,"\t", "State" )
                     print(max(Death),"\t" ,'India', '\t', 'Maharashtra')
                     # printing for the report 
                     outFile.write("\n")
                     outFile.write(" Top Death cases recorded on a country name on a single day as on 15, November 2020.\n")
                     outFile.write("------------------------------------------------------------------------------------\n")
                     outFile.write( "Death\tCountry\tState\n" )
                     outFile.write(f"{max(Death)}\tIndia\tMaharashtra\n")
                     outFile.write("\n")
                    
                     
                     
                     
                     
                     break        
             Choice1 = input("Do you wan to continue (y/n)?:")
             if Choice1 == 'n': # lower or upper case and for printing report message
                  print("WISH TO SEE YOU BACK WITH UPDATED INFORMATION ON DECEMBER 13,2020., Bye..Bye, THANK YOU !!!")
                  print("YOUR REPORT HAS BEEN DOWNLOADED as RESULTS.TXT, please look at the application file PATH")
             elif Choice1 == 'N':
                    print("WISH TO SEE YOU BACK WITH UPDATED INFORMATION ON DECEMBER 13,2020., Bye..Bye, THANK YOU  !!!")
                    print("YOUR REPORT HAS BEEN DOWNLOADED as RESULTS.TXT, please look at the application file PATH")
             
             elif Choice1 == 'Y':
                     print("BACK TO MAIN MENU")
             elif Choice1 == 'y':
                     print("BACK TO MAIN MENU")
             elif Choice1.isdigit():#when choice is a digit
                 print("Sorry for this !! You have Entered a Digit ") # print error message
             elif Choice1.isalnum(): # when alphabet + number
                 print("Sorry for this !!! You have Entered a Alphabet + Number ")
                 
except FileNotFoundError as fnf_error: # file not found message
    print("The file you're trying to open cannot be found !!!",fnf_error)
except ValueError as value_error: #value error message
    print("The value is incorrect !!! ",value_error)
except ZeroDivisionError as division_by_zero: # division by zero error message
    print("ZERO DIVISION ERROR !!!")
     
#####END OF PROGRAM #####