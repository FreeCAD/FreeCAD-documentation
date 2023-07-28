---
- GuiCommand:/fr
   Name:Draft Text
   Name/fr:Draft Texte
   MenuLocation:Annotation → Texte
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**T** **E**
   Version:0.7
   SeeAlso:[Draft Étiquette](Draft_Label/fr.md), [Draft Formes à partir de texte](Draft_ShapeString/fr.md)
---

# Draft Text/fr

## Description

La commande <img alt="" src=images/Draft_Text.svg  style="width:24px;"> **Draft Texte** crée un texte de plusieurs lignes à un endroit donné.

Pour créer un élément de texte avec une flèche, utilisez plutôt la commande [Draft Étiquette](Draft_Label/fr.md).

<img alt="" src=images/Draft_Text_example.png  style="width:400px;"> 
*Un seul point est nécessaire pour positionner le texte*



## Utilisation

Voir aussi : [Draft La barre](Draft_Tray/fr.md) et [Draft Aimantation](Draft_Snap/fr.md).

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Text.svg" width=16px> [Texte](Draft_Text/fr.md)**.
    -   Sélectionnez l\'option **Annotation → <img src="images/Draft_Text.svg" width=16px> Texte** dans le menu.
    -   Utilisez le raccourci clavier : **T** puis **E**.
2.  Le panneau de tâches **Text** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Choisissez un point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
4.  Saisissez le texte souhaité, appuyez sur **Entrée** pour commencer une nouvelle ligne.
5.  Appuyez deux fois sur **Entrée** ou sur le bouton **<img src="images/Button_valid.svg" width=16px> Insérer du texte** pour terminer la commande.

## Options

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut.

-   Pour saisir manuellement des coordonnées, entrez les valeurs de X, Y et Z et appuyez sur **Entrée** après chacune, ou vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Appuyez sur **G** ou cliquez sur la case **Global** pour basculer en mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.20}}
-   Appuyez sur **T** ou cliquez sur la case **Continuer** pour activer le mode continu. Si le mode continu est activé, la commande redémarre après avoir terminé, ce qui vous permet de continuer à créer des textes. Le raccourci ne fonctionne pas dans le deuxième panneau de tâches. Cette option n\'est pas disponible dans le premier panneau de tâches dans FreeCAD version 0.19 et antérieure.
-   Appuyez sur **S** pour activer ou désactiver [Draft Aimantation](Draft_Snap/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Fermer** pour interrompre la commande.



## Remarques

-   Un Draft Texte peut être édité en double-cliquant dessus dans l\'arborescence. {{Version/fr|0.20}}
-   Les Draft Textes créés ou sauvegardés avec la [version 0.21 de FreeCAD](Release_notes_0.21/fr.md) ne sont pas rétrocompatibles.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Texte est dérivé d\'un objet [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Les propriétés suivantes sont supplémentaires, sauf indication contraire :



### Données


{{TitleProperty|Base}}

-    **Placement|Placement**: spécifie la position du texte dans la [Vue 3D](3D_view/fr.md). Voir [Placement](Placement/fr.md).

-    **Text|StringList**: spécifie le contenu du texte. Chaque élément de la liste représente une nouvelle ligne de texte.



### Vue


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: spécifie le style d\'annotation appliqué au texte. Voir [Draft Éditeur styles d\'annotations](Draft_AnnotationStyleEditor/fr.md).

-    **Scale Multiplier|Float**: spécifie le facteur d\'échelle général appliqué au texte.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: spécifie comment le texte est affiché. S\'il s\'agit de {{value|World}}, le texte sera affiché sur un plan défini par sa **Placement**. S\'il s\'agit de {{value|Screen}}, le texte sera toujours tourné vers l\'écran. Il s\'agit d\'une propriété héritée. Les options mentionnées sont les options renommées ({{Version/fr|0.21}}).


{{TitleProperty|Graphics}}

-    **Line Color|Color**: non utilisé.

-    **Line Width|Float**: non utilisé.


{{TitleProperty|Text}}

-    **Font Name|Font**: spécifie la police utilisée pour dessiner le texte. Il peut s\'agir d\'un nom de police, tel que {{value|Arial}}, d\'un style par défaut tel que {{value|sans}}, {{value|serif}} ou {{value|mono}}, d\'une famille telle que {{value|Arial,Helvetica,sans}}, ou d\'un nom avec un style tel que {{value|Arial:Bold}}. Si la police donnée n\'est pas trouvée sur le système, une police par défaut est utilisée à la place.

-    **Font Size|Length**: spécifie la taille des lettres. Le texte peut être invisible dans la [Vue 3D](3D_view/fr.md) si cette valeur est très petite.

-    **Justification|Enumeration**: spécifie si l\'alignement du texte : {{value|Left}}, {{value|Center}} ou {{value|Right}}.

-    **Line Spacing|Float**: spécifie le facteur appliqué à la hauteur de ligne par défaut du texte.

-    **Text Color|Color**: spécifie la couleur du texte.



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Pour créer un Draft Texte, utilisez la méthode `make_text` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode dépréciée `makeText`.


```python
text = make_text(string, placement=None, screen=False)
```

-   Crée un objet `text`, au `placement` qui peut être un `FreeCAD.Placement` mais aussi une `FreeCAD.Rotation` ou un `FreeCAD.Vector`.

-    `string`est une chaîne de caractères ou une liste de chaînes de caractères. Si c\'est une liste, chaque élément est affiché sur sa propre ligne.

-   Si `screen` est `True`, le texte fait toujours face à la caméra, sinon il est affiché dans un plan défini par **Placement**.

Les propriétés d\'affichage de `text` peuvent être modifiées en écrasant ses attributs, par exemple en changeant `ViewObject.FontSize` avec la nouvelle taille en millimètres.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

t1 = "This is a sample text"
p1 = App.Vector(0, 0, 0)

t2 = ["First line", "second line"]
p2 = App.Vector(1000, 1000, 0)

text1 = Draft.make_text(t1, p1)
text2 = Draft.make_text(t2, p2)
text1.ViewObject.FontSize = 200
text2.ViewObject.FontSize = 200

zaxis = App.Vector(0, 0, 1)

t3 = ["Upside", "down"]
p3 = App.Vector(-1000, -500, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 180))
text3 = Draft.make_text(t3, place3)
text3.ViewObject.FontSize = 200

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Text/fr
