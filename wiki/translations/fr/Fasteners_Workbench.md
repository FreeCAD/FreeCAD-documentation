# <img alt="Icône de l\'atelier externe Fasteners" src=images/Fasteners_workbench_icon.svg  style="width:64px;"> Fasteners Workbench/fr


{{TOCright}}

## Introduction

L\'<img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [atelier Fasteners](Fasteners_Workbench/fr.md) est un [atelier externe](External_workbenches/fr.md) qui permet d\'ajouter/fixer diverses fixations aux pièces.

## Utilisation

L\'utilisation est assez simple :

1.  Installez l\'atelier Fasteners via le <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md)
2.  Créez un nouveau document.
3.  Sélectionnez l\'<img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [atelier Fasteners](Fasteners_Workbench/fr.md) dans le [menu déroulant des ateliers](Std_Workbench/fr.md). La [barre d\'outils](#Barre_d.27outils.md) appartenant à l\'atelier sera affichée.

Utilisation simple : En cliquant sur l\'un des boutons de fixation, la fixation en question sera créée à l\'origine avec des propriétés par défaut. Pour modifier les propriétés d\'une fixation, sélectionnez-la et allez dans l\'onglet **Data** de l\'[Éditeur de propriétés](Property_editor/fr.md).

## Problèmes connus 

-   D\'autres problèmes/demandes de fonctionnalités sont disponibles dans la [file d\'attente GitHub des problèmes de l\'atelier Fasteners](https://github.com/shaise/FreeCAD_FastenersWB/issues?utf8=✓&q=is%3Aissue).

## Références

-   Auteur : [shaise](http://theseger.com/projects/author/shaise/)
    -   Concepteur d\'objets : Ulrich Brammer
    -   Architecture de l\'atelier : Shai Seger
-   Page d\'accueil : <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Code source sur github : <https://github.com/shaise/FreeCAD_FastenersWB>

## Installation

Cet atelier peut être installé à partir du <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md). Pour une installation manuelle, voir [Installer des ateliers supplémentaires](Installing_more_workbenches/fr.md).

## Barre d\'outils 

L\'atelier Fasteners comporte deux barres d\'outils. La barre d\'outils **FS Screws** contient de nombreux outils. Si nécessaire, elle peut être étendue en appuyant sur le bouton **&gt;&gt;**.

![](images/Fasteners_toolbars.png ) 
*Les barres d'outils de l'atelier Fasteners*

## Outils

Pour une description détaillée, voir [ici](http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/).

### Commandes

-   <img alt="" src=images/Fasteners_Flip.svg  style="width:32px;"> [Invert fastener](Fasteners_Flip/fr.md): inverser l\'orientation des fixations.

-   <img alt="" src=images/Fasteners_Move.svg  style="width:32px;"> [Move fastener](Fasteners_Move/fr.md) : déplacez la fixation vers un nouvel emplacement.

-   <img alt="" src=images/Fasteners_Shape.svg  style="width:32px;"> [Simplify shape](Fasteners_Shape/fr.md) : changer l\'objet en une forme simple non-paramétrique.

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:32px;"> [Match screws by inner thread diameter (Tap hole)](Fasteners_MatchTypeInner/fr.md) : faire correspondre les vis par diamètre de filetage intérieur (trou de taraudage).

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:32px;"> [Match screws by outer thread diameter (Pass hole)](Fasteners_MatchTypeOuter/fr.md) : faire correspondre les vis selon le diamètre du filetage extérieur (Trou de passage).

-   <img alt="" src=images/Fasteners_BOM.svg  style="width:32px;"> [Generate BOM](Fasteners_BOM/fr.md) : génère la nomenclature des fixations.

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:32px;"> [Screw calculator](Fasteners_ScrewCalculator/fr.md) : affiche un calculateur de trous de vis.

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:32px;"> [Make countersunk](Fasteners_ChamferHole/fr.md) : chanfreiner les trous pour les vis à tête fraisée.

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width:32px;"> [Change fastener parameters](Fasteners_ChangeParameters/fr.md) : change les paramètres des fixations sélectionnées.

### Fixations

**Remarque:** les fixations avec des dimensions métriques ont des icônes orange clair. Les fixations aux dimensions en pouces ont des icônes vertes.

#### Fixations autobloquantes et fixations pour PCB 

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width:32px;"> Ecrou métrique autobloquant.

-   <img alt="" src=images/Fasteners_PEMTHStandoff.svg  style="width:32px;"> Fixation métrique autobloquante.

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width:32px;"> Goujon métrique autobloquant.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width:32px;"> Fixation métrique **PCB** femelle/mâle.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width:32px;"> Entretoise métrique **PCB** Femelle/Femelle.

#### Fixations ISO, DIN et EN 

Les fixations ISO, DIN et EN ont des dimensions métriques.

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width:32px;"> 
**ISO 4017** Vis à tête hexagonale. *Catégories de produits A et B.*

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width:32px;"> 
**ISO 4014** Boulon à tête hexagonale. *Catégories de produits A et B.*

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width:32px;"> **EN 1662** Boulon à tête hexagonale avec embase, série étroite.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width:32px;"> **EN 1665** Boulon hexagonal avec embase, série large.

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width:32px;"> **ISO 4762** Vis à tête cylindrique à six pans creux.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width:32px;"> **DIN 7984** Vis à tête cylindrique à six pans creux à tête basse.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width:32px;"> **DIN 6912** Vis à tête cylindrique à six pans creux à tête basse avec téton de sécurité.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width:32px;"> **ISO 7380-1** Vis à tête ronde à six pans creux.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width:32px;"> **ISO 7380-2** Vis à tête ronde à six pans creux avec embase.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width:32px;"> **ISO 10642** Vis à tête fraisée à six pans creux.

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width:32px;"> **ISO 2009** Vis à tête plate fendue et fraisée. *Grade de produit A*.

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width:32px;"> **ISO 2010** Vis à tête fraisée surélevée fendue. *Grade de produit A*.

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width:32px;"> **ISO 1580** Vis à tête cylindrique fendue. *Grade de produit A*.

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width:32px;"> **ISO 1207** Vis à tête cylindrique fendue. *Grade de produit A*.

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width:32px;"> **DIN 967** Vis à tête cylindrique à empreinte cruciforme avec embase.

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width:32px;"> 
**ISO 7045** Vis à tête cylindrique bombée type H à empreinte cruciforme. *Grade du produit A.*

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width:32px;"> 
**ISO 7046** Vis à tête plate fraisée à empreinte cruciforme. *Grade du produit A.*

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width:32px;"> 
**ISO 7047** Vis à tête fraisée surélevée à empreinte cruciforme. *Grade du produit A.*

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width:32px;"> **ISO 7048** Vis à tête cylindrique avec évidement transversal de type H.

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width:32px;"> **ISO 14579** Vis à tête cylindrique à six pans creux.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width:32px;"> **ISO 14580**Vis à tête cylindrique à six pans creux.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width:32px;"> **ISO 14582** Vis à tête fraisée à six pans creux, tête haute.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width:32px;"> **ISO 14583** Vis à tête cylindrique à six pans creux.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width:32px;"> **ISO 14584** Vis à tête fraisée à six pans creux.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width:32px;"> **ISO 7379** Vis à épaulement à tête creuse hexagonale.

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width:32px;"> **ISO 7089** Rondelle plate, série normale. *Grade de produit A*.

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width:32px;"> **ISO 7090** Rondelle plate chanfreinée, série normale. *Grade de produit A*.

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width:32px;"> **ISO 7092** Rondelle plate, série étroite.

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width:32px;"> **ISO 7093-1** Rondelle plate, série large. *Grade du produit A*.

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width:32px;"> **ISO 7094** Rondelle plate, série très large.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width:32px;"> **ISO 4026** Vis sans tête à six pans creux à bout plat.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width:32px;"> **ISO 4027** Vis sans tête à six pans creux à bout tronconique.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width:32px;"> **ISO 4028** Vis sans tête à six pans creux à téton cylindrique.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width:32px;"> **ISO 4029** Vis sans tête à six pans creux à bout cuvette.

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width:32px;"> 
**ISO 4032** Écrou hexagonal, style 1. *Catégories de produits A et B.*

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width:32px;"> 
**ISO 4033** Écrou hexagonal, style 2. *Catégories de produits A et B.*

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width:32px;"> 
**ISO 4035** Écrou mince hexagonal, chanfreiné. *Catégories de produits A et B.*

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width:32px;"> **EN 1661** Écrou hexagonal avec embase.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width:32px;"> **DIN 557** Écrou carré.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width:32px;"> **DIN 562** Écrou carré.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width:32px;"> **DIN 985** Écrou Nylstop.

#### Fixations ASME 

Les fixations ASME ont des dimensions en pouces.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width:32px;"> **ASME B18.2.1.6** Vis à tête hexagonale UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width:32px;"> **ASME B18.2.1.8** Vis à tête hexagonale UNC avec bride.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width:32px;"> **ASME B18.2.2.1A** Écrou à vis mécanique UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width:32px;"> **ASME B18.2.2.4A** Écrou hexagonal UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width:32px;"> **ASME B18.2.2.4B** Écrou mince hexagonal UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width:32px;"> **ASME B18.3.1A** Vis à tête cylindrique à six pans creux UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width:32px;"> **ASME B18.3.2** Vis à tête fraisée à six pans creux UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width:32px;"> **ASME B18.3.3A** Vis à tête ronde à six pans creux UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width:32px;"> **ASME B18.3.3B** Vis à tête ronde à six pans creux UNC avec bride.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width:32px;"> **ASME B18.3.4** Vis à épaulement à tête creuse hexagonale UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width:32px;"> **ASME B18.3.5A** Vis à tête hexagonale UNC à bout plat.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width:32px;"> **ASME B18.3.5B** Vis à tête hexagonale UNC à bout tronconique.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width:32px;"> **ASME B18.3.5C** Vis sans tête à six pans creux UNC à téton.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width:32px;"> **ASME B18.3.5D** Vis à tête hexagonale UNC à bout cuvette.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width:32px;"> **ASME B18.6.3.1A** Vis à tête plate fendue et fraisée UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width:32px;"> **ASME B18.21.1.12A** Rondelle UN, série étroite.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width:32px;"> **ASME B18.21.1.12B** Rondelle UN, série normale.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width:32px;"> **ASME B18.21.1.12C** Rondelle UN, série large.

### Divers

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width:32px;"> Tige filetée de longueur personnalisée pour le taraudage des trous (métrique).

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width:32px;"> Tige filetée de longueur personnalisée pour le taraudage des trous (pouce).

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width:32px;"> Tube fileté de longueur personnalisée pour couper les filets extérieurs (métrique).

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width:32px;"> Tube fileté de longueur personnalisée pour couper les filets extérieurs (pouce).

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width:32px;"> Tige filetée *DIN 975* de longueur arbitraire (métrique).

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width:32px;"> Tige filetée *UNC* de longueur arbitraire (pouce).

## Autres

-   <img alt="" src=images/preferences-fasteners.svg  style="width:32px;"> 
**Préférences Fasteners**
-   <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:32px;"> 
**Icône Fasteners**

## Liens relatifs à l\'atelier 

-   Wiki de l\'atelier : <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Wiki FreeCAD : <https://www.freecadweb.org/wiki/Fasteners_Workbench>
-   Forum FreeCAD : <https://forum.freecadweb.org/viewtopic.php?t=11429>
-   Tutoriels - Comment utiliser : <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Vidéos :
-   Fichiers :
-   Rapporter les bugs : SVP rapporter les bugs sur <https://github.com/shaise/FreeCAD_FastenersWB/issues>
-   Installation : <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>

## Autres liens 

-   [Génération de trous pour vis à tête fraisée dans freecad (en)](http://theseger.com/projects/2015/07/generating-holes-for-countersunk-screws-in-freecad/)
-   [BOLTS](https://github.com/jreinhardt/BOLTS): une librairie ouverte pour les spécifications techniques
-   [Ateliers externes](External_workbenches/fr.md)
-   [Macros](Macros_recipes/fr.md)



_ _ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > Fasteners Workbench/fr
