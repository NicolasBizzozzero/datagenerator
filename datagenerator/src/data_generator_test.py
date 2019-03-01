import data as dg
import columns as cl

import pandas as pd

from pprint import pprint
# import mimesis
# import faker


# DEFAULT_LABEL = "Constant_c1"  # {class_name}_c{position}

# data is a list of lists
data = dg.dataify(
    cl.Identifier(start=1, label="ID"),
    cl.Constant(value=4, label="constante nulle"),
    # Distribution ? Random float between floor and ceil ? precision ?
    cl.RandomFloat(floor=3, ceil=17),
    cl.RandomInteger(floor=3, ceil=19),  # Same as above
    # cl.FirstName(nationality="fr"),  # utiliser la librairie recemment trouvée
    # cl.CreditCard(bank="boa"),  # Par exemple
    cl.NaN(),
    # cl.RandomString(upper=True, lower=True, whitespaces=False, punctuation=True, choices=["abAEds"]),  # Si choices est passé, ignore les autres paramètres
    cl.Choice(choices=[-1, 1]),  # Pour un label
    lines=1000,
    header=True,  # Renvoie le header ou non
)
# Recup tous les attributs pas passés par leur nom
# Ajouter aléatoirement des Nan
# Certains de ces paramètres ont un paramètre "normalize"
# Ajout d'un paramètre output ? ("lists", "np.array", "pd.dataframe")


# Montrer des exemples après, genre qu'on peut facilement charger dans panda ou dans un classifieur sans perdre de temps.


# methode get_label, retournant le label passé ou le defaut label sinon
# methode compute_value, retournant une valeur
pprint(data)
