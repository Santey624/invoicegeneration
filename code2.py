from docxtpl import DocxTemplate
import pandas as pd
import csv
from datetime import datetime, timedelta

csv_file = 'siddhartha1.csv'
df = pd.read_csv(csv_file)

column_names = ["invoice", 'date', 'duedate', 'taxamount', 'vatvalue', 'total', 'amountinwords','codename','itemname','rate','amount']

# Check if all column_names exist in the DataFrame
missing_columns = [col for col in column_names if col not in df.columns]

if missing_columns:
    print(f"The following columns do not exist in the DataFrame: {', '.join(missing_columns)}")
else:
    # Create a dictionary with the specified columns as keys and their corresponding data as values
    data = {col: df[col].tolist() for col in column_names}

    # Print or use the data as needed
    print(data)

doc = DocxTemplate("imarkdigitalquatation.docx")
context = data  # Use the data dictionary
doc.render(context)
doc.save("generated1_doc.docx")
