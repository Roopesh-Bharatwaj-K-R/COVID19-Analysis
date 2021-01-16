

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 18:30:23 2020

@author: Roopesh Bharatwaj K R
STUDENT ID- A00279933
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from Final_Assignment_Numpy import Linear_Regression,corr_calc,var_calc,std_dev,covar_calc,median_calc,range_calc,calc_mode#,calc_percentage
#from Final_Assignment_Pandas import corr_calc,var_calc,std_dev,covar_calc,median_calc,range_calc
from time import perf_counter
# reading the dataset by PANDAS

df = pd.read_csv("covid_19_data.csv")# PANDAS READING
tips =pd.read_csv("covid_19_data.csv") # SEABORN READING
death = df["Deaths"]
confirmed = df["Confirmed"]
recovered=df["Recovered"]
active =df["Active"]
country =df["Country/Region"]

# Reading the dataset by NUMPY

data = np.loadtxt('covid_19_data.csv', delimiter=',',skiprows=1, usecols=(5,6,7,8))

# assign the columns to the variables
Deaths, Confirmed, Recovered, Active = data.T

# from NUMPY FOR ACTIVE CASES IN DATASET

active_sd=std_dev(Active)
active_median =median_calc(Active)
active_Range=range_calc(Active)
active_mode=calc_mode(Active)
active_corr=corr_calc(Active, Recovered)
active_var=var_calc(Active)
active_covar=covar_calc(Active, Recovered) 
#active_percent=calc_percentage(Active,Recovered)

#FROM NUMPY FOR RECOVERED CASES FROM THE DATASET

recovered_median =median_calc(Recovered)
recovered_Range=range_calc(Recovered)
recovered_mode=calc_mode(Recovered)
recovered_sd=std_dev(Recovered)
recovered_corr=corr_calc(Recovered, Active)
recovered_var=var_calc(Recovered)
recovered_covar=covar_calc(Recovered, Active)
#recovered_percent=calc_percentage(Recovered,Active)
predict= Linear_Regression(Recovered, Active) # LINEAR REGRESSION
predict1= Linear_Regression(Confirmed, Deaths) # LINEAR REGRESSION

df.groupby 

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
              print("3. Study of Covid-19 cases with virtualization. ")
              print("4. Statistical Data of Covid-19.")
              print("5. Advanced Statistical calculation of Covi-19 Data with Virtualization")
              print("6. Top 10 Affectecd countries with Virtualization")
         
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
                 
                  # #break
                
                     
              elif Choice == '2':  # IF USER CHOICE IS 2 --> LOOP STARTS  
             
                  # CALCULATION OF TOTAL DEATH, ACTIVE, RECOVERED, CONFIRMED CASES OF COVID
                  
                      print(" COVID 2019 DATASET DEATILS"     )
                      print('--------------------------------')
                      # Display the size of the DataFrame
                      print("Number of values in dataset:", df.size)
                      print("Number of records in dataset :", len(df))
                      print("Total length of DEAD CASES records in covid-19 dataset is :",len(df.Deaths))
                      print("Total length of CONFIRMED CASES  records in covid-19 dataset is:", len(df.Confirmed)) 
                      print("Total Length of the Recovered Cases of Covid-19 Dataset is :", len(Recovered))
                      print("Total Length of the Active Cases of Covid-19 Dataset is :", len(Active),'\n')
                      print("Description of the  entire dataset:",'\n', df.describe())
                      # 
                      outFile.write(" COVID 2019 DATASET DEATILS\n")
                      outFile.write("----------------------------\n")
                      outFile.write(f"Total length of DEAD CASES records in covid-19 dataset is : {len(df.Deaths)}\nTotal length of CONFIRMED CASES  records in  covid-19 dataset is: {len(df.Confirmed)}\nTotal Length of the Recovered Cases of Covid-19 Dataset is :{ len(Recovered)}\nTotal Length of the Active Cases of Covid-19 Dataset is :{ len(Active)}\n Description of the  entire dataset:\n{ df.describe()}")
                      
                      
                               
              elif Choice == '3': 
                  # IF USER CHOICE IS 3 --> LOOP STARTS  
                  # CALCULATION OF MEAN , MINIMUM AND MAXAMIUM , PECRCENTAGE OF DEATH, ACTIVE, RECOVERED, CONFIRMED CASES OF COVID
                  print()
                  print("STUDY OF COVID-19, DEATH and CONFIRMED CASES OF COVID-19- AS ON 15TH NOVEMBER, 2020. WORLD WIDE ")
                  print('------------------------------------------------------------------------------------------------')
                  print("MEAN :")
                  print('-------')#DEATH MEAN
                  print("The Average number of people died from covid-19 is : ", death.mean() ) 
                  print("The Average number of people confirmed from covid-19 is : ", confirmed.mean()) 
                  print("The Average number of people Recovered from covid-19 is : ", Recovered.mean())
                  print("The Average number of people Active from covid-19 is : ", Active.mean())
                  print()
                  print("MINIMUM AND MAXAMIUM : ")
                  print('-------------------------')# MAX AND MIN OF DEATH VARIABLE
                  print("Maxamium death of covid cases recorded on a day is: ", death.max()) 
                  print ("Least Recorded Death of Covid-19 on a day is :", df.Deaths.idxmin() )
                  print("Maxamium confirmed  of covid cases recorded on a day is: ",df.Confirmed.idxmax())
                  print ("Least Recorded confirmed cases  of Covid-19 on a day is :",df.Confirmed.idxmin())
                  
                  print("Maxamium Recovered of covid cases recorded on a day is: ", Recovered.max()) 
                  print ("Least Recorded Recovered of Covid-19 on a day is :", Recovered.min())
                  print("Maxamium Active of covid cases recorded on a day is: ",Active.max())
                  print ("Least Recorded Active cases  of Covid-19 on a day is :",Active.min())
                  
                  
                  
                  print()
                  print("PERCENTAGE :") 
                  print('-------------')
                  print("Percentage of covid-19 death is:", round(((sum(df.Deaths)/sum(df.Confirmed))*100),2),'%') #sum of death by the sum of confirmed times 100
                  # pie_chart(Death, province)
                  # box_plot(Death)
                  # box_plot(Confirmed)
                  fig, axs = plt.subplots (figsize = (10,10))
                  axs.set_title("Deaths")
                  # Sets the title of the Pie chart
                  # creates the pie chart using regions_data values as the variable and its keys as the labels keys
                  axs.pie(df.Deaths[0:1000], labels = df.Deaths[0:1000])
                  
                  
                  
                  # matplot lib SCATTER PLOT
                  df.plot.scatter("Deaths","Confirmed", title ="Death Case and Confirmed case") # scatter plot of magnitudes v number of stations
                  df.plot(use_index=False, subplots=True, title ="Cases" ) # line plot of numeric values
                  # violin_plot(Death)
                  # pie_chart(country_region_bydeath)
                  # Create the figure and axes
                  # SUBPLOT FOR THE ACTIVE AND RECOVERED CASES FROM NUMPY
                  fig, ax = plt.subplots()
                    # Set the title
                  ax.set_title("Recovered and Active")
                    # set the axis labels
                  ax.set_xlabel("Recovered")
                  ax.set_ylabel("Active")
                    # plot the values
                  ax.plot(data.T[0], data.T[1])
                    # show the plot
                  plt.show()
                  
                  # SEABORN BOX PLOT
                  sns.boxplot(x ='Confirmed', y ='Deaths', data = tips)
                  plt.title("Box Plot for Confirmed and Deaths")
                  plt.show()
                  # seaborn 

                  
                   # PRINTING THE RESULTS
                  outFile.write(" STUDY OF COVID-19, DEATH and CONFIRMED CASES OF COVID-19- AS ON 15TH NOVEMBER, 2020. WORLD WIDE \n")
                  outFile.write("-------------------------------------------------------------------------------------------------\n")
                  outFile.write(" MEAN\n")
                  outFile.write("------\n")
                  outFile.write(f"The Average number of people died from covid-19 is : {death.mean()}\nThe Average number of confirmed cases from covid-19 is : {confirmed.mean()}\n\n MINIMUM AND MAXAMIUM :\n-----------------------\nMaxamium death of covid cases recorded on a day is: {death.max() }\nLeast Recorded Death of Covid-19 on a day is :{ df.Deaths.idxmin()}\nMaxamium confirmed  of covid cases recorded on a day is: {df.Confirmed.idxmax()}\nLeast Recorded confirmed cases  of Covid-19 on a day is :{df.Confirmed.idxmin()}\nPERCENTAGE :\n-------------\nPercentage of covid-19 death is:{round(((sum(df.Deaths)/sum(df.Confirmed))*100),2)}'%'\n")
                     
              elif Choice == '4':
                  
                  print("STASTS OF COVID- 19 DEATH CASES AND CONFIRMED CASES")
                  print('---------------------------------------------------')
                  # MODE 
                  print("DEATH CASES")
                  print('-----------')
                  print("The standard deviation of Death cases from covid-19 : ",round(death.std(), 2))
             
                  # MEDIAN
                  print("The Median of people Death from covid 19 :: ", round(death.median()))
                  # RANGE        
                  print("The range of Death Cases as on date is : ",  (death.max()-death.min()))
                  print("The Mode of Death case as on date:", death.mode())
                   # VARIENCE #ADDITIONAL
                  print("The varience of Death Cases as on date is : ",  death.var())
                  # CORR # ADDITIONAL
                  print("The CORR of Death Cases AND Confirmed  cases as on date is : ",  death.corr(confirmed) )
              
                  print("The covarience of the Confirmed cases as on date is :",'\n', death.cov(confirmed),'\n')
                  
                  print("CONFIRMED CASES")
                  print("---------------")
                  print("The standard deviation of confirmed cases from covid-19 : ",round(confirmed.std(), 2))
                  print("The Median of people confirmed from covid 19 :: ", round(confirmed.median()))
                  print("The range of confirmed Cases as on date is : ",  (confirmed.max()-confirmed.min()))
                  print("The Mode of Confirmed cases as on date:", confirmed.mode())
                  print("The varience  of confirmed Cases as on date is :  ",  confirmed.var())
                  print("The CORR of Death Cases AND Confirmed  cases as on date is : ",  confirmed.corr(death))
                  print("The covarience of the Confirmed cases as on date is :", confirmed.cov(death))
                  # COVARIENCE #ADDITIONAL
                  print("The covarience of Death and Confirmed Cases as on date is : ", death.cov(confirmed),'\n' )
                  print("ACTIVE CASES")
                  print("------------")
                   # STANDARD DEVIATION 
                  print("The standard deviation of Active cases from covid-19 : ",round(active_sd, 2))
                   # MEDIAN
                  print("The Median of people, Active cases  from covid 19 :: ", round(active_median,2))
                   # RANGE        
                  print("The range of  Active Cases as on date is : ",  active_Range )
                  print("The Mode of Active case as on date:", active_mode)
                   # CORR # ADDITIONAL
                  print("The CORR of Recovered Cases AND Active  cases as on date is : ",  active_corr[0,0])
                   # VARIENCE #ADDITIONAL
                  print("The varience of Active  Cases as on date is : ",  active_var)
                   # COVARIENCE #ADDITIONAL
                  print("The covarience of Active and Recovered Cases as on date is : ",active_covar[0,0] ,'\n')
                   #  
                   # RECOVERED CASES IN DATASET USING NUMPY
                  print("RECOVERED CASES")
                  print("---------------")
                  print("The standard deviation of Recovered cases from covid-19 : ",round(recovered_sd, 2))
                   # MEDIAN
                  print("The Median of people,Recovered cases  from covid 19 :: ", round(recovered_median,2))
                   # RANGE        
                  print("The range of Recovered  Cases as on date is : ",  recovered_Range )
                  print("The Mode of Recovered case as on date:", recovered_mode)
                   # CORR # ADDITIONAL
                  print("The CORR of Recovered Cases AND Active  cases as on date is : ",  recovered_corr[0,0])
                   # VARIENCE #ADDITIONAL
                  print("The varience of Recovered  Cases as on date is : ",  recovered_var)
                   # COVARIENCE #ADDITIONAL
                  print("The covarience of Recovered and Active Cases as on date is : ", recovered_covar[0,0])
                 
                  # prining the report
  
                  outFile.write("\n")
                  outFile.write(" STASTS OF COVID- 19 DEATH CASES  \n")
                  outFile.write("----------------------------------\n")
                  outFile.write(" DEATH AND CONFIRMED CASES\n")
                  outFile.write("--------------------------\n")
                  outFile.write(f"The standard deviation of Death cases from covid-19 : {round(death.std(), 2)}\nThe Median of people Death from covid 19 : {round(death.median())}\nThe range of Death Cases as on date is : {(death.max()-death.min())}\nThe Mode of Death case as on date:{death.mode()}\nThe varience of Death Cases as on date is : {death.var()}\nThe CORR of Death Cases AND Confirmed  cases as on date is : {death.corr(confirmed)}\nThe covarience of the Confirmed cases as on date is :\n{death.cov(confirmed)}\nCONFIRMED CASES\n---------------\nThe standard deviation of confirmed cases from covid-19 : {round(confirmed.std(), 2)}\nThe Median of people confirmed from covid 19 :{ round(confirmed.median())}\nThe range of confirmed Cases as on date is :  {confirmed.max()-confirmed.min()}\nThe Mode of Confirmed cases as on date: {confirmed.mode()}\nThe varience  of confirmed Cases as on date is :   {confirmed.var()}\nThe CORR of Death Cases AND Confirmed  cases as on date is :  {confirmed.corr(death)}\nThe covarience of the Confirmed cases as on date is : {confirmed.cov(death)}\nThe covarience of Death and Confirmed Cases as on date is : {death.cov(confirmed)}\nACTIVE CASES\n------------\nThe standard deviation of Active cases from covid-19 : {round(active_sd, 2)}\nThe Median of people, Active cases  from covid 19 :{ round(active_median,2)}\nThe range of  Active Cases as on date is :{active_Range }\nThe Mode of Active case as on date:{ active_mode}\nThe CORR of Recovered Cases AND Active  cases as on date is : {active_corr[0,0]}\nThe varience of Active  Cases as on date is : {active_var}\nThe covarience of Active and Recovered Cases as on date is : {active_covar[0,0] }\nRECOVERED CASES\n---------------\nThe standard deviation of Recovered cases from covid-19 : {round(recovered_sd, 2)}\nThe Median of people,Recovered cases  from covid 19 :{round(recovered_median,2)}\nThe range of Recovered  Cases as on date is : { recovered_Range }\nThe Mode of Recovered case as on date:{ recovered_mode}\nThe CORR of Recovered Cases AND Active  cases as on date is : { recovered_corr[0,0]}\nThe varience of Recovered  Cases as on date is : {recovered_var}\nThe covarience of Recovered and Active Cases as on date is :{ recovered_covar[0,0]}")
                  
              
              elif Choice == '5': # ADDITIONAL ANALYSIS
                
                  print("Additional Analysis on pandas and the Numpy with Virtualization")
                  print("---------------------------------------------------------------",'\n')
                  print("PANDAS")
                  
                  # SKEWNESS # ADDITIONAL ANALYSIS IN PANDAS
                  
                  print("Skewnees of the dataset", '\n', df.skew(axis = 0, skipna = True),'\n')
                  print("Skewness of the Death Column", '\n', death.skew(axis = 0, skipna = True))
                  print("Skewness of the Confirmed Column", '\n', confirmed.skew(axis = 0, skipna = True))
                  
                  # KURIOSIS # ADDITIONAL ANALYSIS IN PANDAS 
                  
                  print( "Kurtosis measure of dataset :",'\n',df.kurtosis(),'\n')
                  print(" Death, Confirmed, Recovere, Active has the heavy Outliers and they are Leptokurtic > 3 ", '\n')
                  
                  # LINEAR REGRESSION ADDITIONAL ANALYSIS IN PANDAS
                  
                  print("Linear Fitment for prediction of the Recovered cases  USING PANDAS: ",'\n')
                  slope=  ((confirmed.cov(recovered))/confirmed.var()) # Dependednt Variable
                  #print("slope", slope)
                  const = ((recovered.mean())-(slope*confirmed.mean())) # Independent Variable
                  #print("const", const)
                  prediction = slope*4 + const # LINEAR FITMENT Y=(M*X+B) 
                  print("Linear Regression for Recovered and Confirmed cases",'\n')
                  start = perf_counter()
                  print("Prediction of Recovered cases when confirmed cases increases 4 times : ",prediction)
                  end = perf_counter()
                  print("Time taken:",end - start, "seconds","For Pandas Linear Regression computation")  
                  #df.plot.scatter("Confirmed", "Recovered", title= "Scatter Plot for Confirmed vs Recovered ")
                  print("From this prediction we can understand that the recovery rate is very less",'\n')
                  
                  
                  # ADDITIONAL ANALYSIS USING NUMPY 
                  
                  print("NUMPY")
                  print("-----",'\n')
                  
                  #  LINEAR REGRESSION -1 Recovered vs Active
                  y= predict(4)
                  print("Linear Regressiion for Recovered and Active ",'\n')
                  start = perf_counter()
                  print("Linear Regression using NumPY for the Recovered and Active cases increased by 4 times ",y)
                  end = perf_counter()
                  print("From this we can understandthat active cases continue to increase")
                  print("Time taken:",end - start, "seconds","For NumPy Linear Regression computation",'\n')  
                  
                  # LINEAR REGRESSION -2 Confirmed vs Death
                  y= predict1(4)
                  print("Linear Regressiion for Confirmed and Death",'\n')
                  start = perf_counter()
                  print("Linear Regression using NumPY for the Confirmed and death cases increased by 4 times ",y)
                  end = perf_counter()
                  print("From this we can understandthat Death cases continue to increase")
                  print("Time taken:",end - start, "seconds","For NumPy Linear Regression computation")  
        
                  # ADDITIONAL ANALYSIS - SEABORN PLOTTING for Confirmed and Recovered 
                  sns.set_style("whitegrid")
                 #tips = sns.load_dataset("covid_19_data")
                  ax = sns.regplot(x="Confirmed", y="Recovered", data= tips)
                  plt.title("Linear Fitment CONFIRMEND AND RECOVERED")
                  plt.show()
                  
                  # ADDITIONAL ANALYSIS- SEABORN PLOT FOR CONFIRMED AND DEATH
                  sns.set_style("whitegrid")
                 #tips = sns.load_dataset("covid_19_data")
                  ax = sns.regplot(x="Confirmed", y="Deaths", data= tips)
                  plt.title("Linear Fitment CONFIRMEND AND DEATHS")
                  plt.show()
                  
                  ###  ADDITIONAL ANALYSIS- SEABORN PLOT FOR RECOVERED AND ACTIVE
                  sns.set_style("whitegrid")
                  ax= sns.regplot(x="Recovered",y="Active", data= tips)
                  plt.title("Recovered vs Active")
                  
                  plt.show()
                  
                  
                  ####outfile###
                  
                  outFile.write(f"Additional Analysis on pandas and the Numpy with Virtualization\n---------------------------------------------------------------\nPANDAS\nSkewnees of the dataset \n{ df.skew(axis = 0, skipna = True)}\nSkewness of the Death Column\n{ death.skew(axis = 0, skipna = True)}\nSkewness of the Confirmed Column\n{confirmed.skew(axis = 0, skipna = True)}\nKurtosis measure of dataset \n{df.kurtosis()}\nDeath, Confirmed, Recovere, Active has the heavy Outliers and they are Leptokurtic > 3 \nLinear Fitment for prediction of the Recovered cases USING PANDAS:\nLinear Regression for Recovered and Confirmed cases\nPrediction of Recovered cases when confirmed cases increases 4 times : {prediction}\nTime taken: {end - start} seconds For Pandas Linear Regression computation\nFrom this prediction we can understand that the recovery rate is very less\nNUMPY\n-----\nLinear Regressiion for Recovered and Active \nLinear Regression using NumPY for the Recovered and Active cases increased by 4 times {y}\nFrom this we can understandthat active cases continue to increase\nTime taken: {end - start} seconds For NumPy Linear Regression computation\nLinear Regressiion for Confirmed and Death\nLinear Regression using NumPY for the Confirmed and death cases increased by 4 times {y}\nFrom this we can understandthat Death cases continue to increase\nTime taken: {end - start} seconds For NumPy Linear Regression computation\n")
                   
                   #####
                 
                  
              elif Choice =='6':
                  # ADDITIONAL ANALYSIS USING PANDAS TO FIND THE ENTIRE LOCATIION OF THE DATA VARIABLE 
                  print("Details abou the death cases with maxamium on a day ",'\n',df.loc[df.Deaths.idxmax()])  # GIVES THE ENTIRE LOCATION
                  print("Details about the Confirmed cases on a day",'\n',df.loc[df.Confirmed.idxmax()])
                  print("Details about the Active cases on a day",'\n',df.loc[df.Active.idxmax()])
                  print("Details about the Recovered cases on a day",'\n',df.loc[df.Recovered.idxmax()],'\n')
                  print("The top 10 of Death cases ")
                  print("------------------------",'\n')
                  print("TOP DEATH",'\n',df.nlargest(10, ['Deaths']))
                 
                  df.plot.hist(df.nlargest(5, ['Deaths',"Confirmed"]))
                  #df.plot.hist(death.max(10))
                  # seaborn
                  sns.violinplot(x= df.Active[0:100], Y= df.Recovered[0:100])
                  plt.title("Violin plot for the Active and Recovered")
                  plt.show()
                  sns.barplot(x= df.Confirmed, y= df.Recovered)
                  plt.title("Bar plot for the Confirmed vs Recovered")
                  plt.show()
                  # matplot # VIOLIN PLOT
                  
                  fig, axs = plt.subplots (figsize = (10,10))
                  axs.set_title("Violin Plot for Death Covid data")
        # set labels
                  axs.violinplot(df.Active[0:20])# for first 20 instances
                  plt.show()
                  
                  
                  
                  
                  outFile.write(f"ADDITIONAL ANALYSIS USING PANDAS TO FIND THE ENTIRE LOCATIION OF THE DATA VARIABLE\nDetails abou the death cases with maxamium on a day \n{df.loc[df.Deaths.idxmax()]}\nDetails about the Confirmed cases on a day\n{df.loc[df.Confirmed.idxmax()]}\nDetails about the Active cases on a day\n{df.loc[df.Active.idxmax()]}\nDetails about the Recovered cases on a day\n{df.loc[df.Recovered.idxmax()]}\nThe top 10 of all cases\n------------------------\nTOP DEATH\n{df.nlargest(10, ['Deaths'])}")
                            
                  
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