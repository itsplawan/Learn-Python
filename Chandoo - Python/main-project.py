from datetime import date
import csv

#This opens the CSV file
filename = "I:/Python/Chandoo - Python/test.csv"

#This obtains the date from datetime library.
dt = date.today()
#This converts the today's date into a format that will be compaitable with CSV.
dt2 = dt.strftime("%d/%m/%Y")

exp = []
stopped = False
#Opens the file and that "w" makes it a writable file. If it is opened in "a" mode, it is in append mode and will add data instead of erasing and starting over.
with open(filename,"a") as file:
    csvwriter = csv.writer(file) #csv.writer is activated to write the data into the file.
    while not stopped:
        e = int(input('Enter your expenses (Enter 0 to stop): ')) #Takes expenses data from the user.
        if e == 0:
            stopped = True
        else:
            csvwriter.writerow([dt2,e]) #Inserts each new data entered by the user into a row in the CSV.
            exp.append(e)
file.close()
