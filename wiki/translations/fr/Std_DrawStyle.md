---
- GuiCommand:/fr
   Name:Std DrawStyle
   Name/fr:Std Style de représentation
   MenuLocation:Affichage → Style de représentation → ...
   Workbenches:Tous
   Shortcut:**V** **1** - **V** **7**
   SeeAlso:[Std Boîte de délimitation](Std_SelBoundingBox/fr.md)
---

## Description

La commande **Std DrawStyle** peut remplacer l\'effet de la [propriété](Property_editor/fr.md) du {{PropertyView/fr|Mode d'affichage}} des objets dans une [vue 3D](3D_view/fr.md).

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Cliquez sur la flèche noire vers le bas à droite du bouton **<img src="images/Std_DrawStyleAsIs.svg" width=16px> [Style de représentation](Std_DrawStyle.md)** et sélectionnez un style dans le menu déroulant.
    -   Dans le menu, accédez à **Affichage → Style de représentation** et sélectionnez un style.
    -   Dans le menu contextuel [3D view](3D_view/fr.md), accédez à {{MenuCommand/fr|Style de représentation}} et sélectionnez un style.
    -   Utilisez l\'un des raccourcis clavier: **V** then **1**, **2**, **3**, **4**, **5**, **6** or **7**.

## Styles de représentation disponibles 

### <img alt="" src=images/Std_DrawStyleAsIs.svg  style="width:32px;"> Tel quel 

Le style **Tel quel** ne remplace pas le {{PropertyView/fr|Display Mode}} des objets.

![](images/Std_DrawStyleAsIs_example.png ) *4 objets identiques chacun avec un mode d'affichage différent (de gauche à droite: «Points», «Filaire», «Ombré» et «Lignes plates») avec le style de dessin «Tel quel» appliqué*

### <img alt="" src=images/Std_DrawStylePoints.svg  style="width:32px;"> Points 

Le style **Points** remplace le {{PropertyView/fr|Display Mode}} des objets. Ce style correspond au mode d\'affichage «Points». Les sommets sont affichés en couleurs unies. Les arêtes et les faces ne sont pas affichées.

![](images/Std_DrawStylePoints_example.png ) *Les mêmes objets avec le style de dessin «Points» appliqué*

### <img alt="" src=images/Std_DrawStyleWireFrame.svg  style="width:32px;"> Filaire 

Le style **Filaire** remplace la {{PropertyView/fr|Display Mode}} des objets. Ce style correspond au mode d\'affichage «Filaire». Les sommets et les bords sont affichés en couleurs unies. Les faces ne sont pas affichés.

![](images/Std_DrawStyleWireframe_example.png ) *Les mêmes objets avec le style de dessin «Filaire» appliqué*

### <img alt="" src=images/Std_DrawStyleHiddenLine.svg  style="width:32px;"> Ligne cachée 

Le style **Ligne cachée** remplace la {{PropertyView/fr|Display Mode}} des objets. Les objets sont affichés comme s\'ils étaient convertis en maillages triangulaires.

![](images/Std_DrawStyleHiddenLine_example.png ) *Les mêmes objets avec le style de dessin «Ligne cachée» appliqué*

### <img alt="" src=images/Std_DrawStyleNoShading.svg  style="width:32px;"> Pas d\'ombre 

Le style **Pas d\'ombre** remplace la {{PropertyView/fr|Display Mode}} des objets. Les sommets, les bords et les faces sont affichés en couleurs unies.

![](images/Std_DrawStyleNoShading_example.png ) *Les mêmes objets avec le style de dessin «Sans ombre» appliqué*

### <img alt="" src=images/Std_DrawStyleShaded.svg  style="width:32px;"> Ombré 

Le style **Ombré** remplace le {{PropertyView/fr|Display Mode}} des objets. Ce style correspond au mode d\'affichage «ombré». Les sommets et les bords ne sont pas affichés. Les faces sont éclairés en fonction de leur orientation.

![](images/Std_DrawStyleShaded_example.png ) *Les mêmes objets avec le style de dessin «Ombré» appliqué*

### <img alt="" src=images/Std_DrawStyleFlatLines.svg  style="width:32px;"> Lignes plates 

Le style **Lignes plates** remplace le {{PropertyView/fr|Display Mode}} des objets. Ce style correspond au mode d\'affichage «Lignes plates». Les sommets et les bords sont affichés en couleurs unies. Les faces sont éclairés en fonction de leur orientation.

![](images/Std_DrawStyleFlatLines_example.png ) *Les mêmes objets avec le style de dessin «Lignes plates» appliqué*

## Remarques

-   Les objets dans une [vue 3D](3D_view/fr.md) ont également une propriété {{PropertyView/fr|Draw Style}}. Cette propriété contrôle le type de ligne utilisé pour les bords. La commande Std DrawStyle ne remplace pas cette propriété.
-   Pour une macro pour basculer entre deux styles de dessin, voir: [Macro Toggle Drawstyle](Macro_Toggle_Drawstyle/fr.md).





{{Std Base navi

}}  
