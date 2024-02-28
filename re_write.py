"""
Description:
  Program is intended to be the inverse of `re_del.py` creating the test files to be deleted by `re_del.py`
"""

import os, argparse
import logging as log

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


log.critical("Program Terminated")