alist = [12,98,49,52,59,95,75,29,10]
print(alist[0:5])
print(alist[5:8])

# list methods
alist.append(62)
print("After appending:",alist)
alist.extend([48,18,63]) #list.extend(list)
print("After extending:",alist)
#list.insert(index,value)  #list.insert(where to inesrt, what to insert)
alist.insert(1,100)
print("After inserting:",alist)
# list.pop(index)
alist.pop(1) # 1 is the index # value at 1 is removed
print("After pop operation:",alist)

if 200 in alist:
    alist.remove(200)
    print("After removing:",alist)
else:
    print("value not in list")

alist.reverse()
print("After reversing:",alist)
alist.sort()
print("After sorting:",alist)
alist.sort(reverse=True)
print("After sorting",alist)

print(alist.reverse())

