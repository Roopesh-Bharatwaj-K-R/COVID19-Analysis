# -*- coding: utf-8 -*-
"""
Created on Thu Dec 1 16:39:17 2020

@author: Roopesh Bharatwaj K R
A00279933

"""

#import pyttsx3  #### pip install pyttsx3 first, which is for the speaker function for interactive menu
from Def_part3 import calc_mean,calc_median,calc_mode,calc_Range,calc_standardDeviation, get_file, calc_general,calc_varience, calc_covar, calc_corr, pie_chart, scatter_plot,violin_plot, box_plot



#import sys
# LIST
file ="covid_19_data.csv"
#file = input("Input the name of the file: ")
Confirmed, Death, province = get_file(file)
# DEATH VARIABLE 
#print(len(Death))
try:
    death_mean = calc_mean(Death) #mean
    death_mode =calc_mode(Death)
except:
        print('error')
 #mode
death_minumum, death_maxamium, death_length = calc_general(Death)
 # min.max,length
death_median =calc_median(Death) # median
death_range= calc_Range(Death) # Range 
death_sd=calc_standardDeviation(Death)# Standard Deviation
death_Corr = calc_corr(Death,Confirmed) # corellation
death_varience = calc_varience(Death) # varience 
death_covar = calc_covar(Death,Confirmed) # covarience
# CONFIRMED VARIABLE 
confirmed_mean =calc_mode(Confirmed)
confirmed_mode =calc_mode(Confirmed) #mode
confirmed_minumum,confirmed_maxamium,confirmed_length  = calc_general(Confirmed)
confirmed_range= calc_Range(Confirmed) # Range 
confirmed_median =calc_median(Confirmed) # median
confirmed_sd=calc_standardDeviation(Confirmed)# Standard Deviation
#confirmed_Corr = calc_corr(Death,Confirmed) # corellation
confirmed_varience = calc_varience(Confirmed) # varience 
confirmed_covar = calc_covar(Death,Confirmed) ## covarience
##
# country_region_bydeath_minumum,country_region_bydeath_maxamium,country_region_bydeath_length =calc_general(country_region_bydeath)


with open("resultS.txt", "w") as outFile:# 
 
    # speaker =pyttsx3.init()
    # speaker.say("WELCOME TO WORLD COVID 2019 DATABASE From JANUARY 2020 TILL 15TH NOVEMBER 2020 !!! ")
    # speaker.runAndWait()
    # print()
  
#WHILE LOOP TO PRINT THE REPORT 
    Choice1 = "y"
    while Choice1.lower() == "y":
             
            # speaker.runAndWait()
              print() 
              print('-----------------------------------------------------------------------------------')  
              print("WELCOME TO WORLD COVID 2019 DATABASE From JANUARY 2020 TILL 15TH NOVEMBER 2020 !!! ")   
              print('-----------------------------------------------------------------------------------') 
              print()
              print()
              print("1. What is covid-19 ? ")
              print("2. World current data for Covid-19 Cases.")
              print("3. Death and confirmed cases  of Covid-19 case study with virtualization. ")
              print("4. Statistical Data of Covid-19.")
         
              print()
              print('***********************************************************************************')
             
              Choice = input("ENTER YOUR CHOICE (1-4) OR PRESS (0) TO EXIT:") # USER INPUT CHOICE 
              print('----------------------------------------------')
              print()
          #CHECK CONDITION IF THE WORD IS A APLHABET
              if  Choice.isalpha():
                #speaker.say("WARNING !!. Please Enter the choice correctly without any alphabet") 
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
                 
                  # PRINTING FUNCTION, ADDITIONAL WORK
                  outFile.write("\n\n-----------------------------------------------------------------------------------\nWELCOME TO WORLD COVID 2019 DATABASE From JANUARY 2020 TILL 15TH NOVEMBER 2020 !!! \n-----------------------------------------------------------------------------------\n\n\n")
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
                      print(" Total length of DEAD CASES records in covid-19 dataset is :",death_length)
                      print(" Total length of CONFIRMED CASES  records in covid-19 dataset is:", confirmed_length) 
                      outFile.write(" COVID 2019 DATASET DEATILS\n")
                      outFile.write("----------------------------\n")
                      outFile.write(f"Total length of DEAD CASES records in covid-19 dataset is : {death_length}\n")
                      outFile.write(f"Total length of CONFIRMED CASES records in covid-19 dataset is : {death_length}\n")
                       
              elif Choice == '3': 
                  # IF USER CHOICE IS 3 --> LOOP STARTS  
             
              # CALCULATION OF MEAN , MINIMUM AND MAXAMIUM , PECRCENTAGE OF DEATH, ACTIVE, RECOVERED, CONFIRMED CASES OF COVID
                  print()
                  print("STUDY OF COVID-19, DEATH and CONFIRMED CASES OF COVID-19- AS ON 15TH NOVEMBER, 2020. WORLD WIDE ")
                  print('------------------------------------------------------------------------------------------------')
                  print("MEAN :")
                  print('-------')#DEATH MEAN
                  print("The Average number of people died from covid-19 is : ", death_mean ) 
                  print("The Average number of people confirmed from covid-19 is : ", confirmed_mean ) 
                  print()
                  print("MINIMUM AND MAXAMIUM : ")
                  print('-------------------------')# MAX AND MIN OF DEATH VARIABLE
                  print("Maxamium death of covid cases recorded on a day is: ",death_maxamium )
                  print ("Least Recorded Death of Covid-19 on a day is :",death_minumum )
                  print("Maxamium confirmed  of covid cases recorded on a day is: ",confirmed_maxamium )
                  print ("Least Recorded confirmed cases  of Covid-19 on a day is :",confirmed_minumum )
                 
                  print()
                  print("PERCENTAGE :") 
                  print('-------------')
                  print("Percentage of covid-19 death is:", round(((sum(Death)/sum(Confirmed))*100),2),'%') #sum of death by the sum of confirmed times 100
                  pie_chart(Death, province)
                  box_plot(Death)
                  box_plot(Confirmed)
                  scatter_plot(Death, Confirmed)
                  violin_plot(Death)
                  # pie_chart(country_region_bydeath)
                 
                 
                  # PRINTING THE RESULTS
                  outFile.write(" STUDY OF COVID-19, DEATH and CONFIRMED CASES OF COVID-19- AS ON 15TH NOVEMBER, 2020. WORLD WIDE \n")
                  outFile.write("-------------------------------------------------------------------------------------------------\n")
                  outFile.write(" MEAN\n")
                  outFile.write("------\n")
                  outFile.write(f"The Average number of people died from covid-19 is : {death_mean}\n")
                  outFile.write(f"The Average number of confirmed cases from covid-19 is : {confirmed_mean}\n")
                  outFile.write("\n")
                  outFile.write(" MINIMUM AND MAXAMIUM : \n")
                  outFile.write('-----------------------\n')# MAX AND MIN OF DEATH VARIABLE
                  outFile.write(f"Maxamium death of covid cases recorded on a day is: {death_maxamium }\n")
                  outFile.write(f"Least Recorded Death of Covid-19 on a day is :{death_minumum}\n")
                  outFile.write(f"Maxamium confirmed casesf covid cases recorded on a day is: {confirmed_maxamium}\n")
                  outFile.write(f"Least Recorded confirmed cases of Covid-19 on a day is :{confirmed_minumum}\n")
                  outFile.write("\n")
                  outFile.write("PERCENTAGE :\n")
                  outFile.write('-------------\n')
                  outFile.write(f"Percentage of covid-19 death is: {round(((sum(Death)/sum(Confirmed))*100),2)},'%'\n")
                  outFile.write("\n")
                  # outFile.write(pie_chart(country_region_bydeath))#    
                  
              elif Choice == '4':
                  # IF USER CHOICE IS 4 --> LOOP STARTS  
             
             
                  # MODE , MEDIAN , RANGE AND STANDARD DEVIATION OF COVID DEATH
                  print()
                  print("STASTS OF COVID- 19 DEATH CASES AND CONFIRMED CASES")
                  print('---------------------------------------------------')
                  # MODE 
                  print("DEATH CASES")
                  print('-----------')
                 
                  # STANDARD DEVIATION 
                 
                  print("The standard deviation of Death cases from covid-19 : ",round(death_sd, 2))
                  print("The standard deviation of confirmed cases from covid-19 : ",round(confirmed_sd, 2))
                  # MEDIAN
            
                  print("The Median of people Death from covid 19 :: ", round(death_median))
                  print("The Median of people confirmed from covid 19 :: ", round(confirmed_median))
                  # RANGE        
                  print("The range of Death Cases as on date is : ",  death_maxamium-death_minumum )
                  print("The range of confirmed Cases as on date is : ",  confirmed_maxamium-confirmed_minumum )
                 
                  # CORR # ADDITIONAL
                  print("The CORR of Death Cases AND Confirmed  cases as on date is : ",  death_Corr )
                 
                 
                  # VARIENCE #ADDITIONAL
                  print("The varience of Death Cases as on date is : ",  death_varience )
                  print("The varience  of confirmed Cases as on date is : ",  confirmed_varience )
                 
                  # COVARIENCE #ADDITIONAL
                  print("The covarience of Death and Confirmed Cases as on date is : ", death_covar )
                 
                 
                  # prining the report

                  outFile.write("\n")
                  outFile.write(" STASTS OF COVID- 19 DEATH CASES  \n")
                  outFile.write("----------------------------------\n")
                  outFile.write(" DEATH AND CONFIRMED CASES\n")
                  outFile.write("--------------------------\n")
                  outFile.write(f"he standard deviation of Death cases from covid-19 : {round(death_sd, 2)}\n")
                  outFile.write("\n")
                  outFile.write(f"he standard deviation of confirmed cases from covid-19 : {round(confirmed_sd, 2)}\n")
                  outFile.write("\n")
                  outFile.write(f"\The Median of people Death from covid 19 :: {round(death_median)}\n")
                  outFile.write("\n")
                  outFile.write(f"\The Median of people confirmed cases from covid 19 :: {confirmed_median}\n")
                  outFile.write("\n")
                  outFile.write(f"The range of Death Cases as on date is : { death_maxamium-death_minumum}\n")
                  outFile.write("\n")
                  outFile.write(f"The range of confirmed cases as on date is : { confirmed_maxamium-confirmed_minumum}\n")
                  outFile.write("\n")
                  outFile.write(f"The Mode of death cases :{ death_mode}\n") 
                  outFile.write("\n")
                  outFile.write(f"The Mode of confirmed  :{confirmed_mode}\n") 
                  outFile.write("\n")
                  outFile.write(f"The corellation of death cases and confirmed cases :{ death_Corr}\n") 
                  outFile.write("\n")
                  outFile.write(f"The varience of Death Cases as on date is :{death_varience}\n") 
                  outFile.write("\n")
                  outFile.write(f"The varience  of confirmed Cases as on date is :{confirmed_varience}\n")
                  outFile.write("\n")
                  outFile.write(f"The covarience of Death and Confirmed Cases as on date is :{ death_covar }\n") 
                
    
                
             
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

#####END OF PROGRAM #####