import pandas as pd
from delivery1 import *
from delivery2 import *

code_list = pd.read_csv('../data/possible_codes.csv')


###
# Resident, house and CE indices
###
person_index_df = pd.DataFrame(create_row_resident(num=3000, code_list = code_list))
person_index_df = split_DOB(person_index_df)

house_index_df = pd.DataFrame(create_row_house(num=500, code_list =  code_list))

ce_index_df = pd.DataFrame(create_row_CE(num=50, code_list =  code_list))


#######
### CHECK
#######

print(house_index_df.head())

#######
### Put people in houses 
########

person_index_df = generate_house_for_person(person_index_df, house_index_df, ce_index_df)
######

# assign residence type 
person_index_df['Residence_Type'] = person_index_df['Household_ID'].apply(assign_residence_type)

# Common last names 
person_index_df = common_surnames_in_house(person_index_df)


####
### Join addresses 
####

#person_index_df = join_to_populate_addresses(person_index_df, house_index_df)

#print(person_index_df.head())
#print(person_index_df.tail())
#print(person_index_df[['Household_ID','Last_Name']].head(10))
#print(person_index_df[['Household_ID','Last_Name']].tail(10))


#####
# duplicate for CCS with modified ID's
#####

ccs_people, ccs_house, ccs_ce = CCS_scramble(person_index_df, house_index_df, ce_index_df)

#####
# Create relationships from census table
#####

census_relationships = generate_relationships(person_index_df)


#####
# Save files
#####

person_index_df.to_csv('../output/census_residents.csv', index = False)
house_index_df.to_csv('../output/census_households.csv', index = False)
ce_index_df.to_csv('../output/census_ce.csv', index = False)
census_relationships.to_csv('../output/census_relationships.csv', index = False)
ccs_people.to_csv('../output/ccs_residents.csv', index = False)
ccs_house.to_csv('../output/ccs_households.csv', index = False)
ccs_ce.to_csv('../output/ccs_ce.csv', index = False)