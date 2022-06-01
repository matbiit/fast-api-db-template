from cloudant.query import Query
from cloudant.client import Cloudant
import json, os
from dotenv import load_dotenv
load_dotenv()

class CloudantConnection(object):

    def __init__(self):

        db_name = "stock"
        
        if 'VCAP_SERVICES' in os.environ:
            vcap = json.loads(os.getenv('VCAP_SERVICES'))
            print('Found VCAP_SERVICES')
            if 'cloudantNoSQLDB' in vcap:
                creds = vcap['cloudantNoSQLDB'][0]['credentials']
                user = creds['username']
                password = creds['password']
                url = 'https://' + creds['host']
                self.client = Cloudant(user, password, url=url, connect=True, auto_renew=True)
        elif "CLOUDANT_URL" in os.environ:
            self.client = Cloudant(os.environ['CLOUDANT_USERNAME'], os.environ['CLOUDANT_PASSWORD'], url=os.environ['CLOUDANT_URL'], connect=True, auto_renew=True)
        elif os.path.isfile('vcap-local.json'):
            with open('vcap-local.json') as f:
                vcap = json.load(f)
                print('Found local VCAP_SERVICES')
                creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
                user = creds['username']
                password = creds['password']
                url = 'https://' + creds['host']
                self.client = Cloudant(user, password, url=url, connect=True, auto_renew=True)

        self.client.connect()
        self.database = self.client[db_name]

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
