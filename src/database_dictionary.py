import json


_EMPTY_JSON_DOCUMENT = """{
    "__env__": {
        "max_ID": 0
    }
}
"""


class DatabaseDictionary:
    filepath = None

    def __init__(self):
        self._load_dictionary()
        # Check if the environment is empty
        try:
            self.content["__env__"]
        except KeyError:
            self._create_env()

    def __str__(self) -> str:
        return self.content.__str__()

    def __repr__(self):
        return self.content.__repr__()

    def __index__(self):
        return self.content.__index__()

    def __getitem__(self, item):
        return self.content[item]

    def _create_env(self):
        self.content["__env__"] = {"max_ID": 0}

    def _load_dictionary(self):
        """ Load the content of the dictionary from the database. """
        global _EMPTY_JSON_DOCUMENT

        try:
            with open(self.filepath) as file:
                self.content = json.load(file)
        except FileNotFoundError:
            with open(self.filepath, 'w') as file:
                file.write(_EMPTY_JSON_DOCUMENT)
            self._load_dictionary()

    def _get_new_id(self) -> int:
        """ Increment the maximum ID of the database then returns it. """
        self.content["__env__"]["max_ID"] += 1
        return self.content["__env__"]["max_ID"]

    def get_max_id(self) -> int:
        """ Getter for the max_ID variable from the dictionary. """
        return self.content["__env__"]["max_ID"]

    def _overwrite(self, safe: bool = True):
        if safe:
            output = self.filepath + "_safe.json"
        else:
            output = self.filepath
        with open(output, 'w') as file:
            json.dump(self.content, file, indent=4, sort_keys=True)


if __name__ == "__main__":
    pass
