import pandas as pd
import delivery1 as d

code_list = pd.read_csv('../data/possible_codes.csv')


###
# Resident_index
###
person_index_df = pd.DataFrame(d.create_row_resident(num=3000, code_list =  code_list))
person_index_df = d.split_DOB(person_index_df)

###
# House_index
###
house_index_df = pd.DataFrame(d.create_row_house(num=500, code_list =  code_list))

###
# CE_index
###
ce_index_df = pd.DataFrame(d.create_row_CE(num=50, code_list =  code_list))


#######
### CHECK
#######

#######
### Put people in houses 
########

person_index_df = d.generate_house_for_person(person_index_df, house_index_df, ce_index_df)
######

print(person_index_df.head())

# assign residence type 
person_index_df['Residence_Type'] = person_index_df['Household_ID'].apply(d.assign_residence_type)


print(person_index_df['Residence_Type'].head())
print(person_index_df['Residence_Type'].tail())
print(person_index_df.tail())
#print(ce_index_df.head())

#####
# Create relationships from census table
#####

census_relationships = d.generate_relationships(person_index_df)


#####
# Save file
#####

person_index_df.to_csv('../output/person_index.csv')
house_index_df.to_csv('../output/house_index.csv')
ce_index_df.to_csv('../output/ce_index.csv')
census_relationships.to_csv('../output/census_relationships.csv')


########
## Make a big table of everything 
########

# Easy to asign house to a person and then join after 

