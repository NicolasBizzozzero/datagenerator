from pprint import pprint

import datagenerator as dg

# import mimesis
# import faker


# DEFAULT_LABEL = "Constant_c1"  # {class_name}_c{position}


def main_todo_afaire():
    data = dg.dataify(
        # Distribution ? Random float between floor and ceil ? precision ?
        # dg.FirstName(nationality="fr"),  # utiliser la librairie recemment trouvée
        # dg.CreditCard(bank="boa"),  # Par exemple
        # dg.RandomString(upper=True, lower=True, whitespaces=False, punctuation=True, choices=["abAEds"]),  # Si choices est passé, ignore les autres paramètres
    )
    # Recup tous les attributs pas passés par leur nom
    # Certains de ces paramètres ont un paramètre "normalize"
    # Ajout d'un paramètre output ? ("lists", "np.array", "pd.dataframe")


def main():
    data = dg.dataify(
        dg.Identifier(start=1, label="ID"),
        dg.Constant(value=4, label="constante nulle"),
        dg.RandomFloat(floor=3, ceil=17),
        dg.RandomInteger(floor=3, ceil=19, missing_value_probability=0.2),
        dg.NaN(),
        dg.Choice(choices=[-1, 1]),
        lines=10
    )
    pprint(data)


if __name__ == '__main__':
    main()
