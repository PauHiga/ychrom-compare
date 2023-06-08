import re

def validate(user_input):
  normalized_input = user_input.upper().strip().replace("*", "/ND/").replace(', ', '/').replace('-', '/').replace('//', '/').strip('/').replace(',', '.')
  match = re.match(r'^\d{1,2}(\.\d{1})?(\/\d{1,2}(\.\d{1})?)*$|^ND$', normalized_input)
  return match