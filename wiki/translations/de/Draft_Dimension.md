---
 GuiCommand:
   Name: Draft Dimension
   Name/de: Draft Maß
   MenuLocation: Anmerkung , Abmessung
   Workbenches: Draft_Workbench/de
   Shortcut: **D** **I**
   Version: 0.8
   SeeAlso: Draft_FlipDimension/de
---

# Draft Dimension/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> **Draft Maß** erstellt ein [lineares Maß](#Lineares_Maß.md), ein[Radiales Maß](#Radiales_Maß.md) oder ein [Winkelmaß](#Winkelmaß.md).

Lineare Maße auf Basis von Kanten und radiale Maße sind parametrisch. Das heißt, dass sie aktualisiert werden, wenn die bemaßte Kante verändert wird. Die bemaßten Kanten können zu Draft-Objekten gehören oder zu Volumenkörpern. Winkelmaße sind nicht parametrisch.

Draft-Maße können auf einem [TechDraw](TechDraw_Workbench/de.md)-Zeichnungsblatt in einer [TechDraw DraftAnsicht](TechDraw_DraftView/de.md) oder [TechDraw ArchAnsicht](TechDraw_ArchView/de.md) angezeigt werden. Alternativ bietet der Arbeitsbereich [TechDraw](TechDraw_Workbench.md) eigene Bemaßungsbefehle, aber die erstellen Maße, die nur auf dem Zeichnungsblatt dargestellt werden und nicht in der [3D-Ansicht](3D_view/de.md).

<img alt="" src=images/Screenshot_Draft_Dimension.jpg  style="width:400px;"> 
*Durch drei Punkte definiertes lineares Maß (Längenmaß)*



## Anwendung

Siehe auch: [Draft Fach](Draft_Tray/de.md), [Draft Fangen](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).



### Lineares Maß 

1.  Wahlweise eine gerade Kante in der [3D-Ansicht](3D_view/de.md) auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Dimension.svg" width=16px> [Abmessung](Draft_Dimension/de.md)** drücken.
    -   Den Menüeintrag **Anmerkung → <img src="images/Draft_Dimension.svg" width=16px> Abmessung** auswählen.
    -   Das Tastaturkürzel **D** dann **I**.
3.  Der Aufgabenbereich **Dimension** wird geöffnet. Siehe [Optionen](#Optionen.md) für mehr Informationen.
4.  Wenn bisher noch keine Kante ausgewählt wurde, wählt man eine der folgenden Möglichkeiten:
    -   
        **E**
        
        oder die Schaltfläche **<img src="images/view-select.svg" width=16px> Kante auswählen** drücken und eine gerade Kante in der [3D-Ansicht](3D_view/de.md) auswählen.

    -   Die **Alt**-Taste drücken und halten, eine gerade Kante in der [3D-Ansicht](3D_view/de.md) auswählen und die **Alt**-Taste loslassen.

    -   Den zu messenden Abstand festlegen durch Auswahl von Punkten:
        -   Den ersten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
        -   Den zweiten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
5.  Zum Positionieren der Maßlinie hat man folgende Möglichkeiten:
    -   Für ein ausgerichtetes Maß:
        -   Einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
    -   Für ein horizontales Maß:
        -   Den Mauszeiger über oder unter die Kante oder die Punkte bewegen.
        -   Die **Shift**-Taste dücken und halten, den Mauszeiger bewegen und einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Für ein vertikales Maß:
        -   Den Mauszeiger links oder rechts neben die Kante oder die Punkte bewegen.
        -   Die **Shift**-Taste dücken und halten, den Mauszeiger bewegen und einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen.



### Radiales Maß 

1.  Wahlweise eine kreisförmige Kante in der [3D-Ansicht](3D_view/de.md) auswählen.
2.  Den Befehl aufrufen, wie oben beschrieben.
3.  Der Aufgabenbereich **Dimension** wird geöffnet. Siehe [Optionen](#Optionen.md) für mehr Informationen.
4.  Wenn bisher noch keine Kante ausgewählt wurde, wählt man eine der folgenden Möglichkeiten:
    -   
        **E**
        
        oder die Schaltfläche **<img src="images/view-select.svg" width=16px> Kante auswählen** drücken und eine kreisförmige Kante in der [3D-Ansicht](3D_view/de.md) auswählen.

    -   Die **Alt**-Taste drücken und halten, eine kreisförmige Kante in der [3D-Ansicht](3D_view/de.md) auswählen unddie **Alt**-Taste loslassen.
5.  Zum Positionieren der Maßlinie hat man folgende Möglichkeiten:
    -   Für ein Durchmessermaß:
        -   Einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
    -   Für ein radiales Maß:
        -   Die **Shift**-Tast drücken und halten und einen Punkt in der [3D-Ansicht](3D_view/de.md).



### Winkelmaß

1.  Den Befehl aufrufen, wie oben beschrieben:
2.  Das Aufgaben-Fenster **Dimension** wird geöffnet. Siehe [Optionen](#Optionen.md) für mehr Informationen.
3.  Eine der folgenden Möglichkeiten auswählen:
    -   
        **E**
        
        oder die Schaltfläche **<img src="images/view-select.svg" width=16px> Kante auswählen** drücken und eine erste gerade Kante in der [3D-Ansicht](3D_view/de.md) auswählen. Diesen Schritt zur Auswahl einer zweiten geraden Kante wiederholen.

    -   Die **Alt**-Taste drücken und halten, zwei gerade Kanten in der [3D-Ansicht](3D_view/de.md) auswählen und die **Alt**-Taste loslassen.
4.  Zum Positionieren der Maßlinie einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen.
5.  Der angezeigte Winkel hängt von den Kanten und dem ausgewählten Punkt ab.



## Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel (für Version 1.0).

-   Zum manuellen Eingeben von Koordinaten, werden die X-, Y- und Z-Komponenten jeweils mit abschließendem **Enter** eingegeben. Oder man drückt die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**, sobald alle gewünschten Werte eingegeben sind. Es ist ratsam, den Mauszeiger aus der [3D-Ansicht](3D_view/de.md) heraus zu bewegen, bevor Koordinaten eingegeben werden.

-    **R**drücken oder die Checkbox **Relativ** aktivieren, um den Relativ-Modus umzuschalten. Ist der Relativ-Modus aktiviert, beziehen sich Koordinaten auf den letzten Punkt, falls vorhanden, andernfalls beziehen sie sich auf den Ursprung des Koordinatensystems.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den Global-Modus umzuschalten. Ist der Global-Modus aktiviert, beziehen sich Koordinaten auf das globale Koordinatensystem, andernfalls beziehen sie sich auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md).

-    **N**drücken oder die Checkbox **Fortsetzen** aktivieren, um den Fortsetzen-Modus umzuschalten. Ist der Fortsetzen-Modus aktiviert, wird der Befehl nach dem Beenden erneut gestartet und ermöglicht so mit dem Erstellen von Maßen fortzufahren. Alle folgenden Maße starten am Endpunkt des vorhergehenden Maßes und verwenden dieselbe Grundlinie wie das erste Maß. Man beachte, dass die Auswahl von Kanten bei aufeinanderfolgenden Maßen nicht möglicht ist.

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. auszuschalten.

-    **Esc**oder die Schaltfläche **Schließen** drücken, um den Befehl fertigzustellen.



## Hinweise

-   Lineare und radiale Draft-Maße können mit dem Befehl [Draft Bearbeiten](Draft_Edit/de.md) editiert werden.
-   Draft-Maße, die mit [FreeCAD Version 0.21](Release_notes_0.21/de.md) erstellt oder gespeichert wurden, sind nicht rückwärtskompatibel.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft Dimension-Objekt ist von einem [App FeaturePython](App_FeaturePython/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Die folgenden sind, wenn nicht anders angegeben, zusätzliche Eigenschaften:



### Daten für lineare und radiale Maße 


{{TitleProperty|Maß}}

-    {{PropertyData/de|Dimline|VectorDistance}}: legt den Punkt fest, durch den die Maßlinie geht.

-    {{PropertyData/de|Linked Geometry|LinkSubList}}: legt das Objekt und die Unterelemente fest mit denen das Maß verbunden ist.

-    {{PropertyData/de|Normal|Vector}}: legt die Normale der Textebene fest.

-    {{PropertyData/de|Support|Link|hidden}}: legt das bemaßte Objekt fest.


{{TitleProperty|Lineares/radiales Maß}}

-    **Direction|Vector**: legt die Richtung des Maßes fest.

-    **Distance|Length**: (nur lesen) legt den Wert des Maßes fest.

-    **End|VectorDistance**: legt den Endpunkt des Maßes fest.

-    **Start|VectorDistance**: legt den Startpunkt des Maßes fest.


{{TitleProperty|Radiales Maß}}

-    **Diameter|Bool**: legt fest, ob ein radiales Maß als Durchmesser Maß ausgegeben wird. Wird bei linearen Maßen nicht verwendet.



### Winkelmaße


{{TitleProperty|Winkelmaß}}

-    **Angle|Angle**: (nur lesen) legt den Wert des Maßes fest.

-    **Center|VectorDistance**: legt die Mitte des Maßes fest.

-    **First Angle|Angle**: legt den Startwinkel des Maßes fest.

-    **Last Angle|Angle**: legt den Endwinkel des Maßes fest.


{{TitleProperty|Maß}}

-    {{PropertyData/de|Dimline|VectorDistance}}: legt den Punkt fest, durch den der Bogen des Maßes geht.

-    {{PropertyData/de|Linked Geometry|LinkSubList|hidden}}: nicht verwendet.

-    {{PropertyData/de|Normal|Vector|hidden}}: legt die Normale der Ebene des Maßes fest.

-    {{PropertyData/de|Support|Link|hidden}}: nicht verwendet.



### Ansicht


{{TitleProperty|Anmerkung}}

-    **Annotation Style|Enumeration**: legt den Stil der Anmerkung die am Maß angebracht ist fest. Siehe [Draft Beschriftungsstil Editor](Draft_AnnotationStyleEditor/de.md).

-    **Scale Multiplier|Float**: legt den allgemeinen Maßstab Faktor der für das Maß gilt fest.


{{TitleProperty|Annzeige  Optionen}}

-    {{PropertyView/de|Display Mode|Enumeration}}: Gibt an, wie der Text angezeigt wird. Ist es {{value|World}}, wird der Text auf einer Ebene angezeigt, die durch die {{PropertyData/de|Normal}} des Maßes festgelegt wird. Ist es {{value|Screen}}, wird der Text immer in Richtung Bildschirm angezeigt. Dies ist eine übernommene Eigenschaft. Die genannten Optionen sind die umbenannten Optionen ({{Version/de|0.21}}).


{{TitleProperty|Graphik}}

-    **Arrow Size|Length**: legt die Größe des Symbols das am Ende der Maßlinie oder des Bogens angezeigt wird fest.

-    **Arrow Type|Enumeration**: legt den Typ des Symbols, dass am Ende einer Maßlinie oder eines Bogens angezeigt wird fest, dieses kann {{value|Punkt}}, {{value|Kreis}}, {{value|Pfeil}}, {{value|Tick}} oder {{value|Tick-2}} sein.

-    **Dim Overshoot|Distance**: legt die zusätzliche Länge die an die Maßlinie addiert wird fest. Wird bei Winkelmaßen nicht verwendet.

-    **Ext Lines|Distance**: legt die Länge der Maßhilfslinien, welche vom der Maßlinie zu den gemessenen Punkten gehen, fest. Verwende {{Value|0}} für volle Maßhilfslinien. Ein negativer Wert legt die Lücke zwischen den Enden der Maßhilfslinien und den gemessenen Punkten fest. Ein positiver Wert legt die maximale Länge der Maßhilfslinien fest. Wird nur bei linearen Maßen verwendet.

-    **Ext Overshoot|Distance**: legt die zusätzliche Länge der Maßhilfslinien über die Maßlinie hinausragend fest. Wird bei Winkelmaßen nicht verwendet.

-    **Flip Arrows|Bool**: legt fest, ob die Richtung der Symbole am Ende der Maßlinie oder des Bogens umgedreht werden soll. Funktioniert nur wenn die Symbole Pfeile sind.

-    **Line Color|Color**: legt die Farbe von Linie oder Bogen und der Pfeile fest.

-    **Line Width|Float**: legt die Breite der Linien oder des Bogens der zum Maß gehört fest.

-    **Show Line|Bool**: legt fest, ob die Maßlinie angezeigt wird. Hat keinen Einfluss auf die Anzeige der Maßhilfslinien und der Überstände. Wird bei Winkelmaßen nicht verwendet.


{{TitleProperty|Text}}

-    **Flip Text|Bool**: legt fest, ob die Richtung des Textes umgedreht werden soll.

-    **Font Name|Font**: Legt die Schrift in der der Text geschrieben wird fest. es kann ein Schriftname, wie {{value|Arial}} sein, ein Standard Stil wie {{value|sans}}, {{value|serif}} oder {{value|mono}}, eine Familie wie {{value|Arial,Helvetica,sans}}, oder ein Name mit einem Stil wie {{value|Arial:Bold}}. Wenn die vorgegebene Schift im System nicht gefunden werden kann, dann wird statt dessen die Standardschrift verwendet.

-    **Font Size|Length**: legt die Größe der Buchstaben fest. der Text kann in der [3D Ansicht](3D_view/de.md) nicht zu sehen sein, wenn der Wert zu klein ist.

-    **Override|String**: legt fest, ob statt des aktuellen Maßwertes ein benutzerdefinierter Text angezeigt wird. Verwende die Zeichenfolge {{value|$dim}} innerhalb des Textes um den aktuellen Maßwert einzufügen.

-    **Text Color|Color**: legt die Farbe des Textes fest. <small>(v0.21)</small> 

-    **Text Position|VectorDistance**: legt die Position des Textes in absoluten Koordinaten fest. {{Value|[0, 0, 0]}} zeigt den Text an seiner Standard Position nahe der Maßlinie oder des Bogens.

-    **Text Spacing|Length**: legt den Abstand zwischen Text und Maßlinie oder Bogen fest.


{{TitleProperty|Einheiten}}

-    **Decimals|Integer**: legt die Anzahl der Nachkommastellen mit der der Maßwert angezeigt wird fest.

-    **Show Unit|Bool**: legt fest ob die Maßeinheit nahe beim Wert der Maßzahl ausgegeben wird. Wird bei Winkelmaßen nicht verwendet.

-    **Unit Override|String**: gibt an, in welcher Maßeinheit der Maßwert angezeigt werden soll, zum Beispiel, {{value|km}}, {{value|m}}, {{value|cm}}, {{value|mm}}, {{value|mi}}, {{value|ft}}, {{value|in}} oder {{value|arch}} für Architekten Einheiten. Lasse dies leer um die Standard Einheit zu verwenden. Wird für Winkelmaße nicht verwendet.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen eines Draft-Maßes wird die Methode `make_dimension` des Draft-Moduls verwendet (<small>(v0.19)</small> ). Diese Methode ersetzt die veraltete Methode `makeDimension`.


```python
dimension = make_dimension(p1, p2, p3=None, p4=None)```

Es gibt mehrere Möglichkeiten,diese Methode aufzurufen, abhängig von den an sie übergebenen Argumenten.


```python
dimension = make_dimension(p1, p2, p3=None)
dimension = make_dimension(object, i1, i2, p4=None)
dimension = make_dimension(object, i1, mode, p4=None)
```

-   Erstellt ein lineares Maß (`dimension`-Objekt), indem es den Abstand zwischen den Punkten `p1` und `p2` misst.
-   Erstellt ein lineares Maß (`dimension`-Objekt), verknüpft mit dem Objekt `object`, das den Abstand zwischen seinen Knotenpunkten mit den Indizes `i1` und `i2` misst.
-   Erstellt ein Bogenmaß (`dimension`-Objekt), verknüpft mit dem Objekt `object`, wobei `i1` der Index der gekrümmten Kante ist, die gemessen wird und `mode` die Art des Maßes festlegt, entweder `"radius"` (Radienmaß) oder `"diameter"` (Durchmessermaß).
    -   
        `p3`
        
        im ersten Aufruf und `p4` in den anderen beiden geben einen optionalenPunkt an, durch den die Maßlinie verlaufen soll.

    -   Alle Punkte werden durch `FreeCAD.Vector`, ihren Ortsvektor festgelegt.

Zum Erstellen eines Winkelmaßes wird die folgende Methode verwendet:


```python
dimension = make_angular_dimension(center, angles, p3, normal=None)
dimension = make_angular_dimension(center, [angle1, angle2], p3, normal=None)
```

-   Erstellt ein Winkelmaß (angular `dimension`) aus `center`, dem gegebenen Mittelpunkt, `angles`, einer Liste mit zwei Elementen, und Punkt `p3`, durch den der Bogen verlaufen soll.
    -   Wenn `angle1 > angle2` ist, wird der angezeigte Winkel aus der Differenz `angle1 - angle2` ermittelt; anderenfalls wird der entgegengesetzte Winkel `360 - (angle2 - angle1)` angezeigt.
    -   Die Winkel sollten in Grad eingegeben werden.

Die Ansicht-Eigenschaften von `dimension` können durch Überschreiben der Attribute geändert werden; z.B. kann `ViewObject.FontSize` (Schrifthöhe) mit einem neuen Wert in Millimetern überschrieben werden.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(-2500, 0, 0)
dimension1 = Draft.make_dimension(p1, p2, p3)
dimension1.ViewObject.FontSize = 200

polygon = Draft.make_polygon(3, radius=1000)
doc.recompute()

p4 = App.Vector(-2000, 1500, 0)
dimension2 = Draft.make_dimension(polygon, 1, 2, p4)
dimension2.ViewObject.FontSize = 200

center = App.Vector(2000, 0, 0)
p5 = App.Vector(3000, 1000, 0)
angle1 = 45
angle2 = 10
dimension3 = Draft.make_angular_dimension(center, [angle1, angle2], p5)
dimension3.ViewObject.FontSize = 200

dimension4 = Draft.make_angular_dimension(center, [angle2, angle1], p5*1.2)
dimension4.ViewObject.FontSize = 200

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Dimension/de
