---
- GuiCommand:/de
   Name:TechDraw Dimension Link
   Name/de:TechDraw MaßVerknüpfen
   MenuLocation:TechDraw → Bemaßungen → Maß mit 3D Geometrie verknüpfen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Ansicht](TechDraw_View/de.md), [TechDraw ProjektionsGruppe](TechDraw_ProjectionGroup/de.md)
---

# TechDraw LinkDimension/de

## Beschreibung

Das Werkzeug MaßVerknüpfen erstellt eine Verknüpfung zwischen einer 3D-Geometrie und einem oder mehreren projizierten Maß(en) auf einer (Zeichnungs-)Seite. Diese Verknüpfung ermöglicht es dem Maß den tatsächlichen 3D-Wert anstelle des projizierten 2D-Wertes zu verwenden.

Dieses Werkzeug wird meistens dafür verwendet, isometrische Ansichten einer Projektionsgruppe zu bemaßen. Die projizierte Länge (angezeigte Länge) einer Linie in einer isometrischen Zeichnungsansicht muss nicht zwangsläufig der tatsächlichen Länge dieser Linie im 3D-Bauteil entsprechen. In einer rechtwinkligen Ansicht sind die projizierten und tatsächlichen Längen immer gleich.

Diese Verknüpfung veranlasst das Maß seinen Wert direkt von der 3D-Geometrie abzuleiten.

## Anwendung

1.  Ein geeignetes Maß auf dem Zeichenblatt erstellen; mit einer der Bemaßungsfunktionen [Längenmaß](TechDraw_LengthDimension/de.md), [MaßHorizontal](TechDraw_HorizontalDimension/de.md), usw. Dieses Maß steht an der richtigen Stelle auf der Seite, zeigt aber den Wert des projizierten Maßes an.
2.  Auswahl der Geometrie in der 3D-Ansicht, z.B. eine Kante, die der bemaßten projizierten Geometrie entspricht.
3.  Schaltfläche **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Maß mit 3D-Geometrie verknüpfen](TechDraw_LinkDimension/de.md)** drücken.
4.  Ein Dialog öffnet sich. Ein oder mehrere Maß(e) auswählen, die mit der ausgewählten 3D-Geometrie verknüpft werden sollen.
5.  Drücke **OK**.

Nachdem die Verknüpfungsoperation abgeschlossen ist, ändert sich die **MeasureType** Eigenschaft der Bemaßung von `Projected` in `True`.

## Beschränkungen

Dimension-Objekte (Maße) sind anfällig für das \"[Topological-Naming-Problem](topological_naming_problem/de.md)\" (Problem der topologischen Benennung). Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de.md) für weitere Informationen. Es wird empfohlen, dass das Verknüpfen von Maßen einer der letzten Schritte der Zeichnungserstellung ist.

Das Verknüpfungswerkzeug wird dich nicht daran hindern, unlogische Verknüpfungen zu erstellen, daher musst du beim Erstellen der Verknüpfung die richtige Kante aus der 3D Ansicht auswählen.

Es gibt derzeit keine Möglichkeit, eine Verknüpfung zu brechen; du kannst den **MeasureType** wieder in `Projected` ändern, so dass die Bemaßung den projizierten Wert anstelle des verknüpften Wertes verwendet.

Beachte, dass, wenn die zu verknüpfende Bemaßung auf zwei Eckpunkten basiert, Du zwei Eckpunkte in der 3D Ansicht auswählen solltest. Wenn die Bemaßung auf einer Kante basiert, solltest Du eine Kante in der 3D Ansicht auswählen.

## Eigenschaften

1.  Der Eigenschaftwert einer verknüpften Abmessung kann von \"Projected\" auf »True« gesetzt werden um zur perspektivischen Ansicht zu wechseln.

## Programmierung


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug MaßVerknüpfung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
to be defined
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LinkDimension/de
