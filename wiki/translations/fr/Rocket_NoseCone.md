---
- GuiCommand:/fr
   Name:Rocket Nose Cone
   Name/fr:Rocket Coiffe
   MenuLocation:Rocket → Nose Cone
   Workbenches:[Rocket](Rocket_Workbench/fr.md)
   Version:0.19
---

# Rocket NoseCone/fr

## Description

Les coiffes sont de formes et de tailles diverses, dont la plupart sont difficiles à modeler sans programmation. Pour de nombreux constructeurs de fusées, cela rend le processus irréalisable. Cette commande permet de créer des coiffes de fusée en utilisant des propriétés simples combinées à un dialogue de tâches spécialisées.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Rocket_NoseCone.svg" width=16px> [Nose Cone](Rocket_NoseCone/fr.md)**.
    -   Sélectionnez l\'option **Rocket → <img src="images/Rocket_NoseCone.svg" width=16px> Nose Cone** dans le menu.
    -   Double-cliquez sur un objet Nose Cone dans la vue du modèle.
2.  Définissez les options et appuyez sur **OK**.

## Options

### Types de coiffe 

La théorie derrière les différentes formes de cône de nez est expliquée ici: [Aérodynamique de la pointe avant](https://fr.wikipedia.org/wiki/A%C3%A9rodynamique_de_la_pointe_avant)

Les types de coiffes pris en charge comprennent:

-   Cône.

![](images/NC_Cone_small.png ) 
*Conique*

-   Ogive.

![](images/NC_Ogive_small.png ) 
*Ogive*

-   Elliptique.

![](images/NC_Elliptical_small.png ) 
*Elliptique*

-   Parabole. La forme généralement considérée comme une parabole n\'est pas générée à l\'aide d\'une série parabolique, mais d\'une série de puissance avec un coefficient de 1/2. Ceci est expliqué dans l\'article de Wikipédia.

![](images/NC_Parabola_small.png ) 
*Parabole (Série de puissances de coefficient 1/2)*

-   Série parabolique. Cette forme est contrainte à l\'aide d\'un coefficient, comme expliqué dans l\'article de Wikipédia.

![](images/NC_Parabolic_0.5_small.png ) 
*Série parabolique de coefficient 1/2* ![](images/NC_Parabolic_1_small.png ) 
*Série parabolique de coefficient 1*

-   Von Karman. Une série Haack avec un coefficient de 0

![](images/NC_Karman_small.png ) 
*Von Karman (Série Haack de coefficient 0)*

-   Série Haack. Cette forme est contrainte à l\'aide d\'un coefficient, comme expliqué dans l\'article de Wikipédia.

![](images/NC_Haack_0.33_small.png ) 
*Série Haack de coefficient 1/3* ![](images/NC_Haack_2_small.png ) 
*Série Haack de coefficient 2*

### Types de coiffe 

Les coiffes peuvent être dessinées dans l\'un des 3 styles

-   Solide: le cône est construit comme une pièce solide, par exemple en bois de balsa.

![](images/NC_Solid_small.png )

-   Creux: Le cône est creux à l\'intérieur avec une épaisseur spécifiée. La fin n\'est pas scellée.

![](images/NC_Hollow_small.png )

-   Couvert: similaire à creux, sauf que l\'extrémité est scellée.

![](images/NC_Capped_small.png )

### Epaulements

Les coiffes peuvent être créés avec ou sans épaulements
![](images/NC_Ogive_small.png ) 
*Ogive avec épaulement* ![](images/NC_No_Shoulder_small.png ) 
*Ogive sans épaulement*

## Propriétés


{{TitleProperty|Rocket Component}}

Ces paramètres sont fournis à titre indicatif et n\'ont aucun effet sur la conception du composant.

-    {{PropertyData/fr|Manufacturer}}: Fabricant lorsqu\'il est connu

-    {{PropertyData/fr|Part Number}}: Numéro de pièce du fabricant

-    {{PropertyData/fr|Description}}: Description du composant

-    {{PropertyData/fr|Material}}: Matériau lorsqu\'il est connu


{{TitleProperty|Coiffe}}

-    {{PropertyData/fr|Nose Type}}: Définit la forme de la coiffe en utilisant le coefficient si nécessaire, voir [Options](#Options.md)

-    {{PropertyData/fr|Nose Style}}: Définit le style de la coiffe, voir [Options](#Options.md)

-    {{PropertyData/fr|Length}}: La longueur de la coiffe sans l\'épaulement

-    {{PropertyData/fr|Radius}}: Le rayon de la base de la coiffe

-    {{PropertyData/fr|Thickness}}: Lorsque le style de la coiffe est creux ou coiffé, cela déterminera l\'épaisseur de la paroi de la coiffe

-    {{PropertyData/fr|Coefficent}}: Combiné avec le type de coiffe, cela définit la forme de la coiffe, voir [Options](#Options.md)

-    {{PropertyData/fr|Shoulder}}: Vrai lorsque la coiffe comprend une épaulement

-    {{PropertyData/fr|Shoulder Length}}: La longueur de l\'épaulement

-    {{PropertyData/fr|Shoulder Radius}}: Le rayon de l\'épaulement. Celui-ci doit être inférieur au rayon de la coiffe conique

-    {{PropertyData/fr|Shoulder Thickness}}: Lorsque le style de la coiffe est creux ou coiffé, cela déterminera l\'épaisseur de la paroi de l\'épaulement

-    {{PropertyData/fr|Resolution}}: Utilisé en interne, ce paramètre définit le nombre de points de données à utiliser lors du dessin du contour de la coiffe

## Script

Voir aussi : _ et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

A définir

## Tutoriels et apprentissage 

[Coiffe atelier Rocket](https://youtu.be/zwLgie2E4Ts) Tutoriel sur YouTube







_ _

---
[documentation index](../README.md) > [API/fr]] et ](Category_API/fr]] et .md) > Rocket NoseCone/fr
