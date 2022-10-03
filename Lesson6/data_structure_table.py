from tabulate import tabulate
 
# assign data
mydata = [
    ["Is is mutable?", "Y", "Y", "N"],
    ["Can we change the size after creation?", "N", "Y", "N"],
    ["Can items in the list be changed?", "Y", "Y", "N"],
    ["How many different types of data can be stored?", "1", "Any", "Any"],
]
 
# create header
head = ["", "List", "Array", "Tuple"]
 
# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))
