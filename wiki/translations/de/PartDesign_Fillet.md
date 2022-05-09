---
- GuiCommand   */de
   Name   *PartDesign Fillet
   Name/de   *PartDesign Verrundung
   MenuLocation   *Part Design → Apply a dress up feature (Verschönerung) → Verrundung
   Workbenches   *[PartDesign Arbeitsbereich](PartDesign_Workbench/de.md)
   SeeAlso   *[Fase](PartDesign_Chamfer.md), [Part Verrundung](Part_Fillet/de.md)
---

# PartDesign Fillet/de


</div>

## Beschreibung

Dieses Werkzeug erstellt Verrundungen (Rundungen) an den ausgewählten Kanten eines Objekts. Ein neuer separater Verrundungseintrag (gefolgt von einer fortlaufenden Nummer, wenn bereits Verrundungen im Dokument vorhanden sind) wird im Projektbaum angelegt.

## Anwendung


<div class="mw-translate-fuzzy">

-   Wähle eine einzelne oder mehrere Kanten oder eine Fläche auf einem Objekt aus und starte das Werkzeug, in dem Du entweder auf sein Symbol klickst oder in das Menü gehst. Wenn du eine Fläche ausgewählt hast, werden alle deine Kanten beim verrunden berücksichtigt.
-   Stelle im erscheinenden [Aufgabenpaneel](Task_panel/de.md) den Verrundungsradius entweder durch Eingabe des Wertes oder durch Klicken auf die Pfeile nach oben/unten ein.
-   Wenn du Kanten oder Flächen hinzufügen möchtest
    -   wähle entweder die Kante/Fläche in der Liste des Dialogs und drücke die Taste **DEL**. *Hinweis*   * Da es mindestens eine Kante für das Formelement geben muss, kann die letzte verbleibende Kante oder Fläche in der Liste nicht entfernt werden.
    -   oder klicke auf die **Entfernen** Schaltfläche. Alle Kanten und Flächen, die zuvor ausgewählt wurden, werden violett hervorgehoben. Wählen Sie die Kante oder die Fläche, die entfernt werden soll.
-   Klicke **OK** zum Bestätigen.
-   Bei einer Kette von Kanten, die tangential zueinander verlaufen, kann eine einzelne Kante ausgewählt werden; die Verrundung erstreckt sich entlang der Kette.
-   Um die Verrundung nach der Validierung der Funktion zu bearbeiten, doppelklicke entweder auf das Label Verrundung im Projektbaum oder klicke mit der rechten Maustaste darauf und wähle **Verrundung bearbeiten**.


</div>

## Notes

-   PartDesign Fillet should not be confused with [Part Fillet](Part_Fillet.md). Unless you know what you are doing, [Part Fillet](Part_Fillet.md) should not be used on a PartDesign Body. See [Part and PartDesign](Part_and_PartDesign.md).
-   Fillets cannot completely consume the adjacent faces.


<div class="mw-translate-fuzzy">

## Bekannte Probleme 


</div>

Verrundungen, Fasen und andere Funktionen, die auf Festkörpern arbeiten, hängen vom zugrunde liegenden OpenCASCADE Technology (OCCT) Kernel ab, den FreeCAD verwendet. Der OCCT Kernel hat gelegentlich Schwierigkeiten, mit zufälligen scharfen Kanten umzugehen, wenn sich zwei Seiten treffen. Wenn dies der Fall ist, kann FreeCAD ohne Erklärung abstürzen.

Wenn FreeCAD vom Terminal aus gestartet wird, kann es nach dem Absturz ein solches Protokoll ausgeben   *


{{code|code=
#1  0x7fff63d660ba in BRep_Tool   *   *Curve(TopoDS_Edge const&, TopLoc_Location&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x2a
#2  0x7fff63d69546 in BRep_Tool   *   *Curve(TopoDS_Edge const&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x46
#3  0x7fff71f4fef5 in ChFi3d_Builder   *   *PerformIntersectionAtEnd(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x3b05
#4  0x7fff71f58307 in ChFi3d_Builder   *   *PerformOneCorner(int, bool) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x1097
#5  0x7fff71ef6218 in ChFi3d_Builder   *   *PerformFilletOnVertex(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x4e8
#6  0x7fff71ef71d1 in ChFi3d_Builder   *   *Compute() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0xe31
#7  0x7fff720ad7c3 in BRepFilletAPI_MakeChamfer   *   *Build() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x33
#8  0x7fff723be48e in PartDesign   *   *Chamfer   *   *execute() from /usr/lib/freecad-daily/lib/_PartDesign.so+0x60e
...
}}

Diese Ausgabe verweist auf Funktionen, die sich in `libTKBRep.so`, `libTKFillet.so`, usw. befinden und OCCT Bibliotheken sind. Wenn diese Art von Abstürzen auftritt, muss das Problem möglicherweise in OCCT und nicht in FreeCAD berichtet und gelöst werden.

Siehe die Forenbeiträge für weitere Informationen   *

-   [Fehler Fase größer als 2 mm verursacht Freecad Abstürze](https   *//forum.freecadweb.org/viewtopic.php?p=263818#p263818)
-   [Segmentfehler bei der Verwendung von Part Design Verrundung](https   *//forum.freecadweb.org/viewtopic.php?p=264827#p264827)

Der Anwender ist auch für die Integrität seines eigenen Modells verantwortlich. Je nach Modell kann es unmöglich sein, eine Verrundung oder Fase durchzuführen, wenn der Körper nicht groß genug ist, um diesen Vorgang zu unterstützen. So wäre es beispielsweise nicht möglich, eine 10 mm Verrundung zu erzeugen, wenn eine Kante nur 5 mm von der nächsten Oberfläche entfernt ist. In diesem Fall wäre der maximale Radius für eine Verrundung 5 mm; der Versuch, einen größeren Wert zu verwenden, kann zu einer Form führen, die nicht berechnet wird, oder sogar zu einem Crash. Wenn die Verwendung der genauen Grenze von 5 mm nicht funktioniert, kann es möglich sein, eine sehr enge Annäherung, wie z.B. 4,9999 mm, zu verwenden, um das gleiche sichtbare Ergebnis zu erzielen.

### Topological naming 


<div class="mw-translate-fuzzy">

### Topologische Benennung 

Kantennummern sind nicht vollständig stabil, daher ist es ratsam, dass Du die Hauptkonstruktionsarbeiten Deines Festkörpers abschließt, bevor Du Funktionen wie Verrundungen und Fasen anwendest, da sonst Kanten den Namen ändern könnten und abgerundete Kanten wahrscheinlich ungültig werden würden.


</div>


<div class="mw-translate-fuzzy">

Lies mehr unter [topologisches Namensproblem](topological_naming_problem/de.md).


</div>

## Skripten


<div class="mw-translate-fuzzy">

Das Werkzeug **[16px|text-top=Fillet|link=PartDesign_Fillet](File   *PartDesign_Fillet.svg.md) [Verrundung](_PartDesign_Fillet/de.md)** kann in einem Makro und in der Python Konsole mit folgender Funktion verwendet werden   *


</div>


```python
Box = Box.makeFillet(3,[Box.Edges[0]]) # 1 Fillet
Box = Box.makeFillet(3,[Box.Edges[1],Box.Edges[2],Box.Edges[3],Box.Edges[4]]) # for several Fillets
```

-   3 = radius
-   Box.Edges\[2\] = Edge with its number


<div class="mw-translate-fuzzy">

Beispiel   *


</div>


```python
import PartDesign
from FreeCAD import Base

Box = Part.makeBox(10,10,10)
Box = Box.makeFillet(3,[Box.Edges[0]]) # pour 1 Fillet
Box = Box.makeFillet(3,[Box.Edges[1],Box.Edges[2],Box.Edges[3],Box.Edges[4]]) # for several Fillets
Part.show(Box)
```





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Fillet/de
