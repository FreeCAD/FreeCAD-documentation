---
- GuiCommand:
   Name:EM FHPath
   Name/fr:EM Chemin FH
   MenuLocation:EM - FHPath
   Workbenches:[EM](EM_Workbench/fr.md)
   Shortcut:**E** **T**
   Version:0.17
   SeeAlso:[EM Noeud FH](EM_FHNode/fr.md), [EM Segment FH](EM_FHSegment/fr.md)
---

# EM FHPath/fr

## Description

L\'outil Chemin FH insère un objet FHPath, c\'est-à-dire un ensemble de segments FastHenry le long d\'un chemin.

![](images/EM_FHPath_Example.png )



*Chemin FH FastHenry*

## Utilisation

L\'objet Chemin FH peut être basé sur n\'importe quelle forme contenant des bords, mais l\'objet Chemin FH est conçu pour fonctionner au mieux avec le support d\'une esquisse ou d\'une polyligne.

1.  Sélectionnez un ou plusieurs objets contenant des bords.
2.  Appuyez sur le bouton **<img src="images/EM_FHPath.svg" width=16px> [EM FHPath](EM_FHPath/fr.md)** ou appuyez sur **E** puis sur **T**. Autant d\'objets FHPath seront créés que les objets sélectionnés.

### Remarques

-   Le Chemin FH créera un ensemble de Noeuds FH et un ensemble de segments FastHenry suivant le chemin formé par les bords.

-   Les bords incurvés seront discrétisés selon les paramètres des propriétés du Chemin FH.

-   Si les segments résultants sont trop courts par rapport à la section transversale, un avertissement sera émis dans la fenêtre Rapport de FreeCAD, car cela peut provoquer des problèmes dans les simulations FastHenry.

-   L\'orientation par défaut des sections transversales du segment FHPath est celle par défaut de FastHenry: le vecteur le long de la largeur est parallèle au plan XY; si la largeur est dans la direction Z, le vecteur largeur est aligné sur l\'axe X. Vous pouvez modifier l\'orientation de la section transversale du premier segment du FHPath en spécifiant la propriété vectorielle **ww**. Cela se fait dans le système de coordonnées de placement de base, c\'est-à-dire que les changements dans le placement préservent l\'orientation relative des connexions croisées sans changer **ww**. Les segments suivants sont automatiquement orientés en appliquant tour à tour les rotations correspondant à l\'angle entre chaque paire de segments. Le premier segment est identifié par le premier nœud de l\'objet FHPath comme indiqué dans l\'arborescence (le plus haut est le premier nœud, quel que soit son nom/numérotation), ou de manière équivalente comme le premier nœud dans le **Nodes** FHPath liste des propriétés.

-   Un Chemin FH aura au moins un Noeud FH de départ et un Noeud FH de fin, s\'il y a au moins un bord dans l\'objet de base. L\'objet FHNode de début et le FHNode de fin seront les mêmes si vous modifiez le chemin, en incluant ou en supprimant des bords de l\'objet de base, ou en modifiant la discrétisation FHPath. Par conséquent, lors du changement de FHPath, vous n\'avez pas à vous soucier des connexions à d\'autres objets déjà effectuées à l\'aide des points de terminaison FHPath, par ex. si vous avez utilisé les points de terminaison comme point de départ pour les objets FHSegment, les objets FHPort, les objets FHEquiv ou les connexions à un objet FHPlane. En particulier, lorsque vous modifiez un FHPath provoquant la création de plusieurs segments, la liste d\'objets FHNode déjà existante sera simplement étendue et les anciennes positions FHNode seront réorganisées. Si, à la place, vous modifiez un FHPath entraînant la suppression de segments, la liste des objets FHNode sera raccourcie et les objets FHNode excédentaires supprimés du document, sauf si l\'un des FHNode a déjà été utilisé dans un autre objet (par exemple, si vous avez utilisé un nœud intermédiaire pour créer un FHSegment). Dans ce cas, le FHNode sera conservé, mais en dehors de l\'objet FHPath, et la connexion sera peut-être suspendue; il appartient à l\'utilisateur de garantir l\'exactitude des connexions.

-   Vous ne pouvez pas déplacer librement l\'objet Chemin FH ou ses Noeuds FH. Pour modifier la position du Chemin FH, déplacez l\'objet de base sous-jacent (l\'objet de base est masqué par défaut, vous pouvez l\'afficher à nouveau en sélectionnant l\'objet dans l\'arborescence et en appuyant sur **Espace**.

-   Les bords incurvés seront discrétisés en un ensemble de segments conformément à la propriété de Chemin FH **Discr**.

## Propriétés

-    **Base**: objet de base sur lequel ce composant est construit.

-    **Nodes**: (lecture seule) La liste de [Noeud FH](EM_FHNode/fr.md) le long du chemin. Pas pour la modification directe de l\'utilisateur.

-    **Width**: largeur des segments du Chemin FH (paramètre de segment \'w\' dans FastHenry).

-    **Height**: hauteur des segments du Chemin FH (paramètre de segment \'h\' dans FastHenry).

-    **Discr**: nombre maximum de segments dans lesquels les bords courbes seront discrétisés.

-    **Sigma**: conductivité des segments du Chemin FH (paramètre de segment \'sigma\' dans FastHenry).

-    **ww**: direction de la section le long de la largeur du premier segment du FHPath (paramètre de segment \'wx\', \'wy\', \'wz\' dans FastHenry).

-    **nhinc**: nombre de filaments dans le sens de la hauteur (paramètre de segment \'nhinc\' dans FastHenry).

-    **nwinc**: nombre de filaments dans le sens de la largeur (paramètre de segment \'nwinc\' dans FastHenry).

-    **rh**: rapport des filaments adjacents dans la direction de la hauteur (paramètre de segment \'rh\' dans FastHenry).

-    **rw**: rapport des filaments adjacents dans le sens de la largeur (paramètre de segment \'rw\' dans FastHenry).

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Chemin FH peut-être utilisé dans des [macros](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante:


```python
path = makeFHPath(baseobj=None,name='FHPath')
```

-   Crée un objet `FHPath`.

-    `baseobj`est l\'objet qui peut être utilisé comme base pour le Chemin FH. Si aucun `baseobj` n\'est donné, l\'utilisateur doit attribuer un objet de base ultérieurement, pour pouvoir utiliser cet objet. `baseobj` est obligatoire et peut être n\'importe quelle forme contenant des bords, même si l\'objet FHPath est conçu pour fonctionner au mieux avec le support d\'une esquisse ou d\'un fil.

-    `name`est le nom de l\'objet.

Exemple:


```python
import FreeCAD, EM
from FreeCAD import Base
import Part, PartGui
spiral = App.ActiveDocument.addObject("Part::Spiral","Spiral")
spiral.Growth=1.00
spiral.Rotations=4.00
spiral.Radius=1.00
spiral.Placement=Base.Placement(Base.Vector(0.00,0.00,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
spiral.Label='Spiral'

fhpath = EM.makeFHPath(spiral)
fhpath.Discr = 40
App.ActiveDocument.recompute()
```





{{EM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [EM](Category_EM.md) > EM FHPath/fr
