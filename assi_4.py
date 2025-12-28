with open('output.txt','wt') as fh:
    fh.write(input('enter text to write to the file:'))
    print('Data succesfully  written to output.txt')
    sh=open('output.txt','at')
    fh.write("\n")
    fh.write(input('enter additional text to append : '))
    print('Data succesfully appended ')
    print('final content  of output.txt')
fh=open('output.txt','rt')
con=fh.readlines()
for line in con:
    print(line)
    