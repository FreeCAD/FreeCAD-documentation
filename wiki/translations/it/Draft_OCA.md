# Draft OCA/it
<div class="mw-translate-fuzzy">


{{docnav/it
|[SVG](Draft_SVG/it.md)
|[Airfoil Data Format .DAT](Draft_DAT/it.md)
|[Draft](Draft_Workbench/it.md)
|IconC=Workbench_Draft.svg
}}


</div>


{{TOCright}}

## Descrizione


<div class="mw-translate-fuzzy">

Draft OCA è un modulo software utilizzato dai comandi <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Open](Std_Open/it.md), [Std Import](Std_Import/it.md) and [Std Export](Std_Export/it.md) per gestire il [formato OCA](http://groups.google.com/group/open_cad_format).


</div>


<div class="mw-translate-fuzzy">

Il formato di file OCA è uno sforzo della comunità per creare un formato di file CAD gratuito, semplice e aperto. OCA è in gran parte basato sul formato di file GCAD generato da [gCAD3D](http://www.gcad3d.org/). Entrambi i formati possono essere importati in FreeCAD e i file OCA esportati da FreeCAD possono essere aperti in gCAD3D.


</div>

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


<div class="mw-translate-fuzzy">

Per ulteriori informazioni, consultare: [Preferenze di Importa/Esporta](Import_Export_Preferences/it.md).


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Si possono esportare elementi in Oca usando la seguente funzione:


</div>


```python
importOCA.export(exportList, filename)
```

-   For the Windows OS: use a {{FileName|/}} (forward slash) as the path separator in {{Incode|filename}}.

Esempio:


```python
import FreeCAD as App
import Draft
import importOCA

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=500)
polygon2 = Draft.make_polygon(5, radius=1500)

doc.recompute()

objects = [polygon1, polygon2]
importOCA.export(objects, "/home/user/Pictures/myfile.oca")
```


<div class="mw-translate-fuzzy">


{{docnav/it
|[SVG](Draft_SVG/it.md)
|[Airfoil Data Format .DAT](Draft_DAT/it.md)
|[Draft](Draft_Workbench/it.md)
|IconC=Workbench_Draft.svg
}}


</div>


 

[Category:File Formats](Category:File_Formats.md)

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft OCA/it
