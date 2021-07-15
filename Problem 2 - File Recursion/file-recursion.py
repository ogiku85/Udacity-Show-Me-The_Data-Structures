
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    result_list = []
    queue = []
    files_in_current_path = []
    current_path = path
    if path is None:
        return 'no path specified'
    elif isinstance(path,str) is not True:
        return 'specified path is not a valid string'
    files_in_current_path = os.listdir(current_path)
    for file in files_in_current_path:
        cwd = os.getcwd()

        filePath = os.path.join(cwd,current_path,file)
        if os.path.isfile(filePath) and filePath.endswith(suffix):
            result_list.append(file)
            
        if os.path.isdir(filePath):
            current_result = find_files(suffix, filePath)
            result_list.extend(current_result)

    return result_list
# test_dir ='C:\Users\RAIN-PC\Documents\UDACITY\ASSIGNMENT\Udacity-Show-Me-The_Data-Structures\Problem 2 - File Recursion\testdir'

#edge case test for invalid path
test_dir = None
result = find_files(".c", test_dir)
print(result) # no path specified

test_dir = 123
result = find_files(".c", test_dir)
print(result) # specified path is not a valid string

#test for existing file extension or suffice
test_dir ="testdir"
result = find_files(".c", test_dir)
print(result) # ['a.c', 'b.c', 'a.c', 't1.c']

#test for non-existent suffix or file extension
result = find_files(".pdf", test_dir)
print(result) #[]