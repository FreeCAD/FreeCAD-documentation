---
 GuiCommand:
   Name: Sketcher ConstrainDistanceY
   Name/de: Sketcher YAbstandFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Vertikalen Abstand festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **I**
   SeeAlso: Sketcher_ConstrainDistanceX/de, Sketcher_ConstrainDistance/de
---

# Sketcher ConstrainDistanceY/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [YAbstandFestlegen](Sketcher_ConstrainDistanceY/de.md): Legt den vertikalen Abstand zwischen zwei Punkten oder den Endpunkten einer Linie fest. Ist ein einzelner Punkt vorausgewählt, bezieht sich der Abstand auf den Ursprung der Skizze.

![](images/Sketcher_ConstraintDistanceY_example.png )



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass nichts ausgewählt ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   
        {{Version/de|1.0}}
        
        : Ist die [Voreinstellung](Sketcher_Preferences/de#Allgemein.md) **Werkzeuge für Maßeinträge** auf {{Value|Einzelnes Werkzeug}} (Standardeinstellung) gesetz: Den Abwärtspfeil rechts neben der Schaltfläche **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** drücken und im Ausklappmenü **<img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Vertikalen Abstand festlegen** auswählen.

    -   Hat die Voreinstellung einen anderen Wert (und in {{VersionMinus/de|0.21}}): Die Schaltfläche **<img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> [Vertikalen Abstand festlegen](Sketcher_ConstrainDistanceY/de.md)** drücken.

    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Vertikalen Abstand festlegen** auswählen.

    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **Bemaßung → <img src="images/Sketcher_ConstrainDistanceY.svg" width=16px> Vertikalen Abstand festlegen** im Kontextmenü auswählen.

    -   Das Tastaturkürzel **I**.
3.  Für weitere Schritte siehe [Sketcher XAbstandFestlegen](Sketcher_ConstrainDistanceX/de#Fortsetzen-Modus.md)



### Einmal-Ausführen-Modus 

Siehe [Sketcher XAbstandFestlegen](Sketcher_ConstrainDistanceX/de#Einmal-Ausführen-Modus.md).



## Skripten

Abstand vom Ursprung:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Abstand zwischen zwei Endpunkten:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Die vertikale Länge der Linie (die GUI erlaubt die Auswahl der Kante, aber das ist nur eine Abkürzung für die Nutzung der beiden Endpunkte derselben Linie):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Die Seite [Skizzierer Skripten](Sketcher_scripting.md) erklärt die Werte, die für `Edge1`, `Edge2`, `Edge`, `PointOfEdge1`, `PointOfEdge2`, `PointOfEdge` und `Line` verwendet werden können, und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceY/de
