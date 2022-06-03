# <img alt="Icône de l\'atelier Spreadsheet" src=images/Workbench_Spreadsheet.svg  style="width   *64px;"> Spreadsheet Workbench/fr

## Introduction

L\'<img alt="" src=images/Workbench_Spreadsheet.svg  style="width   *24px;"> [atelier Spreadsheet](Spreadsheet_Workbench/fr.md) vous permet de créer et d'éditer des feuilles de calcul, de remplir la feuille de calcul avec les données extraites d'un modèle, d'effectuer des calculs et de les exporter vers d'autres applications de tableurs telles que LibreOffice ou Microsoft Excel.


{{TOCright}}

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width   *600px;"> 
*Une feuille de tableur avec un certain nombre de cellules remplies de texte et de quantités*

## Outils

-   <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width   *24px;"> [Créer une feuille de calcul](Spreadsheet_CreateSheet/fr.md)   * créer un nouveau tableur.

-   <img alt="" src=images/Spreadsheet_Import.svg  style="width   *24px;"> [Importer](Spreadsheet_Import/fr.md)    * importe un fichier CSV dans une feuille de calcul.

-   <img alt="" src=images/Spreadsheet_Export.svg  style="width   *24px;"> [Exporter](Spreadsheet_Export/fr.md)    * exporte un fichier CSV depuis une feuille de calcul.

-   <img alt="" src=images/Spreadsheet_MergeCells.svg  style="width   *24px;"> [Fusionner des cellules](Spreadsheet_MergeCells/fr.md)    * fusionne les cellules sélectionnées.

-   <img alt="" src=images/Spreadsheet_SplitCell.svg  style="width   *24px;"> [Diviser une cellule](Spreadsheet_SplitCell/fr.md)    * divise les cellules précédemment fusionnées.

-   <img alt="" src=images/Spreadsheet_AlignLeft.svg  style="width   *24px;"> [Alignement à gauche](Spreadsheet_AlignLeft/fr.md)    * aligne le contenu des cellules sélectionnées vers la gauche.

-   <img alt="" src=images/Spreadsheet_AlignCenter.svg  style="width   *24px;"> [Alignement au centre](Spreadsheet_AlignCenter/fr.md)    * aligne le contenu des cellules sélectionnées au centre, horizontalement.

-   <img alt="" src=images/Spreadsheet_AlignRight.svg  style="width   *24px;"> [Alignement à droite](Spreadsheet_AlignRight/fr.md)    * aligne le contenu des cellules sélectionnées vers la droite.

-   <img alt="" src=images/Spreadsheet_AlignTop.svg  style="width   *24px;"> [Alignement en haut](Spreadsheet_AlignTop/fr.md)    * aligne le contenu des cellules sélectionnées en haut.

-   <img alt="" src=images/Spreadsheet_AlignVCenter.svg  style="width   *24px;"> [Alignement vertical au centre](Spreadsheet_AlignVCenter/fr.md)    * aligne le contenu des cellules sélectionnées au centre, verticalement.

-   <img alt="" src=images/Spreadsheet_AlignBottom.svg  style="width   *24px;"> [Alignement en bas](Spreadsheet_AlignBottom/fr.md)    * aligne le contenu des cellules sélectionnées vers le bas.

-   <img alt="" src=images/Spreadsheet_StyleBold.svg  style="width   *24px;"> [Texte en gras](Spreadsheet_StyleBold/fr.md)    * met en gras le contenu des cellules sélectionnées.

-   <img alt="" src=images/Spreadsheet_StyleItalic.svg  style="width   *24px;"> [Texte en italique](Spreadsheet_StyleItalic/fr.md)    * met le contenu des cellules sélectionnées en italique.

-   <img alt="" src=images/Spreadsheet_StyleUnderline.svg  style="width   *24px;"> [Texte souligné](Spreadsheet_StyleUnderline/fr.md)    * permet de souligner le contenu des cellules sélectionnées.

-   <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width   *24px;"> [Alias](Spreadsheet_SetAlias/fr.md)   * définit l\'alias d\'une cellule sélectionnée.

-    **Noir**et **Blanc** définissent les couleurs de premier plan et d\'arrière-plan des cellules sélectionnées.

## Préférences

-   <img alt="" src=images/Preferences-spreadsheet.svg  style="width   *32px;"> [Préférences](Spreadsheet_Preferences/fr.md)    * les préférences pour le tableur. {{Version/fr|0.20}}

## Insérer et supprimer des lignes et des colonnes 

Des lignes et des colonnes peuvent être insérées ou supprimées en faisant un clic droit sur un en-tête de ligne ou de colonne et en sélectionnant l\'option appropriée dans le menu contextuel. Il est possible de sélectionner d\'abord plusieurs lignes ou colonnes. Soit en maintenant la touche **Ctrl** enfoncée tout en sélectionnant les en-têtes, soit en maintenant le bouton gauche de la souris enfoncé et en faisant glisser la souris.

Dans la version 0.19 de FreeCAD et antérieure, les lignes sont insérées au-dessus des lignes sélectionnées et les colonnes à gauche des colonnes sélectionnées. Dans la version 0.20 de FreeCAD, vous pouvez spécifier le côté d\'insertion.

Remarquez que la suppression de lignes ou de colonnes contenant des données peut entraîner la rupture de la feuille de calcul et de votre modèle si celui-ci repose sur la feuille de calcul. Vous n\'êtes pas prévenu si cela se produit.

## Couper et copier-coller des cellules 

Les opérations couper et copier-coller peuvent être utilisées sur les cellules des feuilles de calcul FreeCAD. Vous pouvez utiliser les raccourcis normaux pour ces opérations    * **Ctrl**+**X**, **Ctrl**+**C** et **Ctrl**+**V** respectivement. Pour sélectionner plusieurs cellules, maintenez la touche **Ctrl** enfoncée tout en sélectionnant, ou maintenez le bouton gauche de la souris enfoncé et faites glisser pour sélectionner une plage de cellules rectangulaires.

Les opérations couper et copier stockent le contenu et les propriétés des cellules dans le presse-papiers. L\'opération coller écrit les données de manière à ce que le contenu de la cellule supérieure gauche des données stockées soit déposé dans la cellule active. Les autres contenus stockés sont placés par rapport à cette cellule. Les formules sont mises à jour en conséquence.

Remarquez que la suppression des cellules contenant des données peut casser la feuille de calcul et votre modèle s\'il repose sur la feuille de calcul. Vous n\'êtes pas prévenu si cela se produit.

Dans la version 0.19 de FreeCAD et antérieures, il y a un bug qui peut provoquer un blocage de FreeCAD si une plage de cellules non-rectangulaire est collée. Il est conseillé d\'enregistrer votre travail avant d\'effectuer toute opération de collage.

## Propriétés d\'une cellule 

Les propriétés d\'une cellule de feuille de calcul peuvent être modifiées en cliquant droit sur la cellule et en sélectionnant **Properties...** dans le menu contextuel. La boîte de dialogue suivante s\'affiche    *

![](images/SpreadsheetCellPropDialog.png )

Comme mentionné dans les onglets, les propriétés suivantes peuvent être changées    *

-   Couleur   * couleur du texte et couleur d\'arrière-plan
-   Alignement   * alignement horizontal et vertical du texte
-   Style   * style du texte    * gras, italique, souligné
-   Affichage unités   *  affiche l\'unité de la cellule. Veuillez lire la section [Unités](#Unités.md) ci-dessous.
-   Alias    *  définit un [alias](Spreadsheet_SetAlias/fr.md) pour cette cellule. Cet alias peut être utilisé dans les formules de cellule et aussi dans les [expressions](Expressions/fr.md) générales; voir la section [Données de la feuille de calcul dans les expressions](#Donn.C3.A9es_de_la_feuille_de_calcul_dans_les_expressions.md) pour plus d\'informations.

## Expressions dans les cellules 

Une cellule de feuille de calcul peut contenir du texte arbitraire ou une expression. Techniquement, les expressions doivent commencer par un signe égal \'=\'. Cependant, le tableur tente d'être intelligent ; si vous entrez ce qui ressemble à une expression sans le signe \'=\', celui-ci sera ajouté automatiquement.

Les expressions cellulaires peuvent contenir des nombres, des fonctions, des références à d\'autres cellules et des références à des propriétés du modèle (voir toutefois les [limitations courantes](#Limitations_Courantes.md) ci-dessous). Les cellules sont référencées par leur colonne (lettre CAPITALE) et leur rangée (nombre). Une cellule peut également être référencée par son [alias](#alias_name.md). Exemple   * B4 + A6

**Remarque   *** Les expressions de cellule sont traitées par FreeCAD comme du code de programmation. Par conséquent, lorsque vous modifiez une cellule, vous voyez que le contenu ne suit pas vos paramètres d\'affichage   *

-   le séparateur décimal est toujours un point
-   le nombre de décimales affichées peut différer de vos [paramètres de préférences](Preferences_Editor/fr#Unit.C3.A9s.md)

Les références aux objets dans le modèle sont expliquées ci-dessous [Références aux données CAO](#R.C3.A9f.C3.A9rences_aux_donn.C3.A9es_CAO.md). L\'utilisation des valeurs de cellule de feuille de calcul pour définir les propriétés du modèle est expliquée ci-dessous [Données de la feuille de calcul dans les expressions](#Donn.C3.A9es_de_la_feuille_de_calcul_dans_les_expressions.md). Pour plus d\'informations sur les expressions et les fonctions disponibles, voir [Expressions](Expressions/fr.md).

## Interaction entre les feuilles de calcul et le modèle de CAO 

Les données contenues dans les cellules d\'une feuille de calcul peuvent être utilisées dans les expressions de paramètres de modèle de CAO. Ainsi, une feuille de calcul peut être utilisée comme source pour les valeurs de paramètres utilisées dans un modèle, regroupant efficacement les valeurs à un endroit. Lorsque les valeurs sont modifiées dans la feuille de calcul, elles sont propagées dans tout le modèle.

De même, les propriétés des objets de modèle CAO peuvent être utilisées dans les expressions des cellules de la feuille de calcul. Cela permet d\'utiliser des propriétés d\'objet telles que le volume ou la surface dans la feuille de calcul. Si le nom d\'un objet dans le modèle CAO est modifié, le changement sera automatiquement propagé à toutes les références dans les expressions de feuille de calcul en utilisant le nom qui a été modifié.

Plusieurs feuilles de calcul peuvent être utilisées dans un document. Une feuille de calcul peut être identifiée à l\'aide de son nom ou de son étiquette.

FreeCAD attribuera automatiquement un nom unique à une feuille de calcul lors de sa création. Ces noms suivent le modèle `Spreadsheet`, `Spreadsheet001`, `Spreadsheet002` et ainsi de suite. Le nom ne peut pas être modifié manuellement et il n\'est pas visible dans les propriétés de la feuille de calcul. Il peut être utilisé pour faire référence à la feuille de calcul dans une [Expression](Expressions/fr.md) (voir ci-dessous [Données de la feuille de calcul dans les expressions](#Donn.C3.A9es_de_la_feuille_de_calcul_dans_les_expressions.md).)

L\'étiquette d\'une feuille de calcul est automatiquement définie sur le nom de la feuille de calcul lors de sa création. Contrairement au nom, l\'étiquette peut être modifiée, par exemple dans le panneau des propriétés ou à l\'aide de l\'action Renommer du menu contextuel. Notez que l\'étiquette d\'une feuille de calcul dans un document doit être unique. Si vous essayez de changer l\'étiquette en une étiquette déjà utilisée par une autre feuille de calcul, FreeCAD n\'acceptera pas la nouvelle étiquette.

FreeCAD vérifie les dépendances cycliques. Voir [limitations courantes](Spreadsheet_Workbench/fr#Limitations_Courantes.md).

### Références aux données CAO 

Comme indiqué ci-dessus, il est possible de référencer les données du modèle CAO dans des expressions de feuille de calcul.

Les expressions calculées dans les cellules de la feuille de calcul commencent par un signe égal (\'=\'). Cependant, le mécanisme de saisie du tableur tente d'être astucieux. Une expression peut être entrée sans le signe \'=\'. Si la chaîne entrée est une expression valide, un \'=\' est automatiquement ajouté lors de la frappe de la touche **Valider**. Si la chaîne entrée n\'est pas une expression valide (souvent le résultat d\'une saisie avec une casse incorrecte, par exemple \"MonCube.longueur\" à la place de \"MonCube.Longueur\"), aucun \'=\' n\'est ajouté et cela est traité comme une simple chaîne de texte.

**Remarque   *** le comportement ci-dessus (insertion automatique de \'=\') a des travers désagréables    *

-   si vous souhaitez conserver une colonne de noms correspondant aux noms d\'[alias](#alias_name.md) dans une colonne de valeurs adjacente, vous devez saisir le nom dans la colonne d\'étiquette avant celle donnée à la cellule dans la colonne de valeur comme nom d\'alias. Sinon, lorsque vous entrez le nom d\'alias dans la colonne d\'étiquette, la feuille de calcul considère qu\'il s\'agit d\'une expression et la remplace par \"=\" ; et le texte affiché correspondra à la valeur de la cellule .
-   Si vous faites une erreur lors de la saisie du nom dans la colonne d\'étiquette et souhaitez le corriger, vous ne pouvez pas le changer simplement en nom d\'alias. Au lieu de cela, vous devez d\'abord remplacer le nom d\'alias par un autre nom, puis corriger le nom du texte dans la colonne d\'étiquette, puis remplacer le nom d\'alias dans la colonne de valeur par son nom d\'origine.

Une façon d\'éviter ces problèmes consiste à préfixer les étiquettes de texte correspondant aux noms d\'alias avec une chaîne fixe, les rendant ainsi différentes. Notez que \"\_\" ne fonctionnera pas, car il est converti en \"=\". Cependant, un blanc, bien qu\'invisible, fonctionnera.

Le tableau suivant montre quelques exemples en supposant que le modèle a une fonctionnalité nommée \"MonCube\"    *

  Donnée CAO                                              Cellule dans la feuille de calcul   Résultat
    
  Longueur paramétrique d\'un Cube dans l\'Atelier Part   =MonCube.Longueur                   Longueur en mm
  Volume du Cube                                          =MonCube.Shape.Volume               Volume en mm³ sans unité
  Type de la forme du Cube                                =MonCube.Shape.ShapeType            String   * Solid
  Nom du Cube                                             =MonCube.Label                      String   * MonCube
  Coordonnée x du centre de gravité du Cube               =MonCube.Shape.CenterOfMass.x       Coordonnée x en mm sans unité

### Données de la feuille de calcul dans les expressions 

Pour utiliser les données de la feuille de calcul dans d\'autres parties de FreeCAD, vous allez généralement créer une [Expression](Expressions/fr.md) qui fait référence à la feuille de calcul et à la cellule contenant les données que vous souhaitez utiliser. Vous pouvez identifier les feuilles de calcul par le nom ou par l\'étiquette, et vous pouvez identifier les cellules par adresse ou par alias. L\'autocomplétion est disponible pour toutes les formes de référencement.

++++
|                      | Feuille de calcul par le nom                        | Feuille de calcul par l\'étiquette                     |
+======================+=====================================================+========================================================+
| Cellule par adresse  |                                      |                                         |
|                      | `<nowiki>=Spreadsheet042.B5</nowiki>`      | `<nowiki>=<<MySpreadsheet>>.B5</nowiki>`      |
|                      |                                                  |                                                     |
++++
| Cellule par l\'alias |                                      |                                         |
|                      | `<nowiki>=Spreadsheet042.MyAlias</nowiki>` | `<nowiki>=<<MySpreadsheet>>.MyAlias</nowiki>` |
|                      |                                                  |                                                     |
++++


<div class="mw-collapsible mw-collapsed">

La méthode recommandée pour faire référence aux données de la feuille de calcul consiste à utiliser l\'étiquette de la feuille de calcul et le nom d\'alias de cellule. Pour une explication plus approfondie des avantages et des inconvénients des modes d\'adressage, consultez la section développée ci-dessous.


<div class="mw-collapsible-content">

L\'utilisation de l\'étiquette de la feuille de calcul présente l\'avantage de pouvoir être librement modifiée pour décrire le contenu de la feuille de calcul. Il est également plus facile d\'identifier la feuille de calcul utilisée car le texte de l\'expression correspond à l\'étiquette affichée dans les vues du modèle et des propriétés. Si vous décidez de modifier l\'étiquette d\'une feuille de calcul, les références existantes au contenu de la feuille de calcul seront mises à jour, de sorte que vous ne casserez pas vos expressions en renommant la feuille de calcul. Le nom interne de la feuille de calcul n\'est pas facilement disponible ailleurs que dans l\'éditeur d\'expression, donc si vous utilisez le nom interne et décidez plus tard de renommer les feuilles de calcul, vous pourriez avoir du mal à retracer vos données d\'expression jusqu\'à leur source.

Sachez que lorsque vous créez une nouvelle feuille de calcul, le nom et l\'étiquette sont identiques, il est donc facile d\'utiliser accidentellement le nom de la feuille de calcul au lieu de l\'étiquette. Un moyen simple d\'éviter cela est de donner à la feuille de calcul un nom significatif avant de commencer à l\'utiliser dans des expressions.

Bien que vous puissiez utiliser le numéro de ligne et de colonne dans une expression pour référencer une cellule, la meilleure pratique consiste à donner à la cellule un nom d\'alias et à l\'utiliser. Voir [Propriétés d\'une cellule](#Propri.C3.A9t.C3.A9s_d.27une_cellule.md) ci-dessus pour savoir comment définir l\'alias. Par exemple, si les données de la cellule B1 contenaient le paramètre de longueur pour un objet, un nom d\'alias de `MyObject_Length` permettrait à la valeur d\'être appelée `<<MyParams>>.MyObject_Length` au lieu de `Spreadsheet.B1`. En plus d\'être beaucoup plus faciles à lire et à comprendre, les noms d\'alias sont également beaucoup plus faciles à modifier si vous décidez d\'ajuster la structure de votre feuille de calcul. L\'utilisation d\'un alias présente également l\'avantage qu\'il est plus facile de voir quelles cellules sont utilisées pour contrôler d\'autres parties du document. Notez que FreeCAD ajustera automatiquement les références de position dans les expressions si vous insérez ou supprimez des lignes et des colonnes dans la feuille de calcul, donc même si vous utilisez des numéros de ligne et de colonne dans une expression, vous pouvez insérer des lignes et des colonnes sans casser les références aux cellules environnantes.


</div>


</div>

### Modèles complexes et recalculs 

La modification d\'une feuille de calcul déclenchera un recalcul du modèle 3D, même si les modifications n\'affectent pas le modèle. Pour un modèle complexe, un recalcul peut prendre beaucoup de temps et devoir attendre après chaque édition est bien sûr assez ennuyeux.

Il existe trois solutions pour y remédier   *

1.  Ignorer temporairement les recalculs   *
    -   Dans la [Vue en arborescence](Tree_view/fr.md), clic droit sur le document <img alt="" src=images/Document.svg  style="width   *24px;"> qui contient la feuille de calcul.
    -   Sélectionnez l\'option **Skip recomputes** dans le menu contextuel.
    -   Il y a un gros inconvénient à cette solution. Les nouvelles valeurs entrées dans la feuille de calcul ne seront pas affichées tant que le document n\'aura pas été recalculé. Au lieu de cela, `#PENDING` est affiché.
    -   Vous pouvez soit recalculer manuellement, en utilisant la commande [Std Rafraîchir](Std_Refresh/fr.md), soit désactiver **Skip recomputes** lorsque vous avez terminé l\'édition.
2.  Utilisez une macro pour ignorer automatiquement les recalculs lors de la modification d\'une feuille de calcul   *
    -   Téléchargez et exécutez [skipSheet.FCMacro](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=48600#p419301).
    -   Cette solution économise quelques étapes par rapport à la première solution, mais présente également l\'inconvénient mentionné.
3.  Mettez la feuille de calcul dans un [fichier séparé](File_Format_FCStd/fr.md)   *
    -   Vous pouvez référencer des données de feuille de calcul à partir d\'un fichier externe **.FCStd** avec cette syntaxe   * `<nowiki>=NameOfFile#<<MySpreadsheet>>.MyAlias</nowiki>`.
    -   L\'avantage d\'avoir la feuille de calcul dans un autre fichier par rapport à la désactivation des recalculs est que la feuille de calcul elle-même est recalculée.
    -   L\'inconvénient est que le modèle ne recalculera pas automatiquement après les modifications apportées à la feuille de calcul.
    -   Dans le scénario où vous ouvrez d\'abord le fichier \'tableur\', changez une ou plusieurs valeurs puis ouvrez le fichier \'modèle\', il n\'y aura aucune indication que le modèle doit être recalculé. Mais si les deux fichiers sont ouverts, l\'icône [Std Rafraîchir](Std_Refresh/fr.md) se mettra à jour correctement pour le fichier \'modèle\' après les modifications apportées au fichier \'tableur\'.

## Unités

Le tableur intègre une notion de dimension (unités) associée aux valeurs de cellule. Un numéro entré sans unité associée n\'a pas de dimension. L\'unité doit être entrée immédiatement après la valeur numérique, sans espace intermédiaire. Si un nombre a une unité associée, cette unité sera utilisée dans tous les calculs. Par exemple, la multiplication de deux longueurs avec l\'unité mm donne une surface avec l\'unité mm².

Si une cellule contient une valeur qui représente une dimension, vous devez la saisir avec son unité associée. Bien que dans de nombreux cas simples, on puisse se débrouiller avec une valeur sans dimension, il est déconseillé de ne pas entrer l\'unité. Si une valeur représentant une dimension est entrée sans son unité associée, certaines séquences d\'opérations obligent FreeCAD à alerter sur les unités incompatibles dans une expression lorsqu\'il apparaît que celle-ci doit être validée. (Cela peut être mieux compris en consultant ce [sujet (en)](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=34713&p=292455#p292438) dans les forums FreeCAD.)

Vous pouvez modifier les unités affichées pour une valeur de cellule à l\'aide de l\'onglet Unités de la boîte de dialogue Propriétés [Unités](#Unit.C3.A9s.md) (ci-dessus). Cela ne change pas la valeur contenue dans la cellule; il ne convertit que la valeur existante pour l\'affichage. La valeur utilisée pour les calculs ne change pas et les résultats des formules utilisant cette valeur ne changent pas. Par exemple, une cellule contenant la valeur \"5.08cm\" peut être affichée sous la forme \"2in\" en modifiant la valeur de l\'onglet des unités en \"in\".

Un nombre sans dimension ne peut pas être changé en nombre avec une unité dans la boîte de dialogue des propriétés de la cellule. On peut mentionner une chaîne unité, et cette chaîne sera affichée ; mais la cellule contient toujours un nombre sans dimension. Afin de changer une valeur sans dimension en une valeur avec dimension, la valeur elle-même doit être entrée à nouveau avec son unité associée.

Parfois, il peut être souhaitable de supprimer une dimension dans une expression. Cela peut être fait en multipliant par 1 avec une unité réciproque.

## Importation et exportation 

### Format CSV 

Les feuilles de calcul FreeCAD peuvent être importées et exportées au format [CSV](https   *//fr.wikipedia.org/wiki/Comma-separated_values) qui peut également être lu et écrit par la plupart des autres applications de feuilles de calcul telles que Microsoft Excel ou LibreOffice Calc. Voir [Spreadsheet Importer](Spreadsheet_Import/fr.md) et [Spreadsheet Exporter](Spreadsheet_Export/fr.md) pour plus d\'informations.

### Format XLSX 

Les feuilles de calcul au format Excel XLSX peuvent être importées avec la commande [Std Importer](Std_Import/fr.md) ou la commande [Std Ouvrir](Std_Open/fr.md). Les fonctionnalités suivantes sont prises en charge    *

-   Toutes les fonctions qui sont également disponibles dans la feuille de calcul FreeCAD. D\'autres fonctions donnent une erreur dans la cellule correspondante après l\'importation.
-   Noms d\'alias pour les cellules.
-   Plusieurs tableaux dans une feuille Excel. Dans ce cas, une feuille de calcul FreeCAD est créée pour chaque tableau Excel.

Les autres fonctionnalités ne sont pas importées dans la feuille de calcul FreeCAD.

## Imprimer

Pour gérer la mise en page nécessaire à l\'impression, les feuilles de calcul FreeCAD sont imprimées en les insérant dans une [TechDraw Vue d\'un tableur](TechDraw_SpreadsheetView/fr.md).

## Limitations courantes 

FreeCAD vérifie les dépendances cycliques. De par sa conception, cette vérification s'arrête au niveau de l'objet feuille de calcul. Par conséquent, vous ne devriez pas avoir de feuille de calcul contenant à la fois des cellules dont les valeurs sont utilisées pour spécifier des paramètres pour le modèle et des cellules dont les valeurs utilisent la sortie du modèle. Par exemple, vous ne pouvez pas avoir de cellules spécifiant la longueur, la largeur et la hauteur d\'un objet, et une autre cellule qui référence le volume total de la forme obtenue. Cette restriction peut être surmontée en disposant de deux feuilles de calcul    * l\'une utilisée comme source de données pour les paramètres d\'entrée du modèle et l\'autre pour les calculs basés sur les données géométriques résultantes.

## Scripts basiques 


```python
import Spreadsheet
sheet = App.ActiveDocument.addObject("Spreadsheet   *   *Sheet","MySpreadsheet")
sheet.Label = "Dimensions"

sheet.set('A1','10mm')
sheet.recompute()
sheet.get('A1')

sheet.setAlias('B1','Diameter')
sheet.set('Diameter','20mm')
sheet.recompute()
sheet.get('Diameter')
```





{{Spreadsheet_Tools_navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Spreadsheet Workbench/fr
