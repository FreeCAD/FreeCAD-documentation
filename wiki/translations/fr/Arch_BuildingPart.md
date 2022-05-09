---
- GuiCommand   */fr
   Name   *Arch BuildingPart
   Name/fr   *Arch Partie de bâtiment
   MenuLocation   *Arch → Partie de bâtiment
   Workbenches   *[Arch](Arch_Workbench/fr.md)
   Version   *0.18
   SeeAlso   *[Arch Bâtiment](Arch_Building/fr.md), [Arch Site](Arch_Site/fr.md)
---

# Arch BuildingPart/fr

## Description

Partie de bâtiment (BuildingPart) remplace les anciens [Arch Niveaux](Arch_Floor/fr.md) et [Arch Bâtiment](Arch_Building/fr.md) par une version plus performante qui peut être utilisée non seulement pour créer un plancher/étage/niveaux mais également pour toutes sortes de situations dans lesquelles différents objets Arch/BIM doivent être groupés. Ce groupe pourra être traité comme un seul objet ou répliqué.

## Utilisation

1.  En option, vous pouvez également sélectionner un ou plusieurs objets à inclure dans votre nouvelle Partie de bâtiment.
2.  Appuyez sur le bouton **<img src="images/Arch_BuildingPart.svg" width=16px> [Partie de bâtiment](Arch_BuildingPart/fr.md)**.

### Remarques

Les Partie de bâtiment ont un [Arch Plan de section](Arch_SectionPlane/fr.md) implicite intégré. {{Version/fr|0.19}}

Ce plan est toujours parallèle au plan de base du BuildingPart, mais vous pouvez spécifier le décalage entre eux. Ainsi, tous les outils qui fonctionnent avec un plan de coupe, tels que [Draft Vue 2D d\'une forme](Draft_Shape2DView/fr.md) et [TechDraw Vue Architecturale](TechDraw_ArchView/fr.md) fonctionnent également avec Parties de bâtiment.

## Options

-   Après avoir créé une Partie de bâtiment, vous pouvez ajouter d\'autres objets à celui-ci en les faisant glisser dans la vue en arborescence ou en utilisant l\'outil **<img src="images/Arch_Add.svg" width=16px> [Arch Ajouter](Arch_Add/fr.md)**.
-   Vous pouvez supprimer des objets d\'une Partie de bâtiment en les faisant glisser dans l\'arborescence ou en utilisant l\'outil **<img src="images/Arch_Remove.svg" width=16px> [Arch Soustraire](Arch_Remove/fr.md)**.
-   En double-cliquant sur l\'objet Partie de bâtiment dans la vue arborescente, le [Draft Plan de travail](Draft_SelectPlane/fr.md) sera défini sur son emplacement et la Partie de bâtiment deviendra active, ce qui signifie que de nouveaux objets lui seront automatiquement ajoutés. Double-cliquez à nouveau sur la Partie de bâtiment pour la désactiver et ramener le plan de travail à sa position précédente. (dans la version 0.19, pour être disponible, cette option doit être définie sur true, dans le panneau Propriété - Interaction - Double-cliquer pour active).
-   La Partie de bâtiment peut afficher une marque dans la vue 3D avec une étiquette et une indication de niveau.
-   Lorsqu\'un élément Partie de bâtiment est déplacé/pivoté, tous ses enfants qui ne possèdent pas de propriété **Move With Host** ou qui l\'ont activé sont déplacés/pivotés ensemble.
-   Les Parties de bâtiment peuvent être [Draft Clonées](Draft_Clone/fr.md).
-   Les Parties de bâtiment peuvent prendre n'importe quel type d'IFC. Leur propriété **IFC Type** détermine son utilisation. Si vous la définissez sur **Building Storey**, ce sera comme un niveau. Si vous la définissez sur **Building**, ce sera comme un bâtiment et si vous la définissez sur **Element Assembly**, ce sera comme un assemblage. Son icône changera pour refléter ce paramètre mais à part cela, cela n'a aucun autre impact dans FreeCAD. Toutefois, le fait d\'être exporté vers IFC sous un type ou un autre peut avoir un impact sur d\'autres applications BIM.
-   Les Parties de bâtiment permettent de définir une **boîte de capture de groupe automatique**. Les objets Draft et Arch suivants, ou tout autre objet qui utilise Draft.autogroup(), seront automatiquement ajoutés à cet objet Partie de bâtiment s\'ils se trouvent entièrement à l\'intérieur de la boîte de capture. {{Version/fr|0.20}}

## Propriétés

Voir aussi    * [Éditeur de propriétés](Property_editor/fr.md)

Une Arch Partie de bâtiment est dérivé d\'un objet [App GeoFeature](App_GeoFeature/fr.md) et hérite de toutes ses propriétés. Elle possède également les propriétés supplémentaires suivantes    *

### Données


{{TitleProperty|Base}}

-    **Group|LinkList**   * Liste des objets référencés.

-    **_ Group Touched|Bool|Hidden**
    


{{TitleProperty|Building Part}}

-    **Area|Area**   * La surface calculée de cet étage.

-    **Height|Length**   * La hauteur de cet objet et de ses objets enfants. Les objets enfants peuvent être, par exemple, des [Arch Walls](Arch_Wall/fr.md). La hauteur de chaque mur doit être définie sur `0` (zéro) de sorte que la propriété de hauteur du BuildingPart se propage aux objets qu\'il contient.

-    **Level Offset|Length**   * Le niveau du point (0,0,0) de ce niveau. Cette valeur est ajoutée à l\'attribut `Placement.Base.z` du BuildingPart, pour indiquer un décalage vertical sans déplacer réellement l\'objet. Le décalage résultant est affiché si **Show Level** est `True`.

-    **Tableau des matériaux|Map|Hidden**   * Une carte MaterialName   *SolidIndexesList qui associe les noms de matériaux à des index de solides à utiliser pour référencer cet objet à partir d\'autres fichiers.

-    **Only Solids|Bool**   * Si mis à true, seuls les solides seront collectés par cet objet lorsqu\'il sera référencé à partir d\'autres fichiers.

-    **Saved Inventor|FileIncluded|Hidden**   * Cette propriété stocke une représentation de l\'inventeur pour cet objet.

-    **Shape|PartShape|Hidden**   * La forme de cet objet.


{{TitleProperty|Children}}

-    **Height Propagate|Bool**   * Si vrai, la valeur de la hauteur se propage aux objets contenus.


{{TitleProperty|IFC}}

-    **Ifc Data|Map|Hidden**   * Données IFC.

-    **Ifc Properties|Map|Hidden**   * Les propriétés IFC de cet objet.

-    **Ifc Type|Enumeration**   * Le type IFC de cet objet.


{{TitleProperty|IFC Attributes}}

-    **Description|String**   * Une description facultative pour ce composant.

-    **Global Id|String**
    

-    **Object Type|String**
    

-    **Overall Height|Length**
    

-    **Overall Width|Length**
    

-    **Partitioning Type|Enumeration**
    

-    **Predefined Type|Enumeration**
    

-    **Tag|String**   * Une balise facultative pour ce composant.

-    **User Defined Partitioning Type|String**
    

### Vue


{{TitleProperty|Auto Group}}

-    **Autogroup Autosize|Bool**   * Définit automatiquement la taille de la boîte de capture à partir du contenu de Partie de bâtiment. {{Version/fr|0.20}}

-    **Autogroup Box|Bool**   * Active/désactive le regroupement automatique (et l\'affichage de la boîte de capture). {{Version/fr|0.20}}

-    **Autogroup Margin|Length**   * Une marge à utiliser lorsque la taille automatique est activée. {{Version/fr|0.20}}

-    **Autogroup Size|IntegerList**   * La boîte de capture pour les objets nouvellement créés, exprimée en \[XMin,YMin,ZMin,XMax,YMax,ZMax\]. {{Version/fr|0.20}}


{{TitleProperty|Building Part}}

-    **Diffuse Color|ColorList|Hidden**   * Les couleurs individuelles de la face.

-    **Display Offset|Placement**   * Une transformation à appliquer à la marque de niveau.

-    **Font Name|Font**   * La police à utiliser pour les textes.

-    **Font Size|Length**   * La taille de la police des textes.

-    **Line Width|Float**   * La largeur de ligne de cet objet.

-    **Origin Offset|Bool**   * Si true, lorsqu\'il est activé, le décalage d\'affichage affectera également la marque d\'origine.

-    **Override Unit|String**   * Une unité facultative pour exprimer les niveaux.

-    **Show Label|Bool**   * Si true, l\'étiquette de l\'objet est affichée lorsqu\'elle est activée.

-    **Show Level|Bool**   * Si true, affiche le niveau.

-    **Show Unit|Bool**   * Si true, affiche l\'unité sur l\'étiquette du niveau.


{{TitleProperty|Children}}

-    **Couleur de ligne des enfants|Couleur**   * La couleur de ligne à appliquer aux enfants de cette Partie de bâtiment.

-    **Children Line Width|Float**   * La largeur de ligne à appliquer aux enfants de cette Partie de bâtiment.

-    **Children Override|Bool**   * Si true, les objets contenus dans cette Partie de bâtiment adopteront ces paramètres de ligne, de couleur et de transparence.

-    **Children Shape Color|Color**   * La couleur de forme à appliquer aux enfants de cette Partie de bâtiment.

-    **Children Transparency|Percent**   * La transparence à appliquer aux enfants de cette Partie de bâtiment.


{{TitleProperty|Clip}}

-    **Auto Cut View|Bool**   * Active la découpe lors de l\'activation de ce niveau.

-    **Cut Margin|Length**   * La distance entre le plan du niveau et la ligne de coupe.

-    **Cut View|Bool**   * Coupe la vue au-dessus de ce niveau.


{{TitleProperty|Interactions}}

-    **Auto Working Plane|Bool**   * Si la valeur est True, le plan de travail sera maintenu en mode Auto.

-    **Double Click Activates|Bool**   * Si True, un double-clic sur cet objet dans l\'arbre l\'active.

-    **Restore View|Bool**   * Si cette option est activée, la vue stockée dans cet objet sera restaurée lors d\'un double-clic.

-    **Save Inventor|Bool**   * Si cette option est activée, la représentation de l\'inventeur de cet objet sera enregistrée dans le fichier FreeCAD, ce qui permettra de le référencer dans d\'autres fichiers en mode léger.

-    **Saved Inventor|FileIncluded|Hidden**   * Un emplacement pour enregistrer la représentation de l\'inventeur de cet objet, s\'il est activé.

-    **Set Working Plane|Bool**   * Si true, lorsqu\'il est activé, le plan de travail s\'adaptera automatiquement à cet élément de construction.

-    **View Data|FloatList|Hidden**   * Données de position de la caméra associées à cet objet.

## Script


**Voir aussi   ***

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Partie de bâtiment (BuildingPart) peut être utilisé à l\'intérieur d\'une [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante    *


```python
BuildingPart = makeBuildingPart(objectslist=None)
```

-   Crée un objet `BuildingPart` à partir de `objectslist` qui est une liste d\'objets.

Exemple    * 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch BuildingPart/fr
