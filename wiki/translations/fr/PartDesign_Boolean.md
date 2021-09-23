---
- GuiCommand:/fr
   Name:PartDesign Boolean
   Name/fr:PartDesign Opérations booléennes
   MenuLocation:Conception de pièces → Opération booléenne
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
---

# PartDesign Boolean/fr

## Description

L**\'opération Booléenne** importe un ou plusieurs [PartDesign Corps](PartDesign_Body/fr.md) ou [PartDesign Clones](PartDesign_Clone/fr.md) (désignés comme \"outils Corps\") dans un PartDesign Corps actif et applique une opération booléenne (fusion, soustraction ou intersection).

![](images/PartDesign_Boolean_example.png )


*A gauche : un corps actif (A) avec des corps (B) et (C). A droite : le résultat après une soustraction booléenne.*

## Utilisation

1.  [Activer le corps](PartDesign_Body/fr#Statut_actif.md) qui doit recevoir la fonction booléenne. ***Remarque** : il est important de s\'assurer que ni le corps actif, ni aucune des fonctions qu\'il contient ne soit sélectionné avant de passer à l\'étape 2.*
2.  Pressez le bouton **<img src="images/PartDesign_Boolean.svg" width=16px> [Opération Booléenne...](PartDesign_Boolean/fr.md)**.
3.  Dans **Paramètres booléens**, cliquez le bouton **Ajouter un corps**. Le corps actif va temporairement disparaître de la vue 3D pour faciliter les sélections.
4.  Dans la [vue 3D](3D_view/fr.md), sélectionnez le corps à utiliser dans la fonction booléenne. Répétez pour ajouter plus de corps.
5.  Sélectionnez le type d\'opération booléenne dans le menu déroulant (fusion, soustraction ou intersection).
6.  Cliquer **OK**.

Alternativement, un ou plusieurs corps peuvent être sélectionnés avant d\'appuyer sur le bouton booléen. Ils seront automatiquement ajoutés.

## Options

-   **Union :** fusionne le ou les corps désignés avec le corps actif.
-   **Soustraction :** soustrait le corps ou les corps désignés du corps actif.
-   **Intersection :** extrait l\'intersection du ou des corps sélectionnés avec le corps actif.
-   Presser le bouton **Enlever un corps** pour retirer un corps, en le sélectionnant dans la [vue 3D](3D_view/fr.md).

## Propriétés

-    {{PropertyData/fr|Type}}: définit l\'opération Booléenne (Addition, Soustraction, Intersection)

-    {{PropertyData/fr|Label}}: nom donné à l\'opération, changer si nécessaire.

-    {{PropertyData/fr|Group}}: liste les corps utilisés.

-    {{PropertyView/fr|Display}}: choix de l\'affichage entre deux modes:

    -   Résultat (par défaut) : affiche le résultat de la fonction booléenne. Dans ce mode, les corps ne peuvent pas être affichés dans leur état d\'origine, même si leur visibilité est activée.
    -   Constituants : affiche les corps concernés dans leur état d\'origine. Ce mode d\'affichage est utile lorsque vous modifiez des corps.

-    {{PropertyView/fr|Sélectionnable}}: true ou false. Si false, l\'objet ne peut pas être sélectionné dans la vue 3D.

-    {{PropertyView/fr|Visibilité}}: true ou false. Si false l\'objet sera invisible dans la vue 3D.

## Limites

-   Pour que Intersection fonctionne avec plus d\'un corps autre que le corps actif, chacun doit avoir une partie commune avec le corps actif.
-   Les corps utilisés adoptent l\'origine locale du corps actif. Si le corps actif n\'est pas situé aux coordonnées (0,0,0) dans le système de coordonnées global, le placement des corps utilisés doit être relatif au corps actif. Il peut être plus facile de transposer le placement du corps actif à l\'origine avant d\'appliquer la fonction booléenne, puis de le replacer à son emplacement d\'origine.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Boolean/fr
