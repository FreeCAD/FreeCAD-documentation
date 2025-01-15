---
 GuiCommand:
   Name: Sketcher ConstrainRadiam
   Name/de: Sketcher RadiamFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Automatisch Radius/Durchmesser festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **K** **S**
   Version: 0.20
   SeeAlso: Sketcher_ConstrainRadius/de, Sketcher_ConstrainDiameter/de
---

# Sketcher ConstrainRadiam/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:24px;"> [Sketcher RadiamFestlegen](Sketcher_ConstrainRadiam/de.md) legt den Radius von Bögen und [B-Spline-Gewichtskreisen](Sketcher_CreateBSpline/de#Hinweise.md) sowie den Durchmesser von Kreisen fest.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   
        {{Version/de|1.0}}
        
        : Ist die [Voreinstellung](Sketcher_Preferences/de#Allgemein.md) **Werkzeuge für Maßeinträge** auf {{Value|Einzelnes Werkzeug}} gesetzt (Standardeinstellung): Den Abwärtspfeil rechts neben der Schaltfläche **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** drücken und die Menüoption **<img src="images/Sketcher_ConstrainRadiam.svg" width=16px> Automatisch Radius oder Durchmesser festlegen** im Ausklappmenü auswählen.

    -   Besitzt die Voreinstellung einen anderen Wert (und in {{VersionMinus/de|0.21}}): Die Schaltfläche **<img src="images/Sketcher_ConstrainRadiam.svg" width=16px> [Automatisch Radius oder Durchmesser festlegen](Sketcher_ConstrainRadiam/de.md)** drücken.

    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainRadiam.svg" width=16px> Automatisch Radius oder Durchmesser festlegen** auswählen.

    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **Abmessung → <img src="images/Sketcher_ConstrainRadiam.svg" width=16px> Automatisch Radius oder Durchmesser festlegen** im Kontextmenü auswählen.

    -   Das Tastaturkürzel **K** dann **S**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Eine der folgenden Möglichkeiten auswählen:
    -   Die Kante eines Kreises oder Kreisbogens auswählen.
    -   Die Kante eines B-Spline-Gewichtskreises auswählen.
5.  Wird eine [festlegende maßliche Randbedingung](Sketcher_ToggleDrivingConstraint/de.md) erstellt, hängt von den [Voreinstellungen](Sketcher_Preferences/de#Anzeige.md) ab, ob ein Dialog geöffnet wird, um ihren [Wert zu bearbeiten](Sketcher_Workbench/de#Randbedingungen_bearbeiten.md).
6.  Eine Randbedingung wird hinzugefügt.
7.  Wahlweise weitere Randbedingungen erstellen.
8.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



### Einmal-Ausführen-Modus 

1.  Eine der folgenden Möglichkeiten auswählen:
    -   Die Kante(n) eines oder mehrerer Kreise oder Kreisbögen auswählen.
    -   Die Kante(n) eines oder mehrerer B-Spline-Gewichtskreise auswählen.
2.  Das Werkzeug aufrufen, wie oben beschrieben.
3.  Wahlweise den [Wert der Randbedingung](Sketcher_Workbench/de#Randbedingungen_bearbeiten.md) bearbeiten.
4.  Abhängig von der Auswahl werden eine oder mehrere Randbedingungen hinzugefügt, siehe [Hinweise](#Hinweise.md).



## Hinweise

-   Werden [festlegende maßliche Randbedingungen](Sketcher_ToggleDrivingConstraint/de.md) erstellt und wurden mehrere Elemente vorausgewählt, die keine [externen Geometrien](Sketcher_External/de.md) sind, erhält nur das erste von ihnen eine maßliche Randbedingung, während Zwischen dem ersten und den anderen die Randbedingung [Gleichheit festlegen](Sketcher_ConstrainEqual/de.md) eingesetzt wird.



## Skripten


```python
Sketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))
Sketch.addConstraint(Sketcher.Constraint('Diameter', ArcOrCircle, App.Units.Quantity('246.0 mm')))
```

Die Seite [Sketcher Skripten](Sketcher_scripting.md) erklärt die Werte, die für `ArcOrCircle` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadiam/de
