"""
Description:
  Program is intended to be given a file name after which the program will recursively search every folder, with the execution point being the root, for the given file

  Program should ignore any folders with the name: `Backup`
  Program should not look at the files in the execution root
"""

import os, argparse
import logging as log

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


  ### For File DELETER
  # Runs through each file in the identified directory
  # for j in glob(i+"*"):
  #   # print(j)
  #   print(os.path.isfile(j))
  # print(glob(i+"*")

log.critical("Program Terminated")