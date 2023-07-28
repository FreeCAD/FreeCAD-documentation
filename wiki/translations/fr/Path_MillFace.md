---
- GuiCommand:/fr
   Name:Path Face
   Name/fr:Path Surfaçage
   MenuLocation:Path → Surfaçage
   Workbenches:[Path](Path_Workbench/fr.md)
---

# Path MillFace/fr

## Description

L\'outil <img alt="" src=images/Path_MillFace.svg  style="width:24px;"> [Surfaçage](Path_MillFace/fr.md) crée une trajectoire pour effectuer une opération de surfaçage sur une surface horizontale. Cette opération est généralement utilisée :

-   pour lisser la surface d\'un brut,
-   pour fraiser une ou plusieurs faces sélectionnées à la profondeur souhaitée en vue d\'effectuer des opérations de dégagement ultérieures dans les limites des régions concernées par cette opération,
-   ou pour appliquer une surface de finition sur la ou les faces sélectionnées.

Cette opération contient une propriété **BoundaryShape** qui permet de modifier la zone de sélection en fonction de la ou des faces sélectionnées.

<img alt="Exemple de l\'opération Surfaçage utilisée pour préparer la surface du brut pour une opération de dégagement ultérieure." src=images/MillFace_Sample.png  style="width:600px;">



## Utilisation

1.  Sélectionnez une ou plusieurs faces à surfacer. **Remarque :** si les faces sélectionnées ont des hauteurs différentes, elles seront toutes fraisées à la profondeur finale.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Path_MillFace.svg" width=16px> [Surfaçage](Path_MillFace/fr.md)**.
    -   Sélectionnez l\'option **Path → <img src="images/Path_MillFace.svg" width=16px> Surfaçage** dans le menu.
3.  Sélectionnez le bon paramètre **BoundaryShape** pour modifier la zone de fraisage en fonction de la ou des faces sélectionnées comme **Géométrie de base**.
4.  Ajustez les autres propriétés selon vos besoins. Elles sont énumérées ci-dessous.



## Avertissements

-   L\'utilisation de cette fonction sur un plan incliné peut produire des résultats inattendus : elle génèrera toujours un parcours pour couper une surface horizontale. L\'étendue de la coupe sera la projection verticale du plan incliné, effectuée à une hauteur correspondante au point le plus bas de ce plan.

-   Étant donné que les outils de parcours fonctionnent uniquement sur la géométrie des arêtes/faces sélectionnées et ne se rapportent pas au reste du modèle 3D, les parcours ne dépasseront pas les limites du plan choisi, même s\'il est entouré de brut inutilisé ou d\'air. Cela laissera des coins non usinés. Ceux-ci peuvent parfois être supprimés avec l\'un des outils de rectification disponibles dans le menu *Path*.



## Surfaçage de face verticale 

-   Cet outil ne fonctionnera pas sur un **plan vertical** ou une surface verticale non plane. Les opérations verticales peuvent être réalisées en utilisant l\'outil [contour des faces](Path_Profile/fr.md) ou l\'outil [contour des bords](Path_Profile/fr.md). Ceux-ci nécessiteront la sélection d\'une face ou d\'une boucle fermée d\'arêtes *incluant le bord supérieur ou inférieur de la surface verticale souhaitée*. L\'extension du parcours peut alors être réduite à l\'aide de l\'outil [Limitation de zones](Path_DressupPathBoundary/fr.md) qui se trouve dans le menu *Path*. Avec l\'outil de finition, sélectionnez l\'option *Créer une boîte* et réduisez la taille pour limiter la portée du parcours du contour. Ces réglages ne permettent toutefois pas de déplacer l\'origine de la zone de contour. Cela doit être fait en ajustant les paramètres de placement dans la [vue en arborescence](Tree_view/fr.md).
-   Cela fonctionnera sur des surfaces composées telles que plusieurs plans verticaux ou surfaces cylindriques assemblées reliées entre elles, à condition qu\'elles forment une surface continue.

## Options

Vide



## Propriétés

***Remarque***: les noms de certaines propriétés de cette liste diffèrent un peu des mêmes paramètres que ceux utilisés dans l\'éditeur de fenêtre de tâche.



### Données


{{TitleProperty|Base}}

Remarque : il est conseillé de ne pas modifier la propriété Placement des opérations de parcours. Il convient plutôt de déplacer ou de faire pivoter le modèle Path Tâche selon les besoins.

-    **Placement**: placement global \[position et rotation\] de l\'objet - par rapport à l\'origine (ou l\'origine du conteneur de l\'objet parent)

    -   
        **Angle**
        
        : angle en degrés appliqué à la rotation de l\'objet autour de la valeur de la propriété Axis

    -   
        **Axis**
        
        : axe (un ou plusieurs) autour duquel l\'objet doit tourner, défini dans les sous-propriétés : X, Y, Z.

        -   
            **X**
            
            : valeur de l\'axe X

        -   
            **Y**
            
            : valeur de l\'axe Y

        -   
            **Z**
            
            : valeur de l\'axe Z

    -   
        **Position**
        
        : Position de l\'objet, définie dans les sous-propriétés : X, Y, Z - par rapport à l\'origine (ou l\'origine du conteneur de l\'objet parent)

        -   
            **X**
            
            : valeur de la distance en X

        -   
            **Y**
            
            : valeur de la distance en Y

        -   
            **Z**
            
            : valeur de la distance en Z

-    **Label**: nom de l\'objet fourni par l\'utilisateur (UTF-8)


{{TitleProperty|Depth}}

-    **Clearance Height**: hauteur nécessaire pour contourner les brides et les obstructions.

-    **Final Depth**: profondeur finale de l\'outil - valeur la plus basse de Z.

-    **Finish Depth**: maximum de matériau retiré lors du passage final.

-    **Safe Height**: seuil supérieur duquel les mouvements rapides sont autorisés.

-    **Start Depth**: profondeur initiale de l\'outil - première profondeur de coupe en Z.

-    **Step Down**: abaissement incrémentiel de l\'outil.


{{TitleProperty|Face}}

-    **BoundaryShape**: forme à utiliser pour le calcul de la limite

-    **ClearEdges**: finir les bords de la surface (applicable uniquement à la boîte englobante)

-    **ExcludeRaisedAreas**: exclure le fraisage des zones en relief à l\'intérieur de la face.

-    **Offset Pattern**: motif à utiliser. (sélectionnez de quelle manière les mouvements horizontaux doivent être effectués).


{{TitleProperty|Path}}

-    **Active**: mettre à False pour empêcher l\'opération de générer du code.

-    **Base**: géométrie de base pour cette opération.

-    **Comment**: commentaire facultatif pour cette opération.

-    **Coolant Mode**: mode de refroidissement pour cette opération.

-    **Cycle Time**: estimation du temps de cycle pour cette opération.

-    **Tool Controller**: définit le contrôleur d\'outil utilisé dans l\'opération.

-    **User Label**: étiquette attribuée par l\'utilisateur.


{{TitleProperty|Pocket}}

-    **Cut Mode**: direction dans laquelle le parcours doit contourner la pièce : sens horaire (ClockWise = CW) ou sens anti-horaire (CounterClockWise = CCW).

-    **Extra Offset**: décalage supplémentaire à appliquer à l\'opération. La direction dépend de l\'opération.

-    **StartAt**: commence la poche au centre ou à la limite

-    **Step Over**: pourcentage du diamètre de l\'outil à utiliser à chaque passage.

-    **Zig Zag Angle**: angle du motif en zigzag

-    **Offset Pattern**: motif de détourage à utiliser

-    **Min Travel**: utiliser le triage 3D du parcours

-    **Keep Tool Down**: tenter d\'éviter les rétractions inutiles.


{{TitleProperty|Rotation}}

-    **Attempt Inverse Angle**: tenter automatiquement l\'angle inverse si la rotation initiale est incorrecte.

-    **Enable Rotation**: active la rotation pour accéder aux poches ou aux zones non normales à l\'axe Z.

-    **Inverse Angle**: inverse l\'angle de la rotation. ***Exemple :** changer une rotation de -22,5 à 22,5 degrés.*

-    **Limit Depth To Face**: impose la profondeur Z de la face sélectionnée comme valeur minimale de la profondeur finale. Des valeurs utilisateur plus élevées pour la profondeur finale seront observées.

-    **Reverse Direction**: inverse l\'orientation de l\'opération de 180 degrés.


{{TitleProperty|Start Point}}

-    **Start Point**: point de départ personnalisé pour le parcours de cette opération.

    -   
        **X**
        
        : valeur de distance X.

    -   
        **Y**
        
        : valeur de distance Y.

    -   
        **Z**
        
        : valeur de distance Z.

-    **Use Start Point**: mis à True, si vous spécifiez manuellement un point de départ. Définissez le point de départ dans le champ Start Point des propriétés de données.



### Vue

Vide



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Exemple :


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path MillFace/fr
