# Python Recursive Deleter
---
## Description:  
re_del - Program is intended to be given a file name after which the program will recursively search every folder, with the execution point being the root, for the given file
re_write - Program is intended to be the inverse of `re_del.py` creating the test files to be deleted by `re_del.py`


--
### Requirements:
- [ ] Program should read/delete files regardless of type
- [ ] Program should ignore any folders with the name: `Backup`
- [ ] Program should not look at the files in the execution root
- [ ] Program should be written to read a `blacklist.json` file that contains a list of file names user would like to delete

---
### Usage:
(explanation of how to use the program)
(re_del)
1. Navigate to the root folder that you want to delete files from
2. Execute `re_del.py`
3. Input the name of the file you would like to delete

(re_write)
1. Execute `re_write.py`
