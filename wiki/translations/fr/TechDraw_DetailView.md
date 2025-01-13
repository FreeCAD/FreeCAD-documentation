---
 GuiCommand:
   Name: TechDraw DetailView
   Name/fr: TechDraw Vue détaillée
   MenuLocation: TechDraw , Vues de Techdraw , Insérer une vue détaillée
   Workbenches: TechDraw_Workbench/fr
   Version: 0.19
   SeeAlso: TechDraw_View/fr
---

# TechDraw DetailView/fr

## Description

L\'outil **TechDraw Vue détaillée** crée une vue d\'une petite zone d\'une vue existante.

![](images/ViewDetail.png ) 
*Vue détaillée avec un contour circulaire*



## Utilisation

1.  Sélectionnez une vue de base pour la vue détaillée.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/TechDraw_DetailView.svg" width=16px> [Insérer une vue détaillée](TechDraw_DetailView/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Vues de Techdraw → <img src="images/TechDraw_DetailView.svg" width=16px> Insérer une vue détaillée** dans le menu.
3.  Un contour de surbrillance est ajouté à la vue de base, une vue détaillée est ajoutée à la page et un panneau de tâches s\'ouvre.
4.  Pour plus de visibilé, il est préférable de déplacer la vue détaillée de manière à ce qu\'elle ne chevauche pas avec la vue de base : maintenez le bouton gauche de la souris enfoncé sur son cadre ou son étiquette et faites-la glisser vers une nouvelle position.
5.  Pour modifier la position du contour de surbrillance, procédez comme suit :
    -   Déplacez le contour en le faisant glisser :
        1.  Appuyez sur le bouton **Déplacez la sélection**.
        2.  Le contour est marqué sur la page et une étiquette temporaire \"glisser\" est ajoutée.
        3.  Maintenez le bouton gauche de la souris enfoncé sur le contour lui-même ou sur cette étiquette et faites glisser le contour vers une nouvelle position.
    -   Déplacez le contour par saisie de coordonnées :
        1.  Modifiez les coordonnées X et Y dans le panneau des tâches. Les coordonnées sont relatives au centre de la vue de base.
6.  Modifiez éventuellement le **Rayon** de la vue détaillée.
7.  Modifier éventuellement le **Type d\'échelle** et le **Facteur d\'échelle** de la vue détaillée. Voir [TechDraw Vue](TechDraw_View/fr#Propriétés.md) pour plus d\'informations.
8.  Spécifier une étiquette **Référence**. Cette étiquette sera affichée près du contour de la surbrillance.



## Remarques

-   Pour modifier une vue détaillée, double-cliquez dessus dans la vue en arborescence.
-   Les contours des vues détaillées peuvent être ronds ou carrés. Ceci est contrôlé par la **Forme du contour pour les vues détaillées** des [préférences](TechDraw_Preferences/fr#Annotation.md).
-   [Forum avec une bonne discussion sur la détermination du point d\'ancrage](https://www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Dans les propriétés de **Base View**, vous pouvez modifier l\'apparence du contour détaillé.

Une vue détaillée, en fait un objet {{Incode|TechDraw::DrawViewDetail}}, est dérivée d\'une [vue de Part](TechDraw_View/fr#Propriétés_Vue_de_Part.md), objet {{Incode|TechDraw::DrawViewPart}}, et hérite de toutes ses propriétés. Elle possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Appearance}}

-    **Show Matting|Bool**: affiche ou cache le fond autour de la vue détaillée. {{Version/fr|1.0}}

-    **Show Highlight|Bool**: affiche ou masque la mise en évidence des détails dans la vue source. {{Version/fr|1.0}}


{{TitleProperty|Detail}}

-    **Base View|Link**: la vue sur laquelle la vue détaillée est basée.

-    **Anchor Point|Vector**: centre de la vue détaillée dans la **Base View**.

-    **Radius|Float**: taille de la zone de la **Base View** affichée dans la vue détaillée.

-    **Reference|String**: un identifiant pour la vue détaillée dans la **Base View**.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DetailView/fr
