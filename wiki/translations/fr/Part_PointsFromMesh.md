---
- GuiCommand:
   Name:Part PointsFromMesh‎
   Name/fr:Part Points à partir de maillage
   MenuLocation:Part - Créer un objet points à partir d'une géométrie
   Workbenches:[Part](Part_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Part Forme à partir du maillage](Part_ShapeFromMesh/fr.md), [Part Convertir en solide](Part_MakeSolid/fr.md), [Part Affiner la forme](Part_RefineShape/fr.md)
---

# Part PointsFromMesh/fr

## Description

L\'outil <img alt="" src=images/Part_PointsFromMesh.svg  style="width:24px;"> [Part Points à partir de maillage](Part_PointsFromMesh/fr.md) crée un objet points à partir d\'un objet géométrique. Pour les {{VersionMinus/fr|0.20}}, l\'objet de base doit être un objet Mesh, dans les versions ultérieures, n\'importe quel objet géométrique peut être sélectionné.

La forme résultante est un composé de sommets qui peut être utilisé comme référence pour créer des polylignes, des esquisses et des faces avec d\'autres outils, comme ceux des ateliers <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench/fr.md) ou <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft](Draft_Workbench/fr.md).



## Utilisation

1.  Sélectionner un objet.
2.  Sélectionner l\'option **Part → <img src="images/Part_PointsFromMesh.svg" width=16px> Créer un objet points à partir d'une géométrie** du menu.
3.  La boîte de dialogue **Distance dans l'espace des paramètres** s\'ouvre.
4.  Entrer une valeur pour la distance.
5.  Appuyer sur le bouton **OK**.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part PointsFromMesh/fr
