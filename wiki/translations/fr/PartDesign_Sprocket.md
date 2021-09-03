---
- GuiCommand:/fr
   Name:PartDesign Sprocket
   Name/fr:PartDesign Pignon
   MenuLocation:Conception de pièces → Sprocket...
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.19
---

## Description

Cet outil vous permet de créer un profil 2D d\'un pignon. Il peut être extrudé avec la fonction [PartDesign Protrusion](PartDesign_Pad/fr.md).

## Utilisation

1.  Aller au menu **Conception de pièces → <img src=images/PartDesign_Sprocket.svg style="width:24px"> Sprocket...**.
2.  Définissez {{PropertyData/fr|Number Of Teeth}} et {{PropertyData/fr|Sprocket Reference}}.
3.  Cliquez sur **OK**.
4.  Si la roue dentée est créée en dehors du corps actif, faites-la glisser et déposez-la dans un corps pour appliquer d\'autres fonctions comme l\'extrusion.

## Propriétés

-    {{PropertyData/fr|Number Of Teeth}}: Nombre de dents.

-    {{PropertyData/fr|Sprocket Reference}}: Le type de pignon. Une liste de définitions de pignons. {{Version/fr|0.20}}. La liste comprend les normes ANSI et ISO ainsi que certaines définitions de pignons pour bicyclettes et motos.

-    {{PropertyData/fr|Pitch}}: Distance entre deux dents.

-    {{PropertyData/fr|Roller Diameter}}: Diamètre des rouleaux de la chaîne pour lesquels le pignon est conçu.

-    {{PropertyData/fr|Thickness}}: Epaisseur principale du pignon. **Remarque :** Le pignon ne peut pas simplement être extrudé avec cette épaisseur car les dents ont des chanfreins latéraux. Il faut donc regarder la définition du pignon pour modéliser un pignon 3D valide. {{Version/fr|0.20}}





{{PartDesign Tools navi

}} 
