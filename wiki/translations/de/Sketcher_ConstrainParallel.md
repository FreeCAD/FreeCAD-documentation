---
 GuiCommand:
   Name: Sketcher ConstrainParallel
   Name/de: Sketcher ParallelFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Parallel festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **P**
   SeeAlso: 
---

# Sketcher ConstrainParallel/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> [Sketcher ParallelFestlegen](Sketcher_ConstrainParallel/de.md) legt Linien parallel zueinander fest.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_ConstrainParallel.svg" width=16px> [Parallel festlegen](Sketcher_ConstrainParallel/de.md)** drücken.

    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainParallel.svg" width=16px> Parallel festlegen** auswählen.

    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **Festlegen → <img src="images/Sketcher_ConstrainParallel.svg" width=16px> Parallel festlegen** im Kontextmenü auswählen.

    -   Das Tastaturkürzel **P**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Zwei Kanten auswählen.
5.  Eine Randbedingung wird hinzugefügt.
6.  Wahlweise weitere Randbedingungen erstellen.
7.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



### Einmal-Ausführen-Modus 

1.  Zwei oder mehr Linien auswählen. {{Version/de|1.0}}: Punkte können in der Auswahl enthalten sein, werden aber ignoriert.
2.  Das Werkzeug aufrufen, wie oben beschrieben oder mit der folgenden zusätzlichen Option:
    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_ConstrainParallel.svg" width=16px> Parallel festlegen** im Kontextmenü auswählen.
3.  Abhängig von der Auswahl werden eine oder mehrere Randbedingungen hinzugefügt.



## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

Die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) erklärt die Werte, die für `Line1` und `Line2` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainParallel/de
