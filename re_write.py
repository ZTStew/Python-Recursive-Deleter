"""
Description:
  Program is intended to be the inverse of `re_del.py` creating the test files to be deleted by `re_del.py`

# Rejected method for searching folders for the reason of it searching hidden folders
# recursively searches all directories returning (dirpath, dirnames, filenames)
# for i in os.walk("./"):
#   print(i[0])
"""

import os, argparse
import logging as log
from glob import glob

# Ignored files must use following format so that the root directory can be added to ignore
ignore = [".\\", ".\\Backup\\", ".\\log\\"]

path = os.path.dirname(os.path.abspath(__file__)) + '\\Log\\recursive_writer.log'

log.basicConfig(
    filename= path,
    level=log.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# log.debug("debug message")
# log.info("info message")
# log.warning("warning message")
# log.error("error message")
# log.critical("critical message")

log.critical("### ### ### V Program Starts V ### ### ###")

args = argparse.ArgumentParser()
args.add_argument(
  "-t",
  "--test",
  type=int,
  help="Declair if the application should run in test mode [0 -> production (default) | 1 -> test mode]."
)

args = args.parse_args()

if args.test:
  log.critical("Test Running")

folders = glob("./**/", recursive = True)

print(folders)

# Searches `folders` for directories that are not included in `ingore`
for i in folders:
  blacklist_flag = False
  # loops through ignore array
  for j in ignore:
    # print(j)
    if j == i:
      blacklist_flag = True
      break

  if blacklist_flag:
    log.info("Ignored Folder: " + i)
    print("Ignored Folder: " + i)
  else:
    log.info("Identified Folder: " + i)
    print("Identified Folder: " + i)




log.critical("Program Terminated")
