 {{Macro/fr
|Name=EdgesToArc
|Icon=Macro_EdgesToArc.png
|Description=Transforme les arêtes sélectionnées si possible en un Arc circulaire. Utile pour restaurer des arcs discrétisés.
|Author=Jreinhardt
|Version=1.0
|Date=2014-01-02
|FCVersion=Toutes versions
|Download=[https://www.freecadweb.org/wiki/images/6/65/Macro_EdgesToArc.png Icône pour votre barre d'outils]
|SeeAlso=[Macro SuperWire](Macro_SuperWire/fr.md)
}}

## Description

Parfois, on rencontre des fils qui contiennent des arcs composés de petits segments de droites. Cela se produit souvent lorsque vous travaillez avec des fichiers provenant d\'autres programmes. Cette macro permet de reconvertir relativement facilement ces arcs \"discrétisés\" en arcs circulaires. Cela réduit la taille du fichier et rend sa gestion plus facile.

Pour utiliser cette macro, vous devez briser le fil en bords individuels à l\'aide de la fonction **<img src="images/Draft_Downgrade.svg" width=16px> [Draft Downgrade](Draft_Downgrade/fr.md)**. Ensuite il suffit de sélectionner les segments que vous voulez convertir en arc circulaire et exécuter la macro. Vous avez besoin d\'au moins deux segments pour exécuter la fonction.

La macro va vérifier si les segments se situent tous sur un cercle commun (segments contigus) et s\'arrêtera si ce n\'est pas le cas. Sinon, un arc sera créé et les segments enlevés.

En raison de petites erreurs dans les calculs, de la fonction **<img src="images/Draft_Upgrade.svg" width=16px> [Draft Upgrade](Draft_Upgrade/fr.md)** la macro peut parfois ne pas de reconstituer toutes les arêtes et arcs. Dans ce cas, la macro [Macro\_SuperWire](Macro_SuperWire/fr.md) offre un moyen plus robuste pour le faire.

## Script

ToolBar Icon ![](images/Macro_EdgesToArc.png )

**Macro\_EdgesToArc.FCMacro**


{{MacroCode|code=

import Draft
import FreeCADGui, FreeCAD
from FreeCAD import Base, Console
from math import atan2, pi, fabs

#This macro replaces a number of edges approximating a circular arc by a proper circular arc.
#It might be necessary to use the superwire macro to recombine the edges back to a wire, because of small errors in the calculations.

sel = FreeCADGui.Selection.getSelection()
if len(sel) < 2:
    Console.PrintError("Too few edges are selected\n")
edges = [s.Shape for s in sel]

start_vertices = []
end_vertices = []
for edge in edges:
    start_vertices.append(edge.Vertexes[0].Point)
    end_vertices.append(edge.Vertexes[1].Point)
vertices = start_vertices + end_vertices

start,end,middle = None,None,None

#find start and end points
for edge in edges:
    is_start = True
    is_end = True
    for point in end_vertices:
        if edge.Vertexes[0].Point.distanceToPoint(point) < 1e-8:
            is_start = False

    for point in start_vertices:
        if edge.Vertexes[1].Point.distanceToPoint(point) < 1e-8:
            is_end = False
    if is_start:
        start = edge.Vertexes[0].Point
    if is_end:
        end = edge.Vertexes[1].Point

#find middle point, at least not too far away from the middle

for v in vertices:
    ratio = v.distanceToPoint(start)/v.distanceToPoint(end)
    if ratio > 0.5 and ratio < 2.:
        middle = v
        break

if middle is None:
    Console.PrintError("Could not find suitable middle point\n")

arc = Part.ArcOfCircle(start,middle,end)

#Check circularity
circular = True
for v in vertices:
    if fabs(v.distanceToPoint(arc.Center) - arc.Radius) > 1e-6:
        Console.PrintError("Edges do not approximate a circular arc\n")
        circular = False
        break

if circular:
        Part.show(arc.toShape())
        for shape in sel:
            FreeCAD.ActiveDocument.removeObject(shape.Name)
}}




