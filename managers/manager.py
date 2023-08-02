from bson import ObjectId

from querying.Filter import Filter


class Manager:
    _collection = None
    _model = None

    @classmethod
    def get(cls, _id: ObjectId):
        return cls._collection.find_one({'_id': _id})

    @classmethod
    def find_one(cls, _filter: Filter):
        return cls._collection.find_one(_filter.formatted_filter)

    @classmethod
    def find(cls, _filter: Filter):
        return cls._collection.find(_filter.formatted_filter)

    @classmethod
    def create_one(cls, model: _model):
        new_document = model.to_dict()
        return cls._collection.insert_one(new_document).inserted_id

    @classmethod
    def create_many(cls, models: list[_model]):
        new_documents = [model.to_dict() for model in models]
        return cls._collection.insert_many(new_documents).inserted_ids

    @classmethod
    def update_one(cls, _filter: Filter, updated_values: dict):
        """
        This method will make a patch in the document that satisfy the filter
        :param _filter: filter to find the entity to update
        :param updated_values: dict with the new values of the entity
        :return: mongo response
        """
        return cls._collection.update_one(_filter.formatted_filter,
                                          {'$set': updated_values})

    @classmethod
    def update_many(cls, _filter: Filter, updated_values: dict):
        """
        This method will make a patch in the document that satisfy the filter
        :param _filter: filter to find the entities to update
        :param updated_values: dict with the new values of the entity
        :return: mongo response
        """
        return cls._collection.update_one(_filter.formatted_filter,
                                          {'$set': updated_values})

    @classmethod
    def delete_one(cls, _filter: Filter):
        return cls._collection.delete_one(_filter.formatted_filter)

    @classmethod
    def delete_many(cls, _filter: Filter):
        return cls._collection.delete_many(_filter.formatted_filter)
