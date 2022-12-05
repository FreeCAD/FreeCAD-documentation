# Draft DXF/it
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Descrizione


<div class="mw-translate-fuzzy">

Draft DXF è un modulo software utilizzato dai comandi <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Apri](Std_Open/it.md), [Importa](Std_Import/it.md) and [Esporta](Std_Export/it.md) per gestire il formato DXF.


</div>

![](images/Screenshot_qcad.jpg ) 
*Disegno fatto con Qcad esportato in DXF, e successivamente aperto in FreeCAD*

## Importazione


<div class="mw-translate-fuzzy">

Sono supportate le versioni DXF R12 - 2007.


</div>

3D solids inside a DXF file are stored under a binary ACIS/SAT blob, which at the moment cannot be read by FreeCAD.

### C++ importer 


<div class="mw-translate-fuzzy">

Possono essere importati i seguenti tipi di oggetti DXF:

-   linee
-   polilinee e polilinee alleggerite
-   circonferenze
-   archi
-   layers (i layers contenenti gli oggetti vengono convertiti in gruppi FreeCAD)
-   testi e testi multipli (mtexts)
-   dimensioni
-   blocchi (solo la geometria; i testi, le dimensioni e gli attributi all\'interno di blocchi sono ignorati)
-   punti
-   linee guida
-   \... e altro


</div>

### Legacy importer 

This importer can import the following DXF objects:

-   lines
-   polylines (and lwpolylines)
-   arcs
-   circles
-   ellipses
-   splines
-   3D faces
-   texts and mtexts
-   leaders
-   layers

## Esportazione


<div class="mw-translate-fuzzy">

I file vengono esportati nel formato DXF R12 che può essere gestito da molte applicazioni.


</div>

### C++ exporter 

Some of the features and limitations of this exporter are:

-   All FreeCAD 2D geometry is exported, except [Draft CubicBezCurves](Draft_CubicBezCurve.md), [Draft BezCurves](Draft_BezCurve.md) and [Draft Points](Draft_Point.md).
-   Straight edges from faces of 3D objects are exported, but curved edges only if they are on a plane parallel to the XY plane of the global coordinate system. Note that a DXF created from 3D objects will contain duplicate lines.
-   Texts and dimensions are not exported.
-   Colors are ignored.
-   Layers are mapped from object names.

### Legacy exporter 


<div class="mw-translate-fuzzy">

Possono essere esportati i seguenti oggetti FreeCAD:

-   linee e spezzate (polilinee)
-   archi e circonferenze
-   testi
-   i colori sono mappati dai colori RGB degli oggetti secondo l\'indice dei colori di autocad (ACI). Il nero è sempre \"da layer\"
-   i layers sono mappati dai nomi dei gruppi. Quando i gruppi sono nidificati, il gruppo più interno attribuisce il nome al livello (layer)
-   le dimensioni, che vengono esportate con dimstyle \"Standard\"
-   \... e altro


</div>

## Installazione


<div class="mw-translate-fuzzy">

Per motivi di licenza, le librerie di importazione e di esportazione [DXF](DXF/it.md) richieste non fanno parte del codice sorgente di FreeCAD.

Per ulteriori informazioni, consultare: [Importare i file DXF in FreeCAD](FreeCAD_and_DXF_Import/it.md).


</div>

## Preferenze


<div class="mw-translate-fuzzy">

Per ulteriori informazioni, consultare: [Preferenze di Importa/Esporta](Import_Export_Preferences/it.md).


</div>

## DWG

Because the DWG format is a proprietary, closed and undocumented format it is hard for open-source projects like FreeCAD to support it. That is why FreeCAD relies on external converters to read and write DWG files. To import a DWG file a converter is used to create a DXF first, which can then be processed by the FreeCAD DXF importer. When exporting to DWG the opposite conversion happens: the DXF created by the FreeCAD DXF exporter is turned into a DWG.

Note that the DXF format allows a 1:1 conversion of the DWG format. All applications that can read and write DWG files can do the same with DXF files, with no data loss. So asking for DXF files instead of DWG files, and supplying DXF files in turn, should not cause any problems.

There is built-in support for the following DWG converters:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, lacks support for some DWG entities).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). <small>(v0.20)</small> 

See [Import Export Preferences](Import_Export_Preferences#DWG.md) and [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) for more information.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[API Draft](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Si possono esportare elementi in DXF usando la seguente funzione:


</div>


```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

-   For the Windows OS: use a **/** (forward slash) as the path separator in {{Incode|filename}}.

Esempio:


```python
import FreeCAD as App
import Draft
import importDXF

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=500)
polygon2 = Draft.make_polygon(5, radius=1500)

doc.recompute()

objects = [polygon1, polygon2]
importDXF.export(objects, "/home/user/Pictures/myfile.dxf")
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Draft](Draft_Workbench.md) > Draft DXF/it
