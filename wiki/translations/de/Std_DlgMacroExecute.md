---
 GuiCommand:
   Name: Std DlgMacroExecute
   Name/de: Std DlgMakroAusführen
   MenuLocation: Makro , Makros...
   Workbenches: Alle
   SeeAlso: Std_DlgMacroExecuteDirect/de
---

# Std DlgMacroExecute/de



## Beschreibung

Der Befehl **Std DlgMakroAusführen** öffnet das Dialogfenster Makro ausführen. Von diesem Dialogfenster aus können Makros ausgeführt, bearbeitet und verwaltet werden.

<img alt="" src=images/Std_DlgMacroExecute_dialog.png  style="width:300px;"> 
*Das Dialogfenster Makro ausführen*



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Std_DlgMacroExecute.svg" width=16px> [Makros...](Std_DlgMacroExecute/de.md)** drücken.
    -   Den Menüeintrag **Makro → <img src="images/Std_DlgMacroExecute.svg" width=16px> Makros...** auswählen.
2.  Das Dialogfenster **Makro ausführen wird** geöffnet. Siehe [Optionen](#Optionen.md).



## Optionen



### Datei suchen / In Datei suchen 

:   
    {{Version/de|1.0}}
    





:   Diese zwei Eingabefelder können verwendet werden, um Makros in den Dateilisten unter **Benutzermakros** oder **Systemmakros** zu filtern. Dies kann ein regulärer Ausdruck sein oder einfacher Text. Groß- und Kleinschreibung werden nicht berücksichtigt.





:   **Datei suchen** filtert die Liste nach Dateinamen. Nur Dateinamen, die dem eingegebenen Text entsprechen, erscheinen in der Liste. **In Dateien suchen** filtert die Liste nach Dateiinhalten. Nur Dateien, deren Textinhalt dem eingegebenen Text entspricht, erscheinen in der Liste.





:   Das Leeren des Eingabefeldes deaktiviert den zugehörigen Filter. Enthalten beide Eingabefelder Texte, werden beide Filter angewendet. Filtern kann auch eine leere Liste ergeben.



### Benutzermakros

:   Unter **Benutzermakros** werden die Makros gelistet, die am **Speicherort der Benutzermakros** zur Verfügung stehen.

1.  Ein Makro in der Liste anklicken, um es auszuwählen.
2.  Der Name des ausgewählten Makros erscheint im Feld **Makroname**.



### Systemmakros

:   Damit **Systemmakros** verwendet werden können, muss zuerst ein Ordner **Macro** als ein Geschwister-Ordner des Ordners **bin**, in dem FreeCAD installiert ist, angelegt und darin ein paar Makros abgelegt werden.





:   Um den Ordner **bin** zu finden, gibt man folgendes in der [Python-Konsole](Python_console/de.md) ein:





:   
    
```python
    App.getHomePath()
    
```
    

1.  Ein Makro in der Liste anklicken, um es auszuwählen.
2.  Der Name des ausgewählten Makros erscheint im Feld **Makroname**.



### Speicherort der Benutzermakros 

1.  Die Schaltfläche **...** drücken, um den Ablageort der Benutzermakros zu ändern.
2.  Zu einem anderen Ordner wechseln und diesen auswählen.



### Ausführen

1.  Zum Ausführen eines Makros gibt es folgende Möglichkeiten:
    -   Das Makro in der Liste auswählen und die Schaltfläche **Ausführen** drücken.
    -   Ein Doppelklick auf das Makro in der Liste.
2.  Das Dialogfenster wird geschlossen.
3.  Das Makro wird ausgeführt.



### Schließen

1.  Die **Esc**-Taste oder Die Schaltfläche **Schließen** drücken, um das Dialogfenster zu schließen.



### Erstellen

1.  Die Schaltfläche **Erstellen** drücken, um eine neue Makrodatei anzulegen.

2.  Einen Namen im Dialogfenster, das gerade geöffnet wurde, eingeben. Die Dateiendung **.FCMacro** muss nicht eingegeben werden.

3.  
    **Enter**oder die Schaltfläche **OK** drücken.

4.  Beide Dialogfenster werden geschlossen.

5.  Die neue Datei wird im Makroeditor geöffnet.



### Löschen

1.  Das Makro, das gelöscht werden soll, in der Liste auswählen.
2.  Die Schaltfläche **Löschen** drücken.
3.  Die Schaltfläche **Ja** im Bestätigungsdialog, der geöffnet wird, drücken.



### Bearbeiten

1.  Das Makro, das bearbeitet werden soll, in der Liste auswählen.
2.  Die Schaltfläche **Bearbeiten** drücken.
3.  Das Dialogfenster wird geschlossen.
4.  Das ausgewählte Makro wird im Makroeditor geöffnet.



### Umbenennen

1.  Das Makro, das umbenannt werden soll, in der Liste auswählen.

2.  Die Schaltfläche **Umbenennen** drücken.

3.  Einen neuen Namen im Dialogfenster, das geöffnet wurde, eingeben. Die Dateiendung **.FCMacro** muss nicht eingegeben werden.

4.  
    **Enter**oder die Schaltfläche **OK** drücken.



### Kopieren

1.  Das Makro, das kopiert werden soll, in der Liste auswählen.

2.  Die Schaltfläche **Kopieren** drücken.

3.  Einen neuen Namen im Dialogfenster, das geöffnet wurde, eingeben. Die Dateiendung **.FCMacro** muss nicht eingegeben werden.

4.  
    **Enter**oder die Schaltfläche **OK** drücken.



### Werkzeugleiste

1.  Das Makro auswählen, das zu einer benutzerdefinierten Symbolleiste hinzugefügt werden soll, in der Liste auswählen.
2.  Die Schaltfläche **Symbolleiste** drücken.
3.  Zwei Dialogfenster führen durch die erforderlichen Schritte. Siehe [Anpassung der Oberfläche](Interface_Customization/de.md) für weitere Informationen.



## Herunterladen

1.  Die Schaltfläche **Herunterladen** drücken, um den [Addon-Manager](Std_AddonMgr/de.md) zu starten.



## Hinweise

-   Mehr über Makros erfährt man auf der Seite [Makros](Macros/de.md).



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md).

-   Der Ablageort der Benutzermakros kann auch in den Voreinstellungen angepasst werden: **Bearbeiten → Einstellungen... → Python → Makro → Makro-Zielpfad**.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std DlgMacroExecute/de
