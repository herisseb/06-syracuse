#### Fonctions secondaires

"""
Module de calcul et de visualisation de la suite de Syracuse.

Ce module permet de générer la suite de Syracuse pour un nombre donné,
d'analyser ses propriétés (temps de vol, altitude maximale) et d'afficher
sa courbe d'évolution via la librairie Plotly.
"""
# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###

def syr_plot(lsyr):
    """
    Affiche le graphique de la suite de Syracuse.

    Args:
        lsyr (list): La liste des valeurs de la suite de Syracuse.

    Returns:
        None: Cette fonction ne retourne rien, elle ouvre une fenêtre graphique.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    l = [n ]
    current_n = n
    # On boucle tant qu'on n'est pas arrivé à 1
    while current_n != 1:
        if current_n % 2 == 0:
            # Si pair, on divise par 2 (division entière //)
            current_n = current_n // 2
        else:
            # Si impair, on multiplie par 3 et on ajoute 1
            current_n = current_n * 3 + 1
        l.append(current_n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    # Le temps de vol correspond au nombre d'étapes après le départ
    # Si la liste a 10 éléments, il y a eu 9 étapes.
    return len(l) - 1

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    source = l[0]
    n = 0
    # On parcourt la liste à partir du 2ème élément (l[1:])
    for x in l[1:]:
        if x > source:
            n += 1
        else:
            # Dès qu'on passe en dessous ou égal à la source, l'altitude est finie
            break
    return n

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    # Utilisation de la fonction max() native de Python
    return max(l)

#### Fonction principale

def main():
    """
    Point d'entrée principal du script.

    Génère la suite de Syracuse pour n=15, affiche le graphique,
    et imprime dans la console les statistiques (temps de vol, altitude).
    """

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
