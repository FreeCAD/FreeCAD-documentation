---
- GuiCommand:
   Name: TechDraw ToggleFrame
   Name/de: TechDraw RahmenUmschalten
   MenuLocation: TechDraw  - TechDraw Ansichten - Ansichtsrahmen ein- oder ausschalten
   Workbenches: [TechDraw](TechDraw_Workbench/de.md)
   SeeAlso: [TechDraw Ansicht](TechDraw_View/de.md), [TechDraw Ansichtengruppe](TechDraw_ProjectionGroup/de.md)
---

# TechDraw ToggleFrame/de



## Beschreibung

Das Werkzeug **TechDraw RahmenUmschalten** schaltet die Darstellung der Umrandungen von Ansichten und Beschriftungen sowie die Anzeige von Knotenpunkten ein bzw. aus.

<img alt="" src=images/TechDraw_ToggleFrame.png  style="width:400px;"> 
*links Umrandung eingeschaltet, rechts Umrandung ausgeschaltet*



## Anwendung

1.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswahl in der [Baumansicht](Tree_view/de.md) aktivieren.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Ansichtsrahmen ein- oder ausschalten](TechDraw_ToggleFrame/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → TechDraw Ansichten → <img src="images/TechDraw_ToggleFrame.svg" width=16px> Ansichtsrahmen ein- oder ausschalten** auswählen.
    -   Wenn ein Zeichnungsblatt im [Hauptansichtsbereich](Main_view_area/de.md) angezeigt wird: Mit der rechten Maustaste in das Fenster des Blattes klicken und im Kontextmenü die Option **Toggle Frames** auswählen.
3.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und noch kein Blatt aktiviert wurde, wird das Dialogfeld **Blattauswahl** geöffnet: {{Version/de|0.20}}
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.
4.  Die aktuell sichtbaren Rahmen der Ansichten werden ausgeblendet bzw. aktuell unsichtbare Rahmen werden wieder dargestellt.
5.  Es kann vorkommen, dass sich Ansichten in unterschiedlichen Darstellungszuständen befinden. In diesem Falle kann ein- oder zweimaliges Aufrufen dieses Werkzeugs die Ansichten wieder synchronisieren.



## Hintergrund

Der gestrichelte Ansichtsrahmen und die Knotenpunkte dienen nur als Referenz, sie sind nicht wirklich Teil der Zeichnung, so dass du sie nicht mehr siehst, wenn du die Seite als PDF oder SVG exportierst.

Der vorgeschlagene Arbeitsablauf ist die Verwendung von **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Ansichtsrahmen ein- oder ausschalten](TechDraw_ToggleFrame/de.md)**, um den Rahmen, der die Ansicht umgibt, und auch die zusätzlichen Punkte zu deaktivieren. Mit den Punkten wähle mit den Messwerkzeugen die richtigen zu messenden Kanten aus und schalte dann den Rahmen (und die Punkte) aus, um das Endergebnis zu sehen. Nicht zufrieden? Schalte den Rahmen (und die Punkte) wieder ein, wähle andere Knotenpunkte aus und erstelle neue Messungen, dann schalte den Rahmen wieder aus.

Du kannst die Größe der Knotenpunkte im [TechDraw Einstellungen/Maßstabs Reiter](TechDraw_Preferences/de#Skalieren.md) einstellen. Bitte setze ihre Größe nicht auf Null, nur klein oder groß genug, damit du sie bequem aufnehmen kannst.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Umschaltwerkzeug verfügt derzeit nicht über eine Programmierschnittstelle.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ToggleFrame/de
