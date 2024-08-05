import os
import csv

# Program-Variables
records_list = []
record_count = 0


 
with open("C:/Users/Administrator/PycharmProjects/Natsu-1/OntaQo/FileAccess/data.txt", "r+") as file:
    for line in file:
        records_list.append(line.strip())
        
# Appending new record
new_record = "5,Brady,Bobby,4222 Clinton Way,Los Angeles,CA"
records_list.append(new_record)

# Open a new csv file
with open("databaseSheet.csv", "w", newline='') as csvfile:
    writer=csv.writer(csvfile)
    
    #Writing-the-heading
    writer.writerow(["Customer ID","Last Name","First Name","Address","City","State","Promo Credit"])
    
    # Process-List-data
    for record in records_list:
        fields=record.split(",")
        fields.append("$500")
        writer.writerow(fields)
        record_count += 1
        
    print(f"There were {record_count} records written to the promo credits csv file")