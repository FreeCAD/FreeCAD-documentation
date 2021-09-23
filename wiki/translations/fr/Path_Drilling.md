---
- GuiCommand:/fr
   Name:Path Drilling
   Name/fr:Path Perçage
   MenuLocation:Path → Perçage
   Workbenches:[Path](Path_Workbench/fr.md)
---

# Path Drilling/fr

## Description

La commande Perçage génère une opération de perçage durant l\'opération.

<img alt="" src=images/Path_Drilling_Sample.png  style="width:400px;"> 
*Ci-dessus: exemple d'opérations de perçage*

## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le Button **<img src="images/Path_Drilling.svg" width=16px> [Perçage](Path_Drilling/fr.md)**.
    -   Sélectionnez l\'option **Path → <img src="images/Path_Drilling.svg" width=16px> Perçage** dans le menu.
2.  Dans la section **Opération** :
    -   Sélectionnez un **Contrôleur d'outil**.
    -   Sélectionnez un **Mode de refroidissement**.
    -   En option, activez et ajustez les éléments suivants :
        -   
            **Peck**
            
            définissez la **Depth**.

        -   
            **Dwell**
            
            définit le **Time** en secondes.

        -   
            **Extended Depth**
            
            .
3.  Dans la section **Géométrie de base**, vérifiez que la liste correspond aux trous destinés à être traités, et ajustez l\'ajout, l\'activation ou la désactivation, si nécessaire. Les trous peuvent être ajoutés en sélectionnant les faces des murs des Trous.
4.  Dans la section **Depths**, vérifiez et ajustez si nécessaire les **Start Depth** et **Final Depth**.
5.  Dans la section **Heights**, vérifiez et, si nécessaire, ajustez les **Safe Height** et **Clearance Height**.
6.  Appuyez sur le bouton **OK** pour générer le(s) chemin(s) de perçage.

## Remarques

-   Lorsque vous utilisez des arêtes pour la géométrie de base, sélectionnez toujours le bord inférieur du trou.
-   Vérifiez toujours que l\'outil choisi est le bon diamètre pour le(s) trou(s) sélectionné(s).
-   **Peck désactivé** génère (cycles de forage pré-programmés G81). **Peck activé** génère (cycles de forage prédéfinis G83).
-   **Dwell activé** est actuellement non pris en charge, mais il est destiné à générer (cycles de forage fixes G82).

## Propriétés

\'\'\' *Remarque* \'\'\': toutes ces propriétés ne sont pas disponibles dans l\'éditeur de fenêtre de tâches. Certaines ne sont accessibles que dans l\'onglet Données du panneau Vue de propriétés pour cette opération.

#### Base

Remarque: il est conseillé de ne pas modifier la propriété Placement des opérations de chemin. Déplacez ou faites pivoter le modèle de tâche de chemin selon vos besoins.

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

-    {{PropertyData/fr|Disabled}}: liste des fonctionnalités désactivées.

#### Profondeur

-    {{PropertyData/fr|Clearance Height}}: hauteur nécessaire pour supprimer les pinces et les obstructions.

-    {{PropertyData/fr|Final Depth}}: profondeur finale de l\'outil - valeur la plus basse de Z.

-    {{PropertyData/fr|Safe Height}}: hauteur au-dessus de laquelle les mouvements rapides sont autorisés. (Hauteur de sécurité rapide entre les sites).

-    {{PropertyData/fr|Start Depth}}: profondeur de départ de l\'outil - *profondeur de la première coupe en Z*.

-    {{PropertyData/fr|Add Tip Length}}: calcule la longueur de la pointe et soustrait de la profondeur finale.

-    {{PropertyData/fr|Dwell Enabled}}: activer le temps (? ndt).

-    {{PropertyData/fr|Dwell Time}}: le temps de pause entre les cycles de picage.

-    {{PropertyData/fr|Peck Depth}}: profondeur de forage incrémental avant de se rétracter pour nettoyer les copeaux.

-    {{PropertyData/fr|Peck Enabled}}: active le picage.

-    {{PropertyData/fr|Retract Height}}: la hauteur du début de l\'alimentation et la hauteur lors de la rétraction de l\'outil lorsque le tracé est terminé.

-    {{PropertyData/fr|Return Level}}: contrôle le retrait de l\'outil. Par défaut = G98.

#### Trajectoire

-    {{PropertyData/fr|Active}}: mis à False, pour empêcher l\'opération de générer du code.

-    {{PropertyData/fr|Comment}}: commentaire facultatif pour cette opération.

-    {{PropertyData/fr|User Label}}: étiquette attribuée par l\'utilisateur.

-    {{PropertyData/fr|Tool Controller}}: définit le contrôleur d\'outil utilisé dans l\'opération.

#### Rotation (*si disponible*) 

-    {{PropertyData/fr|Attempt Inverse Angle}}: tente automatiquement l\'angle inverse si la rotation initiale est incorrecte.

-    

-    {{PropertyData/fr|Enable Rotation}}: active la rotation pour accéder aux trous non normaux sur l\'axe Z.

-    {{PropertyData/fr|Angle Inverse}}: inverse l\'angle de la rotation. \'\' **Exemple:** change une rotation de -22,5 à 22,5 degrés.\'\'

-    {{PropertyData/fr|Reverse Direction}}: inverse l\'orientation de l\'opération de 180 degrés.

## Disposition de l\'éditeur de fenêtre de tâches 

*Les descriptions des paramètres sont fournies dans la liste des propriétés ci-dessus.* Cette section est simplement une représentation des paramètres de l'éditeur de fenêtres pour l'opération.

#### Géométrie de base 

-   **Add**: ajoute les éléments sélectionnés qui doivent être la base du ou des chemins.
-   **Supprimer**: supprime le ou les éléments sélectionnés dans la liste géométrie de base.
-   **Clear**: efface tous les éléments de la liste géométrie de base.

#### Emplacement de base 

-   **Add**: ajoute un emplacement de coordonnées (X, Y) à l\'opération de forage en cours.
-   **Remove**: supprime le ou les éléments d\'emplacement sélectionnés de la liste Emplacement de base.
-   **Edit**: édite l\'élément de lieu sélectionné.

#### Profondeur 

-    {{PropertyData/fr|Start Depth}}
    

-    {{PropertyData/fr|Final Depth}}
    

#### Hauteur

-    {{PropertyData/fr|Safe Height}}
    

-    {{PropertyData/fr|Clearance Height}}
    

#### Opération

-    {{PropertyData/fr|Tool Controller}}
    

-    {{PropertyData/fr|Retract Height}}
    

-    {{PropertyData/fr|Peck}}
    

-    {{PropertyData/fr|Peck Depth}}
    

-    {{PropertyData/fr|Dwell}}
    

-    {{PropertyData/fr|Dwell Time}}
    

-    {{PropertyData/fr|Use Tip Length}}
    

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
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path Drilling/fr
