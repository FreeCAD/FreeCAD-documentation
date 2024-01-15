---
 GuiCommand:
   Name: TechDraw AxoLengthDimension
   Name/de: TechDraw AxonometrischesLängenmaß
   MenuLocation: TechDraw , Maßeinträge , Axonometrisches Längenmaß
   Workbenches: TechDraw_Workbench/de
   Version: 0.21
---

# TechDraw AxoLengthDimension/de



## Beschreibung

Das Werkzeug **TechDraw AxonometrischesLängenmaß** fügt einer axonometrischen Ansicht ein Längenmaß hinzu. Das Maß kann die Länge einer Kante oder der Abstand zwischen zwei Punkten sein.

<img alt="" src=images/TechDraw_AxoLengthDimensionExample.png  style="width:300px;"> 
*Axonometrische Längenmaße basierend auf einer Kante (blau) und zwei Punkten (rot)*



## Anwendung

1.  Eine der folgenden Möglichkeiten auswählen:
    -   Zwei Kanten (e1 und e2 im Bild) auswählen. Die erste Kante definiert die Ausrichtung der Maßlinie und den gemessenen Abstand. Die zweite Kante definiert die Ausrichtung der Maßhilfslinien.
    -   Zwei Kanten (e3 und e4 im Bild) und zwei Punkte (v1 und v2 im Bild) auswählen. Die erste Kante definiert die Ausrichtung der Maßlinie. Die zweite Kante definiert die Ausrichtung der Maßhilfslinien. Die Punkte bestimmen den gemessenen Abstand.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_AxoLengthDimension.svg" width=16px> [Axonometrisches Längenmaß](TechDraw_AxoLengthDimension/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Maßeinträge → <img src="images/TechDraw_AxoLengthDimension.svg" width=16px> Axonometrisches Längenmaß** auswählen.
3.  Ein axonometrisches Längenmaß wird zur Ansicht hinzugefügt.
4.  Das Maß kann an die gewünschte Position gezogen werden.
5.  Falls erforderlich, können Toleranzen, wie auf der [GD&T-Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben, hinzugefügt werden.



### 3D-Abmessungen anzeigen 

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#3D-Abmessungen_anzeigen.md).


<div lang="en" dir="ltr" class="mw-content-ltr">


<small>(v0.22)</small> 

: When dimensioning edges parallel to the global coordinate system axes, the actual (3D) value is calculated automatically and inserted into the dimension label as a text.


</div>



### Eigenschaften anpassen 

Um die Eigenschaften eines Maßes (Dimension-Objekt) zu ändern, wird es in der Zeichnung oder in der [Baumansicht](Tree_view/de.md) doppelt angeklickt. Dadurch wird der Dialog [Maßeintrag](TechDraw_LengthDimension/de#Dialog_Maßeintrag.md) geöffnet.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AxoLengthDimension/de
