---
- GuiCommand:/fr
   Name:Part Thickness
   Name/fr:Part Évidement
   MenuLocation:Pièce → Évidement...
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Décalage](Part_Offset/fr.md)
---

# Part Thickness/fr

## Description

L\'outil <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Évidement](Part_Thickness/fr.md) travaille sur une forme solide et le transforme en un objet creux, donnant à chacune de ses parois une épaisseur définie. Sur certains solides, il vous permet d\'accélérer considérablement le travail et évite de faire des extrusions et des cavités.

## Utilisation

1.  Créer un solide
2.  Sélectionnez une ou plusieurs faces
3.  Cliquez sur l\'outil **<img src="images/Part_Thickness.svg" width=16px> '''Évidement d'un solide sélectionné'''
**
4.  Régler les paramètres (voir [Options](#Options.md))
5.  Cliquez sur **OK** pour confirmer, créer l\'opération et quitter la fonction
6.  Dans le tableau Propriétés ajuster les paramètres si nécessaire.

## Options

-   Épaisseur : Épaisseur de la paroi de l\'objet résultant, définissez la valeur souhaitée
    -   Une valeur positive décalera les faces vers l\'extérieur
    -   Une valeur négative décalera les faces vers l\'intérieur
-   Mode
    -   Couche : Sélectionnez cette option si vous voulez obtenir un élément comme un vase, sans dessus, mais avec le fond
    -   Tuyau : Sélectionnez cette option si vous voulez obtenir un objet comme un tuyau, sans dessus et sans fond. Dans ce cas, il peut être pratique de sélectionner les faces à supprimer avant de démarrer l\'outil. Aidez-vous des boutons de vues prédéfinies ou utilisez les touches numériques.
    -   Recto/verso :
-   Type de raccordement
    -   Arc : supprime les bords extérieurs et créer un congé avec un rayon égal à l\'épaisseur définie
    -   Tangente :
    -   Intersection :
-   Intersection :
-   Auto-intersection : Permet l\'auto-intersection
-   Faces  : Sélectionnez les faces à supprimer, après sélection de la première face, enfoncer Ctrl pour sélectionner les autre faces, utiliser l\'outil de rotation(sans Ctrl) pour faire voir les autres faces et continuer la sélection (après appuis sur Ctrl)
-   Réactualiser la vue : met à jour automatiquement la vue en temps réel

## Limitations

Des formes complexes peuvent produire des résultats bizarres et difficiles à prévoir. Inspectez soigneusement la forme obtenue et enregistrez votre travail avant d\'appliquer l\'opération.

## Liens

Un bon exemple sur la façon d\'utiliser cet outil sur le forum: [Re: Help designing a simple enclosure](http://forum.freecadweb.org/viewtopic.php?f=3&t=3766&p=29741&hilit=enclosure#p29547)

## Exemples

**Cylindre creux**

1.  Créer un **<img src="images/Part_Cylinder.svg" width=16px> [Cylindre](Part_Cylinder/fr.md)** avec un rayon de 10 mm et une hauteur de 20 mm
2.  Sélectionnez la surface supérieure et inférieure du cylindre
3.  Cliquez sur le bouton **<img src="images/_Part_Thickness.svg" width=16px> Évidement
** (pas besoin de modifier les paramètres par défaut) et appuyez sur **OK**

Remarques:

-   Pour cette forme, pensez à utiliser **<img src="images/Part_Tube.svg" width=16px> [Tube](Part_Tube/fr.md)** à la place {{Version/fr|0.19}}
-   Sélectionnez la surface supérieure du cylindre uniquement pour créer un réceptacle

![](images/ThicknessEsempio1.png )

![](images/ThicknessEsempio2.png )

**Enveloppe de boîte**

![](images/ThicknessEsempio3.png )

![](images/ThicknessEsempio4.png )

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Thickness/fr
