import pandas as pd
import numpy as np

#laod into dataframe
file_path = (r'C:\Users\LENOVO\PycharmProjects\internproject2\excelreport.xlsx')

# Read the Excel file into a DataFrame
data = pd.read_excel(file_path)

selected_row=data.iloc[0]
print(selected_row)

# Create a dictionary with the data
data_dict = selected_row

# Create a DataFrame from the dictionary
df = pd.DataFrame(data_dict).T   #here T determines that the rows are transposed into columns

# Save the DataFrame to a CSV file
output_csv_path =r'C:\Users\LENOVO\PycharmProjects\internproject2\siddhartha1.csv'
df.to_csv(output_csv_path)

print("CSV file saved successfully.")

