---
- GuiCommand:/de
   Name:Sketcher ConstrainDistanceX
   Name/de:Sketcher XAbstandFestlegen
   MenuLocation:Sketch → Skizzen-Beschränkungen → Horizontalen Abstand festlegen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**L**
   SeeAlso:[Sketcher AbstandFestlegen](Sketcher_ConstrainDistance/de.md), [Sketcher YAbstandFestlegen](Sketcher_ConstrainDistanceY/de.md)
---

# Sketcher ConstrainDistanceX/de



## Beschreibung

Legt den horizontalen Abstand zwischen zwei Punkten oder Linienenden fest. Falls nur ein Punkt ausgewählt ist, wird der (horizontale) Abstand zum Ursprung (0,0) festgelegt.

![](images/Constraint_H_Distance.png )



## Anwendung

1.  Einen oder zwei Punkte auswählen oder eine Linie.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Horizontalen Abstand festlegen](Sketcher_ConstrainDistanceX/de.md)** drücken.
    -   Das Tastaturkürzel **L**.
    -   Den Menüeintrag **Sketch → Skizzen-Beschränkungen → [<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> Horizontalen Abstand festlegen** auswählen.
3.  Ein Dialogfeld wird geöffnet, um den Wert zu bearbeiten oder zu bestätigen. Zum Bestätigen **OK** drücken.

**Hinweis**: Das Werkzeug kann auch ohne vorherige Auswahl gestartet werden, erfordert aber die Auswahl von zwei Punkten oder einer Linie. Um den Abstand zum Ursprung zu setzen, muss der Ursprungspunkt der Skizze ebenfalls ausgewählt werden. Standardmäßig ist der Befehl im Fortsetzungsmodus, um neue Randbedingungen zu erstellen; ein Druck auf die rechte Maustaste oder auf **Esc** beendet den Befehl.



## Skripten

Abstand vom Ursprung:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Abstand zwischen zwei Endpunkten:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Die horizontale Länge der Linie (die GUI erlaubt die Auswahl der Kante, aber das ist nur eine Abkürzung für die Nutzung der beiden Endpunkte derselben Linie):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Die Seite [Sketcher Skripten](Sketcher_scripting.md) erklärt die Werte, die für `Edge1`, `Edge2`, `Edge`, `PointOfEdge1`, `PointOfEdge2`, `PointOfEdge` und `Line` verwendet werden können, und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceX/de
