from app.db_management.connection import Collection

users:Collection = Collection.users
async def find_user(password, name):
    for i in users:
        return i
    return None

async def get_all_connection(collection):
    name_of_collection = collection.name
    try:
        return list(db[name_of_collection].find({}))
    except Exception as e:
        raise RuntimeError(f"Error to getting data from collection {name_of_collection}: {e}")


async def get_by_id(collection, document_id):
    name_of_collection = collection.name
    try:
        return db[name_of_collection].find_one({"id": document_id})
    except Exception as e:
        raise RuntimeError(f"Error fetching data from collection {name_of_collection}: {e}")


async def add(collection, document):
    name_of_collection = collection.name
    try:
        result = db[name_of_collection].insert_one(document)
        return {"id": str(result.inserted_id)}
    except Exception as e:
        raise RuntimeError(f"Error adding document to collection {name_of_collection}: {e}")


async def update(collection, document_id, data_to_update):
    name_of_collection = collection.name
    try:
        result = db[name_of_collection].update_one({"id": document_id}, {"$set": data_to_update})
        if result.modified_count == 0:
            raise ValueError(f"No document with ID {document_id} found in collection {name_of_collection}")
        return data_to_update
    except Exception as e:
        raise RuntimeError(f"Error updating document in collection {name_of_collection}: {e}")


async def delete(collection, document_id):
    name_of_collection = collection.name
    try:
        deleted_document = db[name_of_collection].find_one_and_delete({"id": document_id})
        if not deleted_document:
            raise ValueError(f"No document with ID {document_id} found in collection {name_of_collection}")
        return deleted_document
    except Exception as e:
        raise RuntimeError(f"Error deleting document from collection {name_of_collection}: {e}")

