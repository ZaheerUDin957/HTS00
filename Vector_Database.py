# Vector_Database.py
class VectorDatabase:
    vectors = {}

    @classmethod
    def save_vector(cls, index, vector):
        cls.vectors[index] = vector

    @classmethod
    def retrieve_vector(cls, index):
        return cls.vectors.get(index)