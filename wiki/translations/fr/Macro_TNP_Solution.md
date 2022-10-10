# Macro TNP Solution/fr
{{Macro/fr
|Name=Macro TNP solution
|Icon=TNP_solution.png
|Description=Il s'agit d'une solution pour le problème de dénomination topologique
|Author=Dprojects
|Date=2022-08-16
|Version=1.0
}}

## Description

![](images/TNP_solution.gif )

Il s\'agit d\'une solution pour le problème de dénomination décrit à la page    * [Problème de dénomination topologique](Topological_naming_problem/fr.md).

Si vous construisez un objet sur un autre objet, ainsi qu\'une esquisse, il est simple à résoudre, car vous savez deux choses    *

1.  Les points de l\'esquisse font toujours partie de la face inférieure.
2.  L\'esquisse et la face inférieure sont dans le même plan.

Pour résoudre le problème du problème de dénomination topologique, vous pouvez    *

**Sauvegardez la clé avant toute opération    ***

Il suffit de sauvegarder la clé avant toute opération. Dans l\'exemple décrit à la page [Problème de dénomination topologique](Topological_naming_problem/fr.md), l\'objet se trouve dans le plan XY. J\'utilise donc la valeur de l\'axe Z du centre de Sketch BoundBox    *


{{MacroCode|code=
ad = FreeCAD.ActiveDocument
p2 = ad.Pad002
s2 = p2.Profile[0]
key = round(s2.Shape.BoundBox.Center[2], precision)
}}

**Ensuite, recherchez la clé stockée sur toutes les faces    ***

Après le redimensionnement, je recherche la clé stockée sur toutes les faces. Parce que si l\'esquisse et la face étaient sur le même plan XY, la valeur de l\'axe Z était la même pour les deux. Dans l\'atelier PartDesign, vous ne pouvez pas déplacer le troisième bloc au-dessus du deuxième bloc, pour avoir un espace entre les deux, c\'est un objet unique, le bloc suivant avec l\'esquisse touchera toujours la face. Sur la nouvelle face, la valeur de l\'axe Z sera toujours la même que la clé stockée. Donc, il faut retourner l\'index de la face. Il n\'y a rien de plus à faire.


{{MacroCode|code=

def getFaceIndex(iObj, iBB)   *index = 0   

    for f in iObj.Shape.Faces   *

        index += 1
        bb = round(f.BoundBox.Center[2], precision)
        if bb == iBB   *
            return index

    return -1

}}

**Dernières étapes**

À la fin, j\'assigne la nouvelle face à l\'esquisse et je recalcule. Pour être honnête, la partie la plus difficile a été d\'assigner la face à Sketch.Support, pour moi la syntaxe est époustouflante ;-)

## Code pour l\'exemple 

Le fichier de test a été téléchargé sur le forum FreeCAD    * [TNP.FCStd](https   *//forum.freecadweb.org/download/file.php?id=198537).


{{MacroCode|code=

__Title__="TNP_solution"
__Author__ = "Dprojects"
__Version__ = "1.0"
__Date__    = "2022-08-16"
__Comment__ = ""
__Web__ = "https   *//github.com/dprojects/Woodworking"
__Wiki__ = "https   *//wiki.freecadweb.org/TNP_solution"
__Icon__  = "TNP_solution.png"
__IconW__  = "TNP_solution.png"
__Help__ = "solution for Topological Naming Problem"
__Status__ = "stable"
__Requires__ = ""
__Communication__ = "http   *//www.freecadweb.org/wiki/index.php?title=User   *Dprojects"

# ####################################################################
#
# This is solution for Topological Naming Problem described at 
# https   *//wiki.freecadweb.org/Topological_naming_problem
#
# MIT License
# 
# Copyright (c) 2022 Darek L github.com/dprojects
# 
# Permission is hereby granted, free of charge, to any 
# person obtaining a copy of this software and associated 
# documentation files (the "Software"), to deal in the 
# Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit 
# persons to whom the Software is furnished to do so, subject 
# to the following conditions   *
# 
# The above copyright notice and this permission notice shall 
# be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.
# 
# ####################################################################

import FreeCAD

# this should be set according 
# FreeCAD user GUI precision settings
precision = 5

# global settings
ad = FreeCAD.ActiveDocument

# middle object to be resized
p1 = ad.Pad001
s1 = p1.Profile[0]

# top object bottom to store key
p2 = ad.Pad002
s2 = p2.Profile[0]

# ####################################################################
def getFaceIndex(iObj, iBB)   *index = 0   

    for f in iObj.Shape.Faces   *

        index += 1
        bb = round(f.BoundBox.Center[2], precision)
        
        FreeCAD.Console.PrintMessage("\n")
        FreeCAD.Console.PrintMessage(index)
        FreeCAD.Console.PrintMessage(" ")
        FreeCAD.Console.PrintMessage(bb)

        if bb == iBB   *
            FreeCAD.Console.PrintMessage(" <=== found")
            return index

    return -1

# ####################################################################
def makeTNP()   *

    # set key
    key = round(s2.Shape.BoundBox.Center[2], precision)

    # resize and cause TNP
    s1.setDatum(9, FreeCAD.Units.Quantity('350'))

    # recompute
    s1.recompute()
    p1.recompute()
    ad.recompute()

    FreeCAD.Console.PrintMessage("\n\n")
    FreeCAD.Console.PrintMessage("Stored key   *"+str(key))
    FreeCAD.Console.PrintMessage("\n")

    # search all faces for solution
    solutionIndex = getFaceIndex(p1, key)
    solution = "Face"+str(solutionIndex)FreeCAD.Console.PrintMessage("\n\n")
    FreeCAD.Console.PrintMessage("Solution   * "+solution)# set exact face to Sketch
    s2.Support = (p1, (solution,))
    ad.recompute()

# ####################################################################
def moveBack()   *

    s1.setDatum(9, FreeCAD.Units.Quantity('250'))
    s2.Support = (p1, ('Face13',))
    ad.recompute()

# ####################################################################
# main
# ####################################################################

# uncomment what you want
makeTNP()
#moveBack()

# ####################################################################

}}

## LA solution 

Le code ci-dessus montre comment résoudre l\'exemple du problème de dénomination topologique décrit à la page    * [Problème de dénomination topologique](Topological_naming_problem/fr.md) mais exactement les mêmes règles que vous pouvez utiliser pour résoudre d\'autres problèmes. L\'approche est simple    *

1.  Mémorisation de la clé avant toute opération
2.  Recherche de la clé après l\'opération

L\'implémentation particulière peut être différente. Dans cet exemple, le plan est XY, mais vous pouvez faire exactement la même chose pour d\'autres axes. Vous pouvez également choisir d\'autres clés. Dans le cadre du projet [Woodworking](https   *//github.com/dprojects/Woodworking), j\'effectue de nombreuses opérations sur des objets inexistants, ce qui m\'a obligé à résoudre le problème du nom topologique à plusieurs reprises.

Ici, je change les objets Cube en objets Epaisseur de PartDesign    *

![](images/TNP_solution_1.gif )

Dans l\'exemple ci-dessous, je change les Cubes en Chanfreins de PartDesign, j\'ai donc dû stocker la clé pour les bords    *

![](images/TNP_solution_2.gif )

L\'exemple ci-dessous est un peu plus compliqué car comme vous le voyez à l\'écran, les références à l\'objet et à la face changent automatiquement. Mais aussi pour faire un trou j\'appelle une fonction définie dans ma bibliothèque et non directement dans l\'outil. Donc, j\'ai dû utiliser une petite astuce avec la sélection et la désélection, pour obtenir une nouvelle référence    *

![](images/TNP_solution_3.gif )

Il existe de nombreux problèmes de ce type lors de la programmation dans FreeCAD, mais ils peuvent tous être résolus de la même manière. J\'espère que cela vous aidera.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro TNP Solution/fr
