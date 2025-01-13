# <img alt="Icône de l\'atelier externe Fasteners" src=images/Fasteners_workbench_icon.svg  style="width:64px;"> Fasteners Workbench/fr






## Introduction

L\'<img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [atelier Fasteners](Fasteners_Workbench/fr.md) est un [atelier externe](External_workbenches/fr.md) qui permet d\'ajouter diverses fixations aux pièces.

<img alt="" src=images/Fasteners_Toolbars.png  style="width:500px;"> 
*La barre d'outils unique optionnelle de l'atelier.<br>
Les fixations à dimensions métriques ont des icônes orange.<br>
Les fixations dont les dimensions sont en pouces ont des icônes vertes.*



## Installation

1.  Installer l\'atelier Fasteners via le <img alt="" src=images/AddonManager.svg  style="width:24px;"> [gestionnaire des extensions](Std_AddonMgr/fr.md). Pour une installation manuelle, voir [Installer des ateliers supplémentaires](Installing_more_workbenches/fr.md).
2.  Redémarrer FreeCAD.
3.  Créer un nouveau document.
4.  Sélectionner l\'<img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [atelier Fasteners](Fasteners_Workbench/fr.md) dans le [sélecteur d\'atelier](Std_Workbench/fr.md).
5.  Vous pouvez modifier la barre d\'outils et la disposition du menu :
    1.  Allez à : **Édition → Préférences... → Fasteners → General settings**.
    2.  Sélectionner l\'une des options disponibles de **Groupement des icônes de vis** :
        -   
            **Rien**
            
            : toutes les fixations apparaissent dans une seule barre d\'outils. Pour voir tous les boutons disponibles, utilisez le bouton **&gt;&gt;** pour la développer.

        -   
            **Barres d'outils séparées**
            
            : les fixations sont regroupées dans plusieurs barres d\'outils. Il s\'agit de la disposition par défaut.

        -   
            **Boutons déroulants**
            
            : les fixations sont regroupées dans des barres d\'outils avec des boutons déroulants.
    3.  Vous pouvez décocher une ou plusieurs options du panneau **Les normes de fixation sont indiquées dans les barres d'outils**. Les options de standard non cochées sont toujours disponibles dans le menu.
    4.  Redémarrez FreeCAD.



## Utilisation

Les fixations peuvent être attachées ou non attachées. Les fixations attachées ont une **Base Object**, un bord circulaire, et leur **Placement** est dynamiquement lié à cet objet. La commande <img alt="" src=images/Fasteners_Move.svg  style="width:16px;"> [Fasteners Déplacer](Fasteners_Move/fr.md) peut être utilisée pour fixer ou détacher une fixation.



### Fixations non attachées 

1.  Sélectionner la fixation souhaitée en cliquant sur son bouton ou en la choisissant dans le menu.
2.  Une fixation est créée à l\'origine.
3.  Vous pouvez modifier les dimensions et les autres propriétés de la fixation :
    1.  Sélectionner la fixation.
    2.  Aller dans l\'onglet **Data** de l\'[éditeur de propriétés](Property_editor/fr.md).
    3.  Modifier les propriétés requises.



### Fixations attachées 

<img alt="" src=images/Fasteners_Attached_Selected.png  style="width:200px;"> <img alt="" src=images/Fasteners_Attached_Created.png  style="width:200px;"> 
*À gauche, deux bords circulaires sélectionnés. À droite, les fixations attachées.*

1.  Sélectionner des trous comme trous de taraudage ou trous de passage en sélectionnant <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:16px;"> [Fasteners Adapter pour le trou taraudé](Fasteners_MatchTypeInner/fr.md) ou <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:16px;"> [Fasteners Adapter pour le trou de passage](Fasteners_MatchTypeOuter/fr.md) respectivement (non utilisé pour les vis à tête fraisée).
2.  Sélectionner une ou plusieurs arêtes circulaires et/ou faces avec des arêtes circulaires. Pour les vis fraisées, le bord supérieur du trou chanfreiné doit être sélectionné.
3.  Sélectionner la fixation souhaitée en cliquant sur son bouton ou en la choisissant dans le menu.
4.  Une fixation est attachée à chacun de ses points sélectionnés.
5.  Les dimensions par défaut de chaque fixation dépendent du rayon du bord circulaire sur lequel elle est fixée. Les vis à tête fraisée sont assorties au diamètre de leur tête, les autres fixations sont assorties au diamètre de leur tige.
6.  Vous pouvez également modifier les dimensions et les autres propriétés des fixations. Voir ci-dessus.
7.  Les fixations qui apparaissent à l\'envers peuvent être inversées avec la commande <img alt="" src=images/Fasteners_Flip.svg  style="width:16px;"> [Inverser la fixation](Fasteners_Flip/fr.md) ou en modifiant leur propriété **Invert**.
8.  Vous pouvez changer la propriété **Offset** pour créer un espace entre les fixations et les bords auxquels elles sont attachées.



## Remarques

-   Pour générer des filetages, la propriété **Thread** d\'une fixation doit être changée en `True`. La génération de filetages est coûteuse. Les recalculs prennent beaucoup plus de temps s\'il y a beaucoup de fixations avec des filetages dans un document.
-   La propriété **Invert** et la propriété **Offset** sont ignorées pour les fixations non attachées.



## Commandes

-   <img alt="" src=images/Fasteners_Flip.svg  style="width:32px;"> [Inverser la fixation](Fasteners_Flip/fr.md) : inverse l\'orientation des fixations attachées.

-   <img alt="" src=images/Fasteners_Move.svg  style="width:32px;"> [Déplacer la fixation](Fasteners_Move/fr.md) : déplace et fixe une fixation sur un bord circulaire. Peut également être utilisé pour détacher une fixation.

-   <img alt="" src=images/Fasteners_Simplify.svg  style="width:32px;"> [Simplifier la forme](Fasteners_Simplify/fr.md) : crée des copies non paramétriques des fixations.

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:32px;"> [Adapter pour le trou taraudé](Fasteners_MatchTypeInner/fr.md) : prend les bords circulaires comme des trous à fileter lorsque de nouvelles fixations y sont attachées.

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:32px;"> [Adapter pour le trou de passage](Fasteners_MatchTypeOuter/fr.md) : prend les bords circulaires comme des trous de passage lorsque de nouvelles fixations y sont attachées.

-   <img alt="" src=images/Fasteners_BOM.svg  style="width:32px;"> [Nomenclature](Fasteners_BOM/fr.md) : crée une feuille de calcul avec une nomenclature pour les fixations du document.

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:32px;"> [Calculateur de trous de vis](Fasteners_ScrewCalculator/fr.md) : affiche une calculatrice pour déterminer la taille des trous de vis.

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width:32px;"> [Paramètres de la fixation](Fasteners_ChangeParameters/fr.md) : change les paramètres des fixations.



## Fixations

Les fixations avec des dimensions métriques ont des icônes orange. Les fixations aux dimensions en pouces ont des icônes vertes.



### Vis et boulons à tête hexagonale 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width:32px;"> **ASME B18.2.1.6** Vis à tête hexagonale UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width:32px;"> **ASME B18.2.1.8** Vis à tête hexagonale UNC avec bride.

-   <img alt="" src=images/Fasteners_DIN571.svg  style="width:32px;"> **DIN 571** Tirefond vis à bois à tête hexagonale.

-   <img alt="" src=images/Fasteners_DIN933.svg  style="width:32px;"> **DIN 933** Vis à tête hexagonale.

-   <img alt="" src=images/Fasteners_DIN961.svg  style="width:32px;"> **DIN 961** Vis à tête hexagonale.

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width:32px;"> **EN 1662** Boulon à tête hexagonale avec embase, série étroite.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width:32px;"> **EN 1665** Boulon à tête hexagonale avec embase, série large.

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width:32px;"> 
**ISO 4014** Boulon à tête hexagonale. *Grades A et B.*

-   <img alt="" src=images/Fasteners_ISO4015.svg  style="width:32px;"> **ISO 4015** Boulon à tête hexagonale avec tige réduite.

-   <img alt="" src=images/Fasteners_ISO4016.svg  style="width:32px;"> 
**ISO 4016** Boulon à tête hexagonale. *Grade C.*

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width:32px;"> 
**ISO 4017** Vis à tête hexagonale. *Grades A et B.*

-   <img alt="" src=images/Fasteners_ISO4018.svg  style="width:32px;"> 
**ISO 4018** Vis à tête hexagonale. *Grade C.*

-   <img alt="" src=images/Fasteners_ISO4162.svg  style="width:32px;"> 
**ISO 4162** Boulon hexagonal à embase cylindro-tronconique, série étroite. *Grade A avec entraînement de grade B.*

-   <img alt="" src=images/Fasteners_ISO8676.svg  style="width:32px;"> 
**ISO 8676** Vis à tête hexagonale à filetage métrique à pas fin entièrement filetées. *Grades A et B.*

-   <img alt="" src=images/Fasteners_ISO8765.svg  style="width:32px;"> **ISO 8765** Vis à tête hexagonale partiellement filetées, à pas fin.

-   <img alt="" src=images/Fasteners_ISO15071.svg  style="width:32px;"> 
**ISO 15071** Vis à tête hexagonale à embase cylindro-tronconique, série étroite. *Grade A*

-   <img alt="" src=images/Fasteners_ISO15072.svg  style="width:32px;"> 
**ISO 15072** Vis à tête hexagonale à embase cylindro-tronconique, à filetage métrique à pas fin, série étroite. *Grade A.*



### Vis à six pans creux 

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width:32px;"> **ASME B18.3.1A** Vis à tête cylindrique à six pans creux UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1G.svg  style="width:32px;"> **ASME B18.3.1G** Vis à tête cylindrique à six pans creux UNC à tête basse.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width:32px;"> **ASME B18.3.2** Vis à tête fraisée à six pans creux UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width:32px;"> **ASME B18.3.3A** Vis à tête ronde à six pans creux UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width:32px;"> **ASME B18.3.3B** Vis à tête ronde à six pans creux UNC avec bride.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width:32px;"> **ASME B18.3.4** Vis à épaulement à tête creuse hexagonale UNC.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width:32px;"> **DIN 6912** Vis à tête cylindrique à six pans creux à tête basse avec téton de sécurité.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width:32px;"> **DIN 7984** Vis à tête cylindrique à six pans creux à tête basse.

-   <img alt="" src=images/Fasteners_ISO2936.svg  style="width:32px;"> **ISO 2936** Clé pour vis à six pans creux.

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width:32px;"> **ISO 4762** Vis à tête cylindrique à six pans creux.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width:32px;"> **ISO 7379** Vis à épaulement à six pans creux.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width:32px;"> **ISO 7380-1** Vis à tête ronde à six pans creux.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width:32px;"> **ISO 7380-2** Vis à tête ronde à six pans creux avec embase.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width:32px;"> **ISO 10642** Vis à tête fraisée à six pans creux.



### Vis à tête creuse torx 

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width:32px;"> **ISO 14579** Vis à métaux tête cylindrique torx.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width:32px;"> **ISO 14580** Vis à métaux tête cylindrique basse torx.

-   <img alt="" src=images/Fasteners_ISO14581.svg  style="width:32px;"> **ISO 14581** Vis à tête fraisée réduite à six lobes internes.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width:32px;"> **ISO 14582** Vis à tête fraisée à six pans creux, tête haute.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width:32px;"> **ISO 14583** Vis à tête cylindrique à six pans creux.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width:32px;"> **ISO 14584** Vis à tête fraisée à six pans creux.



### Vis à tête fendue 

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.2.svg  style="width:32px;"> **ASME B18.6.1.2** Vis à bois à tête fraisée plate et fendue.

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.4.svg  style="width:32px;"> **ASME B18.6.1.4** Vis à bois à tête fraisée ovale et fendue.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width:32px;"> **ASME B18.6.3.1A** Vis à tête plate fendue et fraisée UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.4A.svg  style="width:32px;"> **ASME B18.6.3.4A** Vis à tête fraisée ovale et fendue UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.9A.svg  style="width:32px;"> **ASME B18.6.3.9A** Vis à tête cylindrique fendue UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.10A.svg  style="width:32px;"> **ASME B18.6.3.10A** Vis à tête cylindrique ovale fendue UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.12A.svg  style="width:32px;"> **ASME B18.6.3.12A** Vis à tête bombée fendue UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.16A.svg  style="width:32px;"> **ASME B18.6.3.16A** Vis à tête ronde fendue UNC.

-   <img alt="" src=images/Fasteners_DIN84.svg  style="width:32px;"> 
**DIN 84 (remplacée par ISO 1207)** Vis à tête cylindrique fendue. *Grade A.*

-   <img alt="" src=images/Fasteners_DIN96.svg  style="width:32px;"> **DIN 96** Vis à bois à tête demi-ronde fendue.

-   <img alt="" src=images/Fasteners_GOST1144-1.svg  style="width:32px;"> **GOST 1144-1** Vis à bois à tête demi-ronde fendue.

-   <img alt="" src=images/Fasteners_GOST1144-2.svg  style="width:32px;"> **GOST 1144-2** Vis à bois à tête demi-ronde fendue.

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width:32px;"> **ISO 1207** Vis à tête cylindrique fendue. *Grade A*.

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width:32px;"> **ISO 1580** Vis à tête cylindrique fendue. *Grade A*.

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width:32px;"> **ISO 2009** Vis à tête plate fendue et fraisée. *Grade A*.

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width:32px;"> **ISO 2010** Vis à tête fraisée surélevée fendue. *Grade A*.



### Vis type H à tête cruciforme 

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.3.svg  style="width:32px;"> **ASME B18.6.1.3** Vis à bois à tête fraisée plate.

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.5.svg  style="width:32px;"> **ASME B18.6.1.5** Vis à bois à tête fraisée ovale.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1B.svg  style="width:32px;"> **ASME B18.6.3.1B** Vis à tête fraisée plate UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.4B.svg  style="width:32px;"> **ASME B18.6.3.4B** Vis à tête fraisée ovale UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.9B.svg  style="width:32px;"> **ASME B18.6.3.9B** Vis à tête cylindrique UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.10B.svg  style="width:32px;"> **ASME B18.6.3.10B** Vis à tête cylindrique bombée UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.12C.svg  style="width:32px;"> **ASME B18.6.3.12C** Vis à tête bombée UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.16B.svg  style="width:32px;"> **ASME B18.6.3.16B** Vis à tête ronde UNC.

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width:32px;"> **DIN 967** Vis à tête cylindrique avec collerette.

-   <img alt="" src=images/Fasteners_DIN7996.svg  style="width:32px;"> **DIN 7996** Vis à bois à tête cylindrique.

-   <img alt="" src=images/Fasteners_GOST1144-3.svg  style="width:32px;"> **GOST 1144-3** Vis à bois à tête cylindrique.

-   <img alt="" src=images/Fasteners_GOST1144-4.svg  style="width:32px;"> **GOST 1144-4** Vis à bois à tête cylindrique.

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width:32px;"> 
**ISO 7045** Vis à tête cylindrique bombée. *Grade A.*

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width:32px;"> 
**ISO 7046** Vis à tête plate fraisée. *Grade A.*

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width:32px;"> 
**ISO 7047** Vis à tête fraisée surélevée. *Grade A.*

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width:32px;"> **ISO 7048** Vis à tête cylindrique bombée réduite.

-   <img alt="" src=images/Fasteners_ISO7049-C.svg  style="width:32px;"> **ISO 7049-C** Vis autotaraudeuses à tête cylindrique à pointe conique.

-   <img alt="" src=images/Fasteners_ISO7049-F.svg  style="width:32px;"> **ISO 7049-F** Vis autotaraudeuses à tête cylindrique avec pointe plate.

-   <img alt="" src=images/Fasteners_ISO7049-R.svg  style="width:32px;"> **ISO 7049-R** Vis autotaraudeuses à tête cylindrique avec pointe arrondie.



### Autres têtes de boulon 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.1.svg  style="width:32px;"> **ASME B18.2.1.1** Boulon à tête carrée UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.5.2.svg  style="width:32px;"> **ASME B18.5** Boulon à tête carrée - boulon de carrosserie.

-   <img alt="" src=images/Fasteners_DIN478.svg  style="width:32px;"> **DIN 478** Boulon à tête carrée avec collerette.

-   <img alt="" src=images/Fasteners_DIN603.svg  style="width:32px;"> **DIN 603** Boulon à tête carrée - boulon de carrosserie.

-   <img alt="" src=images/Fasteners_ISO2342.svg  style="width:32px;"> **ISO 2342** Vis sans tête fendue, à fût.



### Vis de réglage 

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width:32px;"> **ASME B18.3.5A** Vis à tête hexagonale UNC à bout plat.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width:32px;"> **ASME B18.3.5B** Vis à tête hexagonale UNC à bout tronconique.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width:32px;"> **ASME B18.3.5C** Vis sans tête à six pans creux UNC à téton.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width:32px;"> **ASME B18.3.5D** Vis à tête hexagonale UNC à bout cuvette.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width:32px;"> **ISO 4026** Vis sans tête à six pans creux à bout plat.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width:32px;"> **ISO 4027** Vis sans tête à six pans creux à bout tronconique.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width:32px;"> **ISO 4028** Vis sans tête à six pans creux à téton cylindrique.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width:32px;"> **ISO 4029** Vis sans tête à six pans creux à bout cuvette.

-   <img alt="" src=images/Fasteners_ISO4766.svg  style="width:32px;"> **ISO 4766** Vis à tête fendue à pointe plate.

-   <img alt="" src=images/Fasteners_ISO7434.svg  style="width:32px;"> **ISO 7434** Vis à tête fendue à pointe conique.

-   <img alt="" src=images/Fasteners_ISO7435.svg  style="width:32px;"> **ISO 7435** Vis à tête fendue à pointe longue.

-   <img alt="" src=images/Fasteners_ISO7436.svg  style="width:32px;"> **ISO 7436** Vis à tête fendue à bout cuvette.



### Vis moletées 

-   <img alt="" src=images/Fasteners_DIN464.svg  style="width:32px;"> **DIN 464** Vis moletée épaulée, forme haute.

-   <img alt="" src=images/Fasteners_DIN465.svg  style="width:32px;"> **DIN 465** Vis moletée épaulée fendue, forme haute.

-   <img alt="" src=images/Fasteners_DIN653.svg  style="width:32px;"> **DIN 653** Vis moletée épaulée, forme basse.



### Écrous

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width:32px;"> **ASME B18.2.2.1A** Écrou hexagonal filetage UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1B.svg  style="width:32px;"> **ASME B18.2.2.1B** Écrou carré filetage UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.2.svg  style="width:32px;"> **ASME 18.2.2.2** Écrou carré UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width:32px;"> **ASME B18.2.2.4A** Écrou hexagonal UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width:32px;"> **ASME B18.2.2.4B** Écrou mince hexagonal UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.5.svg  style="width:32px;"> **ASME 18.2.2.5** Écrou hexagonal à créneaux UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.12.svg  style="width:32px;"> **ASME 18.2.2.12** Écrou hexagonal avec embase UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.13.svg  style="width:32px;"> **ASME 18.2.2.13** Écrou de rallonge hexagonal UNC.

-   <img alt="" src=images/Fasteners_ASMEB18.6.9A.svg  style="width:32px;"> **ASME 18.6.9A** Écrou à oreilles, type A.

-   <img alt="" src=images/Fasteners_DIN315.svg  style="width:32px;"> **DIN 315** Écrou à oreilles.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width:32px;"> **DIN 557** Écrou carré.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width:32px;"> **DIN 562** Écrou carré.

-   <img alt="" src=images/Fasteners_DIN917.svg  style="width:32px;"> **DIN 917** Écrou borgne, forme basse.

-   <img alt="" src=images/Fasteners_DIN928.svg  style="width:32px;"> **DIN 928** Écrou à souder carré

-   <img alt="" src=images/Fasteners_DIN929.svg  style="width:32px;"> **DIN 929** Écrou hexagonal à souder.

-   <img alt="" src=images/Fasteners_DIN934.svg  style="width:32px;"> 
**DIN 934 (remplacé par ISO 4035 et ISO 8673)** Écrou mince hexagonal, chanfreiné. *Grades A et B.*

-   <img alt="" src=images/Fasteners_DIN935.svg  style="width:32px;"> **DIN 935** Écrou hexagonal à créneaux.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width:32px;"> **DIN 985** Écrou Nylstop.

-   <img alt="" src=images/Fasteners_DIN1587.svg  style="width:32px;"> **DIN 1587** Écrou borgne.

-   <img alt="" src=images/Fasteners_DIN6330.svg  style="width:32px;"> **DIN 6330** Écrou hexagonal de 1,5d de haut.

-   <img alt="" src=images/Fasteners_DIN6331.svg  style="width:32px;"> **DIN 6331** Écrou hexagonal avec collier de 1,5d de haut.

-   <img alt="" src=images/Fasteners_DIN6334.svg  style="width:32px;"> **DIN 6334** Écrou de rallonge hexagonal.

-   <img alt="" src=images/Fasteners_DIN7967.svg  style="width:32px;"> **DIN 7967** Écrou PAL auto-freinés.

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width:32px;"> **EN 1661** Écrou hexagonal avec embase.

-   <img alt="" src=images/Fasteners_GOST11860-1.svg  style="width:32px;"> **GOST 11860-1** Écrou borgne.

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width:32px;"> 
**ISO 4032** Écrou hexagonal, style 1. *Grades A et B.*

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width:32px;"> 
**ISO 4033** Écrou hexagonal, style 2. *Grades A et B.*

-   <img alt="" src=images/Fasteners_ISO4034.svg  style="width:32px;"> **ISO 4034** Écrou hexagonal, style 1.

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width:32px;"> 
**ISO 4035** Écrou mince hexagonal, chanfreiné. *Grades A et B.*

-   <img alt="" src=images/Fasteners_ISO4161.svg  style="width:32px;"> **ISO 4161** Écrou hexagonal à embase cylindro-tronconique, style 2, filetage à pas gros.

-   <img alt="" src=images/Fasteners_ISO7040.svg  style="width:32px;"> **ISO 7040** Écrou hexagonal normal autofreiné (à anneau non métallique)

-   <img alt="" src=images/Fasteners_ISO7041.svg  style="width:32px;"> **ISO 7041** Écrou hexagonal autofreiné (à anneau non métallique), style 2.

-   <img alt="" src=images/Fasteners_ISO7043.svg  style="width:32px;"> **ISO 7043** Écrou hexagonal à embase, autofreiné (à anneau non métallique), style 2.

-   <img alt="" src=images/Fasteners_ISO7044.svg  style="width:32px;"> **ISO 7044** Écrou hexagonal à embase, autofreiné, tout métal, style 2.

-   <img alt="" src=images/Fasteners_ISO7719.svg  style="width:32px;"> **ISO 7719** Écrou hexagonal normal autofreiné, tout métal.

-   <img alt="" src=images/Fasteners_ISO7720.svg  style="width:32px;"> **ISO 7720** Écrou hexagonal autofreiné, tout métal, style 2.

-   <img alt="" src=images/Fasteners_ISO8673.svg  style="width:32px;"> 
**ISO 8673** Écrous hexagonaux normaux (style 1) à filetage métrique à pas fin. *Grades A et B.*

-   <img alt="" src=images/Fasteners_ISO8674.svg  style="width:32px;"> 
**ISO 8674** Écrous hexagonaux hauts (style 2) à filetage métrique à pas fin. *Grades A et B.*

-   <img alt="" src=images/Fasteners_ISO8675.svg  style="width:32px;"> 
**ISO 8675** Écrous bas hexagonaux chanfreinés (style 0) à filetage métrique à pas fin. *Grades A et B.*

-   <img alt="" src=images/Fasteners_ISO10511.svg  style="width:32px;"> **ISO 10511** Écrou hexagonal bas autofreiné (à anneau non métallique).

-   <img alt="" src=images/Fasteners_ISO10512.svg  style="width:32px;"> **ISO 10512** Écrou hexagonal normal autofreiné (à anneau non métallique) à filetage métrique à pas fin.

-   <img alt="" src=images/Fasteners_ISO10513.svg  style="width:32px;"> **ISO 10513** Écrou hexagonal haut autofreiné, tout métal, à filetage métrique à pas fin.

-   <img alt="" src=images/Fasteners_ISO10663.svg  style="width:32px;"> **ISO 10663** Écrou hexagonal à embase cylindro-tronconique, style 2, filetage à pas fin.

-   <img alt="" src=images/Fasteners_ISO12125.svg  style="width:32px;"> **ISO 12125** Écrou hexagonal à embase, autofreiné (à anneau non métallique), à filetage métrique à pas fin, style 2.

-   <img alt="" src=images/Fasteners_ISO12126.svg  style="width:32px;"> **ISO 12126** Écrou hexagonal à embase, autofreiné, tout métal, à filetage métrique à pas fin, style 2.

-   <img alt="" src=images/Fasteners_ISO21670.svg  style="width:32px;"> **ISO 21670** Écrou hexagonal à souder, à embase plate.

-   <img alt="" src=images/Fasteners_SAEJ483a1.svg  style="width:32px;"> **SAE J483a 1** Écrou borgne, forme basse.

-   <img alt="" src=images/Fasteners_SAEJ483a2.svg  style="width:32px;"> **SAE J483a 2** Écrou borgne, forme haute.



### Fixations pour rainures en T 

-   <img alt="" src=images/Fasteners_DIN508.svg  style="width:32px;"> **DIN 508** Écrou pour rainures en T.

-   <img alt="" src=images/Fasteners_GN505.svg  style="width:32px;"> **GN 505** Écrou dentelé quart de tour à rainure en T.

-   <img alt="" src=images/Fasteners_GN505.4.svg  style="width:32px;"> **GN 505.4** Boulon à rainure en T dentelée.

-   <img alt="" src=images/Fasteners_GN506.svg  style="width:32px;"> **GN 506** Tasseaux.

-   <img alt="" src=images/Fasteners_GN507.svg  style="width:32px;"> **GN 507** Écrou pour rainures en T.

-   <img alt="" src=images/Fasteners_ISO299.svg  style="width:32px;"> **ISO 299** Écrou pour rainures en T.



### Rondelles

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width:32px;"> **ASME B18.21.1.12A** Rondelle UN, série étroite.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width:32px;"> **ASME B18.21.1.12B** Rondelle UN, série normale.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width:32px;"> **ASME B18.21.1.12C** Rondelle UN, série large.

-   <img alt="" src=images/Fasteners_DIN6319C.svg  style="width:32px;"> **DIN 6319C** Rondelle convexe.

-   <img alt="" src=images/Fasteners_DIN6319D.svg  style="width:32px;"> **DIN 6319D** Rondelle concave.

-   <img alt="" src=images/Fasteners_DIN6319G.svg  style="width:32px;"> **DIN 6319G** Rondelle portée sphérique concave.

-   <img alt="" src=images/Fasteners_DIN6340.svg  style="width:32px;"> **DIN 6340** Rondelle pour dispositifs de serrage.

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width:32px;"> **ISO 7089** Rondelle plate, série normale. *Grade A*.

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width:32px;"> **ISO 7090** Rondelle plate chanfreinée, série normale. *Grade A*.

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width:32px;"> **ISO 7092** Rondelle plate, série étroite. *Grade A*.

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width:32px;"> **ISO 7093-1** Rondelle plate, série large. *Grade A*.

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width:32px;"> **ISO 7094** Rondelle plate, série très large. *Grade C*.

-   <img alt="" src=images/Fasteners_ISO8738.svg  style="width:32px;"> **ISO 8738** Rondelle plate pour axes d\'articulation.

-   <img alt="" src=images/Fasteners_NFE27-619.svg  style="width:32px;"> **NFE27-619** Rondelle cuvette décoletée.



### Tiges, tarauds et filières 

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width:32px;"> Taraud en inch.

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width:32px;"> Filière en inch.

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width:32px;"> Tige filetée en inch UNC.

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width:32px;"> Tige filetée métrique DIN 975.

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width:32px;"> Taraud métrique.

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width:32px;"> Filière métrique.

### Inserts

-   <img alt="" src=images/Fasteners_IUTHeatInsert.svg  style="width:32px;"> Insert thermofixé.

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width:32px;"> Écrou à sertir.

-   <img alt="" src=images/Fasteners_PEMStandoff.svg  style="width:32px;"> Entretoise à sertir.

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width:32px;"> Goujon à sertir.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width:32px;"> Entretoise femelle/femelle pour PCB.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width:32px;"> Entretoise filetée femelle/mâle pour PCB.

-   <img alt="" src=images/Fasteners_4PWTI.svg  style="width:32px;"> Insert en bois fileté à 4 branches (écrous en T DIN 1624).



### Circlips

-   <img alt="" src=images/Fasteners_DIN471.svg  style="width:32px;"> **DIN 471** Circlip extérieur.

-   <img alt="" src=images/Fasteners_DIN472.svg  style="width:32px;"> **DIN 472** Circlip intérieur.

-   <img alt="" src=images/Fasteners_DIN6799.svg  style="width:32px;"> **DIN 6799** Bague d\'arrêt pour arbre.



### Pointes

-   <img alt="" src=images/Fasteners_DIN1143.svg  style="width:32px;"> **DIN 1143** Pointe à tête ronde et plate pour utilisation dans les machines à clouer automatiques.

-   <img alt="" src=images/Fasteners_DIN1144-A.svg  style="width:32px;"> **DIN 1144-A** Pointe pour l\'installation de panneaux composites en laine de bois, tête ronde de 20 mm.

-   <img alt="" src=images/Fasteners_DIN1151-A.svg  style="width:32px;"> **DIN 1151-A** Pointe tête plate.

-   <img alt="" src=images/Fasteners_DIN1151-B.svg  style="width:32px;"> **DIN 1151-B** Pointe tête fraisée.

-   <img alt="" src=images/Fasteners_DIN1152.svg  style="width:32px;"> **DIN 1152** Pointe tête ronde.

-   <img alt="" src=images/Fasteners_DIN1160-A.svg  style="width:32px;"> **DIN 1160-A** Pointe ou clou ardoise.

-   <img alt="" src=images/Fasteners_DIN1160-B.svg  style="width:32px;"> **DIN 1160-B** Pointe ou clou à tête large ardoise.



### Goupilles

-   <img alt="" src=images/Fasteners_ISO1234.svg  style="width:32px;"> **ISO 1234** Goupille fendue.

-   <img alt="" src=images/Fasteners_ISO2338.svg  style="width:32px;"> **ISO 2338** Goupille parallèle.

-   <img alt="" src=images/Fasteners_ISO2339.svg  style="width:32px;"> **ISO 2339** Goupille conique.

-   <img alt="" src=images/Fasteners_ISO2340A.svg  style="width:32px;"> **ISO 2340A** Goujon non fileté.

-   <img alt="" src=images/Fasteners_ISO2340B.svg  style="width:32px;"> **ISO 2340B** Goujon non fileté sans tête (avec trous pour goupilles fendues).

-   <img alt="" src=images/Fasteners_ISO2341A.svg  style="width:32px;"> **ISO 2341A** Goujon non fileté avec tête.

-   <img alt="" src=images/Fasteners_ISO2341B.svg  style="width:32px;"> **ISO 2341B** Goujon non fileté avec tête (avec trous pour goupilles fendues).

-   <img alt="" src=images/Fasteners_ISO8733.svg  style="width:32px;"> **ISO 8733** Goupille parallèle avec filetage intérieur, non trempée.

-   <img alt="" src=images/Fasteners_ISO8734.svg  style="width:32px;"> **ISO 8734** Goupille cylindrique.

-   <img alt="" src=images/Fasteners_ISO8735.svg  style="width:32px;"> **ISO 8735** Goupille cylindrique à trou taraudé, trempée.

-   <img alt="" src=images/Fasteners_ISO8736.svg  style="width:32px;"> **ISO 8736** Goupille de position conique à trou taraudé, non trempée.

-   <img alt="" src=images/Fasteners_ISO8737.svg  style="width:32px;"> **ISO 8737** Goupille de position conique à longueur filetée, non trempée.

-   <img alt="" src=images/Fasteners_ISO8739.svg  style="width:32px;"> **ISO 8739** Goupille cannelée à cannelures constantes sur toute la longueur débouchantes, à bout pilote.

-   <img alt="" src=images/Fasteners_ISO8740.svg  style="width:32px;"> **ISO 8740** Goupille cannelée à cannelures constantes sur toute la longueur débouchantes, à chanfrein.

-   <img alt="" src=images/Fasteners_ISO8741.svg  style="width:32px;"> **ISO 8741** Goupille cannelée à cannelures progressives renversées sur la moitié de la longueur non débouchante.

-   <img alt="" src=images/Fasteners_ISO8742.svg  style="width:32px;"> **ISO 8742** Goupille cannelée à cannelures centrales constantes sur le tiers de la longueur non débouchante.

-   <img alt="" src=images/Fasteners_ISO8743.svg  style="width:32px;"> **ISO 8743** Goupille cannelée à cannelures centrales constantes sur la moitié de la longueur non débouchante.

-   <img alt="" src=images/Fasteners_ISO8744.svg  style="width:32px;"> **ISO 8744** Goupille cannelée à cannelures progressives sur toute la longueur (débouchante).

-   <img alt="" src=images/Fasteners_ISO8745.svg  style="width:32px;"> **ISO 8745** Goupille cannelée à cannelures progressives sur la moitié de la longueur (débouchante).

-   <img alt="" src=images/Fasteners_ISO8746.svg  style="width:32px;"> **ISO 8746** Clous cannelés à tête ronde.

-   <img alt="" src=images/Fasteners_ISO8747.svg  style="width:32px;"> **ISO 8747** Clou cannelé tête fraisée.

-   <img alt="" src=images/Fasteners_ISO8748.svg  style="width:32px;"> **ISO 8748** Goupille élastique spiralée, série épaisse.

-   <img alt="" src=images/Fasteners_ISO8750.svg  style="width:32px;"> **ISO 8750** Goupille élastique spiralée, série moyenne.

-   <img alt="" src=images/Fasteners_ISO8751.svg  style="width:32px;"> **ISO 8751** Goupille élastique spiralée, série mince.

-   <img alt="" src=images/Fasteners_ISO8752.svg  style="width:32px;"> **ISO 8752** Goupille cylindrique creuse, dites goupilles élastiques, série épaisse.

-   <img alt="" src=images/Fasteners_ISO13337.svg  style="width:32px;"> **ISO 13337** Goupille cylindrique creuse, dites goupilles élastiques, série mince.



## Obsolète

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:32px;"> [Fraisage](Fasteners_ChamferHole/fr.md) : chanfreine les trous pour les vis à tête fraisée. Non disponible dans {{VersionPlus/fr|0.5.13}}.



## Références

-   Auteur : [shaise](http://theseger.com/projects/author/shaise/)
    -   Concepteur d\'objets : Ulrich Brammer
    -   Architecture de l\'atelier : Shai Seger
-   Code source : <https://github.com/shaise/FreeCAD_FastenersWB>
-   Rapports de bogues et demandes de fonctionnalités : <https://github.com/shaise/FreeCAD_FastenersWB/issues>
-   Sujet de forum : <https://forum.freecadweb.org/viewtopic.php?t=11429>



## Liens

-   [BOLTS](https://github.com/jreinhardt/BOLTS): une librairie ouverte pour les spécifications techniques


{{Fasteners_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [External_Workbenches](Category_External_Workbenches.md) > Fasteners Workbench/fr
