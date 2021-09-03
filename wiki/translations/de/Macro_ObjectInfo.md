 {{Macro/de
|Name=Macro ObjectInfo
|Translate=Macro ObjectInfo
|Description=Liefert Informationen zum ausgewählten Objekt.
|Author=keithsloan52
|Version=1.0
|Date=2012-11-09
|FCVersion=Until 0.17 '''and PyQt4'''
|Download=Dies ist kein Makro, sondern eine WorkBench. Dekomprimieren Sie die ZIP-Datei und fügen Sie das vollständige Verzeichnis in das Mod-Benutzerverzeichnis ein [https://github.com/KeithSloan/FreeCAD_Info/archive/master.zip Info]
|SeeAlso=<img src=images/Arch_Survey.svg style="width:Arch Survey|24px"> [Arch Survey](Arch_Survey/de.md)
}}

## Beschreibung

Mit diesem WorkBench können Sie die Volumeninformationsfläche, den Massenschwerpunkt und den Moment der Trägheit des ausgewählten Objekts kennen.

<img alt="" src=images/ObjectInfoIt.png  style="width:480px;">

## Installation

Wenn Sie mit Linux arbeiten, müssen Sie im versteckten Ordner .FreeCAD einen Ordner mit dem Namen \"Mod\" erstellen, der sich in Ihrem Home-Ordner befindet. Legen Sie dann im Ordner \"Mod\" einen Ordner mit dem Namen \"Info\" an und extrahieren Sie den Inhalt des Archivs. Unter Windows habe ich keine Ahnung, wo das wäre. Verwenden Sie dasselbe Verfahren für Windows in C:\\Program Files\\FreeCAD\\Mod.

## Anwendung

Starten Sie dann FreeCAD, öffnen Sie Ihre STEP-Datei und wechseln Sie mit dem Workbench-Switcher zur Workbench \"Info\" oder über das Menü Ansicht → Workbench. Wählen Sie nun Ihren Körper aus und klicken Sie auf das Symbol \"Info\". In der linken Taskleiste werden einige Informationen zum Modell angezeigt, darunter Volumen, Oberfläche, Massenmittelpunkt und Trägheitsmoment.

## Code


{{MacroCode|code=
import webbrowser 

##########
# WorkBenche
# Code used to download the zip file from FreeCAD
##########

FreeCAD.Console.PrintMessage("\n" + "You must download the Info.zip file in the author github KeithSloan/FreeCAD_Infosite" + "\n")
FreeCAD.Console.PrintMessage("http://keithsloan.dynu.com/Keith&Jenny/" + "\n")
webbrowser.open("https://github.com/KeithSloan/FreeCAD_Info/archive/master.zip")

}}

## Links

Ein FreeCAD-Benutzer hat ein benutzerfreundliches \"Info\" Modul erstellt, das Sie hier erhalten können :<http://www.sloan-home.co.uk/FreeCAD/Info/Info.html>

Vom Forum [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)




