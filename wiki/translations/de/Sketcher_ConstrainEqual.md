---
 GuiCommand:
   Name: Sketcher ConstrainEqual
   Name/de: Sketcher GleichheitFestlegen 
   MenuLocation: Skizze , Sketcher-Randbedingungen , Gleichheit festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **E**
   SeeAlso: 
---

# Sketcher ConstrainEqual/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> [Sketcher GleichheitFestlegen](Sketcher_ConstrainEqual/de.md) legt fest, dass Linien (gerade Kanten) die gleiche Länge besitzen bzw. dass Kurven (Alle anderen Kanten außer [B-Splines](Sketcher_CreateBSpline/de.md)) die gleiche Krümmung aufweisen. Die Kanten müssen gleichartig sein. Kreise und Kreisbögen sind gleichartig (ihre Radien werden gleichgesetzt), ebenso Ellipsen und Ellipsenbögen (ihre Haupt- und Nebenradien werden jeweils gleichgesetz).



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_ConstrainEqual.svg" width=16px> [Gleichheit festlegen](Sketcher_ConstrainEqual/de.md)** drücken.

    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainEqual.svg" width=16px> Gleichheit festlegen** auswählen.

    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **Constrain → <img src="images/Sketcher_ConstrainEqual.svg" width=16px> Gleichheit festlegen** im Kontextmenü auswählen.

    -   Das Tastaturkürzel **E**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
    -   Zwei Kanten derselben Art auswählen.
4.  Eine Randbedingung wird hinzugefügt.
5.  Wahlweise weitere Randbedingungen erstellen.
6.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



### Einmal-Ausführen-Modus 

1.  Eine oder mehrere Kanten auswählen.
2.  Das Werkzeug wie oben beschrieben aufrufen oder mit der folgenden weiteren Möglichkeit:
    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_ConstrainEqual.svg" width=16px> Gleichheit festlegen** im Kontextmenü auswählen.
3.  Abhängig von der Auswahl werden eine oder mehrere Randbedingungen hinzugefügt.



## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

Die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) erklärt die Werte, die für `Edge1` und `Edge2` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/de
