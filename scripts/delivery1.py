import pandas as pd
import numpy as np
import datetime

import random
random.seed(a=42)

from faker import Faker
Faker.seed(42)
fake = Faker('en_UK')


#############
# generate data row by row
#############

def create_row(num=1):
    output = [{"Resident_ID": random.sample(range(10**18, ((10**19)-1)),1)[0],
              'Household_ID': None,
              'CE_ID': None,
              'First_Name': fake.first_name(),
              'Middle_Name': None,
              'Last_Name': fake.last_name(),
              'date_time_obj': fake.date_between_dates(date_start=datetime.date(1904, 1, 1),
                                                       date_end=datetime.date(2019, 12, 31)),
              'Country_Of_Birth':None,
              'Country_Of_Birth_UK':None,
              'Sex':None,
              'Marital_Status':None,
              'Marital_Status_CCS':None,
              'Residence_Type':None,
              'Ethnic Group (five category)':None,
              'Ethnicity: Tick Box':None,
              'Alternative_Address_Type':None,
              'Alternative_Address_Indicator':None,
              'Alternative_Address':None,
              'Alternative_Address_Postcode':None,
              'Alternative_Address_Country':None,
              'Alternative_Address_OA':None,
              'Alternative_Address_UPRN':None,
              '1_Year_Ago_Address_Type':None,
              '1_Year_Ago_Address':None,
              '1_Year_Ago_Address_Postcode':None,
              '1_Year_Ago_Address_Country':None,
              '1_Year_Ago_Address_OA':None,
              '1_Year_Ago_Address_UPRN':None,
              'Workplace_Type':None,
              'Workplace_Address':None,
              'Workplace_Address_Postcode':None,
              'Workplace_Address_Country':None,
              'Workplace_Address_UPRN':None,
              'Activity Last Week':None,
              'In_Full_Time_Education':None,
              'Is_HH_Term_Time_Address':None,
              'Armed Forces Indicator':None,
              'SIC':None,
              'SOC':None,
              'Census Return Method':None} for x in range(num)]
    return output


person_index_df = pd.DataFrame(create_row(num=10))

############
# date of birth from object
############

def calculate_age_on_31_12_2019(born):
    today = datetime.date(2019, 12, 31)
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

person_index_df['Resident_Day_Of_Birth'] = person_index_df['date_time_obj'].apply(lambda x: x.day)
person_index_df['Resident_Month_Of_Birth'] = person_index_df['date_time_obj'].apply(lambda x: x.month)
person_index_df['Resident_Year_Of_Birth'] = person_index_df['date_time_obj'].apply(lambda x: x.year)
person_index_df['Resident_Age'] = person_index_df['date_time_obj'].apply(calculate_age_on_31_12_2019)
person_index_df['full_DOB'] = person_index_df['date_time_obj'].apply(lambda x: x.strftime("%d%m%Y"))
person_index_df = person_index_df.drop('date_time_obj', axis = 1)


#######
### CHECK
#######

print(person_index_df.head())

#####
# Save file 
#####

person_index_df.to_csv('../output/person_index.csv')