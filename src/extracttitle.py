import re

def extract_title(md):
  title = re.findall(r"^# .*", md.lstrip())
  if len(title) == 0:
    raise Exception("no title found")
  return title[0].replace("# ", "").rstrip().lstrip()
