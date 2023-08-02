---
- GuiCommand:
   Name: Rocket Fin
   Name/fr: Rocket Aileron
   MenuLocation: Rocket -> Fin
   Workbenches: Rocket_Workbench/fr
   Version: 0.19
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
    -   Double-cliquez sur un objet Fin dans la [Vue en arborescence](Tree_view/fr.md).
2.  Définissez les options et appuyez sur **OK**.

## Options

### Type d\'aileron 

La forme générale de l\'aileron.

-   Trapézoïde.

Ce type d\'aileron est utilisé pour presque tous les ailettes à 4 côtés. L\'emplanture reste fixe, mais les bords d\'attaque et de fuite peuvent avoir des valeurs de flèche variables. La longueur de corde de l\'emplanture et de la pointe sont réglées indépendamment.

<img alt="" src=images/Fin_Trapezoid_small.png  style="width:128px;"> 
*Type d'aileron trapézoïdal*

-   Elliptique.

Une forme arrondie généralisée. Les ailerons circulaires sont un cas particulier où la hauteur est égale à la moitié de la corde d\'emplanture.

<img alt="" src=images/Fin_Elliptical_small.png  style="width:128px;"> 
*Type d'aileron elliptique*

-   Personnalisé.

La plupart des ailerons s\'adaptent à l\'une des formes standards. Si ce n\'est pas le cas, il est possible de créer une forme personnalisée à l\'aide d\'une esquisse.

L\'esquisse doit d\'abord être créée. La racine de l\'aileron est dessinée le long de l\'axe X positif. Une fois l\'esquisse sélectionnée dans l\'arborescence du modèle, la sélection de l\'icône Fin permet de créer l\'aileron personnalisé. Le profil de l\'aileron peut être modifié à ce stade.

Il n\'y a aucun moyen d\'associer un aileron personnalisé à une esquisse dans la boîte de dialogue après sa création, il est donc important de créer d\'abord l\'esquisse. Il peut être sélectionné dans la vue Propriétés. La mise à jour de l\'esquisse entraîne celle de l\'aileron.

<img alt="" src=images/Fin_Sketch_small.png  style="width:128px;"> 
*Esquisse utilisée pour créer une forme d'aileron personnalisée* <img alt="" src=images/Fin_Custom_small.png  style="width:128px;"> 
*L'aileron personnalisé créé à partir d'une esquisse*

### Section transversale 

La forme en coupe d\'un aileron peut grandement affecter ses performances à différentes vitesses, ainsi que l\'apparence de la fusée. Diverses sections transversales des ailettes ont été mises en œuvre. Les ailettes sont créées en lissant la section transversale de la base jusqu\'à la section transversale de la pointe, de sorte que toutes les combinaisons de **Section transversale de la base** et **Section transversale de pointe** ne produiront pas d\'ailerons utiles.

-   Carré. Les bords avant et arrière sont au carré.

<img alt="" src=images/CS_Square.png  style="width:128px;"> 
*Coupe transversale carrée *

-   Rond. Les bords d\'attaque et de fuite sont arrondis.

<img alt="" src=images/CS_Round.png  style="width:128px;"> 
*Coupe transversale ronde*

-   Profil aérodynamique. Utilise la forme aérodynamique symétrique du [Profil NACA](https://fr.wikipedia.org/wiki/Profil_NACA) avec une épaisseur maximale à 30% de la membrure.

<img alt="" src=images/CS_Airfoil.png  style="width:128px;"> 
*Coupe transversale de profil aérodynamique*

-   Cale. Le bord de fuite de l\'aileron est carré, convergeant vers un point du bord d\'attaque.

<img alt="" src=images/CS_Wedge.png  style="width:128px;"> 
*Section transversale forme de cale*

-   Diamant. La forme du losange commence à partir d\'un point sur le bord d\'attaque, directement jusqu\'à l\'épaisseur maximale en un point déterminé par **Length 1** et retourne à un point sur le bord de fuite.

<img alt="" src=images/CS_Diamond.png  style="width:128px;"> 
*Section transversale en diamant*

-   Cône du bord d\'attaque (LE). Le bord d\'attaque est effilé jusqu\'à un point déterminé par **Length 1**.

<img alt="" src=images/LE_Taper.png  style="width:128px;"> 
*Coupe transversale conique du bord avant*

-   Cône du bord de fuite (TE). Le bord de fuite est effilé jusqu\'à un point déterminé par **Length 1**.

<img alt="" src=images/TE_Taper.png  style="width:128px;"> 
*Coupe transversale effilée du bord arrière*

-   Biseau. Le bord avant est effilé jusqu\'à un point déterminé par **Length 1** et le bord arrière est effilé jusqu\'à un point déterminé par **Length 2**.

<img alt="" src=images/CS_Taper.png  style="width:128px;"> 
*Section transversale biseautée*

### Attaches à travers la paroi 

Les ailerons à travers la paroi (Through the Wall = TTW) ajoutent une résistance structurelle en s\'étendant à travers le tube du corps externe jusqu\'à un tube du corps interne tel qu\'un support de moteur. Au lieu de se fixer uniquement à l\'extérieur du tube du corps extérieur, ils peuvent être fixés en plusieurs points. En tant que telle, la hauteur de l\'attache serait la distance entre le diamètre extérieur du tube de corps interne et le diamètre externe du tube de corps externe. Les autres paramètres varient en fonction des besoins.

![](images/TTWx4.png ) 
*4 ailerons TTW fixées à un support du moteur central à l'intérieur du tube du corps externe*

## Propriétés


{{TitleProperty|Fin}}

-    **Fin Type**: Définit la forme de l\'aileron.

-    **Height**: La hauteur de l\'aileron.

-    **Profile**: L\'esquisse associée au type d\'aileron personnalisé.

-    **Root Chord**: La distance entre le bord d\'attaque et le bord de fuite de l\'aileron à la racine.

-    **Root Cross Section**: La forme de la section transversale de l\'aileron à l\'emplanture, voir [Options](#Options.md).

-    **Root Length 1**: L\'utilisation dépend de **Fin Root Cross Section** et s\'appliquera à une longueur conique ou similaire, voir [Options](#Options.md).

-    **Root Length 2**: L\'utilisation dépend de **Fin Root Cross Section** et s\'appliquera à une longueur conique ou similaire lorsque plusieurs valeurs sont requises, voir [Options](#Options.md).

-    **Root Per Cent**: Exprime les propriétés **Fin Root Length 1** et **Fin Root Length 2** en pourcentage de la **Fin Root Chord**.

-    **Root Thickness**: Epaisseur maximale à la base de l\'aileron

-    **Sweep Angle**: L\'angle de l\'avant de l\'aileron, un avant vertical étant égal à 0 degré. Cette valeur peut être négative. Le réglage de cette valeur entraînera l\'ajustement de **Sweep Length**.

-    **Sweep Length**: La distance entre l\'avant de l\'emplanture de l\'aileron et l\'avant de l\'extrémité de l\'aileron le long de l\'axe x. Cette valeur peut être négative. Cette valeur peut être négative. Si vous définissez cette valeur, **Sweep Angle** sera ajusté.

-    **Tip Chord**: La distance entre le bord d\'attaque et le bord de fuite de l\'aileron à l\'extrémité.

-    **Tip Cross Section**: La forme de la section transversale de l\'aileron à l\'extrémité, voir [Options](#Options.md).

-    **Tip Length 1**: L\'utilisation dépend de la **Fin Tip Cross Section** et s\'applique à une longueur conique ou similaire, voir [Options](#Options.md).

-    **Tip Length 2**: L\'utilisation dépend de la **Fin Tip Cross Section** et s\'appliquera à une longueur conique ou similaire lorsque plusieurs valeurs sont requises, voir [Options](#Options.md).

-    **Tip Per Cent**: Exprime les propriétés **Fin Tip Length 1** et **Fin Tip Length 2** en pourcentage de la **Fin Tip Chord**.

-    **Tip Thickness**: Epaisseur maximale à l\'extrémité de l\'aileron

-    **Ttw**: Vrai lorsqu\'une attache pour les ailerons Through the Wall est requis, voir [Options](#Options.md).

-    **Ttw Height**: Hauteur de l\'attache TTW

-    **Ttw Length**: Longueur de l\'attache TTW

-    **Ttw Offset**: Distance entre l\'avant de l\'aileron et l\'avant de l\'attache TTW.

-    **Ttw Thickness**: Epaisseur de l\'attache TTW


{{TitleProperty|Rocket Component}}

Ces paramètres sont fournis à titre indicatif et n\'ont aucun effet sur la conception du composant.

-    **Description**: Description du composant

-    **Manufacturer**: Fabricant lorsqu\'il est connu

-    **Material**: Matériau lorsqu\'il est connu

-    **Part Number**: Numéro de pièce du fabricant

## Tutoriels et apprentissage 

[Aileron atelier Rocket](https://youtu.be/8MmEVyGkA0I) Tutoriel sur YouTube



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Rocket Fin/fr
