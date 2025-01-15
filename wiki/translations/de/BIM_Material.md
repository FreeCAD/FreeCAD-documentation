---
 GuiCommand:
   Name: BIM Material
   Name/de: BIM Material
   MenuLocation: Verwalten , Material
   Workbenches: BIM_Workbench/de
---

# BIM Material/de



## Beschreibung

Zeigt den Dialog **BIM-Material** an. Der Dialog erlaubt es, schnell und einfach Tätigkeiten im Zusammenhang mit Material auszuführen, mit besonderem Fokus auf Effizienz bei der Arbeit mit vielen Objekten und vielen Materialien.

1.  Erzeuge ein neues [Material](Arch_SetMaterial/de.md) oder [Mehrfachmaterial](Arch_MultiMaterial/de.md)
2.  Weise gewählten Objekten ein vorhandenes Material oder Mehrfachmaterial zu.

<img alt="" src=images/BIM_materials_screenshot.png  style="width:600px;">



*Der Material Verwalter*



## Anwendung

1.  (Wahlweise) wähle ein oder mehrere Objekte
2.  Drücke die **<img src="images/BIM_Material.svg" width=16px> [Material](BIM_Material/de.md)** Schaltfläche in der Werkzeugleiste.

-   Wenn im aktiven Dokument kein Material vorhanden ist, dann wird das Fenster der Materialverwaltung nicht geöffnet, und es wird ein [Neues Material](Arch_SetMaterial/de.md) erstellt.
-   Wenn es im Dokument mindestens ein Material oder Mehrfachmaterial gibt, wird das Fenster der Materialverwaltung geöffnet.



## Werkzeuge des Material Verwalters 

Mit dem Material Verwalter kannst du::

-   **Materialien nach Namen suchen**: Verwende das suchen Kästchen
-   **ein Material den gewählten Objekten zuweisen**: Drücken von OK während ein Material gewählt ist weist es den Gewählten Objekten zu
-   **Erzeugen eines [Material](Arch_SetMaterial/de.md)**: Drücke die **Erzeuge neues Material** Schaltfläche
-   **Erzeugen eines [Mehrfachmaterial](Arch_MultiMaterial/de.md)**: Drücke die **Erzeuge Mehrfachmaterial** Schaltfläche
-   **Löschen eines Materials**: Wähle ein Material, Rechtsklicke das Material und wähle \"Löschen\"
-   **Löschen nicht verwendeter Materialien**: Drücke die **Lösche nicht Verwendet** Schaltfläche. Alle Materialien die von keinem einzigen Objekt verwendet werden, werden gelöscht
-   **Mische doppelte Materialien**: Drücke die **Mische doppelte** Schaltfläche. Mischt alle Materialien mit genau den gleichen Namen (z.B. Beton und Beton) oder genau gleichen Namen mit numerischem Suffix (z.B. Beton and Beton001)
-   **Umbenennen eines Materials**: Rechtsklick auf ein Material und \"Umbenennen\"
-   **Verdopple ein Material**: Rechtsklick auf ein Material und \"Verdoppeln\". Dies erzeugt eine komplette, unabhängige Kopie des gewählten Materials mit den gleichen Einstellungen
-   **Mische Materialien zusammen**: Rechtsklick auf ein Material und \"Mische zu\...\", Dann wählen eines anderen Materials. Das Erste wird entfernt, und allen Objekten die das Erste verwendet haben wird das Zweite zugeordnet



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Material/de
