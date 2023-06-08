def normalize_data (unprocessed_data):
    processed_data = {}
    for key in unprocessed_data:
      value = unprocessed_data[key].upper().replace("*", "/ND/").replace(', ', '/').replace(' ', '/').replace('-', '/').replace('//', '/').strip('/').replace(',', '.')
      processed_data[key] = value
    return processed_data 