#!/usr/bin/python2

import pandas as pd
#read a CSV file 
df_data = pd.read_csv(sys.argv)

#delete space
#this commands removes the spaces  column names
df_data.coloumns = df_data.columns.str.strip()
#these below commands remove spaces from each cell in the mentioned column
df_data[‘Lane’].str.strip()
df_data[‘Sample_ID’].str.strip()
df_data[‘Index’].str.strip()
df_data[‘Project_ID’].str.strip()
df_data[‘Index’] ].str.strip()

#replace "+" with "P"
df_data[‘Sample_ID’].str.replace(‘+’, ‘P’)
#replace other special characters with "_"

df_data= df_data.replace(r’[^0-9a-zA-Z ]’.’_’, regex= True, inplace= True)


# check if duplicated rows are included in the CSV file
df_data.duplicated()
df_data(subset[‘Sample_ID’]
#if there are duplicated rows, print error message indicating that duplicated rows are detected
#if no duplicated rows, save the modified file as its original name and print message indicating samplesheet looks good.

        
        If len(df)__!= len(df_data.drop_duplicates()):
        print(“ERROR: Duplicated rows detected”)
        else
        df_data.to_csv(“input.csv”)
        print(“Samplesheet looks good.”)




#function to count adenines on string of DNA; if >15 print good; else print Bad
def count(seq):
    num_A = seq.count('A')
    if num_A > 15:
        print('Good!')
        return num_A
    else:
        print('Bad!')
        return 0

count(“GTCAGCTAAATGCAAACACAAGAAC”)
