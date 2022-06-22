---
- GuiCommand   */fr
   Name   *PartDesign Thickness
   Name/fr   *PartDesign Coque
   MenuLocation   *Part Design → Appliquer une fonction d'habillage → Coque
   Workbenches   *[PartDesign](PartDesign_Workbench/fr.md)
   Version   *0.17
   SeeAlso   *[Part Évidement](Part_Thickness/fr.md)
---

# PartDesign Thickness/fr

## Description

L\'outil <img alt="" src=images/PartDesign_Thickness.svg  style="width   *24px;"> **PartDesign Coque** transforme un corps solide en un objet creux avec au moins une face ouverte, en donnant à chacune de ses faces restantes une épaisseur uniforme. Il ajoute un objet **Thickness** au document avec sa représentation correspondante dans le [Vue en arborescence](Tree_view/fr.md).

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width   *600px;"> 
*Solide de base (A) → Solide avec la face sélectionnée à ouvrir (B) → Objet creux résultant (C)*

## Utilisation

### Ajouter une coque 

1.  Vous pouvez accessoirement [activé](PartDesign_Body/fr#Statut_actif.md) le corps auquel appliquer la coque.
2.  Sélectionnez une ou plusieurs faces du corps.
3.  Il existe plusieurs façons de lancer l\'outil    *
    -   Appuyez sur le bouton **<img src="images/PartDesign_Thickness.svg" width=16px> [Coque](PartDesign_Thickness/fr.md)**.
    -   Sélectionnez l\'option **Part Design → Appliquer une fonction d'habillage → <img src="images/PartDesign_Thickness.svg" width=16px> Coque** dans le menu.
4.  S\'il n\'y a pas de corps actif, et qu\'il y a deux corps ou plus dans le document, la boîte de dialogue **Corps actif requis** s\'ouvrira et vous invitera à en activer un. S\'il n\'y a qu\'un seul corps, il sera activé automatiquement.
5.  Le [Panneau des tâches](Task_panel/fr.md) des **Paramètres de la coque**. Voir [Options](#Options.md) pour plus d\'informations.
6.  Appuyez sur le bouton **OK** pour terminer.

   *   *Souvenez-vous*    *
    -   Puisqu\'il doit y avoir au moins une face pour la fonction, la dernière face restant dans la liste ne peut pas être retirée.

### Modifier une coque 

1.  Effectuez l\'une des opérations suivantes    *
    -   Double-cliquez sur l\'objet Thickness dans la [Vue en arborescence](Tree_view/fr.md).
    -   Cliquez avec le bouton droit de la souris sur l\'objet Thickness dans la [Vue en arborescence](Tree_view/fr.md) et sélectionnez **Modifier la coque** dans le menu contextuel.
2.  Le [Panneau des tâches](Task_panel/fr.md) des **Paramètres de la coque** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Appuyez sur le bouton **OK** pour terminer.

## Options

-    **Ajouter une face**   * Ajoutez des faces à la sélection en appuyant sur le bouton **Ajouter une face** et en sélectionnant d\'autres faces.

-    **Supprimer la face**   * Choisissez un moyen de supprimer des faces de la sélection    *

    -   Sélectionnez une ou plusieurs faces dans la liste et appuyez sur la touche **Suppr** ou cliquez droit sur la liste et sélectionnez **Enlever** dans le menu contextuel.
    -   Appuyez sur le bouton **Supprimer la face**. Toutes les faces précédemment sélectionnées sont surlignées en violet. Sélectionnez chaque visage à supprimer.

-   Cliquez sur **Épaisseur**    * Définissez l\'épaisseur de la paroi soit en éditant la valeur, soit en cliquant sur les flèches haut/bas.

-    **Mode**   *

    -   
        **Couche**
        
           * Seule cette option peut être sélectionnée.

    -   
        **Tuyau**
        
           * Non implémenté. Voir [ce sujet du forum](https   *//forum.freecadweb.org/viewtopic.php?p=484495#p484495).

    -   
        **Recto-verso**
        
           * Non implémenté. Voir [idem](https   *//forum.freecadweb.org/viewtopic.php?p=484495#p484495).

-    **Type de raccordement**   *

    -   
        **Arc**
        
           * Lorsque des faces non tangentielles sont décalées, les nouvelles faces qui ne se croisent pas sont jointes par un congé dont le rayon est égal à l\'épaisseur définie.

    -   
        **Intersection**
        
           * Lorsque des faces non tangentielles sont décalées, les nouvelles faces qui ne se croisent pas sont prolongées pour se rencontrer à leur intersection virtuelle.

-    **Intersection**   * Lorsque cette option est cochée, les auto-intersections dans certains modèles sont évitées. Cette option n\'est pas recommandée car elle repose sur une [méthode incomplète OpenCASCADE](https   *//dev.opencascade.org/doc/refman/html/class_b_rep_offset_a_p_i___make_thick_solid.html#af78f35025a31e2ce8bd96c82fb33a981).

-    **Générer la coque vers l'intérieur**   * Lorsque cette case est cochée, les faces sont décalées vers l\'intérieur.

## Remarques

-   Si la coque va vers l\'intérieur, la valeur doit être inférieure à la plus petite hauteur du corps.
-   L\'outil peut échouer avec des formes complexes. Les outils [PartDesign Balayage additif](PartDesign_AdditivePipe/fr.md) ou [PartDesign Lissage additif](PartDesign_AdditiveLoft/fr.md) peuvent mieux fonctionner pour créer des formes complexes.
-   Erreurs connues    *
    -   BRep\_API    * commande non effectuée.
    -   BRep\_Tool    * aucun paramètre sur le bord.
    -   Echec silencieux.

## Propriétés

Voir aussi   * [Éditeur de propriétés](Property_editor/fr.md)

Un objet Part Épaisseur est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes    *

### Données


{{Properties_Title|Base}}

-    **Base|LinkSub**   * Sous-lien vers la liste des arêtes et des faces sélectionnées de l\'élément parent.

-    **Support Transform|Bool**   * Inclut la forme additive/soustractive de base lorsqu\'elle est utilisée dans les caractéristiques de motif. S\'il est désactivé, seule la partie habillée de la forme est utilisée pour le modelage. Valeur par défaut    * `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**   * Lien vers l\'élément parent.

-    **_ Body|LinkHidden|hidden**   * Lien vers le corps du parent.


{{Properties_Title|Part Design}}

-    **Refine|Bool**   * Raffiner la forme (nettoyer les arêtes redondantes) après l\'ajout/soustraction. La valeur par défaut est déterminée par la préférence **Affiner automatiquement le modèle après une opération d'esquisse**. Voir [PartDesign Préférences](PartDesign_Preferences/fr#G.C3.A9n.C3.A9ral.md).


{{Properties_Title|Thickness}}

-    **Value|Length**   * \"Valeur de l\'épaisseur\". Valeur par défaut    * {{value|1 mm}}.

-    **Mode|Enumeration**   * \"Mode\". {{value|Skin}} (par défaut), {{value|Pipe}} ou {{Value|Recto verso}}. Seule {{value|Skin}} est implémentée.

-    **Join|Enumeration**   * \"Type de raccordement\". {{value|Arc}} (par défaut) ou {{Value|Intersection}}.

-    **Reversed|Bool**   * \"Générer l\'épaisseur vers l\'intérieur du solide\". Valeur par défaut    * `False`.

-    **Intersection|Bool**   * \"Activer la gestion de l\'intersection\". Valeur par défaut    * `False`.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Thickness/fr
