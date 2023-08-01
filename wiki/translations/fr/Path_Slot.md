---
- GuiCommand:
   Name:Path Slot
   Name/fr:Path Rainure
   MenuLocation:Path → Rainurer
   Workbenches:[Path](Path_Workbench/fr.md)
   Version:0.19
---

# Path Slot/fr

## Description

L\'outil <img alt="" src=images/Path_Slot.svg  style="width:24px;"> [Rainure](Path_Slot/fr.md) crée une opération de rainurage simple en utilisant différentes méthodes de saisie.

Les entrées comprennent :

-   sélection d\'une ou plusieurs faces ou arêtes.
-   sélection de deux sommets.
-   saisie de deux points personnalisés.

L\'objet Path Rainure est conçu pour faire partie d\'une <img alt="" src=images/Path_Job.svg  style="width:24px;"> [Path Tâche](Path_Job/fr.md).



## Utilisation

1.  Sélectionner la géométrie de référence sur le modèle :
    -   une ou plusieurs faces ou arêtes.
    -   deux sommets.
    -   ***rien*** pour utiliser deux points personnalisés saisis dans la vue Propriété de l\'onglet Données : Custom Point1 et Custom Point2.
2.  Lancez la commande Rainure en utilisant plusieurs méthodes :
    -   En appuyant sur la touche **<img src="images/Path_Slot.svg" width=24px> [Rainurer](Path_Slot/fr.md)** dans la barre d\'outils.

#\* En utilisant **Path** → **<img src="images/Path_Slot.svg" width=24px> [Rainurer](Path_Slot/fr.md)** du menu.

1.  Ajustez les propriétés souhaitées. Les descriptions des propriétés disponibles se trouvent ci-dessous.



### Remarques d\'utilisation 

-   Toutes les rainures :
    -   Le début et la fin d\'un parcours de rainure peuvent être étendus ou raccourcis. Utilisez les propriétés \Extend Path Start\ et \Extend Path End\.
    -   Utilisez la propriété \Layer Mode\ pour couper la rainure en mode \Single-pass\ à la profondeur finale, ou en mode \Multi-pass\ en utilisant la propriété \Step Down\ disponible.
    -   Activez la propriété \Reverse Direction\ pour inverser la direction du parcours de la coupe.

-   Rainures linéaires :
    -   Actuellement, il n\'est pas possible de décaler latéralement (parallèlement à la trajectoire) les rainures linéaires. ***Exemple :*** supposons que le diamètre de l\'outil soit inférieur à la largeur de la zone de rainure à dégager. Le comportement actuel de cette opération est de créer un ensemble de parcours sur un plan le long de la ligne centrale de la rainure désignée, ce qui aura pour conséquence que le volume de la rainure ne sera pas entièrement détouré. Certains utilisateurs souhaiteraient que l\'opération crée plusieurs parcours décalés latéralement pour dégager l\'ensemble de la zone de la rainure. Cela n\'est pas directement possible mais peut être réalisé en utilisant les \"Points personnalisés\", voir \"Fraisage vertical\" ci-dessous. Il est également possible d\'utiliser l\'opération Poche pour un tel détourage.
    -   Créer une rainure linéaire personnalisée en utilisant les propriétés \"Custom Point1\" et \"Custom Point2\" sans sélection de géométrie. ***Exemple :*** lancez une opération de rainurage depuis l\'interface graphique et cliquez sur \OK\ pour sauvegarder. Localisez et éditez les propriétés \Custom Point1\ et \Custom Point2\ dans l\'onglet Données de l\'opération de rainurage nouvellement créée. Recalculez l\'opération pour mettre à jour le parcours.

-   Fraisage vertical :
    -   La plupart des outils de Path ne peuvent pas réaliser un parcours sur un seul plan vertical car la projection sur le plan horizontal a une surface nulle (une limitation interne). L\'opération de rainurage rend cela possible en sélectionnant des \"points personnalisés\" qui définissent une ligne parallèle au plan vertical et des paramètres de profondeur appropriés.

-   Rainures en arc/circulaire :
    -   Créations de rainures en arc/circulaire
        1.  Vous devez sélectionner un arc inférieur de la rainure. Cela produira un parcours directement sur le bord de l\'arc que vous avez sélectionné.
        2.  Vous devrez ensuite modifier la propriété \Extend Radius\ dans l\'onglet \"Données\" de l\'opération. En utilisant l\'éditeur d\'expression, définissez-la à \OpToolDiameter / 2.0\ ou à la version négative \OpToolDiameter / -2.0\, selon que vous avez sélectionné l\'arc intérieur ou extérieur de la rainure.
        3.  Recalculer l\'opération.
        4.  Gardez à l\'esprit que si le diamètre de l\'outil n\'est pas égal à la largeur de la rainure, le parcours ***ne sera pas*** à l\'emplacement correct. Dans ce cas, ajustez la valeur de la propriété \Extend Radius\ mentionnée ci-dessus.
    -   Actuellement, les utilisateurs ne sont pas en mesure de créer une trajectoire en arc/circulaire personnalisée. Une troisième propriété \Custom Center\ devra être ajoutée, ainsi que des modifications supplémentaires au code de base.



## Propriétés

***Remarque***: toutes ces propriétés ne sont pas disponibles dans l\'éditeur de fenêtre de tâches. Certaines ne sont accessibles que dans l\'onglet Données du panneau Vue de propriétés pour cette opération.


{{TitleProperty|Base}}

Remarque : il est conseillé de ne pas modifier la propriété Placement des opérations de parcours. Il convient plutôt de déplacer ou de faire pivoter le modèle Path Tâche selon les besoins.

-    **Placement**: placement global \[position et rotation\] de l\'objet - par rapport à l\'origine (ou à l\'origine du conteneur d\'objet parent)

    -   
        **Angle**
        
        : angle en degrés appliqué à la rotation de l\'objet autour de la valeur de la propriété Axis

    -   
        **Axis**
        
        : axe(s) autour duquel faire pivoter l\'objet, défini dans les sous-propriétés: X, Y, Z

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
        
        : position de l\'objet, définie dans les sous-propriétés: X, Y, Z - par rapport à l\'origine (ou à l\'origine du conteneur d\'objet parent)

        -   
            **X**
            
            : valeur de distance en X

        -   
            **Y**
            
            : valeur de distance en Y

        -   
            **Z**
            
            : valeur de distance en Z

-    **Label**: nom d\'objet fourni par l\'utilisateur (UTF-8)


{{TitleProperty|Depth}}

-    **Clearance Height**: hauteur nécessaire pour supprimer les brides et les obstructions.

-    **Final Depth**: profondeur finale de l\'outil - valeur la plus basse de Z.

-    **Finish Depth**: le maximum de matériau retiré lors du passage final. La hauteur (épaisseur) du dernier niveau de coupe - *pour une meilleure finition*.

-    **Safe Height**: hauteur au-dessus de laquelle les mouvements rapides sont autorisés. (hauteur de sécurité rapide entre les sites).

-    **Start Depth**: profondeur de départ de l\'outil - *Profondeur de la première coupe en Z*.

-    **Step Down**: pas de descente incrémentale de l\'outil pendant l\'opération.

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:300px;"> 
*Référence visuelle pour les propriétés de profondeur (paramètres)*


{{TitleProperty|Path}}

-    **Active**: mettre à False pour empêcher l\'opération de générer du code.

-    **Base**: géométrie de base pour cette opération.

-    **Comment**: commentaire facultatif pour cette opération.

-    **Coolant Mode**: mode de refroidissement pour cette opération.

-    **Cycle Time**: estimation du temps de cycle pour cette opération.

-    **Tool Controller**: définit le contrôleur d\'outil utilisé dans l\'opération.

-    **User Label**: étiquette attribuée par l\'utilisateur.


{{TitleProperty|Slot}}

-    **Custom Point1**: point de départ personnalisé du parcours de la rainure.

-    **Custom Point2**: point de fin personnalisé du parcours de la rainure.

-    **Cut Pattern**: motif de détourage géométrique à utiliser pour l\'opération.

-    **Extend Path End**: positif étend la fin du parcours, négatif raccourcit.

-    **Extend Path Start**: positif étend le début du parcours, négatif raccourcit.

-    **Extend Radius**: pour les arcs/arêtes circulaires, décalez le rayon de la trajectoire.

-    **Layer Mode**: opération en une seule passe en profondeur ou en plusieurs passes jusqu\'à la profondeur finale.

-    **Path Orientation**: orientation du parcours en fonction de la ou des entités sélectionnées.

-    **Reference1**: point à utiliser sur la première entité sélectionnée.

-    **Reference2**: point à utiliser sur la deuxième entité sélectionnée.

-    **Reverse Direction**: option pour inverser la direction de coupe du parcours de la rainure.


{{TitleProperty|Start Point}}

-    **Start Point**: point de départ personnalisé pour le parcours de cette opération.

    -   
        **X**
        
        : valeur de distance en X.

    -   
        **Y**
        
        : valeur de distance en Y.

    -   
        **Z**
        
        : valeur de distance en Z.

-    **Use Start Point**: mis à True, si vous spécifiez manuellement un point de départ. Définissez le point de départ dans le champ Start Point des propriétés de données.



## Disposition de l\'éditeur de la fenêtre des tâches 

*Les descriptions des paramètres sont fournies dans la liste des propriétés ci-dessus.*

Cette section est simplement une représentation des paramètres de l'éditeur de fenêtres pour l'opération.



### Géométrie de base 

-   **Ajouter** : ajoute le(s) élément(s) sélectionné(s) qui doit(vent) être la(les) base(s) pour le(s) trajectoire(s).
-   **Enlever** : supprime le ou les éléments sélectionnés dans la liste de la géométrie de base.
-   **Réinitialiser** : efface tous les éléments de la liste de la géométrie de base.



### Profondeurs

-    **Start Depth**
    

-    **Final Depth**
    

-    **Step Down**
    



### Hauteurs

-    **Safe Height**
    

-    **Clearance Height**
    



### Opération

-    **Tool Controller**: l\'outil et ses paramètres à utiliser pour cette opération

-    **Coolant Mode**: mode de refroidissement pour cette opération.

-    **Start Reference ****: point à utiliser sur la première entité sélectionnée.

-    **End Reference ****: point à utiliser sur la deuxième entité sélectionnée.

-    **Extend Path End**: positif étend la fin du parcours, négatif raccourcit.

-    **Extend Path Start**: positif étend le début du parcours, négatif raccourcit.

-    **Layer Mode**: opération en une seule passe en profondeur ou en plusieurs passes jusqu\'à la profondeur finale.

-    **Path Orientation ****: orientation du parcours en fonction des entités sélectionnées.

-    **Reverse Direction**: option pour inverser la direction de coupe du parcours de la rainure.

**\*\*** la visibilité change en fonction de la géométrie de base sélectionnée.



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
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Slot/fr
