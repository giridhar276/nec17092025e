
name = "python programming"
#name[0]="z"
#name[start:stop:step]
print(name[0])
print(name[1])
print(name[2:9])
print(name[7:9])
print(name[0:18])
print(name[0:18:1])
print(name[:])
print(name[::])
print(name[0:18:2]) #pto rgamn
print(name[0:18:3])
print(name[-1])
print(name[-2])
print(name[-5:-2])
print(name[::-1])



name = "python programming"
print(name.capitalize())
print(name.title())
print(name.upper())
print(name.lower())
print(name.isupper())
print(name)
print(name.islower())
print(name.split(" "))
print(name.center(40))
print(name.center(40,"*"))
print(name.replace("python","ruby"))
print(name.find("in")) # returns index if substring found
print(name.find("abc"))# -1 if not found

aname  = "  python "
print(len(aname))
print(len(aname.strip())) # remove whitespaces at both ends
print(len(aname.lstrip()))# 7
print(len(aname.rstrip()))#8
bname = "I love {} and {}" # template
print(bname.format("Noida","Hyderabad"))
print(bname.format("python","unix"))

print(name.count("p"))
print(name.count("ram"))
print(name.startswith("p"))
print(name.endswith("g"))
print(name.replace("python","spark"))
print(name.encode('utf-16'))


#simple if condition
if name.startswith("p"):
    print("its python")
    print("inside if")
    print("still inside if")

if name.islower():
    print("string is lower")

if name == "python programming":
    print("python")

if 1 < 2:
    print("true")

# if-else
if name.islower():
    print("string is lower")
    print("inside if")
    print("still inside if")
else:
    print("string is upper")
    print("inside else")

#if-elif-elif-elif-elif-else
name = input("Enter any language:")
if name == "python":
    print("python")
elif name == "java":
    print("java")
elif name == "unix":
    print("unix")
elif name == "spark":
    print("spark")
else:
    print("its someother language")

# check for existence of substring in main string
name = "python"
print(name.find("th")) #2
print(name.find("abc")) # -1

if name.find("th") != -1:
    print("substring found")

if 'th' in name:
    print("substring found")
else:
    print("not found")

# stringt concatenation
first = "python"
second = "programming"
final = first + " " + second
print(final)

#string repetition
print(first * 3)

alist = [10,20,30]
blist = [30,40,50]
finalist = alist + blist
print(finalist)
print(alist * 4)


# range(start,stop,step)
for i in range(1,11):
    print(i)

print("reversing numbers")
for val in range(10,0,-1):
    print(val)

print("even numbers")
for i in range(2,11,2):
    print(i) 

name  = "python"
for char in name:
    print(char)

alist = [10,20,"python"]
for val in alist:
    print(val)
