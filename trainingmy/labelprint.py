classLabel = []
filename = 'Labels.txt'
with open(filename,'rt') as ftp:
    classLabel = ftp.read().strip('\n').split('\n')
print(classLabel)