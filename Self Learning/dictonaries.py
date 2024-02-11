import pandas as pd

running = True

filename = "Customer Details.csv"

with open(filename, "a") as output_file:
    while running:
        f_name = str(input('Enter the first name: '))
        m_name = str(input('Enter the middle name: '))
        l_name = str(input('Enter the last name: '))
        age = int(input('Enter the age: '))
        city = str(input('Enter the city: '))
        customer_details = {
            "First Name" : f_name,
            "Middle Name" : m_name,
            "Last Name" : l_name,
            "Age" : age,
            "City" : city
        }
        cd_data = pd.DataFrame(customer_details)
        
