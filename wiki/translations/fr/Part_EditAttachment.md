---
 GuiCommand:
   Name: Part EditAttachment
   Name/fr: Part Ancrage
   MenuLocation: Part , Ancrer...
   Workbenches: Part_Workbench/fr, PartDesign_Workbench/fr
   Version: 0.17
   SeeAlso: Placement/fr, Basic_Attachment_Tutorial/fr
---

# Part EditAttachment/fr

## Description

La commande <img alt="" src=images/Part_EditAttachment.svg  style="width:24px;"> **Part Ancrage** ancre un objet à un ou plusieurs autres objets. L\'objet ancré est lié à l\'objet ou aux objets référencés, ce qui signifie que si le [placement](Std_Placement/fr.md) ou la géométrie de l\'objet ou des objets référencés est modifié, le placement de l\'objet ancré sera mis à jour si nécessaire.



## Dispositifs d\'ancrage 

L\'ancrage d\'un objet est contrôlé par l\'un des quatre dispositifs d\'ancrage. Le dispositif par défaut utilisé pour un objet dépend de son type. Le dispositif d\'ancrage d\'un objet peut être modifié via sa propriété **Attacher Engine** ({{Version/fr|1.0}}) ou sa propriété [cachée](Property_editor/fr#Menu_contextuel.md) **Attacher Type**.

Les dispositifs disponibles sont énumérés dans le tableau ci-dessous. Les dispositifs d\'ancrage contrôlent les **Placement** des objets. Tous les dispositifs peuvent être utilisés pour tous les objets ayant cette propriété. Toutefois, les résultats des trois derniers dispositifs sont plus pertinents si la forme de l\'objet correspond à la \"forme logique\" mentionnée.

  Dispositif d\'ancrage                              Type d\'ancrage               Forme logique
    
  [Dispositif 3D](#Dispositif_3D.md)         Attacher::AttachEngine3D      
  [Dispositif plan](#Dispositif_plan.md)     Attacher::AttachEnginePlane   Face plane coïncidant avec le plan XY du placement
  [Dispositif ligne](#Dispositif_ligne.md)   Attacher::AttachEngineLine    Arête droite colinéaire à l\'axe Z du placement
  [Dispositif point](#Dispositif_point.md)   Attacher::AttachEnginePoint   Sommet coïncidant avec l\'origine du placement

Le reste de cette page est consacré au dispositif 3D. Les modes des autres dispositifs sont seulement listés. Notez que les modes du dispositif plan sont en fait identiques à ceux du dispositif 3D.



## Utilisation

1.  Sélectionnez l\'objet à ancrer.
2.  Faites l\'une des choses suivantes :
    -   Si l\'objet possède déjà une propriété **Map Mode** : cliquez dans ce champ dans l\'éditeur de propriétés et appuyez sur le bouton **...** qui apparaît.
    -   Sélectionnez l\'option **Part → <img src="images/Part_EditAttachment.svg" width=16px> Ancrer...** du menu.
3.  Le panneau des tâches **Ancrage** s\'ouvre.
4.  En haut du panneau des tâches, on peut lire *Non ancré*. Le premier bouton intitulé **Sélection de...** est mis en évidence pour indiquer qu\'une sélection dans la [vue 3D](3D_view/fr.md) est attendue.
5.  Sélectionnez un sommet, une arête ou une face/un plan appartenant à un autre objet.
6.  Dans le champ de saisie situé à droite du bouton, l\'objet et le sous-élément référencés sont affichés. Par exemple, si une face d\'un [Part Cube](Part_Box/fr.md) est sélectionnée, le champ peut afficher {{Value|Box:Face6}}. L\'étiquette du bouton affiche maintenant le type de sous-élément.
7.  Les modes disponibles sont filtrés en fonction des références sélectionnées et de leur ordre. Par exemple, pour les modes [Alignement O-Z-X](#Alignement_O-Z-X.md) à [Alignement O-Y-X](#Alignement_O-Y-X.md), la première référence doit être un sommet. Si la première référence est un sous-élément d\'un type différent, elle est supprimée de la liste.
8.  *Ancré avec le mode * est maintenant affiché en haut du panneau des tâches.
9.  Vous pouvez également sélectionner un autre [mode d\'ancrage](#Mode_d'ancrage.md) dans la liste. Pour plus d\'informations sur les modes d\'ancrage, passez la souris dessus pour faire apparaître une infobulle.
10. Selon le mode sélectionné, ajoutez jusqu\'à trois références supplémentaires en appuyant sur les boutons **Référence2**, **Référence3** et **Référence4** et en répétant l\'étape 5. Il est également possible de spécifier toutes les références avant de sélectionner un mode d\'attachement.
11. Vous pouvez également définir un [décalage de la pièce ancrée](#D.C3.A9calage_de_l.27ancrage.md).
12. Appuyez sur **OK**.
13. Le cas échéant, vous pouvez modifier la propriété **Map Path Parameter** dans l\'[éditeur de propriétés](Property_editor/fr.md).



## Modes d\'ancrage 



### Dispositif 3D 

<img alt="" src=images/Part_Offset_Tasks.png  style="width:250px;">



#### Désactivé

L\'ancrage est désactivé. L\'objet peut être déplacé en modifiant sa propriété [Placement](Placement/fr.md).



#### Translation de l\'origine 

L\'origine est associée à un sommet. L\'orientation est toujours contrôlée par la propriété Placement de l\'objet ancré.

:; Combinaisons de référence :

:   sommet.



#### X Y Z de l\'objet 

Le placement est égal au placement d\'un objet lié.

:; Combinaisons de références :

:   Tout
:   Conique



#### X Z Y de l\'objet 

Les axes X, Y et Z sont mis en correspondance avec les axes locaux X, Z et Y d\'un objet lié, respectivement.

:; Combinaisons de références :

:   Tout
:   Conique



#### Y Z X de l\'objet 

Les axes X, Y et Z sont mis en correspondance avec les axes locaux Y, Z et X d\'un objet lié, respectivement.

:; Combinaisons de références :

:   Tout
:   Conique



#### Plan XY sur un plan 

Le plan XY est aligné de manière à coïncider avec une face plane.

:; Combinaisons de référence :

:   plan.



#### Plan XY tangent à une surface 

Le plan XY est rendu tangent à une face au niveau d\'un sommet.

:; Combinaisons de références :

:   face, sommet
:   sommet, face



#### Axe Z tangent à une arête 

L\'axe Z est aligné de manière à être tangent à une arête. Un sommet supplémentaire permet de définir l\'emplacement de l\'arête.

Si aucun sommet n\'est lié, la propriété **Map Path Parameter** détermine le point.

:; Combinaisons de référence:

:   arête
:   arête, sommet
:   sommet, arête



#### Axes normaux-binormaux de Frenet 

<img alt="" src=images/Attacher_mode_FrenetNB.png  style="width:250px;">

Les axes X et Y sont alignés sur les axes normal (N) et binormal (B) du [Système de Coordonnées Frenet-Serret](https://fr.wikipedia.org/wiki/Rep%C3%A8re_de_Frenet) en un point situé sur un bord incurvé. Un sommet supplémentaire permet de définir où.

Si aucun sommet n\'est lié, la propriété **Map Path Parameter** détermine le point. L\'origine de l\'objet est déplacée vers le sommet si le sommet est le premier, ou maintenue sur la courbe si la courbe est la première.

*Axes normaux-binormaux de Frenet* est similaire à *Axe Z tangent à une arête* sauf que l\'axe X est bien défini.

:;Combinaisons de références :

:   courbe
:   courbe, sommet
:   sommet, courbe



#### Axes tangents-normaux de Frenet 

<img alt="" src=images/Attacher_mode_FrenetTN.png  style="width:250px;">

Les axes X et Y sont alignés sur les axes tangents (T) et normaux (N) du système de coordonnées Frenet-Serret en un point situé sur un bord incurvé. Un sommet supplémentaire permet de définir où.

Voir [Axes normaux-binormaux de Frenet](#Axes_normaux-binormaux_de_Frenet.md).



#### Axes tangents-binormaux de Frenet 

<img alt="" src=images/Attacher_mode_FrenetTB.png  style="width:250px;">

Les axes X et Y sont alignés sur les axes tangents (T) et binormaux (B) du système de coordonnées Frenet-Serret en un point situé sur un bord incurvé. Un sommet supplémentaire permet de définir où.

Voir [Axes normaux-binormaux de Frenet](#Axes_normaux-binormaux_de_Frenet.md).



#### Concentrique

Le plan XY est aligné sur le [cercle osculateur](https://fr.wikipedia.org/wiki/Cercle_osculateur) en un point situé sur une arête. Un sommet supplémentaire permet de définir où.

Si aucun sommet n\'est lié, la propriété **Map Path Parameter** détermine le point.

:; Combinaisons de références :

:   courbe
:   cercle
:   courbe, sommet
:   cercle, sommet
:   sommet, courbe
:   sommet, cercle



#### Section de révolution 

L\'axe Y est aligné sur l\'axe du cercle osculateur en un point d\'une arête. Un sommet supplémentaire permet de définir où.

Voir [Concentrique](#Concentrique.md).



#### Plan XY par 3 points 

Le plan XY est aligné de manière à passer par trois sommets. L\'axe X passera par les deux premiers sommets.

:; Combinaisons de références :

:   sommet, sommet, sommet
:   droite, sommet
:   sommet, droite
:   droite, droite



#### Plan XZ par 3 points 

Le plan XZ est aligné de manière à passer par trois sommets. L\'axe X passe par les deux premiers sommets.

Voir [Plan XY par 3 points](#Plan_XY_par_3_points.md).



#### Pliage

<img alt="" src=images/Attacher_mode_Folding.png  style="width:250px;">

Il s\'agit d\'un mode spécial de pliage des polyèdres. Sélectionnez quatre lignes ayant un point commun dans l\'ordre suivant : ligne de contour (1), ligne de pliage (2), autre ligne de pliage (3), autre ligne de contour (4). Pour déterminer le système de coordonnées, on fait coïncider les lignes de contour sélectionnées en faisant tourner la ligne 1 autour de la ligne 2 et la ligne 4 autour de la ligne 3. L\'origine correspond au point commun, l\'axe X correspond à la ligne 2, l\'axe Y est aligné sur la direction des lignes de contour coïncidentes.

:; Combinaisons de références

:   ligne, ligne, ligne, ligne



#### Inertie CS 

Les axes X, Y et Z correspondent à ceux d\'un système de coordonnées inertielles, construit sur les axes principaux d\'inertie et le centre de masse.

:; Combinaisons de références :

:   Tout
:   Tout, Tout
:   Tout, Tout, Tout
:   Tout, Tout, Tout, Tout



#### Alignement O-Z-X 

L\'origine correspond au premier sommet. Les axes Z et X sont alignés vers un sommet ou le long d\'une ligne.

Voir [Modes d\'ancrage de type O-X-Y](O-X-Y_Type_Attachment_Modes/fr.md) pour plus de détails.

:; Combinaisons de références :

:   sommet, sommet, ligne
:   sommet, ligne, arête
:   sommet, ligne, ligne
:   sommet, arête, arête
:   sommet, sommet
:   sommet, ligne



#### Alignement O-Z-Y 

L\'origine correspond au premier sommet. Les axes Z et Y sont alignés vers un sommet ou le long d\'une ligne.

Voir [Alignement O-Z-X](#Alignement_O-Z-X.md).



#### Alignement O-X-Y 

L\'origine correspond au premier sommet. Les axes X et Y sont alignés vers un sommet ou le long d\'une ligne.

Voir [Alignement O-Z-X](#Alignement_O-Z-X.md).



#### Alignement O-X-Z 

L\'origine correspond au premier sommet. Les axes X et Z sont alignés vers un sommet ou le long d\'une ligne.

Voir [Alignement O-Z-X](#Alignement_O-Z-X.md).



#### Alignement O-Y-Z 

L\'origine correspond au premier sommet. Les axes Y et Z sont alignés vers un sommet ou le long d\'une ligne.

Voir [Alignement O-Z-X](#Alignement_O-Z-X.md).



#### Alignement O-Y-X 

L\'origine correspond au premier sommet. Les axes Y et X sont alignés vers un sommet ou le long d\'une ligne.

Voir [Alignement O-Z-X](#Alignement_O-Z-X.md).



#### XY parallèle au plan 


{{Version/fr|1.0}}

Le plan XY est aligné de manière à être parallèle au plan XY du placement d\'un objet lié et à passer par un sommet. L\'origine correspond à la projection de l\'origine de l\'objet lié sur le plan XY.

Remarquez que vous devez sélectionner un objet entier et non un sous-élément tel qu\'une face ou un plan.

:   ; Combinaisons de référence :
:   Tout objet entier (avec une propriété **Placement**), sommet


<div class="toccolours mw-collapsible mw-collapsed">



### Dispositif plan 


<div class="mw-collapsible-content">

-   Désactivé
-   Origine de la translation
-   XY de l\'objet
-   XZ de l\'objet
-   YZ de l\'objet
-   Face plane
-   Tangente à la surface
-   Normal à l\'arête
-   Frenet NB
-   Frenet TN
-   Frenet TB
-   Concentrique
-   Section révolutionnaire
-   Plan de 3 points
-   Normal à 3 points
-   Pliage
-   Inertie 2-3
-   Alignement O-N-X
-   Alignement O-N-Y
-   Alignement O-X-Y
-   Aligner O-X-N
-   Aligner O-Y-N
-   Aligner O-Y-X
-   XY parallèle au plan {{Version/fr|1.0}}


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### Dispositif ligne 


<div class="mw-collapsible-content">

-   Désactivé
-   X de l\'objet
-   Y de l\'objet
-   Z de l\'objet
-   Axe de courbure
-   Directrice1
-   Directrice2
-   Asymptote1
-   Asymptote2
-   Tangente
-   Normal à l\'arête
-   Binormale
-   Par deux points
-   Ligne de proximité
-   Intersection {{Version/fr|1.0}}
-   1er axe principal
-   2ème axe principal
-   3ème axe principal
-   Normal à la surface


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### Dispositif point 


<div class="mw-collapsible-content">

-   Désactivé
-   Origine de l\'objet
-   Foyer1
-   Foyer2
-   Sur l\'arête
-   Centre de courbure
-   Centre de masse
-   Vertex
-   Point de proximité 1
-   Point de proximité 2


</div>


</div>



## Décalage de l\'ancrage 

Le décalage de l\'ancrage devient actif lorsqu\'un mode d\'ancrage autre que*Désactivé* a été sélectionné. Il permet d\'appliquer un décalage linéaire ou rotatif dans le système de coordonnées de l\'ancrage (attachment coordinate system = ACS), tel que défini par le mode d\'ancrage et le(s) objet(s) référencé(s).

-   **Dans la direction X** : définit une distance de décalage le long de l\'axe X de l\'ACS.

-   **Dans la direction Y** : définit une distance de décalage le long de l\'axe Y de l\'ACS.

-   **Dans la direction Z** : définit une distance de décalage le long de l\'axe Z de l\'ACS.

-   **Autour de l\'axe X** : fait tourner l\'objet ancré autour de l\'axe X de l\'ACS.

-   **Autour de l\'axe Y** : fait tourner l\'objet ancré autour de l\'axe Y de l\'ACS.

-   **Autour de l\'axe Z** : fait tourner l\'objet ancré autour de l\'axe Z de l\'ACS.

-   **Inverser les côtés** : si la case est cochée, l\'ancrage est inversé. Cela équivaut à faire pivoter l\'objet de 180° autour de l\'axe Y de l\'ACS.

## Limitations

-   Si la sélection de deux lignes entraîne une erreur : \"Points are collinear. Can\'t make a plane\", essayez de sélectionner trois sommets à la place [1](https://forum.freecadweb.org/viewtopic.php?f=8&t=55088&p=473614#p473594).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part EditAttachment/fr
