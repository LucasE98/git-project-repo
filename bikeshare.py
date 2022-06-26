import time
import pandas as pd
import numpy as np
import datetime
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
    cities = ['chicago', 'new york city','washington']
    while True:
        city = input("Would you like to see data for Chicago, New York City or Washington?").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Please enter one of the provided cities.")
        else:
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which Month? January, February, March, April, May, June or all?").lower() 
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'):
            print("Something went wrong. Please enter one of the given Month or all.")
        else:
            break
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which Day of the week? PLease type the full name like Monday, etc.. or all.").lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("An unxpected mistake happen, please check that you write the day correct.")
        else: 
            break
            
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
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['year']= df['Start Time'].dt.year
    df['month']= df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1
        df=df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    common_month = df['month'].mode()[0]
    print('Most Popular Start Month:', common_month)
    
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    common_day = df['day'].mode()[0]
    print('Most Popular Start Day:', common_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', common_hour,'o\'clock')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', start_station)
    
    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:', end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    
    df['Combination'] = df['Start Station'] + " " + df['End Station']
    combination_stations = df['Combination'].mode()[0]
    print('The most frequent combination of start and end station is:', combination_stations)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('\nTotal travel time: %s.'%str(datetime.timedelta(seconds = int(total_time))))
    
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('\nMean travel time: %s.'%str(datetime.timedelta(seconds = mean_time)))
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('Counts of user types: \n',count_user_types)
    
    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print('Counts of gender: \n', count_gender)
    except KeyError:
        print('Data is not available for the selected city')    
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        earliest_year = int(earliest_birth_year)
        print('The earliest year of birth: ', earliest_year)
        most_recent_year = df['Birth Year'].max()
        recent_year = int(most_recent_year)
        print('The most recent year of birth: ', recent_year)
        most_common_birth = df['Birth Year'].mode()[0]
        common_birth = int(most_common_birth)
        print('The most common year of birth: ', common_birth)
    except KeyError:
        print('The data is not available')
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)
    
def view_extra_data(df):
    viewer_extras = input('\nWould you like to view 5 individual rows of trip data? Enter Yes or No: \n').lower()
    extras = ['yes']
    view_steps = 0
    while (viewer_extras in extras):
        print(df.iloc[view_steps:view_steps+5])
        view_steps += 5
        viewer_extras = input('Would you like to continue?: ').lower()
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_extra_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
