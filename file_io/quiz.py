# Importing our text
f = open('file_io/files/relative_data.txt', 'r')
lines = f.read()
f.close()
print(lines)