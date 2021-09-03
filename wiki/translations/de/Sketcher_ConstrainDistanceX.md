---
- GuiCommand:/de
   Name:Sketcher ConstrainDistanceX
   Name/de:Skizzierer BeschränkeAbstandX
   MenuLocation:Skizze → Skizzen Beschränkungen → Beschränke Horizontalen Abstand
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Shortcut:**Shift** + **H**
   SeeAlso:[Skizzierer Beschränke Länge](Sketcher_ConstrainDistanceY/de.md), [Skizzierer Beschränke Vertikalen Abstand](Sketcher_ConstrainDistanceY/de.md)
---

## Beschreibung

Fixiert den horizontalen Abstand zwischen zwei Punkten oder Linienenden. Falls nur ein Objekt ausgewählt ist, wird der (horizontale) Abstand zum Ursprung (0,0) festgelegt.

![](images/Constraint_H_Distance.png )

## Anwendung

1.  Greife einen oder zwei Punkte oder eine Linie.
2.  Rufe das Werkzeug auf mehrere Arten auf:
    -   Drücke die **<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Beschränke Horizontalen Abstand](Sketcher_ConstrainDistanceX/de.md)** Schaltfläche in der Werkzeugleiste.
    -   Verwende die **Shift** + **H** Tastaturkürzel. (**H**\' steht für **H**orizontal)
    -   Verwende den **Skizze → Skizziererbeschränkungen → <img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> Beschränke Horizontalen Abstand** aus dem oberen Menü.
3.  Ein Aufklappdialogfeld wird geöffnet, um den Wert zu bearbeiten oder zu bestätigen. Drücke **OK**, um den Wert zu bestätigen.

**Hinweis**: Das Beschränkungswerkzeug kann auch ohne vorherige Auswahl gestartet werden, erfordert aber die Auswahl von zwei Punkten oder einer Linie. Um den Abstand zum Ursprung zu setzen, muss der Ursprungspunkt der Zeichnung ebenfalls selektiert werden. Als Voreinstellung ist der Befehl im \"Continue Mode\", um neue Beschränkungen zu erstellen; drücke die rechte Maustaste oder **Esc** einmal zum Beenden des Befehls.

## Skripten

Abstand vom Ursprung:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, App.Units.Quantity('123.0 mm')))```

Abstand zwischen zwei Endpunkten:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Horizontal span of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Die [Skizzierer Skripten](Sketcher_scripting.md)-Seite erklärt die Werte, die für `Edge1`, `Edge2`, `Edge`, `PointOfEdge1`, `PointOfEdge2`, `PointOfEdge` und `Line` verwendet werden können, und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.





{{Sketcher Tools navi

}}  
