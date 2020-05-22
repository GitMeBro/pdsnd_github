## import all necessary packages and functions.
import csv # read and write csv files
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.




def print_first_point(filename):
    """
    This function prints and returns the first data point (second row) from
    a csv file that includes a header row.
    """
    # print city name for reference
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))
    
    with open(filename, 'r') as f_in:
        ## TODO: Use the csv library to set up a DictReader object. ##
        ## see https://docs.python.org/3/library/csv.html           ##
        trip_reader = csv.DictReader(f_in)
        
        ## TODO: Use a function on the DictReader object to read the     ##
        ## first trip from the data file and store it in a variable.     ##
        ## see https://docs.python.org/3/library/csv.html#reader-objects ##

        for row in trip_reader:
            first_trip = row
            break
        
        ## TODO: Use the pprint library to print the first trip. ##
        ## see https://docs.python.org/3/library/pprint.html     ##
        pprint(first_trip)
        
    # output city name and first trip for later testing
    return (city, first_trip)

# list of files for each city
data_files = ['./data/NYC-CitiBike-2016.csv',
              './data/Chicago-Divvy-2016.csv',
              './data/Washington-CapitalBikeshare-2016.csv',]

# print the first trip from each file, store in dictionary
ex_trips = {}
for data_file in data_files:
    city, first_trip = print_first_point(data_file)
    ex_trips[city] = first_trip




def duration_in_mins(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the trip duration in units of minutes.
    
    Remember that Washington is in terms of milliseconds while Chicago and NYC
    are in terms of seconds. 
    
    HINT: The csv module reads in all of the data as strings, including numeric
    values. You will need a function to convert the strings into an appropriate
    numeric type when making your transformations.
    see https://docs.python.org/3/library/functions.html
    """
    
    if city == 'Washington':
        duration = float(datum['Duration (ms)'])/(1000*60)
    elif city == 'Chicago':
        duration = float(datum['tripduration'])/60
    elif city == 'NYC':
        duration = float(datum['tripduration'])/60
    
    return duration
    

    

# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': 13.9833,
         'Chicago': 15.4333,
         'Washington': 7.1231}

for city in tests:
    assert abs(duration_in_mins(ex_trips[city], city) - tests[city]) < .001



def time_of_trip(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the month, hour, and day of the week in
    which the trip was made.
    
    Remember that NYC includes seconds, while Washington and Chicago do not.
    
    HINT: You should use the datetime module to parse the original date
    strings into a format that is useful for extracting the desired information.
    see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    """
    if city == 'Washington':
        str_to_date = datetime.strptime(datum['Start date'],"%m/%d/%Y %H:%M")
        month = str_to_date.month
        hour = str_to_date.hour
        day_of_week = str_to_date.strftime("%A")
    elif city == 'Chicago':
        str_to_date = datetime.strptime(datum['starttime'],"%m/%d/%Y %H:%M")
        month = str_to_date.month
        hour = str_to_date.hour
        day_of_week = str_to_date.strftime("%A")
    elif city == 'NYC':
        str_to_date = datetime.strptime(datum['starttime'],"%m/%d/%Y %H:%M:%S")
        month = str_to_date.month
        hour = str_to_date.hour
        day_of_week = str_to_date.strftime("%A")
    
    return (month, hour, day_of_week)



# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': (1, 0, 'Friday'),
         'Chicago': (3, 23, 'Thursday'),
         'Washington': (3, 22, 'Thursday')}

for city in tests:
    assert time_of_trip(ex_trips[city], city) == tests[city]



def type_of_user(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the type of system user that made the
    trip.
    
    Remember that Washington has different category names compared to Chicago
    and NYC. 
    """
    
    if city == 'Washington':
        user_type = datum['Member Type']
        if user_type == 'Registered':
            user_type = 'Subscriber'
        else:
            user_type = 'Customer'
    elif city == 'Chicago':
        user_type = datum['usertype']
    elif city == 'NYC':
        user_type = datum['usertype']

    return user_type



# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': 'Customer',
         'Chicago': 'Subscriber',
         'Washington': 'Subscriber'}

for city in tests:
    assert type_of_user(ex_trips[city], city) == tests[city]



def condense_data(in_file, out_file, city):

    """
    This function takes full data from the specified input file
    and writes the condensed data to a specified output file. The city
    argument determines how the input file will be parsed.
    """
    
    with open(out_file, 'w') as f_out, open(in_file, 'r') as f_in:
        # set up csv DictWriter object - writer requires column names for the
        # first row as the "fieldnames" argument
        out_colnames = ['duration', 'month', 'hour', 'day_of_week', 'user_type']        
        trip_writer = csv.DictWriter(f_out, fieldnames = out_colnames)
        trip_writer.writeheader()
        
        ## TODO: set up csv DictReader object ##
        trip_reader = csv.DictReader(f_in)
        
        # collect data from and process each row
        for row in trip_reader:
            # set up a dictionary to hold the values for the cleaned and trimmed
            # data point
            new_point = {}
            datelist = []
            
            city = in_file.split('-')[0].split('/')[-1]
            
            for row in trip_reader:
                first_trip = row
                break

            ## TODO: use the helper functions to get the cleaned data from  ##
            ## the original data dictionaries.                              ##
            ## Note that the keys for the new_point dictionary should match ##
            ## the column names set in the DictWriter object above.         ##
            
            new_point['duration'] = duration_in_mins(first_trip, city)
            
            datelist = time_of_trip(first_trip, city)
            
            new_point['month'] = datelist[0]
            new_point['hour'] = datelist[1]
            new_point['day_of_week'] = datelist[2]
            
            new_point['user_type'] = type_of_user(first_trip, city)
            

            ## TODO: write the processed information to the output file.     ##
            ## see https://docs.python.org/3/library/csv.html#writer-objects ##
            
            with open(out_file, 'a', newline='') as f:
                w = csv.writer(f)
                    
                #w.writerow(new_point.keys())
                w.writerow(new_point.values())



# Run this cell to check your work
city_info = {'Washington': {'in_file': './data/Washington-CapitalBikeshare-2016.csv',
                            'out_file': './data/Washington-2016-Summary.csv'},
             'Chicago': {'in_file': './data/Chicago-Divvy-2016.csv',
                         'out_file': './data/Chicago-2016-Summary.csv'},
             'NYC': {'in_file': './data/NYC-CitiBike-2016.csv',
                     'out_file': './data/NYC-2016-Summary.csv'}}

for city, filenames in city_info.items():
    print_first_point(filenames['out_file'])
    condense_data(filenames['in_file'], filenames['out_file'], city)



def number_of_trips(filename):
    """
    This function reads in a file with trip data and reports the number of
    trips made by subscribers, customers, and total overall.
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        reader = csv.DictReader(f_in)
        
        # initialize count variables
        n_subscribers = 0
        n_customers = 0
        tot_sub_time = 0
        tot_cust_time = 0
        prop_sub = 0
        prop_cust = 0
        
        # tally up ride types
        for row in reader:
            if row['user_type'] == 'Subscriber':
                n_subscribers += 1
                tot_sub_time += float(row['duration'])
            else:
                n_customers += 1
                tot_cust_time += float(row['duration'])
        
        # compute total number of rides
        n_total = n_subscribers + n_customers
        
         # calculate percentage of subscribers vs customers
        prop_sub = 100*n_subscribers/(n_total)
        prop_cust = 100*n_customers/(n_total)
        avg_sub_time = tot_sub_time/n_subscribers
        avg_cust_time = tot_cust_time/n_customers
        
        # return tallies as a tuple
        return(n_subscribers, n_customers, n_total, prop_sub, prop_cust, avg_sub_time, avg_cust_time)



## Modify this and the previous cell to answer Question 4a. Remember to run ##
## the function on the cleaned data files you created from Question 3.      ##

data_file = './data/Washington-2016-Summary.csv'
#print('Washington:', number_of_trips(data_file))
print('Washington, {}').format(number_of_trips(data_file))

data_file = './data/Chicago-2016-Summary.csv'
#print('Chicago:', number_of_trips(data_file))
print('Chicago, {}').format(number_of_trips(data_file))

data_file = './data/NYC-2016-Summary.csv'
#print('NYC:', number_of_trips(data_file))
print('NYC, {}').format(number_of_trips(data_file))

#data_file = './examples/BayArea-Y3-Summary.csv'
#print('BayArea:', number_of_trips(data_file))



## Use this and additional cells to answer Question 4b.                 ##
##                                                                      ##
## HINT: The csv module reads in all of the data as strings, including  ##
## numeric values. You will need a function to convert the strings      ##
## into an appropriate numeric type before you aggregate data.          ##
## TIP: For the Bay Area example, the average trip length is 14 minutes ##
## and 3.5% of trips are longer than 30 minutes.                        ##
def trip_duration(filename):

    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)
        
        avg_trip_time = 0
        count_over30 = 0
        count_under30 = 0
        total_duration = 0
        
        for row in reader:
            total_duration += float(row['duration'])
            
            if float(row['duration']) > 30:
                count_over30 += 1
            else:
                count_under30 += 1
                
        count_total = count_over30 + count_under30
        prop_over30 = 100*count_over30/(count_total)
        prop_under30 = 100*count_under30/(count_total)
        avg_trip_time = total_duration/count_total
        
        return(prop_over30, prop_under30, avg_trip_time)



data_file = './data/Washington-2016-Summary.csv'
print('Washington:', trip_duration(data_file))

data_file = './data/Chicago-2016-Summary.csv'
print('Chicago:', trip_duration(data_file))

data_file = './data/NYC-2016-Summary.csv'
print('NYC:', trip_duration(data_file))

#data_file = './examples/BayArea-Y3-Summary.csv'
#print('BayArea:', trip_duration(data_file))



## Use this and additional cells to answer Question 4c.                ##
##                                                                     ##
## TIP: For the Bay Area example data, you should find the average     ##
## Subscriber trip duration to be 9.5 minutes and the average Customer ##
## trip duration to be 54.6 minutes. Do the other cities have this     ##
## level of difference?                                                ##

data_file = './data/Washington-2016-Summary.csv'
print('Washington:', number_of_trips(data_file)[5:7])

data_file = './data/Chicago-2016-Summary.csv'
print('Chicago:', number_of_trips(data_file)[5:7])

data_file = './data/NYC-2016-Summary.csv'
print('NYC:', number_of_trips(data_file)[5:7])



# load library
import matplotlib.pyplot as plt

# this is a 'magic word' that allows for plots to be displayed
# inline with the notebook. If you want to know more, see:
# http://ipython.readthedocs.io/en/stable/interactive/magics.html
%matplotlib inline 

# example histogram, data taken from bay area sample
data = [ 7.65,  8.92,  7.42,  5.50, 16.17,  4.20,  8.98,  9.62, 11.48, 14.33,
        19.02, 21.53,  3.90,  7.97,  2.62,  2.67,  3.08, 14.40, 12.90,  7.83,
        25.12,  8.30,  4.93, 12.43, 10.60,  6.17, 10.88,  4.78, 15.15,  3.53,
         9.43, 13.32, 11.72,  9.85,  5.22, 15.10,  3.95,  3.17,  8.78,  1.88,
         4.55, 12.68, 12.38,  9.78,  7.63,  6.45, 17.38, 11.90, 11.52,  8.63,]
plt.hist(data)
plt.title('Distribution of Trip Durations')
plt.xlabel('Duration (m)')
plt.show()



## Use this and additional cells to collect all of the trip times as a list ##
## and then use pyplot functions to generate a histogram of trip times.     ##

def getlist(filename):
    
    Citydata = []
    Subdata = []
    Custdata = []

    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)
        
        for row in reader:
            Citydata.append(round(float(row['duration']),2))
            
            if row['user_type'] == 'Subscriber':
                Subdata.append(round(float(row['duration']),2))
            elif row['user_type'] == 'Customer':
                Custdata.append(round(float(row['duration']),2))
        
    return Citydata, Subdata, Custdata

data_file = './data/Washington-2016-Summary.csv'
#print('Washington:', getlist(data_file))
    
plt.hist(getlist(data_file)[0])
plt.title('Distribution of Trip Durations')
plt.xlabel('Duration (m)')
plt.show()



## Use this and additional cells to answer Question 5. ##
plt.hist(getlist(data_file)[1], range=(0, 75))
plt.title('Distribution of Subscriber Trip Durations')
plt.xlabel('Duration (m)')
plt.axis([0, 75, 0, 15000])
plt.grid(True)
plt.show()


plt.hist(getlist(data_file)[2],range=(0, 75))
plt.title('Distribution of Customer Trip Durations')
plt.xlabel('Duration (m)')
plt.axis([0, 75, 0, 2000])
plt.grid(True)
plt.show()



## Use this and additional cells to continue to explore the dataset. ##
## Once you have performed your exploration, document your findings  ##
## in the Markdown cell above.                                       ##

def getMonth(filename):
    
    Submon = []
    Custmon = []

    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)
        
        for row in reader:
            
            if row['user_type'] == 'Subscriber':
                Submon.append(row['month'])
            elif row['user_type'] == 'Customer':
                Custmon.append(row['month'])
        
    return Submon, Custmon



def getDay(filename):
    
    Subday = []
    Custday = []

    with open(filename, 'r') as f_in:
        reader = csv.DictReader(f_in)
        
        for row in reader:
            
            if row['user_type'] == 'Subscriber':
                Subday.append(row['day_of_week'])
            elif row['user_type'] == 'Customer':
                Custday.append(row['day_of_week'])
        
    return Subday, Custday



data_file = './data/Washington-2016-Summary.csv'
#print('Washington:', getlist(data_file))

plt.hist(getMonth(data_file)[0],bins=24)
plt.title('Distribution of Subscriber Usage by Month')
plt.xlabel('Month')
plt.axis([0, 12, 0, 15000])
plt.grid(True)
plt.show()

plt.hist(getDay(data_file)[0],bins=14)
plt.title('Distribution of Subscriber Usage by Day')
plt.xlabel('Day')
plt.axis([0, 7, 0, 5000])
plt.grid(True)
plt.show()

plt.hist(getMonth(data_file)[1],bins=24)
plt.title('Distribution of Customer Usage by Month')
plt.xlabel('Month')
plt.axis([0, 12, 0, 5000])
plt.grid(True)
plt.show()

plt.hist(getDay(data_file)[1],bins=14)
plt.title('Distribution of Customer Usage by Day')
plt.xlabel('Day')
plt.axis([0, 7, 0, 2000])
plt.grid(True)
plt.show()
