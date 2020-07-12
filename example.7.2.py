fname = input('Enter file name: ')
fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From:'):
        continue
    if not line.startswith('From'):
        continue
    else:
        line = line.split()
        line = line[1]
        print(line)
        count += 1

print("there were",count,"lines in the file with From as first word") 