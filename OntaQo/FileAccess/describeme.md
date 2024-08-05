# Files-Access Program

## Introduction
import csv

# Define program variables
records_list = []
record_count = 0

# Read customer information from a text file
input_file = 'customer_data.txt'

# Define a file handle and open your text data file for reading.
with open(input_file, 'r') as file:
    for line in file:
        records_list.append(line.strip())

# Append the new customer record
new_record = "5,Brady,Bobby,4222 Clinton Way,Los Angeles,CA"
records_list.append(new_record)

# Open a new csv file for writing and name it databaseSheet
output_file = 'databaseSheet.csv'
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header
    writer.writerow(["Customer ID", "Last Name", "First Name", "Address", "City", "State", "Promo Credit"])
    
    # Process the list data
    for record in records_list:
        fields = record.split(',')
        fields.append("$500")
        writer.writerow(fields)
        record_count += 1

# Print the record count
print(f"There were {record_count} records written to the promo credits csv file.")


# Defining Program Variables
filePath = 'data.txt' # C:\Users\Administrator\PycharmProjects\Natsu-1\OntaQo\FileAccess
records = []

record_count = 0

def read_txt(filePath):
    """
        * This code snippet reads contents of the .txt file && returns a list of records.
        * Parameters:
            1. filePath(str): The path to the file.
        * Returns a list, the content of the file in lists of records.
    
    """
    try:
        with open(filePath, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
        return lines
    
    except Exception as e:
        print(f"An error occured: {e}")
        return None

# Read records from the file
records =read_txt(filePath)

#Initialize the record count
if records:
    record_count = len(records)

# Print Out the Outputs.
print("Records:", records)
print("Record Count:", record_count)
