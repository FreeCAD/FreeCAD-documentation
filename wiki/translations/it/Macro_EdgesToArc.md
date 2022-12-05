# Macro EdgesToArc/it
{{Macro/it
|Name=EdgesToArc
|Translate=Da Segmento a Arco
|Icon=Macro_EdgesToArc.png
|Description=Sostituisce, se possibile, i segmenti selezionati con un arco di cerchio. Utile per il ripristino di archi discretizzati.
|Author=Jreinhardt
|Version=1.0
|Date=2014-01-02
|FCVersion=Tutte versione
|Download=[https://www.freecadweb.org/wiki/images/6/65/Macro_EdgesToArc.png Icona per la ToolBar]
|SeeAlso=[Macro SuperWire](Macro_SuperWire/it.md)
}}

## Descrizione

A volte si incontrano contorni che contengono archi composti da piccoli segmenti retti. Questo accade spesso quando si lavora con i file di altri programmi. Questa macro rende relativamente facile riconvertire questi archi discretizzati in archi di cerchio. L\'operazione riduce la dimensione del file e lo rende più gestibile.

Per utilizzare questa macro, è necessario degradare il contorno e scomporlo in singoli segmenti con la funzione {{KEY/it|<img src="images/Draft_Downgrade.svg" width=16px> [Draft Downgrade](Draft_Downgrade/it.md)}}. Dopo basta selezionare i segmenti che si desidera sostituire con un arco di cerchio ed eseguire la macro. Servono almeno due segmenti.

La macro controlla se tutti i segmenti si trovano su un cerchio comune e in questo caso crea l\'arco e rimuove i segmenti, altrimenti si interrompe.

A causa di piccole imprecisioni nei calcoli, la funzione {{KEY/it|<img src="images/Draft_Upgrade.svg" width=16px> [Draft Upgrade](Draft_Upgrade/it.md)}} può talvolta non riuscire a ricombinare gli altri bordi e gli archi in un unico contorno. In questo caso la [Macro_SuperWire](Macro_SuperWire/it.md) fornisce un modo più efficace per fare questo.

## Script

ToolBar Icon ![](images/Macro_EdgesToArc.png )

**Macro_EdgesToArc.FCMacro**


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



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro EdgesToArc/it
