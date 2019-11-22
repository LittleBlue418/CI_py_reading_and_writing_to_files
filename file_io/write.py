f = open('file_io/newfile.txt', 'a')
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
f.writelines(lines)
f.close()