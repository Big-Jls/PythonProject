import pymongo
mongo = pymongo.MongoClient()

mydb = mongo.get_database('test')

con = mydb.get_collection('test')

one = con.find_one({'张三':'嘻嘻'})
print(one)

# insert = con.insert_one({
#     '李四':'不嘻嘻'
# })
# print(insert)


