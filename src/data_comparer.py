def report(sample, matches, NDmatches, no_matches):
  if matches + NDmatches >= 20 and matches>0 and no_matches<2:
    return [matches, f'The sample "{sample}" matches the provided pattern with: \n{matches} coincidences\n{NDmatches} ND (not determined)\n{no_matches} not coincidences\n']
  else:
    pass

def compare(sample, docx, user_sample):
  matches = 0
  NDmatches = 0
  no_matches = 0
  for key in docx:
    if key != 'MUESTRA':
      docx_list = docx[key].split('/')
      user_list = user_sample[key].split('/')
      coincidences = set(docx_list).intersection(user_list)
      if key == 'DYS385A/B' and (len(docx_list) == 2 or len(user_list) == 2):
        if len(coincidences) >= 2:
          matches = matches + 1
        elif any('ND' in item for item in (docx_list + user_list)):
          NDmatches = NDmatches + 1
        else: 
          no_matches = no_matches + 1
      else:
        if len(coincidences) >= 1:
          matches = matches + 1
        elif any('ND' in item for item in (docx_list + user_list)):
          NDmatches = NDmatches + 1
        else: 
          no_matches = no_matches + 1

  return report(sample, matches, NDmatches, no_matches)