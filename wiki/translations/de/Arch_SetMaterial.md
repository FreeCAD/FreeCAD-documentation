---
 GuiCommand:
   Name: Arch SetMaterial
   Name/de: Arch MaterialZuordnen
   MenuLocation: Arch , Materialwerkzeuge , Material
   Workbenches: Arch_Workbench/de, BIM_Workbench/de
   Shortcut: **M** **T**
   SeeAlso: Arch_MultiMaterial/de
---

# Arch SetMaterial/de



## Beschreibung

Dieses Werkzeug ermöglicht [Materialien](Material.md) zum aktiven Dokument hinzuzufügen und ein Material einem [Arch](Arch_Workbench/de.md)-Objekt zuzuweisen. Ein Material enthält alle Eigenschaften eines bestimmten Materials und steuert die Farbe des Objekts, dem es zugeordnet ist. Materialien werden in einem Ordner **Materials** im aktiven Dokument gespeichert.

![](images/Arch_materials_01.jpg )



## Anwendung

1.  Wahlweise ein oder mehrere Objekte auswählen, denen ein neues Material zugeordnet werden soll.

2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Arch_SetMaterial.svg" width=16px> [Material](Arch_SetMaterial/de.md)** drücken.
    -   Das Tastaturkürzel **M** dann **T**.
    -   Den Menüeintrag **Arch → Materialwerkzeuge → Material** auswählen.

3.  Ein voreingestelltes Material laden, oder ein neues durch Ausfüllen der Felder erstellen.

4.  
    **OK**drücken.



## Optionen

-   Beim Erstellen eines neuen Materials erlaubt dir ein Aufgabenfeld verschiedene Optionen zu setzen:

![](images/Arch_materials_02.jpg )

-   **Voreinstellungen wählen\...**: Wähle eins der voreingestellten Materialien, entweder wie vorgegeben oder angepasst durch ändern der folgenden Felder:
-   **Name**: Wähle einen Namen für das Material
-   **Bearbeiten**-Schaltfläche: Dies öffnet das aktuelle Material in FreeCADs [Materialeditor](FEM_MaterialEditor/de.md), der es erlaubt, zahlreiche zusätzliche Eigenschaften zu ändern und deine eigenen hinzuzufügen
-   **Beschreibung**: Eine detailliertere Beschreibung des Materials
-   **Farbe**: Eine Anzeigefarbe für das Material, die auf alle Objekte angewendet werden, die dieses Material benutzen
-   **Farbe der Schnittlinie**: Eine Anzeigefarbe für das Material, das auf TechDraw-Seiten angewendet wird, wenn ein Objekt mit diesem Material geschnitten wird und die \"Display materials\"-Eigenschaft auf der enthaltenden Schnittebene auf {{Incode|True}} gesetzt ist.
-   **Standard-code**: Ein Name und Referenznummer eines Spezifikationssystems, wie [Masterformat](https://en.wikipedia.org/wiki/MasterFormat) oder [Omniclass](http://www.omniclass.org/).
-   **Code browser**-Schaltfläche: erlaubt das Öffnen der Referenz in einem Web-Browser
-   **URL**: Eine URL, wo mehr Informationen zu diesem Material gefunden werden können
-   **URL**-Schaltfläche: erlaubt das Öffnen der URL in einem Web-Browser



## Bezug zu IFC 

Dies entspricht in etwa [IfcMaterial](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmaterial.htm).



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch SetMaterial/de
