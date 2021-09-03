---
- GuiCommand:/fr
   Name:Path Pocket Shape
   Name/fr:Path Poche
   MenuLocation:Path → Pocket Shape
   Workbenches:[Path](Path_Workbench/fr.md)
   Shortcut:**P** **O**
   SeeAlso:
---


</div>

## Description

Cet outil crée une opération de poche à partir des faces inférieures ou des parois sélectionnées d\'une ou de plusieurs poches de l\'objet.

L\'objet forme de poche ou Path Pocket Shape est fait pour travailler avec <img alt="" src=images/Path_Job.svg  style="width:24px;"> [Path Tâche](Path_Job/fr.md).

<img alt="" src=images/Path_Pocket_Shape_example.png  style="width:600px;">

## Utilisation


<div class="mw-translate-fuzzy">

1.  Sélectionnez le fond ou une face(s) d\'une poche. Alors qu\'il est généralement plus facile de sélectionner le fond, les faces doivent être sélectionnées lorsqu\'une poche est traversante.
2.  Lancez la commande Pocket Shape à l\'aide de plusieurs méthodes:
    -   En appuyant sur le bouton **<img src="images/Path_Pocket.svg" width=24px> [Pocket Shape](Path_Pocket_Shape/fr.md)** dans la barre d\'outils.
    -   Utilisation du raccourci clavier **P** puis **O**.
    -   Utilisation de la **Path** → **<img src="images/Path_Pocket.svg" width=24px> [Pocket Shape](Path_Pocket_Shape/fr.md)** dans le menu supérieur.
3.  Ajustez les propriétés souhaitées.


</div>

## Propriétés

\'\'\' *Remarque* \'\'\': toutes ces propriétés ne sont pas disponibles dans l\'éditeur de fenêtre de tâches. Certaines ne sont accessibles que dans l\'onglet Données du panneau Vue de propriétés pour cette opération.

#### Base


<div class="mw-translate-fuzzy">

#### Base {#base_1}

Remarque: il est conseillé de ne pas modifier la propriété Placement des opérations de chemin. Déplacez ou faites pivoter le modèle de tâche de chemin selon vos besoins.


</div>

-    {{PropertyData/fr|Placement}}: emplacement global \[position et rotation\] de l\'objet - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent).

    -   
        {{PropertyData/fr|Angle}}
        
        : angle en degrés appliqué à la rotation de l\'objet autour de la valeur de la propriété Axis.

    -   
        {{PropertyData/fr|Axis}}
        
        : axe (un ou plusieurs) autour duquel faire pivoter l\'objet, défini dans les sous-propriétés: x, y, z.

        -   
            {{PropertyData/fr|X}}
            
            : valeur de l\'axe x.

        -   
            {{PropertyData/fr|Y}}
            
            : valeur de l\'axe y.

        -   
            {{PropertyData/fr|Z}}
            
            : valeur de l\'axe z.

    -   
        {{PropertyData/fr|Position}}
        
        : Position de l\'objet, définie dans les sous-propriétés: x, y, z - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent).

        -   
            {{PropertyData/fr|X}}
            
            : valeur de distance x.

        -   
            {{PropertyData/fr|Y}}
            
            : valeur de distance y.

        -   
            {{PropertyData/fr|Z}}
            
            : valeur de distance z.

-    {{PropertyData/fr|Label}}: nom de l\'objet fourni par l\'utilisateur (UTF-8).

#### Profondeur

-    {{PropertyData/fr|Clearance Height}}: hauteur nécessaire pour supprimer les pinces et les obstructions.

-    {{PropertyData/fr|Final Depth}}: profondeur finale de l\'outil - valeur la plus basse de Z.

-    {{PropertyData/fr|Finish Depth}}: Le maximum de matériau retiré lors du passage final. La hauteur (épaisseur) du dernier niveau de coupe - \"\" pour une meilleure finition \".

-    {{PropertyData/fr|Safe Height}}: hauteur au-dessus de laquelle les mouvements rapides sont autorisés. (Hauteur de sécurité rapide entre les sites).

-    {{PropertyData/fr|Start Depth}}: profondeur de départ de l\'outil - \'\' Profondeur de la première coupe en Z \'\'.

-    {{PropertyData/fr|Step Down}}: abaissement incrémental de l\'outil pendant l\'opération.

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;">


<div class="mw-translate-fuzzy">

![](images/Path-DepthsAndHeights.gif ) *Référence visuelle pour les propriétés de profondeur (paramètres)*


</div>

#### Extension

-    {{PropertyData/fr|Coins d'extension}}: lorsque cette option est activée, les bords d\'extension connectés sont combinés à des fils.

-    {{PropertyData/fr|Extension Length Default}}: longueur par défaut des extensions.

#### Face

-    {{PropertyData/fr|Offset Pattern}}: effacement du motif à utiliser. (Sélectionnez la manière dont les mouvements horizontaux doivent être effectués.)

#### Tracé

-    {{PropertyData/fr|Active}}: rend False, pour empêcher l\'opération de générer du code.

-    {{PropertyData/fr|Comment}}: commentaire facultatif pour cette opération.

-    {{PropertyData/fr|User Label}}: étiquette attribuée par l\'utilisateur.

-    {{PropertyData/fr|Tool Controller}}: définit le contrôleur d\'outil utilisé dans l\'opération.

#### Poche

-    {{PropertyData/fr|Cut Mode}}: spécifie un déplacement CW ou CCW pour la coupe.

-    {{PropertyData/fr|Extra Offset}}: décalage supplémentaire à appliquer à l\'opération. La direction dépend du fonctionnement. (Valeur supplémentaire pour rester loin du profil final- *bon pour le parcours grossier*).

-    {{PropertyData/fr|Keep Tool}}: tente d\'éviter les retraits inutiles.

-    {{PropertyData/fr|Min Travel}}: utilise le tri 3D du chemin (lorsque plusieurs géométries de base sont utilisées).

-    {{PropertyData/fr|Start At}}: commence à empocher au centre ou au bord.

-    {{PropertyData/fr|Step Over}}: sélectionne le pas horizontal (**Pourcent** du diamètre de l\'outil: 100% = diamètre de l\'outil).

-    {{PropertyData/fr|Use Outline}}: utilise le contour de la géométrie de base.

-    {{PropertyData/fr|Zig Zag Angle}}: angle du motif en zigzag. (Sélectionnez l'angle de trajectoire par rapport à l'axe X).

#### Rotation

-    {{PropertyData/fr|Attempt Inverse Angle}}: tente automatiquement l\'angle inverse si la rotation initiale est incorrecte.

-    

-    {{PropertyData/fr|Enable Rotation}}: active la rotation pour accéder aux trous non normaux sur l\'axe Z.

-    {{PropertyData/fr|Angle Inverse}}: inverse l\'angle de la rotation. \'\' **Exemple:** change une rotation de -22,5 à 22,5 degrés.\'\'

-    {{PropertyData/fr|Reverse Direction}}: inverse l\'orientation de l\'opération de 180 degrés.

#### Point de départ {#point_de_départ}

-    {{PropertyData/fr|Start Point}}: le point de départ de ce chemin.

-    {{PropertyData/fr|Use Start Point}}: en position True, si vous spécifiez manuellement un point de départ, saisissez Points de départ dans le champ Points de départ des données de la propriété.

## Tasks Window Editor Layout {#tasks_window_editor_layout}


<div class="mw-translate-fuzzy">

## Disposition de l\'éditeur de fenêtre de tâches {#disposition_de_léditeur_de_fenêtre_de_tâches}

*Les descriptions des paramètres sont fournies dans la liste des propriétés ci-dessus.* Cette section est simplement une représentation des paramètres de l'éditeur de fenêtres pour l'opération.


</div>

#### Géométrie de base {#géométrie_de_base}

-   **Add**: ajoute les éléments sélectionnés qui doivent être la base du ou des chemins.
-   **Remove**: supprime le ou les éléments sélectionnés dans la liste emplacement de base.
-   **Edit**: efface tous les éléments de la liste d\'emplacement de base.

#### Extensions

-    {{PropertyData/fr|Show All}}: si cette option est sélectionnée, toutes les extensions potentielles sont visualisées. Extensions activées en violet, extensions désactivées en jaune.

-    {{PropertyData/fr|Extension Corners}}
    

-    {{PropertyData/fr|Extension Length Default}}
    

-   **Enable**

-   **Disable**

-   **Clear**

#### Profondeur {#profondeur_1}

-    {{PropertyData/fr|Start Depth}}
    

-    {{PropertyData/fr|Final Depth}}
    

-    {{PropertyData/fr|Step Down}}
    

#### Hauteur

-    {{PropertyData/fr|Safe Height}}
    

-    {{PropertyData/fr|Clearance Height}}
    

#### Opération

-    {{PropertyData/fr|Tool Controller}}
    

-    {{PropertyData/fr|Cut Mode}}
    

-    {{PropertyData/fr|Pattern}}(motif de décalage)

-    {{PropertyData/fr|Angle}}(angle de zig zag)

-    {{PropertyData/fr|Step Over Percent}}(Pas à pas)

-    {{PropertyData/fr|Pass Extension}}: distance à laquelle l\'opération de surfaçage s\'étendra au-delà des bordes la forme (géométrie de base).

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).


</div>


```python
#Place code example here.
```





{{Path_Tools_navi

}} 
