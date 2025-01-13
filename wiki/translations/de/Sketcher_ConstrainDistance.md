---
 GuiCommand:
   Name: Sketcher ConstrainDistance
   Name/de: Sketcher AbstandFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Abstand festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **K** **D**
   SeeAlso: Sketcher_ConstrainDistanceX/de, Sketcher_ConstrainDistanceY/de
---

# Sketcher ConstrainDistance/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> [Abstand festlegen](Sketcher_ConstrainDistance/de.md): Legt die Länge einer Linie, den Abstand zwischen zwei Punkten, den senkrechten Abstand eines Punktes zu einer Linie fest; oder {{Version/de|0.21}} den Abstand zwischen den Kanten zweier Kreise oder Kreisbögen oder zwischen der Kante eines Kreises oder Kreisbogens und einer Linie; oder {{Version/de|1.0}} die Länge eines Kreisbogens.

![](images/Sketcher_ConstrainDistance_example.png )



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass nichts ausgewählt ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   
        {{Version/de|1.0}}
        
        : Ist die [Voreinstellung](Sketcher_Preferences/de#Allgemein.md) **Werkzeuge für Maßeinträge** auf {{Value|Einzelnes Werkzeug}} (Standardeinstellung) gesetz: Den Abwärtspfeil rechts neben der Schaltfläche **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** drücken und im Ausklappmenü **<img src="images/Sketcher_ConstrainDistance.svg" width=16px> Abstand festlegen** auswählen.

    -   Hat die Voreinstellung einen anderen Wert (und in {{VersionMinus/de|0.21}}): Die Schaltfläche **<img src="images/Sketcher_ConstrainDistance.svg" width=16px> [Abstand festlegen](Sketcher_ConstrainDistance/de.md)** drücken.

    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainDistance.svg" width=16px> Abstand festlegen** auswählen.

    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **Bemaßung → <img src="images/Sketcher_ConstrainDistance.svg" width=16px> Abstand festlegen** im Kontextmenü auswählen.

    -   Das Tastaturkürzel **I**.
3.  Für weitere Schritte siehe [Sketcher XAbstandFestlegen](Sketcher_ConstrainDistanceX/de#Fortsetzen-Modus.md).



### Einmal-Ausführen-Modus 

1.  Eine der folgenden Möglichkeiten auswählen:
    -   Eine einzelne Linie auswählen.

    -   Zwei Punkte auswählen.

    -   Einen Punkt und eine Linie auswählen (in beliebiger Reihenfolge).

    -   Die Kanten zweier Kreise oder Kreisbögen auswählen.

    -   Eine Kante eines Kreises oder Kreisbogens und eine Linie auswählen (in beliebiger Reihenfolge).

    -   
        {{Version/de|1.0}}
        
        : Die Kante eines einzelnen Kreisbogens auswählen.
2.  Das Werkzeug aufrufen, wie oben beschrieben.
3.  Wahlweise den [Wert der Randbedingung](Sketcher_Workbench/de#Randbedingungen_bearbeiten.md) bearbeiten.
4.  Eine Randbedingung wird hinzugefügt.



## Hinweise

-   Wenn es passt, sollte die Verwendung der Randbedingungen [XAbstandFestlegen](Sketcher_ConstrainDistanceX/de.md) oder [YAbstandFestlegen](Sketcher_ConstrainDistanceY/de.md) erwägt werden; sie sind effizienter.



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

Die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) erklärt die Werte, die für `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, `PointOfEdge1`, `PointOfEdge2`, `Line`, `Circle1` und `Circle2` verwendet werden können, und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistance/de
