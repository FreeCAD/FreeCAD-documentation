---
- GuiCommand:/fr
   Name:Draft Hatch
   Name/fr:Draft Hachure
   MenuLocation:Drafting → Hachure
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**H** **A**
   Version:0.20
   SeeAlso:[Draft Motif](Draft_Pattern/fr.md)
---

# Draft Hatch/fr

## Description

La commande <img alt="" src=images/Draft_Hatch.svg  style="width:24px;"> **Draft Hachure** crée des hachures sur les faces planes d\'un objet sélectionné.

## Utilisation

1.  Sélectionnez un objet avec des faces. Seules les faces planes de l\'objet seront hachurées.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Hatch.svg" width=16px> [Hachure](Draft_Hatch/fr.md)**.
    -   Sélectionnez l\'option **Drafting → <img src="images/Draft_Hatch.svg" width=16px> Hachure** dans le menu.
    -   Utilisez le raccourci clavier : **H** puis **A**.
3.  Le panneau de tâches **Hatch** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
4.  Appuyez sur le bouton **OK** pour terminer la commande.

## Options

-   Appuyez sur le bouton **...** pour sélectionner un **Fichier PAT**. Voir [Remarques](#Remarques.md).
-   Sélectionnez un motif **Motif** dans le fichier. Il est actuellement conseillé d\'éviter les motifs avec des lignes pointillées.
-   Spécifiez une échelle **Échelle** pour le motif.
-   Spécifiez un **Rotation** pour le motif.
-   Appuyez sur **Échap** ou sur le bouton **Annuler** pour interrompre la commande.

## Alignement des motifs 

Lorsque le motif de hachures d\'une face est calculé, il est temporairement traduit dans le plan XY global par défaut. Pour une face avec des bords droits, le premier bord droit détermine comment cela se passe. Le premier point de cette arête est placé sur l\'origine, et l\'arête elle-même est alignée avec l\'axe X. Si vous créez une [Draft Polyligne](Draft_Wire/fr.md) dans cette optique, vous pouvez contrôler la façon dont le motif de hachures est aligné avec le contour de la face.

Si toutes les faces de l\'objet sélectionné se trouvent sur le plan XY global, vous pouvez désactiver ce comportement par défaut en définissant la propriété **Translate** de l\'ébauche de hachure sur `False`. Le motif de hachures est alors aligné sur l\'origine et l\'axe X du système de coordonnées global. Pour les faces du plan XY à bords droits, la propriété **Translate** peut être utilisée pour basculer entre les motifs absolus (à gauche dans l\'image) et relatifs (à droite dans l\'image).

<img alt="" src=images/Draft_Hatch_alignment.png  style="width:400px;"> 
*
Deux Draft Polylignes avec des hachures.<br>
Les polylignes ont été créées dans une direction sens horaire en partant du point inférieur gauche.<br>
Pour la hachure à gauche, la propriété Translate est réglée sur false.<br>
Pour la hachure à droite, elle est réglée sur true.
*

## Remarques

-   Pour l\'instant, le conseil est de télécharger un fichier PAT. Vous pouvez en trouver beaucoup en ligne. Vous pouvez par exemple faire une recherche sur le web pour {{FileName|acad.pat}} ou {{FileName|acadiso.pat}}.
-   Un petit fichier PAT est installé avec FreeCAD : {{FileName|<program_folder>/data/Mod/TechDraw/PAT/FCPAT.pat}}, où {{FileName|<program_folder>}} est le dossier du programme FreeCAD :
    -   Sous Linux c\'est généralement {{FileName|/usr/share/freecad}}.
    -   Sous Windows, il s\'agit généralement de {{FileName|C:\Program Files\FreeCAD}}.
    -   Sous macOS, il s\'agit généralement de {{FileName|/Applications/FreeCAD}}.

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

Les préférences suivantes sont en jeu :

-   Fichier PAT : **Outils → Modifier les paramètres... → BaseApp → Preferences → Mod → TechDraw → PAT → FilePattern**.
-   Motif : **Outils → Modifier les paramètres... → BaseApp → Preferences → Mod → TechDraw → PAT → NamePattern**.
-   Échelle : **Outils → Modifier les paramètres... → BaseApp → Preferences → Mod → Draft → HatchPatternScale**.
-   Rotation : **Outils → Modifier les paramètres... → BaseApp → Preferences → Mod → Draft → HatchPatternRotation**.

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Hachure est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{TitleProperty|Hatch}}

-    **Base|Link**: spécifie l\'objet dont les faces sont hachurées.

-    **File|File**: spécifie le fichier PAT.

-    **Pattern|String**: spécifie le nom du motif.

-    **Rotation|Angle**: spécifie la rotation du motif.

-    **Scale|Float**: spécifie l\'échelle du motif.

-    **Translate|Bool**: indique si les faces sont temporairement translatées dans le plan XY global pendant le processus de hachurage. La valeur `False` peut donner de mauvais résultats pour les faces non XY.

## Script

Voir aussi: _.

Pour créer un Draft Hachure, utilisez la méthode `make_hatch` du module Draft :


```python
hatch = make_hatch(baseobject, filename, pattern, scale, rotation)
```

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(4000, 1000)
rectangle.MakeFace = True
filename = App.getHomePath() + "data/Mod/TechDraw/PAT/FCPAT.pat"
pattern = "Horizontal5"
hatch = Draft.make_hatch(rectangle, filename, pattern, scale=50, rotation=45)

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Hatch/fr
