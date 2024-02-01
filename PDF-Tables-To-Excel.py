import tabula
import pandas as pd

# Replace 'your_file.pdf' with the actual path to your PDF file
pdf_path = 'your_file.pdf'

# Extract tables from the PDF
tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

# Convert each table to a DataFrame and store in a list
dfs = [pd.DataFrame(table) for table in tables]

# Save each DataFrame to a separate sheet in an Excel file
with pd.ExcelWriter('output_excel_file.xlsx', engine='xlsxwriter') as writer:
    for i, df in enumerate(dfs):
        df.to_excel(writer, sheet_name=f'Sheet_{i + 1}', index=False)
