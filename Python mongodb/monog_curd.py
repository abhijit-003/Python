from pymongo import MongoClient

client = MongoClient("mongo://localhost:3000/")
db = client['mydatabase']
mycol = db['mycollection']


#CURD
#insert_one()  insert_many()
#update_one()  update_many()
#find() find_one()
#delete_one()  delete_many()

data1 = {
    "name": "abhi", 
    "class": "mca",
    "div": "B"
}

data2 = [{"name":"abhi","class":"mca","div":"B"},
         {"name":"satya","class":"mcs","div":"A"},
         {"name":"abhinav","class":"msc","div":"C"}
         ]

#create
#mycol.inset_one(data1)
#mycol.inset_many(data2);

#read
all_collection = mycol.find()
for x in all_collection:
    print(x) #display all entries

for x in mycol.find_one():
    print(x) #display first entry


#update 
my_query = {"name","abhinav"}
my_values = {"$set",{"class": "MCA"}}

#update a single document
mycol.update_one(my_query,my_values)

#update the multiple entiries
mycol.update_many("$set",{"class":"MCA"})

#delete 
#delete one
mycol.delete_one(my_query)

#delete many
mycol.delete_many(my_query)