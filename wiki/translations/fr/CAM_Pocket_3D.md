---
 GuiCommand:
   Name: CAM Pocket 3D
   Name/fr: CAM Évidement 3D
   MenuLocation: CAM , Évider en 3D
   Workbenches: CAM_Workbench/fr
---

# CAM Pocket 3D/fr

## Description

Cette commande insère un <img alt="" src=images/CAM_3DPocket.svg  style="width:24px;"> [Évidement 3D](CAM_Pocket_3D/fr.md) dans la tâche. Cette opération prend en compte la surface inférieure de la poche, ainsi que les parois sélectionnées qui ne sont pas verticales. Dans son état actuel, cette opération est utilisée pour dégrossir une poche avec des parois non verticales et/ou un fond non horizontal. Une technique de finition courante consiste à utiliser une fraise à bout sphérique avec l\'opération expérimentale de <img alt="" src=images/CAM_Surface.svg  style="width:24px;"> [Surfaçage 3D](CAM_Surface/fr.md).

<img alt="" src=images/Path_3D_Pocket_Sample.png  style="width:600px;"> 
*Exemple d'image de l'opération Évidement 3D utilisée pour dégager un support de batterie cylindrique.*



## Utilisation



### Créer d\'un évidement 3D 

1.  Dans une tâche, sélectionner une ou plusieurs faces dans le modèle de tâche à inclure comme géométrie de base.
2.  Cliquer **<img src="images/CAM_3DPocket.svg" width=16px> [Évider en 3D](CAM_Pocket_3D/fr.md)** ou sélectionnez **CAM** → **<img src="images/CAM_3DPocket.svg" width=16px> [Évider en 3D](CAM_Pocket_3D/fr.md)** du menu.
3.  Choisir un contrôleur d\'outils dans la fenêtre de dialogue de sélection.
4.  Ajouter ou soustraire des éléments de géométrie de base selon les besoins pour configurer l\'opération.
5.  Vérifier l\'onglet Profondeurs pour vous assurer que la profondeur de début, la profondeur de fin et le pourcentage de descente sont corrects. La profondeur finale est déterminée par la sélection de la géométrie du corps et n\'est pas modifiable.
6.  Vérifier l\'onglet Hauteurs pour vous assurer que les hauteurs de sécurité et de dégagement sont appropriées.
7.  Vérifier l\'onglet Opération où le contrôleur d\'outils peut être resélectionné, le mode de coupe peut être configuré pour le fraisage en montée ou conventionnel, le motif peut être défini, le pourcentage de dépassement peut être ajusté et l\'extension de passe peut être appliquée.
8.  Cliquer sur **Appliquer** pour observer le chemin de fraisage des passes de l\'opération. Ajustez les paramètres jusqu\'à ce que vous soyez satisfait de l\'opération.
9.  Cliquer sur **OK** pour enregistrer l\'opération.



## Remarques

-   Tous les parcours générés à partir de cette opération sont basés sur une fraise à bout standard utilisant le diamètre de l\'outil que vous avez sélectionné pour cette opération Évidement 3D.
-   Les fraises à bout sphérique et autres formes ne sont pas respectées pour la génération de parcours même si elles sont sélectionnées comme outil pour cette opération.

## Options

-   Utilisez la propriété **Adaptive Pocket Finish** pour tenter de minimiser l\'usinage en l\'air sous un évidement 3D dans les cas où la poche est un trou dans le modèle.
-   Utilisez la propriété **Adaptive Pocket Start** pour tenter de minimiser le fraisage en l\'air à l\'entrée de la poche. Par exemple, regardez l\'image ci-dessus dans la section [Description](CAM_Pocket_3D#Description.md) de cette page. Afin de réduire le fraisage en l\'air au-dessus de cet évidement 3D, mettez cette propriété sur True et les parcours commenceront plus près de la poche, beaucoup plus près de l\'endroit où la poche commence réellement. Regardez l\'image suivante et notez la différence dans la hauteur de départ du parcours. Le fraisage en l\'air est réduit.

<img alt="" src=images/3D_Pocket_Sample_Adaptive_Start.png  style="width:600px;"> 
*Image d'un exemple d'opération Évidement 3D utilisée pour dégager un support de batterie cylindrique avec le démarrage adaptatif de la poche activé afin de réduire le fraisage de l'air à l'entrée.*

-   Si vous souhaitez traiter l\'ensemble du modèle et du brut, utilisez la propriété **Process Stock Area** mise à True sans sélectionner de géométrie de base.



## Propriétés



### Données


{{TitleProperty|Base}}

Remarque : il est conseillé de ne pas modifier la propriété Placement des opérations de parcours. Il convient plutôt de déplacer ou de faire pivoter le modèle de la Tâche de CAM selon les besoins.

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
            
            : valeur de distance X

        -   
            **Y**
            
            : valeur de la distance Y

        -   
            **Z**
            
            : valeur de distance Z

-    **Label**: nom de l\'objet fourni par l\'utilisateur (UTF-8)


{{TitleProperty|Depth}}

-    **Clearance Height**: hauteur nécessaire pour supprimer les pinces et les obstructions.

-    **Final Depth**: profondeur finale de l\'outil - valeur la plus basse de Z.

-    **Finish Depth**: maximum de matériau retiré lors du passage final.

-    **Safe Height**: seuil supérieur duquel les mouvements rapides sont autorisés.

-    **Start Depth**: profondeur initiale de l\'outil - première profondeur de coupe en Z.

-    **Step Down**: abaissement incrémentiel de l\'outil.


{{TitleProperty|Face}}

-    **Offset Pattern**: effacement du motif à utiliser. (Sélectionnez la manière dont les mouvements horizontaux doivent être effectués.)


{{TitleProperty|Path}}

-    **Active**: mettre à False pour empêcher l\'opération de générer du code.

-    **Base**: géométrie de base pour cette opération.

-    **Comment**: commentaire facultatif pour cette opération.

-    **Coolant Mode**: mode de refroidissement pour cette opération.

-    **Cycle Time**: estimation du temps de cycle pour cette opération.

-    **Tool Controller**: définit le contrôleur d\'outil utilisé dans l\'opération.

-    **User Label**: étiquette attribuée par l\'utilisateur.


{{TitleProperty|Pocket}}

-    **Finition adaptative de poche**: utilise un algorithme adaptatif pour éliminer le fraisage excessif en l\'air sous le fond de la poche planaire.

-    **Adaptive Pocket Start**: utilise un algorithme adaptatif pour éliminer les fraisages excessifs au-dessus de la partie supérieure de la poche planaire.

-    **Cut Mode**: direction que la trajectoire de l\'outil doit prendre autour de la pièce : sens horaire (ClockWise = CW) ou anti sens horaire (CounterClockWise = CCW).

-    **Extra Offset**: décalage supplémentaire à appliquer à l\'opération. La direction dépend de l\'opération.

-    **Handle Multiple Features**: choisit comment traiter les caractéristiques multiples de la géométrie de base.

-    **Keep Tool Down**: tente d\'éviter les rétractions inutiles.

-    **Min Travel**: utilise le triage 3D de la trajectoire

-    **Process Stock Area**: traite le modèle et le stock dans une opération sans géométrie de base sélectionnée.

-    **Start At**: commence la fonction poche au centre ou à la limite

-    **Step Over**: pourcentage du diamètre de l\'outil à passer à chaque passe

-    **Zig Zag Angle**: angle du motif en zigzag


{{TitleProperty|Rotation}}

Remarque : la rotation n\'est pas disponible pour 3D Pocket à partir de la version 0.19.

-    **Enable Rotation**: active la rotation pour accéder aux poches ou aux zones non normales à l\'axe Z.


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

-    **Use Start Point**: mis à True, si vous spécifiez manuellement un point de départ. Définir le point de départ dans le champ Start Point des propriétés de données.



### Vue

Vide



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Exemple :


```python
#Place code example here.
```





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Pocket 3D/fr
