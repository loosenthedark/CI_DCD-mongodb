import os
import pymongo
if os.path.exists('env.py'):
    import env


MONGO_URI = os.environ.get('MONGO_URI')
DATABASE = 'myFirstDB'
COLLECTION = 'celebrities'


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print('MongoDB is connected!')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print('Could not connect to MongoDB!!!: %s') % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

coll.update_one({ "first": "oscar" }, { "$set": { "gender": "m" } })

documents = coll.find()

for doc in documents:
    print(doc)


