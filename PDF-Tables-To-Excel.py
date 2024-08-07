import camelot
import pandas as pd
import cv2  # Add this line

# Replace 'your_file.pdf' with the actual path to your PDF file
pdf_path = "C:/Users/Willi/Downloads/OneDrive_1_01-02-2024/Second counterclaim defendant's affidavit of documents.pdf"

# Extract tables from the PDF
tables = camelot.read_pdf(pdf_path, flavor='stream', pages='all')

# Save each table to a separate sheet in an Excel file
with pd.ExcelWriter("C:/Users/Willi/Downloads/OneDrive_1_01-02-2024/Second counterclaim defendant's affidavit of documents.xlsx", engine='openpyxl') as writer:
    for i, table in enumerate(tables):
        df = table.df
        df.to_excel(writer, sheet_name=f'Sheet_{i + 1}', index=False)
