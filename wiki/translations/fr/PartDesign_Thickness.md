---
- GuiCommand:/fr
   Name:PartDesign Thickness
   Name/fr:PartDesign Épaisseur
   MenuLocation:Part Design → Appliquer une fonction d'habillage → Épaisseur
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Part Évidement](Part_Thickness/fr.md)
---

# PartDesign Thickness/fr

## Description

L\'outil **Épaisseur** s\'applique sur un corps solide et le transforme en un objet creux à paroi épaisse avec au moins une face ouverte, donnant à chacune de ses faces restantes une épaisseur uniforme. Sur certains solides, cela permet d\'accélérer considérablement le travail et d\'éviter les extrusions et les poches.

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width:600px;"> 
*L'outil Epaisseur appliqué à une face (B) d'un solide (A), donnant lieu à l'objet creux (C).*

## Utilisation

1.  Sélectionner un ou plusieurs face(s) sur le corps actif.
2.  Appuyez sur le bouton **<img src="images/PartDesign_Thickness.svg" width=24px> '''Épaisseur'''**.
3.  Définir les **Paramètres d\'épaisseur** (voir [Options](#Options.md)).
4.  Pour ajouter d\'autres faces à ouvrir, appuyer sur le bouton **Ajouter une face** et sélectionner une face dans la [vue 3D](3D_view/fr.md).
5.  Pour supprimer une face précédemment sélectionnée, appuyez sur le bouton **Supprimer la face** et sélectionner une face dans la vue 3D, ou faites un clic droit sur l\'étiquette Face dans la liste et sélectionner *Supprimer*.
6.  Appuyez sur **OK**.

## Options

-   **Épaisseur** : épaisseur de paroi de l\'objet résultant. Définissez la valeur souhaitée.
-   **Mode**
    -   *Couche* : sélectionner cette option pour obtenir un objet comme un vase, sans tête mais avec le fond.
    -   *Tuyau* : sélectionner cette option pour obtenir un objet comme un tuyau, sans tête et sans fond. Dans ce cas, il peut être pratique de sélectionner les faces à supprimer avant de démarrer l\'outil. Aidez-vous des boutons de vues prédéfinies ou utilisez les touches numériques.
    -   *Recto-verso* :
-   **Type de raccordement**
    -   *Arc* : supprime les bords extérieurs et crée un congé avec un rayon égal à l\'épaisseur définie.
    -   *Intersection* : lorsque les faces sont décalées vers l\'extérieur, les arêtes vives sont conservées entre les faces.
-   **Générer l\'épaisseur vers l\'intérieur** : lorsque coché, les faces sont décalées vers l\'intérieur.

## Limites

-   Au moins une face à ouvrir doit être sélectionnée.
-   Si l\'épaisseur va vers l\'intérieur, la valeur doit être inférieure à la plus petite hauteur du corps.
-   La commande peut échouer avec des formes complexes. Dans ce contexte, la surface, par ex. d\'un cône, doit déjà être considérée comme complexe.
    -   [PartDesign Balayage additif](PartDesign_AdditivePipe/fr.md) ou [PartDesign Lissage additif](PartDesign_AdditiveLoft/fr.md) peuvent être plus efficaces pour créer des formes complexes.

## Exemples

1.  Créer une protrusion à partir de l\'esquisse
2.  Créer une deuxième esquisse sur le plan XY
3.  Créer une deuxième protrusion à partir de la deuxième esquisse

Comme dans les images suivantes :

![](images/Braga-primoPad.png )

![](images/Braga-secondoschizzo.png )

![](images/Braga-secondo_Pad.png )

Alors

1.  Sélectionner une face circulaire
2.  Sélectionner **<img src="images/PartDesign_Thickness.svg" width=24px> Epaisseur
**
3.  Ajouter les autres faces circulaires à la sélection

Résultat : ![](images/Brga-spessore.png )

## Erreurs connues 

-   BRep\_API : commande non effectuée
-   BRep\_Tool : aucun paramètre sur le bord
-   Échec silencieux





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Thickness/fr
