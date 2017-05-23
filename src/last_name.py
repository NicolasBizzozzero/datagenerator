import json
from src.vrac.maths import get_random_integer
from enum import Enum


class LastNameDictionary:
    filepath = "../res/last_name.json"

    def __init__(self):
        self._load_dictionary()

    def __str__(self) -> str:
        return self.content.__str__()

    def __repr__(self):
        return self.content.__repr__()

    def __index__(self):
        return self.content.__index__()

    def __getitem__(self, item):
        return self.content[item]

    def _load_dictionary(self):
        """ Load the content of the dictionary from the database. """
        with open(self.filepath) as file:
            self.content = json.load(file)

    def _get_new_id(self) -> int:
        """ Increment the maximum ID of the database then returns it. """
        self.content["__env__"]["max_ID"] += 1
        return self.content["__env__"]["max_ID"]

    def add_name(self, last_name: str):
        """ Add a new name in the dictionary. You can also permanently add it to the database by calling '_overwrite'
        right after adding it.
        """
        last_name = last_name.upper()
        try:
            self.content[last_name]
        except KeyError:
            self.content[last_name] = {"ID": self._get_new_id()}

    def get_max_id(self) -> int:
        """ Getter for the max_ID variable from the dictionary. """
        return self.content["__env__"]["max_ID"]

    def last_names(self) -> iter:
        """ Iterate over the names of the dictionary. """
        for key, item in self.content.items():
            try:
                item["max_ID"]
            except KeyError:
                yield key

    def get_random_last_name(self):
        """ Return a random name from the dictionary. """
        names = list(self.last_names())
        size = len(names)
        return names[get_random_integer(0, size)]

    def _overwrite(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.content, file, indent=4)


def get_random_last_name():
    """ Return a random last name from the database. """
    last_name_dictionary = LastNameDictionary()
    return last_name_dictionary.get_random_last_name().capitalize()


if __name__ == "__main__":
    pass
