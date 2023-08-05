import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def display_data(df, city):
    """
    Displays the continuous raw data upon request by the user.
    Ask user if they want to see the first 5 rows of data
    Display the first 5 rows of data to the user if the answer is yes
    Then ask user if they want to see the next 5 rows of data
    Continue iterating these prompts and displaying the next 5 rows of data
    Stop the program when the user say no or there is no more data to display
    """
    start_loc = 0
    display = input('\nDo you want to see the first 5 rows of data? Enter yes or no.\n')
    while (display.lower() == 'yes'):
        end_loc = start_loc + 5
        print(df.iloc[start_loc : end_loc])
        start_loc = end_loc
        display = input('\nDo you want to see the next 5 rows of data? Enter yes or no.\n')
    print('-'*40)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter city:")
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input("Enter city:")
    city = city.lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter month:")
    while month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Enter month:")
    month = month.lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day of week:")
    while day.lower() not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'sartuday', 'sunday']:
        day = input("Enter day of week:")
    day = day.lower()
    
    print('-'*40)
    return city, month, day


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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("\nThe most common month: ", popular_month)
    
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("\nThe most common day of week: ", popular_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("\nThe most common start hour: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular start station - end station and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("\nThe most commonly used start station: ", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("\nThe most commonly used end station: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip Station'] = df['Start Station'] + ' TO ' + df['End Station']
    popular_common_trip = df['Trip Station'].mode()[0]
    print("\nThe most commonly used trip: ", popular_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\nTotal travel time: ", total_travel_time)

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("\nAverage travel time: ", average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nCounts of user types: \n", user_types)
    
    if city in ['chicago', 'new york']:
    # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("\nCounts of gender: \n", gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yob = df['Birth Year'].min()
        most_recent_yob = df['Birth Year'].max()
        most_common_yob = df['Birth Year'].mode()[0]
        print("\nThe earliest year of birth: ", earliest_yob)
        print("\nThe most recent year of birth: ", most_recent_yob)
        print("\nThe most common year of birth: ", most_common_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df, city)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
