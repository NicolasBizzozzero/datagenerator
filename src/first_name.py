import json
from src.vrac.maths import get_random_integer


class Sex:
    Undefined = "UNDEFINED"
    Male = "MALE"
    Female = "FEMALE"
    Both = "BOTH"


class FirstNameDictionary:
    def __init__(self, filepath: str="databases/first_name.json"):
        self.filepath = filepath
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

    def add_name(self, first_name: str, sex=Sex.Undefined):
        """ Add a new name in the dictionary. You can also permanently add it
        to the database by calling '_overwrite' right after adding it.
        """
        first_name = first_name.upper()
        try:
            if self.content[first_name]["sex"] == sex:
                return
            elif self.content[first_name]["sex"] == Sex.Both:
                return
            elif self.content[first_name]["sex"] == Sex.Undefined:
                self.content[first_name]["sex"] = sex
            elif (self.content[first_name]["sex"] != sex) and (sex != Sex.Undefined):
                self.content[first_name]["sex"] = Sex.Both
        except KeyError:
            self.content[first_name] = {"ID": self._get_new_id(), "sex": sex}

    def get_max_id(self) -> int:
        """ Getter for the max_ID variable from the dictionary. """
        return self.content["__env__"]["max_ID"]

    def first_names(self, sex=Sex.Both) -> iter:
        """ Iterate over the names of the dictionary.
        Defaulting to FEMALE and MALE names. UNDEFINED names will be excluded
        whatsoever.
        """
        if sex != Sex.Both:
            for key, item in self.content.items():
                try:
                    item["max_ID"]
                except KeyError:
                    if item["sex"] in (sex, Sex.Both):
                        yield key
        else:
            for key, item in self.content.items():
                try:
                    item["max_ID"]
                except KeyError:
                    if item["sex"] != Sex.Undefined:
                        yield key

    def get_random_first_name(self, sex=Sex.Both):
        """ Return a random name from the dictionary.
        Defaulting to FEMALE and MALE names. UNDEFINED names will be excluded
        whatsoever.
        """
        names = list(self.first_names(sex=sex))
        size = len(names)
        return names[get_random_integer(0, size)]

    def _overwrite(self, safe: bool = True):
        if safe:
            output = self.filepath + "_safe.json"
        else:
            output = self.filepath
        with open(output, 'w') as file:
            json.dump(self.content, file, indent=4)


def get_random_first_name(sex=Sex.Both):
    """ Return a random first name from the database.
    Defaulting to FEMALE and MALE names. UNDEFINED names will be excluded
    whatsoever.
    """
    first_name_dictionary = FirstNameDictionary()
    return first_name_dictionary.get_random_first_name(sex=sex).capitalize()


if __name__ == "__main__":
    pass
