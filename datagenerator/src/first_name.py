import src.vrac.maths
import src.database_dictionary


class Sex:
    UNDEFINED = "UNDEFINED"
    MALE = "MALE"
    FEMALE = "FEMALE"
    BOTH = "BOTH"


class FirstNameDictionary(src.database_dictionary.DatabaseDictionary):
    filepath = "databases/first_name.json"

    def add_name(self, first_name: str, sex=Sex.UNDEFINED):
        """ Add a new name in the dictionary. You can also permanently add it
        to the database by calling '_overwrite' right after adding it.
        """
        first_name = first_name.upper()
        try:
            if self.content[first_name]["sex"] == sex:
                return
            elif self.content[first_name]["sex"] == Sex.BOTH:
                return
            elif self.content[first_name]["sex"] == Sex.UNDEFINED:
                self.content[first_name]["sex"] = sex
            elif (self.content[first_name]["sex"] != sex) and \
                 (sex != Sex.UNDEFINED):
                self.content[first_name]["sex"] = Sex.BOTH
        except KeyError:
            self.content[first_name] = {"ID": self._get_new_id(), "sex": sex}

    def first_names(self, sex=Sex.BOTH) -> iter:
        """ Iterate over the names of the dictionary.
        Defaulting to FEMALE and MALE names. UNDEFINED names will be excluded
        whatsoever.
        """
        if sex != Sex.BOTH:
            for key, item in self.content.items():
                try:
                    item["max_ID"]
                except KeyError:
                    if item["sex"] in (sex, Sex.BOTH):
                        yield key
        else:
            for key, item in self.content.items():
                try:
                    item["max_ID"]
                except KeyError:
                    if item["sex"] != Sex.UNDEFINED:
                        yield key

    def get_random_first_name(self, sex=Sex.BOTH):
        """ Return a random name from the dictionary.
        Defaulting to FEMALE and MALE names. UNDEFINED names will be excluded
        whatsoever.
        """
        names = list(self.first_names(sex=sex))
        size = len(names)
        return names[src.vrac.maths.get_random_integer(0, size)]


def get_random_first_name(sex=Sex.BOTH):
    """ Return a random first name from the database.
    Defaulting to FEMALE and MALE names. UNDEFINED names will be excluded
    whatsoever.
    """
    first_name_dictionary = FirstNameDictionary()
    return first_name_dictionary.get_random_first_name(sex=sex).capitalize()


if __name__ == "__main__":
    pass
