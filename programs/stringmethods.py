
name = "python programming"


#p   y   t    h    o    n      p  r   o   g   r    a     m    m  i   n    g
#0   1   2    3    4    5  6   7   8  9  10   11   12   13   14  15  16   17 
#                                                                -3  -2   -1
#slicing
#string[start:stop:step]
print(name)
print(name[0])
print(name[1])
print(name[0:5])
print(name[8:13])
print(name[0:18])
print(name[0:18:1])
print(name[::])  # name[0:18:1]
print(name[:])   # name[0:18]
print(name[0:18:2]) #pto po
print(name[1:18:2])
print(name[-1])
print(name[-2])
print(name[-6:-1:-1])
print(name[::-1])



name = "python programming"
print(name.capitalize())
print(name.title())
print(name.center(40))

print(name.center(0,"*"))
print(name.count("p"))
print(name.endswith("p"))
print(name.startswith("q"))
print(name.endswith("g"))
print(name.endswith("w"))
print(name.find("in")) # if substirng is existing.. will return the starting index of i
print(name.find("abc"))# if not found... will return -1

aname = "I love {} and {}"  # template
print(aname.format("Noida","Hyderbad"))

print(name.isalnum())
print(name.isalpha())
print(name.isupper())
print(name.islower())


print(name.split(" ")) # string to list
bname = "    python  "
print(len(bname))
print(len(bname.strip()))
print(len(bname.lstrip()))
print(len(bname.rstrip()))

alist = ["python","programming"] #list
print(" ".join(alist))   # list to string

cname = "PYnToN"
print(cname.swapcase())

name = "python"
print(name.encode("utf-16"))
print(name.encode("utf-32"))

val = 10
print(oct(val))
print(hex(val))


name  = "python programming"
print(name.isalpha())
print(name.isalnum())

# if condition
if name.islower() :
    print("string is lowr")
    print("inside if ")
    print("still inside if ")


if name.startswith("p"):
    print("its python")
    print("inside if")


#if-else
if name.islower() :
    print("string is lowr")
    
else:
    print("string is upper")


#if-elif-elif-elif-else
lang = input("Enter any language:")
if lang == "python":
    print("its python")
elif lang == "java":
    print("its java")
elif lang == "oracle":
    print("its oracle")
else:
    print("its someother language")


#if-elif-elif-elif-else
lang = input("Enter any language:")
if lang == "python":
    print("its python")
else:
    if lang == "java":
        print("its java")
    elif lang == "oracle":
        print("its oracle")
    else:
        print("its someother language")


# range(start,stop,incremental)
for i in range(1,11):
    print(i)
##  displays numbers from 1 to 10
for i in range(1,11,1):
    print(i)
# display all even numbers
for i in range(2,10,2):
    print(i)
# display odd numbers
for i in range(1,10,2):
    print(i)
# display in reverse order
for i in range(10,1,-1):
    print(i)

name = 'python'
for char in name:
    print(char)