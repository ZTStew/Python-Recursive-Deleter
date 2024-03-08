"""
Description:
  Program is intended to be the inverse of `re_del.py` creating the test files to be deleted by `re_del.py`
"""

import os, argparse, shutil
import logging as log
from glob import glob

# Ignored paths must use following format so that the root path can be added to ignore
ignore = [".\\", ".\\Backup\\", ".\\log\\"]

# sets fixed location for .log file 
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

# generates a list of all directories recursively from the root directory
folders = glob("./**/", recursive = True)


# Searches `folders` for paths that are not included in `ignore`
for i in folders:
  ignore_flag = False
  # loops through ignore array
  for j in ignore:
    # Checks if `folders[i]` and `ignore[j]` are the same, meaning the path is in the `ignore` array
    if j == i:
      ignore_flag = True
      break

  # If the directory is listed in `ignore`, log it as such and move on
  if ignore_flag:
    log.info("Ignored Folder: " + i)
    print("Ignored Folder: " + i)
  # Else the directory isn't listed in `ignore` and should be writen to
  else:
    log.info("Identified Folder: " + i)
    print("Identified Folder: " + i)

    # loops through files found in "/Backup"
    for dst in glob("./Backup/*"):
      # copies backup files to identified directory
      shutil.copy(dst, i)
      log.info(dst + " has been copied to " + i)

log.critical("Program Terminated")
