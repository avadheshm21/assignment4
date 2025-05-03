#ASSIGNMENT 4:
# Task 2: Write and Append Data to a File


txt=input("Enter text to write to the file: ")

file1=open("output.txt",'w')
writing_file=file1.write(txt)
print("Data successfully written to output.txt.")
file1.close()


txt2=input("Enter additional text to append: ")

file1=open("output.txt",'a')
append_file=file1.write("\n")
append_file2=file1.write(txt2)
print("Data successfully appended.")
file1.close()

print("Final content of output.txt.")

file1=open("output.txt",'r+')
reading_file=file1.read()
print(reading_file)
file1.close()

