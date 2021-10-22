---
- GuiCommand:/fr
   Name:EM FHPath
   Name/fr:EM FHPath
   MenuLocation:EM → FHPath
   Workbenches:[EM](EM_Workbench/fr.md) (Addon)
   Shortcut:**E** **T**
   SeeAlso:[EM FHNode](EM_FHNode/fr.md), [EM FHSegment](EM_FHSegment/fr.md)
   Version:0.17
---

# EM FHPath/fr

## Description

L\'outil FHPath insère un objet FHPath, c\'est-à-dire un ensemble de segments FastHenry le long d\'un chemin.

![](images/EM_FHPath_Example.png ) 
*FastHenry FHPath*

## Utilisation

L\'objet FHPath peut être basé sur n\'importe quelle forme contenant des bords, mais l\'objet FHPath est conçu pour fonctionner au mieux avec le support d\'une esquisse ou d\'un fil.

1.  Sélectionnez un ou plusieurs objets contenant des bords.
2.  Appuyez sur le bouton **<img src="images/EM_FHPath.svg" width=16px> [EM FHPath](EM_FHPath/fr.md)** ou appuyez sur **E** puis sur **T**. Autant d\'objets FHPath seront créés que les objets sélectionnés.

### Remarques

-   Le FHPath créera un ensemble de FHNodes et un ensemble de segments FastHenry suivant le chemin formé par les bords.

-   Les bords incurvés seront discrétisés selon les paramètres des propriétés FHPath.

-   Si les segments résultants sont trop courts par rapport à la section transversale, un avertissement sera émis dans la fenêtre Rapport de FreeCAD, car cela peut provoquer des problèmes dans les simulations FastHenry.

-   L\'orientation par défaut des sections transversales du segment FHPath est celle par défaut de FastHenry: le vecteur le long de la largeur est parallèle au plan XY; si la largeur est dans la direction Z, le vecteur largeur est aligné sur l\'axe X. Vous pouvez modifier l\'orientation de la section transversale du premier segment du FHPath en spécifiant la propriété vectorielle {{PropertyData/fr|ww}}. Cela se fait dans le système de coordonnées de placement de base, c\'est-à-dire que les changements dans le placement préservent l\'orientation relative des connexions croisées sans changer {{PropertyData/fr|ww}}. Les segments suivants sont automatiquement orientés en appliquant tour à tour les rotations correspondant à l\'angle entre chaque paire de segments. Le premier segment est identifié par le premier nœud de l\'objet FHPath comme indiqué dans l\'arborescence (le plus haut est le premier nœud, quel que soit son nom/numérotation), ou de manière équivalente comme le premier nœud dans le {{PropertyData/fr|Nodes}} FHPath liste des propriétés.

-   Un FHPath aura au moins un FHNode de départ et un FHNode de fin, s\'il y a au moins un bord dans l\'objet de base. L\'objet FHNode de début et le FHNode de fin seront les mêmes si vous modifiez le chemin, en incluant ou en supprimant des bords de l\'objet de base, ou en modifiant la discrétisation FHPath. Par conséquent, lors du changement de FHPath, vous n\'avez pas à vous soucier des connexions à d\'autres objets déjà effectuées à l\'aide des points de terminaison FHPath, par ex. si vous avez utilisé les points de terminaison comme point de départ pour les objets FHSegment, les objets FHPort, les objets FHEquiv ou les connexions à un objet FHPlane. En particulier, lorsque vous modifiez un FHPath provoquant la création de plusieurs segments, la liste d\'objets FHNode déjà existante sera simplement étendue et les anciennes positions FHNode seront réorganisées. Si, à la place, vous modifiez un FHPath entraînant la suppression de segments, la liste des objets FHNode sera raccourcie et les objets FHNode excédentaires supprimés du document, sauf si l\'un des FHNode a déjà été utilisé dans un autre objet (par exemple, si vous avez utilisé un nœud intermédiaire pour créer un FHSegment). Dans ce cas, le FHNode sera conservé, mais en dehors de l\'objet FHPath, et la connexion sera peut-être suspendue; il appartient à l\'utilisateur de garantir l\'exactitude des connexions.

-   Vous ne pouvez pas déplacer librement l\'objet FHPath ou ses FHNodes. Pour modifier la position du FHPath, déplacez l\'objet de base sous-jacent (l\'objet de base est masqué par défaut, vous pouvez l\'afficher à nouveau en sélectionnant l\'objet dans l\'arborescence et en appuyant sur **Espace**.

-   Les bords incurvés seront discrétisés en un ensemble de segments conformément à la propriété {{PropertyData/fr|Discr}} FHPath.

## Propriétés

-    {{PropertyData/fr|Base}}: objet de base sur lequel ce composant est construit.

-    {{PropertyData/fr|Nodes}}: (lecture seule) La liste de [FHNode](EM_FHNode/fr.md) le long du chemin. Pas pour la modification directe de l\'utilisateur.

-    {{PropertyData/fr|Width}}: largeur des segments FHPath (paramètre de segment \'w\' dans FastHenry).

-    {{PropertyData/fr|Height}}: hauteur des segments FHPath (paramètre de segment \'h\' dans FastHenry).

-    {{PropertyData/fr|Discr}}: nombre maximum de segments dans lesquels les bords courbes seront discrétisés.

-    {{PropertyData/fr|Sigma}}: conductivité des segments FHPath (paramètre de segment \'sigma\' dans FastHenry).

-    {{PropertyData/fr|ww}}: direction de la section le long de la largeur du premier segment du FHPath (paramètre de segment \'wx\', \'wy\', \'wz\' dans FastHenry).

-    {{PropertyData/fr|nhinc}}: nombre de filaments dans le sens de la hauteur (paramètre de segment \'nhinc\' dans FastHenry).

-    {{PropertyData/fr|nwinc}}: nombre de filaments dans le sens de la largeur (paramètre de segment \'nwinc\' dans FastHenry).

-    {{PropertyData/fr|rh}}: rapport des filaments adjacents dans la direction de la hauteur (paramètre de segment \'rh\' dans FastHenry).

-    {{PropertyData/fr|rw}}: rapport des filaments adjacents dans le sens de la largeur (paramètre de segment \'rw\' dans FastHenry).

## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil FHPath peut-être utilisé dans des [macros](macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante: 
```python
path = makeFHPath(baseobj=None,name='FHPath')
```

-   Crée un objet `FHPath`.

-    `baseobj`est l\'objet qui peut être utilisé comme base pour le FHPath. Si aucun `baseobj` n\'est donné, l\'utilisateur doit attribuer un objet de base ultérieurement, pour pouvoir utiliser cet objet. `baseobj` est obligatoire et peut être n\'importe quelle forme contenant des bords, même si l\'objet FHPath est conçu pour fonctionner au mieux avec le support d\'une esquisse ou d\'un fil.

-    `name`est le nom de l\'objet.

Example: 
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
[documentation index](../README.md) > EM FHPath/fr
