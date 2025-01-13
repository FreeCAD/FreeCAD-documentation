---
 GuiCommand:
   Name: TechDraw ClipGroup
   Name/fr: TechDraw Fenêtre de rognage
   MenuLocation: TechDraw , Vues de TechDraw , Insérer une fenêtre de rognage
   Workbenches: TechDraw_Workbench/fr
   SeeAlso: 
---

# TechDraw ClipGroup/fr

## Description

Cet outil **TechDraw Fenêtre de rognage** crée une fenêtre de rognage qui peut contenir des vues.

![](images/TechDraw_Clipview.png ) 
*Fenêtre de rognage de différentes vues existantes*



## Utilisation

1.  S\'il y a plusieurs pages de dessin dans le document : activez la page souhaitée en la sélectionnant dans la [vue en arborescence](Tree_view/fr.md).
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/TechDraw_ClipGroup.svg" width=16px> [Insérer une fenêtre de rognage](TechDraw_ClipGroup/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Vues de TechDraw → <img src="images/TechDraw_ClipGroup.svg" width=16px> Insérer une fenêtre de rognage** du menu.
3.  Si le document comporte plusieurs pages de dessin et que vous n\'avez pas encore activé de page, la fenêtre de dialogue **Sélecteur de pages** s\'ouvre :
    1.  Sélectionnez la page désirée.
    2.  Appuyez sur le bouton **OK**.
4.  Les vues peuvent être glissées et déposées vers et depuis le groupe de rognage (Clip) dans l\'arborescence. {{Version/fr|1.0}}



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Une fenêtre de rognage, en fait un objet {{Incode|TechDraw::DrawViewClip}}, possède les [propriétés](TechDraw_View/fr#Propriétés_Vue_de_Part.md) communes à tous les types de vues. Elle possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Clip Group}}

-    **Width|Length**: largeur de la fenêtre de rognage en unités

-    **Height|Length**: hauteur de la fenêtre de rognage en unités

-    **ShowFrame**: si vrai, affiche un cadre autour de la fenêtre de rognage

-    **ShowLabels|Bool**: si vrai, affiche un cadre autour de la fenêtre de rognage

-    **Views|LinkList**: les vues contenues dans la fenêtre de rognage





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ClipGroup/fr
