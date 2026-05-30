class Retriever:

    @staticmethod
    def get(db):

        return db.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": 3
            }
        )