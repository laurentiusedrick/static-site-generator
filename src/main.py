import os
import shutil
from generatepage import generate_page
import sys

def main():
  basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

  def copy_static(path_src, path_dest):
    items = os.listdir(path_src)
    for i in items:
      if os.path.isfile(f"{path_src}/{i}"):
        shutil.copy(f"{path_src}/{i}", f"{path_dest}/{i}")
      elif os.path.isdir(f"{path_src}/{i}"):
        os.mkdir(f"{path_dest}/{i}")
        copy_static(f"{path_src}/{i}", f"{path_dest}/{i}")

  def gen_page_recursive(path_src, path_dest):
    items = os.listdir(path_src)
    for i in items:
      if os.path.isfile(f"{path_src}/{i}"):
        generate_page(f"{path_src}/{i}", f"./template.html", f"{path_dest}/index.html", basepath)
      elif os.path.isdir(f"{path_src}/{i}"):
        gen_page_recursive(f"{path_src}/{i}", f"{path_dest}/{i}")

  if os.path.exists(f"./docs"):
    shutil.rmtree(f"./docs")
  os.makedirs(f"./docs")

  copy_static(f"./static", f"./docs")
  gen_page_recursive(f"./content", f"./docs")


if __name__ == "__main__":
  main()