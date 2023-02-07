---
- GuiCommand:/fr
   Name:PartDesign_Groove
   Name/fr:PartDesign Rainure
   MenuLocation:Part Design → Créer une fonction soustractive → Rainure
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso:[PartDesign Révolution](PartDesign_Revolution/fr.md)
---

# PartDesign Groove/fr

## Description

L\'outil **Rainure** fait pivoter une esquisse ou un profil sélectionné autour d\'un axe donné en découpant la matière du support.

![](images/PartDesign_Groove_example.svg )



*Ci-dessus : l'esquisse (A) tourne autour de l'axe (B); la rainure résultante sur le solide (C) est illustrée à droite.*



## Utilisation

1.  Sélectionnez l\'esquisse à révolutionner.

    :   \- Une face sur le solide existant peut également être utilisée. {{VersionPlus/fr|0.17}}
    :   \- L\'esquisse doit être mappée sur la face plane d\'un solide existant ou d\'une fonction de conception de pièce, sinon un message d\'erreur apparaîtra. {{VersionMinus/fr|0.16}}
2.  Appuyez sur le bouton **<img src="images/PartDesign_Groove.svg" width=24px> '''Rainure'''**.
3.  Définissez les paramètres de la révolution (voir la section suivante).
4.  Appuyez sur le bouton **OK**.

## Options

Lors de la création de la révolution, les **Paramètres de la rainure** permettent de définir les réglages de révolution de l\'esquisse.

+++
| ![](images/partdesign_groove_parameters.png ) | ### Axes                                                                                                                                                                                                                                                                                                                          |
|                                                                          |                                                                                                                                                                                                                                                                                                                                   |
|                                                                          | Cette option spécifie l\'axe autour duquel l\'esquisse doit être tournée.                                                                                                                                                                                                                                                         |
|                                                                          |                                                                                                                                                                                                                                                                                                                                   |
|                                                                          | -   **Axe d\'esquisse vertical** : sélectionne l\'axe d\'esquisse vertical.                                                                                                                                                                                                                                                       |
|                                                                          | -   **Axe d\'esquisse horizontal** : sélectionne l\'axe d\'esquisse horizontal.                                                                                                                                                                                                                                                   |
|                                                                          | -   **Axe d\'esquisse** : sélectionne une ligne de construction contenue dans l\'esquisse utilisée par la Révolution. La première ligne de construction créée dans l\'esquisse sera nommée *Sketch axis 0*. Le menu déroulant contiendra une entrée pour chaque ligne de construction. {{VersionMinus/fr|0.16}}     |
|                                                                          | -   **Ligne de construction** : sélectionne une ligne de construction contenue dans l\'esquisse utilisée par la Révolution. Le menu déroulant contiendra une entrée pour chaque ligne de construction. La première ligne de construction créée dans l\'esquisse sera précédée du chiffre 1. {{VersionPlus/fr|0.17}} |
|                                                                          | -   **Axe (X/Y/Z)** : sélectionne l\'axe X, Y ou Z de l\'origine du corps. {{VersionPlus/fr|0.17}}                                                                                                                                                                                                                  |
|                                                                          | -   **Sélectionner une référence\...** : permet de sélectionner dans la vue 3D une arête du corps ou une [ligne de référence](PartDesign_Line/fr.md). {{VersionPlus/fr|0.17}}                                                                                                                               |
|                                                                          |                                                                                                                                                                                                                                                                                                                                   |
|                                                                          | ### Angle                                                                                                                                                                                                                                                                                                                         |
|                                                                          |                                                                                                                                                                                                                                                                                                                                   |
|                                                                          | Détermine la valeur de la rotation, par exemple, 360 ° seraient, une révolution complète. Il n\'est pas possible de spécifier des angles négatifs (utiliser l\'option **Inversé** à la place) ou des angles supérieurs à 360 °.                                                                                                   |
|                                                                          |                                                                                                                                                                                                                                                                                                                                   |
|                                                                          |                                                                                                                                                                                                                                                                            |
|                                                                          |                                                                                                                                                                                                                                                                                                                                   |
|                                                                          | ### Symétrique au plan                                                                                                                                                                                                                                                                                       |
|                                                                          |                                                                                                                                                                                                                                                                                                                                   |
|                                                                          | La révolution s\'étendra de la moitié de l\'angle spécifié dans les deux directions symétriques au plan d\'esquisse.                                                                                                                                                                                                              |
|                                                                          |                                                                                                                                                                                                                                                                                                                                   |
|                                                                          |                                                                                                                                                                                                                                                                                      |
|                                                                          |                                                                                                                                                                                                                                                                                                                                   |
|                                                                          | ### Inversé                                                                                                                                                                                                                                                                                                                       |
|                                                                          |                                                                                                                                                                                                                                                                                                                                   |
|                                                                          | La direction de la révolution sera inversée du défaut, qui est dans le sens des aiguilles d\'une montre.                                                                                                                                                                                                                          |
+++



## Propriétés

Ci-dessous les propriétés qui peuvent être modifiées après la création de la fonction. Les propriétés sous l\'onglet Données *Base* et *Axis* ne sont pas modifiables.

-    **Angle**: angle de rotation. Voir [Angle](#Angle.md).

-    **Label**: étiquette donnée à l\'opération; peut être changée selon votre convenance.

-    **Midplane**: true (vrai) ou false (faux). Voir [Symétrique au plan](#Sym.C3.A9trique_au_plan.md).

-    **Reversed**: true (vrai) ou false (faux). Voir [Inversé](#Inversé.md).

-    **Refine**: true (vrai) ou false (faux). Si la valeur est true, nettoie le solide des arêtes résiduelles laissées par les fonctions. Voir [Affiner la forme](Part_RefineShape/fr.md) pour plus de détails. {{VersionPlus/fr|0.17}}





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Groove/fr
