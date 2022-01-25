# Task panel/de
{{TOCright}}

## Einführung

Das [Aufgabenpaneel](Task_panel/de.md) erscheint im **Aufgaben** Reiter der [Combo Ansicht](combo_view/de.md), eines der wichtigen Paneele der [Oberfläche](interface/de.md). Es ist ein anpassbaren Bereich, der jede Art von grafischer Widgets, wie z.B. ausklappbare Unterfenster, Tabellen, Eingabefelder, Kontrollkästchen, Drehfelder, Auswahlfelder, Textfelder, Schaltflächen, Beschriftungen, Bilder und andere Elemente enthalten kann, abhängig vom gerade aktiven [Arbeitsbereich](Workbenches/de.md) und dem gerade aktiven Werkzeug.

<img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width:" height="550px;">



*Der Aufgabenreiter, der verschiedene Befehle anzeigt, wenn der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) aktiv ist und eine [Skizze](sketch/de.md) ausgewählt ist.*

## Arbeiten mit dem Aufgabenbereich 

Ein Aufgabenbereich öffnet sich normalerweise, wenn ein Werkzeug aktiviert wird, das eine Benutzereingabe erfordert, entweder durch Drücken einer Schaltfläche in der Werkzeugleiste oder durch Doppelklicken auf ein Objekt. Wenn das Werkzeug keine Benutzereingabe erfordert, erzeugt es sein Ergebnis oder wird beendet, zeigt aber keinen Aufgabenbereich an.

Bei den Benutzereingaben kann es sich um Text, 3D Punktkoordinaten, Elemente aus einer Liste, Flächen aus einer Form oder Optionen zur Änderung der Funktionsweise des Werkzeugs handeln.

![](images/FreeCAD_Combo_view_Task_panel_Sketcher.png )



*Aufgabenbereich, der geöffnet wird, wenn eine [Skizze](Sketch/de.md) bearbeitet wird. Es werden verschiedene Arten von Informationen angezeigt, z. B. Lösermeldungen, Gitteroptionen, Beschränkungen und geometrische Elemente.*

Es gibt viele Befehle, die die Auswahl von vorhandenen Formen oder Objekten aus dem Dokument erfordern. In solchen Fällen wartet der Aufgabenbereich darauf, dass der Benutzer die entsprechenden Objekte aus der [Baumansicht](tree_view/de.md) oder der [3D Ansicht](3D_view/de.md) auswählt. Wenn der Aufgabenbereich geöffnet ist, ist es möglich, zum Reiter **Modell** zu wechseln, um die [Baumansicht](Tree_view/de.md) anzuzeigen und ein Objekt auszuwählen. Sobald dies geschehen ist, kann man zum Reiter **Aufgaben** zurückwechseln, um mit dem Befehl fortzufahren. Der Aufgabenbereich wird in der Regel durch Klicken auf die Schaltfläche **OK** oder die Schaltfläche **Schließen** Schaltfläche oder durch Drücken der **Esc**-Taste auf der Tastatur geschlossen, um den Befehl abzubrechen.

![](images/FreeCAD_Combo_view_Task_panel_ArchComponent.png )



*Aufgabenbereich, der beim Bearbeiten einer [Arch Komponente](Arch_Component/de.md) geöffnet wird. Der Aufgabenbereich wartet darauf, dass der Benutzer Objekte auswählt, die der Komponente hinzugefügt oder von ihr subtrahiert werden können.*

**Hinweis:** Bitte beachte, dass der Wechsel vom **Aufgaben** Reiter zum **Modell** Reiter den aktiven Befehl nicht beendet; die Aufgabe läuft weiterhin im Hintergrund. Der Benutzer ist dafür verantwortlich, den aktiven Befehl ordnungsgemäß zu beenden oder abzubrechen, bevor er eine andere Aufgabe startet; eine laufende Aufgabe zu verlassen, kann beim Versuch, andere Werkzeuge zu starten, zu Fehlern führen.

## Hinweise

-   Benutzer, die von anderen CAD Lösungen umsteigen, die die **ESC** Taste als Teil ihres Arbeitsablaufs verwenden, können in FreeCAD andere Ergebnisse erhalten. Wenn die **ESC** Taste in FreeCAD gedrückt wird und der Aufgabenbereich im Fokus ist, wird der Aufgabenbereich automatisch verlassen. Um diese Funktion zu deaktivieren, siehe [Fine-tuning/de\#ESC Taste](Fine-tuning/de#ESC_Taste.md).

## Skripten


**Bitte diesen Abschnitt neuformulieren und aktualisieren.**

Siehe [Forumsbeitrag](https://forum.freecadweb.org/viewtopic.php?f=10&t=44170&p=376759#p376759) Aufruf, den ein Aufgaben Dialog Widget verwenden kann, um die Aufgabenansicht zu schließen. Es kann mit \"this-\>close()\" geschlossen werden, aber das schließt nur den unteren Teil der Ansicht, nicht die Ansicht selbst.

Verwendung von Python: 
```python
Gui.Control.closeDialog()
```

Verwendung von C++: 
```python
Gui::Control().closeDialog();
```


{{Interface navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Task panel/de
