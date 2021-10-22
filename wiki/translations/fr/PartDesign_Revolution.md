---
- GuiCommand:/fr
   Name:PartDesign_Revolution
   Name/fr:PartDesign Révolution
   MenuLocation:Conception de pièces → Créer une fonction additive → Révolution
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
---

# PartDesign Revolution/fr

## Description

L\'outil **Révolution** produit un solide par révolution d\'une esquisse ou d\'un objet 2D sélectionné autour d\'un axe donné.

![](images/PartDesign_Revolution_example.svg ) 
*Ci-dessus : l'esquisse (A) est révolutionnée de 270 degrés dans le sens antihoraire autour de l'axe (B) ; le solide résultant (C) est montré à droite.*

## Utilisation

1.  Sélectionner l\'esquisse à révolutionner. v0.17 et ultérieures Une face du solide peut également être utilisée.
2.  Appuyer sur le bouton **<img src="images/PartDesign_Revolution.svg" width=24px> '''Révolution d'une esquisse sélectionnée'''**.
3.  Définir les paramètres de la révolution (voir la section suivante).
4.  Appuyer sur le bouton **OK**.

## Options

Lors de la création de la révolution, les **Paramètres de la révolution** permettent de définir les réglages de révolution de l\'esquisse.

+----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/partdesign_revolution_parameters.png ) | ### Axe                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                  | Cette option spécifie l\'axe autour duquel l\'esquisse doit être tournée.                                                                                                                                                                                                                                                                                                                                                |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                  | -   **Axe d\'esquisse vertical** : sélectionne l\'axe d\'esquisse vertical.                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  | -   **Axe d\'esquisse horizontal** : sélectionne l\'axe d\'esquisse horizontal.                                                                                                                                                                                                                                                                                                                                          |
|                                                                                  | -   **Sketch axis**: v0.16 et antérieures sélectionne une ligne de construction contenue dans l\'esquisse utilisée par la Révolution. La première ligne de construction créée dans l\'esquisse sera nommée *Sketch axis 0*. Le menu déroulant contiendra une entrée pour chaque ligne de construction.                                              |
|                                                                                  | -   **Ligne de construction** : v0.17 et ultérieures sélectionne une ligne de construction contenue dans l\'esquisse utilisée par la Révolution. Le menu déroulant contiendra une entrée pour chaque ligne de construction. La première ligne de construction créée dans l\'esquisse sera précédée du chiffre 1.                                   |
|                                                                                  | -   **Axe (X/Y/Z)** : v0.17 et ultérieures sélectionne l\'axe X, Y ou Z de l\'origine du corps.                                                                                                                                                                                                                                                    |
|                                                                                  | -   **Sélectionner une référence\...**: v0.17 et ultérieures permet de sélectionner dans la vue 3D une arête du corps ou une [ligne de référence](PartDesign_Line/fr.md).                                                                                                                                                                  |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                  | ### Angle                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                  | Ceci contrôle l\'angle à travers lequel la révolution doit être formée, par exemple 360° serait une révolution complète et contiguë. Les images de la section [Exemples](#Exemples.md) montrent certaines des possibilités offertes par la spécification de différents angles. Il n\'est pas possible de spécifier des angles négatifs (utilisez plutôt l\'option **Reversed**) ou des angles supérieurs à 360°. |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                  | ### Symétrique au plan                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                  | Si cette case est cochée, la révolution s\'étendra sur la moitié de l\'angle spécifié dans les deux directions à partir du plan de l\'esquisse.                                                                                                                                                                                                                                                                          |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                  | ### Inversé                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                  | Si cette case est cochée, le sens de la révolution est inversé, passant du sens horaire par défaut au sens antihoraire.                                                                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Propriétés

Ci-dessous les propriétés qui peuvent être modifiées après la création de la fonction. Les propriétés sous l\'onglet Données *Base* et *Axis* ne sont pas modifiables.

-    {{PropertyData/fr|Angle}}: angle de rotation. Voir [Angle](#Angle.md).

-    {{PropertyData/fr|Label}}: étiquette donnée à l\'opération; peut être changée selon votre convenance.

-    {{PropertyData/fr|Midplane}}: true (vrai) ou false (faux). Voir [Symétrique au plan](#Symétrique_au_plan.md).

-    {{PropertyData/fr|Reversed}}: true (vrai) ou false (faux). Voir [Inversé](#Inversé.md).

-    {{PropertyData/fr|Refine}}: v0.17 et ultérieures true (vrai) ou false (faux). Si la valeur est true, nettoie le solide des arêtes résiduelles laissées par les fonctions. Voir [Affiner la forme](Part_RefineShape/fr.md) pour plus de détails.

## Exemples

![Exemple de révolution utilisant une ligne de construction comme axe de révolution: dans cette image l\'angle est de 75°, la révolution est sur la ligne de construction (axe Sketch 0).](images/PartDesign_Revolution_axis_fromconstructionlines1.jpg )

## Liens utiles 

Un [exemple](http://forum.freecadweb.org/viewtopic.php?f=3&t=3674) d\'utilisation détaillé sur le forum (en anglais).





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/fr
