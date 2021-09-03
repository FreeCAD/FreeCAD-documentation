---
- GuiCommand:/fr
   Name:TechDraw WeldingSymbol
   Name/fr:TechDraw Symbole de soudure
   Icon:techdraw-weldsymbol.svg
   MenuLocation:TechDraw → Ajouter les informations de soudage...
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Ligne de référence](TechDraw_LeaderLine/fr.md)
---

## Description

L\'outil Symbole de soudure ajoute les spécifications de soudage à une ligne directrice existante.

<img alt="" src=images/TechDraw_WeldingSymbol_example.png  style="width:330px;"> 
*Spécification de soudage ajoutée à une ligne de référence*

## Utilisation

1.  Sélectionnez une ligne existante issue de **<img src="images/TechDraw_LeaderLine.svg" width=16px> [Insérer une ligne de référence à la vue ](TechDraw_LeaderLine/fr.md)
**
2.  Appuyez sur le bouton **<img src="images/TechDraw_WeldSymbol.svg" width=16px> [Ajouter les informations de soudage...](TechDraw_WeldSymbol/fr.md)**.
3.  Une boîte de dialogue s\'ouvre. Il permet de définir des symboles de soudage individuels et le texte d\'accompagnement à ajouter à la ligne de rappel.
4.  Pour quitter la boîte de dialogue et enregistrer les modifications, appuyez sur le bouton OK.
5.  Pour quitter la boîte de dialogue sans enregistrer, appuyez sur le bouton Annuler.
6.  Une fois le symbole de soudage créé, vous pouvez le modifier en double-cliquant sur le symbole de soudure dans l'arbre.

## Propriétés

### Symbole de soudure {#symbole_de_soudure}

-    {{PropertyData/fr|All Around}}: affiche le symbole *All Around* ou *Tout autour* (cercle) au niveau de la brisure de la ligne de rappel.

-    {{PropertyData/fr|Field Weld}}: affiche le symbole *Field Weld* ou *Soudure sur site* (indicateur) au niveau de la brisure de la ligne de rappel.

-    {{PropertyData/fr|Alternate Weld}}: décale le symbole inférieur pour indiquer des soudures alternées.

-    {{PropertyData/fr|Tail Text}}: texte à afficher à la fin de la ligne de rappel.

### Tuile

Chaque symbole individuel (\"côté flèche\" et \"autre côté\") est représenté par un objet \"tuile\". Un symbole de soudure est associé à 1 ou 2 tuiles. Chacun a les propriétés suivantes:

-    {{PropertyData/fr|Parent Tile}}: le symbole de soudure parent

-    {{PropertyData/fr|Tile Row}}: ligne de la tuile. 0 signifie au-dessus de la ligne, -1 en dessous de la ligne. **Remarque:** Si vous changez la rangée d\'une tuile, vous devez également changer la tuile pour le deuxième côté! De cette façon, vous pouvez retourner les côtés.

-    {{PropertyData/fr|Tile Column}}: colonne de la tuile. Pour le moment, il est toujours égal à 0, la propriété n\'est donc pas modifiable.

-    {{PropertyData/fr|Symbol File}}: répertoire et nom de fichier du fichier SVG du symbole.

-    {{PropertyData/fr|Symbol Included}}: répertoire et nom de fichier du fichier SVG de symbole inclus réel. (Il s\'agit d\'un répertoire temporaire.)

-    {{PropertyData/fr|Left Text}}: texte à afficher à gauche du symbole SVG.

-    {{PropertyData/fr|Center Text}}: texte à afficher au-dessus/en dessous du symbole SVG.

-    {{PropertyData/fr|Right Text}}: texte à afficher à droite du symbole SVG.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Symbole peut être utilisé dans des [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
symbolName = "DrawWeldSymbol001")
symbolType = "TechDraw::DrawWeldSymbol"
App.activeDocument().addObject(symbolType, symbolName)
App.activeDocument().Page.addView(App.activeDocument().DrawWeldSymbol001)
App.activeDocument().DrawWeldSymbol001.Leader = myLeader
App.activeDocument().DrawWeldSymbol001.AllAround = True
App.activeDocument().DrawWeldSymbol001.FieldWeld = True
App.activeDocument().DrawWeldSymbol001.AlternatingWeld = True
App.activeDocument().DrawWeldSymbol001.TailText = "process text"

tileName = "DrawTileWeld001"
tileType = "TechDraw::DrawTileWeld"
App.activeDocument().addObject(tileType, tileName)
App.activeDocument().DrawTileWeld001.TileParent = App.activeDocument().DrawWeldSymbol001
App.activeDocument().DrawTileWeld001.TileRow = 0
App.activeDocument().DrawTileWeld001.TileColumn = 0
App.activeDocument().DrawTileWeld001.SymbolFile = fullPathToMySvgFile
App.activeDocument().DrawTileWeld001.LeftText = "left text"
App.activeDocument().DrawTileWeld001.RightText = "right text"
App.activeDocument().DrawTileWeld001.CenterText = "center text"
```

## Tuiles symboles Svg {#tuiles_symboles_svg}

-   Les symboles individuels sont formés de fichiers SVG de 64x64 pixels. Des symboles supplémentaires peuvent être créés dans un programme SVG tel qu\'[Inkscape](https://fr.wikipedia.org/wiki/Inkscape) en utilisant l\'un des symboles fournis par FreeCAD comme modèle.

<img alt="" src=images/Techdraw-WeldingSymbolLayoutArrow.svg  style="width:128px;"> <img alt="" src=images/Techdraw-WeldingSymbolLayoutOther.svg  style="width:128px;">

\* Les symboles individuels sont formés de fichiers SVG de 64x64 pixels (nominaux). Les tuiles ont en fait une \"bordure\" de 4px. La bordure veille à ce que la ligne de repère et le symbole se rencontrent bien.

-   Le symbole est dessiné en noir sur un fond transparent. La largeur du trait est de 0.5mm.
-   Le leader passe au-dessous des symboles pour le côté flèche et au-dessus des symboles pour \"l\'autre\".
-   Il n\'y a pas de norme de dénomination particulière autre que celle d\'ajouter \"Haut/Bas\" à la flèche/autres symboles latéraux.

## Remarques

-   Vous pouvez modifier votre symbol de soudage en double-cliquant dessus dans l\'arborescence. Le double clic dans la zone graphique n'est pas encore supporté.
-   Il existe un paramètre dans [TechDraw Préférences](TechDraw_Preferences/fr.md) pour le répertoire de symboles de soudage par défaut. Vous pouvez ajouter vos propres symboles dans un répertoire personnel.





{{TechDraw Tools navi

}}  
