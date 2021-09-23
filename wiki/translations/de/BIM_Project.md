---
- GuiCommand:Addon
   Name:BIM Projekt
   Workbenches:[BIM](BIM_Workbench/de.md)
   Addon:BIM
   MenuLocation:Verwalten → Projekt verwalten...
---

# BIM Project/de

## Beschreibung

<img alt="" src=images/BIM_project_screenshot.png  style="width:1024px;">

Der Projekteinstellungsdialog ist ein Assistentendialog, der es dir ermöglicht, einen Basissatz von Führungsobjekten im aktuellen Dokument oder in einem neuen Dokument zu erstellen, der dir hilft, mit der Modellierung eines BIM Projekts zu beginnen.

Der Projekteinstellungsdialog kann erstellt werden:

-   Eine neue [Dokument](Document_structure/de.md). Alternativ werden die anderen Objekte im aktuell geöffneten Dokument angelegt.
-   Ein [Standort](Arch_Site/de.md). Das Standortobjekt repräsentiert ein Stück Gelände, auf dem sich dein Projekt befinden wird. Du kannst ihm eine Reihe nützlicher Eigenschaften geben, wie z. B. eine Straßenadresse und Erdkoordinaten. Bei der Erstellung ist der Standort nur ein leerer Container für andere BIM Objekte, aber ein 3D Objekt, das das eigentliche Gelände darstellt, kann später daran angehängt werden.
-   Ein [Gebäude](Arch_Building/de.md). Das Gebäudeobjekt ist ein Container für alle BIM Objekte, die zu einem Gebäude gehören werden. Sie können einen Gebäudetyp definieren und ihm grobe rechteckige Abmessungen geben, die als ein auf der Bodenebene (X,Y) gezeichnetes Rechteck dargestellt werden.
-   Ein Satz von [Achsen](Arch_Axis/de.md), indem Sie deren Anzahl und Abstand definieren. Die Achsen werden als Richtlinien für die Ausrichtung von 2D- und 3D-Objekten verwendet. Diese Achsen können später geändert oder neue Achsen eingeführt werden.
-   Ein Satz von [GebäudeTeile](Arch_BuildingPart/de.md) zur Darstellung von Ebenen. GebäudeTeile sind generische BIM Container Objekte, die verwendet werden können, um andere BIM Objekte auf eine Reihe von sinnvollen Arten zu gruppieren, z. B. wiederholbare Komponenten oder Gebäudeebenen.
-   Ein Satz von Standard [Gruppen](Std_Group/de.md) innerhalb jeder Ebene. Gruppen können verwendet werden, um Ihre BIM Objekte in übersichtlicheren Kategorien zu organisieren, wie z. B. \"Wände\" oder \"Säulen\". Sie haben keinen Einfluss auf das Modell selbst, helfen aber oft, die Struktur Ihres Modells übersichtlicher zu gestalten, wenn es viele Objekte enthält.

### Vorlagen

Das Projektwerkzeug unterstützt zwei Arten von Vorlagen: Nachdem du die verschiedenen Optionen ausgefüllt hast, kann der Inhalt des BIM Projekteinstellungsassistenten als Vorlage **gespeichert** werden. Diese Vorlagen können **wiederhergestellt** und zu einem späteren Zeitpunkt angepasst werden. Die Projektvorlagen werden als einfache Textdateien in deinem FreeCAD Benutzerordner gespeichert.

Alternativ kannst du auch den Inhalt des aktuellen Dokuments als Vorlage speichern. Dadurch wird das aktuell geöffnete Dokument als Standarddatei **.FCStd** gespeichert, enthält aber auch zusätzliche BIM Einstellungen wie die aktuelle Arbeitsebene oder die aktuellen Einheiten. Wenn du die Option **Wiederherstellen** jederzeit verwendest, wird der Inhalt dieser Vorlagendatei mit dem aktiven Dokument zusammengeführt und alle darin gefundenen Einstellungen werden angewendet.

---
[documentation index](../README.md) > BIM Project/de
