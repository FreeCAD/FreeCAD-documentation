---
 GuiCommand:
   Name: Arch Wall
   Name/fr: Arch Mur
   MenuLocation: 3D/BIM , Mur
   Workbenches: BIM_Workbench/fr
   Shortcut: **W** **A**
   SeeAlso: 
---

# Arch Wall/fr

## Description

L\'outil **Arch Mur** crée un objet mur à partir de zéro ou sur la base de n\'importe quel objet basé sur une [forme de Part](Part_Workbench/fr.md) ou sur une [forme de Mesh](Mesh_Workbench/fr.md). Un mur peut être construit sans objet de base, il se comportera alors comme un volume cubique, il sera construit à l\'aide des propriétés de longueur, largeur et hauteur. Lorsque qu\'il est construit sur une forme existante, le mur peut être basé sur :

-   Un **objet linéaire 2D**, tel que des lignes, polylignes, arcs ou esquisses, dans ce cas, vous pouvez modifier l\'épaisseur, l\'alignement (droite, gauche ou centré) et la hauteur. La propriété de longueur n\'a pas d\'effet.
-   Une **face plane**, dans ce cas, vous ne pouvez pas changer la hauteur. La propriété length (longueur) n\'a pas d\'effet. Si le base de la face est verticale, le mur utilisera la propriété largeur au lieu de la propriété hauteur, vous permettant de construire des murs à partir d\'objets en forme d\'espace ou d\'étude de masse.
-   Un **solide**, les propriétés de longueur, de largeur et de hauteur n\'ont aucun effet. Le mur utilise simplement le solide sous-jacent comme forme.
-   Un **maillage**, dans ce cas, sous-jacente doit être un solide fermé, solide manifold.

<img alt="" src=images/Arch_Wall_example.jpg  style="width:780px;"> 
*Murs construits à partir d'une ligne, d'une polyligne, d'une face, d'un solide et d'une esquisse*

Les murs peuvent également avoir des ajouts ou des soustractions. Les ajouts sont d\'autres objets dont les formes sont jointes dans la forme de ce mur, tandis que les soustractions sont soustraites. Des ajouts et des soustractions peuvent être ajoutés avec les outils [Ajouter](Arch_Add/fr.md) et [Supprimer](Arch_Remove/fr.md). Les ajouts et soustractions n\'ont aucune influence sur les paramètres de mur tels que la hauteur et la largeur, qui peuvent encore être modifiés. Les murs peuvent également avoir leur hauteur automatique, s\'ils sont inclus dans un objet de niveau supérieur tel que des [Niveaux](Arch_Floor/fr.md). La hauteur doit être maintenue à 0, puis le mur adoptera la hauteur spécifiée dans l\'objet parent.

Lorsque plusieurs murs doivent se croiser, vous devez les placer sur un [niveau](Arch_Floor/fr.md) pour avoir leurs géométries entrecoupées.



## Utilisation



### Dessiner un mur de zéro 

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Arch_Wall.svg" width=16px> [Mur](Arch_Wall/fr.md)**.
    -   Sélectionnez l\'option **3D/BIM → <img src="images/Arch_Wall.svg" width=16px> Mur** du menu.
    -   Utilisez le raccourci clavier : **W** puis **A**.
2.  Cliquez sur un premier point de la vue 3D, ou tapez les coordonnées.
3.  Cliquez sur un deuxième point de la vue 3D, ou tapez les coordonnées.



### Dessiner un mur sur un objet sélectionné 

1.  Sélectionnez un ou plusieurs objets géométriques de base (objet Draft, esquisse, etc).
2.  Lancez l\'outil comme décrit ci-dessus.
3.  Ajustez les propriétés nécessaires telles que, la hauteur ou la largeur.

## Options

-   Les murs partagent les propriétés et les comportements communs de tous les [Arch Composants](Arch_Component/fr.md)
-   La hauteur, la largeur et l\'alignement d\'un mur peuvent être définis lors du dessin, via le panneau des tâches
-   Lors de l\'accrochage d\'un mur à un mur existant, les deux murs seront joints en un seul. La manière dont les deux murs sont joints dépend de leurs propriétés: s\'ils ont la même largeur, hauteur et alignement, et si l\'option \"Joindre les esquisses de base\" est activée dans les préférences Arch, le mur résultant sera un objet basé sur une esquisse composé de plusieurs segments. Sinon, ce dernier mur sera ajouté au premier en tant qu\'addition.
-   Appuyez sur **X**, **Y** ou **Z** après le premier point pour contraindre le deuxième point sur l\'axe donné.
-   Pour entrer les coordonnées manuellement, entrez simplement les nombres, puis appuyez sur **Entrée** entre chaque composant X, Y et Z.
-   Appuyez sur **R** ou cliquez sur la case à cocher pour cocher/décocher le bouton **Relatif**. Si le mode relatif est activé, les coordonnées du deuxième point sont relatives au premier. Sinon, ils sont absolus, pris à partir du point d\'origine (0,0,0).
-   Appuyez sur **MAJ** tout en dessinant sur [Contrainte](Draft_Constrain/fr.md) votre deuxième point horizontalement ou verticalement par rapport au premier.
-   Appuyez sur **Échap** ou sur le bouton **Annuler** pour abandonner la commande en cours.
-   Double-cliquer sur le mur dans l\'arborescence après sa création vous permet d\'entrer en mode édition et d\'accéder et de modifier ses ajouts et soustractions
-   Les murs multicouches peuvent être facilement créés en construisant plusieurs murs à partir de la même ligne de base. En définissant leur propriété Align sur la gauche ou la droite et en spécifiant une valeur de décalage, vous pouvez créer efficacement plusieurs couches de murs. Placer une fenêtre dans un tel calque de mur propage l\'ouverture vers les autres calques de mur en fonction de la même ligne de base.
-   Les murs peuvent également utiliser un [Arch Multi-matériaux](Arch_MultiMaterial/fr.md). Lors de l\'utilisation d\'un multi-matériaux, le mur deviendra multi-couche, en utilisant les épaisseurs spécifiées par le multi-matériaux. Toute couche d\'épaisseur zéro verra son épaisseur définie automatiquement par l\'espace restant défini par la valeur Largeur du mur, après avoir soustrait les autres couches.
-   Les murs peuvent être conçus pour afficher des blocs, au lieu d\'un seul solide, en activant leur propriété **Make Blocks**. La taille et le décalage des blocs peuvent être configurés avec différentes propriétés, et la quantité de blocs est automatiquement calculée.



## Aimantation

L\'aimantation fonctionne un peu différemment avec les murs Arch par rapport aux autres objets Arch et Draft. Si un mur a un objet de ligne de base, l\'aimantation s\'ancrera à l\'objet de base, au lieu de la géométrie de mur, permettant d\'aligner facilement les murs par leur ligne de base. Si, cependant, vous souhaitez spécifiquement accrocher à la géométrie du mur, appuyez sur **Ctrl** pour basculer l\'aimantation à l\'objet mur.

<img alt="" src=images/Arch_wall_snap.jpg  style="width:780px;"> 
*Le deuxième mur s'aimante perpendiculairement au premier*



## Propriétés

Les objets Wall héritent des propriétés des objets [Part](Part_Workbench.md) et ont également des propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Blocks}}

-    **Block Height**: hauteur de chaque bloc.

-    **Block Length**: longueur de chaque bloc.

-    **Count Broken**: nombre de blocs coupés (lecture seule).

-    **Count Entire**: nombre de blocs entiers (lecture seule).

-    **Joint**: taille des joints, l\'espace vide, entre les blocs.

-    **Make Blocks**: active la génération de blocs.

-    **Offset First**: décalage horizontal de la première ligne de blocs et de toutes les lignes inégales.

-    **Offset Second**: décalage horizontal de la deuxième ligne de blocs et de toutes les lignes paires.


{{TitleProperty|Component}}

Voir [Arch Composant](Arch_Component/fr#Propriétés.md).


{{TitleProperty|IFC}}

Voir [Arch Composant](Arch_Component/fr#Propriétés.md).


{{TitleProperty|IFC Attributes}}

Voir [Arch Composant](Arch_Component/fr#Propriétés.md).


{{TitleProperty|Wall}}

-    **Align**: alignement de la base du mur sur la base de référence : Gauche, Droite ou Centre. La direction de chaque arête de l\'objet de base (Sketch/ArchSketch) est prise en compte, ce qui permet un contrôle plus fin de chaque segment de mur. Voir le schéma ci-dessous. Dans les esquisses, les arcs sont toujours orientés dans le sens inverse des aiguilles d\'une montre. Lorsqu\'un segment courbe d\'un mur est aligné à gauche, l\'arête intérieure du segment correspond à l\'arc de l\'esquisse. Voir aussi **Override Align**.

-    **Area**: surface du mur entier, la séparation en blocs ne fait aucune différence (en lecture seule).

-    **Face**: index de la face de l\'objet de base utilisée. Si la valeur n\'est pas définie ou est 0, l\'objet entier est utilisé

-    **Height**: hauteur du mur. Ignoré si le mur est basé sur un solide. S\'il vaut zéro et que le mur se trouve à l\'intérieur d\'un objet [Niveau](Arch_Floor/fr.md) dont la hauteur est définie, le mur prendra automatiquement la valeur de la hauteur l\'étage.

-    **Length**: longueur du mur. La valeur peut être éditée si le mur est basé sur une esquisse non contrainte avec une seule arête, ou sur une [Draft Polyligne](Draft_Wire/fr.md) avec une seule arête, sinon la valeur est en lecture seule. {{Version/fr|1.0}} La valeur lorsque la propriété est en lecture seule est plus précise. Elle est basée sur le milieu du mur si les segments ont des propriétés **Width**, **Align** et/ou **Offset** différentes. Notez que des imprécisions peuvent subsister si le mur est complexe, par exemple s\'il présente des jonctions en T ou des auto-intersections. Dans ce cas, il est conseillé d\'utiliser la propriété **Horizontal Area** pour effectuer d\'autres calculs.

-    **Normal**: donne une direction pour l\'extrusion du mur. Si la valeur est à (0,0,0), la direction d\'extrusion est automatique.

-    **Offset**: spécifie la distance entre le mur et le niveau de référence. Fonctionne uniquement si la propriété **Align** est à droite ou à gauche. La direction de chaque arête de l\'objet Base (Sketch/ArchSketch) est prise en compte, ce qui permet un contrôle plus fin de chaque segment de mur. Voir aussi **Override Offset**.

-    **Override Align**: cette propriété remplace l\'attribut **Align** pour définir l\'alignement de chaque segment du mur. Elle est ignorée si l\'objet de base fournit des informations sur l\'alignement avec la méthode getAligns() (si une valeur n\'est pas \"Left, Right, Center\", la valeur de \"Align\" sera appliquée). AMÉLIORATION par ArchSketch : l\'outil d\'interface graphique \"Edit Wall Segment Align\" est fourni avec l\'<img alt="" src=images/SketchArch_Workbench.svg  style="width:16px;"> [extension SketchArch](https://github.com/paullee0/FreeCAD_SketchArch) pour permettre aux utilisateurs de définir les valeurs de manière interactive. \"Tolérant au problème de dénomination topologique\" si ArchSketch est utilisé dans la base (et si le module complémentaire SketchArch est installé). Attention : non \"Tolérant au problème de dénomination topologique\" si seulement Sketch est utilisé.

-    **Override Width**: cet attribut remplace l\'attribut **Width** pour définir la largeur de chaque segment du mur. Elle est ignorée si l\'objet de base fournit des informations sur les largeurs, avec la méthode getWidths() (si une valeur est nulle, la valeur de \"Width\" sera appliquée). AMÉLIORATION par ArchSketch : l\'outil d\'interface graphique \"Edit Wall Segment Width\" est fourni avec l\'<img alt="" src=images/SketchArch_Workbench.svg  style="width:16px;"> [extension SketchArch](https://github.com/paullee0/FreeCAD_SketchArch) pour permettre aux utilisateurs de définir les valeurs de manière interactive. \"Tolérant au problème de dénomination topologique\" si ArchSketch est utilisé dans la base (et si le module complémentaire SketchArch est installé). Attention : non \"Tolérant au problème de dénomination topologique\" si seulement Sketch est utilisé.

-    **Override Offset**: ({{Version/fr|1.0}}) cette propriété remplace l\'attribut **Offset** pour définir le décalage de chaque segment de mur. Elle est ignorée si l\'objet de base fournit des informations sur les décalages, avec la méthode getOffsets() (si une valeur est nulle, la valeur de \"Offset\" sera appliquée). AMÉLIORATION par ArchSketch : l\'outil d\'interface graphique \"Edit Wall Segment Offset\" est fourni avec l\'<img alt="" src=images/SketchArch_Workbench.svg  style="width:16px;"> [extension SketchArch](https://github.com/paullee0/FreeCAD_SketchArch) pour permettre aux utilisateurs de sélectionner les bords de manière interactive. \"Tolérant au problème de dénomination topologique\" si ArchSketch est utilisé dans la base (et si le module complémentaire SketchArch est installé). Attention : non \"Tolérant au problème de dénomination topologique\" si seulement Sketch est utilisé. La propriété est ignorée si Base d\'ArchSketch a fourni les arêtes sélectionnées.

-    **Width**: largeur du mur. Ignoré si le mur est basé sur une face ou un solide. Voir aussi **Override Width**.

<img alt="" src=images/Sketch_vs_Wall.jpg  style="width:480px;">



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Mur peut servir dans une [macro](Macros/fr.md), et, à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
Wall = makeWall(baseobj=None, length=None, width=None, height=None, align="Center", face=None, name="Wall")
```

-   Crée un objet `Mur` à partir d\'`objet` donné, qui peut être un [objet Draft](Draft_Workbench/fr.md), un [objet Sketch](Sketcher_Workbench/fr.md), une face ou un solide.
    -   Si aucun `objet` n\'est indiqué, vous pouvez fournir les valeurs numériques pour `longueur`, `largeur` (épaisseur) et `hauteur`.
    -   Si donné, `face` peut être utilisé pour donner l\'index d\'une face à partir de l\'objet sous-jacent, pour construire ce mur, au lieu d\'utiliser tout l\'objet.

-    `align`peut être au `"Centre"`, à `"Gauche"` ou à `"Droite"`.

-   Il renvoie `None` si l\'opération échoue.

Exemple :


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
Draft.move(Wall2, FreeCAD.Vector(0, -1000, 0))
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Wall/fr
