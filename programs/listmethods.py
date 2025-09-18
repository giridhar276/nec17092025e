alist = [43,67,32,15,53,84,37,91,10,10,10,10,10]

#list.append(object)
alist.append(39)
print("After appending:",alist)
#list.extend(iterable)
alist.extend([95,48,19])
print("After exteding:",alist)
#list.insert(index,value)  # list.insert(where,what)
alist.insert(1,99)
print("After inserting:",alist)
#list.pop(index) # value at index will be removed
alist.pop(1)
print("After pop operation:",alist)

if 500 in alist:
    alist.remove(500)
    print("After remove :",alist)
else:
    print("value not in list")

# list.reverse()
alist.reverse()
print("After reversing:",alist)
# list.sort() # ascending order
alist.sort()
print("After sorting :",alist)
# list.sort(reverse=True)
alist.sort(reverse= True)
print("in descending order:",alist)



alist = [10,20,30]
for val in alist:
    print(val)


alist = [10,20,30]
alist.reverse()
for val in alist:
    print(val)

alist = [10,20,30]
for val in alist[::-1]:
    print(val)


if 10 in alist:
    print("value exists")
else:
    print("value not found")