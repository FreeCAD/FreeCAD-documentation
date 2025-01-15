---
 GuiCommand:
   Name: BIM Library
   Name/de: BIM Bibliothek
   MenuLocation: 3D/BIM , Generische 3D-Werkzeuge , Objektbibliothek
   Workbenches: BIM_Workbench/de
---

# BIM Library/de



## Beschreibung

Das Werkzeug **BIM Bibliothek** ermöglicht im aktuellen Modell ein Objekt aus der [FreeCAD-Bauteilbibliothek](Parts_Library_Workbench/de.md) einzusetzen, die über den <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden muss, damit dieses Werkzeug verfügbar ist.

<img alt="" src=images/BIM_Library_screenshot.png  style="width:600px;"> 
*Oben: Der Dialog ''Library browser''' in der [Aufgaben-Tafel](Task_panel/de.md) auf der linken Seite.*



## Anwendung

1.  Die Schaltfläche **<img src="images/BIM_Library.svg" width=16px> [Objektbibliothek](BIM_Library/de.md)** drücken.

    :   Ergebnis: In der [Combo Ansicht](Combo_view/de.md) → [Aufgaben-Fenster](Task_panel/de.md) wird ein Dialog mit dem Titel **Bibliotheken-Browser** angezeigt.
2.  Im Bibliotheken-Browser eine Datei anklicken.
3.  Diese doppelt anklicken oder die Schaltfläche **Einfügen** drücken.
4.  Einen Punkt in der [3D-Ansicht](3D_view/de.md) anklicken oder eine Koordinate manuell eingeben, um das Objekt zu positionieren



## Optionen

-   Es werden [FCStd-](File_Format_FCStd/de.md), STEP- und [BREP](File_Format_FCStd/de#*.brep.md)-Dateien unterstützt. Nur STEP- und BREP-Dateien sind postionierbar. Bei FCStd-Dateien kann keine Positionierung gewählt werden, da sie aus einer komplexen Reihe von Objekten mit signifikanten Positionen bestehen können. Wird eine FCStd-Datei ausgewählt, wird ihr Inhalt an der Position eingefügt, die in der Datei definiert ist.
-   STEP- und BREP-Objekte werden als <img alt="" src=images/Arch_Equipment.svg  style="width:24px;"> [Ausstattung](Arch_Equipment/de.md) ohne separate Basisform eingefügt. Das nachträgliche Hinzufügen einer Basisform zu diesen Objekten zerstört deren aktuelle Form.
-   Beim Positionieren eines Objekts kann dessen Einfügepunkt zwischen Original (dem in der Datei definierten Punkt (`0,0,0`)), oben, Mitte, unten und links, Mitte und rechts wählen.
-   Die Bibliothek kann offline arbeiten, in diesem Fall ist sie darauf angewiesen, dass das Addon Parts Library installiert (und vom Benutzer aktualisiert) wird, oder online, in diesem Fall browst sie direkt aus dem [Parts-Library-Git-Repository](https://github.com/FreeCAD/FreeCAD-library) und ermöglicht das direkte Herunterladen von dort.



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Library/de
