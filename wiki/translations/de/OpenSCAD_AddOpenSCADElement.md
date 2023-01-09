---
- GuiCommand:/de
   Name:OpenSCAD AddOpenSCADElement
   Name/de:OpenSCAD HinzufügenOpenSCADElement
   Empty:1
   MenuLocation:OpenSCAD -> Hinzufügen OpenSCAD Element
   Workbenches:[OpenSCAD](OpenSCAD_Workbench/de.md)
---

# OpenSCAD AddOpenSCADElement/de

## Description


<div class="mw-translate-fuzzy">

## Beschreibung

Füge ein OpenSCAD Element hinzu, indem du OpenSCAD Code in das Aufgabenfeld eingibst und die OpenSCAD Binärdatei ausführst (erfordert OpenSCAD).


</div>

When \'as mesh\' is selected, OpenSCAD renders a Mesh.

Jedesmal beim Drücken von Einfügen wird OpenSCAD-Code ausgeführt und Elemente werden importiert.


<div class="mw-translate-fuzzy">

Falls OpenSCAD erfolgreich zurückkehrt, werden die Meldungen als Warnungen im Reportfenster angezeigt. Dies wird der Fall sein, wenn der Pfad importiert und eingefügt wird und benutzte Dateien defekt sind. Im Falle von ungewünschten Ergebnissen wird dringend empfohlen, einen Blick auf das Reportfenster zu werfen, denn dort könnten viele Ausgaben vom Importer sein. Falls OpenSCAD fehlschlägt, werden die Meldungen als Fehler dargestellt. Bibliotheken können wie gewohnt erreichbar sein, Beispiele hingegen können wie unten gezeigt erreicht werden


</div>

Libraries should be accessible as usual, whereas example can be reached as stated below.


```python
include <../examples/example001.scad>;
```


<div class="mw-translate-fuzzy">

würde die ersten Beispiele einbinden, auch als das OpenSCAD-Symbol bekannt


</div>

## Setup OpenSCAD within FreeCAD 


<div class="mw-translate-fuzzy">

## Installation von OpenSCAD innerhalb von FreeCAD 

**Hinweis:** OpenSCAD muss auf deinem Computer installiert sein, damit FreeCAD diese Funktionalität nutzen kann
Installiere OpenSCAD in der für dein Betriebssystem entsprechenden Weise. Siehe [the OpenSCAD web site](https://www.openscad.org/) für mehr Informationen


</div>

FreeCAD needs to be told where to find the OpenSCAD executable:

-   Switch to the <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [OpenSCAD Workbench](OpenSCAD_Workbench.md) via 
**View → Workbench → OpenSCAD**
-   Open the preferences dialog **Edit → Preferences**
-   Click on \"OpenSCAD\" on the left plane
-   Click on the button labled **...** in **General Settings → General OpenSCAD Settings → OpenSCAD executable** to browse the directory or enter the path (e.g. Ubuntu based Linux distributions `/usr/bin/openscad`) directly into the line input right to the button
-   Close and restart FreeCAD

:   **Result:** A new OpenSCAD icon will appear on the tool bar, and in the OpenSCAD menu, in the FreeCAD OpenSCAD workbench.

Hinweis: Es ist ebenso möglich einen anderen Optionalen Paramter hinzuzufügen, der die maximalen Seiten eines Polygons steuert bevor es als ein Kreis angesehen wird (fn).


<div class="mw-translate-fuzzy">

Beginnend mit <small>(v0.14)</small>  sucht FreeCAD nach der OpenSCAD ausführbaren wenn oben genannte Einstellung leer ist.


</div>





{{OpenSCAD_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD AddOpenSCADElement/de
