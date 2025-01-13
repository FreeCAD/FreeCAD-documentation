---
 GuiCommand:
   Name: Sketcher ConstrainLock
   Name/de: Sketcher Sperren
   MenuLocation: Skizze , Sketcher-Randbedingungen , Sperren
   Workbenches: Sketcher_Workbench/de
   Shortcut: **K** **L**
   SeeAlso: Sketcher_ConstrainBlock/de
---

# Sketcher ConstrainLock/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Sperren](Sketcher_ConstrainLock/de.md) ordnet Punkten die Randbedingungen [Horizontalen Abstand festlegen](Sketcher_ConstrainDistanceX/de.md) und [Vertikalen Abstand festlegen](Sketcher_ConstrainDistanceY/de.md) zu. Ist ein einzelner punkt ausgewählt, beziehen sich die Randbedingungen auf den Ursprung der Skizze. Sind zwei oder mehr Punkte ausgewählt, beziehen sich die Randbedingungen auf den letzten Punkt in der Auswahl.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   
        {{Version/de|1.0}}
        
        : Ist die [Voreinstellung](Sketcher_Preferences/de#Allgemein.md) **Werkzeuge für Maßeinträge** auf {{Value|Einzelnes Werkzeug}} gesetzt (Standardeinstellung): Den Abwärtspfeil rechts neben der Schaltfläche **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** drücken und **<img src="images/Sketcher_ConstrainLock.svg" width=16px> Sperren** in der Ausklappliste auswählen.

    -   Ist die Voreinstellung auf einen anderen Wert gesetzt (und in {{VersionMinus/de|0.21}}): Die Schaltfläche **<img src="images/Sketcher_ConstrainLock.svg" width=16px> [Sperren](Sketcher_ConstrainLock/de.md)** drücken.

    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Sperren** auswählen.

    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view.md) und die Menüoption **Abmessung → <img src="images/Sketcher_ConstrainLock.svg" width=16px> Sperren** im Kontextmenü auswählen.

    -   Das Tastaturkürzel **K** dann **L**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Einen einzelnen Punkt auswählen.
5.  Zwei Randbedingungen werden hinzugefügt.
6.  Wahlweise weitere Randbedingungen erstellen.
7.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



### Einmal-Ausführen-Modus 

1.  Einen oder mehrere Punkte auswählen.
2.  Das Werkzeug aufrufen, wie oben beschrieben.
3.  Abhängig von der Auswahl werden zwei oder mehr Randbedingungen hinzugefügt.



## Hinweise

-   Es gibt keine automatisch Eingabeaufforderung zum Bearbeiten der zur Randbedingung gehörenden Werte. Falls erforderlich, können die Werte [manuell bearbeitet](Sketcher_Workbench/de#Randbedingungen_bearbeiten.md) werden.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/de
