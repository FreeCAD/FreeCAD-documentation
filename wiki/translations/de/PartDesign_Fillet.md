---
- GuiCommand   */de
   Name   *PartDesign Fillet
   Name/de   *PartDesign Verrundung
   MenuLocation   *Part Design → Modifikationen → Verrundung
   Workbenches   *[PartDesign](PartDesign_Workbench/de.md)
   SeeAlso   *[PartDesign Fase](PartDesign_Chamfer/de.md)
---

# PartDesign Fillet/de

## Beschreibung


<div class="mw-translate-fuzzy">

Dieses Werkzeug erstellt Verrundungen (Rundungen) an den ausgewählten Kanten eines Objekts. Ein neuer separater Verrundungseintrag (gefolgt von einer fortlaufenden Nummer, wenn bereits Verrundungen im Dokument vorhanden sind) wird im Projektbaum angelegt.


</div>

## Anwendung

### Add a fillet 


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

### Edit a fillet 

1.  Do one of the following   *
    -   Double-click the Fillet object in the [Tree view](Tree_view.md)
    -   Right-click the Fillet object in the [Tree view](Tree_view.md) and select **Edit Fillet** from the context menu.
2.  The **Fillet parameters** [task panel](Task_panel.md) opens.See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Options

-   To add edges do one of the following   *
    -   Press the **Add** button to start selecting edges and/or faces in the [3D view](3D_view.md).
    -   To select all remaining edges do the following   *
        1.  If required press the **Add** button.
        2.  Use the **Ctrl**+**Shift**+**A** keyboard shortcut, or right-click the list and select **Add all edges** from the context menu. <small>(v0.20)</small> 
-   To remove edges do one of the following   *
    -   Press the **Remove** button to start deselecting edges and/or faces in the [3D view](3D_view.md). Selected elements are highlighted in purple.
    -   Select one or more elements in the list and press the **Del** key, or right-click the list and select **Remove** from the context menu.
-   Set the **Radius** of the fillet.
-   Check the **Use all edges** checkbox to select all edges of the previous feature. This deactivates the selection list and the related buttons. <small>(v0.20)</small> 

## Notes

-   PartDesign Fillet should not be confused with [Part Fillet](Part_Fillet.md). Unless you know what you are doing, [Part Fillet](Part_Fillet.md) should not be used on a PartDesign Body. See [Part and PartDesign](Part_and_PartDesign.md).
-   Fillets cannot completely consume the adjacent faces.

## Properties

See also   * [Property editor](Property_editor.md).

A PartDesign Fillet object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties   *

### Data


{{Properties_Title|Base}}

-    **Base|LinkSub**   * Link to the selected edges and faces of the parent feature. Can be a link to only the parent feature if **Use All Edges** is `True`.

-    **Support Transform|Bool**   * If `True` the filleted shape of the additive/subtractive parent feature will be used when the fillet object is included in a [pattern](PartDesign_Workbench#Transformation_tools.md), else only the shape of the fillet itself will be used. The default is `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**   * Link to the parent feature.

-    **_ Body|LinkHidden|hidden**   * Link to the parent body.


{{Properties_Title|Fillet}}

-    **Radius|QuantityConstraint**   * The fillet radius. The default is {{value|1 mm}}.

-    **Use All Edges|Bool**   * If `True` all edges of the feature are filleted, and the edges specified by **Base** are ignored. The default is `False`.


{{Properties_Title|Part Design}}

-    **Refine|Bool**   * If `True` redundant edges are removed from the result of the operation. The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).


<div class="mw-translate-fuzzy">

## Bekannte Probleme 


</div>


<div class="mw-translate-fuzzy">

Verrundungen, Fasen und andere Funktionen, die auf Festkörpern arbeiten, hängen vom zugrunde liegenden OpenCASCADE Technology (OCCT) Kernel ab, den FreeCAD verwendet. Der OCCT Kernel hat gelegentlich Schwierigkeiten, mit zufälligen scharfen Kanten umzugehen, wenn sich zwei Seiten treffen. Wenn dies der Fall ist, kann FreeCAD ohne Erklärung abstürzen.


</div>


<div class="mw-translate-fuzzy">

Wenn FreeCAD vom Terminal aus gestartet wird, kann es nach dem Absturz ein solches Protokoll ausgeben   *


</div>


{{code|lang=text|code=
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


<div class="mw-translate-fuzzy">

Diese Ausgabe verweist auf Funktionen, die sich in `libTKBRep.so`, `libTKFillet.so`, usw. befinden und OCCT Bibliotheken sind. Wenn diese Art von Abstürzen auftritt, muss das Problem möglicherweise in OCCT und nicht in FreeCAD berichtet und gelöst werden.


</div>

Siehe die Forenbeiträge für weitere Informationen   *

-   [Fehler Fase größer als 2 mm verursacht Freecad Abstürze](https   *//forum.freecadweb.org/viewtopic.php?p=263818#p263818)
-   [Segmentfehler bei der Verwendung von Part Design Verrundung](https   *//forum.freecadweb.org/viewtopic.php?p=264827#p264827)

### Topological naming 


<div class="mw-translate-fuzzy">

### Topologische Benennung 

Kantennummern sind nicht vollständig stabil, daher ist es ratsam, dass Du die Hauptkonstruktionsarbeiten Deines Festkörpers abschließt, bevor Du Funktionen wie Verrundungen und Fasen anwendest, da sonst Kanten den Namen ändern könnten und abgerundete Kanten wahrscheinlich ungültig werden würden.


</div>


<div class="mw-translate-fuzzy">

Lies mehr unter [topologisches Namensproblem](topological_naming_problem/de.md).


</div>





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Fillet/de
