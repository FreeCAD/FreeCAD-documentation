---
 GuiCommand:
   Name: Std DrawStyle
   Name/fr: Std Style de représentation
   MenuLocation: Affichage , Style de représentation , ...
   Workbenches: Tous
   Shortcut: **V** **1** - **V** **7**
   SeeAlso: Std_SelBoundingBox/fr
---

# Std DrawStyle/fr

## Description

La commande **Std Style de représentation** peut remplacer l\'effet de la [propriété](Property_editor/fr.md) **Display Mode** des objets dans une [vue 3D](3D_view/fr.md).



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Cliquez sur la flèche noire vers le bas à droite du bouton **<img src="images/Std_DrawStyleAsIs.svg" width=16px> [Style de représentation](Std_DrawStyle/fr.md)** et sélectionnez un style dans le menu déroulant.
    -   Dans le menu, allez à **Affichage → Style de représentation** et sélectionnez un style.
    -   Dans le menu contextuel de la [vue 3D](3D_view/fr.md), accédez à **Style de représentation** et sélectionnez un style.
    -   Utilisez l\'un des raccourcis clavier : **V** puis **1**, **2**, **3**, **4**, **5**, **6** or **7**.



## Styles des représentations disponibles 



### <img alt="" src=images/Std_DrawStyleAsIs.svg  style="width:24px;"> Par défaut 

Le style **Par défaut** ne supplante pas **Display Mode** des objets.

![](images/Std_DrawStyleAsIs_example.png ) 
*4 objets identiques chacun avec un mode d'affichage différent (de gauche à droite: "Points", "Filaire", "Ombré" et "Filaire ombré") avec le style de représentation '''Par défaut'''*

### <img alt="" src=images/Std_DrawStylePoints.svg  style="width:24px;"> Points 

Le style **Points** remplace **Display Mode** des objets. Ce style correspond au mode d\'affichage \"Points\". Les sommets sont affichés en couleurs unies. Les arêtes et les faces ne sont pas affichées.

![](images/Std_DrawStylePoints_example.png ) 
*Les mêmes objets avec le style "Points" appliqué*



### <img alt="" src=images/Std_DrawStyleWireFrame.svg  style="width:24px;"> Filaire 

Le style **Filaire** remplace **Display Mode** des objets. Ce style correspond au mode d\'affichage \"Filaire\". Les sommets et les bords sont affichés en couleurs unies. Les faces ne sont pas affichés.

![](images/Std_DrawStyleWireframe_example.png ) 
*Les mêmes objets avec le style "Filaire" appliqué*



### <img alt="" src=images/Std_DrawStyleHiddenLine.svg  style="width:24px;"> Ligne cachée 

Le style **Ligne cachée** remplace **Display Mode** des objets. Les objets sont affichés comme s\'ils étaient convertis en maillages triangulaires.

![](images/Std_DrawStyleHiddenLine_example.png ) 
*Les mêmes objets avec le style "Ligne cachée" appliqué*



### <img alt="" src=images/Std_DrawStyleNoShading.svg  style="width:24px;"> Pas d\'ombrage 

Le style **Pas d\'ombrage** remplace **Display Mode** des objets. Les sommets, les bords et les faces sont affichés en couleurs unies.

![](images/Std_DrawStyleNoShading_example.png ) 
*Les mêmes objets avec le style "Pas d'ombrage" appliqué*



### <img alt="" src=images/Std_DrawStyleShaded.svg  style="width:24px;"> Ombré 

Le style **Ombré** remplace **Display Mode** des objets. Ce style correspond au mode d\'affichage \"Ombré\". Les sommets et les bords ne sont pas affichés. Les faces sont éclairés en fonction de leur orientation.

![](images/Std_DrawStyleShaded_example.png ) 
*Les mêmes objets avec le style "Ombré" appliqué*



### <img alt="" src=images/Std_DrawStyleFlatLines.svg  style="width:24px;"> Filaire ombré 

Le style **Filaire ombré** remplace **Display Mode** des objets. Ce style correspond au mode d\'affichage \"Filaire ombré\". Les sommets et les bords sont affichés en couleurs unies. Les faces sont éclairés en fonction de leur orientation.

![](images/Std_DrawStyleFlatLines_example.png ) 
*Les mêmes objets avec le style "Filaire ombré" appliqué*



## Remarques

-   Les objets dans une [vue 3D](3D_view/fr.md) ont également une propriété **Draw Style**. Cette propriété contrôle le type de ligne utilisé pour les bords. La commande Std Style de représentation ne remplace pas cette propriété.
-   Pour une macro, pour basculer entre deux styles de dessin, voir : [Macro Toggle Drawstyle](Macro_Toggle_Drawstyle/fr.md).



---
⏵ [documentation index](../README.md) > Std DrawStyle/fr
