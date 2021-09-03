
{{Page in progress}}




<div class="mw-translate-fuzzy">


{{docnav/it|[SVG](Draft_SVG/it.md)|[Airfoil Data Format .DAT](Draft_DAT/it.md)|[Draft](Draft_Module/it.md)|IconC=Workbench_Draft.svg}}


</div>


{{TOCright}}

## Descrizione


<div class="mw-translate-fuzzy">

Draft OCA è un modulo software utilizzato dai comandi <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Open](Std_Open/it.md), [Std Import](Std_Import/it.md) and [Std Export](Std_Export/it.md) per gestire il [formato OCA](http://groups.google.com/group/open_cad_format).


</div>

Il formato di file OCA è uno sforzo della comunità per creare un formato di file CAD gratuito, semplice e aperto. OCA è in gran parte basato sul formato di file GCAD generato da [gCAD3D](http://www.gcad3d.org/). Entrambi i formati possono essere importati in FreeCAD e i file OCA esportati da FreeCAD possono essere aperti in gCAD3D.

## Importazione

Si posssono importare i seguenti oggetti OCA:

-   Linee
-   Archi e circonferenze
-   Aree chiuse

## Esportazione

È possibile esportare i seguenti oggetti FreeCAD:

-   Linee e spezzate (polilinee)
-   Archi e circonferenze
-   Facce

## Preferenze

Per ulteriori informazioni, consultare: [Preferenze di Importa/Esporta](Import_Export_Preferences/it.md).

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Si possono esportare elementi in Oca usando la seguente funzione: 
```python
importOCA.export(exportList, filename)
```

Esempio: 
```python
import FreeCAD, Draft, importOCA

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(1000, 1000, 0)
p3 = FreeCAD.Vector(2200, 1500, 0)
p4 = FreeCAD.Vector(2500, -100, 0)

obj1 = Draft.makeWire([p1, p2, p3, p4])
obj2 = Draft.makeWire([p1, -2.3*p2, -0.8*p3, -1.8*p4])

objects = [obj1, obj2]

importOCA.export(objects, "/home/user/Pictures/myfile.oca")
```


<div class="mw-translate-fuzzy">


{{docnav/it|[SVG](Draft_SVG/it.md)|[Airfoil Data Format .DAT](Draft_DAT/it.md)|[Draft](Draft_Module/it.md)|IconC=Workbench_Draft.svg}}


</div>


 

[Category:File Formats{{\#translation:}}](Category:File_Formats.md)
