---
 GuiCommand:
   Name: BIM ProjectManager
   Name/de: BIM Projektmanager
   MenuLocation: Manage , Manage project...
   Workbenches: BIM_Workbench/de
---

# BIM ProjectManager/de



## Beschreibung

Der Dialog **BIM Project Setup** ermöglicht einen Basissatz von Leitobjekten im aktuellen Dokument oder in einem neuen Dokument zu erstellen, der dabei hilft, mit der Modellierung eines BIM-Projekts zu beginnen.

<img alt="" src=images/BIM_project_screenshot.png  style="width:600px;"> 
*BIM-Projekt-Setup*



## Anwendung

Mit dem Dialog BIM Project Setup können erstellt werden:

-   Eine neues [Dokument](Document_structure/de.md). Alternativ werden die anderen Objekte im aktuell geöffneten Dokument angelegt.
-   Ein [Grundstück](Arch_Site/de.md). Das Grundstückobjekt repräsentiert ein Stück Gelände, auf dem sich dein Projekt befinden wird. Du kannst ihm eine Reihe nützlicher Eigenschaften geben, wie z. B. eine Straßenadresse und Erdkoordinaten. Bei der Erstellung ist der Standort nur ein leerer Container für andere BIM-Objekte, aber ein 3D-Objekt, das das eigentliche Gelände darstellt, kann später daran angehängt werden.
-   Ein [Gebäude](Arch_Building/de.md). Das Gebäudeobjekt ist ein Container für alle BIM-Objekte, die zu einem Gebäude gehören. Sie können einen Gebäudetyp definieren und ihm grobe rechteckige Abmessungen geben, die als ein auf der Bodenebene (X,Y) gezeichnetes Rechteck dargestellt werden.
-   Ein Satz von [Achsen](Arch_Axis/de.md), indem Sie deren Anzahl und Abstand definieren. Die Achsen werden als Richtlinien für die Ausrichtung von 2D- und 3D-Objekten verwendet. Diese Achsen können später geändert oder neue Achsen eingeführt werden.
-   Ein Satz von [Gebäudeteilen](Arch_BuildingPart/de.md) zur Darstellung von Geschossen (Etagen, Stockwerke). GebäudeTeile sind generische BIM-Container-Objekte, die verwendet werden können, um andere BIM-Objekte auf eine Reihe von sinnvollen Arten zu gruppieren, z.B. wiederholbare Komponenten oder Stockwerke.
-   Ein Satz von Standard-[Gruppen](Std_Group/de.md) innerhalb jeder Etage. Gruppen können verwendet werden, um BIM-Objekte in übersichtlicheren Kategorien zu organisieren, wie z. B. \"Wände\" oder \"Säulen\". Sie haben keinen Einfluss auf das Modell selbst, helfen aber oft, die Struktur eines Modells übersichtlicher zu gestalten, wenn es viele Objekte enthält.



## Vorlagen

Das Projektwerkzeug unterstützt zwei Arten von Vorlagen:

-   Nachdem die verschiedenen Optionen ausgefüllt wurden, kann der Inhalt des BIM-Projekteinstellungsassistenten als Vorlage **gespeichert** werden. Diese Vorlagen können **wiederhergestellt** und zu einem späteren Zeitpunkt angepasst werden. Die Projektvorlagen werden als einfache Textdateien im FreeCAD-Benutzerordner gespeichert.
-   Alternativ kann der Inhalt des aktuellen Dokuments als Vorlage gespeichert werden. Dies sichert das aktuell geöffnete Dokument als Standard-**.FCStd**-Datei, beinhaltet aber auch zusätzliche BIM-Einstellungen wie die aktuelle Arbeitsebene oder aktuelle Einheiten. Die Option **wiederherstellen** kann jederzeit dazu verwendet werden, die Inhalte dieser Vorlage in das aktive Dokument zu laden und alle darin gefundenen Einstellungen anzuwenden.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM ProjectManager/de
