# Macro at Startup/de
## Einführung


{{TOCright}}

In dieser Dokumentation wird erklärt, wie ein Makro so eingerichtet wird, dass es beim Start von FreeCAD automatisch ausgeführt wird.


<div class="mw-translate-fuzzy">

Vor Beginn sind folgende Dinge zu beachten    *

-   Das automatische Ausführen von Makros beim Start kann als Sicherheitsrisiko betrachtet werden. Du solltest nur Makros ausführen, denen du vertraust und die du zuvor getestet hast.
-   Du benötigst wahrscheinlich einige Python- und Codierungsbegriffe, um diesem Verfahren zu folgen
-   Wenn auf Benutzerordner (\'Mod\', \'Makro\', \...) verwiesen wird, befinden sich diese in deinem FreeCAD Benutzerordner. Du kannst sie unter Start und Konfiguration → [Benutzerbezogene Informationen](Start_up_and_Configuration/de#Benutzerbezogene_Informationen.md) finden.
-   Dies sollte nicht für Makros gemacht werden, die sich mit der Teilemodellierung befassen. Dies ist eher für Makros geeignet, die Funktionen hinzufügen, die Benutzeroberfläche verbessern, \...


</div>

## Anleitung

### Das Makro vorbereiten 

Im Allgemeinen wird es vorkommen, dass ein Makro nicht direkt mit einem Programmstart kompatibel ist und feinabgestimmt werden muss


<div class="mw-translate-fuzzy">

Betrachte das untenstehende Makro, das du von irgendwo heruntergeladen hast und das in deinem \'Makro\' Ordner mit dem Namen \'MeinSuperMakro.FCMakro\' gespeichert ist   *


</div>

    ## Import section ##
    from PySide import QtGui

    ## Definition section (classes, functions, ...)
    class MyMsgBox(QtGui.QMessageBox)   *

        def __init__(self)   *
            super(MyMsgBox, self).information(None, "MyTitle", "MyText")

    ## Main instruction section
    MyMsgBox()


<div class="mw-translate-fuzzy">

Alle Makros zeigen generell eine ähnliche Struktur   * Zuerst ein Import-, dann ein Definitions- und abschließend der Hauptbefehlsabschnitt. Wir werden uns auf letzteren fokussieren, weil diese Hauptbefehle (die recht einfach zu erkennen sind, weil sie am Anfang der Zeile stehen) tatsächlich die sind, die das Makro \'ausführen\'. In einem späteren Schritt müssen wir das Makro programmatisch importieren und dann ausführen. Dies ist in der aktuellen Struktur des Makros nicht möglich. Um das zu tun, müssen wir die Hauptbefehle in eine Funktion -z.B. run()- einschließen und dafür sorgen, dass diese Funktion auch bei einem manuellen Start durch den Benutzer aufgerufen wird. Wenn du nicht wirklich sicher bist, was du tust, wird es empfohlen, mit einer Kopie des Makros zu arbeiten (oder einfach das Original-Makro zu lassen, wie es ist). Die Originaldatei sollte wie folgt geändert werden   *


</div>

    from PySide import QtGui
    ## The 2 below lines shall be added if not already present to ensure FreeCAD modules are imported
    import FreeCAD as App
    import FreeCADGui as Gui

    class MyMsgBox(QtGui.QMessageBox)   *

        def __init__(self)   *
            super(MyMsgBox, self).information(None, "MyTitle", "MyText")

    ## Enclose the main instructions in a function
    def run()   *
        MyMsgBox()

    ## Ensure main instructions are still called in case of manual run
    if __name__ == '__main__'   *
        run()

Falls die Funktion \'run()\' bereits im Makro existiert, kannst du jeden anderen geeigneten Namen verwenden. Nun ist das Makro bereits, um in den FreeCAD-Start integriert zu werden.

### In FreeCAD Start integrieren 


<div class="mw-translate-fuzzy">

Erstelle zunächst einen neuen Ordner in deinem Benutzerordner \'Mod\', sagen wir \'MacroStartup\'. Kopiere das modifizierte Makro in diesen neu erstellten Ordner und benenne es mit der Erweiterung \'.py\' um, falls dies noch nicht der Fall ist (beachte, dass, wenn du das Makro selbst entwickelst, es auch im \'Makro\' Ordner mit der Erweiterung \'.py\' benannt werden kann, so dass du es beim Kopieren nicht umbenennen musst). Erstelle schließlich im gleichen Ordner eine Datei namens \'InitGui.py\', die folgenden Code enthält


</div>

    def runStartupMacros(name)   *
        # Do not run when NoneWorkbench is activated because UI isn't yet completely there
        if name != "NoneWorkbench"   *
            # Run macro only once by disconnecting the signal at first call
            FreeCADGui.getMainWindow().workbenchActivated.disconnect(runStartupMacros)

            # Following 2 lines shall be duplicated for each macro to run
            import MySuperMacro
            MySuperMacro.run()

            # Eg. if a second macro shall be launched at startup
            # import MyWonderfulMacro
            # MyWonderfulMacro.run()

    # The following 2 lines are important because InitGui.py files are passed to the exec() function...
    # ...and the runMacro wouldn't be visible outside. So explicitly add it to __main__
    import __main__
    __main__.runStartupMacros = runStartupMacros

    # Connect the function that runs the macro to the appropriate signal
    FreeCADGui.getMainWindow().workbenchActivated.connect(runStartupMacros)

Beachte, dass dies nur einmal geschehen soll. Wenn du mehr als ein Makro ausführen möchtest, kannst du einfach die anderen in derselben Datei hinzufügen (siehe die Kommentare zum obigen Code).


<div class="mw-translate-fuzzy">

Wir sind durch. Dein Makro sollte beim nächsten FreeCAD Start automatisch ausgeführt werden.


</div>

Beachte, dass, wenn das Originalmakro über den Erweiterungsverwalter heruntergeladen wurde, es bei der Aktualisierung überschrieben wird und du daher die Schritte hier erneut befolgen musst.

## General Notes 

-   In the example \'InitGui.py\' script above, the function named \'runStartupMacros()\' may be changed, so long as you also change the other four references to it, so they all match.
-   This script will be run prior to the auto loading of your desired startup workbench in the FreeCAD Preferences, [General settings](Preferences_Editor#General_settings.md).

### Linux

### MacOS

### Windows

-   In the above example, you may place the \'MacroStartup\' folder within the \'Mod\' folder of your FreeCAD root directory (whether installed version or portable version), or you may create a \'Mod\' folder along side the \'Macro\' folder in \'%USERPROFILE%\\AppData\\Roaming\\FreeCAD\\\', and place the \'MacroStartup\' folder there.
-   From observation, the workbenches found within either \'Mod\' folder are loaded alphabetically. Those in the FreeCAD root \'Mod\' folder are loaded first, then FreeCAD scans the \'%USERPROFILE%\\AppData\\Roaming\\FreeCAD\\Mod\' folder for additional workbenches.

## Verwandtes


<div class="mw-translate-fuzzy">

-   [Extra_python_modules#LazyLoader](Extra_python_modules#LazyLoader.md) LazyLoader ist ein Python-Modul, das verzögertes Laden erlaubt.


</div>




[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md) [Category   *Macros](Category_Macros.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Macros](Category_Macros.md) > Macro at Startup/de
