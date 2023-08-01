---
- GuiCommand:/fr
   Name:Path 3DSurface
   Name/fr:Path Surface
   MenuLocation:Path → Surface
   Workbenches:[Path](Path_Workbench/fr.md)
   Version:0.19
---

# Path Surface/fr

## Description

Cet outil crée une nouvelle opération de <img alt="" src=images/Path_Surface.svg  style="width:24px;"> [Surface](Path_Surface/fr.md), capable de générer des trajectoires G-code pour toute la surface supérieure d\'un modèle 3D (ou capable de travailler avec des faces sélectionnées) et permet d\'éviter des faces. Cette opération offre plusieurs motifs de coupe: ligne, zigzag, circulaire, zigzag circulaire, décalage et spirale (similaire à un motif adaptatif). Depuis la version 0.19, cette opération propose de nombreuses personnalisations pour permettre une plus grande productivité.

L\'opération <img alt="" src=images/Path_Surface.svg  style="width:24px;"> [Surface](Path_Surface/fr.md) est également capable de générer des parcours de surfaçage 3D de base. Les capacités de rotation sont limitées à l\'ensemble du modèle et ne permettent pas d\'isoler des faces ou des régions spécifiques. Les parcours rotatifs sont également limités aux motifs de coupe de lignes.

L\'outil 3D Surface s\'interface avec OCL.pyd, un module Open Source tiers intitulé [OpenCamLib](OpenCamLib/fr.md) qui génère des chemins d\'outil à partir d\'un modèle 3D. OpenCamLib n\'est pas directement intégré à FreeCAD.

**Remarque:** pour utiliser l\'opération Surface 3D, vous devez:

1.  Installer correctement [OpenCamLib](OpenCamLib/fr.md).
2.  Activez [Fonctions expérimentales](Path_experimental/fr.md) de l\'atelier Path.
3.  Vérifiez **Édition → Préférences... → Path → Advanced → Enable OCL dependent features**.



## Utilisation

Les instructions d\'utilisation pour plusieurs variantes de [Surface](Path_Surface/fr.md) sont présentées ici.



#### Opération de base 

1.  Appuyez sur l\'icône **<img src="images/Path_Surface.svg" width=24px> [Surface](Path_Surface/fr.md)** ou sélectionnez **Path → Surface** dans le menu déroulant.
2.  Sélectionnez le contrôleur d\'outil pour l\'opération dans la fenêtre contextuelle de la boîte de dialogue Contrôleur d\'outil, le cas échéant.
3.  Dans l\'onglet Géométrie de base, sélectionnez les faces spécifiques sur lesquelles vous souhaitez vous concentrer et/ou éviter pour l\'opération.
4.  Ajustez les profondeurs d\'opération selon vos besoins dans l\'onglet Profondeurs: Profondeur de départ, Profondeur de finition, Descente.
5.  Faites des ajustements dans l\'onglet Hauteurs si nécessaire.
6.  Configurez les paramètres dans l\'onglet Opérations si nécessaire:
    -   Choisissez votre mode de refroidissement.
    -   Choisissez la boîte de délimitation: Brut ou Boîte de délimitation de base
    -   Définissez le type de scan pour l\'opération: planaire ou rotationnel
    -   Sélectionnez le mode de calque pour l\'opération: passe unique ou passe multiple
        1.  Un seul passage est pour une passe finale
        2.  Multi-pass peut être utilisé pour le dégagement en combinaison avec l\'utilisation du décalage de profondeur pour laisser une couche de surface mince pour une passe de finition
    -   Ajoutez un décalage supplémentaire à la boîte de délimitation en X et Y comme vous le souhaitez (*Scans rotatifs uniquement*)
    -   Réglez la direction du Drop Cutter: X ou Y. Il s\'agit de la direction linéaire dans laquelle la fraise (broche) se déplacera. (*Scans rotatifs uniquement*)
    -   Ajoutez une valeur de décalage de profondeur si vous souhaitez laisser une épaisseur de matériau spécifiée sur la surface, par exemple une passe de finition finale
    -   Définissez l\'intervalle d\'échantillonnage utilisé pour l\'analyse OCL.
    -   Définissez la valeur Step Over en pourcentage du diamètre de l\'outil.
    -   Cochez la case Utiliser le point de départ si vous souhaitez fournir un point de départ pour l\'opération dans la vue des propriétés de l\'onglet de données de l\'opération.
    -   L\'application des limites est activée par défaut. Cela force l\'outil de coupe à rester à l\'intérieur des limites de la géométrie de l\'entité pour l\'opération, comme une opération d\'empoquetage. Désactivez cette option pour permettre au couteau de s\'étendre vers l\'extérieur de la géométrie de l\'entité. La propriété Ajustement des limites remplace cette propriété.
    -   L\'optimisation des trajectoires linéaires est activée par défaut. La désactivation donnera un résultat gcode plus long et augmentera probablement le temps de découpe.
7.  Si vous souhaitez prévisualiser le résultat avant d\'accepter les paramètres, cliquez sur **Appliquer**
8.  Cliquez sur le bouton **OK** pour confirmer et générer des chemins.

Pour obtenir des effets différents ou plus complexes, définissez des propriétés d\'opération supplémentaires dans l\'onglet Données de la vue Propriétés pour l\'opération.



#### Scans rotationnels (4ème axe) 

1.  Lancez une [Opération de base](#Op.C3.A9ration_de_base.md) comme décrit ci-dessus et définissez le **Type de scan** à **Rotationel**.
2.  **Remarque:** La sélection de face n\'est pas disponible pour les scans rotationnels, les modifications apportées à la géométrie de base sont donc ignorées.
3.  Localisez l\'onglet Données et la vue Propriétés pour la nouvelle opération [Parcours](Path_Surface/fr.md). Une section **Rotation** devrait être disponible avec des propriétés supplémentaires à ajuster, listées ci-dessous.
    Il est recommandé de définir toutes les propriétés de rotation souhaitées en une seule fois avant de recalculer. Pour ce faire, cliquez sur la touche ENTRÉE immédiatement après avoir modifié un paramètre de propriété. Ce processus vous permettra de modifier et d\'enregistrer plusieurs propriétés avant de recalculer l\'opération.
4.  Ajustez les paramètres suivants selon vos besoins:
    -   Définissez **Cutter Tilt** sur l\'index de décalage (angle) \[0-90\]. (Utilisé pour les fraises hémisphériques)
    -   Remplacez **Drop Cutter Dir** par l\'axe de déplacement de la fraise (broche).
    -   Modifiez **Drop Cutter Extra Offset** pour étendre la boîte de délimitation dans les directions X et Y.
    -   Définissez **Rotation Axis** sur l\'axe souhaité.
    -   Ajustez **Start Index** pour démarrer l\'index (angle) \[0-360\].
    -   Ajustez **Stop Index** pour arrêter l\'index (angle) \[0-360\].
5.  Cliquez sur l\'icône **[<img src=images/_View-refresh.svg style="width:16px"> [Rafraîchir](Std_Refresh/fr.md)** dans la barre d\'outils.
6.  Attendez les résultats \...



##### Remarques sur les scans rotationnels 

-   Les balayages **Rotationnels** nécessitent beaucoup plus de temps et de traitement que les balayages **Planaires**. Les facteurs ayant une incidence sur le temps de traitement comprennent: l\'intervalle d\'échantillonnage, l\'interpolation, le diamètre de l\'outil et la taille du modèle. Encore une fois, les analyses en rotation peuvent prendre beaucoup de temps. Certains peuvent prendre 3, 5 ou 10 minutes ou plus.
-   Pour des raisons de temps, il est préférable de ne pas recalculer un balayage rotationnel après chaque changement de propriété. Considérez plutôt l'un des éléments suivants :
    -   utilisez la technique **pour modifier tous les paramètres avec la touche ENTREE** mentionnée à l\'étape 2 ci-dessus puis l\'opération **[<img src=images/View-refresh.svg style="width:16px"> [Rafraîchir](Std_Refresh/fr.md)**.
    -   désactiver l\'opération avec l\'outil **<img src="images/Path_OpActiveToggle.svg" width=16px> [Activer une opération](Path_OpActiveToggle/fr.md)**, apportez vos modifications aux propriétés de l\'opération, puis cliquez sur le **<img src="images/Path_OpActiveToggle.svg" width=16px> [Activer une opération](Path_OpActiveToggle/fr.md)** à nouveau pour réactiver l\'opération, ce qui déclenche un recalcul en interne.
-   L\'opération **<img src="images/Path_Surface.svg" width=16px> [Surface](Path_Surface/fr.md)** est toujours considérée comme une \"fonctionnalité expérimentale\" au 25/06/2019. En tant que tel, elle peut contenir quelques bugs qui doivent encore être clairement identifiés. Veuillez signaler les bogues et les problèmes sur le [FreeCAD Path/CAM Forum](https://forum.freecadweb.org/viewforum.php?f=15).
-   Le **<img src="images/Path_Simulator.svg" width=16px> [Path Simulateur FAO](Path_Simulator/fr.md)** intégré ne prend pas en charge la simulation du 4ème axe. Vous devrez utiliser un simulateur tiers pour inspecter ou vérifier visuellement les parcours. Voir la section [Ressources](#Ressources.md) ci-dessous pour des suggestions.
-   Vous verrez probablement des lignes de rotation rouges autour de votre modèle dans la fenêtre. C\'est normal dans FreeCAD pour le moment.



##### Remarques sur les scans de modèles complexes 

Des temps de traitement excessivement longs (plus de 10 minutes) peuvent se produire lors du traitement de grands modèles complexes. En plus des facteurs déjà mentionnés, les étapes suivantes peuvent aider à identifier les causes et les solutions potentielles.

**\'\'Mémoire insuffisante**\'\'
Vérifiez la quantité de mémoire disponible pendant l\'exécution du scan à l\'aide d\'un outil tel que le **Gestionnaire des tâches, onglet Mémoire** de Windows. Si plus de 90 % de la mémoire est constamment utilisée, alors un petit paramètre **Déflexion linéaire** pourrait générer un maillage trop important pour la mémoire disponible.
Pour confirmer cela \...

1.  Créez une nouvelle **<img src="images/Path_Surface.svg" width=24px> [Surface](Path_Surface/fr.md)** opération.
2.  Passez à l\'onglet Modèle et augmentez la valeur de **Linear Deflection**. Par exemple, passez de 2,5 um à 20 um.
3.  Revenez à l\'onglet Tâches pour terminer la configuration de l\'opération.
4.  Cliquez sur le bouton **OK** pour confirmer et générer les trajectoires.

Pour faire de cette valeur la valeur par défaut pour toutes les nouvelles **<img src="images/Path_Surface.svg" width=24px> [Surface](Path_Surface/fr.md)** opérations, modifiez le paramètre **GeometryTolerance**.
**Outils → Editer paramètres... → Préférences → Mod → Path → GeometryTolerance **.
Notez qu\'à partir de la version 0.19, la **Linear Deflection** par défaut = GeometryTolerance / 4.

**\'\'Géométrie non valide**\'\'
Si un modèle contient une géométrie invalide, le temps de numérisation peut augmenter considérablement. Un modèle peut être vérifié à l\'aide de la fonction [Part Vérifier la géométrie](Part_CheckGeometry/fr.md) dans l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;">**atelier Part**.
Pour exécuter l\'outil :

1.  Passez dans l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;">**atelier Part** et sélectionnez le modèle à vérifier.
2.  Cliquez sur le bouton **<img src="images/Part_CheckGeometry.svg" width=16px> [Part Vérifier la géométrie](Part_CheckGeometry/fr.md)** disponible dans la barre d\'outils de l\'atelier de pièce OU utilisez l\'entrée **Pièce → <img src="images/Part_CheckGeometry.svg" width=16px> Vérifier la géométrie** dans le menu supérieur.
3.  Cliquez sur le bouton **Exécuter la vérification** et examinez les résultats.

Si les résultats comprennent des éléments comme *BOPAlgo SelfIntersect*, alors la géométrie n\'est pas valide et doit être corrigée en ajustant le modèle.
(Conseil : les opérations booléennes et les commandes Loft peuvent parfois introduire des *Self Intersections*)
.



#### Formes d\'outils (de coupe) disponibles 

Cette opération 3D Surface utilise actuellement [OpenCamLib](OpenCamLib/fr.md) pour extraire les trajectoires de la base de la pièce. En tant que tel, une traduction des paramètres de l\'outil est nécessaire entre le contrôleur d\'outil de FreeCAD et OCL afin de compléter le balayage avec la forme de votre outil (cutter).

Ces formes d'outils sont respectées et disponibles pour cette opération 3D Surface:

-   Fraise à queue
-   Fraise hémisphérique
-   Fraise à tête cylindrique
-   Fraise à chanfreiner
-   Graveur

Si vous choisissez d\'exécuter le simulateur de trajectoire dans l\'atelier Path, il utilise uniquement la fraise de bout standard pour simuler des trajectoires. Par conséquent, vous ne verrez pas l'enlèvement de matière spécifique à une forme d'outil. L\'enlèvement de matière est illustré à l\'aide de la forme de la fraise.

REMARQUE: à compter de mai 2019, seule la fraise en bout dispose d\'un type de test permettant de déterminer l\'exactitude de la traduction des paramètres de l\'outil FreeCAD-OCL. Veuillez poster tout commentaire concernant une utilisation autre que l'usine finale dans la section [Path/CAM](https://forum.freecadweb.org/viewforum.php?f=15) des forums FreeCAD.



## Propriétés: Version 0.19 

***Remarque***: toutes ces propriétés ne sont pas disponibles dans l\'éditeur de fenêtre de tâches. Certaines ne sont accessibles que dans l\'onglet Données du panneau Vue de propriétés pour cette opération.


{{TitleProperty|Base}}

Remarque: il est conseillé de ne pas modifier la propriété Placement des opérations de chemin. Déplacez ou faites pivoter le modèle de tâche de chemin selon vos besoins.

-    **Placement**: emplacement global \[position et rotation\] de l\'objet - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent).

    -   
        **Angle**
        
        : angle en degrés appliqué à la rotation de l\'objet autour de la valeur de la propriété Axis.

    -   
        **Axis**
        
        : axe (un ou plusieurs) autour duquel faire pivoter l\'objet, défini dans les sous-propriétés: X, Y, Z.

        -   
            **X**
            
            : valeur de l\'axe X.

        -   
            **Y**
            
            : valeur de l\'axe Y.

        -   
            **Z**
            
            : valeur de l\'axe Z.

    -   
        **Position**
        
        : position de l\'objet, définie dans les sous-propriétés: X, Y, Z - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent).

        -   
            **X**
            
            : valeur de distance X.

        -   
            **Y**
            
            : valeur de distance Y.

        -   
            **Z**
            
            : valeur de distance Z.

-    **Label**: nom de l\'objet fourni par l\'utilisateur (UTF-8).


{{TitleProperty|Clearing Options}}

-    **Bound Box**: si l\'opération est limitée par l\'objet stock ou par le cadre englobant de l\'objet de base

-    **Cut Mode**: la direction dans laquelle le parcours d\'outil doit aller autour de la pièce: Climb (sens horaire) ou Conventionnel (sens anti horaire)

-    **Cut Pattern**: motif d\'effacement à utiliser

-    **Cut Pattern Reversed**: inverser l\'ordre de coupe des trajectoires des recouvrement entre les passes. Pour les motifs de coupe circulaire, commencez par l\'extérieur et travaillez vers le centre

-    **Depth Offset**: décalage de l\'axe Z par rapport à la surface de l\'objet

-    **Layer Mode**: mode de complétion de l\'opération: simple ou multi-passes

-    **Pattern Center At**: choisir l\'emplacement du point central pour commencer le motif de coupe

-    **Pattern Center Custom**: définit le point de départ du motif de coupe

-    **Profile Edges**: permet de profiler des bords de la sélection. Les options suivantes sont disponibles (les images peuvent être vues dans ce message du forum : <https://forum.freecad.org/viewtopic.php?p=676452#p676452>) :

    -   
        **None**
        
        : ne pas créer de profil

    -   
        **Only**
        
        : ne crée qu\'un profil et aucune trajectoire interne

    -   
        **First**
        
        : commencer par le profil, puis le reste

    -   
        **Last**
        
        : commencer par le reste, puis le profil

-    **Sample Interval**: l\'intervalle d\'échantillonnage. Les petites valeurs entraînent de longs temps d\'attente

-    **Step Over**: pourcentage de dépassement du chemin de coupe-goutte


{{TitleProperty|Depth}}

-    **Clearance Height**: hauteur nécessaire pour éviter les pinces et les obstructions.

-    **Final Depth**: profondeur finale de l\'outil - valeur la plus basse de Z.

-    **Safe Height**: seuil supérieur duquel les mouvements rapides sont autorisés.

-    **Start Depth**: profondeur initiale de l\'outil - première profondeur de coupe en Z.

-    **Step Down**: abaissement incrémentiel de l\'outil.


{{TitleProperty|Mesh Conversion}}

-    **Angular Deflection**: des valeurs plus petites donnent un maillage plus fin et plus précis. Des valeurs plus petites augmentent beaucoup le temps de traitement

-    **Linear Deflection**: des valeurs plus petites donnent un maillage plus fin et plus précis. Des valeurs plus petites n\'augmentent pas beaucoup le temps de traitement mais peuvent augmenter la consommation de mémoire.


{{TitleProperty|Optimization}}

-    **Circular Use G2 G3**: convertit les arcs coplanaires en commandes gcode G2/G3 pour les modèles de coupe \"Circular\" et \"CircularZigZag\".

-    **Gap Sizes**: retour d\'information : trois plus petits écarts identifiés dans la géométrie du chemin

-    **Gap Threshold**: les intervalles d\'artefacts colinéaires et co-radiaux qui sont inférieurs à ce seuil sont fermés dans la trajectoire.

-    **Optimize Linear Paths**: active l\'optimisation des trajectoires linéaires (points colinéaires). Supprime les points colinéaires inutiles de la sortie G-Code

-    **Optimize Step Over Transitions**: permet une optimisation distincte des transitions entre chaque étape sur la trajectoire


{{TitleProperty|Path}}

-    **Active**: mettre à False pour empêcher l\'opération de générer du code.

-    **Base**: géométrie de base pour cette opération.

-    **Comment**: commentaire facultatif pour cette opération.

-    **Coolant Mode**: mode de refroidissement pour cette opération.

-    **Cycle Time**: estimation du temps de cycle pour cette opération.

-    **Tool Controller**: définit le contrôleur d\'outil utilisé dans l\'opération.

-    **User Label**: étiquette attribuée par l\'utilisateur.


{{TitleProperty|Rotation}}

-    **Cutter Tilt**: définit l\'angle d\'inclinaison de la fraise (broche).

-    **Drop Cutter Dir**: direction le long de laquelle les lignes de Dropcutter sont créées

-    **Drop Cutter Extra Offset**: décalage supplémentaire par rapport au cadre de sélection sélectionné - utilisez des sous-propriétés pour définir les valeurs

    -   
        **X**
        
        : valeur de distance X

    -   
        **Y**
        
        : valeur de distance Y

    -   
        **Z**
        
        : valeur de distance Z

-    **Rotation Axis**: définit l\'axe de rotation du modèle.

-    **Start Index**: index de départ (angle) pour la rotation

-    **Stop Index**: index d\'arrêt (angle) pour la rotation


{{TitleProperty|Selected Geometry Settings}}

-    **Avoid Last X Faces**: évite de couper les \"N\" dernières faces dans la liste Géométrie de base des faces sélectionnées

-    **Avoid Last X Internal Features**: ne pas couper les fonctionnalités internes sur les faces évitées

-    **Boundary Adjustment**: des valeurs positives poussent l\'outil de coupe vers ou au-delà de la limite. Les valeurs négatives éloignent la fraise de la limite

-    **Boundary Enforcement**: si true, l\'outil de découpe restera à l\'intérieur des limites du modèle ou des faces sélectionnées

-    **Handle Multiple Features**: choisissez comment traiter plusieurs entités de géométrie de base

-    **Internal Features Adjustment**: les valeurs positives poussent l\'outil de coupe vers ou dans l\'entité. Les valeurs négatives retirent l\'outil de coupe de la fonction

-    **Internal Features Cut**: coupe des zones de fonction internes dans une face sélectionnée plus grande


{{TitleProperty|Start Point}}

-    **Start Point**: point de départ personnalisé pour lE PARCOURS de cette opération, défini dans les sous-propriétés : X, Y, Z

    -   
        **X**
        
        : valeur de l\'axe X

    -   
        **Y**
        
        : valeur de l\'axe Y

    -   
        **Z**
        
        : valeur de l\'axe Z

-    **Use Start Point**: mis à True, si vous spécifiez un point de départ


{{TitleProperty|Surface}}

-    **Scan Type**: planaire : balayage surfacique plat et 3D. Rotationnel : balayage rotatif sur le 4ème axe.


{{TitleProperty|Waste}}

-    **Ignore Waste**: ignore les zones situées en dessous de la profondeur spécifiée.

-    **Ignore Waste Depth**: profondeur utilisée pour identifier les zones de déchets à ignorer.

-    **Release From Waste**: coupe les déchets jusqu\'à la profondeur sur le bord du modèle, ce qui libère le modèle.



## Editeur de la fenêtre des tâches 

*Les descriptions des paramètres sont fournies dans la liste des propriétés ci-dessus.*

Cette section est simplement une représentation des paramètres de l'éditeur de fenêtres pour l'opération.



### Localisation de la base 

-   **Sélection de géométrie de base à importer**: utilisez cette liste pour sélectionner la géométrie de base à importer à partir de l\'opération existante sélectionnée
-   **Importer**: importe la géométrie de base de l\'opération sélectionnée dans la liste des géométries de base des opérations courantes
-   **Liste des géométries de base pour l\'opération en cours**: liste des géométries de base pour l\'opération en cours, le cas échéant
-   **Ajouter**: ajoute le ou les éléments sélectionnés qui devraient être la (les) base(s) du (des) parcours
-   **Supprimer**: supprimez les éléments sélectionnés dans la liste Base Location
-   **Editer**: efface tous les éléments de la liste Base Location



### Profondeur

-    **Start Depth**
    

-    **Final Depth**
    

-    **Step Down**
    



### Hauteur

-    **Safe Height**
    

-    **Clearance Height**
    



### Opération

-    **Tool Controller**
    

-    **Coolant Mode**
    

-    **BoundBox**
    

-    **Scan Type**
    

-    **Layer Mode**
    

-    **BoundBox extra offset X**
    

-    **BoundBox extra offset Y**
    

-    **Drop Cutter Direction**
    

-    **Depth Offset**
    

-    **Step Over**
    

-    **Sample Interval**
    

-    **Optimize Output Enabled**
    

-    **Use Start Point**
    

-    **Boundary Enforcement**
    

-    **Optimize Linear Paths**
    



## Ressources

-   Simulateur G-code(tracé): [NCViewer](https://ncviewer.com/)
-   Simulateur G-code(tracé): [CAMotics](https://www.camotics.org/)





{{Path Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Surface/fr
