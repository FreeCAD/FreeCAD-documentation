---
- GuiCommand:
   Name:Sketcher ConstrainDistance
   Name/de:Sketcher AbstandFestlegen
   MenuLocation:Sketch → Skizzen-Beschränkungen → Distanz festlegen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**K** **D**
   SeeAlso:[Sketcher XAbstandFestlegen](Sketcher_ConstrainDistanceX/de.md), [Sketcher YAbstandFestlegen](Sketcher_ConstrainDistanceY/de.md)
---

# Sketcher ConstrainDistance/de



## Beschreibung

Die Randbedingung **AbstandFestlegen** legt die Länge einer Linie, den senkrechten Abstand eines Punktes zu einer Linie, den Abstand zwischen zwei Punkten und, {{Version/de|0.21}}, den Abstand zwischen zwei Kreiskurven oder zwischen einem Kreis und einer linie fest.

![](images/Sketcher_ConstrainDistance_example.png )



## Anwendung

1.  Eine Linie, einen Punkt und eine Linie, zwei Punkte, zwei Kreiskurven oder eine Kreiskurve und eine linie auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> [Abstand festlegen](Sketcher_ConstrainDistance/de.md)** in der Sketcher-Werkzeugleiste drücken.
    -   Das Tastaturkürzel **K** dann **D**.
    -   Den Menüeintrag **Sketch → Skizzen-Beschränkungen  → [<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> Abstand festlegen** auswählen.
3.  Ein Dialogfeld wird geöffnet, um den Wert zu bearbeiten oder zu bestätigen. Zum Bestätigen **OK** drücken.

**Hinweis**: Das Werkzeug kann auch ohne vorherige Auswahl gestartet werden (außer bei Kreis-zu-Kreis- und Kreis-zu-Linie-Auswahl). Um den lotrechten Abstand zwischen einem Punkt und einer Linie festzulegen muss der Punkt zuerst ausgewählt werden. Standardmäßig befindet sich der Befehl im Fortsetzungsmodus, um neue Randbedingungen zu erstellen; ein Druck auf die rechte Maustaste oder auf Esc beendet den Befehl.



### Hinweis

Wenn es passt, sollte die Verwendung von **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [XAbstandFestlegen](Sketcher_ConstrainDistanceX/de.md)** oder **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [YAbstandFestlegen](Sketcher_ConstrainDistanceY/de.md)** erwägt werden. Diese Randbedingungen sind robuster und schneller zu berechnen als das Werkzeug **AbstandFestlegen**.



## Skripten

Abstand vom Ursprung:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Abstand zwischen zwei Endpunkten:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Länge der Linie (die GUI erlaubt die Auswahl der Kante, aber das ist nur eine Abkürzung für die Nutzung der beiden Endpunkte derselben Linie):


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Senkrechter Abstand eines Punktes (`Edge, PointOfEdge`) zu einer Linie (`Line`):


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, Line, 0, App.Units.Quantity('123.0 mm')))```

Abstand zwischen den Kanten zweier Kreise:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Circle1, 0, Circle2, 0, App.Units.Quantity('123.0 mm')))```

Die Seite [Sketcher Skripten](Sketcher_scripting.md) erklärt die Werte, die für `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, `PointOfEdge1`, `PointOfEdge2`, `Line`, `Circle1` und `Circle2` verwendet werden können, und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistance/de
