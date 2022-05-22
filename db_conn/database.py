from cloudant.query import Query
from cloudant.client import Cloudant
import os
from dotenv import load_dotenv
load_dotenv()

class CloudantConnection(object):

    def __init__(self):

        user = os.getenv("CLOUDANT_USER")
        pwd = os.getenv("CLOUDANT_PWD")
        host = os.getenv("CLOUDANT_HOST")
        database = os.getenv("CLOUDANT_DATABASE")
        
        self.client = Cloudant(user, pwd, url=host, connect=True, auto_renew=True)
        self.client.connect()
        self.database = self.client[database]

    def retrieve_items(self):
        list = []
        for document in self.database:
            list.append(document)
        return list
    
    def retrieve_item(self, item_id):
        return self.database['item:' + str(item_id)]
    
    def update_item(self, item):
        my_document = self.database['item:' + str(item.id)]
        my_document['desc'] = item.desc
        my_document['amount'] = item.amount
        my_document.save()
        return my_document

    def add_item(self, item):
        doc = { "_id": "item:" + str(item.id), "desc": item.desc, "amount": str(item.amount) }
        my_document = self.database.create_document(doc)
        if my_document.exists():
            my_document.save()
            return my_document
        else:
            raise Exception('Error inserting document into cloudant')
        
    def delete_item(self, item):
        try:
            self.database['item:' + str(item.id)].delete()
            return {"result": "success" }
        except:
             return {"result": "failed" }
