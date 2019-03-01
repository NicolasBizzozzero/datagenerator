import src.vrac.maths
import src.database_dictionary


class LastNameDictionary(src.database_dictionary.DatabaseDictionary):
    filepath = "databases/last_name.json"

    def add_name(self, last_name: str):
        """ Add a new name in the dictionary. You can also permanently add it
        to the database by calling '_overwrite' right after adding it.
        """
        last_name = last_name.upper()
        try:
            self.content[last_name]
        except KeyError:
            self.content[last_name] = {"ID": self._get_new_id()}

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
        return names[src.vrac.maths.get_random_integer(0, size)]


def get_random_last_name():
    """ Return a random last name from the database. """
    last_name_dictionary = LastNameDictionary()
    return last_name_dictionary.get_random_last_name().capitalize()


if __name__ == "__main__":
    pass
