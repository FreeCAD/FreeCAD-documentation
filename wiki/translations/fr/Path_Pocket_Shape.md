---
- GuiCommand   */fr
   Name   *Path Pocket Shape
   Name/fr   *Path Poche
   MenuLocation   *Path → Poche
   Workbenches   *[Path](Path_Workbench/fr.md)
---

# Path Pocket Shape/fr

## Description

Cet outil crée une opération de poche à partir des faces inférieures ou des parois sélectionnées d\'une ou de plusieurs poches de l\'objet.

L\'objet Path Forme de poche est fait pour travailler avec une <img alt="" src=images/Path_Job.svg  style="width   *24px;"> [Path Tâche](Path_Job/fr.md).

<img alt="" src=images/Path_Pocket_Shape_example.png  style="width   *600px;">

## Utilisation

1.  Sélectionnez le fond ou une face(s) d\'une poche. Alors qu\'il est généralement plus facile de sélectionner le fond, les faces doivent être sélectionnées lorsqu\'une poche est traversante.
2.  Il existe plusieurs façons de lancer la commande    *
    -   Appuyez sur le bouton **<img src="images/Path_Pocket_Shape.svg" width=16px> [Poche](Path_Pocket_Shape/fr.md)**.
    -   Sélectionnez l\'option **Path → <img src="images/Path_Pocket_Shape.svg" width=16px> Poche** dans le menu.
3.  Ajustez les propriétés souhaitées.

## Propriétés

\'\'\' *Remarque* \'\'\'   * toutes ces propriétés ne sont pas disponibles dans l\'éditeur de fenêtre de tâches. Certaines ne sont accessibles que dans l\'onglet Données du panneau Vue de propriétés pour cette opération.


{{TitleProperty|Base}}

Remarque   * il est conseillé de ne pas modifier la propriété Placement des opérations de chemin. Déplacez ou faites pivoter le modèle de tâche de chemin selon vos besoins.

-    **Placement**   * emplacement global \[position et rotation\] de l\'objet - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent).

    -   
        **Angle**
        
           * angle en degrés appliqué à la rotation de l\'objet autour de la valeur de la propriété Axis.

    -   
        **Axis**
        
           * axe (un ou plusieurs) autour duquel faire pivoter l\'objet, défini dans les sous-propriétés   * x, y, z.

        -   
            **X**
            
               * valeur de l\'axe x.

        -   
            **Y**
            
               * valeur de l\'axe y.

        -   
            **Z**
            
               * valeur de l\'axe z.

    -   
        **Position**
        
           * Position de l\'objet, définie dans les sous-propriétés   * x, y, z - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent).

        -   
            **X**
            
               * valeur de distance x.

        -   
            **Y**
            
               * valeur de distance y.

        -   
            **Z**
            
               * valeur de distance z.

-    **Label**   * nom de l\'objet fourni par l\'utilisateur (UTF-8).


{{TitleProperty|Depth}}

-    **Clearance Height**   * hauteur nécessaire pour supprimer les pinces et les obstructions.

-    **Final Depth**   * profondeur finale de l\'outil - valeur la plus basse de Z.

-    **Finish Depth**   * Le maximum de matériau retiré lors du passage final. La hauteur (épaisseur) du dernier niveau de coupe - \"\" pour une meilleure finition \".

-    **Safe Height**   * hauteur au-dessus de laquelle les mouvements rapides sont autorisés. (Hauteur de sécurité rapide entre les sites).

-    **Start Depth**   * profondeur de départ de l\'outil - \'\' Profondeur de la première coupe en Z \'\'.

-    **Step Down**   * abaissement incrémental de l\'outil pendant l\'opération.

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width   *500px;"> 
*Référence visuelle pour les propriétés de profondeur (paramètres)*


{{TitleProperty|Extension}}

-    **Extension Corners**   * lorsque cette option est activée, les bords d\'extension connectés sont combinés à des fils.

-    **Extension Length Default**   * longueur par défaut des extensions.


{{TitleProperty|Face}}

-    **Offset Pattern**   * effacement du motif à utiliser. (Sélectionnez la manière dont les mouvements horizontaux doivent être effectués.)


{{TitleProperty|Path}}

-    **Active**   * mis à False, pour empêcher l\'opération de générer du code.

-    **Comment**   * commentaire facultatif pour cette opération.

-    **User Label**   * étiquette attribuée par l\'utilisateur.

-    **Tool Controller**   * définit le contrôleur d\'outil utilisé dans l\'opération.


{{TitleProperty|Pocket}}

-    **Cut Mode**   * spécifie un déplacement CW ou CCW pour la coupe.

-    **Extra Offset**   * décalage supplémentaire à appliquer à l\'opération. La direction dépend du fonctionnement. (Valeur supplémentaire pour rester loin du profil final- *bon pour le parcours grossier*).

-    **Keep Tool**   * tente d\'éviter les retraits inutiles.

-    **Min Travel**   * utilise le tri 3D du chemin (lorsque plusieurs géométries de base sont utilisées).

-    **Start At**   * commence à empocher au centre ou au bord.

-    **Step Over**   * sélectionne le pas horizontal (**Pourcent** du diamètre de l\'outil   * 100% = diamètre de l\'outil).

-    **Use Outline**   * utilise le contour de la géométrie de base.

-    **Zig Zag Angle**   * angle du motif en zigzag. (Sélectionnez l'angle de trajectoire par rapport à l'axe X).


{{TitleProperty|Rotation}}

-    **Attempt Inverse Angle**   * tente automatiquement l\'angle inverse si la rotation initiale est incorrecte.

-    

-    **Enable Rotation**   * active la rotation pour accéder aux trous non normaux sur l\'axe Z.

-    **Angle Inverse**   * inverse l\'angle de la rotation. \'\' **Exemple   *** change une rotation de -22,5 à 22,5 degrés.\'\'

-    **Reverse Direction**   * inverse l\'orientation de l\'opération de 180 degrés.


{{TitleProperty|Start Point}}

-    **Start Point**   * le point de départ de ce chemin.

-    **Use Start Point**   * en position True, si vous spécifiez manuellement un point de départ, saisissez Points de départ dans le champ Points de départ des données de la propriété.

## Présentation de l\'éditeur de fenêtre de tâches 

*Les descriptions des paramètres sont fournies dans la liste des propriétés ci-dessus.* Cette section est simplement une représentation des paramètres de l'éditeur de fenêtres pour l'opération.

### Géométrie de base 

-   **Add**   * ajoute les éléments sélectionnés qui doivent être la base du ou des chemins.
-   **Remove**   * supprime le ou les éléments sélectionnés dans la liste emplacement de base.
-   **Edit**   * efface tous les éléments de la liste d\'emplacement de base.

### Extensions

-    **Show All**   * si cette option est sélectionnée, toutes les extensions potentielles sont visualisées. Extensions activées en violet, extensions désactivées en jaune.

-    **Extension Corners**
    

-    **Extension Length Default**
    

-   **Enable**

-   **Disable**

-   **Clear**

### Profondeurs

-    **Start Depth**
    

-    **Final Depth**
    

-    **Step Down**
    

### Hauteurs

-    **Safe Height**
    

-    **Clearance Height**
    

### Opération

-    **Tool Controller**
    

-    **Cut Mode**
    

-    **Pattern**(motif de décalage)

-    **Angle**(angle de zig zag)

-    **Step Over Percent**(Pas à pas)

-    **Pass Extension**   * distance à laquelle l\'opération de surfaçage s\'étendra au-delà des bordes la forme (géométrie de base).

## Script


**Voir aussi   ***

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Pocket Shape/fr
