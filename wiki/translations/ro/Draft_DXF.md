








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

The importer has two modes, settable under **Edit → Preferences → Import/Export → DXF**: One is built-in, C++-based and fast, the other is legacy, coded in Python, slower, and requires the installation of an add-on, but can sometimes handle some entities better and can create more refined FreeCAD objects. Both support all DXF versions starting from R12.

3D objects inside a DXF file are stored under a binary ACIS/SAT blob, which at the moment cannot be read by FreeCAD. Simpler entities like 3DFACEs, though, are supported.

The following DXF objects can be imported:

-   lines
-   polylines (and lwpolylines)
-   circles
-   arcs
-   splines
-   ellipses
-   layers
-   texts and mtexts
-   dimensions
-   blocks (only geometry. texts, dimensions and attributes inside blocks will be skipped)
-   points
-   leaders
-   paper space objects


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

Files are exported in the R14 DXF format which can be handled by many applications.

The following FreeCAD objects can be exported:

-   all of FreeCAD\'s 2D geometry such as Draft objects or sketches
-   3D objects are exported as a flattened 2D view
-   Compound objects are exported as blocks
-   texts
-   colors are mapped from objects RGB colors to autocad color index (ACI). Black will always be \"by layer\"
-   layers are mapped from group names. When groups are nested, the deepest group gives the layer name.
-   dimensions, which are exported with \"Standard\" dimstyle.


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


**See also:**

[Draft API](Draft_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

You can export elements to DXF by using the following function: 
```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

Example: 
```python
import Draft, importDXF

Polygon1 = Draft.makePolygon(3, radius=500)
Polygon2 = Draft.makePolygon(5, radius=1500)

objects = [Polygon1, Polygon2]

importDXF.export(objects, "/home/user/Pictures/myfile.dxf")
```


<div class="mw-translate-fuzzy">


</div>


 

[Category:User Documentation](Category:User_Documentation.md) [Category:File Formats{{\#translation:}}](Category:File_Formats.md)
