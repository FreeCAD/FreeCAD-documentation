---
- GuiCommand:/fr
   Name:Rocket Fin
   Name/fr:Rocket Aileron
   MenuLocation:Rocket → Fin
   Workbenches:[Rocket](Rocket_Workbench/fr.md)
   Version:0.19
---

# Rocket Fin/fr

## Description

Les ailerons sont utilisés pour contrôler aérodynamiquement la direction du vol.

<img alt="" src=images/Nike_Fin_TTW_2.png  style="width:256px;"> 
*Un aileron conique avec une attache TTW*

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Rocket_Fin.svg" width=16px> [Fin](Rocket_Fin/fr.md)**.
    -   Sélectionnez l\'option **Rocket  → <img src="images/Rocket_Fin.svg" width=16px> Fin** dans le menu.
    -   Double-cliquez sur un objet Fin dans la vue du modèle.
2.  Définissez les options et appuyez sur **OK**.

## Options

### Type d\'aileron 

Pour le moment, seules les ailettes de forme \"trapézoïdale\" sont supportées. Cela changera au fur et à mesure du développement de l\'atelier.

### Section transversale 

La forme en coupe d\'un aileron peut grandement affecter ses performances à différentes vitesses, ainsi que l\'apparence de la fusée. Diverses sections transversales des ailettes ont été mises en œuvre. Les ailettes sont créées en lissant la section transversale de la base jusqu\'à la section transversale de la pointe, de sorte que toutes les combinaisons de **Section transversale de la base** et **Section transversale de pointe** ne produiront pas d\'ailerons utiles.

-   Carré. Les bords avant et arrière sont au carré.

<img alt="" src=images/CS_Square.png  style="width:128px;"> 
*Coupe transversale carrée *

-   Rond. Les bords d\'attaque et de fuite sont arrondis.

<img alt="" src=images/CS_Round.png  style="width:128px;"> 
*Coupe transversale ronde *

-   Profil aérodynamique. Utilise la forme aérodynamique symétrique du [Profil NACA](https://fr.wikipedia.org/wiki/Profil_NACA) avec une épaisseur maximale à 30% de la membrure.

<img alt="" src=images/CS_Airfoil.png  style="width:128px;"> 
*Coupe transversale de profil aérodynamique *

-   Cale. Le bord de fuite de l\'aileron est carré, convergeant vers un point du bord d\'attaque.

<img alt="" src=images/CS_Wedge.png  style="width:128px;"> 
*Section transversale forme de cale*

-   Diamant. La forme du losange commence à partir d\'un point sur le bord d\'attaque, directement jusqu\'à l\'épaisseur maximale en un point déterminé par **Length 1** et retourne à un point sur le bord de fuite.

<img alt="" src=images/CS_Diamond.png  style="width:128px;"> 
*Section transversale en diamant *

-   Cône du bord d\'attaque (LE). Le bord d\'attaque est effilé jusqu\'à un point déterminé par **Length 1**

<img alt="" src=images/LE_Taper.png  style="width:128px;"> 
*Coupe transversale conique du bord avant*

-   Cône du bord de fuite (TE). Le bord de fuite est effilé jusqu\'à un point déterminé par **Length 1**

<img alt="" src=images/TE_Taper.png  style="width:128px;"> 
*Coupe transversale effilée du bord arrière*

-   Biseau. Le bord avant est effilé jusqu\'à un point déterminé par **Length 1** et le bord arrière est effilé jusqu\'à un point déterminé par **Length 2**

<img alt="" src=images/CS_Taper.png  style="width:128px;"> 
*Section transversale biseautée*

### Attaches à travers le mur (TTW) 

À travers la paroi, les ailerons ajoutent une résistance structurelle en s\'étendant à travers le tube du corps externe jusqu\'à un tube du corps interne tel qu\'un support de moteur. Au lieu de se fixer uniquement à l\'extérieur du tube du corps extérieur, il peut être fixé en plusieurs points. En tant que telle, la hauteur de l\'attache serait la distance entre le diamètre extérieur du tube de corps interne et le diamètre externe du tube de corps externe. Les autres paramètres varient en fonction des besoins.
![](images/TTWx4.png ) 
*4 ailerons TTW fixées à un support du moteur central à l'intérieur du tube du corps externe*

## Propriétés


{{TitleProperty|Rocket Component}}

Ces paramètres sont fournis à titre indicatif et n\'ont aucun effet sur la conception du composant.

-    {{PropertyData/fr|Manufacturer}}: Fabricant lorsqu\'il est connu

-    {{PropertyData/fr|Part Number}}: Numéro de pièce du fabricant

-    {{PropertyData/fr|Description}}: Description du composant

-    {{PropertyData/fr|Material}}: Matériau lorsqu\'il est connu


{{TitleProperty|Coiffe}}

-    {{PropertyData/fr|Fin Type}}: Définit la forme de l\'aileron. Pour le moment, seules les aileron trapézoïdales sont pris en charge.

-    {{PropertyData/fr|Height}}: La hauteur de l\'aileron.

-    {{PropertyData/fr|Sweep Length}}: La distance entre l\'avant de la base de l\'aileron et l\'avant de la pointe de l\'aileron le long de l\'axe des x. Cela peut être négatif. Le réglage de cette valeur entraînera l\'ajustement de **Sweep Angle** .

-    {{PropertyData/fr|Sweep Angle}}: L\'angle de l\'avant de l\'aileron, avec un front vertical de 0 degré. Cela peut être négatif. Le réglage de cette valeur entraînera l\'ajustement de la **Sweep Length**.

-    {{PropertyData/fr|Fin Root Cross Section}}: La forme de la section transversale de l\'aileron à la base, voir [Options](#Options.md)

-    {{PropertyData/fr|Fin Root Chord}}: La distance entre les bords d\'attaque et de fuite des ailerons à la base

-    {{PropertyData/fr|Fin Root Thickness}}: Épaisseur maximale à la base de l\'aileron

-    {{PropertyData/fr|Fin Root Use Percentage}}: Exprime les propriétés **Fin Root Length 1** et **Fin Root Length 2** sous forme de pourcentage de **Fin Root Chord**

-    {{PropertyData/fr|Fin Root Length 1}}: L\'utilisation dépend de la **Fin Root Cross Section** et s\'appliquera à une longueur du biseau ou similaire, voir [Options](#Options.md)

-    {{PropertyData/fr|Fin Root Length 2}}: L\'utilisation dépend de la **Fin Root Cross Section** et s\'appliquera à une longueur du biseau ou similaire lorsque plusieurs valeurs sont requises, voir [Options](#Options.md)

-    {{PropertyData/fr|Fin Tip Cross Section}}: La forme de la section transversale de l\'aileron à l\'extrémité, voir [Options](#Options.md)

-    {{PropertyData/fr|Fin Tip Chord}}: La distance entre les bords d\'attaque et de fuite des ailerons à l\'extrémité

-    {{PropertyData/fr|Fin Tip Thickness}}: Épaisseur maximale à l\'extrémité de l\'aileron

-    {{PropertyData/fr|Fin Tip Use Percentage}}: Exprime les propriétés **Fin Tip Length 1** et **Fin Tip Length 2** sous forme de pourcentage de la **Fin Tip Chord**

-    {{PropertyData/fr|Fin Tip Length 1}}: L\'utilisation dépend de la **Fin Tip Cross Section** et s\'appliquera à une longueur du biseau ou similaire, voir [Options](#Options.md)

-    {{PropertyData/fr|Fin Tip Length 2}}: L\'utilisation dépend de la **Fin Tip Cross Section** et s\'appliquera à une longueur du biseau ou similaire lorsque plusieurs valeurs sont requises, voir [Options](#Options.md)

-    {{PropertyData/fr|TTW Tab}}: Vrai lorsqu\'une attache pour les ailettes à travers la paroi est requise, voir [Options](#Options.md)

-    {{PropertyData/fr|TTW Offset}}: Distance entre l\'avant de l\'aileron et l\'avant de l\'attache TTW

-    {{PropertyData/fr|TTW Length}}: Longueur de l\'attache TTW

-    {{PropertyData/fr|TTW Height}}: Hauteur de l\'attache TTW

-    {{PropertyData/fr|TTW Thickness}}: Epaisseur de l\'attache TTW

## Script

Voir aussi : [:<img src="images/Property.png" style="width:16px"> API/fr](:<img src="images/Property.png" style="width:16px"> API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

A définir

## Tutoriels et apprentissage 

[Aileron atelier Rocket](https://youtu.be/8MmEVyGkA0I) Tutoriel sur YouTube







[<img src="images/Property.png" style="width:16px"> Addons](Category_Addons.md) [<img src="images/Property.png" style="width:16px"> External Workbenches](Category_External_Workbenches.md)

---
[documentation index](../README.md) > [API/fr]] et ](Category_API/fr]] et .md) > Rocket Fin/fr
