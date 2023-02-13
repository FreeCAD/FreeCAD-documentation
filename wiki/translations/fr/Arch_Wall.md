---
- GuiCommand:/fr
   Name:Arch Wall
   Name/fr:Arch Mur
   MenuLocation:Arch → Mur
   Workbenches:[Arch](Arch_Workbench/fr.md)
   Shortcut:**W** **A**
   SeeAlso:[Arch Structure](Arch_Structure/fr.md)
---

# Arch Wall/fr

## Description

Cet outil crée un objet mur à partir de zéro ou sur la base de n\'importe quel objet basé sur une [forme de Part](Part_Workbench/fr.md) ou sur une [forme de Mesh](Mesh_Workbench/fr.md). Un mur peut être construit sans objet de base, il se comportera alors comme un volume cubique, il sera construit à l\'aide des propriétés de longueur, largeur et hauteur. Lorsque qu\'il est construit sur une forme existante, le mur peut être basé sur :

-   Un **objet linéaire 2D**, tel que ligne, fil, arc ou croquis, dans ce cas, vous pouvez modifier l\'épaisseur, l\'alignement (droite, gauche ou centré) et la hauteur. La propriété de longueur n\'a pas d\'effet.
-   Une **face plane**, dans ce cas, vous ne pouvez pas changer la hauteur. La propriété length (longueur) n\'a pas d\'effet. Si le base de la face est verticale, le mur utilisera la propriété largeur au lieu de la propriété hauteur, vous permettant de construire des murs à partir d\'objets en forme d\'espace ou d\'étude de masse.
-   Un **solide**, les propriétés de longueur, de largeur et de hauteur n\'ont aucun effet. Le mur utilise simplement le solide sous-jacent comme forme.
-   Un **maillage**, dans ce cas, sous-jacente doit être un solide fermé, solide manifold.

<img alt="" src=images/Arch_Wall_example.jpg  style="width:780px;"> 
*Murs construits à partir d'une ligne, d'une polyligne, d'une face, d'un solide et d'une esquisse*

Les murs peuvent également avoir des ajouts ou des soustractions. Les ajouts sont d\'autres objets dont les formes sont jointes dans la forme de ce mur, tandis que les soustractions sont soustraites. Des ajouts et des soustractions peuvent être ajoutés avec les outils [Ajouter](Arch_Add/fr.md) et [Supprimer](Arch_Remove/fr.md). Les ajouts et soustractions n\'ont aucune influence sur les paramètres de mur tels que la hauteur et la largeur, qui peuvent encore être modifiés. Les murs peuvent également avoir leur hauteur automatique, s\'ils sont inclus dans un objet de niveau supérieur tel que des [Niveaux](Arch_Floor/fr.md). La hauteur doit être maintenue à 0, puis le mur adoptera la hauteur spécifiée dans l\'objet parent.

Lorsque plusieurs murs doivent se croiser, vous devez les placer sur un [niveau](Arch_Floor/fr.md) pour avoir leurs géométries entrecoupées.



## Utilisation



### Dessiner un mur de zéro 

1.  Pressez le bouton **<img src="images/Arch_Wall.svg" width=16px> [Mur](Arch_Wall/fr.md)** ou pressez les touches **W** puis **A**.
2.  Cliquez le premier point dans la vue 3D ou rentrez des coordonnées.
3.  Cliquez le second point dans la vue 3D ou rentrez des coordonnées.



### Dessinez un mur sur un objet sélectionné 

1.  Sélectionnez un ou plusieurs objets géométriques de base (objet Draft, esquisse, etc)
2.  Cliquez sur le bouton **<img src="images/Arch_Wall.svg" width=16px> [Mur](Arch_Wall/fr.md)** ou pressez les touches **W** et **A**.
3.  Ajustez les propriétés nécessaires telles que, la hauteur ou la largeur.

## Options

-   Les murs partagent les propriétés et les comportements communs de tous les [Arch Composants](Arch_Component/fr.md)
-   La hauteur, la largeur et l\'alignement d\'un mur peuvent être définis lors du dessin, via le panneau des tâches
-   Lors de l\'accrochage d\'un mur à un mur existant, les deux murs seront joints en un seul. La manière dont les deux murs sont joints dépend de leurs propriétés: s\'ils ont la même largeur, hauteur et alignement, et si l\'option \"Joindre les esquisses de base\" est activée dans les préférences Arch, le mur résultant sera un objet basé sur une esquisse composé de plusieurs segments. Sinon, ce dernier mur sera ajouté au premier en tant qu\'addition.
-   Appuyez sur **X**, **Y** ou **Z** après le premier point pour contraindre le deuxième point sur l\'axe donné.
-   Pour entrer les coordonnées manuellement, entrez simplement les nombres, puis appuyez sur **Entrée** entre chaque composant X, Y et Z.
-   Appuyez sur **R** ou cliquez sur la case à cocher pour cocher/décocher le bouton **Relatif**. Si le mode relatif est activé, les coordonnées du deuxième point sont relatives au premier. Sinon, ils sont absolus, pris à partir du point d\'origine (0,0,0).
-   Appuyez sur **MAJ** tout en dessinant sur [Contrainte](Draft_Constrain/fr.md) votre deuxième point horizontalement ou verticalement par rapport au premier.
-   Appuyez sur **Echap** ou sur le bouton **Annuler** pour abandonner la commande en cours.
-   Double-cliquer sur le mur dans l\'arborescence après sa création vous permet d\'entrer en mode édition et d\'accéder et de modifier ses ajouts et soustractions
-   Les murs multicouches peuvent être facilement créés en construisant plusieurs murs à partir de la même ligne de base. En définissant leur propriété Align sur la gauche ou la droite et en spécifiant une valeur de décalage, vous pouvez créer efficacement plusieurs couches de murs. Placer une fenêtre dans un tel calque de mur propage l\'ouverture vers les autres calques de mur en fonction de la même ligne de base.
-   Les murs peuvent également utiliser [Arch Matériaux multiples](Arch_MultiMaterial/fr.md). Lors de l\'utilisation d\'un multi-matériau, le mur deviendra multi-couche, en utilisant les épaisseurs spécifiées par le multi-matériau. Toute couche d\'épaisseur zéro verra son épaisseur définie automatiquement par l\'espace restant défini par la valeur Largeur du mur, après avoir soustrait les autres couches.
-   Les murs peuvent être conçus pour afficher des blocs, au lieu d\'un seul solide, en activant leur propriété **Make Blocks**. La taille et le décalage des blocs peuvent être configurés avec différentes propriétés, et la quantité de blocs est automatiquement calculée. {{Version/fr|0.18}}



## Aimantation

L\'aimantation fonctionne un peu différemment avec les murs Arch par rapport aux autres objets Arch et Draft. Si un mur a un objet de ligne de base, l\'aimantation s\'ancrera à l\'objet de base, au lieu de la géométrie de mur, permettant d\'aligner facilement les murs par leur ligne de base. Si, cependant, vous souhaitez spécifiquement accrocher à la géométrie du mur, appuyez sur **Ctrl** pour basculer l\'aimantation à l\'objet mur.

<img alt="" src=images/Arch_wall_snap.jpg  style="width:780px;"> 
*Le deuxième mur s'aimante perpendiculairement au premier*



## Propriétés

Les objets mur héritent des propriétés de [Part](Part_Workbench/fr.md), et ont également les propriétés supplémentaires suivantes :

-    **Align**: alignement de la base du mur sur la base de référence : Gauche, Droite ou Centre

-    **Base**: objet de base sur lequel ce mur est construit

-    **Face**: index de la face de l\'objet de base utilisée. Si la valeur n\'est pas définie ou est 0, l\'objet entier est utilisé

-    **Force Wire**: si la valeur est True le mur est basé sur une face, seul le bord de la face est utilisée, résultant en un mur bordant la face

-    **Length**: longueur du mur (non utilisé lorsque le mur est basé sur une face)

-    **Width**: largeur du mur. (non utilisé lorsque le mur est basé sur une face)

-    **Height**: hauteur du mur (non utilisé lorsque le mur est basé sur une face). Si aucune hauteur n\'est donnée et que le mur est à l\'intérieur d\'un objet [Niveau](Arch_Floor/fr.md) avec sa hauteur définie, le mur prendra automatiquement la valeur de la hauteur de l\'étage.

-    **Normal**: donne une direction pour l\'extrusion du mur. Si la valeur est à (0,0,0), la direction d\'extrusion est automatique.

-    **Offset**: spécifie la distance entre le mur et le niveau de référence. Fonctionne uniquement si la propriété Align est à droite ou à gauche (Right ou Left).


{{Version/fr|0.18}}

-    **Make Blocks**: propriété pour créer les blocs

-    **Block Length**: longueur de chaque bloc

-    **Block Height**: hauteur de chaque bloc

-    **Offset First**: décalage horizontal de la première ligne de blocs

-    **Offset Second**: décalage horizontal de la deuxième ligne de blocs

-    **Joint**: taille des joints entre chaque bloc

-    **Count Entire**: nombre de blocs entiers (lecture seule)

-    **Count Broken**: nombre de blocs coupés (lecture seule)



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
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Wall/fr
