---
- GuiCommand:
   Name:Arch CurtainWall
   Name/fr:Arch Mur-rideau
   MenuLocation:Arch - Mur-rideau
   Workbenches:[Atelier Arch](Arch_Workbench/fr.md)
   Shortcut:**C** **W**
   Version:0.19
   SeeAlso:[Arch Mur](Arch_Wall/fr.md), [Arch Grille](Arch_Grid/fr.md)
---

# Arch CurtainWall/fr

## Description

Cet outil crée un [Mur-rideau](https://fr.wikipedia.org/wiki/Mur-rideau) en subdivisant une face de base en faces quadrangulaires puis en créant un meneau vertical sur les bords verticaux, des meneaux horizontaux sur les bords horizontaux et remplit les espaces entre les meneaux avec des panneaux.

<img alt="" src=images/Arch_CurtainWall_example.png  style="width:780px;">

Les murs-rideaux peuvent être créés à partir de n\'importe quel type d\'objet existant, auquel cas toutes les faces de l\'objet seront subdivisées. L\'outil fonctionne donc mieux s\'il est utilisé avec un objet qui n\'a qu\'une seule face. En règle générale, vous devez d\'abord créer une face, de préférence liée par exactement 4 arêtes, qui représente la zone que vous souhaitez remplir avec un mur-rideau, puis appliquer l\'outil.

Les murs-rideaux peuvent également être construits à partir d\'un objet linéaire, tel qu\'une ligne, un arc ou une polyligne, comme l\'outil [Arch Mur](Arch_Wall/fr.md).

Les faces à double courbure ou les faces à plus de 4 arêtes fonctionneront également mais le résultat est moins prévisible.

Les faces seront divisées en facettes quadrangulaires. Si les 4 points de la facette sont coplanaires, une facette carrée est créée. Sinon, il est divisé en deux triangles et un meneau diagonal est ajouté.

Si vous avez besoin d\'une subdivision non régulière, il est également possible de créer votre propre objet subdivisé, par exemple à l\'aide de [Arch Grille](Arch_Grid/fr.md) et de définir les subdivisions verticales et horizontales du mur-rideau sur 1.

Vous pouvez également utiliser l\'outil de mur-rideau sans aucun objet sélectionné, auquel cas vous pourrez dessiner une ligne de base, qui sera extrudée verticalement pour former la face sur laquelle le mur-rideau sera construit.



## Utilisation



### Dessiner un mur-rideau de zéro 

1.  Assurez-vous que rien n\'est sélectionné
2.  Appuyez sur le bouton **<img src="images/Arch_CurtainWall.svg" width=16px> [Mur-rideau](Arch_CurtainWall/fr.md)
** ou appuyez sur les touches **C** puis **W**
3.  Cliquez sur un premier point de la vue 3D ou rentrez des coordonnées
4.  Cliquez sur un deuxième point de la vue 3D ou rentrez des coordonnées
5.  Ajustez les propriétés nécessaires



### Création d\'un mur-rideau à partir d\'un objet sélectionné 

1.  Sélectionnez un ou plusieurs objets de géométrie de base (objet Draft, esquisse, etc).
2.  Appuyez sur le bouton **<img src="images/Arch_CurtainWall.svg" width=16px> [Mur-rideau](Arch_CurtainWall/fr.md)** ou appuyez sur les touches **C** puis **W**.
3.  Ajustez les propriétés nécessaires.

## Options

-   Les murs-rideaux partagent les propriétés et les comportements communs à tous les [Arch Composants](Arch_Component/fr.md)
-   Les meneaux des murs-rideaux peuvent être fabriqués à partir d\'un profil carré automatique (définissez leurs propriétés **Mullion Size** Taille de meneau) ou à partir d\'un profil personnalisé (définissez leur propriété **Mullion Profile** Profil de meneau). Les meneaux peuvent être centrés sur chaque arête ou placés relativement au point (0,0,0) en désactivant la propriété **Center Profile**. Par exemple, si vous voulez qu\'un profil soit placé légèrement derrière les panneaux, vous dessinerez ce profil légèrement en dessous du point d\'origine (0,0,0)
-   Les murs-rideaux supportent [Arch Matériaux multiples](Arch_MultiMaterial/fr.md). A l\'intérieur du multi-matériaux, la couche **Frame** sera utilisée pour les meneaux et la couche **Glass panel** pour les panneaux ou **Solid panel** si aucune couche de panneau de verre existe dans le multi-matériau.
-   Les murs-rideaux peuvent être basés sur un objet linéaire tel qu\'une ligne, un arc ou une polyligne. Dans ce cas, en interne, une surface de base sera construite en extrudant l\'objet linéaire selon la direction donnée par la propriété **Vertical Direction** par la longueur donnée par la propriété **Height**.



## Propriétés

Les objets Mur-rideau héritent des propriétés des objets [Arch Composants](Arch_Component/fr.md) et ont également des propriétés supplémentaires suivantes:

-    **Vertical Mullion Number**: nombre de meneaux verticaux

-    **Vertical Mullion Alignment**: si le profil des meneaux verticaux est aligné avec la surface ou non

-    **Vertical Sections**: nombre de sections verticales de ce mur-rideau

-    **Vertical Mullion Height**: hauteur du profil vertical des meneaux, si aucun profil n\'est utilisé

-    **Vertical Mullion Width**: largeur du profil vertical des meneaux, si aucun profil n\'est utilisé

-    **Vertical Mullion Profile**: profil pour les meneaux verticaux (désactive la taille des meneaux verticaux)

-    **Horizontal Mullion Number**: nombre de meneaux horizontaux

-    **Horizontal Mullion Alignment**: si le profil des meneaux horizontaux est aligné avec la surface ou non

-    **Horizontal Sections**: nombre de sections horizontales de ce mur-rideau

-    **Horizontal Mullion Height**: hauteur du profil des meneaux horizontaux, si aucun profil n\'est utilisé

-    **Horizontal Mullion Width**: largeur du profil des meneaux horizontaux, si aucun profil n\'est utilisé

-    **Horizontal Mullion Profile**: profil pour les meneaux horizontaux (désactive la taille des meneaux horizontaux)

-    **Diagonal Mullion Number**: nombre de meneaux diagonaux

-    **Diagonal Mullion Size**: taille des meneaux diagonaux, le cas échéant, si aucun profil n\'est utilisé

-    **Diagonal Mullion Profile**: profil pour les meneaux diagonaux, le cas échéant (désactive la taille des meneaux horizontaux)

-    **Panel Number**: nombre de panneaux

-    **Panel Thickness**: épaisseur des panneaux

-    **Swap Horizontal Vertical**: échange les lignes horizontales et verticales

-    **Refine**: effectuer des soustractions entre les composants afin qu\'ils ne se chevauchent pas

-    **Center Profiles**: centre le profil sur les bords ou non

-    **Vertical Direction**: référence de direction verticale à utiliser par cet objet pour déduire les directions verticales/horizontales. Maintenez-le proche de la direction verticale réelle de votre mur-rideau

-    **Height**: hauteur de ce mur-rideau, au cas où elle serait basée sur un objet linéaire

-    **Host**: hôte de ce mur-rideau. Le mur-rideau apparaîtra intégré dans son objet hôte dans l\'arborescence (aucune autre action n\'est effectuée)



## Faire des murs à ossature 

Les murs-rideaux sont pratiques à utiliser en conjonction avec des [Arch Murs](Arch_Wall/fr.md) pour créer des murs à ossature (murs où une couche structurelle intérieure est faite de cadres, généralement en bois ou en métal, au lieu d\'un matériau homogène comme le béton ou la brique) .

<img alt="" src=images/Frame_wall_example.png  style="width:780px;">

La procédure décrite ci-dessous crée un mur et un mur-rideau sur la base d\'une même ligne de base, puis donne au mur un multi-matériau qui laisse un espace vide, où le mur-rideau est placé:

1.  Créez un [Arch Mur](Arch_Wall/fr.md) normal, soit en cliquant sur deux points d\'un objet linéaire existant
2.  Sélectionnez l\'objet de base du mur d\'arc nouvellement créé
3.  Appuyez sur le bouton **<img src="images/Arch_CurtainWall.svg" width=16px> [Mur-rideau](Arch_CurtainWall/fr.md)** ou appuyez sur les touches **C** puis **W** pour créer un mur-rideau de la même ligne de base que le mur
4.  Assurez-vous que le mur et le mur-rideau ont la même **Hauteur**
5.  Définissez le nombre de **horizontal sections** du mur-rideau sur zéro si vous ne souhaitez que des cadres verticaux
6.  Définissez la **horizontal mullion width** (largeur horizontale du meneau) et **horizontal mullion height** (ou utilisez un profil de meneau)
7.  Préparez deux (ou plus) [Arch Matériau](Arch_SetMaterial/fr.md), un pour les panneaux, un pour le vide où le cadre sera
8.  Créez un [Arch Multi-matériau](Arch_MultiMaterial/fr.md), en utilisant une couche du matériau du panneau, une couche du matériau vide avec une valeur de largeur négative (ce qui le rendra non dessiné) correspondant à la hauteur verticale du meneau du mur-rideau et une autre couche de matériau de panneau
9.  Attribuer le multi-matériau au mur
10. Définissez la propriété **Host** du mur-rideau sur le mur que nous avons créé au premier point



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Mur-rideau peut être utilisé à l\'intérieur d\'une [macro](Macros/fr.md), et à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante : 
```python
MyCurtainWall = makeCurtainWall(baseobj)
```

Exemple:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseface = FreeCAD.ActiveDocument.addObject('Part::Extrusion','Extrusion')
baseface.Base = baseline
baseface.DirMode = "Normal"
baseface.LengthFwd = 2000
curtainwall = Arch.makeCurtainWall(baseface)
curtainWall.VerticalSections = 6
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CurtainWall/fr
