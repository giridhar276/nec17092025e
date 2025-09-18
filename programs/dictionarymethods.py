book = {"chap1": 10 ,"chap2":20 ,"chap3":30}
print("Initial dictionary :",book)
# add new keyvalue
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60

print("Updated dictionary:", book)

# display individual values
print(book['chap1'])
print(book["chap2"])
print(book["chap3"])

# display keys
print(book.keys())

for key in book.keys():
    print(key)

## display values
print(book.values())

for value in book.values():
    print(value)


# display items
print(book.items())


for k,v in book.items():
    print("key:", k)
    print("value:",v)
    print("-------")


# key-value will be removed from dictionary
book.pop("chap1")
print("After pop operation :", book)


book.popitem() # remove last key-value
print(book)
book.popitem() # remove last key-value
print(book)
book.popitem() # remove last key-value
print(book)

book = {"chap1":10 ,"chap2":20}
newbook = {"chap3":30 ,"chap4":40}
finalbook = { **book, **newbook}
print(finalbook)

#method2
book.update(newbook)
print("updated book is ",book)