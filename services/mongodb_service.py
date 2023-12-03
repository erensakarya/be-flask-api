import os
from pymongo import MongoClient, errors


# maxPoolSize of pymongo connections is 100!


class MongodbService:
    def __init__(self, mode):
        self.mode = mode

    def get_client_and_db(self):
        if self.mode == "development":
            client = MongoClient(host=os.environ.get("DEV_HOSTNAME"),
                                 port=int(os.environ.get("PORT")))
        elif self.mode == "docker_single":
            client = MongoClient(host=os.environ.get("DOCKER_SINGLE_HOST"),
                                 port=int(os.environ.get("PORT")))
        elif self.mode == "docker_cluster":
            uri = (f"mongodb://{os.environ.get('DOCKER_CLUSTER_HOST1')}:{os.environ.get('PORT')},"
                   f"{os.environ.get('DOCKER_CLUSTER_HOST2')}:{os.environ.get('PORT')},"
                   f"{os.environ.get('DOCKER_CLUSTER_HOST3')}:{os.environ.get('PORT')}/"
                   f"?replicaSet={os.environ.get('REPLICA_SET')}&readPreference=primaryPreferred")
            # Read preference option:
            # indicates the preference to read from a primary but use a secondary if there is no primary available.
            # https://www.mongodb.com/docs/manual/core/read-preference/#replica-set-read-preference-max-staleness
            client = MongoClient(uri)
        else:
            raise Exception("Mode parameter should have been in ('development', 'docker_single', 'docker_cluster')!")
        db = client[f'{os.environ.get("DATABASE")}']
        return client, db

    def get_all_orders(self):
        client, db = self.get_client_and_db()
        collection = db['orders']
        cursor = collection.find({})
        cursor_list = list({"name": document['name'], "status": document['status']} for document in cursor)
        client.close()
        return cursor_list

    def get_specific_order_if_exists(self, order_name):
        client, db = self.get_client_and_db()
        collection = db['orders']
        cursor = collection.find({"name": f"{order_name}"})
        cursor_list = list({"name": document['name'], "status": document['status']} for document in cursor)
        client.close()
        return cursor_list

    def add_order(self, order_name):
        client, db = self.get_client_and_db()
        collection = db['orders']
        try:
            data = {"name": f"{order_name}", "status": "being_prepared"}
            collection.insert_one(data)
            client.close()
            return {"message": f"{order_name} order added successfully!"}
        except errors.DuplicateKeyError:
            return {"message": f"Duplicate key error! name: {order_name}"}
        except Exception as e:
            return {"message": e}

    def update_order_name(self, order_name, order_name_new):
        client, db = self.get_client_and_db()
        collection = db['orders']
        try:
            _filter = {'name': f'{order_name}'}
            new_name = {"$set": {'name': f"{order_name_new}"}}
            response = collection.update_one(_filter, new_name)
            client.close()
            if response.modified_count == 1:
                return {"message": f"{order_name} order modified as {order_name_new}!"}
            else:
                return {"message": f"There is no {order_name} order to be modified!"}
        except Exception as e:
            return {"message": e}

    def update_order_status(self, order_name, status):
        client, db = self.get_client_and_db()
        collection = db['orders']
        try:
            _filter = {'name': f'{order_name}'}
            new_status = {"$set": {'status': f"{status}"}}
            response = collection.update_one(_filter, new_status)
            client.close()
            if response.modified_count == 1:
                return {"message": f"{order_name} order's status has been modified as {status}!"}
            else:
                return {"message": f"There is no {order_name} order"
                                   f" or the status of {order_name} order is already {status}!"}
        except Exception as e:
            return {"message": e}

    def delete_order(self, order_name):
        client, db = self.get_client_and_db()
        collection = db['orders']
        try:
            response = collection.delete_one({'name': f"{order_name}"})
            client.close()
            if response.deleted_count == 1:
                return {"message": f"{order_name} order has been deleted!"}
            else:
                return {"message": f"There is no {order_name} order to be deleted!"}
        except Exception as e:
            return {"message": e}
