# Manual:Creating and manipulating geometry/fr
{{Manual:TOC}}

Dans les chapitres précédents, nous avons exploré les différents ateliers de FreeCAD et comment chacun d\'entre eux présente son propre ensemble d\'outils et de types de géométrie. Les mêmes principes s\'appliquent lorsque l\'on travaille avec FreeCAD par le biais de scripts Python.

Nous avons également observé que la plupart des ateliers de FreeCAD s\'appuient sur un atelier fondamental : l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [atelier Part](Part_Workbench/fr.md). De nombreux autres ateliers, tels que l\'<img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [atelier Draft](Draft_Workbench/fr.md), utilisent les outils et la géométrie de l\'atelier Part, ce qui est exactement ce que nous ferons dans ce chapitre - utiliser Python pour créer et manipuler la géométrie de la pièce.

Pour commencer à travailler avec la géométrie Part en Python, nous devons effectuer l\'équivalent en script du passage à l\'atelier Part : importer le module Part.


```python
import Part 
```

Prenez le temps d\'explorer le module Part en tapant **Part.** dans la console Python et en parcourant les méthodes et attributs disponibles dans la fenêtre d\'autocomplétion. C\'est un excellent moyen de se familiariser avec les fonctionnalités offertes par le module. Vous trouverez une variété de fonctions pratiques, telles que makeBox et makeCircle, qui vous permettent de créer rapidement des formes géométriques et des objets à l\'aide d\'une seule commande. La plupart de ces fonctions proposent également des paramètres facultatifs, ce qui vous permet de contrôler précisément les dimensions et l\'emplacement.

Passez un peu de temps à parcourir le contenu du module vous aidera non seulement à comprendre quels sont les outils à votre disposition, mais vous donnera également un aperçu du fonctionnement de l\'atelier Part sous le capot. Ces connaissances fondamentales s\'avéreront précieuses lorsque nous commencerons à créer et à manipuler des géométries par programme. Tapez la commande suivante


```python
Part.makeBox(3,5,7) 
```

Cette commande crée une boîte 3D, également connue sous le nom de prisme rectangulaire, avec des dimensions spécifiques. Le premier paramètre, 3, définit la longueur de la boîte sur l\'axe X. Le deuxième paramètre, 5, définit la largeur sur l\'axe Y. Le troisième paramètre, 7, spécifie la hauteur sur l\'axe Z. Le deuxième paramètre, 5, définit la largeur le long de l\'axe Y et le troisième paramètre, 7, spécifie la hauteur le long de l\'axe Z. Bien que cette fonction génère la géométrie de la boîte, elle ne l\'ajoute pas automatiquement au document FreeCAD actif. Dans la console Python, vous verrez ce qui suit :


```python
<Solid object at 0x5f43600> 
```

La sortie **\<Solid object at 0x5f43600\>** indique qu\'une Part Shape a été créée en mémoire. Il s\'agit d\'un objet géométrique stocké à une adresse mémoire spécifique, comme le montre la valeur hexadécimale (0x5f43600). Cependant, il est important de comprendre que ce que nous avons créé ici n\'est pas encore un objet document FreeCAD. Il existe seulement en tant que forme géométrique brute dans la mémoire.

Cette distinction met en évidence un concept fondamental de FreeCAD : les objets et leur géométrie sont indépendants. Un objet document FreeCAD sert de conteneur qui héberge une forme. Ces objets document peuvent avoir des propriétés supplémentaires, telles que la longueur, la largeur et la hauteur, et ils peuvent être paramétriques. Les objets paramétriques recalculent leur géométrie (ou leur forme) de manière dynamique chaque fois qu\'une de leurs propriétés est modifiée. Par exemple, la modification de la longueur d\'une boîte paramétrique régénérera automatiquement sa forme avec la valeur mise à jour.

Dans ce cas, nous avons créé manuellement une forme à l\'aide de la fonction **Part.makeBox()**. Cette forme est un objet non paramétrique, ce qui signifie qu\'elle ne sera pas mise à jour automatiquement en fonction des propriétés - elle est statique à moins que nous ne la manipulions par programme. Pour que cette forme fasse partie du document FreeCAD actif, il faudrait qu\'elle soit assignée à un objet document (comme un **Part::Feature**), ce qui la relierait à l\'interface graphique et la rendrait visible et gérable dans l\'environnement FreeCAD.

Cette séparation entre les formes et les objets documentaires est ce qui rend FreeCAD très polyvalent, permettant aux utilisateurs de manipuler les formes de manière programmatique et de les intégrer dans un flux de travail de modélisation paramétrique selon les besoins.

Nous pouvons maintenant créer facilement un document objet \"générique\" dans le document actuel (assurez-vous que vous avez au moins un nouveau document ouvert) et donnez-lui une forme de boîte comme celle que nous venons de faire :


```python
boxShape = Part.makeBox(3,5,7)
myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
myObj.Shape = boxShape
FreeCAD.ActiveDocument.recompute()
```

Voici le détail des commandes précédentes :

-   **boxShape = Part.makeBox(3,5,7)** : crée une boîte 3D de dimensions 3x5x7 (longueur, largeur et hauteur) et la stocke en tant que Part Shape dans la variable boxShape. Cette forme n\'existe qu\'en mémoire et ne fait pas encore partie du document FreeCAD.

-   **myObj = FreeCAD.ActiveDocument.addObject(\"Part::Feature\", \"MyNewBox\")** : ajoute un nouvel objet Part::Feature nommé \"MyNewBox\" au document FreeCAD actif et l\'affecte à la variable myObj. Le nouvel objet apparaîtra dans l\'arborescence du document FreeCAD.

-   **myObj.Shape = boxShape** : lie la géométrie boxShape à la propriété Shape de myObj, intégrant la géométrie dans le document FreeCAD.

-   **FreeCAD.ActiveDocument.recompute()** : met à jour le document pour refléter les changements, en s\'assurant que le nouvel objet et sa géométrie apparaissent dans l\'interface graphique.

Remarquez comment nous avons traité **myObj.Shape**. Cela a été fait de la même manière que dans le chapitre précédent, où nous avons modifié d\'autres propriétés d\'un objet, comme **box.Height = 5**. En fait, **Shape** est aussi une propriété, tout comme **Height**. Cependant, au lieu de prendre un nombre, **Shape** nécessite une Part Shape. Dans le prochain chapitre, nous verrons de plus près comment ces objets paramétriques sont construits.

Pour l\'instant, explorons les formes de pièces plus en détail. Dans le chapitre sur la modélisation traditionnelle avec l\'atelier Part, nous avons présenté un tableau expliquant comment les Part Shapes sont construites et les différents composants dont elles sont constituées, tels que les **sommets**, les **arêtes** et les **faces**. Ces mêmes composants sont disponibles lorsque l\'on travaille avec des formes partielles en Python, ce qui permet une exploration et une manipulation détaillées de la géométrie. Les Part Shapes dans FreeCAD ont toujours les attributs suivants :

-   **Vertex** : points dans l\'espace 3D qui définissent les coins ou les extrémités de la géométrie.
-   **Edges** : lignes droites ou courbes reliant deux sommets.
-   **Wires** : boucles fermées ou ouvertes formées par une ou plusieurs arêtes connectées.
-   **Faces** : surfaces entourées par un ou plusieurs polylignes.
-   **Shells** : groupes de faces connectées, formant une surface continue.
-   **Solids** : volumes 3D entourés d\'une ou plusieurs coques.

Tous ces attributs sont représentés sous forme de listes en Python. Chaque liste peut contenir un nombre quelconque d\'éléments ou être vide, en fonction de la forme explorée. Par exemple, une boîte aura huit **Vertexes**, douze **Edges**, six **Faces**, une **Shell** et un **Solid**, tandis qu\'une ligne n\'aura que deux **Vertexes\'\' et une**Edge\'\'\', tous les autres attributs étant vides. Ces composants sont des éléments fondamentaux de la géométrie d\'une pièce et sont accessibles et manipulables par programme. Comprendre comment ils interagissent permet d\'exercer un contrôle puissant sur la création et la modification des modèles 3D. Nous pouvons accéder à ces listes comme suit :


```python
print(boxShape.Vertexes)
print(boxShape.Edges)
print(boxShape.Wires)
print(boxShape.Faces)
print(boxShape.Shells)
print(boxShape.Solids)
```

Trouvons l\'aire de chaque face de notre boîte ci-dessus : (Veillez à indenter la deuxième ligne, comme elle apparaît ci-dessous. Appuyez deux fois sur Entrée après la dernière ligne pour exécuter la commande Python).


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

Comme vous le voyez, si notre boxShape a un attribut \"Vertexes\", chaque bord de la boxShape a également un attribut \"Vertexes\". Comme on peut s\'y attendre, la boxShape aura 8 sommets, tandis que l\'arête n\'en aura que 2, qui font tous deux partie de la liste de 8.

Nous pouvons toujours vérifier quel est le type de forme :


```python
print(boxShape.ShapeType)
print(boxShape.Faces[0].ShapeType)
print(boxShape.Vertexes[2].ShapeType)
```

Voici une brève explication des commandes ci-dessus :

-   **print(boxShape.ShapeType)** : affiche le type de la forme de premier niveau représentée par **boxShape**. Dans ce cas, puisque **boxShape** a été créée comme une boîte à l\'aide de **Part.makeBox**, la sortie sera \"Solid\", indiquant que la forme est un objet solide en 3D.

-   **print(boxShape.Faces\[0\].ShapeType)** : accède à la première face de la liste **Faces** de **boxShape** (index 0) et affiche son type de forme. Pour une boîte, chaque face est une surface plane, la sortie sera donc \"Face\".

-   **\'print(boxShape.Vertexes\[2\].ShapeType)** : accède au troisième sommet de la liste **Vertexes** de **boxShape** (index 2) et affiche son type de forme. Comme il s\'agit d\'un point spécifique dans l\'espace 3D, la sortie sera \"Vertex\".

Pour résumer le concept des Part Shapes : tout commence par des **Vertex** (sommet ou point), les éléments les plus basiques de la géométrie. En utilisant un ou deux **Vertex**, vous pouvez créer un **Edge** (arête) (notez que les cercles complets ne nécessitent qu\'un seul **Vertex**). Une ou plusieurs *Arêtes* peuvent alors former une *Polyligne*, qui peut être ouverte ou fermée. Lorsque vous avez un ou plusieurs **Polylignes** fermées, vous pouvez créer une **Face**. Les **Polylignes** supplémentaires à l\'intérieur de la **Polyligne** principale agiront comme des **trous** dans la **Face**. La combinaison d\'une ou de plusieurs *Faces* permet de construire une *Coque*, qui est essentiellement une collection de surfaces connectées. Si une *Coque* est entièrement fermée et étanche, elle peut alors être utilisée pour former un *Solide*, un objet 3D avec un volume. Enfin, un nombre quelconque de formes de n\'importe quel type, y compris des *Sommets*, des *Arêtes*, des *Polylignes*, des *Faces*, des *Coques* ou des *Solides*, peuvent être regroupées en un *Composé*, qui agit comme un conteneur pour de multiples formes.

Nous pouvons maintenant essayer de créer des formes complexes à partir de zéro, en construisant tous leurs composants un par un. Par exemple, essayons de créer un volume comme celui-ci:

<img alt="" src=images/Exercise_python_03.jpg  style="width:600px;">

Nous commencerons par créer une forme planaire comme celle-ci :

<img alt="" src=images/Wire.png  style="width:600px;">

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

Remarquez que nous n\'avons pas besoin de créer des **Vertexes** explicitement. Au lieu de cela, nous pouvons directement créer des **Part.LineSegments** en utilisant des **FreeCAD Vectors**. En effet, à ce stade, nous travaillons avec une géométrie de base, et non avec des **arêtes** réelles. Un **Part.LineSegment**, tout comme **Part.Circle**, **Part.Arc**, **Part.Ellipse**, ou **Part.BSpline**, définit la géométrie sous-jacente mais ne génère pas d\'arête en soi. Dans FreeCAD, les arêtes sont toujours construites à partir d\'une telle géométrie de base, qui est stockée dans l\'attribut **Curve** de l**\'Arête**. Cela signifie qu\'une arête est essentiellement une enveloppe autour de la géométrie de base, héritant de ses propriétés. Si vous avez une arête, vous pouvez accéder à sa géométrie sous-jacente en vous référant à l\'attribut de la courbe. La commande suivante :


```python
print(Edge.Curve) 
```

vous permet de comprendre la structure sous-jacente de l\'arête et la manière dont elle a été construite. Revenons maintenant à notre exercice et construisons les segments d\'arc. Pour créer un arc, nous avons besoin de trois points : un point de départ, un point d\'arrivée et un point central qui détermine la courbure. Pour ce faire, nous pouvons utiliser la fonction **Part.Arc**, qui prend ces trois points en entrée et génère la géométrie de base d\'un arc.

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

Les géométries de base disposent également d\'une fonction **toShape()** qui fait exactement la même chose :


```python
E1 = L1.toShape()
E2 = L2.toShape()
 ...
```

Une fois que nous avons une série d\'arêtes, nous pouvons maintenant former une **polyligne**, en lui donnant une liste d\'arêtes. Nous devons faire attention à l\'ordre. Remarquez également les parenthèses.


```python
W = Part.Wire([E1,E4,E2,E3]) 
```

Et nous pouvons vérifier si notre polyligne a été correctement compris, et qu\'il est correctement fermé :


```python
print( W.isClosed() ) 
```

Ce qui imprimera \"True\" ou \"False\". Pour faire une **face**, nous avons besoin de **polylignes fermées**, donc c\'est toujours une bonne idée de vérifier cela avant de créer la face. Maintenant, nous pouvons créer une face, en lui donnant une seule polyligne (ou une liste de polylignes si nous voulons des trous) :


```python
F = Part.Face(W) 
```

Ensuite, nous l\'extrudons :


```python
P = F.extrude(FreeCAD.Vector(0,0,10)) 
```

Notez que P est déjà un **solide** :


```python
print(P.ShapeType) 
```

En effet, lorsque nous extrudons une seule face, nous obtenons toujours un solide. Ce ne serait pas le cas, par exemple, si nous avions extrudé la polyligne suivante à la place :


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
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Manual:Creating and manipulating geometry/fr
