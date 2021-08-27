import pymongo

class MongoDB:
    """
    A base class to interface with the MongoDB Database.

    ## Parameters
    ---------------
    collection: `str`
        the collection to use

    ## Example
    ---------------
    ```
    class SomeFeature(MongoDB):
        def __init__(self):
            super().__init__("collection_name")

        def get_all_documents(self):
            return self.data.find()
    ```
    """
    def __init__(self, collection):
        self.client = pymongo.MongoClient("mongodb://mongo:27017/") # use mongodb://localhost:27017 if you're running the code locally
        self.data = self.client["discordbot"][collection]
