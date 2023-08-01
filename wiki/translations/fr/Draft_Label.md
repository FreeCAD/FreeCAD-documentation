---
- GuiCommand:/fr
   Name:Draft Label
   Name/fr:Draft Étiquette
   MenuLocation:Annotation → Étiquette
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**D** **L**
   Version:0.17
   SeeAlso:[Draft Texte](Draft_Text/fr.md), [Draft Formes à partir texte](Draft_ShapeString/fr.md)
---

# Draft Label/fr

## Description

La commande <img alt="" src=images/Draft_Label.svg  style="width:24px;"> **Draft Étiquette** crée un texte de plusieurs lignes avec une ligne d\'attache à deux segments et une flèche.

Si un objet ou un sous-élément (face, arête ou sommet) est sélectionné au lancement de la commande, on peut faire en sorte que le texte affiche un ou deux attributs de l\'élément sélectionné, notamment la position, la longueur, l\'aire, le volume et le matériau. Le texte sera alors lié aux attributs et sera mis à jour si leurs valeurs changent.

Pour insérer un élément de texte sans flèche, utilisez plutôt la commande [Draft Texte](Draft_Text/fr.md).

<img alt="" src=images/Draft_Label_example.jpg  style="width:400px;"> 
*Différentes étiquettes avec différentes orientations, flèches et informations*



## Utilisation

Voir aussi : [Draft La barre](Draft_Tray/fr.md), [Draft Aimantation](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Sélectionnez éventuellement un objet ou un sous-élément (sommet, arête ou face) dont vous souhaitez afficher les attributs.
2.  Il existe plusieurs façons d\'invoquer la commande :
    -   Appuyez sur le **<img src="images/Draft_Label.svg" width=16px> [Étiquette](Draft_Label/fr.md)**.
    -   Sélectionnez l\'option **Annotation → <img src="images/Draft_Label.svg" width=16px> Étiquette** dans le menu.
    -   Utilisez le raccourci clavier : **D** puis **L**.
3.  Le panneau de tâches **Étiquette** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
4.  Si vous avez sélectionné un élément : sélectionnez une option dans la liste déroulante **Label type**. Voir [Types d\'étiquettes](#Label_types.md) ci-dessous.
5.  Choisissez le premier point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**. Ce point indique la cible (tête de flèche). Il peut se trouver n\'importe où, il n\'est pas nécessaire qu\'il soit sur un élément.
6.  Choisissez le deuxième point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**. Ce point indique le début du segment horizontal ou vertical de l\'amorce.
7.  Choisissez le troisième point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** bouton. Ce point indique le point de base du texte.

## Options

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut.

-   Pour saisir manuellement des coordonnées, entrez les valeurs X, Y et Z et appuyez sur **Entrée** après chacune. Ou bien vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Appuyez sur **R** ou cliquez sur la case **Relative** pour activer le mode relatif. Si le mode relatif est activé, les coordonnées sont relatives au dernier point, si disponible, sinon elles sont relatives à l\'origine du système de coordonnées.
-   Appuyez sur **G** ou cliquez sur la case **Global** pour activer le mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.20}}
-   Appuyez sur **S** pour activer ou désactiver [Draft Aimantation](Draft_Snap/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Fermer** pour abandonner la commande.



## Types d\'étiquettes 

Les types d\'étiquettes suivants sont disponibles :

-    {{Value|Custom}}: affiche le contenu de **Custom Text**.

-    {{Value|Name}}: affiche le nom interne de l\'objet cible. Le nom interne est attribué lors de la création de l\'objet et reste fixe pendant toute l\'existence de l\'objet.

-    {{Value|Label}}: affiche le libellé de l\'objet cible. Le libellé d\'un objet peut être modifié par l\'utilisateur.

-    {{Value|Position}}: affiche les coordonnées du point de base de l\'objet cible, du sommet cible ou du centre de masse du sous-élément cible, le cas échéant.

-    {{Value|Length}}: affiche la longueur de l\'objet ou du sous-élément cible, le cas échéant.

-    {{Value|Area}}: affiche la surface de l\'objet ou du sous-élément cible, le cas échéant.

-    {{Value|Volume}}: affiche le volume de l\'objet cible, le cas échéant.

-    {{Value|Tag}}: affiche l\'attribut `Tag` de l\'objet cible, le cas échéant. Les objets créés avec l\'[atelier Arch](Arch_Workbench/fr.md) peuvent avoir cet attribut.

-    {{Value|Matériau}}: affiche le libellé du matériau de l\'objet cible, le cas échéant.

-    {{Value|Label + Position}}: affiche le libellé du matériau de l\'objet cible, le cas échéant.

-    {{Value|Label + Longueur}}
    

-    {{Value|Label + Area}}
    

-    {{Value|Label + Volume}}
    

-    {{Value|Label + Material}}
    



## Remarques

-   La direction du deuxième segment de l\'amorce détermine l\'alignement du texte. Si le segment est horizontal et pointe vers la droite, le texte est aligné sur la gauche et vice versa. Si le deuxième segment va verticalement vers le haut, le texte est aligné sur la gauche. S\'il va verticalement vers le bas, le texte est aligné sur la droite.
-   Les Draft Étiquettes créées ou enregistrées avec la \[\[Release_notes_0.21/fr\|version 0.21\] de FreeCAD\] ne sont pas rétrocompatibles.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Etiquette est dérivé d\'un objet [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Les propriétés suivantes sont supplémentaires, sauf indication contraire :



### Données


{{TitleProperty|Base}}

-    **Custom Text|StringList**: spécifie le contenu du texte si **Label Type** est {{Value|Custom}} (personnalisé). Chaque élément de la liste représente une nouvelle ligne de texte.

-    **Label Type|Enumeration**: spécifie le type d\'information affiché par l\'étiquette. Voir [Types d\'étiquettes](#Types_d.27.C3.A9tiquettes.md).

-    **Placement|Placement**: spécifie la position du texte dans la [Vue 3D](3D_view/fr.md) et, à moins que **Straight Direction** ne soit {{Value|Custom}} (personnalisé), également du premier segment de tête, qui est le segment où le texte est rattaché. Voir [Placement](Placement/fr.md).

-    **Text|StringList**: (en lecture seule) spécifie le contenu du texte qui est effectivement affiché. Chaque élément de la liste représente une nouvelle ligne de texte.


{{TitleProperty|Leader}}

-    **Points|VectorList**: spécifie les points de l\'amorce.

-    **Straight Direction|Enumeration**: spécifie la direction du premier segment de l\'amorce : {{Value|Custom}}, {{Value|Horizontal}} ou {{Value|Vertical}}.

-    **Straight Distance|Distance**: spécifie la longueur du premier segment d\'amorce. Utilisé uniquement si **Straight Direction** est {{Value|Horizontale}} ou {{Value|Verticale}}. Si la distance est positive, l\'amorce part du côté droit du texte et le texte s\'aligne sur la droite. Sinon, l\'amorce part du côté gauche du texte et le texte s\'aligne sur la gauche.


{{TitleProperty|Target}}

-    **Target|LinkSub**: spécifie l\'objet et le sous-élément facultatif auquel l\'étiquette est liée.

-    **Target Point|Vector**: spécifie la position de la pointe de l\'amorce, qui est l\'endroit où la flèche est attachée.



### Vue


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: spécifie le style d\'annotation appliqué à l\'étiquette. Voir [Draft Editeur styles d\'annotations](Draft_AnnotationStyleEditor/fr.md).

-    **Scale Multiplier|Float**: spécifie le facteur d\'échelle général appliqué à l\'étiquette.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: spécifie comment le texte est affiché. S\'il s\'agit de {{value|World}}, le texte sera affiché sur un plan défini par la **Placement** de l\'étiquette. S\'il s\'agit de {{value|Screen}}, le texte sera toujours tourné vers l\'écran. Il s\'agit d\'une propriété héritée. Les options mentionnées sont les options renommées ({{Version/fr|0.21}}).


{{TitleProperty|Graphics}}

-    **Arrow Size|Length**: spécifie la taille du symbole affiché à l\'extrémité de la flèche.

-    **Arrow Type|Enumeration**: spécifie le type de symbole affiché à l\'extrémité de l\'amorce, qui peut être {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} ou {{value|Tick-2}}.

-    **Frame|Enumeration**: spécifie le type de cadre dessiné autour du texte. Les options actuelles sont {{Value|None}} ou {{Value|Rectangle}}.

-    **Line|Bool**: indique s\'il faut afficher la ligne d\'attache. S\'il est `False`, seuls la flèche et le texte sont affichés.

-    **Line Color|Color**: spécifie la couleur de l\'amorce et de la flèche. Également utilisée pour le cadre ({{Version/fr|0.20}}).

-    **Line Width|Float**: spécifie la largeur de l\'amorce. Également utilisé pour le cadre ({{Version/fr|0.20}}).


{{TitleProperty|Text}}

-    **Text Name|Font**: spécifie la police utilisée pour dessiner le texte. Il peut s\'agir d\'un nom de police, tel que {{value|Arial}}, d\'un style par défaut tel que {{value|sans}}, {{value|serif}} ou {{value|mono}}, d\'une famille telle que {{value|Arial,Helvetica,sans}}, ou d\'un nom avec un style tel que {{value|Arial:Bold}}. Si la police donnée n\'est pas trouvée sur le système, une police par défaut est utilisée à la place. {{Version/fr|0.21}}

-    **Font Size|Length**: spécifie la taille des lettres. Le texte peut être invisible dans la [Vue 3D](3D_view/fr.md) si cette valeur est très petite. {{Version/fr|0.21}}

-    **Justification|Enumeration**: spécifie l\'alignement horizontal du texte : {{value|Left}}, {{value|Center}} ou {{value|Right}}. Utilisé uniquement si **Straight Direction** est {{Value|Custom}} (personnalisée). Sinon, l\'alignement horizontal est basé sur le signe (positif ou négatif) de **Straight Distance**.

-    **Line Spacing|Float**: spécifie le facteur appliqué à la hauteur de ligne par défaut du texte.

-    **Max Chars|Integer**: spécifie le nombre maximum de caractères sur chaque ligne du texte.

-    **Text Alignment|Enumeration**: spécifie l\'alignement vertical du texte : {{value|Top}}, {{value|Middle}} ou {{value|Bottom}}.

-    **Text Color|Color**: spécifie la couleur du texte.



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Pour créer une Draft Étiquette, utilisez la méthode `make_label` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode dépréciée `makeLabel`.


```python
label = make_label(target_point=App.Vector(0, 0, 0),
                   placement=App.Vector(30, 30, 0),
                   target_object=None, subelements=None,
                   label_type="Custom", custom_text="Label",
                   direction="Horizontal", distance=-10,
                   points=None)
```

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(4000, 1000)
doc.recompute()

p1 = App.Vector(-200, 1000, 0)
place1 = App.Placement(App.Vector(-1000, 1300, 0), App.Rotation())

label1 = Draft.make_label(p1, place1, target_object=rectangle, distance=500, label_type="Label")
label1.ViewObject.TextSize = 200

p2 = App.Vector(-200, 0, 0)
place2 = App.Placement(App.Vector(-1000, -300, 0), App.Rotation())

label2 = Draft.make_label(p2, place2, target_object=rectangle, distance=500, label_type="Custom",
                          custom_text="Beware of the sharp edges")
label2.ViewObject.TextSize = 200

p3 = App.Vector(1000, 1200, 0)
place3 = App.Placement(App.Vector(2000, 1800, 0), App.Rotation())

label3 = Draft.make_label(p3, place3, target_object=rectangle, distance=-500, label_type="Area")
label3.ViewObject.TextSize = 200

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Label/fr
