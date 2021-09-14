---
- GuiCommand:/fr
   Name:Path Profile
   Name/fr:Path Profilage
   MenuLocation:Path → Profilage
   Workbenches:[Path](Path_Workbench/fr.md)
   Version:0.19
---

## Description

L\'outil **<img src="images/Path_Profile.png" width=16px> [Profile](Path_Profile/fr.md)** crée une opération de contour basée sur les fonctions sélectionnées du modèle. L\'outil a été introduit dans la version 0.19. Il propose trois opérations qui étaient gérées par des outils distincts dans les versions précédentes.

Toutes les opérations créent des objets qui font partie d\'une **<img src="images/Path_Job.svg" width=24px> [Path Tâche](Path_Job/fr.md)**.

Voici les opérations disponibles:

### Opération de contour 

Une opération **Contour** est la valeur par défaut. Elle crée une simple découpe de contour externe d\'objets 3D complexes basés sur <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/fr.md). Le modèle entier de la Tâche sert d\'entrée pour l\'opération, que la géométrie du corps soit sélectionnée ou non lorsque la commande Contour est appelée.

### Opération Profile Face 

Une opération **Profile Face** crée un tracé de contour simple à partir d\'une ou plusieurs faces sélectionnées d\'un objet.

### Opération Profile Edges 

Une opération **Profile Edges** crée un tracé de contour simple à partir des arêtes sélectionnées.

<img alt="" src=images/Path_profile_example.jpg  style="width:600px;">

## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Path_Profile.svg" width=16px> [Path Profilage](Path_Profile/fr.md)**.
    -   Sélectionnez l\'option **Path → <img src="images/Path_Profile.svg" width=16px> Profilage** dans le menu.
2.  Activez la section Géométrie de base en cliquant sur son onglet, et sélectionnez les caractéristiques du modèle de travail.
    -   Si aucune caractéristique n\'est sélectionnée, la commande passe par défaut à une opération **Contour**, contournant le modèle entier.
    -   Si des faces sont sélectionnées, le résultat est une opération **Profile Face**.
    -   Si des arêtes sont sélectionnées, alors le résultat est une opération **Profile Edges**.
        **REMARQUE** : Cette opération a reçu des améliorations pour permettre la fonctionnalité sur certaines sélections d\'arêtes ouvertes (non bouclées). Voir la section **Notes d\'utilisation** ci-dessous pour des informations supplémentaires sur les meilleures pratiques pour le profilage des arêtes ouvertes.
3.  Activez la section Opération en cliquant sur son onglet, et ajustez les paramètres de l\'opération comme vous le souhaitez.
4.  Appuyez éventuellement sur le bouton **Appliquer** pour prévisualiser l\'opération avec les paramètres actuels.
5.  Cliquez sur le bouton **OK** ou sur le bouton **Annuler** pour créer ou annuler l\'opération.

**Remarque importante: Path Profilage ne prend pas en charge les autres détails de l\'objet. Vous devez ajuster les propriétés, en particulier la profondeur finale, avec soin, une erreur pourrait endommager votre pièce**.

Un point de départ peut être activé à partir de l\'onglet Opération dans l\'éditeur de fenêtre de tâches, en utilisant un emplacement défini dans **Property View → Data → Start Point**.

Apportez des ajustements supplémentaires à l\'opération en modifiant les propriétés de l\'opération dans l\'onglet Données de la vue des propriétés. Les propriétés avancées seront situées ici, le cas échéant.

## Remarques d\'utilisation 

-   L\'opération **<img src="images/Path_Profile.svg" width=16px> [Profil](Path_Profile/fr.md)** est capable de profiler **bords ouverts** (une ou plusieurs arêtes continues qui ne forme une boucle vue de la *vue de dessus*)
    -   Il est préférable de sélectionner les bords supérieurs (bords les plus hauts) pour la sélection. Après cela, vous devrez définir manuellement la profondeur finale de l\'opération. La sélection des bords inférieurs uniquement est imprévisible et renverra probablement des trajectoires indésirables dans de nombreuses situations ; cependant, elle renverra des trajectoires correctes dans certaines situations.
    -   Les bords sélectionnés doivent former un bord continu *tel que vu de la vue de dessus*. Les bords supérieurs sélectionnés peuvent avoir des hauteurs différentes, à condition qu\'ils se connectent à une coordonnée commune (X, Y) - des hauteurs Z différentes sont acceptables dans *certains **\*\**** cas.
        **\*\***Dans certains cas, l\'utilisateur devra inclure dans sa sélection l\'arête de connexion verticale droite entre deux arêtes adjacentes de hauteurs différentes partageant une coordonnée commune (X, Y).
    -   Les bords supérieurs étant sélectionnés, la profondeur finale de l\'opération devra être définie manuellement.
    -   Lors du profilage des bords ouverts, la propriété \Side\ ou\ Cut Side\ est désactivée en interne même si elle sera probablement visible dans la fenêtre de l\'éditeur de tâches et la liste Propriétés dans l\'onglet Données.
-   Lors du profilage du modèle entier (un contour complet du modèle), la propriété \Side\ ou\ Cut Side\ est codée en dur sur \Outside\ même si elle peut être disponible pour une entrée utilisateur.

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
        
        : position de l\'objet, définie dans les sous-propriétés: x, y, z - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent).

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

-    {{PropertyData/fr|Finish Depth}}: maximum de matériau retiré lors du passage final. La hauteur (épaisseur) du dernier niveau de coupe - \"pour une meilleure finition\".

-    {{PropertyData/fr|Safe Height}}: hauteur au-dessus de laquelle les mouvements rapides sont autorisés. (Hauteur de sécurité rapide entre deux endroits)

-    {{PropertyData/fr|Start Depth}}: profondeur de départ de l\'outil - *Profondeur de la première coupe en Z*.

-    {{PropertyData/fr|Step Down}}: abaissement incrémental de l\'outil pendant l\'opération.

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:300px;"> 
*Référence visuelle pour les propriétés de profondeur (paramètres)*

#### Tracé

-    {{PropertyData/fr|Active}}: mettre à Falsepour empêcher l\'opération de générer du code.

-    {{PropertyData/fr|Base}}: géométrie de base pour cette opération.

-    {{PropertyData/fr|Comment}}: commentaire facultatif pour cette opération.

-    {{PropertyData/fr|Coolant Mode}}: mode de refroidissement pour cette opération.

-    {{PropertyData/fr|Cycle Time}}: estimation du temps de cycle pour cette opération.

-    {{PropertyData/fr|Tool Controller}}: définit le contrôleur d\'outil utilisé dans l\'opération.

-    {{PropertyData/fr|User Label}}: étiquette attribuée par l\'utilisateur.

#### Profilage

-    {{PropertyData/fr|Direction}}: direction dans laquelle la trajectoire d\'outil doit contourner la pièce: dans le sens horaire \[CW\] ou dans le sens antihoraire \[CCW\].

-    {{PropertyData/fr|Expand Profile}}: étend l\'effacement du profil au-delà du décalage supplémentaire.

-    {{PropertyData/fr|Expand Profile Step Over}}: définit le pourcentage de passage, en fonction du diamètre de l\'outil.

-    {{PropertyData/fr|Handle Multiple Features}}: choix de comment traiter plusieurs entités Géométrie de base.

-    {{PropertyData/fr|OffsetExtra}}: valeur supplémentaire pour rester à l\'écart du profil final - bon pour l\'ébauche du parcours d\'outil.

-    {{PropertyData/fr|Process Circles}}: vérifie si vous souhaitez que cette opération de profil s\'applique également aux trous cylindriques, *qui sont normalement percés*.

-    {{PropertyData/fr|Process Holes}}: vérifie si cette opération de profil doit également traiter les trous dans la géométrie de base. **Notez** que cela n\'inclut pas les trous cylindriques.

-    {{PropertyData/fr|Process Perimeter}}: Vérifie si cette opération de profil doit également traiter le périmètre extérieur des formes géométriques de base.

-    {{PropertyData/fr|Side}}: (coupe le côté) côté du bord que l\'outil doit couper. Cela n\'a d\'importance que si «Use Compensation» est True (coché).

-    {{PropertyData/fr|Use Compensation}}: si cette case est cochée, l\'opération de profil est décalée du rayon de l\'outil. La direction du décalage est déterminée par le côté de coupe.

#### Rotation

-    {{PropertyData/fr|Attempt Inverse Angle}}: tente automatiquement l\'angle inverse si la rotation initiale est incorrecte.

-    {{PropertyData/fr|Enable Rotation}}: active la rotation pour accéder aux poches ou aux zones qui ne sont pas normales à l\'axe Z.

-    {{PropertyData/fr|Inverse Angle}}: inverse l\'angle de rotation. \'\' **Exemple:** change une rotation de -22,5 à 22,5 degrés.\'\'

-    {{PropertyData/fr|Limit Depth To Face}}: applique la profondeur Z de la face sélectionnée comme valeur la plus basse pour la profondeur finale. Des valeurs utilisateur plus élevées pour la profondeur finale seront observées.

-    {{PropertyData/fr|Reverse Direction}}: inverse l\'orientation de l\'opération de 180 degrés.

#### Point de départ 

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

## Présentation de l\'éditeur de fenêtre de tâches 

*Les descriptions des paramètres sont fournies dans la liste des propriétés ci-dessus.* Cette section est simplement une représentation des paramètres de l'éditeur de fenêtres pour l'opération.

#### Géométrie de base 

-   **Add**: ajoute les éléments sélectionnés qui doivent être la base du ou des chemins.
-   **Delete**: supprime le ou les éléments sélectionnés dans la liste emplacement de base.
-   **Clear**: efface tous les éléments de la liste d\'emplacement de base.

#### Profondeurs

-    {{PropertyData/fr|Start Depth}}
    

-    {{PropertyData/fr|Final Depth}}
    

-    {{PropertyData/fr|Step Down}}
    

#### Hauteurs

-    {{PropertyData/fr|Safe Height}}
    

-    {{PropertyData/fr|Clearance Height}}
    

#### Opération

-    {{PropertyData/fr|Tool Controller}}
    

-    {{PropertyData/fr|Coolant Mode}}
    

-    {{PropertyData/fr|Cut Side **}}
    

-    {{PropertyData/fr|Direction}}
    

-    {{PropertyData/fr|Extra Offset}}
    

-    {{PropertyData/fr|Enable Rotation}}
    

-    {{PropertyData/fr|Use Start Point}}
    

-    {{PropertyData/fr|Use Compensation}}
    

-    {{PropertyData/fr|Process Holes **}}
    

-    {{PropertyData/fr|Process Circles **}}
    

-    {{PropertyData/fr|Process Perimeter **}}
    

**\*\*** La disponibilité change en fonction des sélections dans la section Géométrie de base.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Exemple:


```python
#Place code example here.
```





{{Path_Tools_navi

}} 
