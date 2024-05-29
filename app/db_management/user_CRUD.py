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

async def get_all_connection(collection):
    try:
        return list(db[collection].find({}))
    except Exception as e:
        raise RuntimeError(f"Error to getting data from collection {collection}: {e}")


# async def get_by_id(collection, document_id):
#     name_of_collection = collection.name
#     try:
#         return db[name_of_collection].find_one({"id": document_id})
#     except Exception as e:
#         raise RuntimeError(f"Error fetching data from collection {name_of_collection}: {e}")
#


#
# async def delete(collection, document_id):
#     name_of_collection = collection.name
#     try:
#         deleted_document = collections[name_of_collection].find_one_and_delete({"id": document_id})
#         if not deleted_document:
#             raise ValueError(f"No document with ID {document_id} found in collection {name_of_collection}")
#         return deleted_document
#     except Exception as e:
#         raise RuntimeError(f"Error deleting document from collection {name_of_collection}: {e}")
#
