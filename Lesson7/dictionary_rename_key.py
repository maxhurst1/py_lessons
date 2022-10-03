sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

def rename_key(key, name):
    value = sampleDict[key]
    del sampleDict[key]
    sampleDict[name] = value
rename_key("city", "location")
print(sampleDict)
