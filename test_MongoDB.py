from pymongo import MongoClient

uri = "mongodb+srv://adityaboken1_db_user:Aalsoy1234@cluster0.guzqioe.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)