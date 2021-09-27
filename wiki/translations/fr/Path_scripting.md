# Path scripting/fr
{{TOCright}}

## Introduction

L\'atelier Path propose des outils pour importer, créer, manipuler et exporter des [parcours-outils](https://fr.wikipedia.org/wiki/Programmation_de_commande_num%C3%A9rique) dans FreeCAD. Avec eux, l\'utilisateur peut importer, voir et modifier des programmes G-Code existants, créer des chemins d\'outils depuis des formes 3D et exporter ces chemins d\'outils vers G-Code.

L\'atelier Path en est actuellement à ses débuts et n\'offre pas toutes les fonctions avancées de certaines alternatives commerciales. Cependant, l\'interface de script python facilite la modification ou le développement d\'outils plus puissants.

## Démarrage rapide 

Les objets Path de FreeCAD sont des commandes de séquences de déplacement. Voici une utilisation typique :


```python
>>> import Path
>>> c1 = Path.Command("g1x1")
>>> c2 = Path.Command("g1y4")
>>> c3 = Path.Command("g1 x2 y2") # spaces end newlines are not considered
>>> p = Path.Path([c1,c2,c3])
>>> o = App.ActiveDocument.addObject("Path::Feature","mypath")
>>> o.Path = p
>>> print p.toGCode()
```

## Le Format G-Code interne de FreeCAD 

Un concept préliminaire est important à appréhender. La plus grande partie de l\'implémentation ci-dessous est fortement liée aux commandes de déplacement qui ont les même noms que ceux de G-Code mais sans être proche d\'une implémentation spécifique à un contrôleur. Nous avons choisi des noms tels que « G0 » pour indiquer un mouvement « rapide » ou « G1 » pour un déplacement « d\'alimentation » pour la performance (sauvegarde de fichier efficace) et pour minimiser le travail de traduction de et vers les autres formats G-Code. Puisque le monde de la CNC utilise des milliers de dialectes G-Code, nous avons choisi de rester avec une partie simplifiée de ce code. On pourrait décrire le format G-Code de FreeCAD comme une forme indépendante des machines.

Les données Path sont sauvegardées directement sous cette forme de G-Code dans les fichiers .FCStd

Toutes les traductions de et vers des dialectes G-Code FreeCAD sont réalisées par des scripts pre et post. Cela signifie que si vous voulez travailler avec une machine qui utilise un contrôleur spécifique tel que LinuxCNC, Fanuc, Mitusubishi, ou HAAS, etc., vous devrez utiliser (ou écrire s\'il n\'existe pas) un post-processeur pour ce contrôleur spécifique (allez voir la section « Importer et exporter du G-Code » ci-dessous).

### Référence GCode 

Les règles et les lignes directrices suivantes définissent le jeu de G-Code employé en interne dans FreeCAD:

-   la donnée G-Code, dans les objets Path de FreeCAD, est séparée en « Commandes ». Une Commande est définie par un nom qui doit débuter par G ou M et (optionnellement) des arguments, qui sont sous la forme Lettre = Nombre Flottant, par exemple X 0.02 ou Y 3.5 ou F 300. Ce sont des exemples typiques de commandes G-Code de FreeCAD:




    G0 X2.5 Y0 (le nom de commande est G0, les arguments X=2.5 et Y=0)

    G1 X30 (le nom de commande est G1, le seul argument  X=30)

    G90 (le nom de commande est G90, sans argument)

-   Pour la partie numérique d\'une commande G ou M, les deux formes « G1 » ou « G01 » sont acceptées.
-   Seules les commandes débutant par G ou M sont actuellement acceptées pour l\'instant.
-   Seuls les millimètres sont acceptés pour le moment. G20/G21 ne sont pas pris en compte.
-   Les arguments sont toujours triés alphabétiquement. Cela signifie que si vous créez une commande « G1 X2 Y4 F300 », elle sera écrite comme « G1 F300 X2 Y4 ».
-   Les arguments ne peuvent pas être répétés dans une même commande. Par exemple, « G1 X1 Y2 X2 Y3 » ne fonctionnera pas. Vous devrez la séparer en deux, par exemple: « G1 X1 Y2, G1 X2 Y3 ».
-   Les arguments X, Y, Z, A, B, C sont absolus ou relatifs, en fonction du mode G90/G91 actuel. C\'est par défaut à absolu (si ce n\'est pas spécifié).
-   I, J, K sont toujours relatifs au dernier point. K peut être oublié.
-   X, Y, ou Z (et A, B, C) peuvent être oubliés. Dans ce cas, les coordonnées X, Y ou Z précédentes sont gardées.
-   Les commandes G-code autres que celles listées dans la table ci-dessous sont supportées, ceci étant, elles sont sauvegardées dans le path data (tant qu\'elles satisfont aux règles ci-dessus, bien sûr), mais elle ne produiront tout simplement pas de résultat visible à l\'écran. Par exemple, vous pouvez ajouter la commande G81, elle sera enregistrée mais pas affichée.

### Liste des commandes G-Code actuellement acceptées 

  Commande        Description                                                                  Arguments acceptés   Affiché
  --------------- ---------------------------------------------------------------------------- -------------------- ------------
  G0              déplacement rapide                                                           X,Y,Z,A,B,C          Rouge
  G1              déplacement normal                                                           X,Y,Z,A,B,C          Vert
  G2              arc dans le sens des aiguilles                                               X,Y,Z,A,B,C,I,J,K    Vert
  G3              arc inverse du sens des aiguilles                                            X,Y,Z,A,B,C,I,J,K    Vert
  G81, G82, G83   perçage                                                                      X,Y,Z,R,Q            Rouge/Vert
  G38.2           déplacement droit de la sonde (utilisé lors du fonctionnement de la sonde)   Z, F                 Jaune
  G90             coordonnées absolues                                                                              
  G91             coordonnées relatives                                                                             
  (Message)       commentaire                                                                                       

## L\'objet Command 

L\'objet Command représente une commande gcode. Il a trois attributs: Nom, Paramètres et Placement, ainsi que deux méthodes: toGCode() et setFromGCode(). En interne, il ne contient qu\'un nom et un dictionnaire de paramètres. La suite (placement et gcode) est interprétée depuis/vers ces données.


```python
>>> import Path
>>> c=Path.Command()
>>> c
Command  ( )
>>> c.Name = "G1"
>>> c
Command G1 ( )
>>> c.Parameters= {"X":1,"Y":0}
>>> c
Command G1 ( X:1 Y:0 )
>>> c.Parameters
{'Y': 0.0, 'X': 1.0}
>>> c.Parameters= {"X":1,"Y":0.5}
>>> c
Command G1 ( X:1 Y:0.5 )
>>> c.toGCode()
'G1X1Y0.5'
>>> c2=Path.Command("G2")
>>> c2
Command G2 ( )
>>> c3=Path.Command("G1",{"X":34,"Y":1.2})
>>> c3
Command G1 ( X:34 Y:1.2 )
>>> c3.Placement
Placement [Pos=(34,1.2,0), Yaw-Pitch-Roll=(0,0,0)]
>>> c3.toGCode()
'G1X34Y1.2'
>>> c3.setFromGCode("G1X1Y0")
>>> c3
Command G1 [ X:1 Y:0 ]
>>> c4 = Path.Command("G1X4Y5")
>>> c4
Command G1 [ X:4 Y:5 ]
>>> p1 = App.Placement()
>>> p1.Base = App.Vector(3,2,1)
>>> p1
Placement [Pos=(3,2,1), Yaw-Pitch-Roll=(0,0,0)]
>>> c5=Path.Command("g1",p1)
>>> c5
Command G1 [ X:3 Y:2 Z:1 ]
>>> p2=App.Placement()
>>> p2.Base = App.Vector(5,0,0)
>>> c5
Command G1 [ X:3 Y:2 Z:1 ]
>>> c5.Placement=p2
>>> c5
Command G1 [ X:5 ]
>>> c5.x
5.0
>>> c5.x=10
>>> c5
Command G1 [ X:10 ]
>>> c5.y=2
>>> c5
Command G1 [ X:10 Y:2 ]
```

## L\'objet Path 

L\'objet Path contient une liste de commandes.


```python
>>> import Path
>>> c1=Path.Command("g1",{"x":1,"y":0})
>>> c2=Path.Command("g1",{"x":0,"y":2})
>>> p=Path.Path([c1,c2])
>>> p
Path [ size:2 length:3 ]
>>> p.Commands
[Command G1 [ X:1 Y:0 ], Command G1 [ X:0 Y:2 ]]
>>> p.Length
3.0
>>> p.addCommands(c1)
Path [ size:3 length:4 ]
>>> p.toGCode()
'G1X1G1Y2G1X1'

lines = """
G0X-0.5905Y-0.3937S3000M03
G0Z0.125
G1Z-0.004F3
G1X0.9842Y-0.3937F14.17
G1X0.9842Y0.433
G1X-0.5905Y0.433
G1X-0.5905Y-0.3937
G0Z0.5
"""

slines = lines.split('\n')
p = Path.Path()
for line in slines:
    p.addCommands(Path.Command(line))

o = App.ActiveDocument.addObject("Path::Feature","mypath")
o.Path = p

# but you can also create a path directly form a piece of gcode.
# The commands will be created automatically:

p = Path.Path()
p.setFromGCode(lines)
```

En simplifiant, un objet Path peut aussi être créé directement depuis une séquence G-Code complète. Elle sera automatiquement divisée en séquences de commandes.


```python
>>> p = Path.Path("G0 X2 Y2 G1 X0 Y2")
>>> p
Path [ size:2 length:2 ]
```

## Caractéristique de Path 

Path est un objet document de FreeCAD, qui contient un chemin et le présente en une vue 3D.


```python
>>> pf = App.ActiveDocument.addObject("Path::Feature","mypath")
>>> pf
<Document object>
>>> pf.Path = p
>>> pf.Path
Path [ size:2 length:2 ]
```

Path contient aussi une propriété de Placement. Changer la valeur de ce placement modifiera la position dans la vue 3D, bien que l\'information Path elle-même, ne soit pas modifiée. La transformation est purement visuelle. Cela vous permet, par exemple, de créer un Path autour d\'une face qui a une orientation particulière sur votre modèle, qui n\'aura pas la même orientation que la matière première que vous positionnerez sur votre CNC.

Néanmoins, Path Compounds peut utiliser le Placement de ses enfants (voir ci-dessous).

## Objets Tool et Tooltable 

**REMARQUE :** Ce type d\'utilisation des outils est déprécié à partir de la version officielle 0.19. Dans la version 0.19, le nouveau système d\'outils ToolBit a été mis en place pour remplacer cet ancien système. Par conséquent, le codage a changé par rapport à ce qui est représenté ci-dessous. Veuillez consulter la page [Path Outils](Path_Tools/fr.md) pour plus d\'informations.

===Script \<= 0.18===

L\'objet Tool contient les définitions d\'un outil de CNC. L\'objet Tooltable contient, lui, une liste ordonnée d\'outils. Les Tooltables sont reliées comme propriété dans les caractérisques de Path Project et peuvent donc être éditées par l\'interface graphique en double-cliquant sur le bouton « Edit tooltable » de l\'arborescence d\'un projet dans les tâches qui s\'ouvrent.

Les tables d\'outils peuvent être importées depuis les .xml de FreeCAD et les formats .tooltable de HeeksCad et exportés au format .xml de FreeCAD depuis cette interface.


```python
>>> import Path
>>> t1=Path.Tool()
>>> t1
Tool Default tool
>>> t1.Name = "12.7mm Drill Bit"
>>> t1
Tool 12.7mm Drill Bit
>>> t1.ToolType
'Undefined'
>>> t1.ToolType = "Drill"
>>> t1.Diameter= 12.7
>>> t1.LengthOffset = 127
>>> t1.CuttingEdgeAngle = 59
>>> t1.CuttingEdgeHeight = 50.8
>>> t2 = Path.Tool("my other tool",tooltype="EndMill",diameter=10)
>>> t2
Tool my other tool
>>> t2.Diameter
10.0
>>> table = Path.Tooltable()
>>> table
Tooltable containing 0 tools
>>> table.addTools(t1)
Tooltable containing 1 tools
>>> table.addTools(t2)
Tooltable containing 2 tools
>>> table.Tools
{1: Tool 12.7mm Drill Bit, 2: Tool my other tool}
>>> 
```

## Caractéristiques

### Path Compound 

L\'objectif de cette fonction est d\'assembler un ou plusieurs chemins d\'outils et l\'(les) associer à une table d\'outils. La fonction Compound se comporte aussi comme un groupe standard FreeCAD dont vous pouvez y ajouter ou y enlever les objets directement depuis la vue arborescente. Vous pouvez aussi réordonner les items en double-cliquant sur l\'objet Compound de la vue arborescente et réordonner ses élements dans la vue de Taches qui s\'ouvre.


```python
>>> import Path
>>> p1 = Path.Path("G1X1")
>>> o1 = App.ActiveDocument.addObject("Path::Feature","path1")
>>> o1.Path=p1
>>> p2 = Path.Path("G1Y1")
>>> o2 = App.ActiveDocument.addObject("Path::Feature","path2")
>>> o2.Path=p2
>>> o3 = App.ActiveDocument.addObject("Path::FeatureCompound","compound")
>>> o3.Group=[o1,o2]
```

Une caractéristique importante de Path Compounds est la possibilité de prendre en compte ou non le Placement des sous-chemins en cochant leur propriété UsePlacements à True ou False. Sans cela, les données Path des sous-chemins seront simplement ajoutées séquentiellement. Si c\'est positionné sur True, chaque commande des sous-chemins, s\'ils contiennent des informations de position (G0, G1, etc..), seront d\'abord transformés par Placement avant d\'être ajoutés.

En créant un composant avec un seul sous-chemin, vous pouvez donc de rendre le Placement du sous-chemin « réel » (il affecte les données Path).

### Path Project 

Le projet Path est une sorte d\'extension de Compound, qui possède quelques propriétés liées à la machine telle que tooltable. Il a principalement été créé pour être le type d\'objet à exporter en gcode une fois que la totalité de l\'initialisation du chemin est prête. L\'objet Project est maintenant codé en python, d\'où un mécanisme de création un peu différent:


```python
>>> from PathScripts import PathProject
>>> o4 = App.ActiveDocument.addObject("Path::FeatureCompoundPython","prj")
>>> PathProject.ObjectPathProject(o4)
>>> o4.Group = [o3]
>>> o4.Tooltable
Tooltable containing 0 tools
```

Le module Path propose aussi un éditeur graphique de table d\'outils qui peut être appelé depuis python, en lui donnant un objet qui possède une propriété ToolTable:


```python
>>> from PathScripts import TooltableEditor
>>> TooltableEditor.edit(o4)
```

### Path Shape 

Attribuez la forme wire Part à un objet Path normal à l\'aide de le script Path.fronShape() (ou mieux encore avec Path.fronShapes()). En donnant comme paramètre un objet wire Part, son chemin sera automatiquement calculé à partir de la forme. Notez que dans ce cas, le placement est positionné automatiquement sur le premier point du fil et l\'objet n\'est donc plus déplaçable en changeant sa position. Pour le déplacer, la forme sous-jacente doit être bougée.


```python
>>> import Part
>>> import Path
>>> v1 = FreeCAD.Vector(0,0,0)
>>> v2 = FreeCAD.Vector(0,2,0)
>>> v3 = FreeCAD.Vector(2,2,0)
>>> v4 = FreeCAD.Vector(3,3,0)
>>> wire = Part.makePolygon([v1,v2,v3,v4])
>>> o = FreeCAD.ActiveDocument.addObject("Path::Feature","myPath2")
>>> o.Path = Path.fromShape(wire)
>>> FreeCAD.ActiveDocument.recompute()
>>> p =  o.Path
>>> print(p.toGCode())
```

### Python

Les fonctions Path::Feature et Path::FeatureShape ont une version en python, appelées respectivement Path::FeaturePython et Path::FeatureShapePython, qui peuvent être utilisées pour créer des objets paramétriques dérivés plus avancés.

## Importer et exporter du GCode 

### Format Natif 

Les fichiers G-Code peuvent être directement importés et exportés par l\'interface graphique, en utilisant les éléments du menu « open », « insert » ou « export ». Après la saisie du nom de fichier, une fenêtre de dialogue apparaît pour demander quel script de traitement doit être utilisé. Cela peut être fait depuis python:

Les informations de Path sont stockées dans des objets Path utilisants le jeu gcode décrit dans la section « format G-Code interne de FreeCAD » ci-dessus. Ce jeu peut être importé ou exporté « tel quel » ou converti vers/depuis une version spécifique de G-Code adapté à votre machine.

Si vous avez un programme G-Code très simple et standard, qui respecte les règles décrites dans la section « format G-Code interne de FreeCAD » ci-dessus, par exemple le boomerang de <http://www.cnccookbook.com/GWESampleFiles.html>, il peut être importé directement dans un objet Path, sans traduction (c\'est la même chose qu\'utiliser l\'option « None » de l\'invite graphique):


```python
import Path
f = open("/path/to/boomerangv4.ncc")
s = f.read()
p = Path.Path(s)
o = App.ActiveDocument.addObject("Path::Feature","boomerang")
o.Path = p
```

De même, vous pouvez obtenir l\'information path comme un G-Code « indépendant » et le sauvegarder manuellement dans un fichier:


```python
text = o.Path.toGCode()
print text
myfile = open("/path/to/newfile.ngc")
myfile.write(text)
myfile.close()
```

Si vous avez besoin d\'une sortie adaptée, vous aurez alors besoin de convertir ce G-Code « indépendant » dans un format adapté à votre machine. C\'est le travail des scripts de post-traitement.

### Utiliser les scripts de pre- et post-traitement 

Si vous avez un fichier G-Code écrit pour une machine spécifique, qui ne respecte pas les règles internes utilisées de FreeCAD, décrites dans la section « format G-Code interne de FreeCAD » ci-dessus, il pourrait échouer à l\'import et/ou ne pas être correctement affiché en 3D. Pour y remédier, vous pouvez utiliser un scrit de pré-traitement qui convertira le format spécifique de votre machine vers celui de FreeCAD.

Si vous connaissez le nom du script de pré-traitement, vous pouvez importer votre fichier en l\'utilisant, depuis la console python de cette manière:


```python
import example_pre
example_pre.insert("/path/to/myfile.ncc","DocumentName")
```

De la même manière, vous pouvez sortir un objet Path vers G-Code, en utilisant un script de post-traitement comme ceci:


```python
import example_post
example_post.export (myObjectName,"/path/to/outputFile.ncc")
```

### Écrire des scripts de traitement 

Les scripts de pré- et post-traitement se comportent comme d\'autres importateurs/exportateurs habituels de FreeCAD. Lors du choix d\'un script de pré/post traitement depuis l\'invite, le processus d\'import/export sera redirigé vers le script spécifique donné. Les scripts de pré-traitement doivent contenir au moins des méthodes open(filename) et insert(filename,docname). Les scripts de post-traitement doivent implémenter export(objectslist,filename).

Les scripts sont placés soit dans le répertoire Mod/Path/PathScripts soit dans le répertoire path macro de l\'utilisateur. Vous pouvez leur donner le nom que vous voulez mais par convention et pour être utilisé dans les menus de l\'interface graphique, les noms des scripts de pré-traitement doivent terminer par « \_pre », les scripts de post-traitement avec « \_post » (assurez-vous d\'utiliser underscore et pas le trait-d\'union, sinon python ne pourra pas les importer). Voici un exemple de pré-traitement très, très simple. Des exemple plus complexes peuvent être trouvés dans le répertoire Mod/Path/PathScripts:


```python
def open(filename):
    gfile = __builtins__.open(filename)
    inputstring = gfile.read()
    # the whole gcode program will come in as one string,
    # for example: "G0 X1 Y1\nG1 X2 Y2"
    output = ""
    # we add a comment
    output += "(This is my first parsed output!)\n"
    # we split the input string by lines
    lines = inputstring.split("\n")
    for line in lines:
        output += line
        # we must insert the "end of line" character again
        # because the split removed it
        output += "\n"
    # another comment
    output += "(End of program)"
    import Path
    p = Path.Path(output)
    myPath = FreeCAD.ActiveDocument.addObject("Path::Feature","Import")
    myPath.Path = p
    FreeCAD.ActiveDocument.recompute()
```

Les pré- et post-traitements travaillent exactement de la même manière. Ils font simplement le contraire: les scripts pré convertissent un G-Code spécifique vers le G-Code de FreeCAD, alors que les scripts post convertissent le G-Code de FreeCAD vers un G-Code spécifique à une machine.

## Ajout de toutes les faces d\'une ShapeString à la liste de BaseFeature d\'une opération ProfileFromFaces 

Cet exemple est basé sur une [discussion sur le forum germanophone](https://forum.freecadweb.org/viewtopic.php?f=13&t=33310&p=279991#p279959).

### Prérequis

-   Créer un solide avec ShapeString comme Cutout
-   Créer un travail en utilisant ce solide comme son BaseObject
-   Créez une opération ProfileFromFaces nommée \"Profile\_Faces\" avec une BaseGeometry vide.

### Le code 

Le code suivant va ensuite ajouter toutes les faces de ShapeString et créer les chemins:


```python
doc = App.ActiveDocument
list_of_all_element_faces = []
for i, face in enumerate(doc.ShapeString.Shape.Faces):
    list_of_all_element_faces.append('Face' + str(i + 1))


doc.Profile_Faces.Base = [(doc.ShapeString, tuple(list_of_all_element_faces))]
doc.recompute()
```





{{Path_Tools_navi

}} {{Powerdocnavi}}

_ _

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Path](Path_Workbench.md) > Path scripting/fr
