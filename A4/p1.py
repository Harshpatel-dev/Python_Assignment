import csv
from collections import OrderedDict

sum = 0.0
airCar_dic = {}
# opening the CSV file
with open('MET_Office_2011_Air_Data.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)

  # displaying the contents of the CSV file
  for i , lines in enumerate(csvFile):
        if i>0:
            sum = sum + float(lines[1])
            if(airCar_dic.get(lines[11]) == None):
                airCar_dic[lines[11]] = float(lines[3])
            else:
                airCar_dic[lines[11]] += float(lines[3])
   
print("Total cost of all tickets : " , sum)

aircarrier_cost = dict(sorted(airCar_dic.items(),key=lambda item : item[1]))

for i , (k, v) in enumerate(aircarrier_cost.items()):
    print(k, v)



