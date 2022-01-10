---
- GuiCommand:/fr
   Name:Part Tube
   Name/fr:Part Tube
   MenuLocation:Pièce → Primitives → Créer un tube
   Workbenches:[Part](Part_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Part Primitives](Part_CreatePrimitives/fr.md)
---

# Part Tube/fr

## Description

La commande Tube permet d\'insérer un tube dans le document actif. Le tube est traité géométriquement comme la découpe d\'un petit cylindre en un plus grand. Par défaut, la commande insère un tube de 10 mm de hauteur avec un rayon extérieur de 5 mm et un rayon intérieur de 2 mm. Ces paramètres peuvent être modifiés après l\'ajout de l\'objet.

![Capture d\'écran d\'un tube](images/Part_Tube-screenshot.png )

## Utilisation

Pour créer un tube :

-   appuyez sur le bouton **<img src="images/Part_Tube.svg" width=16px> Tube** dans la barre d\'outils
-   utilisez le menu **Pièce → Primitives → Tube**

Pour éditer le tube

-   soit vous
    -   le sélectionnez dans l\'arborescence et double-cliquez dessus
    -   modifiez les paramètres dans la boîte de dialogue qui apparaît
-   soit vous utilisez l\'[Éditeur de propriétés](Property_editor/fr.md) pour éditer les paramètres

## Propriétés

-   Via l\'[Éditeur de propriétés](Property_editor/fr.md):
    -   
        **Placement**
        
        : Spécifie l\'orientation et la position de la boîte dans l\'espace 3D. Voir [Placement](Placement/fr.md). Le point de référence est le coin inférieur avant gauche de la boîte.

    -   
        **Label**
        
        : Nom donné à l\'opération. Ce nom peut être modifié à votre convenance.

    -   
        **Height**
        
        : Définit la hauteur (10 mm par défaut).

    -   
        **Inner Radius**
        
        : Définit le rayon intérieur (2 mm par défaut).

    -   
        **Outer Radius**
        
        : Définit le rayon extérieur (5 mm par défaut).

## Script

Un Part Tube peut être créé en utilisant la fonction suivante:


```python
tube = FreeCAD.ActiveDocument.addObject("Part::Tube", "myTube")
```

-   Où {{Incode|"myTube"}} est le nom de l\'objet.
-   La fonction restitue l\'objet nouvellement créé.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Tube/fr
