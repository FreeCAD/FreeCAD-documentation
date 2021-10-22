---
- GuiCommand:/fr
   Name:Rocket Transition
   Name/fr:Rocket Transition
   MenuLocation:Rocket → Transition
   Workbenches:[Rocket](Rocket_Workbench/fr.md)
   Version:0.19
---

# Rocket Transition/fr

## Description

Les transitions sont comme [Coiffe](Rocket_NoseCone/fr.md) à bien des égards. Bien que généralement coniques, elles peuvent avoir les mêmes formes que les coiffes mais sont beaucoup plus polyvalents.

L\'application la plus courante consiste à passer d\'un diamètre de corps à un autre, par exemple entre les étapes, ou à la base d\'un carénage de charge utile. Elle peut également être utilisée pour la pointe d\'une fusée où le diamètre de la fusée diminue vers la tuyère d\'échappement.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Rocket_Transition.svg" width=16px> [Transition](Rocket_Transition/fr.md)**.
    -   Sélectionnez l\'option **Rocket  → <img src="images/Rocket_Transition.svg" width=16px> Transition** dans le menu.
    -   Double-cliquez sur un objet Transition dans la vue du modèle.
2.  Définissez les options et appuyez sur **OK**.

## Options

### Types de transition 

Les transitions prennent en charge toutes les formes prises en charge par Coiffe, voir [Options de coiffe](Rocket_NoseCone/fr#Options.md) pour plus de détails.

### Styles de transition 

Les transitions prennent en charge tous les styles pris en charge par Coiffe, voir [Options de coiffe](Rocket_NoseCone/fr#Options.md) pour plus de détails.

De plus, les transitions ont une autre option de style, *Solid Core*. Pour ce style, la transition est solide mais avec un trou d\'une extrémité à l\'autre. Un exemple où cela pourrait être utilisé est une transition en balsa conçue pour maintenir un tube du corps à la manière d\'une bague de centrage.

![](images/Core_transition_with_tube.png ) 
*Transition avec épaulement arrière tenant un tube du corps*

![](images/Core_transition.png ) 
*Transition avec épaulement arrière montrant le noyau interne*

### Coupé

Des formes telles qu\'une ogive ou une parabole peuvent être appliquées de deux manières. Le standard, non coupé, traite l\'axe parallèle à l\'axe central décalé par le plus petit des rayons avant et arrière comme l\'axe de dessin de la forme. La méthode découpée applique une version plus grande de la courbe centrée autour de l\'axe de transition et coupe la partie en avant du rayon le plus petit. Dans cet exemple, la courbe non découpée est dessinée de *x=0* à *x=60* autour de l\'axe *y=0*. La version découpée étend la forme le long de l\'axe x jusqu\'à *y=0* et ne prend que la partie de *x=0* à *x=60*.
![](images/ParabolaClippedVsNon.png ) 
*Courbes coupées et non coupées pour une transition parabolique*
Pour certaines formes, cela ne fait aucune différence dans la forme de la transition, comme pour les formes coniques ou ogives. Dans ces cas, le découpage est ignoré.
![](images/OgiveClippedVsNon.png ) 
*Courbes coupées et non coupées pour une transition en ogive*

## Remarques

Il y a des problèmes connus avec le dessin des transitions sur lesquels on travaille actuellement.

-   Les versions coupées des transitions elliptiques produisent des formes non valides
-   Les versions coupées où le rayon avant est plus grand que le rayon arrière peuvent produire des formes invalides. Si tel est le cas, vous pouvez concevoir la transition vers l\'arrière et utiliser la position pour la faire pivoter.

## Propriétés


{{TitleProperty|Rocket Component}}

Ces paramètres sont fournis à titre indicatif et n\'ont aucun effet sur la conception du composant.

-    {{PropertyData/fr|Manufacturer}}: Fabricant lorsqu\'il est connu

-    {{PropertyData/fr|Part Number}}: Numéro de pièce du fabricant

-    {{PropertyData/fr|Description}}: Description du composant

-    {{PropertyData/fr|Material}}: Matériau lorsqu\'il est connu


{{TitleProperty|Transition}}

-    {{PropertyData/fr|Transition Type}}: Définit la forme de la transition en utilisant le coefficient si nécessaire, voir [Options](#Options.md)

-    {{PropertyData/fr|Transition Style}}: Définit le style de la transition, voir [Options](#Options.md)

-    {{PropertyData/fr|Clipped}}: Définit la forme de la transition en combinaison avec **Transition Type**, voir [Options](#Options.md)

-    {{PropertyData/fr|Length}}: La longueur de la transition sans les épaules

-    {{PropertyData/fr|Aft Radius}}: Le rayon de la base de la transition

-    {{PropertyData/fr|Fore Radius}}: Le rayon de l\'avant de la transition

-    {{PropertyData/fr|Core Radius}}: Lorsque **Transition Type** est *Solid Core*, cela déterminera la taille du trou à travers la transition, voir [Options](#Options.md)

-    {{PropertyData/fr|Thickness}}: Lorsque **Transition Type** est *Hollow* ou *Capped*, cela déterminera l\'épaisseur de la paroi de la transition

-    {{PropertyData/fr|Coefficent}}: Combiné avec le **Transition Type**, cela définit la forme de la transition, voir [Options](#Options.md)

-    {{PropertyData/fr|Aft Shoulder}}: Vrai lorsque la transition comprend un épaulement à la base

-    {{PropertyData/fr|Aft Shoulder Length}}: La longueur de l\'épaulement

-    {{PropertyData/fr|Aft Shoulder Radius}}: Le rayon de l\'épaule. Celui-ci doit être inférieur au **Fore Radius** de la transition

-    {{PropertyData/fr|Aft Shoulder Thickness}}: Lorsque **Transition Type** est *Hollow* ou *Capped*, cela déterminera l\'épaisseur de la paroi de l\'épaulement

-    {{PropertyData/fr|Fore Shoulder}}: Vrai lorsque la transition inclut un épaulement à l\'extrémité avant

-    {{PropertyData/fr|Fore Shoulder Length}}: La longueur de l\'épaulement

-    {{PropertyData/fr|Fore Shoulder Radius}}: Le rayon de l\'épaule. Cela doit être inférieur au **Fore Radius** de la transition

-    {{PropertyData/fr|Fore Shoulder Thickness}}: Lorsque **Transition Type** est *Hollow* ou *Capped*, cela déterminera l\'épaisseur de la paroi de l\'épaulement

-    {{PropertyData/fr|Resolution}}: Utilisé en interne, ce paramètre définit le nombre de points de données à utiliser lors du dessin du contour de la coiffe

## Script

Voir aussi : _ et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

A définir

## Tutoriels et apprentissage 

[Transitions atelier Rocket](https://youtu.be/O5Ze4MYAHNA) Tutoriel sur YouTube







_ _

---
[documentation index](../README.md) > [API/fr]] et ](Category_API/fr]] et .md) > Rocket Transition/fr
