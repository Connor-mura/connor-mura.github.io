# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter: 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, usr, pwd): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = usr
        PASS = pwd
        HOST = '127.0.0.1' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%s/%s?authSource=%s&directConnection=true' % (USER,PASS,HOST,PORT,DB,DB)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
            
    # Create method to implement the C in CRUD. 
    def create(self, data: dict) -> bool:
        """inserts a document into the aac database animals collection"""
        if data is not None and isinstance(data, dict): #if data exists and is dict
            try:
                insert_result = self.database.animals.insert_one(data)  # data should be dictionary
                return insert_result.acknowledged #returns true if insert is valid
            except Exception as e: 
                print(f"Error inserting in database: {e}")#handles database issues
                return False
        else: 
            raise Exception("Nothing to save, entry invalid")#handles argument/type issues
            return False

    #Read method to implement the R in CRUD.
    def read(self, query: dict) -> list:
        """queries for documents in aac database animals collection"""
        if query is not None and isinstance(query, dict): #if query exists and is dict
            try:
                cursor = self.database.animals.find(query) #search
                return list(cursor)#returns list 
            except Exception as e:
                print(f"Error reading from database: {e}")#handles database issues
                return []#returns empty list
        else:
            print("Cannot read from database")#handles argument/type issues
            return []
    
    #Update method to implement the U in CRUD
    def update(self, query: dict, data: dict) -> int:
        """updates a document in aac database animals collection"""
        if query is not None and isinstance(query, dict) and data is not None and isinstance(data, dict): #if query and data exist and are dict
            try:
                update_result = self.database.animals.update_many(query, {"$set": data}) #updates
                return update_result.modified_count #returns number of modified records
            except Exception as e:
                print(f"Error updating database: {e}")#handles database issues
                return 0
        else:
            print("Cannot update database")#handles argument/type issues
            return 0
    
    #Delete method to implement the D in CRUD
    def delete(self, query: dict) -> int:
        """deletes documents in aac database animals collection"""
        if query is not None and isinstance(query, dict): #if query exists and is dict
            try:
                delete_result = self.database.animals.delete_many(query) #deletes
                return delete_result.deleted_count #returns number of deleted records
            except Exception as e:
                print(f"Error deleting from database: {e}")#handles database issues
                return 0
        else:
            print("Cannot delete from database")#handles argument/type issues
            return 0
    
    