---
 GuiCommand:
   Name: Part Thickness
   Name/fr: Part Évider
   MenuLocation: Part , Évider...
   Workbenches: Part_Workbench/fr
   SeeAlso: Part_Offset/fr
---

# Part Thickness/fr

## Description

L\'outil <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Évider](Part_Thickness/fr.md) travaille sur une forme solide et la transforme en un objet creux, en donnant à chacune de ses faces une épaisseur définie et constante. Sur certains solides, il permet d\'accélérer considérablement le travail et d\'éviter de faire des extrusions et des cavités.



## Utilisation

1.  Créer un solide
2.  Sélectionner une ou plusieurs faces
3.  Cliquer sur l\'outil **<img src="images/Part_Thickness.svg" width=16px> '''Évider...'''
**
4.  Régler les paramètres (voir [Options](#Options.md))
5.  Cliquer sur **OK** pour confirmer, créer l\'opération et quitter la fonction
6.  Dans le tableau des Propriétés, ajuster les paramètres si nécessaire.

## Options

-    **Épaisseur**: épaisseur de la paroi de l\'objet résultant, définir la valeur souhaitée

    -   Une valeur positive décalera les faces vers l\'extérieur
    -   Une valeur négative décalera les faces vers l\'intérieur

-    **Mode**-   
        **Objet creux**
        
        : sélectionner cette option pour obtenir un élément comme un vase, sans dessus mais avec le fond.

    -   
        **Tube**
        
        : sélectionner cette option pour obtenir un objet comme un tube, sans dessus et sans fond. Dans ce cas, il peut être pratique de sélectionner les faces à supprimer avant de démarrer l\'outil. Utiliser les boutons de vues prédéfinies ou utiliser les touches numériques.

    -   
        **Recto/verso**
        
        :

-    **Type de jointure**-   
        **Arc**
        
        : supprime les bords extérieurs et créer un congé avec un rayon égal à l\'épaisseur définie.

    -   
        **Tangent**
        
        :

    -   
        **Intersection**
        
        :

-    **Intersection**:

-    **Auto-intersection**: permet l\'auto-intersection

-    **Faces**: sélectionner les faces à supprimer puis cliquer **Terminé**.

-    **Mise à jour de la vue**: met à jour automatiquement la vue en temps réel.



## Remarques

-   Les objets [App Link](App_Link/fr.md) liés aux types d\'objets appropriés peuvent également être utilisés comme objets sources. {{Version/fr|0.20}}
-   Les formes complexes peuvent produire des résultats bizarres et difficiles à prévoir. Inspectez soigneusement la forme obtenue et sauvegardez votre travail avant d\'appliquer l\'opération.



## Liens

Un bon exemple sur la façon d\'utiliser cet outil sur le forum : [Re: Help designing a simple enclosure](http://forum.freecadweb.org/viewtopic.php?f=3&t=3766&p=29741&hilit=enclosure#p29547)



## Exemples

**Cylindre creux**

1.  Créer un **<img src="images/Part_Cylinder.svg" width=16px> [Part Cylindre](Part_Cylinder/fr.md)** avec un rayon de 10 mm et une hauteur de 20 mm
2.  Sélectionner la surface supérieure et inférieure du cylindre
3.  Cliquer sur le bouton **<img src="images/_Part_Thickness.svg" width=16px> Évider...
** (pas besoin de modifier les paramètres par défaut) et appuyer sur **OK**

Remarques :

-   Pour cette forme, pensez à utiliser **<img src="images/Part_Tube.svg" width=16px> [Part Tube](Part_Tube/fr.md)** à la place.
-   Sélectionnez la surface supérieure du cylindre uniquement pour créer un réceptacle.

<img alt="" src=images/ThicknessEsempio1.png  style="width:600px;">

<img alt="" src=images/ThicknessEsempio2.png  style="width:600px;">

**Enveloppe de boîte**

<img alt="" src=images/ThicknessEsempio3.png  style="width:600px;">

<img alt="" src=images/ThicknessEsempio4.png  style="width:600px;">



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Thickness/fr
