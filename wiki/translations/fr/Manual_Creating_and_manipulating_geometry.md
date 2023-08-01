# Manual:Creating and manipulating geometry/fr
{{Manual:TOC/fr}}

Dans les chapitres précédents, nous avons appris les différents ateliers de FreeCAD et chacun d\'entre eux met en œuvre ses propres outils et types de géométrie. Les mêmes concepts s\'appliquent lorsque vous travaillez à partir du code Python.

Nous avons également vu que la grande majorité des ateliers de FreeCAD dépendent d\'un atelier extrêmement important: l'[atelier Part](Part_Workbench/fr.md). En fait, d\'autres ateliers tels que [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) font exactement ce que nous allons faire dans ce chapitre: ils utilisent le code Python pour créer et manipuler la géométrie Part.

Donc, la première chose que nous devons faire pour travailler avec la géométrie des pièces, c\'est de faire l'équivalent en Python à la connexion vers l'atelier Part: importer le module Part:


```python
import Part 
```

Prenez une minute pour explorer le contenu du module Part en tapant Part. et jouer avec les différentes méthodes disponibles. Le module Part offre plusieurs fonctions telles que makeBox, makeCircle, etc \... qui vont créer instantanément un objet pour vous. Essayez ceci, par exemple :


```python
Part.makeBox(3,5,7) 
```

Lorsque vous appuyez sur Entrée après avoir tapé la ligne ci-dessus, rien n\'apparaîtra dans la vue 3D, mais quelque chose comme ça sera imprimé dans la console Python  :


```python
<Solid object at 0x5f43600> 
```

C\'est là qu\'un concept important intervient. Ce que nous avons créé ici est une forme de pièce. Ce n\'est pas un document objet de FreeCAD (pas encore). Dans FreeCAD, les objets et leur géométrie sont indépendants. Pensez à un document objet de FreeCAD en tant que conteneur, qui accueillera une forme. Les objets paramétriques auront également des propriétés telles que Longueur et Largeur et **recalculeront** leur forme à la volée chaque fois que l\'une des propriétés change. Ce que nous avons fait ici est de calculer une forme manuellement.

Nous pouvons maintenant créer facilement un document objet \"générique\" dans le document actuel (assurez-vous que vous avez au moins un nouveau document ouvert) et donnez-lui une forme de boîte comme celle que nous venons de faire:


```python
boxShape = Part.makeBox(3,5,7)
myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
myObj.Shape = boxShape
FreeCAD.ActiveDocument.recompute()
```

Notez comment nous avons traité myObj.Shape, voyez que cela se fait exactement comme nous l\'avons fait dans le chapitre précédent lorsque nous avons changé des propriétés d\'un objet, comme par exemple box.Height=5. En réalité, **Shape** est également une propriété tout comme Hauteur. Seulement il faut une forme de Part (Part Shape), pas un nombre. Au prochain chapitre, nous examinerons plus en profondeur la façon dont ces objets paramétriques sont construits.

Pour l\'instant, explorons nos formes de pièces plus en détail. À la fin du chapitre [Modélisation traditionnelle avec l\'atelier Part](Manual:Traditional_modeling,_the_CSG_way/fr.md) nous avons montré un tableau qui explique comment les formes sont construites dans Part ainsi que leurs différents composants (sommets, arêtes, faces, etc. ou Vertices, edges, faces, etc). Les mêmes composants existent ici et peuvent être récupérés à partir de Python. Les objets Part ont toujours les attributs suivants: sommets, arêtes, lignes, faces, coquilles et solides (Vertices, Edges, Wires, Faces, Shells and Solids). Tous constituent des listes qui peuvent contenir n\'importe quel nombre d\'éléments ou être vides :


```python
print(boxShape.Vertexes)
print(boxShape.Edges)
print(boxShape.Wires)
print(boxShape.Faces)
print(boxShape.Shells)
print(boxShape.Solids)
```

Par exemple, trouvons l\'aire de chaque face de notre forme de boîte ci-dessus : (Veillez à indenter la deuxième ligne, comme elle apparaît ci-dessous. Appuyez deux fois sur Entrée après la dernière ligne pour exécuter la commande Python).


```python
for f in boxShape.Faces:
   print(f.Area)
```

Ou pour chaque arête, son point de départ et son point final:


```python
for e in boxShape.Edges:
   print("New edge")
   print("Start point:")
   print(e.Vertexes[0].Point)
   print("End point:")
   print(e.Vertexes[1].Point)
```

Comme vous le voyez, si notre boxShape a un attribut \"Vertexes\", chaque Edge de la BoxShape a également un attribut \"Vertexes\". Comme nous pouvons nous y attendre, le BoxShape aura 8 sommets (Vertexes), tandis que l'arête en aura seulement 2, qui font partie de la liste des 8.

Nous pouvons toujours vérifier quel est le type de forme :


```python
print(boxShape.ShapeType)
print(boxShape.Faces[0].ShapeType)
print(boxShape.Vertexes[2].ShapeType)
```

Donc, pour reprendre le sujet des Formes Part: tout commence avec les Vertices (sommets). Avec un ou deux sommets, vous formez un Edge (arête) (les cercles complets n\'ont qu\'un seul sommet). Avec une ou plusieurs arêtes, vous formez une ligne composite (wire). Avec une ou plusieurs lignes fermées, vous formez une face (les lignes supplémentaires deviennent des «trous» dans la face). Avec une ou plusieurs Faces, vous créez une coquille (Shell). Quand une coquille est entièrement fermée (étanche), vous pouvez former un solide. Et enfin, vous pouvez joindre n\'importe quel nombre de Formes (Shapes) de tous types ensemble, ce qui s\'appelle alors un Composé (Compound).

Nous pouvons maintenant essayer de créer des formes complexes à partir de zéro, en construisant tous leurs composants un par un. Par exemple, essayons de créer un volume comme celui-ci:

![](images/Exercise_python_03.jpg )

Nous commencerons par créer une forme planaire comme celle-ci :

![](images/Wire.png )

D\'abord, créons les quatre points de base :


```python
V1 = FreeCAD.Vector(0,10,0)
V2 = FreeCAD.Vector(30,10,0)
V3 = FreeCAD.Vector(30,-10,0)
V4 = FreeCAD.Vector(0,-10,0)
```

Ensuite, nous pouvons créer les deux segments de droites :

![](images/Line.png )


```python
L1 = Part.LineSegment(V1,V2)
L2 = Part.LineSegment(V4,V3)
```

Notez que nous n\'avons pas eu besoin de créer Vertices. Nous pourrions immédiatement créer Parts.LineSegments à partir des Vecteurs FreeCAD. C\'est parce que nous n\'avons pas encore créé Edges. Un Part.LineSegment (tout comme Part.Circle, Part.Arc, Part.Ellipse ou Part.BSpline) ne crée pas un Edge mais plutôt une géométrie de base sur laquelle un Edge sera créé. Les arêtes (Edges) sont toujours fabriquées à partir d\'une telle géométrie de base qui est enregistrée dans son attribut Curve. Donc, si vous avez un Edge, faire:


```python
print(Edge.Curve) 
```

vous montrera de quel type de Edge il s'agit, c\'est-à-dire s\'il est basé sur une ligne, un arc, etc. Mais revenons à notre exercice et construisons les segments d\'arc. Pour cela, nous aurons besoin d\'un troisième point, afin que nous puissions utiliser le commode Part.Arc, qui prend 3 points :

![](images/Circel.png )


```python
VC1 = FreeCAD.Vector(-10,0,0)
C1 = Part.Arc(V1,VC1,V4)
VC2 = FreeCAD.Vector(40,0,0)
C2 = Part.Arc(V2,VC2,V3)
```

Maintenant, nous avons 2 lignes (L1 et L2) et 2 arcs (C1 et C2). Nous devons les transformer en arêtes (edges) :


```python
E1 = Part.Edge(L1)
E2 = Part.Edge(L2)
E3 = Part.Edge(C1)
E4 = Part.Edge(C2)
```

Par ailleurs, les géométries de base disposent également d\'une fonction toShape() qui fait exactement la même chose :


```python
E1 = L1.toShape()
E2 = L2.toShape()
 ...
```

Une fois que nous avons une série d\'arêtes (Edges), nous pouvons maintenant former une polyligne, en lui donnant une liste d\'arêtes. Nous devons faire attention à l\'ordre. Notez également les parenthèses.


```python
W = Part.Wire([E1,E4,E2,E3]) 
```

Et nous pouvons vérifier si notre Wire (ligne composite) a été correctement compris, et qu\'il est correctement fermé :


```python
print( W.isClosed() ) 
```

Ce qui imprimera \"True\" ou \"False\". Pour faire une Face, nous avons besoin de lignes composites fermées (Wires), donc c\'est toujours une bonne idée de vérifier cela avant de créer la Face. Maintenant, nous pouvons créer une Face, en lui donnant une seule ligne composite (Wire) (ou une liste de lignes composites si nous voulons des trous) :


```python
F = Part.Face(W) 
```

Ensuite, nous l\'extrudons :


```python
P = F.extrude(FreeCAD.Vector(0,0,10)) 
```

Notez que P est déjà un solide :


```python
print(P.ShapeType) 
```

En effet, lorsque nous extrudons une seule face, nous obtenons toujours un solide. Ce ne serait pas le cas, par exemple, si nous avions extrudé la ligne composite (Wire) suivante à la place :


```python
S = W.extrude(FreeCAD.Vector(0,0,10))
print(S.ShapeType)
```

Ce qui, bien sûr, nous donnera une coquille creuse, les faces supérieure et inférieure manquant.

Maintenant que nous avons notre forme définitive, nous sommes impatients de la voir à l\'écran! Créons donc un objet générique et affectons-lui notre nouveau solide:


```python
myObj2 = FreeCAD.ActiveDocument.addObject("Part::Feature","My_Strange_Solid")
myObj2.Shape = P
FreeCAD.ActiveDocument.recompute()
```

Alternativement, le module Part fournit également un raccourci qui fait l\'opération ci-dessus plus rapidement (mais vous ne pouvez pas choisir le nom de l\'objet) :


```python
Part.show(P) 
```

Tout ce qui précède, et bien plus encore, est expliqué en détail sur la page [Programmation dans Part](Topological_data_scripting/fr.md) en même temps que des exemples.

**Lire plus d\'informations :**

-   [Atelier Part](Part_Workbench/fr.md)
-   [Programmation dans Part](Topological_data_scripting/fr.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating and manipulating geometry/fr
