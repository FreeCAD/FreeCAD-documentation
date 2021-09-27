---
- GuiCommand:/fr
   Name:Arch Site
   Name/fr:Arch Site
   MenuLocation:Arch → Site
   Workbenches:[Arch](Arch_Workbench/fr.md)
   Shortcut:**S** **I**
   SeeAlso:[Arch Niveaux](Arch_Floor/fr.md), [Arch Bâtiment](Arch_Building/fr.md)
---

# Arch Site/fr

## Description

**Arch Site** est un objet spécial qui combine les propriétés d\'un objet groupe FreeCAD standard et un objet Arch. Il est particulièrement adapté pour représenter un site entier, ou un terrain. Dans un travail architectural fait d\'IFC, il est surtout utilisé pour organiser votre modèle qui contient un objet [Arch Bâtiment](Arch_Building/fr.md). Arch Site est également utilisé pour gérer et afficher un terrain physique et peut calculer le volume de terre a ajouter ou a supprimer.

## Utilisation

1.  Optionnellement, sélectionnez un ou plusieurs objets pour les inclure dans votre nouveau site.
2.  Pressez le bouton **<img src="images/Arch_Site.svg" width=16px> [Crée un objet site...](Arch_Site/fr.md)** ou pressez les touches **S** puis **I**.

## Options

-   Après la création d\'un site, vous pouvez ajouter des objets par glisser-déposer dans l\'arborescence ou en utilisant l\'outil **<img src="images/Arch_Add.svg" width=16px> [Arch Ajouter](Arch_Add/fr.md)**. Cela détermine uniquement quel objet fait partie du site donné et n\'a aucun effet sur le terrain lui-même.
-   Vous pouvez supprimer les objets d\'un site par un glisser-déposer hors du site ou de la vue arborescente ou en utilisant l\'outil **<img src="images/Arch_Remove.svg" width=16px> [Arch Soustraire](Arch_Remove/fr.md)**.
-   Vous pouvez ajouter un objet terrain en éditant le site propriété {{PropertyData/fr|Terrain}}. Le terrain doit être une coquille ouverte (open shell) ou une surface.
-   Vous pouvez ajouter ou les soustraire des volumes du terrain de base, en double-cliquant sur le site, et ajouter des objets à ces soustractions ou groupes ajoutés. Les objets doivent être des solides.
-   La propriété {{PropertyData/fr|Extrusion Vector}} peut être utilisée pour résoudre certains problèmes qui peuvent apparaître lorsque vous travaillez avec des soustractions et des additions. Afin de réaliser ces additions/soustractions, la surface du terrain doit être extrudée en un solide, qui est ensuite convenablement fusionnée/soustraite. En fonction de la topologie du terrain, cette extrusion peut échouer avec le vecteur d\'extrusion par défaut. Vous pourrez donc être en mesure de remédier au problème en changeant sa valeur.

## Propriétés

### Data

-    {{PropertyData/fr|Terrain}}: Le terrain de base du site

-    {{PropertyData/fr|Address}}: L\'adresse du site (rue numéro)

-    {{PropertyData/fr|Postal Code}}: Le code postal

-    {{PropertyData/fr|City}}: La ville du site

-    {{PropertyData/fr|Country}}: Le pays du site

-    {{PropertyData/fr|Latitude}}: La latitude du site

-    {{PropertyData/fr|Longitude}}: La longitude du site

-    {{PropertyData/fr|Url}}: L\'adresse URL du site sur une carte web

-    {{PropertyData/fr|Projected Area}}: La surface de projection de l'objet dans le plan XY

-    {{PropertyData/fr|Perimeter}}: La longueur du périmètre du terrain

-    {{PropertyData/fr|Addition Volume}}: Le volume de terre a ajouter dans le terrain

-    {{PropertyData/fr|Subtraction Volume}}: Le volume de terre a soustraire du terrain

-    {{PropertyData/fr|Extrusion Vector}}: Le vecteur d\'extrusion a utiliser pour une opéraion booléenne

-    {{PropertyData/fr|Remove Splitter}}: Efface le splitter de la forme résultante

-    {{PropertyData/fr|Declination}}: L'angle entre le nord vrai et le nord dans ce document, c'est-à-dire l'axe des Y. {{version/fr|0.18}} Cela signifie que par défaut (déclinaison de 0 degré) le Nord pointe vers l'axe Y et est vers l'est dans l\'Axe X; l\'angle est incrémenté dans les sens contraire des aiguilles d\'une montre. Cette propriété était connue auparavant comme une {{PropertyData/fr|North Deviation}}.

-    {{PropertyData/fr|EPW File}}: Permet de joindre à ce site un fichier EPW provenant du [site Ladybug données EPW](https://www.ladybug.tools/epwmap/). Ceci est nécessaire pour afficher les diagrammes de la rose des vents. {{version/fr|0.19}}

### Vue

-    {{PropertyView/fr|Solar Diagram}}: Affiche ou cache le diagramme du soleil

-    {{PropertyView/fr|Solar Diagram Color}}: La couleur du diagramme du soleil

-    {{PropertyView/fr|Solar Diagram Position}}: La position du diagramme du soleil

-    {{PropertyView/fr|Solar Diagram Scale}}: L\'échelle du diagramme du soleil

-    {{PropertyView/fr|Wind Rose}}: Affiche ou masque le diagramme de la rose des vents (nécessite que la propriété de données **EPW File** soit remplie et que le module Python de Ladybug soit installé (voir ci-dessous)

## Travail typique 

Commencez par créer un objet qui représente votre terrain. Ce doit être une surface ouverte pas un solide. Par exemple, il est facile d\'importer des données de maillage, qui peuvent être transformées en une forme de pièce à partir du menu **Part → Créer une forme à partir d'un maillage**. Créez ensuite un objet Site et définissez sa propriété {{PropertyData/fr|Terrain}} sur la pièce que nous venons de créer:

![](images/Arch_site_example_01.jpg )

Créez les volumes (les volumes doivent être des solides) qui représentent les surfaces à travailler. Double cliquez sur l\'objet Site dans la vue 3D, et ajoutez ou soustrayez ces volumes du groupe. Cliquez sur OK.

![](images/Arch_site_example_02.jpg )

La géométrie du site est alors calculée, les surfaces les périmètres et volumes sont automatiquement recalculés.

![](images/Arch_site_example_03.jpg )

## Diagrammes solaires et éoliens 

Si _ peut afficher un diagramme solaire et/ou une rose des vents. Pour cela, les propriétés {{PropertyData/fr|Longitude}}, {{PropertyData/fr|Latitude}} et {{PropertyData/fr|NorthDeviation}} doivent être correctement définies et {{PropertyView/fr|SolarDiagram}} ou {{PropertyView/fr|Wind Rose}} activée `True`. Respectivement {{Version/fr|0.17}} et {{Version/fr|0.19}}

**Remarque**: Si vous n\'avez pas Ladybug, [pysolar](http://pysolar.org/) est toujours pris en charge pour générer des diagrammes solaires mais pas les roses des vents. Pysolar 0.7 ou supérieur est requis. Cette version ne fonctionne qu\'avec Python 3. Si vous avez besoin de cette fonctionnalité avec Python 2, vous devriez avoir Pysolar 0.6 car c\'est la dernière version qui fonctionne avec Python 2. Cependant, Ladybug est un outil beaucoup plus puissant qui sera probablement plus utilisé dans l\'avenir. Nous vous recommandons donc de l\'utiliser au lieu de pysolar. Ladybug peut être installé simplement via [pip](https://github.com/ladybug-tools/ladybug).

![](images/Freecad-solar-diagram.jpg )

## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil site est utilisable dans une [macro](macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
Site = makeSite(objectslist=None, baseobj=None, name="Site")
```

-   Crée un objet `Site` à partir de `objectlist` qui est une liste d\'objets ou `baseobj` qui est un `Shape` ou `Terrain`.

Exemple: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Building = Arch.makeBuilding([Wall])
Site = Arch.makeSite([Building])

FreeCAD.ActiveDocument.recompute()
FreeCAD.Gui.ActiveDocument.ActiveView.viewIsometric()
```

### Diagramme solaire 

Tant que le module `pysolar` est présent, un diagramme solaire peut être ajouté au site. Définissez les angles de longitude, de latitude et de déclinaison selon les besoins, ainsi qu\'une échelle adéquate pour la taille de votre modèle.

Veuillez noter que Pysolar 0.7 ou supérieur est requis et que cette version ne fonctionne qu\'avec Python 3.


```python
Site.Longitude = -46.38
Site.Latitude = -23.33
Site.Declination = 30
#Site.Compass = True

Site.ViewObject.SolarDiagram = True
Site.ViewObject.SolarDiagramScale = 10000
FreeCAD.ActiveDocument.recompute()
```

### Diagramme solaire indépendant du site 

Solar diagram peut aussi être créé avec la fonction suivante 
```python
Node = makeSolarDiagram(longitude, latitude, scale=1, complete=False)
```

-   Crée un diagramme solaire en tant que nœud Pivy en utilisant `longitude` et `latitude` avec `scale` facultatif.
-   Si `complete` est mis à `True`, les 12 mois sont montrés ce qui affiche l\'[Analemme](https://fr.wikipedia.org/wiki/Analemme).


```python
import FreeCADGui, Arch

Node = Arch.makeSolarDiagram(-46.38, -23.33, scale=10000, complete=True)
FreeCAD.Gui.ActiveDocument.ActiveView.getSceneGraph().addChild(Node)
```

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Site/fr
