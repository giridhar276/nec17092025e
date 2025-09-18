
#regular way # traditional way
fobj = open("employees.txt","r")
for line in fobj:
    line = line.strip()
    print(line)
fobj.close()


#pythonic way
#context manager
# if any line starts using keyword 'with'... it is called context manager
# file is closed automatically when we move out of intentation

with open("employees.txt","r") as fobj:
    for line in fobj:
        line = line.strip()
        print(line)


with open("employees.txt","r") as fobj:
    print(fobj.readlines())
