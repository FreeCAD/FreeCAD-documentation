---
- GuiCommand   */fr
   Name   *Part Loft
   Name/fr   *Part Lissage
   MenuLocation   *Part → Lissage...
   Workbenches   *[Part](Part_Workbench/fr.md)
   Version   *0.13
   SeeAlso   *[Part Balayage](Part_Sweep/fr.md)
---

# Part Loft/fr

## Présentation

L\'outil **Part Lissage** est utilisé pour créer une face, une coquille ou une forme solide à partir de deux ou plusieurs profils. Les profils peuvent être un point (sommet), ligne (Arête), un fil ou une face. Arêtes et fils peuvent être soit ouverts ou fermés. Il existe différents [limites et complications](Part_Loft/fr#Limitations_et_complications.md), voir ci-dessous, mais les profils peuvent provenir des [primitives de l\'atelier Part](Part_Workbench/fr.md), des [objets de l\'atelier Draft](Draft_Workbench/fr.md) et des [esquisses](Sketcher_Workbench/fr.md).

Le Lissage a trois paramètres, \"Surface réglée\", \"Créer le solide\" et \"Fermé\", chacun avec une valeur soit \"true\" (vrai) soit \"false\" (faux).

Si \"Créer le solide\" est à \"true\", FreeCAD crée un solide si les profils sont une géométrie fermée; si \"false\", FreeCAD crée une face ou (si plus d\'une face) une coque pour les profils ouverts ou fermés.

Si \"Surface réglée\" est à \"true\", FreeCAD crée une face, des faces ou un solide depuis les surfaces réglées. [Page de Wikipedia sur Surface réglée.](https   *//fr.wikipedia.org/wiki/Surface_r%C3%A9gl%C3%A9e)

Si \"Fermé\" est à\"true\", FreeCAD essaye de lisser le dernier profil vers le premier profil pour créer une figure fermée.

Pour plus d\'informations sur la façon dont les profils sont réunis, consultez la page [Part Détails techniques du lissage](Part_Loft_Technical_Details/fr.md).

![centre\|Part\_Loft. À partir de trois profils qui sont deux Part Cercles et une Part Ellipse. Les paramètres sont Solide \"True\" et Surface réglée \"True\"](images/Part_Loft_solid_ruled_from3profiles_example_FreeCAD_0_13.jpg )

## Remarques

-   Les objets [App Link](App_Link/fr.md) liés aux types d\'objets appropriés et les conteneurs [App Part](App_Part/fr.md) contenant les objets visibles appropriés peuvent également être utilisés comme profils et trajectoires. {{Version/fr|0.20}}

## Limitations et complications 

-   Un sommet ou un point
    -   Un sommet ou un point ne peuvent être utilisés que dans le premier et/ou le dernier profil dans la liste des profils.
        -   Par exemple    *
            -   vous ne pouvez pas lisser d\'un cercle à un point, à une ellipse.
            -   Cependant vous pourriez Lisser d\'un point à un cercle à une ellipse à un autre point.
-   Les profils de géométrie ouvert ou fermé ne peuvent pas être mélangés dans un seul Lissage.
    -   Dans un Lissage, tous les profils (lignes, fils etc.) doivent être soit ouverts ou fermé.
        -   Par exemple    *
            -   FreeCAD ne peut pas Lisser entre un Cercle et une Ligne.
-   Fonctionnalités de l\'Atelier Draft
    -   Les Fonctionnalités de l\'Atelier Draft peuvent être directement utilisées comme un profil dans FreeCAD 0,14 ou plus tard.
        -   Par exemple, les fonctionnalités suivantes de Draft peuvent être utilisées comme profils dans un Lissage de Pièce
            -   Polygone.
            -   Point, ligne, fil,
            -   B-spline, Courbe de Bézier
            -   Cercle, Ellipse, Rectangle
-   Esquisses de PartDesign
    -   Le profil peut être créé avec un croquis. Toutefois, seule une esquisse valide sera affichée dans la liste pour être disponible pour la sélection.
    -   Le croquis doit contenir un seul fil ou ligne ouverte ou fermée (peut être plusieurs lignes, si ces lignes sont toutes connectées car elles sont alors un seul fil)
-   Atelier Pièce
    -   le profil peut être une pièce primitive géométrique valide qui peut être créée avec un des outils [Primitives](Part_Primitives/fr.md)
        -   par exemple la pièce primitive géométrique suivante peut être un profil valide
            -   point (Sommet), ligne (Arête)
            -   Hélice, Spirale
            -   Cercle, Ellipse
            -   Polygone régulier
            -   Plan (Face)

-   Lissages fermés
    -   Les résultats de lissages fermés peuvent être inattendus - le lissage peut développer des torsions ou déformations. Le Lissage est très sensible au placement des profils et àla complexité des courbes nécessaires pour connecter les sommets correspondant à tous les profils.

## Un exemple de Lissage 

L\'outil Lissage est dans le l\'Atelier Part, menu Part -\> Lissage\... ou via l\'icône dans la barre d\'outils.

![](images/Part_Loft_Ikon_Ballon_Hilfe.png )

Dans les \"Tâches\", il y aura deux listes    * \"Profils disponibles\" et \"Profils sélectionnés\".

![](images/Part_Loft_Liste3.png )

### Sélection des sections 

Dans la liste \"Profils disponibles\", les éléments disponibles sont affichés. Deux sections doivent être sélectionnés l\'un après l\'autre dans cette liste.

![](images/Part_Loft_Liste_Auswahl_3b.png )

Par la suite, la flèche bleue indique quel élément est ajouté à la liste des \"Profils sélectionnés\".

![](images/Part_Loft_Liste_Auswahl_3c.png )

Les éléments sélectionnés doivent être du même type.

Astuce    * les éléments actif/sélectionnés dans la liste sont affichés dans la zone 3D comme actif/sélectionné.

### Commande complète 

Si les deux sections sont sélectionnés, la commande peut être appliquée avec le bouton \"OK\".

![](images/Part_Loft_Liste_Auswahl_3d.png )

### Résultat

À partir de lignes fermées, nous obtenons des surfaces qui pourraient être considérées comme un aspect superficiel de solides.

![](images/Part_Loft_geschlossen.png )

Si en effet un solide doit être créé, cocher la case \"Créer le solide\" ou après la création du Lissage, basculer sur l\'onglet *propriétés* *données* et mettez *solid* à true.

La procédure est analogue pour les polylignes ouverts.

### Modification de la sélection des sections 

Si vous souhaitez modifier la sélection des sections après la création du loft, vous pouvez sélectionner le champ Sections dans l\'onglet Données et cliquer sur le bouton représentant des points de suspension. La liste de toutes les sections sélectionnables apparaît. La sélection actuelle est mise en surbrillance. Vous pouvez supprimer ou ajouter des sections supplémentaires.

La séquence des sections dépend de la séquence des clics dans la liste. Si vous souhaitez apporter des modifications substantielles, il est recommandé de tout désélectionner en premier puis de recommencer la sélection dans le bon ordre.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/fr
