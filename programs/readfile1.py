
# method1
fobj = open("employees.txt","r")
for line in fobj:
    line = line.strip()
    print(line)
fobj.close()
print("---------------------------------------------------")
#method2    fobj.readlines() ------> list
fobj = open("employees.txt","r")
print(fobj.readlines())
fobj.close()
print("---------------------------------------------------")
#method3    fobj.read() ------> string   just like Ctrl+A  Ctrl+C   Ctrl+V
fobj = open("employees.txt","r")
print(fobj.read())
fobj.close()
print("---------------------------------------------------")
# method4 : using pandas
import pandas 
df = pandas.read_csv("employees.txt")
print(df)



