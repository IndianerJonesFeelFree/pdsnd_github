###Header:  Bikeshop - Statistic - Software
###Author:  Johannes Baumer
###Date:    15.07.2023

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        print("Choose one city")
        print("Chicago")
        print("New York")
        print("Washington")
        print("Also over all an analysis can be done - than choose")
        print("All")
        city = input("\nEnter your city-interest?\n")



    # get user input for month (all, january, february, ... , june)
        print("Choose one month")
        print("January")
        print("February")
        print("March")
        print("April")
        print("May")
        print("June")
        print("Also over all an analysis can be done - than choose")
        print("All")
        month = input("\nEnter your month-interest?\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
        print("Choose one day of the week")
        print("Monday")
        print("Tuesday")
        print("Wednesday")
        print("Thursday")
        print("Friday")
        print("Saturday")
        print("Sunday")
        print("Also over all an analysis can be done - than choose")
        print("All")
        day = input("\nEnter your day-interest?\n")


        if city not in ["Chicago", "New York", "Washington", "All"]:
            print("Try again - the city-spelling was incorrect")
        else:
            if month not in ["January", "February", "March", "April", "May", "June", "All"]:
                print("Try again - the month-spelling was incorrect")
            else:
                if day not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "All"]:
                    print("Try again - the day-spelling was incorrect")
                else:
                    return city, month, day

        print('-'*40)


def display(df):
    i = 0
    j = i+5
    x = 5
    while True:
        print(df[i:j])
        i=i+5
        j=j+5
        reshow = input('\nWould you like to see x more lines? Standard is 5 more? yes or no.\n')
        if reshow.lower() != 'no':
            continue
        break



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if city in ["Chicago", "New York", "Washington"]:
        CITY_DATA = {'Chicago': 'chicago.csv',
                     'New York': 'new_york_city.csv',
                     'Washington': 'washington.csv'}


        # load data file into a dataframe
        df = pd.read_csv(CITY_DATA[city])
        df.to_csv('file_name.csv')
    else:
        df = pd.concat(map(pd.read_csv, ['chicago.csv', 'new_york_city.csv','washington.csv']))
        #df.to_csv('All.csv')

    print("The quantities of the different columns are")
    print(df.count())

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns


    df['day_of_week'] = df['Start Time'].dt.day_name()

    df['hour'] = df['Start Time'].dt.hour

    df['month'] = df['Start Time'].dt.month

    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("\nThe most common month in your data choice is: ", months[df['month'].mode()[0]-1])

    # display the most common day of week
    print("\nThe most common day of week in your data choice is: ", df['day_of_week'].mode()[0])

    # display the most common start hour
    print("\nThe most common hour in your data choice is: ", df['hour'].mode()[0])

    print("\nThis took %s ms." % round((time.time() - start_time)*1000, 2))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("\nThe most commonly used start station in your data choice is: ", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("\nThe most commonly used end station in your data choice is: ", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print("\nThe most commonly done Trip in your data choice is from: \n", df['Start Station'].mode()[0])
    print("\nto\n", df['End Station'].mode()[0])
    print("\nThis took %s ms." % round((time.time() - start_time)*1000, 2))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("\nThe total travel time for your data choice is: ", round(df['Trip Duration'].sum()/3600, 2) ,"h")

    # display mean travel time
    print("\nThe mean travel time for your data choice is: ", round(df['Trip Duration'].mean()/3600, 2), "h")

    print("\nThis took %s ms." % round((time.time() - start_time)*1000, 2))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("\nThe counts of user types for your data choice is: \n", df['User Type'].value_counts())

    # Display counts of gender
    try:
        print("\nThe counts of gender for your data choice is: \n", df['Gender'].value_counts())
    except:
        print("No Gender column available!!")
    # Display earliest, most recent, and most common year of birth
    try:
        print("\nThe earliest year of birth for your data choice is: ", df['Birth Year'].min())
        print("\nThe most recent year of birth for your data choice is: ", df['Birth Year'].max())
        print("\nThe most common year of birth for your data choice is: ", df['Birth Year'].mode()[0])
    except:
        print("No Birth year column available!!")
    print("\nThis took %s ms." % round((time.time() - start_time)*1000, 2))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)
        display(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
