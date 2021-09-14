---
- GuiCommand:/fr
   Name:Part Tube
   Name/fr:Part Tube
   MenuLocation:Pièce → Primitives → Créer un tube
   Workbenches:[Part](Part_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Part Primitives](Part_CreatePrimitives/fr.md)
---

## Description

La commande Tube permet d\'insérer un tube dans le document actif. Le tube est traité géométriquement comme la découpe d\'un petit cylindre en un plus grand. Par défaut, la commande insère un tube de 10 mm de hauteur avec un rayon extérieur de 5 mm et un rayon intérieur de 2 mm. Ces paramètres peuvent être modifiés après l\'ajout de l\'objet.

![Capture d\'écran d\'un tube](images/Part_Tube-screenshot.png )

## Utilisation

Pour créer un tube :

-   appuyez sur le bouton **<img src="images/Part_Tube.svg" width=16px> Créer un tube** dans la barre d\'outils
-   utilisez le menu **Pièce → Primitives → Créer un tube**

Pour éditer le tube

-   Soit
    -   sélectionnez-le dans l\'arborescence et double-cliquez dessus
    -   modifier les paramètres dans la boîte de dialogue qui apparaît
-   ou utilisez l\'[Éditeur de propriétés](Property_editor/fr.md) pour éditer les paramètres

## Propriétés

-   Via l\'[Éditeur de propriétés](Property_editor/fr.md):
    -   **Height:** Définit la hauteur (la valeur par défaut est 10 mm).
    -   **Inner Radius:** Définit le rayon intérieur (la valeur par défaut est 2 mm).
    -   **Outer Radius:** Définit le rayon extérieur (la valeur par défaut est 5 mm).
    -   **Placement:** Spécifie l\'orientation et la position de la boîte dans l\'espace 3D. Voir [Placement](Placement/fr.md). Le point de référence est le coin inférieur avant gauche de la boîte.
    -   **Label:** L\'étiquette est le nom donné à l\'opération. Ce nom peut être changé à votre convenance.





 
