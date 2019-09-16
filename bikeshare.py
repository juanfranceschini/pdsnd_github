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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Select a city (chicago, new york city, washington) ")

    while city not in ("chicago","new york city","washington"):
        print("hmmm something went wrong. try again please")
        city = input("Select a city (chicago, new york city, washington) ")

    print("great! you chose" +" "+ city)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Select a month (all, january, february, ... , june) ")

    while month not in ("all","january","february","march","april","may","june"):
        print("hmmm something went wrong. try again please")
        month = input("Select a month (all, january, february, ... , june) ")

    print("great! you chose" +" "+ month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Select a day (all, monday, tuesday, ... sunday) ")

    while day not in ("all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"):
        print("hmmm something went wrong. try again please")
        day = input("Select a day (all, monday, tuesday, ... sunday) ")

    print("great! you chose" +" "+ day)

    print('-'*100)
    print('-'*100)
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = df['month'].mode()[0]
    common = months[common_month-1]
    print("the most common month is"+" "+ str(common))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("the most common day of the week is"+" "+ str(common_day))

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("the most common start hour is"+" "+ str(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("the most common start station is"+" "+ start_station)


    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("the most common end station is"+" "+ end_station)


    # TO DO: display most frequent combination of start station and end station trip
    start_end = df['Start Station'].str.cat(df['End Station'],sep="-").mode()[0]
    print("the most frequent combination of start and end station is"+" "+ start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print("total travel time is"+" "+str(int(travel_time/60))+" minutes")


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("mean travel time is"+" "+str(int(mean_time/60))+" minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("These are the counts of user types:"+" "+str(user_types))
    print("\n")
    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts().dropna()
    print("These are the counts of gender:"+" "+str(gender))

    print("\n")
    # TO DO: Display earliest, most recent, and most common year of birth
    recent_bday = df['Birth Year'].max()
    earliest_bday = df['Birth Year'].min()
    common_bday = df['Birth Year'].mode()
    print("the most recent year of birth is"+" "+ str(int(recent_bday)))
    print("the earliest year of birth is"+" "+ str(int(earliest_bday)))
    print("the most common year of birth is"+" "+ str(int(common_bday)))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        part1 = input('\nWould you like to keep going? Enter yes or no.\n')
        if part1.lower() != 'yes':
            break
        time_stats(df)
        part2 = input('\nWould you like to keep going? Enter yes or no.\n')
        if part2.lower() != 'yes':
            break
        station_stats(df)
        part3 = input('\nWould you like to keep going? Enter yes or no.\n')
        if part3.lower() != 'yes':
            break
        trip_duration_stats(df)
        part4 = input('\nWould you like to keep going? Enter yes or no.\n')
        if part4.lower() != 'yes':
            break
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
