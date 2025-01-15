---
 GuiCommand:
   Name:  Sketcher ConstrainHorVer
   Name/de:  Sketcher HorVerFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Horizontal/Vertikal
   Workbenches: Sketcher_Workbench/de
   Shortcut: **A**
   Version: 1.0
   SeeAlso: Sketcher_ConstrainHorizontal/de, Sketcher_ConstrainVertical/de
---

# Sketcher ConstrainHorVer/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:24px;"> [Sketcher HorVerFestlegen](Sketcher_ConstrainHorVer/de.md) legt Linien oder Punktpaare horizontal (parallel zur horizontalen Achse der Skizze) oder vertikal fest, was auch immer dichter an der aktuellen Ausrichtung liegt.

Dieses Werkzeug kombiniert die Werkzeuge [Sketcher HorizontalFestlegen](Sketcher_ConstrainHorizontal/de.md) und [Sketcher VertikalFestlegen](Sketcher_ConstrainVertical/de.md).



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Ist die [Voreinstellung](Sketcher_Preferences/de#Allgemein.md) **Automatisches Werkzeug für HorizontalFestlegen oder. VertikalFestlegen** aktiviert (Standardeinstellung): Die Schaltfläche **<img src="images/Sketcher_ConstrainHorVer.svg" width=16px> [Horizontal / vertikal festlegen](Sketcher_ConstrainHorVer/de.md)** button.
    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainHorVer.svg" width=16px> Horizontal / vertikal festlegen** auswählen.
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **Festlegen → <img src="images/Sketcher_ConstrainHorVer.svg" width=16px> Horizontal / vertikal festlegen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **A**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Eine der folgenden Möglichkeiten auswählen:
    -   Zwei Punkte auswählen.
    -   Eine einzelne Linie auswählen.
5.  Eine Randbedingung wird hinzugefügt.
6.  Wahlweise weitere Randbedingungen erstellen.
7.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



### Einmal-Ausführen-Modus 

1.  Eine der folgenden Möglichkeiten auswählen:
    -   Zwei oder mehr Punkte auswählen (die Auswahlreihenfolge kann von Bedeutung sein, siehe [Hinweise](#Hinweise.md)).
    -   Eine oder mehrere Linien auswählen. Punkte können in der Auswahl enthalten sein, werden aber ignoriert.
2.  Das Werkzeug aufrufen, wie oben beschrieben oder mit der folgenden zusätzlichen Möglichkeit:
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view.md) und die Menüoption **<img src="images/Sketcher_ConstrainHorVer.svg" width=16px> Horizontal / vertikal festlegen** im Kontextmenü auswählen.
3.  Abhängig von der Auswahl werden eine oder mehrere Randbedingungen hinzugefügt.



## Hinweise

-   Mehr als 2 Punkte werden in der Auswahlreihenfolge bearbeitet, jeweils ein Paar zur Zeit. Der erste Punkt wird dem zweiten zugeordnet. Wenn eine Randbedingung zwischen ihnen festgelegt wird, kann sich der zweite Punkt bewegen. Die neue Lage des zweiten Punktes bestimmt, welche Randbedingung zwischen dem zweiten und dem dritten Punkt festgelegt wird usw.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorVer/de
