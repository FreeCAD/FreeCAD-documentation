---
- GuiCommand:Addon/de
   Name: BIM Library
   Name/de: BIM Bibliothek
   MenuLocation: 3D Modellierung - Bibliothek
   Workbenches: <img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench/de.md)
   Addon: BIM
   SeeAlso: [Arch Ausrüstung](Arch_Equipment/de.md)
---

# BIM Library/de

## Beschreibung

Mit dem Werkzeug BIM-Bibliothek kann man im aktuellen Modell ein Objekt aus der [FreeCAD-Bauteilbibliothek](Parts_Library/de.md) platzieren, die über den <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden muss, damit dieses Werkzeug verfügbar ist.

<img alt="" src=images/BIM_Library_screenshot.png  style="width:800px;"> 
*Oben: Siehe das '''Bibliotheksbrowser''' Dialogfeld im [Aufgabenpaneel](Task_panel/de.md) auf der linken Seite.*

## Anwendung

1.  Drücke die **<img src="images/BIM_Library.png" width=16px> [BIM Bibliothek](BIM_Library/de.md)** Taste

    :   Ergebnis: In der [Combo Ansicht](Combo_view/de.md) → [Aufgabenpaneel](Task_panel/de.md) wird ein Dialog mit dem Titel **Bibliotheksbrowser** angezeigt
2.  Klicke im Bibliotheksbrowser auf eine Datei
3.  Doppelklicke darauf oder drücke die Taste **Einfügen** Taste
4.  Klicke auf einen Punkt in der [3D Ansicht](3D_view/de.md) oder gib eine Koordinate manuell ein, um das Objekt zu platzieren

## Optionen

-   Es werden [FCStd](FCStd.md), [STEP](STEP.md) und [BREP](BREP.md) Dateien unterstützt. Nur STEP und BREP Dateien sind postionierbar. Bei FCStd Dateien kannst du keine Positionierung wählen, da sie aus einer komplexen Reihe von Objekten mit signifikanten Positionen bestehen können. Wenn du eine FCStd Datei auswählst, wird ihr Inhalt an der Position eingefügt, die in der Datei definiert ist.
-   STEP und BREP Objekte werden als <img alt="Arch Equipment" src=images/Arch_Equipment.svg  style="width:24px;"> eingefügt [Ausrüstung](Arch_Equipment/de.md) ohne separate Basisform eingefügt. Das nachträgliche Hinzufügen einer Basisform zu diesen Objekten zerstört deren aktuelle Form.
-   Beim Platzieren eines Objekts kannst du dessen Einfügepunkt zwischen Original (dem in der Datei definierten (`0,0,0`) Punkt), oben, Mitte, unten und links, Mitte und rechts wählen.
-   Die Bibliothek kann offline arbeiten, in diesem Fall ist sie darauf angewiesen, dass die Erweiterung \"Teilebibliothek\" installiert (und vom Benutzer aktualisiert) wird, oder online, in diesem Fall browst sie direkt aus dem [Teilebibliothek-Git-Repository](https://github.com/FreeCAD/FreeCAD-library) und ermöglicht das direkte Herunterladen von dort.



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > [Arch](Category_Arch.md) > BIM Library/de
