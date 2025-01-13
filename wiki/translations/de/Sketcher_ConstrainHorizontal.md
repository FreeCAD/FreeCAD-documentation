---
 GuiCommand:
   Name: Sketcher ConstrainHorizontal
   Name/de: Sketcher HorizontalFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Horizontal festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **H**
   SeeAlso: Sketcher_ConstrainHorVer/de, Sketcher_ConstrainVertical/de
---

# Sketcher ConstrainHorizontal/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> [Sketcher HorizontalFestlegen](Sketcher_ConstrainHorizontal/de.md) legt Linien oder Punktpaare horizontal fest (parallel zur horizontalen Achse der Skizze).


{{Version/de|1.0}}

: In den meisten Fällen ist es ratsam das kombinierte Werkzeug [Sketcher HorVerFestlegen](Sketcher_ConstrainHorVer/de.md) zu verwenden.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   
        {{Version/de|1.0}}
        
        : Ist die [Voreinstellung](Sketcher_Preferences/de#Allgemein.md) **Kombiniertes Werkzeug für automatisch horizontal bzw. vertikal festlegen** aktiviert (Standardeinstellung): Den Abwärtspfeil rechts neben der Schaltfläche **<img src="images/Sketcher_ConstrainHorVer.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** drücken und **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Horizontal festlegen** in der Ausklappliste auswählen.

#\* Ist die Voreinstellung nicht aktiviert (und in {{VersionMinus/de|0.21}}): Die Schaltfläche **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> [Horizontal festlegen](Sketcher_ConstrainHorizontal/de.md)** drücken.

#\* Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Horizontal festlegen** auswählen.

#\* Das Tastaturkürzel **H**.

1.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
2.  Eine der folgenden Möglichkeiten auswählen:
3.  Wahlweise eine der folgenden Möglichkeiten auswählen:
    -   Zwei Punkte auswählen.
    -   Eine einzelne Linien auswählen.
4.  Eine Randbedingung wird hinzugefügt.
5.  Wahlweise weitere Randbedingungen erstellen.
6.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



### Einmal-Ausführen-Modus 

1.  Eine der folgenden Möglichkeiten auswählen:
    -   Zwei oder mehr Punkte auswählen.
    -   Eine oder mehrere Linien auswählen. Punkte können in der Auswahl enthalten sein, werden aber ignoriert.
2.  Das Werkzeug aufrufen, wie oben beschrieben oder mit der folgenden zusätzlichen Option:
    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_ConstrainHorizontal.svg" width=16px> Horizontal festlegen** im Kontextmenü auswählen.
3.  Abhängig von der Auswahl werden eine oder mehrere Randbedingungen hinzugefügt.



## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

Die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) erklärt die Werte, die für `Line` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/de
