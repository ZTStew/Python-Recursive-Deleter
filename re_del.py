"""
Description:
  Program is intended to be given a file name after which the program will recursively search every folder, with the execution point being the root, for the given file

  Program should ignore any folders with the name: `Backup`
  Program should not look at the files in the execution root
"""

import os, argparse, json
import logging as log
from glob import glob
from pathlib import Path
import re

# function to clean the blacklist provided data
def cleanBlacklist(blacklist):
  for item in range(len(blacklist)):
    blacklist[item] = blacklist[item].lower()

  return blacklist

# Ignored paths must use following format so that the root path can be added to ignore
ignore = [".\\", ".\\Backup\\", ".\\log\\"]
# blacklist = cleanBlacklist(["README.md", "test.txt"])

# pulls data from `blacklist.json`
with open(os.path.dirname(os.path.abspath(__file__)) + '\\blacklist.json', 'r') as blacklist:
    data=json.loads(blacklist.read())

# cleans data in `blacklist`
blacklist = cleanBlacklist(data["blacklist"])

# Sets location of file that will contain the log file
path = os.path.dirname(os.path.abspath(__file__)) + '\\Log\\recursive_deleter.log'

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

args = argparse.ArgumentParser(description="Program recursively deletes all files found in Blacklist.log")
args.add_argument(
  "-t",
  "--test",
  type=int,
  help="Declair if the application should run in test mode [0 -> production (default) | 1 -> test mode]."
)

args = args.parse_args()

# log.warning("Blacklisted Files: ", blacklist)

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
    # print("Ignored Folder: " + i)
  # Else the directory isn't listed in `ignore` and should be writen to
  else:
    log.info("Identified Folder: " + i)
    print("Identified Folder: " + i)


    # loops through each file found in each directory
    # Changes directory name to allow glob to be able to handle directories with '[]' in the name
    for file in glob(re.sub('([\[\]])','[\\1]',i) + "*"):
      print(file)
      # print(os.path.splitext(file)[1])
      # print(Path(file).stem)
      # loops through the blacklisted files
      for i in range(len(blacklist)):
        # checks if `file` matches both the spelling and file extension of the blacklisted file
        if Path(file).stem.lower() == Path(blacklist[i]).stem and os.path.splitext(file)[1].lower() == os.path.splitext(blacklist[i])[1]:
          log.info("File Deleted: " + file)
          # print("Blacklisted File: " + file)
          # removes the file
          os.remove(file)

log.critical("Program Terminated")
