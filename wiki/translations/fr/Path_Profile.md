---
- GuiCommand:/fr
   Name:Path Profile
   Name/fr:Path Contournage
   MenuLocation:Path → Contournage
   Workbenches:[Path](Path_Workbench/fr.md)
   Version:0.19
---

# Path Profile/fr



## Description

L\'outil <img alt="" src=images/Path_Profile.png  style="width:16px;"> [Contournage](Path_Profile/fr.md) crée une opération de contour basée sur les fonctions sélectionnées du modèle. L\'outil a été introduit dans la version 0.19. Il propose trois opérations qui étaient gérées par des outils distincts dans les versions précédentes.

Toutes les opérations créent des objets qui font partie d\'une **<img src="images/Path_Job.svg" width=24px> [Path Tâche](Path_Job/fr.md)**.

Voici les opérations disponibles :



### Opération Contour 

Une opération **Contour** est la valeur par défaut. Elle crée une simple découpe de contour externe d\'objets 3D complexes basés sur <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/fr.md). Le modèle entier de la tâche sert d\'entrée pour l\'opération, que la géométrie du corps soit sélectionnée ou non lorsque la commande Contour est appelée.



### Opération Contour de face 

Une opération **Contour de face** crée un parcours de contour simple à partir d\'une ou plusieurs faces sélectionnées d\'un objet.



### Opération Contour de bords 

Une opération **Contour de bords** crée un parcours de contour simple à partir des arêtes sélectionnées.

<img alt="" src=images/Path_profile_example.jpg  style="width:600px;">



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Path_Profile.svg" width=16px> [Contournage](Path_Profile/fr.md)**.
    -   Sélectionnez l\'option **Path → <img src="images/Path_Profile.svg" width=16px> Contournage** dans le menu.
2.  Activez la section Géométrie de base en cliquant sur son onglet et sélectionnez les fonctions du modèle de la tâche.
    -   Si aucune fonction n\'est sélectionnée, la commande passe par défaut à une opération **Contournage**, contournant le modèle entier.
    -   Si des faces sont sélectionnées, le résultat est une opération **Contour des faces**.
    -   Si des arêtes sont sélectionnées, alors le résultat est une opération **Contour des bords**.
        **REMARQUE** : cette opération a reçu des améliorations pour permettre la fonctionnalité sur certaines sélections d\'arêtes ouvertes (non bouclées). Voir la section [Remarques d\'utilisation](#Remarques_d'utilisation.md) ci-dessous pour des informations supplémentaires sur les meilleures pratiques pour le contour des arêtes ouvertes.
3.  Activez la section Opération en cliquant sur son onglet et ajustez les paramètres de l\'opération comme vous le souhaitez.
4.  Appuyez sur le bouton **Appliquer** pour prévisualiser l\'opération avec les paramètres actuels.
5.  Cliquez sur le bouton **OK** ou sur le bouton **Annuler** pour créer ou annuler l\'opération.

**Remarque importante : Path Contournage ne prend pas en charge les autres détails de l\'objet. Vous devez ajuster les propriétés, en particulier la profondeur finale, avec soin, une erreur pourrait endommager votre pièce**.

Un point de départ peut être activé à partir de l\'onglet Opération dans l\'éditeur de fenêtre de tâches, en utilisant un emplacement défini dans **Vue de la propriété → Données → Start Point**.

Apportez des ajustements supplémentaires à l\'opération en modifiant les propriétés de l\'opération dans l\'onglet Données de la vue des propriétés. Les propriétés avancées seront situées ici, le cas échéant.



## Remarques d\'utilisation 

-   L\'opération **<img src="images/Path_Profile.svg" width=16px> [Contournage](Path_Profile/fr.md)** est capable de d\'effectuer le contour des **bords ouverts** (une ou plusieurs arêtes continues qui ne forme une boucle vue de la *vue de dessus*)
    -   Il est préférable de sélectionner les bords supérieurs (bords les plus hauts) pour la sélection. Après cela, vous devrez définir manuellement la profondeur finale de l\'opération. La sélection des bords inférieurs uniquement est imprévisible et renverra probablement des trajectoires indésirables dans de nombreuses situations ; cependant, elle renverra des parcours correctes dans certaines situations.
    -   Les bords sélectionnés doivent former un bord continu *tel que vu de la vue de dessus*. Les bords supérieurs sélectionnés peuvent avoir des hauteurs différentes, à condition qu\'ils se connectent à une coordonnée commune (X, Y) - des hauteurs Z différentes sont acceptables dans *certains **\*\**** cas.
        **\*\***Dans certains cas, l\'utilisateur devra inclure dans sa sélection l\'arête de connexion verticale droite entre deux arêtes adjacentes de hauteurs différentes partageant une coordonnée commune (X, Y).
    -   Les bords supérieurs étant sélectionnés, la profondeur finale de l\'opération devra être définie manuellement.
    -   Lors du contour des bords ouverts, la propriété \"Side\" ou \"Cut Side\" est désactivée en interne même si elle sera probablement visible dans la fenêtre de l\'éditeur de tâches et la liste Propriétés dans l\'onglet Données.
-   Lors du contour du modèle entier (un contour complet du modèle), la propriété \"Side\" ou \"Cut Side\" est codée en dur sur \"Outside\" même si elle peut être disponible pour une entrée utilisateur.



## Propriétés

***Remarque***: toutes ces propriétés ne sont pas disponibles dans l\'éditeur de fenêtre de tâches. Certaines ne sont accessibles que dans l\'onglet Données du panneau Vue de propriétés pour cette opération.


{{TitleProperty|Base}}

Remarque : il est conseillé de ne pas modifier la propriété Placement des opérations de parcours. Déplacez ou faites pivoter le modèle de la tâche selon vos besoins.

-    **Placement**: emplacement global \[position et rotation\] de l\'objet - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent).

    -   
        **Angle**
        
        : angle en degrés appliqué à la rotation de l\'objet autour de la valeur de la propriété Axis.

    -   
        **Axis**
        
        : axe (un ou plusieurs) autour duquel faire pivoter l\'objet, défini dans les sous-propriétés: x, y, z.

        -   
            **X**
            
            : valeur de l\'axe x.

        -   
            **Y**
            
            : valeur de l\'axe y.

        -   
            **Z**
            
            : valeur de l\'axe z.

    -   
        **Position**
        
        : position de l\'objet, définie dans les sous-propriétés: x, y, z - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent).

        -   
            **X**
            
            : valeur de distance x.

        -   
            **Y**
            
            : valeur de distance y.

        -   
            **Z**
            
            : valeur de distance z.

-    **Label**: nom de l\'objet fourni par l\'utilisateur (UTF-8).


{{TitleProperty|Depth}}

-    **Clearance Height**: hauteur nécessaire pour supprimer les pinces et les obstructions.

-    **Final Depth**: profondeur finale de l\'outil - valeur la plus basse en Z.

-    **Finish Depth**: maximum de matériau retiré lors du passage final. La hauteur (épaisseur) du dernier niveau de coupe - \"pour une meilleure finition\".

-    **Safe Height**: hauteur au-dessus de laquelle les mouvements rapides sont autorisés. (Hauteur de sécurité rapide entre deux endroits)

-    **Start Depth**: profondeur de départ de l\'outil - *Profondeur de la première coupe en Z*.

-    **Step Down**: descente incrémental de l\'outil pendant l\'opération.

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


{{TitleProperty|Profile}}

-    **Direction**: direction dans laquelle la trajectoire d\'outil doit contourner la pièce: dans le sens horaire \[CW\] ou dans le sens antihoraire \[CCW\].

-    **Expand Profile**: étend le détourage du contour au-delà du décalage supplémentaire.

-    **Expand Profile Step Over**: définit le pourcentage des recouvrement entre les passes, en fonction du diamètre de l\'outil.

-    **Handle Multiple Features**: choix de comment traiter plusieurs fonctionnalités de la géométrie de base.

-    **OffsetExtra**: valeur supplémentaire pour rester à l\'écart du contour final - bon pour l\'ébauche du parcours d\'outil.

-    **Process Circles**: vérifie si vous souhaitez que cette opération de contour s\'applique également aux trous cylindriques, *qui sont normalement percés*.

-    **Process Holes**: vérifie si cette opération de contour doit également traiter les trous dans la géométrie de base. **Notez** que cela n\'inclut pas les trous cylindriques.

-    **Process Perimeter**: vérifie si cette opération de contour doit également traiter le périmètre extérieur des formes géométriques de base.

-    **Side**: (coupe le côté) côté du bord que l\'outil doit couper. Cela n\'a d\'importance que si *Utiliser la compensation* est coché.

-    **Use Compensation**: si cette case est cochée, l\'opération de contour est décalée du rayon de l\'outil. La direction du décalage est déterminée par le côté de coupe.


{{TitleProperty|Rotation}}

-    **Attempt Inverse Angle**: tente automatiquement l\'angle inverse si la rotation initiale est incorrecte.

-    **Enable Rotation**: active la rotation pour accéder aux poches ou aux zones qui ne sont pas normales à l\'axe Z.

-    **Inverse Angle**: inverse l\'angle de rotation. ***Exemple :** change une rotation de -22,5 à 22,5 degrés.*

-    **Limit Depth To Face**: applique la profondeur Z de la face sélectionnée comme valeur la plus basse pour la profondeur finale. Des valeurs utilisateur plus élevées pour la profondeur finale seront observées.

-    **Reverse Direction**: inverse l\'orientation de l\'opération de 180 degrés.


{{TitleProperty|Start Point}}

-    **Start Point**: point de départ personnalisé pour le parcours de cette opération.

    -   
        **X**
        
        : valeur de distance x.

    -   
        **Y**
        
        : valeur de distance y.

    -   
        **Z**
        
        : valeur de distance z.

-    **Use Start Point**: mis à True, si vous spécifiez manuellement un point de départ. Définissez le point de départ dans le champ Start Point des propriétés de données.



## Disposition de l\'éditeur de la fenêtre des tâches 

*Les descriptions des paramètres sont fournies dans la liste des propriétés ci-dessus.* Cette section est simplement une représentation des paramètres de l'éditeur de fenêtres pour l'opération.



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

-    **Tool Controller**
    

-    **Coolant Mode**
    

-    **Cut Side ****
    

-    **Direction**
    

-    **Extra Offset**
    

-    **Enable Rotation**
    

-    **Use Start Point**
    

-    **Use Compensation**
    

-    **Process Holes ****
    

-    **Process Circles ****
    

-    **Process Perimeter ****
    

**\*\*** La disponibilité change en fonction des sélections dans la section Base Geometry.



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
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Profile/fr
