---
- TutorialInfo:/fr
   Topic:Scripting
   Level:Base
   Time:
   Author:onekk Carlo
   FCVersion:0.19
   Files:
---

# Scripts/fr








## Introduction

Avec Scripting, nous entendons créer des objets topologiques à l\'aide de l\'interpréteur Python de FreeCAD. FreeCAD pourrait être utilisé comme un \"très bon\" remplacement d\'OpenSCAD, principalement parce qu\'il a un véritable interpréteur Python, ce qui signifie qu\'il a un vrai langage de programmation à bord, presque tout ce que vous pouvez faire avec l\'interface graphique est faisable avec un script Python.

Malheureusement, les informations sur les scripts dans la documentation, et même dans ce wiki sont éparpillées et manquent d\'uniformité \"d\'écriture\" et la plupart d\'entre elles sont expliquées d\'une manière trop technique.

## Mise en appétit 

Le premier obstacle d\'une manière simple à la création de scripts est qu\'il n\'y a pas de moyen direct d\'accéder à l\'éditeur Python interne de FreeCAD via un élément de menu ou une icône dans la zone de la barre d\'outils, mais sachant que FreeCAD ouvre un fichier avec un `.py ` dans l\'éditeur Python interne, l\'astuce la plus simple est de créer dans votre éditeur de texte préféré, puis de l\'ouvrir avec la commande habituelle **Fichier → Ouvrir**.

Pour faire les choses d\'une manière polie, le fichier doit être écrit avec un certain ordre, l\'éditeur Python FreeCAD a une bonne \"Syntaxe HIghlighting\" qui manque dans de nombreux éditeurs simples comme le Notepad Windows ou certains éditeurs Linux de base, il suffit donc d\'écrire ces quelques lignes:


```python
"""script.py

   Primo script per FreeCAD

"""
```

Enregistrez-les avec un nom significatif avec l\'extension `.py` et chargez le fichier résultant dans FreeCAD, avec la commande **Fichier - Ouvrir**.

Un exemple simple de ce qu\'il est nécessaire d\'avoir dans un script est présenté dans cette partie du code que vous pourriez utiliser comme modèle pour presque tous les futurs scripts:


```python
"""filename.py

   Here a short but significant description of what the script do 

"""

import FreeCAD
from FreeCAD import Base, Vector
import Part
from math import pi, sin, cos

DOC = FreeCAD.activeDocument()
DOC_NAME = "Pippo"

def clear_doc():
    """
    Clear the active document deleting all the objects
    """
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)

def setview():
    """Rearrange View"""
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()

if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()
else:
    clear_doc()

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5
```

Certaines astuces sont incorporées dans le code ci-dessus:

-    `import FreeCAD`Cette ligne importe FreeCAD dans l\'interpréteur FreeCAD Python, cela peut sembler redondant, mais ce n\'est pas le cas.

-    `from FreeCAD import Base, Vector`Base et Vector sont largement utilisés dans l\'écriture de scripts FreeCAD, les importer de cette manière vous évitera de les appeler avec `FreeCAD.Vector` ou `FreeCAD.Base` au lieu de `Base` ou `Vector`, cela économisera de nombreuses frappes et rendra les lignes de code beaucoup plus petites.

Commençons par un petit script qui fait un très petit travail, mais qui montre la puissance de cette approche.


```python
def cubo(nome, lung, larg, alt):
    obj_b = DOC.addObject("Part::Box", nome)
    obj_b.Length = lung
    obj_b.Width = larg
    obj_b.Height = alt

    DOC.recompute()

    return obj_b

# objects definition

obj = cubo("test_cube", 5, 5, 5)

setview()
```

Mettez ces lignes après le code \"modèle\" et appuyez sur la flèche verte dans la **Barre d\'outils Macro**

Vous verrez des choses magiques, un nouveau document est ouvert nommé \"Pippo\" (nom italien pour **Toqué**) et vous verrez dans la vue 3D un [Cube](Part_Box/fr.md) comme ci-dessous.

![Test Cube](images/Cubo.png )

## Quelque chose en plus\... 

Pas trop étonnant? Oui, mais il faut commencer quelque part, on peut faire la même chose avec un [Cylindre](Part_Cylinder/fr.md), ajouter ces lignes de code après la méthode `cubo()` et avant la ligne : `# objects definition`.


```python
def base_cyl(nome, ang, rad, alt ):
    obj = DOC.addObject("Part::Cylinder", nome)
    obj.Angle = ang
    obj.Radius = rad
    obj.Height = altDOC.recompute()

    return obj   

```

Même ici, rien de trop excitant. Mais veuillez noter quelques particularités:

-   L\'absence de la référence habituelle à l \'`App.`, présente dans de nombreux extraits de code de documentation est délibérée. Ce code pourrait être utilisé même en invoquant FreeCAD comme module dans un interpréteur Python externe, la chose n\'est pas facilement faisable avec une AppImage, mais avec un certain soin, cela pourrait être fait. De plus, dans la devise standard de Python, \"mieux explicite qu\'implicite\", `App.` explique de manière très \"mal\" d\'où viennent les choses.
-   Notez l\'utilisation du nom \"constant\" attribué au document actif dans `DOC` = `FreeCAD.activeDocument()`. activeDocument n\'est pas une \"constante\" au sens strict, mais d\'une manière \"sémantique\" c\'est notre \"Document actif\", qui pour notre utilisation sera une \"constante\" appropriée. La convention Python d\'utiliser le nom \"ALL CAPS\" pour \"constantes\", sans oublier que `DOC` est beaucoup plus court que `FreeCAD.activeDocument()`.
-   Chaque méthode retourne une géométrie, cela sera clair dans la suite de la page.
-   Géométrie n\'avait pas la propriété `Placement`, lors de l\'utilisation de géométries simples pour créer une géométrie plus complexe, gérer `Placement` est une chose délicate.

Maintenant, que faire avec ces géométries?

Introduisons les opérations booléennes. Comme exemple pour démmarrer, placez ces lignes après `base_cyl(...`, cela crée une méthode pour une **Fusion** également connue sous le nom d\'opération **Union**:


```python
def fuse_obj(nome, obj_0, obj_1):
    obj = DOC.addObject("Part::Fuse", nome)
    obj.Base = obj_0
    obj.Tool = obj_1
    obj.Refine = True
    DOC.recompute()

    return obj
```

Rien d\'exceptionnel ici aussi, notez cependant l\'uniformité dans le codage des méthodes; Cette approche est plus linéaire que celles vues autour d\'autres tutoriels sur les scripts, cette \"linéarité\" aide grandement à la lisibilité et aussi avec les opérations couper-copier-coller.

Utilisons les géométries, supprimons les lignes sous la section de code commençant par `# objects definition` et insérons les lignes suivantes:


```python
# objects definition

obj = cubo("cubo_di_prova", 5, 5, 5)

obj1 = base_cyl('primo cilindro', 360,2,10)

fuse_obj("Fusione", obj, obj1)

setview()
```

Lancez le script avec la flèche verte et nous verrons dans la vue 3D quelque chose comme:

![cube and cylinder](images/Cucil.png )

## Placement

Le concept de placement est relativement complexe, voir [tutoriel avion](Aeroplane/fr.md) pour une explication plus approfondie.

Nous avons généralement besoin de placer des géométries respectueuses les unes des autres, lorsque la construction d\'un objet complexe est une tâche récurrente, le moyen le plus courant est d\'utiliser la propriété geometry `Placement`.

FreeCAD offre un large choix de moyens pour définir cette propriété, l\'un est plus adapté à l\'autre en fonction des connaissances et du parcours de l\'utilisateur, mais plus l\'écriture est simple et expliquée dans le Tutoriel cité, plus il utilise une définition particulière de la partie `Rotation` de `Placement`, assez facile à apprendre.


```python 
FreeCAD.Placement(Vector(0, 0, 0), FreeCAD.Rotation(10, 20, 30), Vector(0, 0, 0))
```

Mais par rapport à d\'autres considérations, une chose est cruciale, la géométrie **point de référence**, c\'est-à-dire le point à partir duquel l\'objet est modélisé par FreeCAD, comme décrit dans ce tableau, copié de [Placement](Placement/fr.md):

  Objet                             Point de référence
   
  Part.Box                          gauche (minx), avant (miny), bas (minz) sommet
  Part.Sphere                       centre de la sphère (c\'est-à-dire centre de la boîte englobante)
  Part.Cylinder                     centre de la face inférieure
  Part.Cone                         centre de la face inférieure (ou sommet si le rayon inférieur est 0)
  Part.Torus                        centre du tore
  Fonctions dérivées d\'esquisses   La fonction hérite de la position de l\'esquisse sous-jacente. Les esquisses commencent toujours par Position = (0, 0, 0). Cette position correspond à l\'origine dans l\'esquisse.

Cette information doit être gardée à l\'esprit, en particulier lorsque nous devons appliquer une rotation.

Quelques exemples peuvent aider, supprimez toute la ligne après la méthode `base_cyl` et insérez la partie de code ci-dessous:


```python
def sfera(nome, rad):
    obj = DOC.addObject("Part::Sphere", nome)
    obj.Radius = radDOC.recompute()

    return obj   

def mfuse_obj(nome, objs):
    obj = DOC.addObject("Part::MultiFuse", nome)
    obj.Shapes = objs
    obj.Refine = True
    DOC.recompute()

    return obj

def aeroplano():

    lung_fus = 30
    diam_fus = 5
    ap_alare = lung_fus * 1.75
    larg_ali = 7.5
    spess_ali = 1.5   
    alt_imp = diam_fus * 3.0  
    pos_ali = (lung_fus*0.70)
    off_ali = (pos_ali - (larg_ali * 0.5))

    obj1 = base_cyl('primo cilindro', 360, diam_fus, lung_fus)

    obj2 = cubo('ali', ap_alare, spess_ali, larg_ali, True, off_ali)

    obj3 = sfera("naso", diam_fus)
    obj3.Placement = FreeCAD.Placement(Vector(0, 0, lung_fus), FreeCAD.Rotation(0, 0, 0), Vector(0, 0, 0))

    obj4 = cubo('impennaggio', spess_ali, alt_imp, larg_ali, False, 0)
    obj4.Placement = FreeCAD.Placement(Vector(0, alt_imp * -1, 0), FreeCAD.Rotation(0, 0, 0), Vector(0, 0, 0))

    objs = (obj1, obj2, obj3, obj4)

    obj = mfuse_obj("Forma esempio", objs)
    obj.Placement = FreeCAD.Placement(Vector(0, 0, 0), FreeCAD.Rotation(0, 0, -90), Vector(0, 0, pos_ali))

    DOC.recompute()

    return obj

# objects definition

aeroplano()

setview()
```

Expliquons quelque chose dans le code:

-   Nous avons utilisé une méthode pour définir une sphère, en utilisant la définition la plus simple, en utilisant uniquement le rayon.
-   Nous avons introduit une deuxième écriture pour **Union** ou **Fusion**, en utilisant plusieurs objets, pas trés éloignés de l\'habituel **Part::Fuse** qu\'il utilise **Part:Multifuse** et n\'utilise qu\'une seule propriété `Shapes`. Nous avons passé un **tuple** comme arguments mais il accepte aussi une **liste**.
-   Nous avons défini un objet complexe **aeroplano** (mot italien pour avion) mais nous l\'avons fait de manière **\"paramétrique\"** en définissant certains paramètres et en dérivant d\'autres paramètres, grâce à des calculs , basé sur les principaux paramètres.
-   Nous avons utilisé des propriétés de placement `Placement` dans la méthode et avant de renvoyer les géométries finales, nous avons utilisé une propriété `Rotation` avec l\'écriture *Yaw-Pitch-Roll*. Notez le dernier `Vector(0, 0, pos_ali)` qui définit un **centre de rotation** de toute la géométrie.

    
  ![aeroplane example](images/Aereo.png )   ![aereo rotated](images/Aereo2.png )   ![Prop Placement](images/Aereo-prop.png )
    

On peut facilement remarquer que la géométrie **aeroplano** tourne autour de son \"barycentre\" ou \"centre de gravité\", que j\'ai fixé au centre de l\'aile, un endroit relativement \"naturel\", mais qui pourrait être placé n\'importe où vous voulez.

Le premier `Vector(0, 0, 0)` est le vecteur de translation, non utilisé ici, mais si vous remplacez `aeroplano()` par ces lignes:


```python
obj_f = aeroplano()

print(obj_F.Placement)
```

Vous verrez dans la fenêtre Rapport ce texte:


```python
Placement [Pos=(0, -21, 21), Yaw-Pitch-Roll=(0, 0, -90)]
```

Que s\'est-il passé?

FreeCAD a traduit le `Vector(0, 0, 0), FreeCAD.Rotation(0, 0, -90), Vector(0, 0, pos_ali)` en un autre mot notre définition `Placement` qui spécifie trois composants, **Translation**, **Rotation** et **centre de rotation** en valeurs \"internes\" de seulement deux composants, **Translation** et **Rotation**.

vous pouvez facilement visualiser la valeur de `pos_ali` en utilisant une instruction print dans la méthode `aeroplano(...` et voir que c\'est:


```python
pos ali =  21.0
```

en d\'autres termes, le **centre de rotation** de la géométrie est à `Vector(0, 0, 21)`, mais ce centre de rotation n\'est pas affiché dans l\'interface graphique, il pourrait être entré comme { {incode\|Placement}}, il n\'a pas pu être facilement récupéré.

C\'est le sens du mot \"maladroit\" que j\'ai utilisé pour définir la propriété `Placement`.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripts/fr
