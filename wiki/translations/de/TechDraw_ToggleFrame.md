---
- GuiCommand:/de
   Name:TechDraw ToggleFrame
   Name/de:TechDraw UmschaltenRahmen
   MenuLocation:TechDraw → Ansichtsrahmen ein-/ausschalten
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Ansicht](TechDraw_View/de.md), [TechDraw Projektionsgruppe](TechDraw_ProjectionGroup/de.md)
---

## Beschreibung

Das Werkzeug schaltet die Umrandungen in den Ansichten und Anmerkungen, sowie die Anzeige der Fangpunkte usw. ein oder aus.

<img alt="" src=images/TechDraw_ToggleFrame.png  style="width:400px;"> 
*links Umrandung eingeschaltet, rechts Umrandung ausgeschaltet*

## Anwendung

1.  Wenn du mehrere Zeichnungsseiten in deinem Dokument hast, musst du die gewünschte Seite im Baum auswählen.
2.  Drücke die **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Ansichtsrahmen ein-/ausschalten](TechDraw_ToggleFrame/de.md)** Schaltfläche.
3.  Wenn Ansichtsrahmen derzeit sichtbar sind, werden sie verschwinden. Wenn Ansichtsrahmen nicht sichtbar sind, werden sie angezeigt.
4.  Es ist möglich, dass sich verschiedene Ansichten in unterschiedlichen Zuständen der Rahmenanzeige befinden. Wenn dies passiert drücke die **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Ansichtsrahmen ein-/ausschalten](TechDraw_ToggleFrame/de.md)** Schaltfläche ein oder zweimal um die Ansichten neu zu synchronisieren.

## Hintergrund

Der gestrichelte Ansichtsrahmen und die Knotenpunkte dienen nur als Referenz, sie sind nicht wirklich Teil der Zeichnung, so dass du sie nicht mehr siehst, wenn du die Seite als PDF oder SVG exportierst.

Der vorgeschlagene Arbeitsablauf ist die Verwendung von **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Turn View Frames On/Off](TechDraw_ToggleFrame/de.md)** um den Rahmen, der die Ansicht umgibt, und auch die zusätzlichen Punkte zu deaktivieren. Mit den Punkten wähle mit den Messwerkzeugen die richtigen zu messenden Kanten aus und schalte dann den Rahmen (und die Punkte) aus, um das Endergebnis zu sehen. Nicht zufrieden? Schalte den Rahmen (und die Punkte) wieder ein, wähle andere Knotenpunkte aus und erstelle neue Messungen, dann schalte den Rahmen wieder aus.

Du kannst die Größe der Knotenpunkte im [TechDraw Einstellungen/Maßstabs Reiter](TechDraw_Preferences/de#Skalieren.md) einstellen. Bitte setze ihre Größe nicht auf Null, nur klein oder groß genug, damit du sie bequem aufnehmen kannst.

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Umschaltwerkzeug verfügt derzeit nicht über eine Programmierschnittstelle.





{{TechDraw Tools navi

}}  
