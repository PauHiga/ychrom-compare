def report(sample, matches, NDmatches):
  if matches + NDmatches >= 20:
    return [f"{matches}{NDmatches}", f"{sample} matches the provided pattern with {matches + NDmatches} coincidences, with {NDmatches} ND (not determined)"]