

fobj = open("employees111.txt","r")
deptset = set()
#processing
for line in fobj:
    line = line.strip()
    output = line.split(",")
    deptset.add(output[2])
# display output
for dept in deptset:
    print(dept)
fobj.close()