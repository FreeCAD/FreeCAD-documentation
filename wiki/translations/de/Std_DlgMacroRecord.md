---
 GuiCommand:
   Name: Std DlgMacroRecord
   Name/de: Std DialogMakroAufzeichnen
   MenuLocation: Macros/de , Makro aufzeichnen...
   Workbenches: Alle
   Siehe auch: Std_DlgMacroExecuteDirect/de
---

# Std DlgMacroRecord/de



## Beschreibung

Der **Std DlgMacroRecord** Befehl startet eine [Makro](Macros/de.md) Aufnahmesitzung, während der Benutzeraktionen in einem FreeCAD Makro, einer Datei mit der **.FCMacro** Erweiterung gespeichert werden. Ein Makro kann später wiedergegeben und ausgeführt werden, um die aufgezeichneten Aktionen zu wiederholen.

![](images/Std_DlgMacroRecord_dialog.png ) 
*Das Dialogfeld Makroaufzeichnung*



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Std_DlgMacroRecord.svg" width=16px> [Makro aufzeichnen...](Std_DlgMacroRecord/de.md)** drücken.
    -   Den Menüeintrag **Makro → <img src="images/Std_DlgMacroRecord.svg" width=16px> Makro aufzeichnen...** auswählen.
2.  Das Dialogfeld Makroaufzeichnung wird geöffnet.
3.  Im Eingabefeld **Makroname** einen Namen für das Makro eingeben.
4.  Wahlweise den **Makro-Zielpfad** durch drücken der Schaltfläche **...** anpassen.
5.  Die **Stop**-Taste funktioniert zu diesem Zeitpunkt nicht.
6.  Die Schaltfläche **Aufzeichnen** drücken, um das Dialogfeld zu schließen und die Aufzeichnung zu starten.
7.  Das Schaltflächensymbol des Befehls ändert sich zu **<img src="images/Std_MacroStopRecord.svg" width=16px>** und der Menütext ändert sich zu **Stop macro recording**.
8.  Die Aktionen ausführen, die aufgezeichnet werden sollen.
9.  Um die Aufnahmesitzung zu beenden, gibt es folgenden Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Std_MacroStopRecord.svg" width=16px> [Stop macro recording](Std_DlgMacroRecord/de.md)** drücken.
    -   Den Menüeintrag **Makro → <img src="images/Std_MacroStopRecord.svg" width=16px> Makroaufzeichnung stoppen** auswählen.



## Optionen

-   Wenn das Dialogfeld \"Makroaufzeichnung\" angezeigt wird: **Esc** oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Hinweise

-   Um das aufgezeichnete Makro auszuführen, verwende den Befehl [Std DlgMakroAusführen](Std_DlgMacroExecute/de.md).
-   Weitere Informationen über Makros findest du auf der [Makros](Macros/de.md) Seite.



## Einstellungen

-   Der Makropfad kann auch in den Einstellungen geändert werden: **Bearbeiten → Einstellungen... → Python → Makro → Makropfad**. Siehe [Einstellungseditor](Preferences_Editor/de#Makro.md).
-   In den meisten Fällen ist es unerwünscht, Aktionen aufzuzeichnen, die das Modell nicht ändern: unter **Bearbeiten → Einstellungen... → Allgemein → Makro → GUI Befehle** eine der folgenden Möglichkeiten ausführen:
    -   Um diese Aktionen auszuschließen, das Kontrollkästchen {{CheckBox|FALSE|GUI Befehle aufzeichnen}} deaktivieren.
    -   Um sie nur als Kommentar einzufügen, die beiden Kontrollkästchen {{CheckBox|TRUE|GUI Befehle aufzeichnen}} und {{CheckBox|TRUE|Aufzeichnen als Kommentar}} markieren.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std DlgMacroRecord/de
