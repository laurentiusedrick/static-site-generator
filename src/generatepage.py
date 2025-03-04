from markdowntohtmlnode import markdown_to_html_node
from extracttitle import extract_title
import os
import sys

def generate_page(from_path, template_path, dest_path, basepath):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  from_file_string = open(from_path, "r").read()
  template_file_string = open(template_path, "r").read()
  html = markdown_to_html_node(from_file_string).to_html()
  title = extract_title(from_file_string)

  html_ready = template_file_string.replace("{{ Title }}", title).replace("{{ Content }}", html)
  if basepath != "./":
    html_ready = html_ready.replace("href=\"/", f"href=\"{basepath}").replace("src=\"/", f"src=\"{basepath}")


  # ["docs", ....]
  dest_paths = dest_path.replace(basepath, "").split("/")

  # composing folder
  for i in range(1, len(dest_paths)):
    if i != len(dest_paths) and not os.path.exists(basepath + "/".join(dest_paths[:i])):
      os.makedirs(basepath +"/".join(dest_paths[:i]))
    
  f = open(dest_path, "x")
  f.write(html_ready)
  f.close()

  
