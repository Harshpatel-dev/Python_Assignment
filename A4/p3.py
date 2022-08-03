# w+ : Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

import os
import csv

directory = "output"
  
# Parent Directory path
parent_dir = "D:\D-48 Harsh Patel\A4"

path = os.path.join(parent_dir, directory)

if(os.path.exists(path) == False):
    os.mkdir(path)

print(path)

single_file = open(f"{path}\single.csv", 'w+')
return_file = open(f"{path}\\return.csv", 'w+')

with open('D:\D-48 Harsh Patel\A4\MET_Office_2011_Air_Data.csv' , mode='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
  single_writer = csv.writer(single_file)
  return_writer = csv.writer(return_file)

  # displaying the contents of the CSV file
  for i , lines in enumerate(csvFile):
        if i>0:
            if lines[5] == "Single":
                    single_file.write(f"{line}\n")
            else:
                for line in lines:
                    return_file.write(f"{line}\n")

single_file.close()
return_file.close()


