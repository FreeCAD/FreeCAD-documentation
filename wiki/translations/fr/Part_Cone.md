---
- GuiCommand:/fr
   Name:Part Cone
   Name/fr:Part Cône
   MenuLocation:Pièce → Primitives → Cône
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Primitives](Part_Primitives/fr.md)
---

# Part Cone/fr

## Description

Un cône paramétrique tronqué est une primitive disponible sur la barre d\'outils Part, ou dans le menu (primitives sub-menu) une boite de dialogue primitives géométriques est ouverte.

<img alt="" src=images/Otherwisedefault270degree_Part_Cone.png  style="width:300px;"> 
*Cône dont le paramètre "Angle" est réglé sur 270 degrés et tous les autres paramètres sont réglés sur leurs valeurs par défaut.*

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Atelier Part](Part_Workbench/fr.md)
2.  Lancez la commande de deux manières:
    -   Appuyez sur le bouton **<img src="images/Part_Cone.svg" width=16px> Créer un solide conique** dans la barre d\'outils.
    -   Sélectionnez **Pièce → Primitives → <img src="images/Part_Cone.svg" width=16px> Cône** dans la barre de menus.

**Résultat:** les valeurs par défaut créent un cône paramétrique tronqué qui est positionné à l\'origine (point 0,0,0) et attaché au plan xy global. Sa hauteur de 10 mm se situe le long de l\'axe z global. Le rayon inférieur {{PropertyData/fr|Radius 1}} est de 2 mm, le rayon supérieur {{PropertyData/fr|Radius 2}} est de 4 mm.

Les propriétés du cône peuvent être éditées ultérieurement, soit dans l\'[Éditeur de propriétés](Property_editor/fr.md), soit en double-cliquant sur le prisme dans la [Vue par arborescence](Tree_view/fr.md).

## Propriétés

-    {{PropertyData/fr|Radius 1}}: Rayon de l\'arc ou du cercle définissant la face inférieure.

-    {{PropertyData/fr|Radius 2}}: Rayon de l\'arc ou du cercle définissant la face supérieure.

-    {{PropertyData/fr|Height}}: Hauteur du cône de la pièce

-    {{PropertyData/fr|Angle}}: Nombre de degrés de l\'arc ou des cercles définissant les faces supérieure et inférieure du cône tronqué. La valeur par défaut de 360° crée des faces circulaires, une valeur inférieure créera une partie de cône définie par des faces supérieure et inférieure dont les bords sont définis par un arc du nombre de degrés et deux rayons.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cone/fr
