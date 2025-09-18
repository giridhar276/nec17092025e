
info = {
"id": "0001",
"type": "donut",
"name": "Cake",
"image":
{
"url": "images/0001.jpg",
"width": 200,
"height": 200
},
"thumbnail":
{
"url": "images/thumbnails/0001.jpg",
"width": 32,
"height": 32
}
}

val = 10
print(isinstance(val,int)) # True
print(isinstance(val,str)) # False
print(isinstance(val,list)) # False

for key,value in info.items():
    if isinstance(value,str):
        print(key.ljust(20),value)
    elif isinstance(value,dict): 
        for skey,svalue in value.items():
            finalkey = key + skey
            print(finalkey.ljust(20),svalue)