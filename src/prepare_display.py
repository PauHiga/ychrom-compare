def process(report):
  raw_not_processed = report[1]
  raw_results = report[0]
  samples_analyzed = report[2]

  raw_results.sort(key=lambda x: x[0], reverse=True)

  string_report = '\n'.join(item[1] for item in raw_results)

  not_processed_report = ''
  if len(raw_not_processed)>0:
    not_processed = ''.join(raw_not_processed)
    not_processed_report = 'The following samples could not be processed:\n' + not_processed + "Please make sure that all the markers for each sample are presented in a single table. Verify that the samples' names are written exactly the same in each row, and there are no samples' names repeated.\n\n"

  if not_processed_report != '' and len(raw_results) > 0:
    report = f"{samples_analyzed} samples analyzed.\n\n" + not_processed_report  + "\n ------------ Matches found sorted by number of coincidences ------------\n\n(Asterisks * are evaluated as ND)\n\n\n" + string_report

  elif samples_analyzed == 0:
    report = f"No samples to compare were found in this file."

  else:
    report = f"No coincidences found in {samples_analyzed} samples analyzed."

  return report
