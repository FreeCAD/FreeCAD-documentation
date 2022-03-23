---
- GuiCommand:/de
   Name:Sketcher ConstrainDistanceY
   Name/de:Skizzierer BeschränkeAbstandY
   MenuLocation:Skizze → Skkizzierer Beschränkungen → Beschränke Vertikaler Abstand
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Shortcut:**Umschalten** + **V**
   SeeAlso:[Skizzierer Beschränke Horizontaler Abstand](Sketcher_ConstrainDistanceX/de.md), [Skizzierer Beschränke Länge](Sketcher_ConstrainDistance/de.md)
---

# Sketcher ConstrainDistanceY/de


</div>

## Beschreibung

Fixiert den vertikalen Abstand zwischen zwei Punkten oder Linienenden. Falls nur ein Objekt ausgewählt ist, wird der (vertikale) Abstand zum Ursprung (0,0) festgelegt.

![](images/Sketcher_ConstraintDistanceY_example.png )

## Anwendung


<div class="mw-translate-fuzzy">

1.  Greife einen oder zwei Punkte oder eine Linie.
2.  Rufe das Werkzeug auf mehrere Arten auf:
    -   Drücke die **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Beschränke Vertikalen Abstand](Sketcher_ConstrainDistanceY/de.md)** Schaltfläche in der Werkzeugleiste.
    -   Verwende die **Shift** + **V** Tastaturkürzel. (**V**\' steht für **V**ertikal)
    -   Verwende den **Skizze → Skizziererbeschränkungen →  [<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> Beschränke Vertikalen Abstand** Eintrag aus dem oberen Menü.
3.  Ein Aufklappdialogfeld wird geöffnet, um den Wert zu bearbeiten oder zu bestätigen. Drücke **OK**, um den Wert zu bestätigen.


</div>

**Hinweis**: Das Beschränkungswerkzeug kann auch ohne vorherige Auswahl gestartet werden, erfordert aber die Auswahl von zwei Punkten oder einer Linie. Um den Abstand zum Ursprung zu setzen, muss der Ursprungspunkt der Zeichnung ebenfalls selektiert werden. Als Voreinstellung ist der Befehl im \"Continue Mode\", um neue Beschränkungen zu erstellen; drücke die rechte Maustaste oder **Esc** einmal zum Beenden des Befehls.

## Skripten

Abstand vom Ursprung:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge, PointOfEdge, App.Units.Quantity('123.0 mm')))```

Abstand zwischen zwei Endpunkten:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Vertikaler Abstand der Linie (die GUI erlaubt die Auswahl der Kante, aber das ist nur eine Abkürzung für die Nutzung der beiden Endpunkte der gleichen Linie):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Die [Skizzierer Skripten](Sketcher_scripting.md)-Seite erklärt die Werte, die für `Edge1`, `Edge2`, `Edge`, `PointOfEdge1`, `PointOfEdge2`, `PointOfEdge` und `Line` verwendet werden können, und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceY/de
