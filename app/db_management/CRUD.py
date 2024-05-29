from app.db_management.connection import users, db


async def add(collection, document):
    try:
        result = db[collection].insert_one(document.__dict__)
        return {"id": str(result.inserted_id)}
    except Exception as e:
        raise RuntimeError(f"Error adding document to collection {collection}: {e}")


async  def get_one(collection, document):
    try:
        res = db[collection].find_one({'name':document.name})
        return res
    except Exception as e:
        raise RuntimeError(f"Error to getting data from collection {collection}: {e}")


async def update(collection, document_id, data_to_update):
    try:
        result = db[collection].update_one({'id': document_id}, {"$set": data_to_update.__dict__})
        if result.modified_count == 0:
            raise ValueError(f"No document with ID {document_id} found in collection {collection}")
        return "the object updated"
    except Exception as e:
        raise RuntimeError(f"Error updating document in collection {collection}: {e}")

async def get_all_collection(collection):
    try:
        return list(db[collection].find({}))
    except Exception as e:
        raise RuntimeError(f"Error to getting data from collection {collection}: {e}")

async def get_by_id(collection, document_id):
    try:
        return db[collection].find_one({"id": document_id})
    except Exception as e:
        raise RuntimeError(f"Error fetching data from collection {collection}: {e}")

async def get_all(collection, document_id):
    try:
        return db[collection].find_one({"id": document_id})
    except Exception as e:
        raise RuntimeError(f"Error fetching data from collection {collection}: {e}")


async def delete(collection, user_id, document_id ):
    try:
        deleted_document = db[collection].find_one_and_delete({"id": document_id, "user":user_id})
        if not deleted_document:
            raise ValueError(f"No document with ID {document_id} found in collection {collection}")
        return deleted_document
    except Exception as e:
        raise RuntimeError(f"Error deleting document from collection {collection}: {e}")

