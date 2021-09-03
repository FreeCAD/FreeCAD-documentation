---
- GuiCommand:/de
   Name:Sketcher ConstrainDistance
   Name/de:Skizzierer BeschränkeAbstand
   MenuLocation:Skizze → Skizzen Beschränkungen → Abstand Beschränken
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Shortcut:**Umschalten** + **D**
   SeeAlso:[Horizontalen Abstand beschränken](Sketcher_ConstrainDistanceX/de.md), [Vertikalen Abstand beschränken](Sketcher_ConstrainDistanceY/de.md)
---

## Beschreibung

Die **Beschränke Abstand** beschränkt die Länge einer Linie, den senkrechten Abstand zwischen einem Punkt und einer Linie oder den Abstand zwischen zwei Punkten auf einen bestimmten Wert.

![](images/Sketcher_ConstrainDistance_example.png )

## Anwendung

1.  Wähle zwei Punkte oder eine Linie oder einen Punkt und eine Linie.
2.  Aufrufen des Befehls auf verschiedene Weise:
    -   Drücke die **<img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> [Abstand beschränken](Sketcher_ConstrainDistance/de.md)** Schaltfläche in der Skizzierer Werkzeugleiste.
    -   Verwende die **Shift** + **D** Tastaturkürzel. (**D**\' steht für **D**istance; engl.: Abstand)
    -   Verwende den **Skizze → Skizziererbeschränkungen  → <img src=images/Sketcher_ConstrainDistance.svg style="width:16px"> Abstand beschränken** Eintrag aus dem oberen Menü.
3.  Ein Einblenddialogfeld wird geöffnet, um den Wert zu bearbeiten oder zu bestätigen. Drücken **OK**, um den Wert zu bestätigen.

**Hinweis**: Das Beschränkungswerkzeug kann auch ohne vorherige Auswahl gestartet werden. Um den lotrechten Abstand zwischen einem Punkt und einer Linie zu setzen, muss der Punkt zuerst selektiert werden. Als Voreinstellung ist der Befehl im \"Continue Mode\", um neue Beschränkungen zu erstellen; drücke die rechte Maustaste oder **Esc** einmal zum Beenden des Befehls.

### Fingerzeig

Falls anwendbar, erwäge bitte die Verwendung der **<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> <img src=images/Sketcher_ConstrainDistanceY.svg style="width:Horizontaler Abstand](Sketcher_ConstrainDistanceX/de.md)** oder **[16px"> [Vertikaler Abstand](Sketcher_ConstrainDistanceY/de.md)** Beschränkungen stattdessen. Diese Beschränkungen sind robuster und schneller zu berechnen als das **BeschränkungAbstand** Werkzeug.

## Skripten

Abstand vom Ursprung:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, App.Units.Quantity('123.0 mm')))```

Abstand zwischen zwei Endpunkten:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Length of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line: 
```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Distanz von Punkt (`Edge, PointOfEdge`) zum nächsten Punk auf Linie (`Line`): 
```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, Line, App.Units.Quantity('123.0 mm')))```

Die [Skizzierer Skripten](Sketcher_scripting.md)-Seite erklärt die Werte, die für `Edge1`, `Edge2`, `Edge`, `PointOfEdge1`, `PointOfEdge2`, `PointOfEdge` und `Line` verwendet werden können, und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.





{{Sketcher Tools navi

}}  
