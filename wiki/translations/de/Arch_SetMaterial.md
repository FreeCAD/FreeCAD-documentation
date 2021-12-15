---
- GuiCommand:/de
   Name:Arch SetMaterial
   Name/de:Arch SetzeMaterial
   MenuLocation:Arch → Material Werkzeuge → Material
   Workbenches:[Arch](Arch_Workbench/de.md), [BIM](BIM_Workbench/de.md)
   Shortcut:**M** **T**
   SeeAlso:[Arch CompSetMaterial](Arch_CompSetMaterial/de.md), [Arch MultiMaterial](Arch_MultiMaterial/de.md)
---

# Arch SetMaterial/de

## Beschreibung

Die Material Werkzeuge erlauben dir [Materialien](Material/de.md) zum aktiven Dokument hinzuzufügen und ein Material einem [Arch](Arch_Workbench/de.md)-Objekt zuzuweisen. Materialien können alle Eigenschaften eines bestimmten Materials aufweisen und die Farbe des Objekts steuern, an das es angehängt wird. Materialien werden in einem **Materialien** Ordner im aktiven Dokument gespeichert.

![](images/Arch_materials_01.jpg )

## Anwendung

1.  Wähle optional ein oder mehrere Objekte aus, denen du ein neues Material zuordnen möchtest.
2.  Rufe den Befehl auf mehrere Arten auf:
    -   Drücke die **<img src="images/Arch_SetMaterial.svg" width=16px> [Material](Arch_SetMaterial/de.md)** Schaltfläche in dr Werkzeugleiste
    -   Verwende die **M** dann **T** Tastaturkürzel.
    -   Verwende die **Arch → Material Werkzeuge → Material** Eintrag aus dem oberen Menü.
3.  Lade ein voreingestelltes Material, oder erstelle ein neues durch Ausfüllen der Felder .
4.  Drücke **OK**.

## Optionen

-   Beim Erstellen eines neuen Materials erlaubt dir ein Aufgabenfeld verschiedene Optionen zu setzen:

![](images/Arch_materials_02.jpg )

-   **Voreinstellungen wählen\...**: Wähle eins der voreingestellten Materialien, entweder wie vorgegeben oder angepasst durch ändern der folgenden Felder:
-   **Kopiere bestehende\...**: Kopiere eins der bestehenden Materialien
-   **Name**: Wähle einen Namen für das Material
-   **Bearbeiten**-Schaltfläche: Dies öffnet das aktuelle Material in FreeCAD\'s [Materialeditor](Material_editor/de.md), der es erlaubt, zahlreiche zusätzliche Eigenschaften zu ändern und deine eigenen hinzuzufügen
-   **Beschreibung**: Eine detailliertere Beschreibung des Materials
-   **Farbe**: Eine Anzeigefarbe für das Material, die auf alle Objekte angewendet werden, die dieses Material benutzen
-   **Farbe der Schnittlinie**: Eine Anzeigefarbe für das Material, das auf TechDraw-Seiten angewendet wird, wenn ein Objekt mit diesem Material geschnitten wird und die \"Display materials\"-Eigenschaft auf der enthaltenden Schnittebene auf {{Incode|True}} gesetzt ist.
-   **Transparenz**: Ein Transparenzwert für dieses Material (0-99)
-   **Standard-code**: Ein Name und Referenznummer eines Spezifikationssystems, wie [Masterformat](https://en.wikipedia.org/wiki/MasterFormat) oder [Omniclass](http://www.omniclass.org/).
-   **Code browser**-Schaltfläche: erlaubt das Öffnen der Referenz in einem Web-Browser
-   **URL**: Eine URL, wo mehr Informationen zu diesem Material gefunden werden können
-   **URL**-Schaltfläche: erlaubt das Öffnen der URL in einem Web-Browser
-   **Vater**: ?

## Bezug zu IFC 

Dies entspricht in etwa [IfcMaterial](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmaterial.htm).

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SetMaterial/de
