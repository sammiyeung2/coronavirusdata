"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
========================================================================================================================
COMPSCI 2120A/9642A/ DIGIHUM 2220A - Assignment 1
Student Name: SAMMI YEUNG
Student Number: 251082261
========================================================================================================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
"""
ITEMS TO COMPLETE...

General:
--> Ensure that the code runs without errors. (done)

Bug Fixes:
--> Fix the "get_daily_increase()" function to return a list containing the daily increase in cases. (done)
--> Fix the "get_cumulative_increase()" function to return a list containing the cumulative increase in cases. (done)

Function calls:
--> Use the appropriate function call to get the Confirmed_Negative-Daily data (in a list) from the 
"Confirmed_Negative-Cumulative" column. You can call the list "confirmed_negative_daily".     (done)
--> Use the appropriate function call to add the "Confirmed_Negative-Daily" column to the covid19_data dataframe.
Label it as "Confirmed_Negative-Daily".    (done)

--> Use the appropriate function call to get the Confirmed_Positive-Cumulative data (in a list) from the 
"Confirmed_Positive-Daily" column. You can call the list "confirmed_positive_cumulative".    (done)
--> Use the appropriate function call to add the "Confirmed_Positive-Cumulative" column to the covid19_data dataframe.
Label it as "Confirmed_Positive-Cumulative".       (done)
--> Use the appropriate function call(s) to find the maximum increase in the "Confirmed_Positive_Daily" column 
(i.e. the highest daily increase in positive cases). Print the value out in a full sentence.   (done)

--> Use the appropriate function call to export the final dataframe to a csv file. The final dataframe should contain
the original data from "covidtesting_cs2120-snippet.csv" AND your two added columns. Save the csv file and attach it 
to your assignment submission.
"""

#pandas is a library included with Anaconda. It's great for manipulating csv files as "dataframes".
import pandas as pd

#Here we are reading the csv file "covidtesting_cs2120-snippet.csv" into a dataframe called "covid19_data"
covid19_data = pd.read_csv("covidtesting_cs2120-snippet.csv")

#Uncomment the line below to print the csv contents
print(covid19_data)

"""
This function finds the daily increase of cases in a dataframe and returns a list with all of these increases.
i.e. for "Confirmed_Negative-Cumulative" as an input column, it should return a list where each subsequent
entry is equal to the number of "new" confirmed negative cases for that corresponding day. 
"""


def get_daily_increase(dataframe, col_name):
    #In the lines below we are creating a list called "daily_increase" and adding an initial value to the list
    daily_increase = []
    daily_increase.append(dataframe.iloc[0][col_name])


    #This loops through the column, finding all of the daily increases
    for i in range(len(dataframe[col_name])-1):
        # Uncomment the line below to see how many iterations are in the loop
        #print(i)

        #!!! YOUR CODE BELOW. The line below is incorrect. Fix it with the correct operation(s)  (done)
        daily_increase.append(dataframe.iloc[i+1][col_name] - dataframe.iloc[i][col_name])

    # Uncomment the line below to see what daily_increase looks like
    print(daily_increase)

    return daily_increase


"""
This function finds the cumulative increase of cases in a dataframe and returns a list with all of those increases.
i.e. for "Confirmed_Positive-Daily" as an input column, it should return a list where the entry for a particular day
is equal to the sum of all previous daily entries (# of cases) + the current daily entry (# of cases). 
"""
def get_cumulative_increase(dataframe, col_name):
    cumulative_increase = []
    cumulative_increase.append(0)

    # This loops through the column, adding all of the increases (cumulative) to the list
    for i in range(0,len(dataframe[col_name])):

        # !!! YOUR CODE BELOW. There is a syntax error in the line below. Provide your correction. (done)
        cumulative_increase.append(cumulative_increase[i]+dataframe.iloc[i][col_name])

    cumulative_increase.pop(0)
    #Uncomment the line below to see what cumulative_increase looks like
    print(cumulative_increase)

    return cumulative_increase

"""
This function returns the overall number of cases for 2 cumulative case lists (i.e. Confirmed_Positive-Cumulative and
Confirmed_Negative-Cumulative).
"""
def total_cumulative_count(cumulative_list1, cumulative_list2):
    total_cumulative_count = cumulative_list1[len(cumulative_list1)-1] + cumulative_list2[len(cumulative_list2)-1]
    return total_cumulative_count

"""
This function adds a list (i.e. the output of cumulative_increase) to a dataframe. You can use this
function to call cumulative_increase and add the returned list to your covid19_data dataframe.
"""
def add_column_to_dataframe(dataframe, column_name, column_list):
    dataframe[column_name] = column_list

"""
This function returns the maximum value of a list.
"""
def get_max_of_list(list):
    return max(list)

"""
This function returns a dataframe column as a list.
"""
def convert_df_column_to_list(dataframe, column_name):
    return dataframe[column_name].tolist()

"""
This function exports a dataframe to a specific csv file named "a1_submission.csv". Include this csv file in your submission.
"""
def export_dataframe_to_csv(dataframe):
    dataframe.to_csv("a1_submission.csv",index=False)

#----------------------------------------------------------------------------------------------------------

#!!! YOUR CODE BELOW. CALL ALL OF YOUR FUNCTIONS HERE!

#creating and naming the list; in quotes = set data; not in quotes (list name) = variable
confirmed_negative_daily = get_daily_increase(covid19_data, "Confirmed_Negative-Cumulative")

#structure it into the column formatting
add_column_to_dataframe(covid19_data, "Confirmed_Negative-Daily", confirmed_negative_daily)
print(covid19_data)

#creating and naming the list
confirmed_positive_cumulative = get_cumulative_increase(covid19_data, "Confirmed_Positive-Daily")

#structure it into the column formatting
add_column_to_dataframe(covid19_data, "Confirmed_Positive-Cumulative", confirmed_positive_cumulative)
print(covid19_data)

#change it into list before we can calculate the max
confirmed_positive_daily = convert_df_column_to_list(covid19_data, "Confirmed_Positive-Daily")
print(get_max_of_list(confirmed_positive_daily), "is the highest daily increase in positive cases.")

#turn into new excel file
export_dataframe_to_csv(covid19_data)




