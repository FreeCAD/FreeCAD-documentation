---
 GuiCommand:
   Name: Sketcher ConstrainBlock
   Name/de: Sketcher Fixieren
   MenuLocation: Skizze , Sketcher-Randbedingungen , Fixieren
   Workbenches: Sketcher_Workbench/de
   Shortcut: **K** **B**
   Version: 0.17
   SeeAlso: Sketcher_ConstrainLock/de
---

# Sketcher ConstrainBlock/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:24px;"> [Sketcher Fixieren](Sketcher_ConstrainBlock/de.md) setzt Kanten an Ort und Stelle mit einer einzigen Randbedingung fest. Es ist hauptsächlich für [B-Splines](Sketcher_CreateBSpline/de.md) gedacht, die sonst nur schwer vollständig bestimmt werden können.

Die Randbedingung Fixieren betrifft zurzeit nur die frei beweglichen Teile einer Kante. Fixierten Kanten können andere Randbedingungen hinzugefügt werden, und das Hinzufügen von weiteren Randbedingungen zu fixierten Kanten, kann diese verändern.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_ConstrainBlock.svg" width=16px> [Fixieren](Sketcher_ConstrainBlock/de.md)** drücken.

    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainBlock.svg" width=16px> Fixieren** auswählen.

    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **Festlegen → <img src="images/Sketcher_ConstrainBlock.svg" width=16px> Fixieren** im Kontextmenü auswählen.

    -   Das Tastaturkürzel **K** dann **B**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Eine einzelne Kante auswählen.
5.  Eine Randbedingung wird hinzugefügt.
6.  Wahlweise weitere Randbedingungen erstellen.
7.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



### Einmal-Ausführen-Modus 

1.  Eine oder mehrere Kanten auswählen.
2.  Das Werkzeug wie oben beschrieben aufrufen oder mit der folgenden weiteren Möglichkeit:
    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_ConstrainBlock.svg" width=16px> Fixieren** im Kontextmenü auswählen.
3.  Abhängig von der Auswahl werden eine oder mehrere Randbedingungen hinzugefügt.



## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

Die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) erklärt die Werte, die für `Edge` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/de
