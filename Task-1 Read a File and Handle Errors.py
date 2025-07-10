try:
    sample_file = open ("sample.txt", "r")
    print("Reading file content:")
    print("Line 1:", sample_file.readline())
    print("Line 2:", sample_file.readline())
except:
    print("Error: The 'sample.txt' was not found")
