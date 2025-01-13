---
 GuiCommand:
   Name: Sketcher ConstrainDistanceX
   Name/de: Sketcher XAbstandFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Horizontalen Abstand festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **L**
   SeeAlso: Sketcher_ConstrainDistanceY/de, Sketcher_ConstrainDistance/de
---

# Sketcher ConstrainDistanceX/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [XAbstandFestlegen](Sketcher_ConstrainDistanceX/de.md): Legt den horizontalen Abstand zwischen zwei Punkten oder den Endpunkten einer Linie fest. Ist ein einzelner Punkt vorausgewählt, bezieht sich der Abstand auf den Ursprung der Skizze.

![](images/Constraint_H_Distance.png )



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass nichts ausgewählt ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   
        {{Version/de|1.0}}
        
        : Ist die [Voreinstellung](Sketcher_Preferences/de#Allgemein.md) **Werkzeuge für Maßeinträge** auf {{Value|Einzelnes Werkzeug}} (Standardeinstellung) gesetz: Den Abwärtspfeil rechts neben der Schaltfläche **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** drücken und im Ausklappmenü **<img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Horizontalen Abstand festlegen** auswählen.

    -   Hat die Voreinstellung einen anderen Wert (und in {{VersionMinus/de|0.21}}): Die Schaltfläche **<img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> [Horizontalen Abstand festlegen](Sketcher_ConstrainDistanceX/de.md)** drücken.

    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Horizontalen Abstand festlegen** auswählen.

    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **Bemaßung → <img src="images/Sketcher_ConstrainDistanceX.svg" width=16px> Horizontalen Abstand festlegen** im Kontextmenü auswählen.

    -   Das Tastaturkürzel **L**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Eine der folgenden Möglichkeiten auswählen:
    -   Zwei Punkte auswählen (einer von beiden kann der Ursprung sein).
    -   Eine einzelne Linie auswählen.
5.  Wurde eine [festlegende maßliche Randbedingung](Sketcher_ToggleDrivingConstraint/de.md) erstellt, wird abhängig von den [Voreinstellungen](Sketcher_Preferences/de#Anzeige.md) ein Dialog zum [Bearbeiten seines Wertes](Sketcher_Workbench/de#Randbedingungen_bearbeiten.md) geöffnet.
6.  Eine Randbedingung wird hinzugefügt.
7.  Wahlweise weitere Randbedingungen erstellen.
8.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



### Einmal-Ausführen-Modus 

1.  Eine der folgenden Möglichkeiten auswählen:
    -   Ein oder zwei Punkte auswählen.
    -   Eine einzelne Linie auswählen.
2.  Das Werkzeug aufrufen, wie oben beschrieben.
3.  Wahlweise den [Wert der Randbedingung](Sketcher_Workbench/de#Randbedingungen_bearbeiten.md) bearbeiten.
4.  Eine Randbedingung wird hinzugefügt.



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
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceX/de
