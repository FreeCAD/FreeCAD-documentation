---
- GuiCommand   */fr
   Name   *FEM MeshNetgenFromShape
   Name/fr   *FEM Maillage FEM à partir d'une forme de Netgen
   MenuLocation   *Maillage → Maillage FEM à partir d'une forme de Netgen
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM MeshNetgenFromShape/fr

## Description

Pour une analyse par éléments finis, la géométrie doit être discrétisée en [FEM Maillage](FEM_Mesh/fr.md). Cette commande utilise Netgen (qui doit être installé sur le système) pour calculer le maillage.

En fonction de votre système d\'exploitation et de votre paquetage d\'installation, Netgen peut être fourni avec FreeCAD ou pas. Pour plus d\'informations voir [FEM Installation des composants requis](FEM_Install/fr.md).

## Utilisation

1.  Sélectionnez la forme que vous voulez analyser. Pour un volume, il doit s\'agir d\'un solide ou d\'un compsolide (composé de solides). Un compsolid est nécessaire si votre pièce est faite de plusieurs matériaux. (Un compsolid peut être créé avec la commande [Part Fragments booléens](Part_BooleanFragments/fr.md)).
    -   Appuyez sur le bouton **<img src="images/FEM_MeshNetgenFromShape.svg" width=16px> [Maillage FEM à partir d'une forme de Netgen](FEM_MeshNetgenFromShape/fr.md)**, ou bien
    -   Sélectionnez le bouton **Maillage → <img src="images/FEM_MeshGmshFromShape.svg" width=16px> Maillage FEM à partir d'une forme de Netgen** dans le menu.
2.  Modifiez éventuellement les paramètres.
3.  Cliquez sur le bouton **Appliquer** pour réaliser un maillage, ou sur le bouton **OK** pour réaliser un maillage et fermer le dialogue.

## Propriétés

-    **Max. Size**   * taille maximale de l\'élément en mm.

-    **Second order**   * les éléments de second ordre contiennent plus de noeuds par élément. En général, il suffit d\'utiliser un maillage plus grossier pour obtenir la même précision de solution qu\'avec les éléments de premier ordre,

    -   true (valueur par défaut) ; éléments de second ordre,
    -   false ; éléments de premier ordre.

-    **Fineness**   * définit la finesse du maillage.

-    **Growth Rate**   * définit de combien les éléments adjacents peuvent différer en taille.

-    **Nb. Segs per Edge**   * définit le nombre minimum de segments de maille par arête.

-    **Nb. Segs per Radius**   * définit le nombre minimum de segments de maillage par rayon.

-    **Optimize**   *

    -   true (valeur par défaut); applique un algorithme d\'optimisation pour améliorer la qualité du maillage,
    -   false;





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshNetgenFromShape/fr
