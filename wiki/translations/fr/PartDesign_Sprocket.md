---
 GuiCommand:
   Name: PartDesign Sprocket
   Name/fr: PartDesign Pignon
   MenuLocation: Part Design , Pignon...
   Workbenches: PartDesign_Workbench/fr
   Version: 0.19
---

# PartDesign Sprocket/fr

## Description

Cet outil vous permet de créer un profil 2D d\'un pignon (ou roue à chaîne). Il peut être extrudé avec la fonction [PartDesign Protrusion](PartDesign_Pad/fr.md).



## Utilisation

1.  En règle générale, activer le bon corps.
2.  Allez dans le menu **Part Design → [<img src=images/PartDesign_Sprocket.svg style="width:16px"> Pignon...**.
3.  Définissez **Number Of Teeth** et **Sprocket Reference**.
4.  Cliquez sur **OK**.
5.  S\'il n\'y avait pas de corps actif : glisser et déposer le pignon dans un corps pour appliquer d\'autres fonctions comme l\'extrusion.



## Propriétés

-    **Number Of Teeth**: nombre de dents.

-    **Sprocket Reference**: type de pignon. Une liste de définitions de pignons. {{Version/fr|0.20}}. La liste comprend les normes ANSI et ISO ainsi que certaines définitions de pignons pour bicyclettes et motos.

-    **Pitch**: distance entre deux dents.

-    **Roller Diameter**: diamètre des roulements pour lesquels le pignon est conçu.

-    **Thickness**: épaisseur principale du pignon. **Remarque :** le pignon ne peut pas simplement être extrudé avec cette épaisseur car les dents ont des chanfreins latéraux. Il faut donc regarder la définition du pignon pour modéliser un pignon 3D valide. {{Version/fr|0.20}}





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Sprocket/fr
