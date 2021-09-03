---
- GuiCommand:/fr
   Name:Path Slot
   Name/fr:Path Rainure
   Workbenches:[Path](Path_Workbench/fr.md)
   MenuLocation:Path → Slot
   Shortcut:
   Version:0.19
   SeeAlso:
---


</div>

## Description

Cet outil crée une opération de rainurage simple en utilisant différentes méthodes de saisie. Les entrées comprennent:

-   sélection d\'une ou plusieurs faces ou arêtes.
-   sélection de deux sommets.
-   saisie de deux points personnalisés.

L\'objet Path Rainure est conçu pour faire partie d\'une <img alt="" src=images/Path_Job.svg  style="width:24px;"> [Path Tâche](Path_Job/fr.md).

## Utilisation

1.  Select the reference geometry on the model:.
    -   one or more faces or edges.
    -   two vertices.
    -   \'\'\' *nothing* \'\'\' to use two custom points entered in the Property View of the Data tab: Custom Point1 and Custom Point2.
2.  Invoke the Slot command using several methods:
    -   Pressing the **<img src="images/Path_Slot.svg" width=24px> [Slot](Path_Slot.md)** button in the toolbar.

\#\* Using the ** Path** → **<img src="images/Path_Slot.svg" width=24px> [Slot](Path_Slot.md)** entry from the top menu.

1.  Adjust the desired properties. Descriptions of available properties are found below.

#### Usage Notes {#usage_notes}


<div class="mw-translate-fuzzy">

1.  Sélectionnez la géométrie de référence sur le modèle:.
    -   une ou plusieurs faces ou arêtes.
    -   deux sommets.
    -   \'\'\' *rien* \'\'\' pour utiliser deux points personnalisés entrés dans la vue des propriétés de l\'onglet Données: Point1 personnalisé et Point2 personnalisé.
2.  Appelez la commande Slot en utilisant plusieurs méthodes:
    -   En appuyant sur le bouton **<img src="images/Path_Slot.svg" width=24px> [Slot](Path_Slot/fr.md)** dans la barre d\'outils.

\#\* En utilisant la ** Path** → **<img src="images/Path_Slot.svg" width=24px> [Slot](Path_Slot/fr.md)** dans le menu supérieur.

1.  Ajustez les propriétés souhaitées. Les descriptions des propriétés disponibles se trouvent ci-dessous.

#### Notes d\'utilisation {#notes_dutilisation}

-   Tous les emplacements:
    -   Le début et la fin d\'un chemin d\'emplacement peuvent être étendus ou raccourcis. Utilisez les propriétés \Extend Path Start\ et \Extend Path End\.
    -   Utilisez la propriété \Layer Mode\ pour couper la fente en mode \Single-pass\ à la profondeur finale, ou en mode \Multi-pass\ en utilisant la propriété \Step Down\ disponible.
    -   Activez la propriété \Reverse Direction\ pour inverser la direction du chemin de coupe.

-   Fentes linéaires:
    -   Actuellement, il n\'est pas possible de décaler les fentes linéaires latéralement (parallèlement à la trajectoire de déplacement). \'\' **Exemple:** \'\' Supposons que vous ayez un diamètre d\'outil inférieur à la largeur de la zone de rainure que vous effacez. Le comportement actuel de cette opération est de créer un chemin de fente unique au centre de la fente désignée, ce qui aura pour résultat que la zone de fente ne sera pas complètement effacée. Certains utilisateurs souhaiteraient que l\'opération crée plusieurs chemins décalés latéralement pour effacer toute la zone de logement; cette opération n\'est pas prévue, alors - utilisez l\'opération Pocket pour un tel effacement.
    -   Créez une fente linéaire personnalisée en utilisant les propriétés \Custom Point1\ et \Custom Point2\ sans sélection de géométrie. \'\' **Exemple:** \'\' Lancez une opération de slot dans l\'interface graphique et cliquez sur \OK\ pour enregistrer. Recherchez et modifiez maintenant les propriétés \Custom Point1\ et \Custom Point2\ dans l\'onglet Data de l\'opération Slot nouvellement créée. Recalculez l\'opération pour mettre à jour le chemin.

-   Arc/fentes circulaires:
    -   Création de rainures en arc/circulaire
        1.  Vous devrez sélectionner un arc inférieur de la fente. Cela produira un chemin directement sur l\'arête de l\'arc que vous avez sélectionnée.
        2.  Vous devrez ensuite éditer la propriété \Extend Radius\ dans l\'onglet Data de l\'opération. À l\'aide de l\'éditeur d\'expression, définissez-le sur \OpToolDiameter / 2.0\ ou sur la version négative \OpToolDiameter / -2.0\ selon vos besoins, selon que vous avez sélectionné l\'arc intérieur ou extérieur de l\'emplacement.
        3.  Recalculez l\'opération.
        4.  Gardez à l\'esprit que si le diamètre de la fraise n\'est pas égal à la largeur de la fente, le chemin ***ne sera pas*** au bon endroit. Dans ce cas, ajustez la valeur de la propriété \Extend Radius\ mentionnée ci-dessus.
    -   Actuellement, les utilisateurs ne peuvent pas créer un arc/chemin circulaire personnalisé. Une troisième propriété \Custom Center\ devra être ajoutée, ainsi que des modifications supplémentaires à la base de code.


</div>

## Propriétés

\'\'\' *Remarque* \'\'\': toutes ces propriétés ne sont pas disponibles dans l\'éditeur de fenêtre de tâches. Certaines ne sont accessibles que dans l\'onglet Données du panneau Vue de propriétés pour cette opération.

#### Base

Remarque: il est conseillé de ne pas modifier la propriété Placement des opérations de chemin. Déplacez ou faites pivoter le modèle de tâche de chemin selon vos besoins.

-    {{PropertyData/fr|Placement}}: placement global \[position et rotation\] de l\'objet - par rapport à l\'origine (ou à l\'origine du conteneur d\'objet parent)

    -   
        {{PropertyData/fr|Angle}}
        
        : angle en degrés appliqué à la rotation de l\'objet autour de la valeur de la propriété Axis

    -   
        {{PropertyData/fr|Axis}}
        
        : axe(s) autour duquel faire pivoter l\'objet, défini dans les sous-propriétés: x, y, z

        -   
            {{PropertyData/fr|X}}
            
            : valeur de l\'axe x

        -   
            {{PropertyData/fr|Y}}
            
            : valeur de l\'axe y

        -   
            {{PropertyData/fr|Z}}
            
            : valeur de l\'axe z

    -   
        {{PropertyData/fr|Position}}
        
        : position de l\'objet, définie dans les sous-propriétés: x, y, z - par rapport à l\'origine (ou à l\'origine du conteneur d\'objet parent)

        -   
            {{PropertyData/fr|X}}
            
            : valeur de distance x

        -   
            {{PropertyData/fr|Y}}
            
            : valeur de distance y

        -   
            {{PropertyData/fr|Z}}
            
            : valeur de distance z

-    {{PropertyData/fr|Label}}: nom d\'objet fourni par l\'utilisateur (UTF-8)

#### Profondeur

-    {{PropertyData/fr|Clearance Height}}: hauteur nécessaire pour supprimer les pinces et les obstructions.

-    {{PropertyData/fr|Final Depth}}: profondeur finale de l\'outil - valeur la plus basse de Z.

-    {{PropertyData/fr|Finish Depth}}: le maximum de matériau retiré lors du passage final. La hauteur (épaisseur) du dernier niveau de coupe - \"pour une meilleure finition\".

-    {{PropertyData/fr|Safe Height}}: hauteur au-dessus de laquelle les mouvements rapides sont autorisés. (Hauteur de sécurité rapide entre les sites).

-    {{PropertyData/fr|Start Depth}}: profondeur de départ de l\'outil - *Profondeur de la première coupe en Z*.

-    {{PropertyData/fr|Step Down}}: abaissement incrémental de l\'outil pendant l\'opération.

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:300px;"> 
*Référence visuelle pour les propriétés de profondeur (paramètres)*

#### Tracé

-    {{PropertyData/fr|Active}}: mettre à False pour empêcher l\'opération de générer du code.

-    {{PropertyData/fr|Base}}: géométrie de base pour cette opération.

-    {{PropertyData/fr|Comment}}: commentaire facultatif pour cette opération.

-    {{PropertyData/fr|Coolant Mode}}: mode de refroidissement pour cette opération.

-    **Cycle Time**: estimation du temps de cycle pour cette opération.

-    {{PropertyData/fr|Tool Controller}}: définit le contrôleur d\'outil utilisé dans l\'opération.

-    {{PropertyData/fr|User Label}}: étiquette attribuée par l\'utilisateur.

#### Rainure

-    {{PropertyData/fr|Custom Point1}}: entrez un point de départ personnalisé pour le chemin de la rainure.

-    {{PropertyData/fr|Custom Point2}}: entrez un point de fin personnalisé pour le chemin de de la rainure.

-    {{PropertyData/fr|Cut Pattern}}: définissez le motif de nettoyage géométrique à utiliser pour l\'opération.

-    {{PropertyData/fr|Extend Path End}}: positif étend la fin du chemin, négatif raccourcit.

-    {{PropertyData/fr|Extend Path Start}}: positif étend le début du chemin, négatif raccourcit.

-    {{PropertyData/fr|Extend Radius}}: pour les arcs/arêtes circulaires, décalez le rayon de la trajectoire.

-    {{PropertyData/fr|Layer Mode}}: terminez l\'opération en une seule passe en profondeur ou en plusieurs passes jusqu\'à la profondeur finale.

-    {{PropertyData/fr|Path Orientation}}: choisissez l\'orientation du chemin en fonction de la ou des entités sélectionnées.

-    {{PropertyData/fr|Reference1}}: choisissez le point à utiliser sur la première entité sélectionnée.

-    {{PropertyData/fr|Reference2}}: choisissez le point à utiliser sur la deuxième entité sélectionnée.

-    {{PropertyData/fr|Reverse Direction}}: activez cette option pour inverser la direction de coupe du chemin de la rainure.

#### Point de départ {#point_de_départ}

-    {{PropertyData/fr|Start Point}}: point de départ personnalisé pour le chemin de cette opération.

    -   
        {{PropertyData/fr|X}}
        
        : valeur de distance x.

    -   
        {{PropertyData/fr|Y}}
        
        : valeur de distance y.

    -   
        {{PropertyData/fr|Z}}
        
        : valeur de distance z.

-    {{PropertyData/fr|Use Start Point}}: Mis à True, si vous spécifiez manuellement un point de départ. Définissez le point de départ dans le champ Point de départ des données de propriété.

## Présentation de l\'éditeur de fenêtre de tâches {#présentation_de_léditeur_de_fenêtre_de_tâches}

*Les descriptions des paramètres sont fournies dans la liste des propriétés ci-dessus.* Cette section est simplement une représentation des paramètres de l'éditeur de fenêtres pour l'opération.

#### Géométrie de base {#géométrie_de_base}

-   **Add**: ajoute les éléments sélectionnés qui devraient être la ou les bases du ou des chemins
-   **Delete**: supprime les éléments sélectionnés dans la liste Géométrie de base.
-   **Clear**: efface tous les éléments de la liste Géométrie de base.

#### Profondeurs

-    {{PropertyData/fr|Start Depth}}
    

-    {{PropertyData/fr|Final Depth}}
    

-    {{PropertyData/fr|Step Down}}
    

#### Hauteurs

-    {{PropertyData/fr|Safe Height}}
    

-    {{PropertyData/fr|Clearance Height}}
    

#### Opération

-    {{PropertyData/fr|Tool Controller}}: l\'outil et ses paramètres à utiliser pour cette opération

-    {{PropertyData/fr|Coolant Mode}}: mode de refroidissement pour cette opération.

-    {{PropertyData/fr|Start Reference **}}: choisissez le point à utiliser sur la première entité sélectionnée.

-    {{PropertyData/fr|End Reference **}}: choisissez le point à utiliser sur la deuxième entité sélectionnée.

-    {{PropertyData/fr|Extend Path End}}: positif étend la fin du chemin, négatif raccourcit.

-    {{PropertyData/fr|Extend Path Start}}: positif étend le début du chemin, négatif raccourcit.

-    {{PropertyData/fr|Layer Mode}}: terminez l\'opération en une seule passe en profondeur ou en plusieurs passes jusqu\'à la profondeur finale.

-    {{PropertyData/fr|Path Orientation **}}: choisissez l\'orientation du chemin en fonction des entités sélectionnées.

-    {{PropertyData/fr|Reverse Direction}}: activez cette option pour inverser la direction de coupe du chemin de la fente.

**\*\*** la visibilité change en fonction de la géométrie de base sélectionnée.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Exemple:


```python
#Place code example here.
```


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}} 
