---
 GuiCommand:
   Name: TechDraw Dimension Link
   Name/de: TechDraw MaßVerknüpfen
   MenuLocation: TechDraw , Maßeinträge , Maß mit 3D-Geometrie verknüpfen
   Workbenches: TechDraw_Workbench/de
   SeeAlso: TechDraw_View/de, TechDraw_ProjectionGroup/de
---

# TechDraw LinkDimension/de

Das Werkzeug **TechDraw MaßVerknüpfen** wird zukünftig als überholt gelten. Das Werkzeug [TechDraw Maßreparatur](TechDraw_DimensionRepair/de.md) kann zum Ändern von sowohl 2D- als auch 3D-Referenzen verwendet werden.



## Beschreibung

Das Werkzeug **TechDraw MaßVerknüpfen** erstellt eine Verknüpfung zwischen einer 3D-Geometrie und einem oder mehreren projizierten Maß(en) auf einem Zeichnungsblatt. Diese Verknüpfung ermöglicht es dem Maß den tatsächlichen 3D-Wert anstelle des projizierten 2D-Wertes zu verwenden.

Dieses Werkzeug wird meistens dafür verwendet, isometrische Ansichten einer Projektionsgruppe zu bemaßen. Die projizierte Länge (angezeigte Länge) einer Linie in einer isometrischen Zeichnungsansicht muss nicht zwangsläufig der tatsächlichen Länge dieser Linie im 3D-Bauteil entsprechen. In einer rechtwinkligen Ansicht sind die projizierten und tatsächlichen Längen immer gleich.

Diese Verknüpfung veranlasst das Maß seinen Wert direkt von der 3D-Geometrie abzuleiten.



## Anwendung

1.  Ein geeignetes Maß mit einer der Bemaßungsfunktionen [Längenmaß](TechDraw_LengthDimension/de.md), [MaßHorizontal](TechDraw_HorizontalDimension/de.md) usw. auf dem Zeichnungsblatt erstellen. Dieses Maß steht an der richtigen Stelle auf der Seite, zeigt aber den Wert des projizierten Maßes an.

2.  Auswahl der Geometrie in der 3D-Ansicht, z.B. eine Kante, die der bemaßten projizierten Geometrie entspricht.

3.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Maß mit 3D-Geometrie verknüpfen](TechDraw_LinkDimension/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Maßeinträge  → <img src="images/TechDraw_LinkDimension.svg" width=16px> Maß mit 3D-Geometrie verknüpfen** auswählen.

4.  Der Aufgaben-Bereich wird geöffnet.

5.  Ein oder mehrere Maß(e) auswählen, die mit der ausgewählten 3D-Geometrie verknüpft werden sollen.

6.  
    **OK**drücken.

Die Verknüpfungsoperation ändert die {{PropertyData/de|MeasureType}} des Maßes von `Projected` (projiziertes Maß) auf `True` (tatsächliche Länge).



## Einschränkungen

Dimension-Objekte (Maße) sind anfällig für das \"[Topological-Naming-Problem](topological_naming_problem/de.md)\" (Problem der topologischen Benennung). Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de.md) für weitere Informationen. Es wird empfohlen, dass das Verknüpfen von Maßen einer der letzten Schritte der Zeichnungserstellung ist.

Das Verknüpfungswerkzeug hindert niemanden daran, unlogische Verknüpfungen zu erstellen, daher muss jeder selbst darauf achten, beim Erstellen der Verknüpfung die richtige Kante aus der 3D Ansicht auzuswählen.

Es gibt derzeit keine Möglichkeit, eine Verknüpfung aufzulösen, aber die {{PropertyData/de|MeasureType}} kann zurück auf `Projected` geändert werden, so dass das Maß wieder den projizierten Wert anstelle des verknüpften Wertes verwendet.

Zu beachten ist, dass, wenn das zu verknüpfende Maß auf zwei Eckpunkten basiert, zwei Eckpunkte in der 3D-Ansicht ausgewählt werden sollten. Wenn das Maß auf einer Kante basiert, sollte eine Kante in der 3D-Ansicht ausgewählt werden.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug TechDraw MaßVerknüpfen kann nicht direkt in Makros verwendet werden, aber durch das Ändern der {{PropertyData/de|References 3D}} kann das gleiche Ergebnis erreicht werden.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LinkDimension/de
