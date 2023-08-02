---
- GuiCommand:
   Name: Std DlgMacroRecord
   Name/de: Std DialogMakroAufzeichnen
   MenuLocation: Macros/de -> Makro aufzeichnen...
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
    -   Drücke die **<img src="images/Std_DlgMacroRecord.svg" width=16px> [Std DlgMakroAufzeichnen](Std_DlgMacroRecord/de.md)** Schaltfläche.
    -   Wähle die **Makro → <img src="images/Std_DlgMacroRecord.svg" width=16px> Makroaufnahme...** Option aus dem Menü.
2.  Das Dialogfeld Makroaufzeichnung wird geöffnet.
3.  Gib einen Namen für das Makro in das Eingabefeld **Makroname** ein.
4.  Ändere wahlweise den **Makropfad** durch drücken der **...** Taste
5.  Die **Stop** Taste funktioniert zu diesem Zeitpunkt nicht.
6.  Drücke die **Aufzeichnen** Schaltfläche, um das Dialogfeld zu schließen und die Aufzeichnungssitzung zu starten.
7.  Führe die Aktionen aus, die du aufzeichnen möchtest.
8.  Um die Aufnahmesitzung zu beenden, führe eine der folgenden Aktionen aus:
    -   Drücke die **<img src="images/Std_MacroStopRecord.svg" width=16px> [Std MacroStopRecord](Std_MacroStopRecord.md)** Schaltfläche.
    -   Wähle den **Makro → <img src="images/Std_MacroStopRecord.svg" width=16px>. Stoppe Makroaufzeichnung**s Option aus dem Menü.



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
