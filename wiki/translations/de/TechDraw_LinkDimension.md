---
- GuiCommand:/de
   Name:TechDraw Dimension Link
   Name/de:TechDraw Bemaßung verknüpfen
   MenuLocation:TechDraw → Bemaßungen → Maß mit 3D Geometrie verknüpfen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Ansicht](TechDraw_View/de.md), [TechDraw ProjektionsGruppe](TechDraw_ProjectionGroup/de.md)
---

# TechDraw LinkDimension/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Mit dem Werkzeug \"Bemaßung verknüpfen\" wird eine Verlinkung zwischen einem 3D-Bauteil und einer Ansicht auf einer Zeichnung erstellt. Dieser Link ermöglicht es den tatsächlichen 3D-Wert anstelle des angezeigten projizierten 2D-Wert zu verwenden.


</div>


<div class="mw-translate-fuzzy">

Dieses Werkzeug wird gewöhnlich dafür verwendet um isometrische Ansichten zu bemaßen. Die projezierte Länge bzw. angezeigte Länge einer Linie in einer isometrischen Zeichnungsansicht ist nicht gleich der tatsächlichen Länge dieser Linie im 3D-Bauteil. In einer rechtwinkligen Ansicht sind die projezierten und tatsächlichen Längen immer gleich.


</div>


<div class="mw-translate-fuzzy">

Dieses Werkzeug verlinkt die tatsächliche Länge einer Linie im 3D-Bauteil mit der angezeigten Länge in der isometrischen Zeichnungsansicht.


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  Erstelle eine geeignete Bemaßung auf dem Zeichenblatt mit einer der folgenden Methoden [Bemaßung Länge](TechDraw_LengthDimension/de.md), [Bemaßung Horizontal](TechDraw_HorizontalDimension/de.md), usw. Diese Bemaßung steht an der richtigen Stelle auf der Seite, zeigt aber den projizierten Bemaßungswert an.
2.  Wähle die Geometrie in der 3D Ansicht, z.B. eine Kante, die der projizierten Geometrie Ihrer Bemaßung entspricht.
3.  Drücke die **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Bemaßungsverknüpfung](TechDraw_LinkDimension/de.md)** Schaltfläche.
4.  Ein Dialog öffnet sich. Wähle eine oder mehrere Bemaßungen aus, die mit der ausgewählten 3D Geometrie verknüpft werden sollen.
5.  Drücke **OK**.


</div>

Nachdem die Verknüpfungsoperation abgeschlossen ist, ändert sich die **MeasureType** Eigenschaft der Bemaßung von `Projected` in `True`.

## Beschränkungen


<div class="mw-translate-fuzzy">

Bemaßungsobjekte sind anfällig für Probleme der \"topologischen Benennung\". Weitere Informationen findest Du in den Informationen im Werkzeug [TechDraw Längenbemaßung](TechDraw_LengthDimension/de.md). Es wird empfohlen, dass das Verknüpfen von Bemaßungen einer der letzten Schritte im Zeichenprozess ist.


</div>

Das Verknüpfungswerkzeug wird dich nicht daran hindern, unlogische Verknüpfungen zu erstellen, daher musst du beim Erstellen der Verknüpfung die richtige Kante aus der 3D Ansicht auswählen.

Es gibt derzeit keine Möglichkeit, eine Verknüpfung zu brechen; du kannst den **MeasureType** wieder in `Projected` ändern, so dass die Bemaßung den projizierten Wert anstelle des verknüpften Wertes verwendet.

Beachte, dass, wenn die zu verknüpfende Bemaßung auf zwei Eckpunkten basiert, Du zwei Eckpunkte in der 3D Ansicht auswählen solltest. Wenn die Bemaßung auf einer Kante basiert, solltest Du eine Kante in der 3D Ansicht auswählen.

## Eigenschaften

1.  Der Eigenschaftwert einer verknüpften Abmessung kann von \"Projected\" auf »True« gesetzt werden um zur perspektivischen Ansicht zu wechseln.

## Programmierung


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


<div class="mw-translate-fuzzy">

Das Bemaßungsverknüpfungswerkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen verwendet werden:


</div>


```python
to be defined
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LinkDimension/de
