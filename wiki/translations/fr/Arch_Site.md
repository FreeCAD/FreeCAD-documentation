---
 GuiCommand:
   Name: Arch Site
   Name/fr: Arch Site
   MenuLocation: 3D/BIM , Site
   Workbenches: BIM_Workbench/fr
   Shortcut: **S** **I**
   SeeAlso: 
---

# Arch Site/fr

## Description

**Arch Site** est un objet spécial qui combine les propriétés d\'un objet groupe FreeCAD standard et des objets Arch. Il est particulièrement adapté pour représenter un site entier ou un terrain. Dans un travail architectural fait d\'IFC, il est surtout utilisé pour organiser votre modèle qui contient des objets de [bâtiments](Arch_Building/fr.md). Arch Site est également utilisé pour gérer et afficher un terrain physique et peut calculer le volume de terre a ajouter ou a supprimer.



## Utilisation

1.  Vous pouvez sélectionner un ou plusieurs objets pour les inclure dans votre nouveau site.
2.  Pressez le bouton **<img src="images/Arch_Site.svg" width=16px> [Site](Arch_Site/fr.md)** ou pressez les touches **S** puis **I**.

## Options

-   Après la création d\'un site, vous pouvez ajouter des objets par glisser-déposer dans la [vue en arborescence](Tree_view/fr.md) ou en utilisant le bouton **<img src="images/Arch_Add.svg" width=16px> [Arch Ajouter](Arch_Add/fr.md)**. Cela ne détermine que les objets qui font partie du site donné et n\'a aucun effet sur le terrain.
-   Vous pouvez supprimer les objets d\'un site par un glisser-déposer hors du site de la [vue en arborescence](Tree_view/fr.md) ou en utilisant le bouton **<img src="images/Arch_Remove.svg" width=16px> [Arch Supprimer](Arch_Remove/fr.md)**.
-   Vous pouvez ajouter un objet terrain en modifiant la propriété **Terrain** du site. Le terrain peut être une coque ouverte ou ({{Version/fr|0.21}}) un solide.
-   Vous pouvez ajouter des volumes à ajouter ou à soustraire du terrain de base en double-cliquant sur le site et en ajoutant des objets à ses groupes Additions ou Soustractions. Les objets doivent être des solides.
-   La propriété **Extrusion Vector** peut être utilisée pour résoudre certains problèmes qui peuvent apparaître lorsque le terrain est une coque ouverte et qu\'il y a des additions et/ou des soustractions. Afin d\'effectuer ces additions/soustractions, la coque ouverte est extrudée en un solide, qui est ensuite assemblé/soustrait de manière appropriée. Selon la topologie du terrain, cette extrusion peut échouer avec le vecteur d\'extrusion par défaut. Vous pouvez alors remédier au problème en modifiant cette valeur. Cette propriété est ignorée si le terrain est un solide.



## Propriétés



### Données

-    **Terrain**: terrain de base du site

-    **Address**: adresse du site (rue numéro)

-    **Postal Code**: code postal

-    **City**: ville du site

-    **Country**: pays du site

-    **Latitude**: latitude du site

-    **Longitude**: longitude du site

-    **Url**: adresse URL du site sur une carte web

-    **Projected Area**: surface de projection de l'objet dans le plan XY

-    **Perimeter**: longueur du périmètre du terrain

-    **Addition Volume**: volume de terre a ajouter dans le terrain

-    **Subtraction Volume**: volume de terre a soustraire du terrain

-    **Extrusion Vector**: vecteur d\'extrusion a utiliser pour une opéraion booléenne

-    **Remove Splitter**: efface les séparations de la forme résultante

-    **Declination**: angle entre le nord vrai et le nord dans ce document, c'est-à-dire l'axe des Y. Cela signifie que par défaut (déclinaison de 0 degré) le Nord pointe vers l'axe Y et est vers l'est dans l\'Axe X; l\'angle est incrémenté dans les sens contraire des aiguilles d\'une montre. Cette propriété était connue auparavant comme une **North Deviation**.

-    **EPW File**: permet de joindre à ce site un fichier EPW provenant du [site web de données EPW de Ladybug](https://www.ladybug.tools/epwmap/). Ceci est nécessaire pour afficher les diagrammes de la rose des vents.



### Vue

-    **Solar Diagram**: affiche ou cache le diagramme du soleil

-    **Solar Diagram Color**: couleur du diagramme du soleil

-    **Solar Diagram Position**: position du diagramme du soleil

-    **Solar Diagram Scale**: échelle du diagramme du soleil

-    **Wind Rose**: affiche ou masque le diagramme de la rose des vents (nécessite que la propriété de données **EPW File** soit remplie et que le module Python de Ladybug soit installé (voir ci-dessous)



## Flux de travail typique 

Commencez par créer un objet qui représente votre terrain. Par exemple, il est facile d\'importer des données de maillage, qui peuvent être transformées en une Part Forme à partir du menu **Part → Créer une forme à partir d'un maillage**. Créez ensuite un objet Site et définissez sa propriété **Terrain** sur la pièce que nous venons de créer :

![](images/Arch_site_example_01.jpg )

Créez les volumes (les volumes doivent être des solides) qui représentent les surfaces à travailler. Double cliquez sur l\'objet Site dans la vue 3D, et ajoutez ou soustrayez ces volumes du groupe. Cliquez sur OK.

![](images/Arch_site_example_02.jpg )

La géométrie du site est alors calculée, les surfaces les périmètres et volumes sont automatiquement recalculés.

![](images/Arch_site_example_03.jpg )



## Diagrammes solaires et éoliens 

Si [Ladybug](https://www.ladybug.tools/ladybug.html) est installé, [Arch Site](Arch_Site/fr.md) peut afficher un diagramme solaire et/ou une rose des vents. Pour cela, les propriétés **Longitude**, **Latitude** et **NorthDeviation** doivent être correctement définies et {{PropertyView/fr|SolarDiagram}} ou {{PropertyView/fr|Wind Rose}} activée `True`.

**Remarque** : si vous n\'avez pas Ladybug, [pysolar](http://pysolar.org/) est toujours pris en charge pour générer des diagrammes solaires mais pas les roses des vents. Pysolar 0.7 ou supérieur est requis. Cependant, Ladybug est un outil beaucoup plus puissant qui sera probablement plus utilisé dans l\'avenir. Nous vous recommandons donc de l\'utiliser au lieu de pysolar. Ladybug peut être installé simplement via [pip](https://github.com/ladybug-tools/ladybug).

![](images/Freecad-solar-diagram.jpg )



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Site est utilisable dans une [macro](Macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
Site = makeSite(objectslist=None, baseobj=None, name="Site")
```

-   Crée un objet `Site` à partir de `objectlist` qui est une liste d\'objets ou `baseobj` qui est un `Shape` ou `Terrain`.

Exemple : 
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

Un diagramme solaire peut être créé avec la fonction suivante, indépendamment de tout site. 
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





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Site/fr
