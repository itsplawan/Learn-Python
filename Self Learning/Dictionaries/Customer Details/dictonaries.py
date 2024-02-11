import pandas as pd
import os

running = True

filename = "Self Learning\Dictionaries\Customer Details\Customer Details.csv"

with open(filename, "a") as output_file:
    while running:
        f_name = str(input('Enter the first name: '))
        m_name = str(input('Enter the middle name: '))
        l_name = str(input('Enter the last name: '))
        age = int(input('Enter the age: '))
        city = str(input('Enter the city: '))
        customer_details = {
            "First Name": [f_name],
            "Middle Name": [m_name],
            "Last Name": [l_name],
            "Age": [age],
            "City": [city]
        }
        cd_data = pd.DataFrame(customer_details)
#Line 23 to line 29 is code helped by ChatGPT and I still have to learn this.
        
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
        # File is not empty, append data without headers
            
            cd_data.to_csv(filename, mode='a', index=True, header=False)
        else:
        # File is empty or doesn't exist, write headers
            cd_data.to_csv(filename, mode='a', index=True, header=True)

        loop_test = input('Do you want to add another customer? (Y)es/(N)o: ')
        if loop_test.upper() != "Y":
            running = False
