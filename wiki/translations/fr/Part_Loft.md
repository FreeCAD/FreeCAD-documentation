---
- GuiCommand:
   Name:Part Loft
   Name/fr:Part Lissage
   MenuLocation:Part - Lissage...
   Workbenches:[Part](Part_Workbench/fr.md)
   Version:0.13
   SeeAlso:[Part Balayage](Part_Sweep/fr.md)
---

# Part Loft/fr



## Présentation

L\'outil **Part Lissage** est utilisé pour créer une face, une coque ou une forme solide à partir de deux ou plusieurs profils. Les profils peuvent être un point (sommet), ligne (arête), une polyligne ou une face. Arêtes et polylignes peuvent être soit ouvertes ou fermées. Il existe différents [limitations et complications](Part_Loft/fr#Limitations_et_complications.md), voir ci-dessous, mais les profils peuvent provenir de [primitives de l\'atelier Part](Part_Workbench/fr.md), d\'[objets de l\'atelier Draft](Draft_Workbench/fr.md) et d\'[esquisses](Sketcher_Workbench/fr.md).

Le Lissage a trois paramètres, \"Surface réglée\", \"Créer le solide\" et \"Fermé\", chacun avec une valeur soit \"vrai\" soit \"fausse\".

Si \"Créer le solide\" est à \"vrai\", FreeCAD crée un solide si les profils sont une géométrie fermée; si \"faux\", FreeCAD crée une face ou (si plus d\'une face) une coque pour les profils ouverts ou fermés.

Si \"Surface réglée\" est à \"vrai\", FreeCAD crée une face, des faces ou un solide à partir des surfaces réglées. [Page de Wikipedia sur Surface réglée.](https://fr.wikipedia.org/wiki/Surface_r%C3%A9gl%C3%A9e)

Si \"Fermé\" est à \"vrai\", FreeCAD essaye de lisser le dernier profil vers le premier profil pour créer une figure fermée.

Pour plus d\'informations sur la façon dont les profils sont réunis, consultez la page [Part Détails techniques du lissage](Part_Loft_Technical_Details/fr.md).

![centre\|Part_Loft. À partir de trois profils qui sont deux Part Cercles et une Part Ellipse. Les paramètres sont Solide \"True\" et Surface réglée \"True\"](images/Part_Loft_solid_ruled_from3profiles_example_FreeCAD_0_13.jpg )



## Remarques

-   Les objets [App Link](App_Link/fr.md) liés aux types d\'objets appropriés et les conteneurs [App Part](App_Part/fr.md) contenant les objets visibles appropriés peuvent également être utilisés comme profils et trajectoires. {{Version/fr|0.20}}



## Limitations et complications 

-   Un sommet ou un point
    -   Un sommet ou un point ne peuvent être utilisés que dans le premier et/ou le dernier profil dans la liste des profils.
        -   Par exemple :
            -   vous ne pouvez pas lisser d\'un cercle à un point, à une ellipse.
            -   cependant vous pourriez lisser d\'un point à un cercle à une ellipse à un autre point.
-   Les profils de géométrie ouverts ou fermés ne peuvent pas être mélangés dans un seul lissage.
    -   Dans un lissage, tous les profils (lignes, polylignes etc.) doivent être soit ouverts ou fermé.
        -   Par exemple :
            -   FreeCAD ne peut pas lisser entre un cercle et une ligne.
-   Fonctionnalités de l\'atelier Draft
    -   Les fonctions de l\'atelier Draft peuvent être directement utilisées comme un profil dans FreeCAD 0.14 ou plus tard.
        -   Par exemple, les fonctionnalités suivantes de Draft peuvent être utilisées comme profils dans un Lissage de Pièce
            -   polygone.
            -   point, ligne, polyligne,
            -   B-spline, courbe de Bézier
            -   cercle, ellipse, rectangle
-   Esquisses de PartDesign
    -   Le profil peut être créé avec une esquisse. Toutefois, seule une esquisse valide sera affichée dans la liste pour être disponible pour la sélection.
    -   L\'esquisse doit contenir une seule polyligne ou ligne ouverte ou fermée (peut être plusieurs lignes, si ces lignes sont toutes connectées car elles sont alors une seule polyligne)
-   Atelier Part
    -   le profil peut être une Part primitive géométrique valide qui peut être créée avec un des outils [Part Primitives](Part_Primitives/fr.md)
        -   par exemple la Part primitive géométrique suivante peut être un profil valide
            -   point (sommet), ligne (arête)
            -   hélice, spirale
            -   cercle, ellipse
            -   polygone régulier
            -   plan (face)

-   Lissages fermés
    -   Les résultats des lissages fermés peuvent être inattendus - le lissage peut développer des torsions ou des plis. Le lissage est très sensible au placement des profils et à la complexité des courbes nécessaires pour relier les sommets correspondants dans tous les profils.



## Un exemple de lissage 

L\'outil Lissage est dans le l\'atelier Part, menu Part -\> Lissage\... ou via l\'icône dans la barre d\'outils.

![](images/Part_Loft_Ikon_Ballon_Hilfe.png )

Dans les \"Tâches\", il y aura deux listes : \"Profils disponibles\" et \"Profils sélectionnés\".

![](images/Part_Loft_Liste3.png )

### Sélection des sections 

Dans la liste \"Profils disponibles\", les éléments disponibles sont affichés. Deux sections doivent être sélectionnés l\'un après l\'autre dans cette liste.

![](images/Part_Loft_Liste_Auswahl_3b.png )

Par la suite, la flèche bleue indique quel élément est ajouté à la liste des \"Profils sélectionnés\".

![](images/Part_Loft_Liste_Auswahl_3c.png )

Les éléments sélectionnés doivent être du même type.

Astuce : les éléments actif/sélectionnés dans la liste sont affichés dans la zone 3D comme actif/sélectionné.



### Commande complète 

Si les deux sections sont sélectionnés, la commande peut être appliquée avec le bouton \"OK\".

![](images/Part_Loft_Liste_Auswahl_3d.png )



### Résultat

À partir de lignes fermées, nous obtenons des surfaces qui pourraient être considérées comme un aspect superficiel de solides.

![](images/Part_Loft_geschlossen.png )

Si en effet un solide doit être créé, cocher la case \"Créer le solide\" ou après la création du lissage, basculer sur l\'onglet *propriétés* *données* et mettez *solid* à true.

La procédure est analogue pour les polylignes ouverts.



### Modification de la sélection des sections 

Si vous souhaitez modifier la sélection des sections après la création du loft, vous pouvez sélectionner le champ Sections dans l\'onglet Données et cliquer sur le bouton représentant des points de suspension. La liste de toutes les sections sélectionnables apparaît. La sélection actuelle est mise en surbrillance. Vous pouvez supprimer ou ajouter des sections supplémentaires.

La séquence des sections dépend de la séquence des clics dans la liste. Si vous souhaitez apporter des modifications substantielles, il est recommandé de tout désélectionner en premier puis de recommencer la sélection dans le bon ordre.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/fr
