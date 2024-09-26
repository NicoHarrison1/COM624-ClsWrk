import csv
import statistics
from fileinput import filename
from statistics import median

# The median is the middle
# add and divide for the mean
# mode is the one you see the most
# range is the difference between

data_list = []
headings = []
filename = 'titanic_samples.csv'

with open(filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    headings = next(csv_reader)

    for row in csv_reader:
        data_list.append(row)

    csvfile.close()

print(data_list)

# Looking for missing age
list_of_ages = []
median_age = 0

for passenger in data_list:

    # calculating the median age

    if passenger[1] != '':
        list_of_ages.append(float(passenger[1]))

    # sort the list (smallest to greatest)
    list_of_ages.sort()

# finding the median value
median_age = statistics.median(list_of_ages)
print(median_age, "MEDIAN AGE")


# Adding median age to data column field -----------------------------------

for passenger in data_list:

    if passenger[1] == '':
        passenger[1] = median_age

# Writing final data back to file -----------------------
cleaned_file = 'titanic_cleaned.csv'

with open(cleaned_file, 'w', newline="") as file:
    csvwriter = csv.writer(file)  # 2. create a csvwriter object
    csvwriter.writerow(headings)  # 4. write the header
    csvwriter.writerows(data_list)

    file.close()

