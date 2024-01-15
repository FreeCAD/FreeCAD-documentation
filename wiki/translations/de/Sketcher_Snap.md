---
 GuiCommand:
   Name: Sketcher Snap
   Name/de: Sketcher Einrasten
   Workbenches: Sketcher_Workbench/de
   Version: 0.21
   SeeAlso: Sketcher_Grid/de
---

# Sketcher Snap/de



## Beschreibung

Der Befehl **Sketcher Einrasten** schaltet den Einrastmodus für alle Skizzen ein bzw. aus. Einzelne Einstellungen können im zugehörigen Menü angepasst werden.

Einrasten funktioniert nur während Geometrie erstellt wird. Man beachte, dass das Einrasten nur eine Zeichenhilfe ist; es legt keine zusätzlichen Randbedingungen fest.



## Anwendung

1.  Die Schaltfläche **<img src="images/Sketcher_Snap.svg" width=16px> [Einrasten umschalten](Sketcher_Snap/de.md)** drücken, um Einrasten ein- oder auszuschalten.
2.  Wahlweise rechts auf den Pfeil nach unten klicken, um das Menü zu öffnen. Die Einstellungen in diesem Menü können nur geändert werden, wenn das Einrasten eingeschaltet ist:
    ![](images/Sketcher_Snap_Menu.png )
    -   Ist die Checkbox **Snap to grid** aktiviert, wird der Mauszeiger auf Rasterlinien und deren Kreuzungspunkten einrasten. Dies funktioniert auch, wenn das Raster ausgeblendet ist.
    -   Ist die Checkbox **Snap to objects** aktiviert, wird der Mauszeiger auf Kanten von Geometrien und auf Mittelpunkten von Linien und Bögen einrasten.
    -   Der Wert für **Snap angle** bestimmt den Winkel für das Einrasten auf Winkeln. Eirasten erfolgt auf Vielfachen dieses Winkels, ausgehend von der positiven X-Achse der Skizze. Die **Ctrl**-Taste muss für dieses Einrasten gedrückt gehalten werden. Es funktioniert nur, wenn bestimmte Geometrien erstellt werden, wie z.B. [Linien](Sketcher_CreateLine/de.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Snap/de
