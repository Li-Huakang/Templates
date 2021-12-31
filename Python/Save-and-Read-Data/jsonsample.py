import json
data = [
    {
    "vgs":"3V",
    "data":[[1,2],[2,4]]
},
    {
    "vgs":"3V",
    "data":[[1,2],[2,4]]
}
]

# save as json
jsondata = json.dumps(data, indent=2)
print(jsondata)
f = open('data.json', 'w')
f.write(jsondata)
f.close()

# read json
f1 = open('data.json', 'r')
content = f1.read()
a = json.loads(content)
print(type(a))
print(a)
f1.close()