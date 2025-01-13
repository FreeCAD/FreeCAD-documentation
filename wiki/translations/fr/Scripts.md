---
 TutorialInfo:r
   Topic: Scripting
   Level: Base
   Time: 
   Author: onekk Carlo
   FCVersion: 0.19
   Files: 
---

# Scripts/fr








## Introduction

Par script, nous entendons la création d\'objets topologiques à l\'aide de l\'interpréteur Python de FreeCAD. FreeCAD pourrait être utilisé comme un \"très bon\" remplaçant d\'OpenSCAD, principalement parce qu\'il possède un véritable interpréteur Python, ce qui signifie qu\'il dispose d\'un véritable langage de programmation, presque tout ce que vous pouvez faire avec l\'interface graphique est réalisable avec un script Python.

Malheureusement, les informations sur les scripts dans la documentation, et même dans ce wiki sont éparpillées et manquent d\'uniformité \"d\'écriture\" et la plupart d\'entre elles sont expliquées d\'une manière trop technique.



## Commencer

Le premier obstacle d\'une manière simple à la création de scripts est qu\'il n\'y a pas de moyen direct d\'accéder à l\'éditeur Python interne de FreeCAD via un élément de menu ou une icône dans la zone de la barre d\'outils, mais sachant que FreeCAD ouvre un fichier avec un `.py ` dans l\'éditeur Python interne, l\'astuce la plus simple est de créer dans votre éditeur de texte préféré, puis de l\'ouvrir avec la commande habituelle **Fichier → Ouvrir**.

Pour faire les choses d\'une manière polie, le fichier doit être écrit avec un certain ordre, l\'éditeur Python FreeCAD a une bonne \"Syntaxe Highlighting\" qui manque dans de nombreux éditeurs simples comme le Notepad de Windows ou certains éditeurs Linux de base, il suffit donc d\'écrire ces quelques lignes :


```python
"""filename.py

   A short description of what the script does

"""
```

Enregistrez-les avec un nom significatif avec l\'extension `.py` et chargez le fichier résultant dans FreeCAD, avec la commande **Fichier → Ouvrir**.

Un exemple simple de ce qu\'il est nécessaire d\'avoir dans un script est présenté dans cette partie du code que vous pourriez utiliser comme modèle pour presque tous les futurs scripts:


```python
"""filename.py

   First FreeCAD Script

"""

import FreeCAD
from FreeCAD import Placement, Rotation, Vector
import FreeCADGui

DOC_NAME = "Wiki_Example"
DOC = FreeCAD.newDocument(DOC_NAME)
FreeCAD.setActiveDocument(DOC.Name)

ROT0 = Rotation(0, 0, 0)
VEC0 = Vector(0, 0, 0)

# Helper function

def set_view():
    """Rearrange View."""
    if not FreeCAD.GuiUp:
        return
    doc = FreeCADGui.ActiveDocument
    if doc is None:
        return
    view = doc.ActiveView
    if view is None:
        return
    # Check if the view is a 3D view:
    if not hasattr(view, "getSceneGraph"):
        return
    view.viewAxometric()
    view.fitAll()
```

Certaines astuces sont incorporées dans le code ci-dessus:

-    `import FreeCAD`Cette ligne importe FreeCAD dans l\'interpréteur FreeCAD Python, cela peut sembler redondant, mais ce n\'est pas le cas.

-    `from FreeCAD import Placement, Rotation, Vector`**Placement** **Rotation** et **Vector** sont largement utilisés dans l\'écriture de scripts FreeCAD, les importer de cette manière vous évitera de les appeler avec `FreeCAD.Vector` ou `FreeCAD.Placement` au lieu de `Vector` ou `Placement`, cela économisera de nombreuses frappes et rendra les lignes de code beaucoup plus petites.

Commençons par un petit script qui fait un très petit travail, mais qui montre la puissance de cette approche.


```python
# Script functions

def my_box(name, len, wid, hei):
    """Create a box."""
    obj_b = DOC.addObject("Part::Box", name)
    obj_b.Length = len
    obj_b.Width = wid
    obj_b.Height = hei

    DOC.recompute()

    return obj_b

# objects definition

obj = my_box("test_cube", 5, 5, 5)

set_view()
```

Ecrivez les lignes de code ci-dessus après `# Script functions` et appuyez sur la flèche verte dans la **Barre d\'outils des macros**

Vous verrez des choses magiques, un nouveau document est ouvert nommé \"Wiki_example\" et vous verrez dans la vue 3D un [Cube](Part_Box/fr.md) comme ci-dessous.

![Test cube](images/Cubo.png )



## Quelque chose en plus 

Pas si surprenant ? Oui, mais il faut commencer quelque part, on peut faire la même chose avec un [Cylindre](Part_Cylinder/fr.md), ajouter ces lignes de code après la fonction `my_box()` et avant la ligne : `# objects definition`.


```python
def my_cyl(name, ang, rad, hei):
    """Create a Cylinder."""
    obj = DOC.addObject("Part::Cylinder", name)
    obj.Angle = ang
    obj.Radius = rad
    obj.Height = hei

    DOC.recompute()

    return obj
```

Même ici, rien de trop excitant. Mais veuillez noter quelques particularités:

-   L\'absence de la référence habituelle à l \'`App.`, présente dans de nombreux extraits de code de documentation est délibérée. Ce code pourrait être utilisé même en invoquant FreeCAD comme module dans un interpréteur Python externe, la chose n\'est pas facilement faisable avec une AppImage, mais avec un certain soin, cela pourrait être fait. De plus, dans la devise standard de Python, \"mieux explicite qu\'implicite\", `App.` explique de manière très \"mal\" d\'où viennent les choses.
-   Notez l\'utilisation du nom \"constant\" attribué au document actif dans `DOC &#61; FreeCAD.activeDocument()`. activeDocument n\'est pas une \"constante\" au sens strict, mais d\'une manière \"sémantique\" c\'est notre \"Document actif\", qui pour notre utilisation sera une \"constante\" appropriée. La convention Python d\'utiliser le nom \"ALL CAPS\" pour \"constantes\", sans oublier que `DOC` est beaucoup plus court que `FreeCAD.activeDocument()`.
-   Chaque fonction retourne une géométrie, cela sera clair dans la suite de la page.
-   Géométrie n\'avait pas la propriété `Placement`, lors de l\'utilisation de géométries simples pour créer une géométrie plus complexe, gérer `Placement` est une chose délicate.

Maintenant, que faire avec ces géométries?

Introduisons les opérations booléennes. Comme exemple pour démmarrer, placez ces lignes après `my_cyl`, cela crée une fonction pour une **Fusion** également connue sous le nom d\'opération **Union** :


```python
def fuse_obj(name, obj_0, obj_1):
    """Fuse two objects."""
    obj = DOC.addObject("Part::Fuse", name)
    obj.Base = obj_0
    obj.Tool = obj_1
    obj.Refine = True
    DOC.recompute()

    return obj
```

Rien d\'exceptionnel ici aussi, notez cependant l\'uniformité dans le codage des fonctions. Cette approche est plus linéaire que celles vues autour d\'autres tutoriels sur les scripts, cette \"linéarité\" aide grandement à la lisibilité et aussi avec les opérations couper-copier-coller.

Utilisons les géométries, supprimons les lignes sous la section de code commençant par `# objects definition` et insérons les lignes suivantes:


```python
# objects definition

obj = my_box("test_cube", 5, 5, 5)

obj1 = my_cyl("test_cyl", 360, 2, 10)

fuse_obj("Fusion", obj, obj1)

set_view()
```

Lancez le script avec la flèche verte et nous verrons dans la vue 3D quelque chose comme :

![Cube et cylindre](images/Cucil.png )

## Placement

Le concept de placement est relativement complexe, voir [tutoriel avion](Aeroplane/fr.md) pour une explication plus approfondie.

Nous avons généralement besoin de placer des géométries respectueuses les unes des autres, lorsque la construction d\'un objet complexe est une tâche récurrente, le moyen le plus courant est d\'utiliser la propriété geometry `Placement`.

FreeCAD offre un large choix de moyens pour définir cette propriété, l\'un est plus adapté à l\'autre en fonction des connaissances et du parcours de l\'utilisateur, mais plus l\'écriture est simple et expliquée dans le Tutoriel cité, plus il utilise une définition particulière de la partie `Rotation` de `Placement`, assez facile à apprendre.


```python
FreeCAD.Placement(Vector(0, 0, 0), FreeCAD.Rotation(10, 20, 30), Vector(0, 0, 0))
```

Mais par rapport à d\'autres considérations, une chose est cruciale, la géométrie **point de référence**, c\'est-à-dire le point à partir duquel l\'objet est modélisé par FreeCAD, comme décrit dans ce tableau, copié de [Placement](Placement/fr.md) :

  Objet                             Point de référence
   
  Part.Box                          gauche (minx), avant (miny), bas (minz) sommet
  Part.Sphere                       centre de la sphère
  Part.Cylinder                     centre de la face inférieure
  Part.Cone                         centre de la face inférieure (ou sommet si le rayon inférieur est 0)
  Part.Torus                        centre du tore
  Fonctions dérivées d\'esquisses   La fonction hérite de la position de l\'esquisse sous-jacente. Les esquisses commencent toujours par Position = (0, 0, 0). Cette position correspond à l\'origine dans l\'esquisse.

Cette information doit être gardée à l\'esprit, en particulier lorsque nous devons appliquer une rotation.

Quelques exemples peuvent vous aider, supprimez la fonction `my_box` et toutes les lignes après la fonction `my_cyl` et ajoutez le code ci-dessous après la fonction `my_cyl` :


```python
def my_sphere(name, rad):
    """Create a Sphere."""
    obj = DOC.addObject("Part::Sphere", name)
    obj.Radius = rad

    DOC.recompute()

    return obj

def my_box2(name, len, wid, hei, cent=False, off_z=0):
    """Create a box with an optional z offset."""
    obj_b = DOC.addObject("Part::Box", name)
    obj_b.Length = len
    obj_b.Width = wid
    obj_b.Height = hei

    if cent is True:
        pos = Vector(len * -0.5, wid * -0.5, off_z)
    else:
        pos = Vector(0, 0, off_z)

    obj_b.Placement = Placement(pos, ROT0, VEC0)

    DOC.recompute()

    return obj_b

def mfuse_obj(name, objs):
    """Fuse multiple objects."""
    obj = DOC.addObject("Part::MultiFuse", name)
    obj.Shapes = objs
    obj.Refine = True
    DOC.recompute()

    return obj

def airplane():
    """Create an airplane shaped solid."""
    fuselage_length = 30
    fuselage_diameter = 5
    wing_span = fuselage_length * 1.75
    wing_width = 7.5
    wing_thickness = 1.5
    tail_height = fuselage_diameter * 3.0
    tail_position = fuselage_length * 0.70
    tail_offset = tail_position - (wing_width * 0.5)

    obj1 = my_cyl("main_body", 360, fuselage_diameter, fuselage_length)

    obj2 = my_box2("wings", wing_span, wing_thickness, wing_width, True, tail_offset)

    obj3 = my_sphere("nose", fuselage_diameter)
    obj3.Placement = Placement(Vector(0, 0, fuselage_length), ROT0, VEC0)

    obj4 = my_box2("tail", wing_thickness, tail_height, wing_width, False, 0)
    obj4.Placement = Placement(Vector(0, tail_height * -1, 0), ROT0, VEC0)

    objs = (obj1, obj2, obj3, obj4)

    obj = mfuse_obj("airplane", objs)
    obj.Placement = Placement(VEC0, Rotation(0, 0, -90), Vector(0, 0, tail_position))

    DOC.recompute()

    return obj

# objects definition

airplane()

set_view()

```

Expliquons quelque chose dans le code:

-   Nous avons utilisé une fonction pour définir une sphère, en utilisant la définition la plus simple, en utilisant uniquement le rayon.
-   Nous avons introduit une deuxième écriture pour **Union** ou **Fusion**, en utilisant plusieurs objets, pas trés éloignés de l\'habituel **Part::Fuse** qu\'il utilise **Part:Multifuse** et n\'utilise qu\'une seule propriété `Shapes`. Nous avons passé un **tuple** comme arguments mais il accepte aussi une **liste**.
-   Nous avons défini un objet complexe **un avion** mais nous l\'avons fait de manière **\"paramétrique\"** en définissant certains paramètres et en dérivant d\'autres paramètres, grâce à des calculs , basé sur les principaux paramètres.
-   Nous avons utilisé des propriétés de placement `Placement` dans la fonction et avant de renvoyer les géométries finales, nous avons utilisé une propriété `Rotation` avec l\'écriture *Yaw-Pitch-Roll*. Notez le dernier `Vector(0, 0, tail_position)` qui définit un **centre de rotation** de toute la géométrie.

++++
| ![Exemple d\'un avion](images/Aereo.png ) | ![Rotation de l\'avion](images/Aereo2.png ) | ![Propriété de placement](images/Aereo-prop.png ) |
++++

On peut facilement remarquer que la géométrie de l**\'avion** tourne autour de son \"barycentre\" ou \"centre de gravité\", que j\'ai fixé au centre de l\'aile, un endroit relativement \"naturel\", mais qui pourrait être placé n\'importe où vous voulez.

Le premier `Vector(0, 0, 0)` est le vecteur de translation, non utilisé ici, mais si vous remplacez `airplane()` par ces lignes :


```python
obj_f = airplane()

print(obj_F.Placement)
```

Vous verrez dans la fenêtre Rapport ce texte:


```python
Placement [Pos=(0, -21, 21), Yaw-Pitch-Roll=(0, 0, -90)]
```

Que s\'est-il passé?

FreeCAD a traduit `Vector(0, 0, 0), FreeCAD.Rotation(0, 0, -90), Vector(0, 0, tail_position)` en d\'autres termes notre définition `Placement` qui spécifie trois composants, **Translation**, **Rotation** et **centre de rotation** en valeurs \"internes\" de seulement deux composants, **Translation** et **Rotation**.

vous pouvez facilement visualiser la valeur de `tail_position` en utilisant une instruction print dans la fonction `airplane()` et voir que c\'est :


```python
tail_position = 21.0
```

en d\'autres termes, le **centre de rotation** de la géométrie est à `Vector(0, 0, 21)`, mais ce centre de rotation n\'est pas affiché dans l\'interface graphique, il pourrait être entré comme `Placement`, il n\'a pas pu être facilement récupéré.

C\'est le sens du mot \"maladroit\" que j\'ai utilisé pour définir la propriété `Placement`.

Voici l\'exemple de code complet avec un docstring de script décent selon la [convention de docstrings de Google](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html#example-google) :


```python
"""Sample code.

Filename:
   airplane.py

Author:
    Dormeletti Carlo (onekk)

Version:
    1.0

License:
    Creative Commons Attribution 3.0

Summary:
    This is sample code written for a FreeCAD Wiki page.
    It creates an airplane shaped solid using standard "Part WB" shapes.

"""

import FreeCAD
from FreeCAD import Placement, Rotation, Vector
import FreeCADGui

DOC_NAME = "Wiki_Example"
DOC = FreeCAD.newDocument(DOC_NAME)
FreeCAD.setActiveDocument(DOC.Name)

ROT0 = Rotation(0, 0, 0)
VEC0 = Vector(0, 0, 0)

# Helper function

def set_view():
    """Rearrange View."""
    if not FreeCAD.GuiUp:
        return
    doc = FreeCADGui.ActiveDocument
    if doc is None:
        return
    view = doc.ActiveView
    if view is None:
        return
    # Check if the view is a 3D view:
    if not hasattr(view, "getSceneGraph"):
        return
    view.viewAxometric()
    view.fitAll()

# Script functions

def my_cyl(name, ang, rad, hei):
    """Create a Cylinder."""
    obj = DOC.addObject("Part::Cylinder", name)
    obj.Angle = ang
    obj.Radius = rad
    obj.Height = hei

    DOC.recompute()

    return obj

def my_sphere(name, rad):
    """Create a Sphere."""
    obj = DOC.addObject("Part::Sphere", name)
    obj.Radius = rad

    DOC.recompute()

    return obj

def my_box2(name, len, wid, hei, cent=False, off_z=0):
    """Create a box with an optional z offset."""
    obj_b = DOC.addObject("Part::Box", name)
    obj_b.Length = len
    obj_b.Width = wid
    obj_b.Height = hei

    if cent is True:
        pos = Vector(len * -0.5, wid * -0.5, off_z)
    else:
        pos = Vector(0, 0, off_z)

    obj_b.Placement = Placement(pos, ROT0, VEC0)

    DOC.recompute()

    return obj_b

def mfuse_obj(name, objs):
    """Fuse multiple objects."""
    obj = DOC.addObject("Part::MultiFuse", name)
    obj.Shapes = objs
    obj.Refine = True
    DOC.recompute()

    return obj

def airplane():
    """Create an airplane shaped solid."""
    fuselage_length = 30
    fuselage_diameter = 5
    wing_span = fuselage_length * 1.75
    wing_width = 7.5
    wing_thickness = 1.5
    tail_height = fuselage_diameter * 3.0
    tail_position = fuselage_length * 0.70
    tail_offset = tail_position - (wing_width * 0.5)

    obj1 = my_cyl("main_body", 360, fuselage_diameter, fuselage_length)

    obj2 = my_box2("wings", wing_span, wing_thickness, wing_width, True, tail_offset)

    obj3 = my_sphere("nose", fuselage_diameter)
    obj3.Placement = Placement(Vector(0, 0, fuselage_length), ROT0, VEC0)

    obj4 = my_box2("tail", wing_thickness, tail_height, wing_width, False, 0)
    obj4.Placement = Placement(Vector(0, tail_height * -1, 0), ROT0, VEC0)

    objs = (obj1, obj2, obj3, obj4)

    obj = mfuse_obj("airplane", objs)
    obj.Placement = Placement(VEC0, Rotation(0, 0, -90), Vector(0, 0, tail_position))

    DOC.recompute()

    return obj

# objects definition

airplane()

set_view()
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripts/fr
