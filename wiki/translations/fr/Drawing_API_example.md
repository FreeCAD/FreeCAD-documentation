# Drawing API example/fr
## Introduction

Le flux de travail de l\'interface utilisateur graphique pour l\' [atelier Drawing](Drawing_Workbench/fr.md) est limité. Utiliser un script pour l\'interface est plus intéressante.

## Exemple simple 

Vous devez en premier lieu charger les modules Pièce (Part) et Mise en plan (Drawing): 
```python
import FreeCAD, Part, Drawing
```

Créez une petite pièce. 
```python
Part.show(Part.makeBox(100,100,100).cut(Part.makeCylinder(80,100)).cut(Part.makeBox(90,40,100)).cut(Part.makeBox(20,85,100)))
```

Projection directe. G0 veut dire arête vive, G1 est une tangente continue. 
```python
Shape = App.ActiveDocument.Shape.Shape
[visibleG0,visibleG1,hiddenG0,hiddenG1] = Drawing.project(Shape)
print "visible edges:", len(visibleG0.Edges)
print "hidden edges:", len(hiddenG0.Edges)
```

Tout est projeté sur le plan Z: 
```python
print "Bnd Box shape: X=",Shape.BoundBox.XLength," Y=",Shape.BoundBox.YLength," Z=",Shape.BoundBox.ZLength
print "Bnd Box project: X=",visibleG0.BoundBox.XLength," Y=",visibleG0.BoundBox.YLength," Z=",visibleG0.BoundBox.ZLength
```

Un autre vecteur de projection 
```python
[visibleG0,visibleG1,hiddenG0,hiddenG1] = Drawing.project(Shape,App.Vector(1,1,1))
```

Projeter en format SVG 
```python
resultSVG = Drawing.projectToSVG(Shape,App.Vector(1,1,1))
print resultSVG
```

## Exemple paramétrique 

Créer le corps 
```python
import FreeCAD
import Part
import Drawing

# Create three boxes and a cylinder
App.ActiveDocument.addObject("Part::Box","Box")
App.ActiveDocument.Box.Length=100.00
App.ActiveDocument.Box.Width=100.00
App.ActiveDocument.Box.Height=100.00

App.ActiveDocument.addObject("Part::Box","Box1")
App.ActiveDocument.Box1.Length=90.00
App.ActiveDocument.Box1.Width=40.00
App.ActiveDocument.Box1.Height=100.00

App.ActiveDocument.addObject("Part::Box","Box2")
App.ActiveDocument.Box2.Length=20.00
App.ActiveDocument.Box2.Width=85.00
App.ActiveDocument.Box2.Height=100.00

App.ActiveDocument.addObject("Part::Cylinder","Cylinder")
App.ActiveDocument.Cylinder.Radius=80.00
App.ActiveDocument.Cylinder.Height=100.00
App.ActiveDocument.Cylinder.Angle=360.00
# Fuse two boxes and the cylinder
App.ActiveDocument.addObject("Part::Fuse","Fusion")
App.ActiveDocument.Fusion.Base = App.ActiveDocument.Cylinder
App.ActiveDocument.Fusion.Tool = App.ActiveDocument.Box1

App.ActiveDocument.addObject("Part::Fuse","Fusion1")
App.ActiveDocument.Fusion1.Base = App.ActiveDocument.Box2
App.ActiveDocument.Fusion1.Tool = App.ActiveDocument.Fusion
# Cut the fused shapes from the first box
App.ActiveDocument.addObject("Part::Cut","Shape")
App.ActiveDocument.Shape.Base = App.ActiveDocument.Box 
App.ActiveDocument.Shape.Tool = App.ActiveDocument.Fusion1
# Hide all the intermediate shapes 
Gui.ActiveDocument.Box.Visibility=False
Gui.ActiveDocument.Box1.Visibility=False
Gui.ActiveDocument.Box2.Visibility=False
Gui.ActiveDocument.Cylinder.Visibility=False
Gui.ActiveDocument.Fusion.Visibility=False
Gui.ActiveDocument.Fusion1.Visibility=False
```

Insérer un objet Page et assigner un modèle. 
```python
App.ActiveDocument.addObject('Drawing::FeaturePage','Page')
App.ActiveDocument.Page.Template = App.getResourceDir()+'Mod/Drawing/Templates/A3_Landscape.svg'
```

Créer une vue de votre objet \"Shape\", définir la position et l\'assigner à une page. 
```python
App.ActiveDocument.addObject('Drawing::FeatureViewPart','View')
App.ActiveDocument.View.Source = App.ActiveDocument.Shape
App.ActiveDocument.View.Direction = (0.0,0.0,1.0)
App.ActiveDocument.View.X = 10.0
App.ActiveDocument.View.Y = 10.0
App.ActiveDocument.Page.addObject(App.ActiveDocument.View)
```

Créer une seconde vue de l\'objet, le but ici est de faire une rotation de 90 degrés. 
```python
App.ActiveDocument.addObject('Drawing::FeatureViewPart','ViewRot')
App.ActiveDocument.ViewRot.Source = App.ActiveDocument.Shape
App.ActiveDocument.ViewRot.Direction = (0.0,0.0,1.0)
App.ActiveDocument.ViewRot.X = 290.0
App.ActiveDocument.ViewRot.Y = 30.0
App.ActiveDocument.ViewRot.Scale = 1.0
App.ActiveDocument.ViewRot.Rotation = 90.0
App.ActiveDocument.Page.addObject(App.ActiveDocument.ViewRot) 
```

Créer une troisième vue de votre objet ici une vue isométrique. Nous activons les lignes cachées. 
```python
App.ActiveDocument.addObject('Drawing::FeatureViewPart','ViewIso')
App.ActiveDocument.ViewIso.Source = App.ActiveDocument.Shape
App.ActiveDocument.ViewIso.Direction = (1.0,1.0,1.0)
App.ActiveDocument.ViewIso.X = 335.0
App.ActiveDocument.ViewIso.Y = 140.0
App.ActiveDocument.ViewIso.ShowHiddenLines = True
App.ActiveDocument.Page.addObject(App.ActiveDocument.ViewIso) 
```

Changer quelque chose et mise à jour. La mise à jour modifie les vues et la page. 
```python
App.ActiveDocument.View.X = 30.0
App.ActiveDocument.View.Y = 30.0
App.ActiveDocument.View.Scale = 1.5
App.ActiveDocument.recompute()
```

### Accéder aux objets et détails 

Obtenir des fragments SVG d\'une vue. 
```python
ViewSVG = App.ActiveDocument.View.ViewResult
print ViewSVG
```

Obtenir l\'ensemble de la page des résultats (c\'est un fichier dans le répertoire temporaire avec uniquement le droit en lecture). 
```python
print "Resulting SVG document: ",App.ActiveDocument.Page.PageResult
file = open(App.ActiveDocument.Page.PageResult,"r")
print "Result page is ",len(file.readlines())," lines long"
```

Important: libérer le fichier! 
```python
del file
```

Insérer une vue avec votre propre contenu: 
```python
App.ActiveDocument.addObject('Drawing::FeatureView','ViewSelf')
App.ActiveDocument.ViewSelf.ViewResult = """<g id="ViewSelf"
  stroke="rgb(0, 0, 0)"
  stroke-width="0.35"
  stroke-linecap="butt"
  stroke-linejoin="miter"
  transform="translate(30,30)"
  fill="#00cc00"
  >

  <ellipse cx="40" cy="40" rx="30" ry="15"/>
  </g>"""
App.ActiveDocument.Page.addObject(App.ActiveDocument.ViewSelf)
App.ActiveDocument.recompute()

del ViewSVG
```

Ce qui donne le résultat suivant:

![](images/DrawingScriptResult.jpg )

### Généralités sur les dimensions et les tolérances 


**Voir aussi :**

[Extension dimensionnement Drawing](Drawing_Dimensioning_Addon/fr.md)

Dessiner les dimensions et les tolérances est encore en cours de développement mais vous pouvez accéder à des fonctionnalités de base avec un peu de travail.

Tout d\'abord vous avez besoin d\'obtenir le module Python gdtsvg (attention: le lien peut être rompu):

<https://github.com/jcc242/FreeCAD>

Pour obtenir un cadre de contrôle de cette fonctionnalité, essayez ce qui suit: 
```python
import gdtsvg as g # Import the module, I like to give it an easy handle
ourFrame = g.ControlFrame("0","0", g.Perpendicularity(), ".5", g.Diameter(), g.ModifyingSymbols("M"), "A",  
           g.ModifyingSymbols("F"), "B", g.ModifyingSymbols("L"), "C", g.ModifyingSymbols("I"))
```

Voici une bonne répartition du contenu d\'un cadre de contrôle : <http://www.cadblog.net/adding-geometric-tolerances.htm>

Les paramètres à transmettre pour contrôler la trame sont les suivants:

1.  Coordonnée X dans le système de coordonnées SVG (type chaîne de caractères)
2.  Coordonnée Y dans le système de coordonnées SVG (type chaîne de caractères)
3.  Le symbole caractéristique géométrique souhaité (tuple, chaîne svg en premier, largeur du symbole en second, hauteur du symbole en troisième)
4.  La tolérance (type chaîne de caractères)
5.  (facultatif) Le symbole de diamètre (tuple, type chaîne de caractères svg en premier, largeur du symbole en deuxième, hauteur du symbole en troisième)
6.  (facultatif) Matériau modifiant la condition (tuple, type chaîne de caractères svg en premier, largeur du symbole en deuxième, hauteur du symbole en troisième)
7.  (facultatif) Première donnée (type chaîne de caractères)
8.  (facultatif) Condition de modification de la première donnée (tuple, type chaîne de caractères svg en premier, largeur du symbole en deuxième, hauteur du symbole en troisième)
9.  (facultatif) Deuxième donnée (type chaîne de caractères)
10. (facultatif) Condition de modification de la deuxième donnée (tuple, type chaîne de caractères svg en premier, largeur du symbole en deuxième, hauteur du symbole en troisième)
11. (facultatif) Troisième donnée (type chaîne de caractères)
12. (facultatif) Condition matérielle du troisième point de référence (tuple, type chaîne de caractères svg en premier, largeur du symbole en deuxième, hauteur du symbole en troisième)

La fonction ControlFrame retourne un type contenant (type chaîne de caractères Svg, largeur hors tout de la fenêtre de contrôle, hauteur hors tout du cadre de la fenêtre de contrôle).

Pour obtenir une dimension, essayez ce qui suit: 
```python
import gdtsvg
ourDimension = linearDimension(point1, point2, textpoint, dimensiontext, linestyle=getStyle("visible"), 
               arrowstyle=getStyle("filled"), textstyle=getStyle("text")
```

Les entrées pour la dimension linéaire sont:

1.  point1, un tuple (x,y) avec des coordonnées svg, c'est l'un des points que vous souhaitez coter entre
2.  point2, un tuple (x,y) avec des coordonnées svg, c'est le deuxième point que vous souhaitez coter entre
3.  textpoint, un tuple (x,y) de coordonnées svg, c\'est ici que se trouvera le texte de votre dimension
4.  dimensiontext, une chaîne contenant le texte que la dimension doit indiquer
5.  linestyle, une chaîne contenant des styles svg (css), qui utilise la fonction getStyle pour récupérer une chaîne prédéfinie, pour styliser l\'apparence des lignes.
6.  arrowstyle, une chaîne contenant des styles svg (css), à l\'aide de la fonction getStyle pour récupérer une chaîne prédéfinie, afin de donner un style à l\'apparence des flèches
7.  textstyle, une chaîne contenant des styles svg (css), à l\'aide de la fonction getStyle pour récupérer une chaîne prédéfinie, pour définir l\'apparence du texte

Vous pouvez procéder comme ci-dessus pour afficher les dimensions sur la page de dessin. Ce module est très bogué, et, peut être rompu à tout moment, des rapports de bugs, sont les bienvenus sur la page github pour l\'instant, ou contactez jcc242, sur les forums, si vous validez un bug, ou quelque chose d\'autre.


 {{Drawing Tools navi}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > [Drawing](Category_Drawing.md) > Drawing API example/fr
