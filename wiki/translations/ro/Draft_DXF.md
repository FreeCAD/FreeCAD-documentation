# Draft DXF/ro
{{TOCright}}

## Description

Draft DXF is a software module used by the <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Open](Std_Open.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import.md) and <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export.md) commands to handle the DXF file format.

![](images/Screenshot_qcad.jpg ) *Qcad drawing exported to DXF, which is subsequently opened in FreeCAD*


<div class="mw-translate-fuzzy">

### Deschiderea

Această funcție deschide un fișier DXF (orice versiune de la 12 la 2007) într-un nou desen. Următoarele tipuri de obiecte DXF sunt suportate în mod curent:

-   lines
-   polylines and lwpolylines
-   circles
-   arcs
-   layers (layers containing objects are conveted to FreeCAD Groups)
-   texts and mtexts
-   dimensions
-   blocks (only geometry. texts, dims and attributes inside blocks will be skipped)
-   points <small>(v0.13)</small> 
-   leaders <small>(v0.13)</small> 

Alte entități DXF nu sunt importate în prezent deoarece nu există un obiect FreeCAD corespunzător. Odată cu implementarea noii funcționalități, va fi posibil să importați mai multe tipuri de entități.


</div>

Two importers are available, which one is used can be specified under **Edit → Preferences... → Import-Export → DXF**. One is built-in, C++-based and fast, the other is legacy, coded in Python, slower, and requires the installation of an add-on, but can handle some entities better and can create more refined FreeCAD objects. Both support all DXF versions starting from R12.

3D solids inside a DXF file are stored under a binary ACIS/SAT blob, which at the moment cannot be read by FreeCAD.

### C++ importer 

This importer can import the following DXF objects:

-   lines
-   polylines (and lwpolylines)
-   arcs
-   circles
-   ellipses
-   splines
-   points
-   texts and mtexts
-   dimensions
-   leaders
-   blocks (only geometry, texts, dimensions and attributes inside blocks are skipped)
-   layers
-   paper space objects

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


<div class="mw-translate-fuzzy">

### Export

DXF-ul exportat este compatibil cu versiunea Autocad 12 sau mai recentă, deci ar trebui să se deschidă în orice aplicație care suportă formatul dxf. În prezent, se exportă următoarele obiecte FreeCAD:

-   linii și fire (polilinii)
-   arce și cercuri
-   texte
-   culorile sunt cartografiate de la obiectele RGB culori la indexul de culoare autocad (ACI). Negrul va fi întotdeauna \"după strat\"
-   straturile sunt mapate din numele grupului. Când grupurile sunt imbricate, cel mai adânc grup dă numele stratului.
-   dimensiuni, care sunt exportate cu dimensiune \"Standard\"


</div>

There are also two exporters. The legacy exporter exports to the R12 DXF format, the C++ exporter to the R14 DXF format. Both formats can be handled by many applications.

### C++ exporter 

Some of the features and limitations of this exporter are:

-   All FreeCAD 2D geometry is exported, except [Draft CubicBezCurves](Draft_CubicBezCurve.md), [Draft BezCurves](Draft_BezCurve.md) and [Draft Points](Draft_Point.md).
-   Straight edges from faces of 3D objects are exported, but curved edges only if they are on a plane parallel to the XY plane of the global coordinate system. Note that a DXF created from 3D objects will contain duplicate lines.
-   Texts and dimensions are not exported.
-   Colors are ignored.
-   Layers are mapped from object names.

### Legacy exporter 

Some of the features and limitations of this exporter are:

-   All FreeCAD 2D geometry is exported, except [Draft Points](Draft_Point.md). But ellipses, B-splines and Bézier curves are not exported properly.
-   3D objects are exported as flattened 2D views.
-   Compound objects are exported as blocks.
-   Texts and dimensions are exported.
-   The colors in the DXF are based on the line color of objects. Black is mapped to \"ByBlock\", other colors are mapped using AutoCAD Color Index (ACI) colors.
-   Layers are mapped from layer and group names. When groups are nested, the deepest group gives the layer name.


<div class="mw-translate-fuzzy">

## Instalarea


</div>


<div class="mw-translate-fuzzy">

**Warning**: Din motive de licență, bibliotecile de import / export dxf nu mai fac parte din codul sursă al FreeCAD. Din acest motiv, ele trebuie să fie instalate de dvs., utilizatorul, după ce ați instalat FreeCAD. Există o modalitate de a permite FreeCAD să facă acest lucru în mod automat sau puteți să o faceți manual.


</div>

## Preferences


<div class="mw-translate-fuzzy">

### Preferințe

Următorii parametrii pot fi specificați în tab-ul [Draft Preferences](Draft_Preferences.md) (menu Edit -\> Preferences -\> Draft):

-   Import style: Aceasta vă permite să alegeți modul în care vor fi desenate obiecte din fișierul dxf în FreeCAD. Puteți alege între:
    -   None: aceasta este cea mai rapidă, nu există nici o conversie, toate obiectele vor fi negre cu lățimea de 2px (implicit FreeCAD)
    -   Utilizați culoarea și lungimea liniei implicite: Toate obiectele importate dxf vor lua linia curentă / culoarea curentă din bara de comandă draft
    -   Culoarea originală și lungimea liniei: Obiectele vor păstra culoarea și lățimea liniei (dacă este specificat) pe care le au în fișierul dxf
    -   Culorile mapate la lungimea liniei: Dacă este selectată această opțiune, se folosește opțiunea de fișier de mapare de mai jos.
-   Fișier de mapare a culorilor: aceasta vă permite să specificați un fișier de mapare care va fi utilizat pentru traducerea culorilor dxf la culoare și la lungime de linie, la fel ca un stil de complot care funcționează în Autocad. Fișierul de mapare trebuie să fie un fișier text separat de file. Există o utilitate gratuită numită [Vizualizator de stil Plot](http://www.noliturbare.com/TablePrintGUI.php) care poate converti fișierele Autocad CTB sau STB (stiluri plot) la fișierele de cartografiere separate în tab-uri, gata de utilizare în FreeCAD. În mod alternativ, avem aici câteva fișiere [ home-mapping](Draft_mapping_files.md) disponibile aici.
-   Import texts: Aceasta vă permite să specificați dacă doriți să importați texte și dimensiuni dxf sau nu. Multe texte ar putea face munca voastră în FreeCAD foarte grea, deci este posibil să doriți să folosiți această opțiune ceva timp.
-   Import obiecte layout: Porniți această opțiune dacă doriți să importați obiect spațiu de hârtie. Acestea vor fi îmbinate în același document ca obiectele spațiului model.


</div>

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To export objects to DXF use the `export` method of the importDXF module.


```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

-   For the Windows OS: use a {{FileName|/}} (forward slash) as the path separator in {{Incode|filename}}.

Example:


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


 

[Category:User Documentation](Category:User_Documentation.md) [Category:File Formats](Category:File_Formats.md)

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft DXF/ro
