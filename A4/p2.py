import csv
from itertools import count

def find_journey_cost(file):
    journey_dest = input("Enter journey finish point : ")
    csvFile = csv.reader(file)
    sum=0
    count = 0
    for i,val in enumerate(csvFile):
         if i>0:
            if(val[10]==journey_dest):
                x=(float)(val[3])
                count += 1
                sum=sum+x
    print("Cost for all journeys with ",journey_dest," is >> ",sum)
    print("Average cost for all the journeys with ",journey_dest," finishing point : ",round(sum/count,2))
            

with open('Met_office_2011_Air_Data.csv') as file:
    find_journey_cost(file)
  