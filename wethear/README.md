Pandas library is used to process dataset

1. Reading csv file and naming each column using pandas
2. writing programs for each questions

Methodology:
Q1) What is the range of dates in the dataset?
    a) min() is used in date column to get oldest date
    b) max() is used in date column to get latest date
    c) showing the result

Q2) How many countries are included in the dataset?
    a) nunique() function of pandas is used to get total number of distinct entries present in countries column.
    b) printed the result

Q3) What is the coldest day ever recorded in Toronto? How cold was it?
    a) rows containing Toronto as city is extracted and a subdata is created
    b) minimum temperature is extracted from sub data using min()
    b) coldest row(s) are extracted by comparing temperature in the subdata and minimum temperature.
    c) date(s) present in coldest row(s) are the date of days in toronto's coldest days.

Q4) What is the snowfall total for Denver in 2014?
    a) rows containing Denver as city is extracted and a sub dataset is created
    b) from the sub dataset obtained, again another sub dataset is created with rows in which the year is 2014
    c) to extract year from date DatetimeIndex function of pandas is used
    d) sum of all the snowfall data is taken to get the total snowfall.

Q5) What are the top 5 rainiest cities in 2018? How much rain did each receive? Assume rain to be the amount of total precipitation minus any snowfall.
    a) dataset of year 2018 is extracted from given dataset
    b) a column of rain is added in the extracted dataset 
    c) values of rain column is nothing but total precipitation minus any snowfall
    d) dataset is then sorted by rain values in decending order
    e) top 5 rows is then selected from the sorted dataset to get the most rainiest cities of 2018

Q6) How many days in each month of 2019 did Olympia, Washington see some sort of precipitation falling?
    a) dataset of year 2019 is extracted from given dataset
    b) dataset of washington state is extracted from new dataset
    c) dataset of Olympia city is extracted from washington's dataset
    d) a dictionary is created with 12 months with each count = 0
    e) iterating through each row of final dataset obtained until dataset is empty
    f) if precipitation falling is not equal to zero then increment the count of respective month
    g) month can be obtained by using datetimeindex function of pandas
