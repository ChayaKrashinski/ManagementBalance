from app.db_management.connection import users, db


async def add(collection, document):
    """
     Add a document to a collection in the database.

     Parameters:
     - collection (str): The name of the collection in the database to which the document should be added.
     - document (object): The document to be added to the collection. Ensure that the document matches the required format in the database.

     Returns:
     - dict: A dictionary containing the ID of the document that was added to the collection in the database.

     Raises:
     - RuntimeError: If any error occurs during the addition process, a RuntimeError with a corresponding error message will be raised.
     """
    try:
        result = db[collection].insert_one(document.__dict__)
        return {"id": str(result.inserted_id)}
    except Exception as e:
        raise RuntimeError(f"Error adding document to collection {collection}: {e}")


async def get_one(collection, document):
    """
    Retrieve a single document from a collection in the database.

    Parameters:
    - collection (str): The name of the collection in the database from which to retrieve the document.
    - document (object): The document used as a query parameter to retrieve a matching document from the collection.

    Returns:
    - dict or None: A dictionary representing the retrieved document if found, or None if no matching document is found.

    Raises:
    - RuntimeError: If any error occurs during the retrieval process, a RuntimeError with a corresponding error message will be raised.
    """
    try:
        res = db[collection].find_one({'name': document.name})
        return res
    except Exception as e:
        raise RuntimeError(f"Error to getting data from collection {collection}: {e}")


async def update(collection, document_id, data_to_update):
    """
    Update a document in a collection in the database.

    Parameters:
    - collection (str): The name of the collection in the database where the document to be updated resides.
    - document_id (str): The ID of the document to be updated.
    - data_to_update (object): The data with which to update the document.

    Returns:
    - str: A string indicating that the object has been successfully updated.

    Raises:
    - ValueError: If no document with the specified ID is found in the collection, a ValueError will be raised.
    - RuntimeError: If any other error occurs during the update process, a RuntimeError with a corresponding error message will be raised.
    """
    try:
        result = db[collection].update_one({'id': document_id}, {"$set": data_to_update.__dict__})
        if result.modified_count == 0:
            raise ValueError(f"No document with ID {document_id} found in collection {collection}")
        return "the object updated"
    except Exception as e:
        raise RuntimeError(f"Error updating document in collection {collection}: {e}")


async def get_all_collection(collection):
    """
      Retrieve all documents from a collection in the database.

      Parameters:
      - collection (str): The name of the collection in the database from which to retrieve all documents.

      Returns:
      - list: A list containing dictionaries, each representing a document retrieved from the collection.

      Raises:
      - RuntimeError: If any error occurs during the retrieval process, a RuntimeError with a corresponding error message will be raised.
      """
    try:
        return list(db[collection].find({}))
    except Exception as e:
        raise RuntimeError(f"Error to getting data from collection {collection}: {e}")


async def get_by_id(collection, document_id):
    """
    Retrieve a document from a collection in the database by its ID.

    Parameters:
    - collection (str): The name of the collection in the database from which to retrieve the document.
    - document_id (str): The ID of the document to retrieve.

    Returns:
    - dict or None: A dictionary representing the retrieved document if found, or None if no matching document is found.

    Raises:
    - RuntimeError: If any error occurs during the retrieval process, a RuntimeError with a corresponding error message will be raised.
    """

    try:
        return db[collection].find_one({"id": document_id})
    except Exception as e:
        raise RuntimeError(f"Error fetching data from collection {collection}: {e}")


async def get_all(collection, document_id):
    """
    Retrieve all documents from a collection in the database with a specific ID.

    Parameters:
    - collection (str): The name of the collection in the database from which to retrieve the documents.
    - document_id (str): The ID of the documents to retrieve.

    Returns:
    - Cursor: A cursor object containing the documents retrieved from the collection.

    Raises:
    - RuntimeError: If any error occurs during the retrieval process, a RuntimeError with a corresponding error message will be raised.
    """
    try:
        return db[collection].find({"id": document_id})
    except Exception as e:
        raise RuntimeError(f"Error fetching data from collection {collection}: {e}")


async def delete(collection, user_id, document_id):
    """
    Delete a document from a collection in the database.

    Parameters:
    - collection (str): The name of the collection in the database from which to delete the document.
    - user_id (str): The ID of the user who owns the document.
    - document_id (str): The ID of the document to delete.

    Returns:
    - dict or None: A dictionary representing the deleted document if found and deleted, or None if no matching document is found.

    Raises:
    - ValueError: If no document with the specified ID is found in the collection, a ValueError will be raised.
    - RuntimeError: If any other error occurs during the deletion process, a RuntimeError with a corresponding error message will be raised.
    """
    try:
        deleted_document = db[collection].find_one_and_delete({"id": document_id, "user": user_id})
        if not deleted_document:
            raise ValueError(f"No document with ID {document_id} found in collection {collection}")
        return deleted_document
    except Exception as e:
        raise RuntimeError(f"Error deleting document from collection {collection}: {e}")
