---
- GuiCommand:/fr
   Name:PartDesign Hole
   Name/fr:PartDesign Perçage
   MenuLocation:Part Design → Créer une fonction soustractive → Perçage
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Cavité](PartDesign_Pocket/fr.md)
---

# PartDesign Hole/fr

## Description

La fonction **Perçage** crée un ou plusieurs trous à partir des cercles et des arcs d\'une esquisse sélectionnée. Si des arcs sont présents, ils doivent faire partie de contours fermés. Toutes les entités autres que des arcs ou des cercles sont ignorées mais elles doivent tout de même former des contours fermés. De nombreux paramètres peuvent être définis, tels que le filetage et la taille, l\'ajustement, le type de trou (fraise, lamage, droit) etc\...

Les centres des cercles et des arcs sont utilisés pour positionner les trous, mais veuillez noter que leurs rayons ne sont pas pris en compte. Les trous générés seront identiques même si les rayons varient.

<img alt="" src=images/Countersunk_and_counterbored_holes_cross-section1.png  style="width:600px;">



*Coupe longitudinale d'un trou fraisé (à gauche) et d'un trou chambré (à droite).*



## Utilisation

1.  Appuyez sur le bouton **<img src="images/PartDesign_Hole.svg" width=16px> '''Perçage'''**.
2.  Si une esquisse inutilisée existante est trouvée, elle sera automatiquement utilisée. Si plus d\'une esquisse est trouvée, un panneau **Sélectionner une fonction** apparaît pour faire une sélection. Alternativement, une esquisse peut être sélectionnée avant de lancer la commande Perçage.
3.  Définir les paramètres du perçage, voir la section [Options](#Options.md).
4.  Appuyez sur **OK**.

## Options

Selon la sélection effectuée, certains champs seront activés ou resteront désactivés.

![](images/PartDesign_Hole_parameters.png )



### Filetage et taille 

-   **Profil** : si défini sur *Aucun*, aucune information de filetage n\'est définie. Les profils de filetages [ISO](https://fr.wikipedia.org/wiki/Filetage_m%C3%A9trique) et [UTS](https://fr.wikipedia.org/wiki/Filetage_unifi%C3%A9) activent les champs *Direction*, *Taille*, *Adapter* et *Classe*.
-   **Fileté** : si coché, les données de filetage seront ajoutées à la fonction Trou et le diamètre mineur du trou sera utilisé. Si cette case n\'est pas cochée, le trou est considéré comme non fileté et le diamètre principal nominal avec le *jeu* défini est choisi.
-   **Modèle de taraudage** : si cette case est cochée, un taraudage réel est modélisé. Cela consomme beaucoup de puissance de calcul et n\'est généralement pas utilisé pour les modèles, sauf à des fins d\'affichage ou parfois pour les impressions 3D. S\'il est utilisé, il est conseillé de le vérifier comme l\'une des dernières actions effectuées sur le modèle car cela augmenterait considérablement le temps de recalcul. ({{Version/fr|0.20}})
-   **Direction** : définit le sens du filetage (pas à droite ou pas à gauche) si l\'option *Fileté* est cochée.
-   **Taille** : définit la taille du fil. Nécessite que le \"profil\" soit défini sur l\'un des profils [ISO](https://fr.wikipedia.org/wiki/Filetage_m%C3%A9trique) ou [UTS](https://fr.wikipedia.org/wiki/Filetage_unifi%C3%A9).
-   **Découpe du trou** : définit le diamètre du trou de dégagement standard, étroit ou large. Pour les filetages ISO, les diamètres sont conformes à la norme ISO 273, pour les UTS, ils sont calculés à l\'aide d\'une règle empirique car il n\'existe pas de norme les définissant. Disponible uniquement pour les trous non filetés.
-   **Adapter** : définit l\'ajustement standard ou proche pour les profils filetés.
-   **Classe** : définit la classe de tolérance.
-   **Diamètre** : définit le diamètre du trou si le *Profil* a été défini sur *Aucun*.
-   **Profondeur** : profondeur du trou à partir du plan d\'esquisse. *Dimension* permet d\'indiquer une valeur dans un champ. *A travers tout* va réaliser le trou à travers tout le corps. **Remarque :** Pour des raisons techniques, *A travers tout* est en fait un trou de 10 mètres de profondeur. Si vous avez besoin de trous plus profonds, utilisez *Dimension*.



### Trou découpé 

-   **Type** : définit le type de coupe de trou: *Aucun* signifie pas de coupe, les autres types sont les différentes normes pour les vis et les types génériques *Lamage*, *Fraisage* et ({{Version/fr|0.21}}) *Contre-perçage*.
-   **Diamètre** : définit le diamètre supérieur (au plan d\'esquisse) pour la découpe du trou.
-   **Profondeur** : la profondeur est définie différemment selon le **Type** :
    -   Pour un *Lamage*, il s\'agit de la profondeur du trou découpé, mesurée à partir du plan de l\'esquisse.
    -   Pour un *Fraisage*, c\'est la profondeur du sommet de la tête de la vis sous le plan de l\'esquisse.
    -   Pour un *Contre-perçage*, il s\'agit de la profondeur de la partie cylindrique de la coupe du trou.
-   **Angle de fraisage** : angle de la découpe du trou conique. Applicable uniquement pour les fraisages.



### Pointe de perçage 

-   **Type** : définit la fin du trou si *Profondeur* est réglé sur *Cote*.
    -   **Plat** produit un fond plat
    -   **En angle** définit une pointe conique. Son option **Tenir compte de la profondeur** soustraira la hauteur conique de la *Dimension*. Ainsi, si par exemple la *Dimension* est de 7.00 et que l\'option n\'est pas utilisée, la partie cylindrique du trou sera 7.00 et la profondeur nécessaire pour la partie conique est ajoutée à la profondeur du trou. Si l\'option est utilisée, la profondeur totale du trou, pointe conique comprise, sera de 7.00.



### Divers

-   **Conique** : définit un angle de conicité au trou. La valeur est calculée à partir du plan d\'esquisse normal. 90 degrés définit un trou droit. Une valeur inférieure à 90 génère un rayon de trou plus petit en sortie; une valeur supérieure à 90 agrandit le rayon du trou en sortie.
-   **Inversé** : inverse la direction d\'extrusion du trou. La direction par défaut est la direction de mappage de l\'esquisse de perçage avec son ancrage.



## Propriétés

La plupart des propriétés des Données sont les mêmes que celles indiquées dans [Options](#Options.md).

-    **Label**: nom donné à l\'objet, ce nom peut être changé à la convenance.

-    **Refine**: vrai ou faux. Si la valeur est \"true\" (vraie), nettoie le solide des bords résiduels laissés par les fonctions. Voir **<img src="images/Part_RefineShape.svg" width=16px> [Part Affiner la forme](Part_RefineShape/fr.md)** pour plus de détails.

## Limitations

-   Par défaut, la fonction de perçage est extrudée en dessous du plan d\'esquisse. Si le solide se trouve sur le Plan XY et que l\'esquisse du trou est attachée au Plan XY, la fonction essaiera d\'extruder du solide et ne produira apparemment aucun résultat. Dans ce cas, l\'option *Reversed* doit être définie, sinon, l\'esquisse peut être mappée sur la face inférieure du solide.
-   Le modèle de taraudage ne fonctionne que si Inversé n\'est pas défini.



## Définitions des types de coupes 

Les types de coupes (types de vis) sont définis dans des fichiers [json](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation). Il existe un ensemble de fichiers distribués avec FreeCAD, mais les utilisateurs peuvent créer leurs propres définitions. Les fichiers sont à rechercher dans <UserAppDataDir>/PartDesign/Hole. `UserAppDataDir` peut être trouvé en tapant `App.getUserAppDataDir()` dans la [console Python](Python_console/fr.md).

Le fichier doit contenir :

-   **name** : Le nom de la définition. Il doit être unique car il sera utilisé comme identifiant dans l\'interface utilisateur de FreeCAD et comme index interne.
-   **cut_type** : Soit `countersink` ou `counterbore`.
-   **thread_type** : Soit `metric` ou `metricfine`.
-   **angle** : L\'angle d\'un chanfrein (pas nécessaire pour un alésage).
-   **data** : Une liste de dimensions, composée de :
    -   **thread** : Nom du filetage connu de FreeCAD.
    -   **diameter** : Le diamètre de la coupe.
    -   **depth** : Profondeur du chambrage (non nécessaire pour le fraisage).

Exemple : {{Code|lang=json|code=
{
    "name": "DIN 7984",
    "cut_type": "counterbore",
    "thread_type": "metric",
    "data": [
        { "thread": "M2",   "diameter":  4.3, "depth":  1.6 },
        { "thread": "M2.5", "diameter":  5.0, "depth":  2.0 },
        …
    ]
}
}}





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Hole/fr
