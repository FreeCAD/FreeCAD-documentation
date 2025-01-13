---
 GuiCommand:
   Name: TechDraw FaceCenterLine
   Name/fr: TechDraw Ligne centrale à une face
   MenuLocation: TechDraw , Ajouter des lignes , Ajouter une ligne centrale à des faces
   Workbenches: TechDraw_Workbench/fr
   Version: 0.19
   SeeAlso: TechDraw_CosmeticVertex/fr, TechDraw_2LineCenterLine/fr, TechDraw_2PointCenterLine/fr, TechDraw_CosmeticEraser/fr
---

# TechDraw FaceCenterLine/fr

## Description

L\'outil **TechDraw Ligne centrale à une face** ajoute une ligne médiane à une ou plusieurs faces.

<img alt="" src=images/TechDraw_FaceCenterLine_Sample.png  style="width:400px;"> 
*Ligne centrale ajoutée a une face*



## Utilisation

1.  Sélectionnez une ou plusieurs faces dans une vue.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/TechDraw_FaceCenterLine.svg" width=16px> [Ajouter une ligne centrale à des faces](TechDraw_FaceCenterLine/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Ajouter des lignes → <img src="images/TechDraw_FaceCenterLine.svg" width=16px> Ajouter une ligne centrale à des faces** du menu.
3.  Un panneau de tâches s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
4.  Appuyez sur le bouton **OK** pour confirmer.
5.  Une ligne centrale est ajoutée au milieu de la boîte de délimitation de la ou des face(s) sélectionnée(s).



## Édition

N\'importe quel outil de ligne centrale (<img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:16px;"> TechDraw Ligne centrale à une face, <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:16px;"> [TechDraw Ligne centrale entre 2 lignes](TechDraw_2LineCenterLine/fr.md) et <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:16px;"> [TechDraw Ligne centrale entre 2 points](TechDraw_2PointCenterLine/fr.md)) peuvent être utilisés pour éditer n\'importe quelle ligne centrale.

1.  Sélectionnez une ligne centrale.
2.  Lancez un outil de ligne centrale.
3.  Un panneau de tâches s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
4.  Appuyez sur le bouton **OK** pour confirmer.

## Options

-   **Orientation** :
    -   **Vertical** : force la ligne centrale à être verticale. Ignoré pour Ligne centrale entre 2 points.
    -   **Horizontal** : force la ligne centrale à être horizontale. Ignoré pour Ligne centrale entre 2 points.
    -   **Aligné** : non disponible pour Ligne centrale à une face. Force la ligne centrale à suivre la direction générale des arêtes sélectionnées pour Ligne centrale entre 2 lignes. Ignoré pour Ligne centrale entre 2 points.
-   **Décalage horizontal** : déplace la ligne centrale à gauche ou à droite de sa position normale.
-   **Décalage vertical** : déplace la ligne centrale vers le haut ou vers le bas par rapport à sa position normale.
-   **Pivoter** : fait pivoter la ligne centrale autour de son point central (en degrés. + dans le sens inverse des aiguilles d\'une montre, - dans le sens des aiguilles d\'une montre).
-   **Étendre de** : allonge la ligne centrale de cette valeur.
-   **Couleur** : couleur de la ligne centrale.
-   **Épaisseur** : largeur de la ligne centrale.
-   **Style** : style de la ligne centrale. Les options sont :
    -   <img alt="" src=images/Continuous-line.svg  style="width:20px;"> 
**Continu**
    -   <img alt="" src=images/Dash-line.svg  style="width:20px;"> 
**Tiret**
    -   <img alt="" src=images/Dot-line.svg  style="width:20px;"> 
**Point**
    -   <img alt="" src=images/DashDot-line.svg  style="width:20px;"> 
**Tiret Point**
    -   <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> 
**Tiret Point Point**



## Remarques

-   Pour supprimer une ligne centrale, sélectionnez-la et appuyez sur **Supprimer**. {{Version/fr|1.0}}
-   Une ligne centrale à une face remplacera éventuellement deux propriétés d\'affichage :
    -   
        **HorizCenterLine**
        
        : affiche un trait d\'axe horizontal dans la vue.

    -   
        **VertCenterLine**
        
        : affiche un trait d\'axe vertical dans la vue.



## Propriétés

Les lignes centrales n\'ont pas de propriétés propres car elles ne sont pas des objets du document.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw FaceCenterLine/fr
