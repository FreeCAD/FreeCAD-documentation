# Splash screen/de
## Beschreibung

Der Begrüßungsbildschirm (Splash-Screen) ist ein Bild, das während des Starts von FreeCAD erscheint. Der Begrüßungsbildschirm kann im [Voreinstellungseditor](Preferences_Editor/de#Allgemein_2.md) ausgeschaltet werden, indem die Option \"Splashscreen beim Starten anzeigen\" deaktiviert wird.


{{Version/de|1.0}}

: Das Bild des Begrüßungsbildschirms wird zufällig aus mehreren Bildern ausgewählt, die Modelle von Anwendern zeigen und ausgewählte Addon-Arbeitsbereiche.



## Benutzerdefinierter Begrüßungsbildschirm 

Um einen eigenen Begrüßungsbildschirm einzusetzen, muss der als Abbildung mit dem Namen **splash_image.png** in einem der, vom jeweiligen Betriebssystem abhängigen, folgenden Verzeichnisse abgelegt werden:

-   **Linux:** **$XDG_DATA_HOME/FreeCAD/Gui/images/** (das entspricht normalerweise **~/.local/share/FreeCAD/Gui/images/**)
-   **Windows:** **%APPDATA%\FreeCAD\Gui\images\** (normalerweise **C:\Users\username\AppData\Roaming\FreeCAD\Gui\images\**)
-   **MacOS:** **~/Library/Application Support/FreeCAD/Gui/images/**

Das Verzeichnis kann Durch Eingeben des Python-Befehls {{Incode|App.getUserAppDataDir()}} in der [Python-Konsole](Python_console/de.md) gefunden werden. Die Ordner {{Incode|Gui}} und {{Incode|images}} müssen eventuell zuerst noch angelegt werden. Derselbe eigene Begrüßungsbildschirm wird für alle FreeCAD-Versionen auf diesem Computer eingesetzt.



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > Splash screen/de
