---
- GuiCommand:/fr
   Name:Arch Pipe
   Name/fr:Arch Tuyau
   MenuLocation:Arch → Outils pour la tuyauterie → Tuyau
   Workbenches:[Arch](Arch_Workbench/fr.md)
   Shortcut:**P** **I**
   Version:0.17
   SeeAlso:[Arch Raccord](Arch_PipeConnector/fr.md), [Arch Equipement](Arch_Equipment/fr.md)
---

# Arch Pipe/fr

## Description

Cet outil vous permet de créer un tube à partir de zéro ou à partir d\'objets basés sur (Draft, Sketch, etc..) sélectionnés et contenant une et une seule polyligne ouverte.

## Utilisation

1.  Sélectionnez une forme linéaire [Part](Part_Workbench/fr.md) telle qu\'une [Draft Ligne](Draft_Line/fr.md), un [Draft Polyligne](Draft_Wire.md) ou une [Esquisse](Sketcher_NewSketch/fr.md) ouverte.
2.  Appelez cette commande en utilisant plusieurs méthodes:
    -   En appuyant sur le bouton **<img src="images/Arch_Pipe.svg" width=16px> [Tuyau](Arch_Pipe/fr.md)** dans la barre d\'outils.
    -   En appuyant sur le raccourci clavier **P** puis **I**.
    -   Depuis **Arch → Outils pour la tuyauterie → Tuyau** dans le menu supérieur.

## Options

-   Tuyau partage les propriétés et comportements communs à tous les composants [Arch Composant](Arch_Component/fr.md)

## Propriétés

-    **Length**: Donne une longueur au tube, s\'il n\'est pas basé sur un fil (wire).

-    **Diameter**: Le diamètre du tube, s\'il n\'est pas basé sur un profil

-    **Base**: Le fil est basé seulement sur le tube

-    **Profile**: Le tube est basé sur le profil. S\'il n\'y a pas de profil, le tube est cylindrique.

## Processus de travail typique 

-   Commencez le placement des sanitaires hydrauliques (le fichier exemple ci dessous est un fichier step importé). Sélectionnez l\'objet et activez l\'Arch Equipments en cliquant sur le bouton [Arch Equipement](Arch_Equipment/fr.md).

![](images/Arch_pipe_example_01.jpg )

-   Dans Arch Equipments vous avez maintenant une nouvelle propriété **SnapPoints** qui est une liste de vecteurs 3D. Cela vous permet d\'ajouter des points d\'accrochage personnalisés, auxquels vous pouvez vous accrocher lorsque le bouton d\'accrochage [Draft Spécial](Draft_Snap_Special/fr.md) est activé. Actuellement, cette propriété n\'est cependant disponible que pour python. Dans le cas ci-dessus, j\'ai ajouté un nouveau point d\'accrochage à la sortie du wc. Les vecteurs à l\'intérieur des SnapPoints apparaissent sur le modèle sous forme de points blancs:

FreeCAD.ActiveDocument.Equipment.SnapPoints=[FreeCAD.Vector(0,0,100)]

![](images/Arch_pipe_example_02.jpg )

-   Avec [Draft Aimantation Spécial](Draft_Snap_Special/fr.md), vous pouvez maintenant vous accrocher sur tous ces points:

![](images/Arch_pipe_example_03.jpg )

-   Maintenant vous pouvez créer vos tubes en utilisant les fonctions Draft Lignes, Draft Polylignes ou Esquisses. La meilleure solution est d\'utiliser uniquement Draft Lignes:

![](images/Arch_pipe_example_04.jpg )

-   Il y a maintenant un nouvel outil [Draft Pente](Draft_Slope/fr.md) qui permet de donner une pente aux lignes, par exemple: 5% (0.05). Nous pouvons donc donner facilement une pente aux tubes de décharge. Seul la coordonnée Z est changée avec cet outil, il faut donner le départ et la fin, la coordonnées de départ (haut) reste inchangé.

![](images/Arch_pipe_example_05.jpg )

-   Maintenant nous n\'avons qu\'a sélectionner les lignes et cliquer sur le bouton [Arch Tuyau](Arch_Pipe/fr.md). Arch Tuyau travaille avec n\'importe quel objet ligne et seulement avec des lignes ouvertes.

![](images/Arch_pipe_example_06.jpg )

-   Vous pouvez maintenant créer des connexions avec deux ou trois tubes coïncidents en cliquant sur le bouton [Arch Raccord](Arch_PipeConnector/fr.md). Si vous sélectionnez trois tubes, deux tubes doivent être alignés pour créer un élément de départ:

![](images/Arch_pipe_example_07.jpg )

-   Changer le rayon de courbure ne modifie pas la longueur résultante du tracé des tubes (pour changer la résultante, vous devez changer le départ et l\'arrivée des tubes). Vous pouvez donc tracer votre chemin de lignes sans vous soucier des courbes et rayon des coudes.

Il est aussi possible de créer un tube sans ligne de base, dans ce cas utilisez la propriété \"Length\" pour définir la longueur.

## Script


**Voir aussi:**

[API](Arch_API/fr.md) and [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Tube peut être utilisé dans une [macro](macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante : 
```python
Pipe = makePipe(baseobj=None, diameter=0, length=0, placement=None, name="Pipe")
```

-   Creates a `Pipe` object from the given `baseobj` and `diameter`.
    -   
        `baseobj`
        
        is a [Draft Line](Draft_Line.md) or [Draft Wire](Draft_Wire.md).

    -   If `baseobj` is omitted, a straight pipe can be created with just the `diameter` and the `length` in the Z direction.
-   If a `placement` is given, it is used.


```python
import Draft, Arch

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2500, 200, 0)
p3 = FreeCAD.Vector(3100, 1000, 0)
p4 = FreeCAD.Vector(3500, 500, 0)
Line = Draft.makeWire([p1, p2, p3, p4])

Pipe = Arch.makePipe(Line, 200)
FreeCAD.ActiveDocument.recompute()

Pipe2 = Arch.makePipe(diameter=120, length=3000)
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Pipe/fr
