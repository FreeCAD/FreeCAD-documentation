---
 GuiCommand:
   Name: Assembly CreateView
   Name/fr: Assembly Vue éclatée
   MenuLocation: Assemblage , Créer une vue éclatée
   Workbenches: Assembly_Workbench/fr
   Shortcut: **V**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateView/fr

## Description

L\'outil <img alt="" src=images/Assembly_CreateView.svg  style="width:24px;"> [Assembly Vue éclatée](Assembly_CreateView/fr.md) crée un conteneur de vues éclatées (objet Exploded_Views) dans l\'assemblage actif qui contient une (par défaut) ou plusieurs vues éclatées (objets Exploded_View). Un assemblage ne peut contenir qu\'un seul conteneur de vues éclatées.

Une vue éclatée rassemble les déplacements (objets Move) utilisés pour déplacer les pièces de la position assemblée à la position éclatée. Les positions modifiées des pièces assemblées et les représentations des déplacements ne sont visibles que lorsqu\'une vue éclatée est éditée et dans les vues TechDraw dérivées d\'une vue éclatée.



## Utilisation

1.  Assurez-vous qu\'un assemblage est actif.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Assembly_CreateView.svg" width=16px> [Créer une vue éclatée](Assembly_CreateView/fr.md)**.
    -   Sélectionnez l\'option **Assemblage → <img src="images/Assembly_CreateView.svg" width=16px> Créer une vue éclatée** du menu.
    -   Utilisez le raccourci clavier : **E**.
3.  Si aucun objet Exploded_Views ne préexiste : un conteneur Exploded_Views est ajouté à l\'assemblage actif.
4.  Un objet Exploded_View est ajouté au conteneur Exploded_Views.
5.  La fenêtre de dialogue **Créer une vue éclatée** s\'ouvre dans le [panneau des tâches](Task_panel/fr.md).
6.  Vous pouvez cocher la case **Pièces comme un seul solide** pour\...
7.  Vous pouvez choisir une façon d\'ajouter un déplacement :
    -   Éclatez radialement :
        1.  Appuyez sur **Éclater radialement**
        2.  Toutes les pièces sont sélectionnées et un dragueur apparaît (voir [Remarques](##Remarques.md)).
        3.  Vous pouvez réaligner le manipulateur en sélectionnant une option dans la liste déroulante *\'Aligner le manipulateur sur\...*.
            -   Aligner sur\...
                1.  Sélectionnez une arête ou une face de n\'importe quelle pièce pour aligner le manipulateur.
            -   Alignez sur le centre de la pièce.
                1.  Le manipulateur est aligné sur le centre de la pièce bloquée.
            -   Alignez sur l\'origine de la pièce.
                1.  Le manipulateur est aligné sur l\'origine de la pièce bloquée.
        4.  Déplacez le manipulateur en utilisant une ou plusieurs des options suivantes (seul le décalage par rapport au point de départ compte, la direction de chaque pièce est calculée séparément) :
            -   Appuyez et maintenez le bouton gauche de la souris sur une flèche d\'axe et faites glisser pour déplacer l\'objet le long de cet axe.
            -   Appuyez sur le bouton gauche de la souris et maintenez-le enfoncé sur un plan, puis faites glisser l\'objet pour le déplacer le long de ce plan.
            -   Appuyez et maintenez le bouton gauche de la souris sur une sphère et faites glisser l\'objet pour le faire pivoter autour de cet axe.
        5.  Un mouvement (voir [Remarques](##Remarques.md)) est ajouté une fois que le bouton gauche de la souris est relâché.
    -   Éclatez en suivant des mouvements séparés :
        1.  Sélectionnez une ou plusieurs pièces.
        2.  Un manipulateur apparaît.
        3.  Vous pouvez réaligner le manipulateur (voir ci-dessus).
        4.  Déplacez le manipulateur comme décrit ci-dessus (les directions selon les poignées du manipulateur sont prises en compte).
        5.  Un déplacement est ajouté une fois que le bouton gauche de la souris est relâché.
        6.  Vous pouvez pouvez sélectionner/désélectionner des pièces et/ou répéter le déplacement pour ajouter d\'autres déplacements.
8.  Faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **OK** pour confirmer et fermer l\'outil.
    -   Appuyez sur le bouton **Annuler** pour annuler tous les changements et fermer l\'outil.
9.  Toutes les pièces sont replacées dans leur position d\'assemblage et les lignes de connexion sont masquées.



## Remarques

-   Le manipulateur est un outil similaire au manipulateur de transformation (<img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std Transformer](Std_TransformManip/fr.md)) mais sans le panneau des tâches **Incréments**.
-   Un objet Move dans la [vue en arborescence](Tree_view/fr.md) est représenté dans la [vue 3D](3D_view/fr.md) par une ligne rouge en pointillés pour chaque pièce impliquée dans ce déplacement. Ces lignes de connexion ne sont visibles que lorsque cet outil est en cours d\'exécution, ou dans une vue TechDraw dérivée d\'un objet Exploded_View.
-   Pour ajouter une vue éclatée à une page TechDraw : passez à l\'atelier TechDraw, ajoutez une page, sélectionnez l\'objet vue éclatée dans l\'arborescence et cliquez sur [TechDraw Insérer une vue](TechDraw_View/fr.md).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Les conteneurs Exploded_Views sont des objets {{Incode|Assembly::ViewGroup}}. Les objets Exploded_View sont dérivés de la classe {{Incode|ExplodedView}} et les objets Move de la classe {{Incode|ExplodedViewStep}}.

### Assembly::ViewGroup



#### Données


{{TitleProperty|Base}}

-    **Label|String**:

-    **Label2|String|Hidden**:

-    **Expression Engine|ExpressionEngine|Hidden**:

-    **Visibility|Bool|Hidden**:

-    **Group|LinkList**:

-    **_ Group Touched|Bool|Hidden**:



#### Vue


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**:

-    **Show In Tree|Bool**:

-    **Visibility|Bool**:


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**:

-    **Selection Style|Enumeration**:

### ExplodedView

Un objet **ExplodedView** est dérivé d\'un [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



#### Données 


{{TitleProperty|Exploded View}}

-    **Moves|LinkList**: liste des objets Move de la vue éclatée.

### ExplodedViewStep

Un objet **ExplodedViewStep** est dérivé d\'un [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



#### Données 


{{TitleProperty|Exploded Move}}

-    **Move Type|Enumeration**: type de mouvement. ({{Value|Normal}}, {{Value|Radial}}).

-    **Movement Transform|Placement**: déplacement du mouvement.

    :   L\'emplacement final est le résultat du placement initial \* cet emplacement.

-    **Obj Names|StringList**: objets déplacés par le mouvement.

-    **Parts|LinkList**: parties contenant les objets déplacés par le mouvement.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateView/fr
