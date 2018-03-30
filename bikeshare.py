## TODO: import all necessary packages and functions
import csv
import time
import calendar
import pandas as pd
import datetime
from collections import Counter



## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'



def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')

    if city == 'New York' or city == 'new york':
        return new_york_city
    if city =='chicago' or city == 'Çhicago':
        return chicago
    if city == 'Washinton' or city == 'washington':
        return washington





def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    if time_period == 'month' or time_period == 'Month':
         return 'month'
    if time_period == 'day' or time_period == 'Day':
        return 'day'
    if time_period == 'none' or time_period == 'None':
        return 'none'


def get_month():
    month = input('\nWhich month? jan, feb, mar, apr, may, jun,jul,aug,sep,oct,nov,dec?\n')
    return month

def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = int(input('\nWhich day of the week ? Please type your response as an integer(i.e. 1= Sunday).\n'))
    return day

def get_month_number(month):
    month_number = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    return month_number.index(month) + 1




def popular_month(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    month_count=[]
    df = pd.read_csv(city_file)
    start_time_column=(pd.to_datetime(df['Start Time']))
    col_month=start_time_column.apply(lambda start_time_column: start_time_column.month) # to extract month from date column
    c=[]
    c=(Counter(col_month))#to count the occurence of months
    popular=max(c) # to count maximum occurence
    Month_name=calendar.month_name[popular] #find out the name of month
    return Month_name
#
# functio done by isha
def popular_day(city_file,time_period,month):
    df = pd.read_csv(city_file)
    start_time_column = (pd.to_datetime(df['Start Time']))
    weekday=''
    if time_period == 'none':
     col_day=start_time_column.dt.weekday# to extract the weekday from date
     c=[]
     c = (Counter(col_day))  # to count the occurence of days
     popular1=max(c)   # to count maximum occurence
     weekday=calendar.day_name[popular1]
    if time_period=='month':
      month_number = get_month_number(month)
      df['Start Time'] = pd.to_datetime(df['Start Time'])
      month_data=df.ix[df.ix[:, 'Start Time'].apply(lambda x: x.month) == month_number, :]
      #col_day=month_data['Start Time'].apply(lambda start_time_column: start_time_column.dt.weekday)
      col_day=month_data['Start Time'].dt.dayofweek
      c = []
      c = (Counter(col_day))  # to count the occurence of days
      popular1 = max(c)  # to count maximum occurence
      weekday = calendar.day_name[popular1]
    return weekday



#function done by isha
def popular_hour(city_file, time_period,monthOrDay):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    df = pd.read_csv(city_file)
    start_time_column=(pd.to_datetime(df['Start Time']))
    c = []
    pop_hour=''
    if time_period == 'none':
     col_hour=start_time_column.apply(lambda start_time_column: start_time_column.hour) # to extract Hour from date column
     c=(Counter(col_hour))#to count the occurence of hour
     pop_hour=max(c) # to count maximum occurence

    if time_period=='month':
      month_number=get_month_number(monthOrDay)
      df['Start Time'] = pd.to_datetime(df['Start Time'])
      month_data=df.ix[df.ix[:, 'Start Time'].apply(lambda x: x.month) == month_number, :]
      col_hour=pd.to_datetime(month_data['Start Time']).apply(lambda start_time_column: start_time_column.hour)
      c = (Counter(col_hour))  # to count the occurence of hour
      pop_hour = max(c)


    if time_period == 'day':
      df['Start Time'] = pd.to_datetime(df['Start Time'])
      day_data = df.ix[df.ix[:, 'Start Time'].apply(lambda x: x.day) == monthOrDay, :]
      col_hour = pd.to_datetime(day_data['Start Time']).apply(lambda start_time_column: start_time_column.hour)
      c = (Counter(col_hour))  # to count the occurence of hour
      pop_hour = max(c)

    return pop_hour

#  Function done by isha
def trip_duration(city_file, time_period,monthOrDay):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    df = pd.read_csv(city_file)
    total=''
    average=''
    if time_period=='none':
     total = df['Trip Duration'].sum()
     average= total/len(df['Trip Duration'])
     print("Total Trip duration is "+str(total))
     print("Average Trip Duration is " +str(average))
    if time_period=='month':
      month_number = get_month_number(monthOrDay)
      df['Start Time'] = pd.to_datetime(df['Start Time'])
      month_data=df.ix[df.ix[:, 'Start Time'].apply(lambda x: x.month) == month_number, :]
      Trip_data=month_data['Trip Duration']
      total=Trip_data.sum()
      average=total/len(Trip_data)
      print("Total Trip duration is " + str(total))
      print("Average Trip Duration is " + str(average))
    if time_period=='day':
      df['Start Time'] = pd.to_datetime(df['Start Time'])
      day_data = df.ix[df.ix[:, 'Start Time'].apply(lambda x: x.day) == monthOrDay, :]
      Trip_data = day_data['Trip Duration']
      total = Trip_data.sum()
      average = total / len(Trip_data)
      print("Total Trip duration is " + str(total))
      print("Average Trip Duration is " + str(average))



# #function done by isha
def popular_stations(city_file, time_period,monthorday):
    '''TODO: fill out docstring with description, arguments, and return values.
         Question: What is the most popular start station and most popular end station?
    '''
    df = pd.read_csv(city_file)
    if time_period=='none':
     start_station = df['Start Station']
     end_station = df['End Station']
     popular_start_station = max(Counter(start_station))
     print('The most popular start station is  '+popular_start_station)
     popular_end_station=max(Counter(end_station))
     print('The most popular End station is  ' +popular_end_station)
    if time_period == 'month':
     month_number = get_month_number(monthorday)
     df['Start Time'] = pd.to_datetime(df['Start Time'])
     month_data = df.ix[df.ix[:, 'Start Time'].apply(lambda x: x.month) == month_number, :]
     start_station=month_data['Start Station']
     end_station = month_data['End Station']
     popular_start_station = max(Counter(start_station))
     print('The most popular start station is  ' + popular_start_station)
     popular_end_station = max(Counter(end_station))
     print('The most popular End station is  ' + popular_end_station)
    if time_period=='day':
      df['Start Time'] = pd.to_datetime(df['Start Time'])
      day_data = df.ix[df.ix[:, 'Start Time'].apply(lambda x: x.day) == monthorday, :]
      start_station = day_data['Start Station']
      end_station = day_data['End Station']
      popular_start_station = max(Counter(start_station))
      print('The most popular start station is  ' + popular_start_station)
      popular_end_station = max(Counter(end_station))
      print('The most popular End station is  ' + popular_end_station)







def popular_trip(city_file, time_period,monthorday):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    StartSt=''
    Endst=''

    if time_period=='none':
     data= df.groupby(['Start Station','End Station']).size().reset_index(name="Time")
     maximumtrip=max(data['Time'])
     for index, row in data.iterrows():
         if row['Time']==maximumtrip:
          StartSt=row['Start Station']
          Endst=row['End Station']
    if time_period == 'month':
      month_number = get_month_number(monthorday)
      df['Start Time'] = pd.to_datetime(df['Start Time'])
      month_data = df.ix[df.ix[:, 'Start Time'].apply(lambda x: x.month) == month_number, :]
      data=month_data.groupby(['Start Station','End Station']).size().reset_index(name="Time")
      maximumtrip = max(data['Time'])
      for index, row in data.iterrows():
           if row['Time'] == maximumtrip:
               StartSt = row['Start Station']
               Endst = row['End Station']
    if time_period=='day':

      df['Start Time'] = pd.to_datetime(df['Start Time'])
      day_data = df.ix[df.ix[:, 'Start Time'].apply(lambda x: x.day) == monthorday, :]
      data = day_data.groupby(['Start Station', 'End Station']).size().reset_index(name="Time")
      maximumtrip = max(data['Time'])
      for index, row in data.iterrows():
        if row['Time'] == maximumtrip:
         StartSt = row['Start Station']
         Endst = row['End Station']
    print('The Most Popular Trip is started from '+ StartSt +' and Ends on ' +Endst )










def users(city_file, time_period,monthorday):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    row_data=''
    if time_period=='none':
     user_type=df['User Type']
     c=Counter(user_type)
     print(c)
    if time_period=='month':
      month_number = get_month_number(monthorday)
      df['Start Time'] = pd.to_datetime(df['Start Time'])
      row_data = df.ix[df.ix[:, 'Start Time'].apply(lambda x: x.month) == month_number, :]
      user_type = row_data['User Type']
      c = Counter(user_type)
      print(c)
    if time_period == 'day':
       df['Start Time'] = pd.to_datetime(df['Start Time'])
       row_data = df.ix[df.ix[:, 'Start Time'].apply(lambda x: x.day) == monthorday, :]
       user_type = row_data['User Type']
       c = Counter(user_type)
       print(c)




def gender(city_file, time_period):
   '''TODO: fill out docstring with description, arguments, and return values.
     Question: What are the counts of gender?
     '''
   df = pd.read_csv(city_file)
   if city_file==chicago or city_file==new_york_city:
      gender_data=df['Gender']
      c = Counter(gender_data)
      print(c)





def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    if city_file !='washington.csv':
     birthyear_max=df.loc[df['Birth Year'].idxmax()]
     print("The Youngest User is having Birth Year ")
     print(birthyear_max['Birth Year'])
     birthyear_min = df.loc[df['Birth Year'].idxmin()]
     print("The Oldest User is having birth year " )
     print(birthyear_min['Birth Year'])





# def display_data():
#     '''Displays five lines of data if the user specifies that they would like to.
#     After displaying five lines, ask the user if they would like to see five more,
#     continuing asking until they say stop.
#
#     Args:
#         none.
#     Returns:
#         TODO: fill out return type and description (see get_city for an example)
#     '''
#     display = input('\nWould you like to view individual trip data?'
#                     'Type \'yes\' or \'no\'.\n')
#     # TODO: handle raw input and complete function
#
#
def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    # filter by day
    if time_period =='month':
     month=get_month()
    if time_period=='day':
     day=get_day()


    print('Calculating the first statistic...')


    # #What is the most popular month for start time?
    if time_period == 'none'or time_period=='none':
       start_time = time.time()
       pop_month=popular_month(city)
       print("The most popular month is " + pop_month)
    elif  time_period =='month':
      print("The most Popular month is  " + month)



    print("Calculating the next statistic...")

     # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    #
    #
    if time_period == 'none':
      month = 0
      start_time = time.time()
      pop_day=popular_day(city,time_period,month)
      print("The most popular day is " +pop_day)
    elif time_period=='month':
      pop_day = popular_day(city, time_period, month)
      print("The most popular day is " + pop_day)
    elif time_period=='day':
      print("The most popular day is " +str(day))



#         # TODO: call popular_day function and print the results
#
#print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
#
#     start_time = time.time()
#
#     # What is the most popular hour of day for start time?
#     # TODO: call popular_hour function and print the results
#
      #print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    if time=='month':
     pop_hour=popular_hour(city,time_period,month)
     print("Popular Hour is " + str(pop_hour))
    if time_period=='day':
     pop_hour = popular_hour(city, time_period,day)
     print("Popular Hour is " + str(pop_hour))
    if time_period=='none':
     pop_hour = popular_hour(city, time_period,0)
     print("Popular Hour is " +str(pop_hour))


#     # What is the total trip duration and average trip duration?
#     # TODO: call trip_duration function and print the results
    if time_period=='none':
     month=0
     trip_duration(city,time_period,month)
    if time_period=='month':
      trip_duration(city, time_period, month)
    if time_period=='day':
      trip_duration(city, time_period, day)

#
#     print("That took %s seconds." % (time.time() - start_time))
#     print("Calculating the next statistic...")
#     start_time = time.time()
#
   # What is the most popular start station and most popular end station?
     # TODO: call popular_stations function and print the results
    if time_period=='none':
     month=0
     popular_stations(city,time_period,month)
    if time_period=='month':
     popular_stations(city, time_period, month)
    if time_period=='day':
     popular_stations(city, time_period, day)




#    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
#     start_time = time.time()
#
#     # What is the most popular trip?
#     # TODO: call popular_trip function and print the results
    if time_period=='none':
     popular_trip(city,time_period,0)
    if time_period == 'month':
      popular_trip(city, time_period,month)
    if time_period=='day':
      popular_trip(city, time_period, day)

#
#     print("That took %s seconds." % (time.time() - start_time))
#     print("Calculating the next statistic...")
#     start_time = time.time()

#     # What are the counts of each user type?
#     # TODO: call users function and print the results
    if time_period=='none':
     users(city,time_period,0)
    if time_period=='month':
     users(city,time_period,month)
    if time_period=='day':
     users(city,time_period,day)

#     print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")

#     # What are the counts of gender?
#     # TODO: call gender function and print the results

    gender(city,time_period)
    birth_years(city, time_period)
#     # TODO: call birth_years function and print the results
#
#     print("That took %s seconds." % (time.time() - start_time))
#
#     # Display five lines of data at a time if user specifies that they would like to
#     display_data()
#
#     # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
     statistics()
#
#
if __name__ == "__main__":
 statistics()