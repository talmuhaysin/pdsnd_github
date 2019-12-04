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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nWould you like to see data for Chicago, New York City, or Washington?\n').lower()
    while(True):
            if(city == 'chicago' or city == 'new york city' or city == 'washington'):
                break
            else:
                city = input('please type correct city: ').lower()

    # get user input for month (all, january, february, ... , june)
    month = input('\nWhich month would you like to show data for ? January, February, March, April, May, or June or All to display data of all months?\n').lower().capitalize()
    while(True):
            if(month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May' or month == 'June' or month == 'All'):
                break
            else:
                month = input('please type correct month\n').lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day =  input('Which day would you like to show data for ? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday , Sunday or All to display data of all days?\n').lower().capitalize()
    while(True):

            if(day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday' or day == 'Sunday' or day == 'All'):
                break
            else:
                day = input('please type correct day: ').lower()
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
    df = pd.read_csv(CITY_DATA[city])


    # convert the start and end times from strings to dates, so we can extract the day/month from them
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract the day and month into their separate columns
    df['day'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month_name()

    # filter by month if applicable
    if month != 'All':
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month:\n{} \n".format(popular_month))

    # display the most common day of week
    popular_day = df['day'].mode()[0]
    print("Most common day:\n{} \n".format(popular_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour:\n{} \n".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_used_start_station = df['Start Station'].mode()
    print('common_used_start_station:', common_used_start_station)

    # display most commonly used end station
    common_used_end_station = df['End Station'].mode()
    print('common_used_end_station:', common_used_end_station)

    # display most frequent combination of start station and end station trip
    df['route'] = df['Start Station'] + df['End Station']
    common_frequent_route = df['route'].mode()
    print('common_frequent_route:', common_frequent_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print('Total travel time:', Total_Travel_Time)

    # display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if "Gender" in  df.columns:
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    else :
        print("Gender is not available")

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in  df.columns:
        Earliest_Year = df['Birth Year'].min()
        print('Earliest Year:', Earliest_Year)

        Most_Recent_Year = df['Birth Year'].max()
        print('Most Recent Year:', Most_Recent_Year)

        Most_common_Year = df['Birth Year'].mode()
        print('Most Common Year:',Most_common_Year)
    else :
        print("Birth Year is not available")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        want_raw_data = input("Would you like to see more of the raw data?").strip().lower()
        start = 0
        end = 5 #not included
        while(want_raw_data == "yes"):
            print(df.iloc[start:end])
            start += 5
            end += 5
            want_raw_data = input("Would you like to see more of the raw data?").strip().lower()

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
