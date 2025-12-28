try:
    fh=open('sample.txt','rt');

    content=fh.read()
    print(content)     
except:
    print(" Error:the file 'sample.txt'  was not found")    