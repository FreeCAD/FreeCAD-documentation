---
- GuiCommand:/fr
   Name:Path Face
   Name/fr:Path Surfaçage
   MenuLocation:Path → Face
   Workbenches:[Path](Path_Workbench/fr.md)
---

# Path MillFace/fr

## Description

L\'outil <img alt="" src=images/Path_MillFace.svg  style="width:24px;"> [Surfaçage](Path_MillFace/fr.md) crée une trajectoire pour effectuer une opération de surfaçage sur une surface horizontale. Cette opération est généralement utilisée :

-   pour lisser la surface d\'un brut,
-   pour fraiser une ou plusieurs faces sélectionnées à la profondeur souhaitée en vue d\'effectuer des opérations de dégagement ultérieures dans les limites des régions concernées par cette opération,
-   ou pour appliquer une surface de finition sur la ou les faces sélectionnées.

Cette opération contient une propriété **BoundaryShape** qui permet de modifier la zone de sélection en fonction de la ou des faces sélectionnées.

<img alt="Exemple de l\'opération Surfaçage utilisée pour préparer la surface du stock pour une opération de dégagement ultérieure." src=images/MillFace_Sample.png  style="width:600px;">

## Utilisation

1.  Sélectionnez une ou plusieurs faces à surfacer. **Remarque:** Si les faces sélectionnées ont des hauteurs différentes, elles seront toutes fraisées à la profondeur finale.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Path_MillFace.svg" width=16px> [Face](Path_MillFace/fr.md)**.
    -   Sélectionnez l\'option **Path → <img src="images/Path_MillFace.svg" width=16px> Face** dans le menu.
3.  Sélectionnez le bon paramètre **BoundaryShape** pour modifier la zone de fraisage en fonction de la ou des faces sélectionnées comme **Base Geometry**.
4.  Ajustez les autres propriétés selon vos besoins. Elles sont énumérées ci-dessous.

## Avertissements

-   L\'utilisation de cette fonction sur un plan incliné peut produire des résultats inattendus: elle génèrera toujours un chemin pour couper une surface horizontale. L\'étendue de la coupe sera la projection verticale du plan incliné, effectuée à une hauteur correspondante au point le plus bas de ce plan.

-   Étant donné que les outils de tracé fonctionnent uniquement sur la géométrie des arêtes/faces sélectionnées et ne se rapportent pas au reste du modèle 3D, les tracés ne dépasseront pas les limites du plan choisi, même s\'il est entouré de brut inutilisé ou d\'air. Cela laissera des coins non usinés. Ceux-ci peuvent parfois être supprimés avec l\'un des outils de rectification disponibles dans le menu *Path*.

## Surfaçage de face verticale 

-   Cet outil ne fonctionnera pas sur un **plan vertical** ou une surface verticale non plane. Les opérations verticales peuvent être réalisées en utilisant l\'outil de profil de face ou l\'outil de profil de bord. Ceux-ci nécessiteront la sélection d\'une face ou d\'une boucle fermée d\'arêtes *incluant le bord supérieur ou inférieur de la surface verticale souhaitée*. L\'étendue de la trajectoire peut alors être réduite à l\'aide de l\'outil *Boundary Dress-up* qui se trouve dans le menu *Path*. Avec l\'outil Dress-up, sélectionnez l\'option *Create Box* et réduisez la taille pour limiter la portée de la trajectoire du profil. Ces réglages ne permettent toutefois pas de déplacer l\'origine de la zone de contour. Cela doit être fait en ajustant les paramètres de placement dans la [vue en arborescence](Tree_view/fr.md).
-   Cela fonctionnera sur des surfaces composées telles que plusieurs plans verticaux ou surfaces cylindriques assemblées reliées entre elles, à condition qu\'elles forment une surface continue.

## Options

Vide

## Propriétés

***Remarque***: les noms de certaines propriétés de cette liste diffèrent un peu des mêmes paramètres que ceux utilisés dans l\'éditeur de fenêtre de tâche.

### Données


{{TitleProperty|Base}}

Remarque: il est conseillé de ne pas modifier la propriété Placement des opérations de chemin. Déplacez ou faites pivoter le modèle de tâche de chemin selon vos besoins.

-    **Placement**: Placement global \[position et rotation\] de l\'objet - par rapport à l\'origine (ou l\'origine du conteneur de l\'objet parent)

    -   
        **Angle**
        
        : Angle en degrés appliqué à la rotation de l\'objet autour de la valeur de la propriété Axis

    -   
        **Axis**
        
        : Axe (un ou plusieurs) autour duquel l\'objet doit tourner, défini dans les sous-propriétés : x, y, z.

        -   
            **X**
            
            : valeur de l\'axe x

        -   
            **Y**
            
            : valeur de l\'axe des y

        -   
            **Z**
            
            : valeur de l\'axe z

    -   
        **Position**
        
        : Position de l\'objet, définie dans les sous-propriétés : x, y, z - par rapport à l\'origine (ou l\'origine du conteneur de l\'objet parent)

        -   
            **X**
            
            : valeur de distance x

        -   
            **Y**
            
            : valeur de la distance en y

        -   
            **Z**
            
            : valeur de distance en z

-    **Label**: Nom de l\'objet fourni par l\'utilisateur (UTF-8)


{{TitleProperty|Depth}}

-    **Clearance Height**: hauteur nécessaire pour supprimer les pinces et les obstructions.

-    **Final Depth**: profondeur finale de l\'outil - valeur la plus basse de Z.

-    **Finish Depth**: maximum de matériau retiré lors du passage final.

-    **Safe Height**: seuil supérieur duquel les mouvements rapides sont autorisés.

-    **Start Depth**: profondeur initiale de l\'outil - première profondeur de coupe en Z.

-    **Step Down**: abaissement incrémentiel de l\'outil.


{{TitleProperty|Face}}

-    **BoundaryShape**: Forme à utiliser pour le calcul de la limite

-    **ClearEdges**: Effacer les bords de la surface (applicable uniquement à BoundBox)

-    **ExcludeRaisedAreas**: Exclure le fraisage des zones en relief à l\'intérieur de la face.

-    **Offset Pattern**: Motif de décalage à utiliser. (Sélectionnez de quelle manière les mouvements horizontaux doivent être effectués).


{{TitleProperty|Path}}

-    **Active**: mettre à Falsepour empêcher l\'opération de générer du code.

-    **Base**: géométrie de base pour cette opération.

-    **Comment**: commentaire facultatif pour cette opération.

-    **Coolant Mode**: mode de refroidissement pour cette opération.

-    **Cycle Time**: estimation du temps de cycle pour cette opération.

-    **Tool Controller**: définit le contrôleur d\'outil utilisé dans l\'opération.

-    **User Label**: étiquette attribuée par l\'utilisateur.


{{TitleProperty|Pocket}}

-    **Cut Mode**: La direction dans laquelle le parcours doit contourner la pièce : sens horaire (ClockWise = CW) ou anti sens horaire (CounterClockWise = CCW).

-    **Extra Offset**: Décalage supplémentaire à appliquer à l\'opération. La direction dépend de l\'opération.

-    **StartAt**: Commencez la poche au centre ou à la limite

-    **Step Over**: Pourcentage du diamètre de l\'outil à dépasser à chaque passage.

-    **Zig Zag Angle**: Angle du motif en zigzag

-    **Offset Pattern**: Motif de dégagement à utiliser

-    **Min Travel**: Utiliser le triage 3D du parcours

-    **Keep Tool Down**: Tente d\'éviter les rétractions inutiles.


{{TitleProperty|Rotation}}

-    **Attempt Inverse Angle**: Tente automatiquement l\'angle inverse si la rotation initiale est incorrecte.

-    **Enable Rotation**: Active la rotation pour accéder aux poches ou aux zones non normales à l\'axe Z.

-    **Inverse Angle**: Inverse l\'angle de la rotation. ***Exemple:** changer une rotation de -22,5 à 22,5 degrés.*

-    **Limit Depth To Face**: Impose la profondeur Z de la face sélectionnée comme valeur minimale de la profondeur finale. Des valeurs utilisateur plus élevées pour la profondeur finale seront observées.

-    **Reverse Direction**: Inverse l\'orientation de l\'opération de 180 degrés.


{{TitleProperty|Start Point}}

-    **Start Point**: point de départ personnalisé pour le chemin de cette opération.

    -   
        **X**
        
        : valeur de distance x.

    -   
        **Y**
        
        : valeur de distance y.

    -   
        **Z**
        
        : valeur de distance z.

-    **Use Start Point**: Mis à True, si vous spécifiez manuellement un point de départ. Définissez le point de départ dans le champ Point de départ des données de propriété.

### Vue

Vide

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Exemple :


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path MillFace/fr
