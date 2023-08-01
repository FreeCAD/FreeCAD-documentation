---
- GuiCommand:/fr
   Name:Part_Chamfer
   Name/fr:Part Chanfrein
   MenuLocation:Part → Chanfrein...
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Congé](Part_Fillet/fr.md)
---

# Part Chamfer/fr

## Description

**Part Chanfrein** applique un chanfrein sur le ou les bords sélectionnés d\'un objet. Une boîte de dialogue vous permet de choisir le ou les bords sur lesquels vous souhaitez travailler ainsi que de modifier divers paramètres de chanfrein.

![Exemple de chanfrein](images/Chamfer-example.png )



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Part_Chamfer.svg" width=16px> Chanfrein...**.
    -   Sélectionnez l\'option **Part → Chanfrein...** dans le menu.
2.  Sélectionnez la forme à chanfreiner dans la boîte de dialogue.
3.  Sélectionnez les arêtes à chanfreiner en cochant la case correspondante dans la boîte de dialogue de chanfreinage ou en les sélectionnant directement sur le modèle.
4.  Modifiez les paramètres du chanfrein.
5.  Appuyez sur **OK** pour fermer la boîte de dialogue de chanfrein et appliquer le chanfrein.

## Options

![Dialog-chamfer](images/Dialog-chamfer.png )

-   Lorsque vous sélectionnez des arêtes sur le modèle, vous avez la possibilité de les sélectionner par arête ou par face. La sélection par face sélectionne tous les bords de cette face.
-   Chanfrein de longueur constante ou chanfrein de longueur variable.
    -   Un chanfrein de longueur constante créera un chanfrein avec des bords équidistants du bord d\'origine à la distance spécifiée.
    -   Un chanfrein de longueur variable aura des arêtes pouvant être définies à des distances différentes de l\'arête d\'origine, ce qui vous permettra de créer un chanfrein à angle variable.



## Propriétés

![Part Propriétes du chanfrein](images/Part_Chamfer-Properties.png ) 


{{Properties_Title|Base}}

-    **Base**: forme sur laquelle le chanfrein doit être appliqué.

-    **Placement**: spécifie l\'orientation et la position de la forme dans l\'espace 3D.

-    **Label**: étiquette donnée à l\'objet. A changer en fonction de vos besoins.




## Limitations

Le chanfrein peut ne rien faire si le résultat touche ou traverse le bord adjacent suivant. Donc, si vous n\'obtenez pas le résultat attendu, essayez avec une valeur inférieure. C\'est pareil pour <img alt="" src=images/Part_Fillet.svg  style="width:24px;"> [Part Congé](Part_Fillet/fr.md).

Notez également que la fonction Chanfrein est affectée par le [problème de nommage topologique](Topological_naming_problem/fr.md) lorsque toute modification est apportée à une étape de modélisation plus tôt dans la chaîne qui affecte le nombre de facettes ou de sommets. Cela pourrait entraîner des résultats imprévisibles. En attendant que cela soit résolu, il est conseillé d'appliquer les opérations Chanfrein et <img alt="" src=images/Part_Fillet.svg  style="width:24px;"> [Part Congé](Part_Fillet/fr.md) aux dernières étapes de la chaîne.



## Script

L\'outil Chanfrein peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) en ajoutant un objet Chanfrein au document.

**Exemple de script :**


```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part::Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
chmfr = FreeCAD.ActiveDocument.addObject("Part::Chamfer", "myChamfer")
chmfr.Base = FreeCAD.ActiveDocument.myCube
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
chmfr.Edges = myEdges
FreeCADGui.ActiveDocument.myCube.Visibility = False
FreeCAD.ActiveDocument.recompute()
```

**Explication de l\'exemple du script :**


```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part::Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
```

-   Crée un cube de 5 mm sur lequel nous pouvons appliquer des bords chanfreinés. Voir [Part API](Part_API/fr.md) pour une explication de la méthode makeBox.


```python
chmfr = FreeCAD.ActiveDocument.addObject("Part::Chamfer", "myChamfer")
```

-   Ajoute un nouvel objet au document de type Chanfrein (de l\'atelier Part) avec le libellé \"myChamfer\".


```python
chmfr.Base = FreeCAD.ActiveDocument.myCube
```

-   Spécifie que la forme de base de l\'objet chanfrein doit être \"myCube\".


```python
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
```

-   Crée un tableau vide \"myEdges\" puis l\'ajoute aux paramètres de chanfrein de chaque bord.
-   La syntaxe pour chaque élément doit être (edge#, chamfer start length, chamfer end length) c\'est-à-dire (arête#, longueur du début du chanfrein, longueur de l\'extrémité du chanfrein).


```python
chmfr.Edges = myEdges
```

-   Définit l\'attribut Edges de notre objet Chamfer égal au tableau que nous venons de créer.


```python
FreeCADGui.ActiveDocument.myCube.Visibility = False
```

-   Cette ligne cache simplement \"myCube\" de sorte que notre objet \"myChamfer\" nouvellement créé soit le seul visible.


```python
FreeCAD.ActiveDocument.recompute()
```

-   Recalcule tous les composants modifiés à l\'écran et actualise l\'affichage.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Chamfer/fr
