## TODO: import all necessary packages and functions
import csv
import time
import calendar
import pandas as pd
import datetime
from collections import Counter
from pprint import pprint
from itertools import islice



## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'



def get_city():
    '''
    The Function is use to take the input from user as to
     which city's data the user wants to see
     :return: The city file
    '''

    flag=1
    while flag==1:
      city_input = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for chicago, new york, or washington?\n')
      city=city_input.lower()
      if city == 'chicago' or city == 'new york' or city == 'washington':
       flag=0
       if city == 'new york':
        return new_york_city
       if city == 'chicago':
        return chicago
       if city == 'washington':
         return washington
      else :
       print('The city entered is do not exist in list ,please re-enter the city ')
       flag=1







def get_time_period():
    '''
    The function is used for taking input from user
    regarding the time period .If user want us to filter data on basis of day/month/none
    :return: time period
    '''

    time_input = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    time_period=time_input.lower()
    if time_period == 'month':
         return 'month'
    if time_period == 'day' or time_period == 'Day':
        return 'day'
    if time_period == 'none' or time_period == 'None':
        return 'none'


def get_month():
    '''
     The function is used for taking input from user ,about the month .
     If user sleected time period as month then this function is used to find out which month .
     :return: month as a string
     '''
    flag=1
    mn=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    while flag ==1  :
     month = input('\nWhich month? jan, feb, mar, apr, may, jun,jul,aug,sep,oct,nov,dec?\n')
     for i in mn:
      if i == month:
       flag=0
       break;

    return month

def get_day():
    '''
     The function is used for taking input from user ,about the day .
     If user sleected time period as day then this function is used to find out which day of week .
     :return: day as an integer
     '''
    flag=1
    day=''
    while flag==1:
      day_input = int(input('\nWhich day of the week ? Please type your response as an integer(i.e. 1= Sunday).\n'))
      print(day)
      if day_input > 7:
       print('Please enter day of week between 1-7 ')
       flag=1
      else :
       flag=0
       day=day_input
    return day

def get_month_number(month):
    '''
         This function converts Month name to Month Number
         :return: month as an integer
         '''

    month_number = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    return month_number.index(month) + 1




def popular_month(df):
    '''
            Based on time period ,this function find out Popular Month of the particular city
            :return: month Name
    '''

    month_count=[]
    start_time_column=(pd.to_datetime(df['Start Time']))
    col_month=start_time_column.apply(lambda start_time_column: start_time_column.month) # to extract month from date column
    c=[]
    c=(Counter(col_month))#to count the occurence of months
    popular=max(c) # to count maximum occurence
    Month_name=calendar.month_name[popular] #find out the name of month
    return Month_name

# functio done by isha
def popular_day(df,time_period,monthorday):
    '''
               Based on time period ,this function find out Popular day of the week of the particular city
               :return: Weekday name
       '''
    start_time_column = (pd.to_datetime(df['Start Time']))
    weekday=''
    if time_period == 'none':
     col_day=start_time_column.dt.weekday# to extract the weekday from date
     c=[]
     c = (Counter(col_day))  # to count the occurence of days
     popular1=max(c)   # to count maximum occurence
     weekday=calendar.day_name[popular1]
    if time_period=='month':
      month_number = get_month_number(monthorday)
      df['Start Time'] = pd.to_datetime(df['Start Time'])
      month_data=df.ix[df.ix[:, 'Start Time'].apply(lambda x: x.month) == month_number, :]
      #col_day=month_data['Start Time'].apply(lambda start_time_column: start_time_column.dt.weekday)
      col_day=month_data['Start Time'].dt.dayofweek
      c = []
      c = (Counter(col_day))  # to count the occurence of days
      popular1 = max(c)  # to count maximum occurence
      weekday = calendar.day_name[popular1]

    if time_period =='day':
      weekday = calendar.day_name[monthorday]


    return weekday



#function done by isha
def popular_hour(df, time_period,monthOrDay):
    '''
                  Based on time period ,this function find out Popular hour of the day of the particular city
                  :return: hour as integer
          '''

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
def trip_duration(df, time_period,monthOrDay):
    '''
                  Based on time period ,this function find out Average and Total Trip Duration
                  of particular city

          '''

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
def popular_stations(df, time_period,monthorday):
    '''
     Based on time period ,this function find out Popular Start and End station of the city

     '''
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







def popular_trip(df, time_period,monthorday):
    '''
     Based on time period ,this function find out Popular trip i.e. most common combination of start and end station
     of particular city

    '''

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










def users(df, time_period,monthorday):
    '''
                  Based on time period ,this function counts the type of Users

    '''

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
    '''
         This function counts the total of all gender who subscribed the services
     '''

    df = pd.read_csv(city_file)
    if city_file==chicago or city_file==new_york_city:
      gender_data=df['Gender']
      c = Counter(gender_data)
      print(c)





def birth_years(city_file, time_period):
    '''
            This function find out the most Youngest and and most oldest subscriber
        '''
    df = pd.read_csv(city_file)
    if city_file !='washington.csv':
     birthyear_max=df.loc[df['Birth Year'].idxmax()]
     print("The Youngest User is having Birth Year ")
     print(birthyear_max['Birth Year'])
     birthyear_min = df.loc[df['Birth Year'].idxmin()]
     print("The Oldest User is having birth year " )
     print(birthyear_min['Birth Year'])





def display_data(city):
     '''
            This function displays individual trip
        '''

     display_input = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
     display=display_input.lower()
     if display =='yes':

      print('\nCity: {}'.format(city))
      with open(city, 'r') as f_in:
       trip_reader = csv.DictReader(f_in)
         # first_trip = next(trip_reader)
         # pprint(first_trip)
       for i, row in enumerate(trip_reader):
        pprint(row)
        if (i >= 5):
         check=input('Do you want to display more data (yes/no)')
         if check.lower()=='no':
          break;


#
#
def statistics():

    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    df = pd.read_csv(city)


    # Filter by time period (month, day, none)
    time_period = get_time_period()

    # filter by day
    if time_period =='month':
     month=get_month()
    if time_period=='day':
     day=get_day()


    print('Calculating the first statistic...')


    # #What is the most popular month for start time?
    if time_period == 'none':
       start_time = time.time()
       pop_month=popular_month(df)
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
      pop_day=popular_day(df,time_period,month)
      print("The most popular day is " +pop_day)
    elif time_period=='month':
      pop_day = popular_day(df, time_period, month)
      print("The most popular day is " + pop_day)
    elif time_period=='day':
      pop_day = popular_day(df, time_period, day)
      print("The most popular day is " + pop_day)



#
#print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
#
#     start_time = time.time()
#
#     # What is the most popular hour of day for start time?

#
      #print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    if time=='month':
     pop_hour=popular_hour(df,time_period,month)
     print("Popular Hour is " + str(pop_hour))
    if time_period=='day':
     pop_hour = popular_hour(df, time_period,day)
     print("Popular Hour is " + str(pop_hour))
    if time_period=='none':
     pop_hour = popular_hour(df, time_period,0)
     print("Popular Hour is " +str(pop_hour))


#     # What is the total trip duration and average trip duration?

    if time_period=='none':
     month=0
     trip_duration(df,time_period,month)
    if time_period=='month':
      trip_duration(df, time_period, month)
    if time_period=='day':
      trip_duration(df, time_period, day)

#
#     print("That took %s seconds." % (time.time() - start_time))
#     print("Calculating the next statistic...")
#     start_time = time.time()
#
   # What is the most popular start station and most popular end station?

    if time_period=='none':
     month=0
     popular_stations(df,time_period,month)
    if time_period=='month':
     popular_stations(df, time_period, month)
    if time_period=='day':
     popular_stations(df, time_period, day)




#    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
#     start_time = time.time()
#
#     # What is the most popular trip?

    if time_period=='none':
     popular_trip(df,time_period,0)
    if time_period == 'month':
      popular_trip(df, time_period,month)
    if time_period=='day':
      popular_trip(df, time_period, day)

#
#     print("That took %s seconds." % (time.time() - start_time))
#     print("Calculating the next statistic...")
#     start_time = time.time()

#     # What are the counts of each user type?

    if time_period=='none':
     users(df,time_period,0)
    if time_period=='month':
     users(df,time_period,month)
    if time_period=='day':
     users(df,time_period,day)

#     print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")

#     # What are the counts of gender?


    gender(city,time_period)
    birth_years(city, time_period)

#
#     print("That took %s seconds." % (time.time() - start_time))
#
#     # Display five lines of data at a time if user specifies that they would like to
    display_data(city)
#
#     # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
     statistics()
#
#
if __name__ == "__main__":
 statistics()