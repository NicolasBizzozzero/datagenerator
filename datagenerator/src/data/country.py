import src.vrac.maths
import src.database_dictionary


class Continent:
    AFRICA = "AFRICA"
    ASIA = "ASIA"
    EUROPE = "EUROPE"
    NORTH_AMERICA = "NORTH AMERICA"
    SOUTH_AMERICA = "SOUTH AMERICA"
    ANTARCTICA = "ANTARCTICA"
    AUSTRALIA = "AUSTRALIA"


class CountryDictionary(src.database_dictionary.DatabaseDictionary):
    filepath = "databases/country.json"

    def add_country(self, country: str, country_code: str):
        """ Add a new country in the dictionary. You can also permanently add it
        to the database by calling '_overwrite' right after adding it.
        """
        country = country.upper()
        try:
            self.content[country]
        except KeyError:
            self.content[country] = {"ID": self._get_new_id(),
                                     "code": country_code}

    def countries(self) -> iter:
        """ Iterate over the countries of the dictionary. """
        for key, item in self.content.items():
            try:
                item["max_ID"]
            except KeyError:
                yield key

    def get_random_country(self):
        """ Return a random country from the dictionary. """
        countries = list(self.countries())
        size = len(countries)
        return countries[src.vrac.maths.get_random_integer(0, size)]


def get_random_country():
    """ Return a random country from the database. """
    country_dictionary = CountryDictionary()
    return country_dictionary.get_random_country().capitalize()


if __name__ == "__main__":
    pass
