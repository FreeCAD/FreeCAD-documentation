---
- GuiCommand:/fr
   Name:Draft ShapeString
   Name/fr:Draft Formes à partir texte
   MenuLocation:Drafting → Formes à partir de texte
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**S** **S**
   Version/fr:0.14
   SeeAlso:[Draft Texte](Draft_Text/fr.md), [Draft Etiquette](Draft_Label/fr.md), [Part Extrusion](Part_Extrude/fr.md)
---

## Description

La commande <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;"> **Draft Formes à partir de texte** crée une forme composée qui représente une chaîne de texte. Cette forme peut être utilisée pour créer des lettres en 3D avec la commande [Part Extrusion](Part_Extrude/fr.md).

La commande Draft Formes à partir de texte n\'est pas destinée aux annotations de texte standard. La commande [Draft Texte](Draft_Text/fr.md) ou la commande [Draft Etiquette](Draft_Label/fr.md) doivent être utilisées à cette fin.

![](images/Draft_ShapeString_Example400.png ) *Un seul point requis pour positionner la Forme à partir de texte*

## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_ShapeString.svg" width=16px> [Créer une forme à partir d'une chaîne de texte...](Draft_ShapeString/fr.md)**.
    -   Sélectionnez l\'option {{MenuCommand|Drafting → <img src="images/Draft_ShapeString.svg" width=16px> Forme à partir de texte}} dans le menu.
    -   Utilisez le raccourci clavier : **S** puis **S**.
2.  Le panneau de tâches {{MenuCommand|ShapeString}} s\'ouvre.
3.  Cliquez sur un point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées.
4.  Vous pouvez également appuyer sur le bouton **Réinitialiser le point** pour réinitialiser le point à l\'origine.
5.  Saisissez une {{MenuCommand|Chaîne}}.
6.  Spécifiez la {{MenuCommand|Hauteur}}.
7.  Pour sélectionner une police, effectuez l\'une des opérations suivantes :
    -   Saisissez un chemin de fichier dans la zone de saisie {{MenuCommand|Fichier de police}}.
    -   Appuyez sur le bouton **...** et sélectionnez un fichier.
    -   Appuyez sur le bouton **OK** pour terminer la commande.

## Options

-   Appuyez sur **Echap** ou sur le bouton **Fermer** pour annuler la commande.

## Remarques

-   Les polices prises en charge sont TrueType ({{FileName|.ttf}}), OpenType ({{FileName|.otf}}) et Type 1 ({{FileName|.pfb}}).
-   La commande est limitée au texte LTR (left-to-right (de gauche-à-droite)). Par conséquent, pour le moment, le texte RTL (right-to-left + top-to-bottom (de droite-à-gauche + haut-vers-bas)) n\'est pas supporté.
-   De très petites hauteurs de texte peuvent entraîner des formes de caractères déformées en raison de la perte de détails lors de la mise à l\'échelle.
-   De nombreuses polices de caractères génèrent une géométrie problématique. Ceci est dû au fait que les contours des polices sont autorisés à se chevaucher, à avoir de petits espaces et à avoir des directions différentes dans un glyphe. Ces conditions sont considérées comme des erreurs dans les fils utilisés pour définir les faces.
-   Les Draft Formes à partir texte peuvent également être créées avec la [Macro Fonts Win10 PYMP](Macro_Fonts_Win10_PYMP/fr.md).
-   Pour créer des ébauches de chaînes de caractères disposées de manière circulaire, utilisez la [Macro FCCircularText](Macro_FCCircularText/fr.md).

## Tutoriels

-   [Draft Tutoriel Forme à partir de texte](Draft_ShapeString_tutorial/fr.md) : pour extruder une chaîne de caractère, positionnez-la dans un espace 3D et créez une gravure dans un autre corps.
-   [How to use ShapeStrings in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623)

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Le fichier de police par défaut peut être modifié dans les préférences : {{MenuCommand|Édition → Préférences... → Draft → Textes et cotes → Fichier de police par défaut de Forme de texte}}. Voir [Draft Préférences](Draft_Preferences/fr.md).

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Forme à partir texte est dérivé d\'un [Part Part2DObject](Part_Part2DObject/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{TitleProperty|Draft}}

-    {{PropertyData/fr|Font File|File}}: spécifie le chemin du fichier de police utilisé pour dessiner le texte.

-    {{PropertyData/fr|Size|Length}}: spécifie la hauteur générale du texte.

-    {{PropertyData/fr|String|String}}: spécifie la chaîne de texte à afficher. Contrairement à un [Draft Texte](Draft_Text/fr.md), une Draft Forme à partir texte ne peut afficher qu\'une seule ligne de texte.

-    {{PropertyData/fr|Tracking|Length}}: spécifie l\'espacement supplémentaire entre les caractères du texte.

### Vue


{{TitleProperty|Draft}}

-    {{PropertyView/fr|Pattern|Enumeration}}: spécifie le [Draft Motif](Draft_Pattern/fr.md) avec lesquel remplir les surfaces du texte. Cette propriété ne fonctionne que si {{PropertyView/fr|Display Mode}} est {{value|Flat Lines}}.

-    {{PropertyView/fr|Pattern Size|Float}}: spécifie la taille du [Draft Motif](Draft_Pattern/fr.md).

## Script

Voir aussi: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour créer une Draft Forme à partir texte, utilisez la méthode `make_shapestring` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode dépréciée `makeShapeString`.


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```

-   Crée une forme composée `shapestring` à l\'aide du `String` spécifié et du chemin d\'accès complet d\'un `FontFile` pris en charge.

-    `Size`est la hauteur du texte obtenu en millimètres.

-    `Tracking`est l\'espacement supplémentaire entre les caractères en millimètres.

L\'emplacement de la Forme à partir de texte peut être modifié en écrasant ses attributs `Placement` ou en écrasant individuellement ses attributs `Placement.Base` et `Placement.Rotation`.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

font1 = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
font2 = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
font3 = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

S1 = Draft.make_shapestring("This is a sample text", font1, 200)

S2 = Draft.make_shapestring("Inclined text", font2, 200, 10)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(-1000, 500, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 45))
S2.Placement = place2

S3 = Draft.make_shapestring("Upside-down text", font3, 200, 10)
S3.Placement.Base = App.Vector(0, -1000, 0)
S3.Placement.Rotation = App.Rotation(zaxis, 180)

doc.recompute()
```





 
