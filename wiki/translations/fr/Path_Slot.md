---
- GuiCommand   */fr
   Name   *Path Slot
   Name/fr   *Path Rainure
   MenuLocation   *Path → Rainure
   Workbenches   *[Path](Path_Workbench/fr.md)
   Version   *0.19
---

# Path Slot/fr

## Description

Cet outil crée une opération de rainurage simple en utilisant différentes méthodes de saisie. Les entrées comprennent   *

-   sélection d\'une ou plusieurs faces ou arêtes.
-   sélection de deux sommets.
-   saisie de deux points personnalisés.

L\'objet Path Rainure est conçu pour faire partie d\'une <img alt="" src=images/Path_Job.svg  style="width   *24px;"> [Path Tâche](Path_Job/fr.md).

## Utilisation

1.  Sélectionner la géométrie de référence sur le modèle    *.
    -   une ou plusieurs faces ou arêtes.
    -   deux sommets.
    -   *\'* rien pour utiliser deux points personnalisés saisis dans la vue Propriété de l\'onglet Données    * Custom Point1 et Custom Point2.
2.  Lancez la commande Rainure en utilisant plusieurs méthodes    *
    -   En appuyant sur la touche **<img src="images/Path_Slot.svg" width=24px> [Rainure](Path_Slot/fr.md)** dans la barre d\'outils.

#\* En utilisant **Path** → **<img src="images/Path_Slot.svg" width=24px> [Rainure](Path_Slot/fr.md)** dans le menu supérieur.

1.  Ajustez les propriétés souhaitées. Les descriptions des propriétés disponibles se trouvent ci-dessous.

### Remarques d\'utilisation 

-   Tous les emplacements   *
    -   Le début et la fin d\'un chemin d\'emplacement peuvent être étendus ou raccourcis. Utilisez les propriétés \Extend Path Start\ et \Extend Path End\.
    -   Utilisez la propriété \Layer Mode\ pour couper la fente en mode \Single-pass\ à la profondeur finale, ou en mode \Multi-pass\ en utilisant la propriété \Step Down\ disponible.
    -   Activez la propriété \Reverse Direction\ pour inverser la direction du chemin de coupe.

-   Fentes linéaires   *
    -   Actuellement, il n\'est pas possible de décaler les fentes linéaires latéralement (parallèlement à la trajectoire de déplacement). ***Exemple   **** Supposons que vous ayez un diamètre d\'outil inférieur à la largeur de la zone de rainure que vous effacez. Le comportement actuel de cette opération est de créer un chemin de fente unique au centre de la fente désignée, ce qui aura pour résultat que la zone de fente ne sera pas complètement effacée. Certains utilisateurs souhaiteraient que l\'opération crée plusieurs chemins décalés latéralement pour effacer toute la zone de logement; cette opération n\'est pas prévue, alors - utilisez l\'opération Pocket pour un tel effacement.
    -   Créez une fente linéaire personnalisée en utilisant les propriétés \Custom Point1\ et \Custom Point2\ sans sélection de géométrie. ***Exemple   **** Lancez une opération de slot dans l\'interface graphique et cliquez sur \OK\ pour enregistrer. Recherchez et modifiez maintenant les propriétés \Custom Point1\ et \Custom Point2\ dans l\'onglet Data de l\'opération Slot nouvellement créée. Recalculez l\'opération pour mettre à jour le chemin.

-   Arc/fentes circulaires   *
    -   Création de rainures en arc/circulaire
        1.  Vous devrez sélectionner un arc inférieur de la fente. Cela produira un chemin directement sur l\'arête de l\'arc que vous avez sélectionnée.
        2.  Vous devrez ensuite éditer la propriété \Extend Radius\ dans l\'onglet Data de l\'opération. À l\'aide de l\'éditeur d\'expression, définissez-le sur \OpToolDiameter / 2.0\ ou sur la version négative \OpToolDiameter / -2.0\ selon vos besoins, selon que vous avez sélectionné l\'arc intérieur ou extérieur de l\'emplacement.
        3.  Recalculez l\'opération.
        4.  Gardez à l\'esprit que si le diamètre de la fraise n\'est pas égal à la largeur de la fente, le chemin ***ne sera pas*** au bon endroit. Dans ce cas, ajustez la valeur de la propriété \Extend Radius\ mentionnée ci-dessus.
    -   Actuellement, les utilisateurs ne peuvent pas créer un arc/chemin circulaire personnalisé. Une troisième propriété \Custom Center\ devra être ajoutée, ainsi que des modifications supplémentaires à la base de code.

## Propriétés

***Remarque***   * toutes ces propriétés ne sont pas disponibles dans l\'éditeur de fenêtre de tâches. Certaines ne sont accessibles que dans l\'onglet Données du panneau Vue de propriétés pour cette opération.


{{TitleProperty|Base}}

Remarque   * il est conseillé de ne pas modifier la propriété Placement des opérations de chemin. Déplacez ou faites pivoter le modèle de tâche de chemin selon vos besoins.

-    **Placement**   * placement global \[position et rotation\] de l\'objet - par rapport à l\'origine (ou à l\'origine du conteneur d\'objet parent)

    -   
        **Angle**
        
           * angle en degrés appliqué à la rotation de l\'objet autour de la valeur de la propriété Axis

    -   
        **Axis**
        
           * axe(s) autour duquel faire pivoter l\'objet, défini dans les sous-propriétés   * x, y, z

        -   
            **X**
            
               * valeur de l\'axe x

        -   
            **Y**
            
               * valeur de l\'axe y

        -   
            **Z**
            
               * valeur de l\'axe z

    -   
        **Position**
        
           * position de l\'objet, définie dans les sous-propriétés   * x, y, z - par rapport à l\'origine (ou à l\'origine du conteneur d\'objet parent)

        -   
            **X**
            
               * valeur de distance x

        -   
            **Y**
            
               * valeur de distance y

        -   
            **Z**
            
               * valeur de distance z

-    **Label**   * nom d\'objet fourni par l\'utilisateur (UTF-8)


{{TitleProperty|Depth}}

-    **Clearance Height**   * hauteur nécessaire pour supprimer les pinces et les obstructions.

-    **Final Depth**   * profondeur finale de l\'outil - valeur la plus basse de Z.

-    **Finish Depth**   * le maximum de matériau retiré lors du passage final. La hauteur (épaisseur) du dernier niveau de coupe - \"pour une meilleure finition\".

-    **Safe Height**   * hauteur au-dessus de laquelle les mouvements rapides sont autorisés. (Hauteur de sécurité rapide entre les sites).

-    **Start Depth**   * profondeur de départ de l\'outil - *Profondeur de la première coupe en Z*.

-    **Step Down**   * abaissement incrémental de l\'outil pendant l\'opération.

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width   *300px;"> 
*Référence visuelle pour les propriétés de profondeur (paramètres)*


{{TitleProperty|Path}}

-    **Active**   * mettre à False pour empêcher l\'opération de générer du code.

-    **Base**   * géométrie de base pour cette opération.

-    **Comment**   * commentaire facultatif pour cette opération.

-    **Coolant Mode**   * mode de refroidissement pour cette opération.

-    **Cycle Time**   * estimation du temps de cycle pour cette opération.

-    **Tool Controller**   * définit le contrôleur d\'outil utilisé dans l\'opération.

-    **User Label**   * étiquette attribuée par l\'utilisateur.


{{TitleProperty|Slot}}

-    **Custom Point1**   * entrez un point de départ personnalisé pour le chemin de la rainure.

-    **Custom Point2**   * entrez un point de fin personnalisé pour le chemin de de la rainure.

-    **Cut Pattern**   * définissez le motif de nettoyage géométrique à utiliser pour l\'opération.

-    **Extend Path End**   * positif étend la fin du chemin, négatif raccourcit.

-    **Extend Path Start**   * positif étend le début du chemin, négatif raccourcit.

-    **Extend Radius**   * pour les arcs/arêtes circulaires, décalez le rayon de la trajectoire.

-    **Layer Mode**   * terminez l\'opération en une seule passe en profondeur ou en plusieurs passes jusqu\'à la profondeur finale.

-    **Path Orientation**   * choisissez l\'orientation du chemin en fonction de la ou des entités sélectionnées.

-    **Reference1**   * choisissez le point à utiliser sur la première entité sélectionnée.

-    **Reference2**   * choisissez le point à utiliser sur la deuxième entité sélectionnée.

-    **Reverse Direction**   * activez cette option pour inverser la direction de coupe du chemin de la rainure.


{{TitleProperty|Start Point}}

-    **Start Point**   * point de départ personnalisé pour le chemin de cette opération.

    -   
        **X**
        
           * valeur de distance x.

    -   
        **Y**
        
           * valeur de distance y.

    -   
        **Z**
        
           * valeur de distance z.

-    **Use Start Point**   * Mis à True, si vous spécifiez manuellement un point de départ. Définissez le point de départ dans le champ Point de départ des données de propriété.

## Présentation de l\'éditeur de fenêtre de tâches 

*Les descriptions des paramètres sont fournies dans la liste des propriétés ci-dessus.* Cette section est simplement une représentation des paramètres de l'éditeur de fenêtres pour l'opération.

### Géométrie de base 

-   **Add**   * ajoute les éléments sélectionnés qui devraient être la ou les bases du ou des chemins
-   **Delete**   * supprime les éléments sélectionnés dans la liste Géométrie de base.
-   **Clear**   * efface tous les éléments de la liste Géométrie de base.

### Profondeurs

-    **Start Depth**
    

-    **Final Depth**
    

-    **Step Down**
    

### Hauteurs

-    **Safe Height**
    

-    **Clearance Height**
    

### Opération

-    **Tool Controller**   * l\'outil et ses paramètres à utiliser pour cette opération

-    **Coolant Mode**   * mode de refroidissement pour cette opération.

-    **Start Reference ****   * choisissez le point à utiliser sur la première entité sélectionnée.

-    **End Reference ****   * choisissez le point à utiliser sur la deuxième entité sélectionnée.

-    **Extend Path End**   * positif étend la fin du chemin, négatif raccourcit.

-    **Extend Path Start**   * positif étend le début du chemin, négatif raccourcit.

-    **Layer Mode**   * terminez l\'opération en une seule passe en profondeur ou en plusieurs passes jusqu\'à la profondeur finale.

-    **Path Orientation ****   * choisissez l\'orientation du chemin en fonction des entités sélectionnées.

-    **Reverse Direction**   * activez cette option pour inverser la direction de coupe du chemin de la fente.

**\*\*** la visibilité change en fonction de la géométrie de base sélectionnée.

## Script


**Voir aussi   ***

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Exemple   *


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Slot/fr
