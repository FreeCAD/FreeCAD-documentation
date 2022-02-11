# <img alt="" src=images/preferences-techdraw.svg  style="width:64px;">  TechDraw Roadmap/de


<div class="mw-translate-fuzzy">

Die [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md) wurde offiziell als Teil von FreeCAD in der Version 0.17 eingeführt. Sie ist relativ neu und hat noch nicht die Jahre der Entwicklung hinter sich, von denen einige andere Arbeitsbereich profitiert haben. Dennoch erfüllt TechDraw nun sein ursprüngliches Konstruktionsziel und kann nun \"grundlegende technische Zeichnungen auf der Grundlage des 3D Modells erstellen\".


</div>

Hier ist ein grober Fahrplan der Bereiche, die in Zukunft angegangen werden sollen (in keiner bestimmten Reihenfolge).


<div class="mw-translate-fuzzy">

### Aktuelle Aktivität 

-   Fehlerbehebungen in Vorbereitung auf die Version 0.19
-   Anwendungsprobleme in Vorbereitung auf die Version 0.19


</div>

-   TBD


<div class="mw-translate-fuzzy">

### Demnächst

-   Noch zu definieren


</div>

-   TBD


<div class="mw-translate-fuzzy">

### Jüngste Änderungen 

-   siehe unten


</div>

-   TBD

## Zukünftiges

### Navigation Models 


<div class="mw-translate-fuzzy">

### Navigationsmodelle

TechDraw unterstützt nicht die verschiedenen Navigationsmodelle, die im Rest von FreeCAD verwendet werden (CAD, Blender usw.).


</div>

### HLR vs Face Occlusion 


<div class="mw-translate-fuzzy">

### HLR gegen Flächenokklusion 

TechDraw PartViews verwendet die OCC Algorithmen zur Entfernung verdeckter Linien, um die Form zu projizieren. HLR ist rechenintensiv, und einige (viele? die meisten?) Ansichten erfordern keine Anzeige verdeckter Linien. Eine neue Methode zur Erzeugung von Ansichten ist erforderlich. Dazu kann es erforderlich sein, das Bild direkt von der 3D Anzeige zu erhalten.


</div>

### Draft/Arch coexistence 


<div class="mw-translate-fuzzy">

### Entwurf/Arch Koexistenz 

Es gibt Inkonsistenzen zwischen der Art und Weise, wie die Module Draft/Arch und TechDraw Formen darstellen. Dies schränkt die Eignung von TechDraw für Draft/Arch Anwender ein. Ein bemerkenswerter Mangel ist, dass TechDraw nicht in der Lage ist, Bemaßungen auf die Svg Bilder anzuwenden, die es von Draft/Arch erhält.


</div>

### Templates


<div class="mw-translate-fuzzy">

### Vorlagen

Die Erstellung einer Vorlage mit editierbaren Textfeldern erfordert erhebliches Fachwissen mit [SVG](SVG.md) und einem SVG Editor wie Inkscape. Die Vereinfachung des Erstellungsprozesses von Vorlagen wird eine Priorität im Entwicklungszyklus der Version 0.18 sein.


</div>

### Fehlerbehebungen/Funktionsforderungen

Siehe Bugtracker für aktuelle Informationen.


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Roadmap/de
