#Assignment 4
#Task 1: Read a File and Handle Errors


try:
    file1=open("sample.txt",'r+')
    reading_file=file1.read()
    print("Reading file content:\n", reading_file)
    file1.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")





