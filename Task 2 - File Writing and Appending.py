output_file = open('output.txt', 'w')
output_file.write(input("Enter Text to write to file:"))
print("Data Successfully written to output.txt.")
output_file.close()

output_file = open('output.txt', 'a')
output_file.writelines(input("Enter additional text to append:"))
print("Data successfully appended.")
output_file.close()

output_file = open('output.txt', 'r+')
print ("Final content of output.txt: \n", output_file.readlines())
output_file.close()