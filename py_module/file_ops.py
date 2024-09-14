
try:
    f = open("myfile.txt", 'r')
    # print(f.read())
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    
    # print(f.readlines())
finally:
    f.close()
