from docx import Document
from . import normalize_data
from src import data_comparer

def process(document_path, user_sample):
    document = Document(document_path)
    tables = document.tables

    processed_samples = 0
    coincidences_messages = []
    samples_not_processed = []

    for table in tables:
        table_headers = []
        table_samples_values = []
        raw_docxrows = [[cell.text.strip().replace("\n", "").upper() for cell in row.cells] for row in table.rows]

        first_column_values = set(cell.text.strip().replace("\n", "").upper() for cell in table.columns[0].cells)   

        first_marker_in_header = table.rows[0].cells[1].text.strip().replace("\n", "").upper()

        column_values_list = list(first_column_values)
        
        for i in range(len(column_values_list)):
            full_row = []
            for item in raw_docxrows:
                if column_values_list[i] in item:
                    item.remove(column_values_list[i])
                    full_row.extend(list(filter(None, item)))

            full_row_complete = [column_values_list[i]]
            full_row_complete.extend(full_row)

            if first_marker_in_header in full_row_complete:
                table_headers = tuple(full_row_complete)
            else:    
                table_samples_values.append(tuple(full_row_complete))
        if 'DYS389II' in table_headers:
          for sample_values in table_samples_values:
              if len(sample_values) != 23:
                  samples_not_processed.append(f"{sample_values[0]}\n")
              else:
                  data = {table_headers[i]:sample_values[i] for i in range(len(table_headers))}
                  docx_data = normalize_data.normalize_data(data)
                  user_data = normalize_data.normalize_data(user_sample)
                  message = (data_comparer.compare(data['MUESTRA'], docx_data, user_data))
                  if message:
                    coincidences_messages.append(message)
          processed_samples = processed_samples + len(table_samples_values)

    return [coincidences_messages, samples_not_processed, processed_samples]