---
- GuiCommand:
   Name: Part CheckGeometry‏‎
   Name/de: Part GeometriePrüfen
   MenuLocation: Formteil - Geometrie überprüfen
   Workbenches: [Part](Part_Workbench/de.md)
---

# Part CheckGeometry/de



## Beschreibung

Das Werkzeug **<img src="images/Part_CheckGeometry.svg" width=16px> [Part GeometriePrüfen](Part_CheckGeometry.md)** führt eine Überprüfung durch und meldet, ob die Geometrie ein gültiger Volumenkörper ist.



## Anwendung

1.  Ein Teil auswählen (dabei darauf achten, das gesamte Teil auszuwählen und nicht nur eine Fläche, um zu prüfen, ob es ein gültiger Volumenkörper ist)
2.  Das Werkzeug aufrufen, durch eine der folgenden Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Part_CheckGeometry.svg" width=16px> Geometrie überprüfen** anklicken, die sich in der Werkzeugleiste des Arbeitsbereichs Part befindet.
    -   Den Meinüeintrag **Formteil → <img src="images/Part_CheckGeometry.svg" width=16px> Geometrie überprüfen** im Hauptmenü auswählen.

Ergebnisse werden im [Aufgabenbereich](Task_panel/de.md) aufgeführt. Wenn die Prüfung einen Fehler anzeigt: Im Reportfenster eine bestimmte Fehlernachricht anklicken und das entsprechende geometrische Objekt (Kante, Fläche usw.) wird in der [3D-Ansicht](3D_view/de.md) hervorgehoben.



## Optionen

### Skip settings page 

If ticked, subsequent invocations of the tool skip showing the **Settings** task panel.



### BOP-Check ausführen 

Wenn aktiviert, wird eine zusätzliche eine Prüfung der booleschen Operationen durchgeführt (BOP check).

### Log errors 

Wenn aktiviert, werden alle gefundenen Fehler auch im [Ausgabefenster](Report_view/de.md) gelistet.



## Form-Inhalt 

In addition to detecting potential geometry errors, this tool shows a range of properties regarding the selected object:

-   Checked object
-   Shape type
-   Number of geometric entities: vertices, edges, wires, faces, shells, solids, compsolids, compounds, total shapes
-   Geometric and mass properties:
    -   Area
    -   Volume
    -   Mass
    -   Length
    -   Center of mass
    -   Orientation
    -   Symmetry axis
    -   Symmetry point
    -   Moments
    -   First axis of inertia
    -   Second axis of inertia
    -   Third axis of inertia
    -   Radius of gyration
    -   Global placement



## Hinweise

-   [App-Link](App_Link/de.md)-Objekte verknüpft mit passenden Objektarten und [App-Part](App_Part/de.md)-Container, die passende sichtbare Objekte enthalten, können auch mit diesem Werkzeug überprüft werden. Für [App-Link](App_Link/de.md)-Objekte wird die Form des verknüpften Objekts geprüft. Für [App-Part](App_Part/de.md)-Container werden die enthaltenen sichtbaren Objekte als Verbund geprüft. {{Version/de|0.20}}
-   FreeCAD hat keine Möglichkeiten Geometrien automatisch zu reparieren. Wenn Fehler entdeckt werden, müssen die erforderlichen Schritte, um das Modell zu erstellen, untersucht und von Hand korrigiert werden.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CheckGeometry/de
