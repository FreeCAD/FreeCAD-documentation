---
- TutorialInfo:/de
   Topic:Programmierung
   Level:durchschnittliche Programmierer
   Zeit:15 Minuten
   FCVersion:Alle
   Author:[Mario52](User_Mario52.md)
---

# How to install macros/de







## Beschreibung

Seit v0.17 ist es einfach, Makros mit Hilfe des [Erweiterungsverwalter](Std_AddonMgr/de.md) hinzuzufügen. Ein normaler Benutzer braucht nicht mehr zu tun, als dieses Werkzeug zu benutzen. Lies weiter, um weitere Informationen zur Installation von [Makros](macros/de.md) zu erhalten.

Makros sind Befehlssequenzen, die zur Ausführung einer komplexen Zeichenoperation verwendet werden. Makros sind [Python](Python/de.md) Skripte, d.h. sie sind Textdateien, die mit einem Texteditor geschrieben und bearbeitet werden können.

Während Python Skripte normalerweise die Erweiterung `.py` haben, sollten FreeCAD Makros die Erweiterung `.FCMacro` haben. Eine Sammlung von Makros, die von erfahrenen Anwendern geschrieben wurden, findest Du auf der Seite [Makrozepte](macros_recipes/de.md).

Siehe [Einführung in Python](Introduction_to_Python/de.md), um mehr über die Programmiersprache Python zu erfahren, und dann [Python Skript Tutorium](Python_scripting_tutorial/de.md) und [FreeCAD Skript Grundlagen](FreeCAD_Scripting_Basics/de.md), um das Schreiben von Makros zu erlernen.

Hier ist ein Video über [Installieren von FreeCAD Makros in Ubuntu](https://wiki.opensourceecology.org/wiki/Installing_Macros_in_FreeCAD).



## Das Makro Menü und die Werkzeugleiste 

### Toolbar


<div class="mw-translate-fuzzy">

### Werkzeugleiste

-   <img alt="record" src=images/Std_DlgMacroRecord.svg  style="width:32px;"> [Aufzeichnen](Std_DlgMacroRecord/de.md)
-   <img alt="stop" src=images/Std_MacroStopRecord.svg  style="width:32px;"> [Makro Aufzeichnung Beenden](Std_MacroStopRecord/de.md)
-   <img alt="open editor" src=images/Std_DlgMacroExecute.svg  style="width:32px;"> [Makros\...](Std_DlgMacroExecute/de.md)
-   <img alt="execute" src=images/Std_DlgMacroExecuteDirect.svg  style="width:32px;"> [Makro Ausführen](Std_DlgMacroExecuteDirect/de.md)


</div>

### Menu


<div class="mw-translate-fuzzy">

### Menü

Neben den Werkzeugen in der Werkzeugleiste sind auch die folgenden Funktionen im **Makro** Menü verfügbar.

-   [An den entfernten Debugger anhängen](Std_MacroAttachDebugger/de.md)
-   <img alt="" src=images/Std_MacroStartDebug.svg  style="width:32px;"> [Fehlersuche Makro](Std_MacroStartDebug/de.md)
-   <img alt="" src=images/Std_MacroStopDebug.svg  style="width:32px;"> [Fehlersuche beenden](Std_MacroStopDebug/de.md)
-   [Schritt weiter](Std_MacroStepOver/de.md)
-   [Schritt nach vorn](Std_MacroStepInto/de.md)
-   [Umschalten Haltepunkt](Std_ToggleBreakpoint/de.md)


</div>



## Makros Verzeichnis 


<div class="toccolours mw-collapsible mw-collapsed">

Makros werden in einem bestimmten Ordner unter dem FreeCAD Benutzerverzeichnis erstellt. Dieses Verzeichnis kann im [Makrodialog ausführen](Std_DlgMacroExecute/de.md), oder im [Einstellungseditor](Preferences_Editor/de.md), über das Menü **Bearbeiten → Einstellungen → Allgemein →  Makro → Makro Aufnahme Einstellungen**.

Heruntergeladene Makros sollten ebenfalls in diesem Verzeichnis abgelegt werden.


<div class="mw-collapsible-content">

### Default directory 


<div class="mw-translate-fuzzy">

### Standardverzeichnis

Makros können einfach kopiert werden in


</div>


```python
$ROOT_DIR/
```

wobei `$ROOT_DIR` ein Verzeichnis der obersten Ebene ist, das von FreeCAD beim Start durchsucht wird.

Der `$ROOT_DIR` könnte ein systemweites Verzeichnis sein, in diesem Fall wird das Makro für alle Benutzer installiert.

-   Unter Linux ist es normalerweise `/usr/share/freecad/`
-   Unter Windows ist es normalerweise `C:\Program Files\FreeCAD\`
-   Unter Mac OSX ist es normalerweise `/Applications/FreeCAD/`


<div class="mw-translate-fuzzy">

Der `$ROOT_DIR` könnte das Verzeichnis eines bestimmten Benutzers sein.

-   Unter Linux ist es normalerweise `/home/username/.FreeCAD/`
-   Unter Windows ist es normalerweise `C:\Benutzername\Benutzername\Anwendungsdaten\FreeCAD\`
-   Unter Mac OSX ist es normalerweise `/Benutzer/Benutzername/Bibliothek/Einstellungen/FreeCAD/`


</div>

### Configuring the user directory 


<div class="mw-translate-fuzzy">

### Konfigurieren des Benutzerverzeichnisses 

1\. Öffne das Menü **Makro → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Makros...](Std_DlgMacroExecute/de.md)**, um den [Makrodialog ausführen](Std_DlgMacroExecute/de.md).


</div>

![](images/Dxf_Importer_Install_01.png ) 
*align=center|Öffnen des Makro ausführen Dialogs*


<div class="mw-translate-fuzzy">

2\. Setze den entsprechenden `Nutzer Makros Standort`.

-   Linux: normalerweise `/home/username/.FreeCAD/`
-   Windows: normalerweise `C:\Users\username\AppData\Roaming\FreeCAD\`
-   MacOS: normalerweise `/Users/username/Library/Preferences/FreeCAD/`


</div>

![](images/Dxf_Importer_Install_02.png ) 
*align=center|Setting of the macros directory*

3\. Navigiere zu diesem Verzeichnis auf deinem Computer.

-   Linux: Füge die Adresse in deinen Dateimanager ein, \"Nautilus\" oder andere. Eventuell musst du **Ctrl**+**H** drücken, um das versteckte Verzeichnis `.FreeCAD/` sichtbar zu machen.
-   Windows: Füge die Adresse in dein \"Datei Suchprogramm\" ein und bestätige.
-   MacOS: Suche den Ordner im \"Finder\" oder füge die Adresse in ein \"Datei Suchprogramm\" ein; merke dir das `file:///` Vorsatzzeichen im \"Datei Suchprogramm\" für eine Datei auf der Festplatte.

![](images/Dxf_Importer_Install_03.png ) 
*align=center|Accessing the macros directory in the operating system*

4\. Füge diesem Verzeichnis Makrodateien hinzu.

-   Linux: Lasse den Dateimanager geöffnet und setze ein Lesezeichen für den schnelleren Zugriff.
-   Windows: Lasse das Datei Suchprogramm geöffnet.
-   MacOS: Lasse entweder ein \"Finder\"-Fenster geöffnet, oder setze ein Lesezeichen für den Speicherort in deinem \"Datei Suchprogramm\", oder richte einen \"Alias\" ein, um darauf zu zeigen, oder ziehe den Ordner in die \" Seitenleiste\" des \"Finders\", so dass er von anderen Programmen, wie z.B. Texteditoren, verwendet werden kann.

![](images/Dxf_Importer_Install_04.png ) 
*align=center|Macros directory*





</div>


</div>



## Makros installieren 


<div class="toccolours mw-collapsible mw-collapsed">



### Automatische Methode 

Ab FreeCAD 0.17 verwendet man den [Addon-Manager](Std_AddonMgr/de.md) in **Werkzeuge → Addon-Manager**, um ein Makro zu installieren, das in das [FreeCAD-Macros](https://github.com/FreeCAD/FreeCAD-macros)-Repositorium aufgenommen wurde.


<div class="mw-collapsible-content">

In früheren Versionen von FreeCAD konntest du zwei automatisierte Wege nutzen, um Makros und andere Addons zu installieren:

-   [addons_installer.FCMacro](https://github.com/FreeCAD/FreeCAD-addons): selbst ein Makro, dies war der Vorläufer des Zusatzmanagers, und wird im [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons) Repositorium beherbergt. Bei Neuinstallationen von FreeCAD muss dieses Tool nicht verwendet werden.
-   [freecad-pluginloader](https://github.com/microelly2/freecad-pluginloader): ebenfalls ein Makro, es kann verwendet werden, um neue Komponenten in FreeCAD zu installieren. Es wird nicht mehr weiterentwickelt.

Der empfohlene Weg, Zusätze, d.h. [externe Arbeitsbereiche](external_workbenches/de.md) und Makros zu installieren, ist mit dem [Addon-Manager](Std_AddonMgr/de.md). Du kannst jedoch immer noch Makros mit den in den folgenden Abschnitten beschriebenen manuellen Methoden zu deinem System hinzufügen; dies ist nützlich, wenn du deinen eigenen Code entwickelst und testest.


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### Manuelle Methode 1. Kopiere den Code in den Makro Editor 

=

Für Makros, die relativ klein sind, 300 Zeilen oder weniger, kann der Code kopiert und direkt in den FreeCAD Makro-Editor eingefügt werden.


<div class="mw-collapsible-content">

Wir werden <img alt="" src=images/Part_Prism_Apothem.svg  style="width:24px;"> [Macro Apothem Based Prism GUI](Macro_Apothem_Based_Prism_GUI/de.md) als ein Beispiel verwenden.

1\. Gehe auf die Makro Wiki Seite, die unter [Makro Rezepte](Macros_recipes/de.md) aufgelistet sein sollte.

Wenn es ein benutzerdefiniertes Symbol gibt, lade es herunter; klicke mit der rechten Maustaste darauf und wähle `Bild speichern unter...`; platziere das Symbol im Makroverzeichnis. Dieses Symbol kann als Tastaturkürzel für das Makro in einer [benutzerdefinierten Werkzeugleiste](Customize_Toolbars/de.md) verwendet werden. Das Standardsymbol ist <img alt="" src=images/Text-x-python.png  style="width:24px;">.

![](images/Macro_Install_HowTo_28.png ) 
*align=center|Downloading the icon from the macro page*

2\. Wähle auf der Makroseite den Code innerhalb der Abschnitte **Skript** oder **Makro** aus und kopiere ihn.

3\. Öffne in FreeCad das Menü **Makro → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Makros...](Std_DlgMacroExecute/de.md)**, um den [Makro Dialog ausführen](Std_DlgMacroExecute/de.md) zu öffnen.

![](images/Dxf_Importer_Install_01.png ) 
*align=center|Öffnen des Makro ausführen Dialogs*

4\. Klicke **Erstelle**.

![](images/Macro_Install_HowTo_17.png ) 
*align=center|Creating a new macro*

5\. Gib den Makronamen ein, hier `Macro_Apothem_Based_Prism_GUI`, und drücke **OK**.

![](images/Macro_Install_HowTo_18.png ) 
*align=center|Entering the macro name*

6\. Der Makro Editor öffnet sich und zeigt den vollständigen Pfad des neuen Makros an.

![](images/Macro_Install_HowTo_19.png ) 
*align=center|The macro editor*

7\. Füge den Code in das Editorfenster ein und klicke dann auf das Kreuz auf der Registerkarte, um das Fenster zu schließen.

![](images/Macro_Install_HowTo_20.png ) 
*align=center|Closing the macro editor*

8\. Ein Fenster erscheint, das nach Bestätigung zum Speichern des Codes fragt; klicke auf **Ja**. Du kannst auch **Ctrl**+**S** verwenden, um die Datei zu speichern.

Starte FreeCAD neu, um das neue Makro korrekt zu registrieren.

![](images/Macro_Install_HowTo_27.png ) 
*align=center|Asking for confirmation to save the code*

9\. Öffne dann das Menü erneut, **Makro → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Makros...](Std_DlgMacroExecuteDirect/de.md)**, wähle das neue Makro und drücke **Ausführen**.

![](images/Macro_Install_HowTo_21.png ) 
*align=center|Selecting the macro to run it*

10\. Das Makro läuft jetzt. Fülle die Felder mit deinen Werten aus und klicke auf die Schaltfläche **OK**.

![](images/Macro_Install_HowTo_22.png ) 
*align=center|The macro in action; fill in the information and press OK when ready*

11\. Dieses Makro sollte einen Fehler zurückgeben, wenn kein Dokument aktiv ist; andere Makros öffnen ein neues Dokument, wenn keines existiert.

Erstelle ein neues Dokument mit **Datei → <img src="images/Std_New.svg" width=16px>  [Neu](Std_New/de.md)**, und wiederhole dann die vorherigen Schritte, um das Makro auszuführen.

![](images/Macro_Install_HowTo_23.png) 
*align=center|Das Makro gibt einen Fehler zurück, wenn kein Dokument aktiv ist*

12\. Sobald ein aktives Dokument verfügbar ist, wird das Makro ausgeführt und ein Objekt erstellt.

![](images/Macro_Install_HowTo_24.png ) 
*align=center|Vom Makro erzeugtes Objekt*

13\. Du kannst das Makro erneut im Editor öffnen, um es auszuführen oder zu modifizieren. Gehe zu **Makro → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Makros...](Std_DlgMacroExecute/de.md)**, wähle das Makro aus und drücke **Bearbeiten**.

![](images/Macro_Install_HowTo_25.png ) 
*align=center|Öffnen des Makros im Editor*

14\. Das Makro kann nun mit **Makro → <img src="images/Std_DlgMacroExecuteDirect.svg" width=16px> [Makro ausführen](Std_DlgMacroExecute.md)**, oder durch Klicken auf die **<img src="images/Std_DlgMacroExecuteDirect.svg" width=16px> [Ausführen](Std_DlgMacroExecute/de.md)** Taste in der Werkzeugleiste.

![](images/Macro_Install_HowTo_26.png ) 
*align=center|Ausführen des im Editor geladenen Makros*


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### Manuelle Methode 2. Hinzufügen einer Makrodatei aus einer komprimierten .zip-Datei 

Einige Makros sind zu groß, als dass es unbequem ist, sie zu kopieren und in den Makro Editor einzufügen, oder sie können nicht im Wiki beherbergt werden. In diesem Fall kann der Code irgendwo anders beherbergt werden, in einem Github Repositorium oder im [FreeCAD Forum](https://forum.freecadweb.org/). Der Code kann auch in eine `.zip` Datei, einen Tarball `.tar.xz` oder eine andere Art von Archiv komprimiert werden, wenn es mehrere Dateien enthält. Wenn der Code auf diese Weise verteilt wird, sollte das Archiv extrahiert und die Dateien im Makro Verzeichnis abgelegt werden.


<div class="mw-collapsible-content">

Wir werden <img alt="" src=images/Text-x-python.png  style="width:24px;"> [Makro Schrauben Ersteller](Macro_screw_maker1_2.md) als ein Beispiel.

1\. Lade den komprimierten Code aus dem Forum herunter, [Screw Maker](http://forum.freecadweb.org/viewtopic.php?f=22&t=6558#p52887).

Du musst einen Dekompressor verwenden, um die internen Dateien zu erhalten.

-   Für Windows kannst Du ein Programm wie [7-zip](http://www.7-zip.org/) oder [L-Zarc](http://www.kanmandet.dk/?p=37) oder [quickzip](http://www.quickzip.org/quickzip51.html) verwenden.
-   Für Linux kannst Du einen Befehl vom Terminal aus verwenden


```python
unzip your_file.zip -d your_directory
```

2\. Lade das komprimierte Archiv mit dem Makrocode in einen lokalen Ordner herunter.

![](images/Macro_Install_HowTo_01.png ) 
*align=center|Herunterladen des komprimierten Archivs in ein lokales Verzeichnis*

3\. Entpacke die Datei in dem Ordner.

![](images/Macro_Install_HowTo_02.png ) 
*align=center|Entpacken der Datei im Ordner*

4\. Der Entpacker erstellt ein neues Verzeichnis mit den entpackten Dateien.

![](images/Macro_Install_HowTo_03.png ) 
*align=center|Neues Verzeichnis nach dem Entpacken des Archivs erstellt*

5\. Gehe in das neue Verzeichnis und kopiere oder schneide die Makrodatei aus.

![](images/Macro_Install_HowTo_04.png ) 
*align=center|Eingeben des neu erstellten Verzeichnisses mit der entpackten Makrodatei*

6\. Gehe in das Makroverzeichnis und füge die Datei dort ein.

![](images/Macro_Install_HowTo_05.png ) 
*align=center|Platzieren der Makrodatei im Makroverzeichnis*

7\. Öffne in FreeCAD das Menü **Makro → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Makros...](Std_DlgMacroExecute/de.md)**, um den [Makro Dialog ausführen](Std_DlgMacroExecute/de.md) zu öffnen.

![](images/Macro_Install_HowTo_06.png ) 
*align=center|Öffnen des Makro ausführen Dialogs*

8\. Wähle das neue Makro aus und drücke **Ausführen**.

![](images/Macro_Install_HowTo_07.png ) 
*align=center|Auswählen des Makros zur Ausführung*

9\. Das Makro läuft jetzt. Wähle die gewünschten Optionen aus und klicke auf die Schaltfläche **Erstellen**.

<img alt="" src=images/Macro_Install_HowTo_08.png  style="width:640px;"> 
*align=center|Das Makro in Aktion; wähle die gewünschten Optionen und drücke Erstellen, wenn du bereit bist.*

![](images/Macro_Install_HowTo_30.png ) 
*align=center|Vom Makro erzeugtes Objekt*


</div>


</div>



## Ausführen eines Makros in der Kommandozeile 


<div class="toccolours mw-collapsible mw-collapsed">

Kommandozeile ein Makro ausführen (.FCMacro oder .py)


<div class="mw-collapsible-content">

unter Windows


```python
"C:\Program Files\FreeCAD\bin\FreeCAD.exe" "C:\Users\userName\AppData\Roaming\FreeCAD\Mod\WorkFeature\start_WF.FCMacro"
```

unter Linux


```python
todo
```


</div>


</div>



## Fehler in Makros 


<div class="toccolours mw-collapsible mw-collapsed">



### Einrückungsfehler

Der weiße Raum am Anfang der Zeilen (Einrückung) ist in der Programmiersprache [Python](Python/de.md) sehr wichtig und ein integraler Bestandteil des Codes. Ein ungeeignetes Leerzeichen kann dazu führen, dass der Code nicht läuft oder Fehler aufweist.

Dieser Abschnitt beschreibt einige Fehler, die beim Kopieren und Einfügen sowie beim Schreiben von Makrocode auftreten können.


<div class="mw-collapsible-content">

Ein typischer Einrückungsfehler sieht wie folgt aus:


```python
<unknown exception traceback><type 'exceptions.IndentationError'>: ('expected an indented block', ('C:/Users/d/AppData/Roaming/FreeCAD/Macro_Apothem_Based_Prism_GUI.FCMacro', 21, 3, 'def priSm(self):\n'))
```



#### Beispiel 1 

Wenn der Code keine Einrückung aufweist, wird der Code nicht funktionieren. Klassen (`class`) und Funktionsdefinitionen (`def()`), sowie Kontrollstrukturen (`if`, `while`, `for`) sollten von einem Block eingerückten Codes gefolgt werden.

Dieser Fehler ist möglich, wenn der Benutzer den Code nicht korrekt kopiert und alle Leerzeichen versehentlich entfernt wurden.

![](images/Macro_Install_HowTo_09.png ) 
*align=center|Python Code, der keine Einrückung hat; er wird einen Fehler verursachen, wenn er ausgeführt wird*

Einrückungsproblem behoben.

![](images/Macro_Install_HowTo_10.png ) 
*align=center|Python Code mit der richtigen Einrückung*

Wenn der Code ausgewählt ist, sollten alle Zeilen bis zum linken Rand hervorgehoben werden, um anzuzeigen, dass die Zeilen ausgerichtet sind.

![](images/Macro_Install_HowTo_11.png ) 
*align=center|Python Code hervorgehoben, was zeigt, dass alle Zeilen am linken Rand beginnen*



#### Beispiel 2 

Wenn ein zusätzliches Leerzeichen am Anfang aller Zeilen eingefügt, wird der Python Interpreter versagen und sich über unnötige Einrückungen beschweren. In diesem Fall muss in alle Zeilen das anfangs Leerzeichen entfernt werden.

![](images/Macro_Install_HowTo_12.png ) 
*align=center|Python Code mit zusätzlichem Leerzeichen in jeder Zeile*



#### Beispiel 3 

Hier wurde der Code aus einem Foren Thema durch Verwendung **Alles auswählen** Schaltfläche kopiert. Anscheinend ist die Auswahl gut.

![](images/Macro_Install_HowTo_14.png ) 
*align=center|Python Code kopiert aus einem Forum*

Wenn die Auswahl jedoch in den Makro Editor eingefügt wird, scheint es zu einer unerwünschten Einrückung zu kommen.

![](images/Macro_Install_HowTo_15.png ) 
*align=center|Python Code aus einem Forum in den Makro Editor kopiert; unnötige Einrückung wird hinzugefügt*

In this case, the initial spaces need to be removed. This can be done with a specialized text editor to quickly decrease the indentation of the lines.

Unter Windows [Notepad++](http://notepad-plus-plus.org/) kann die Auswahl ausgeführt mit **Alt** + Maus ziehen und dann verwenden **Bearbeiten → Einrücken → Verringere die Einrückung**.

![](images/Macro_Install_HowTo_16.png ) 
*align=center|Python Code mit der korrekten Einrückung*



#### Beispiel 4 

Hier wählt die Auswahl auch die Zeilennummern im Codebeispiel aus. Wenn diese Auswahl in den Makro Editor eingefügt wird, funktioniert sie nicht. Es müssen alle Zeilennummern entfernt und die Leerzeichen so angepasst werden, dass der Python Code die richtige Einrückung hat.

![](images/Macro_Install_HowTo_29.png ) 
*align=center|Auswahl, die auch die Zeilennummern auswählt; wenn dieser Code in den Makro Editor eingefügt wird, wird es nicht funktionieren*



#### Guter Code 

![](images/Macro_Install_HowTo_13.png ) 
*align=center|Python Code mit der richtigen Einrückung*


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### Keine Textausgabe aus Makros 

Makros können Informationen in der Berichtsansicht ausgeben, um zu zeigen, was der Code während der Ausführung tut.

Wenn keine Information angezeigt wird, stelle sicher, dass die Reportansicht und die [Python](Python/de.md) Konsole sichtbar sind und dass die Ausgabe auf die Berichtsansicht gerichtet ist.


<div class="mw-collapsible-content">

#### Printing information 


<div class="mw-translate-fuzzy">

##### Druckinformationen

FreeCAD Makros haben zwei Methoden, um Informationen in die Berichtsansicht zu drucken.


</div>

Die FreeCAD Funktionen


```python
FreeCAD.Console.PrintMessage("Hello World! \n")
FreeCAD.Console.PrintError("Hello World! \n")
FreeCAD.Console.PrintWarning("Hello World! \n")
```

Die einfache Python Funktion


```python
print("Hello World!")
```

#### Enabling the report view 


<div class="mw-translate-fuzzy">

#### Aktivieren der Berichtsansicht 

Um die in der Konsole angezeigten Informationen zu sehen, solltest Du:


</div>

1\. Gehe zum Menü **Ansicht → Paneele**.

![](images/Macro_Install_HowTo_31.png )

![](images/Macro_Install_HowTo_32.png ) 
*align=center|Sichtbarmachung der Panels im Menü Ansicht → Paneele*

2\. Aktiviere die `Berichtansicht` und die `Python Konsole`.

![](images/Macro_Install_HowTo_33.png ) 
*align=center|Aktivieren der Berichtsansicht und der Python Konsole*

3\. Die Bedienfelder sind jetzt sichtbar, und Befehle wie `FreeCAD.Console.PrintMessage()` geben jetzt Informationen aus, die in der `Berichtansicht` angezeigt werden.

![](images/Macro_Install_HowTo_34.png ) 
*align=center|FreeCAD Hauptfenster mit der Berichtsansicht und der Python Konsole*

#### Enabling the print() command 


<div class="mw-translate-fuzzy">

===== Aktivieren des Befehls print() ==== FreeCAD muss möglicherweise so konfiguriert werden, dass die Funktion `print()` von [Python](Python/de.md) seine Ausgabe korrekt in die Berichtsansicht umleitet.


</div>

1\. Gehe in den [Einstellungs Editor](Preferences_Editor/de.md) mit dem Menü **Bearbeiten → Einstellungen**.

![](images/Macro_Install_HowTo_35.png ) 
*align=center|In den Einstellungen Editor gehen*

2\. Gehe zum Abschnitt **Allgemein**, und dann **Ausgabefenster → Python Interpreter**.

![](images/Macro_Install_HowTo_36.png ) 
*align=center|Ausgabefenster Einstellungen*

3\. Beide Kästchen ankreuzen:

-   <img alt="" src=images/Case_a_cocher_O.png  style="width:16px;"> Interne Python Ausgabe in die Berichtsansicht umleiten

-   <img alt="" src=images/Case_a_cocher_O.png  style="width:16px;"> Umleiten interner Python Fehler in die Berichtsansicht

und drücke dann die **OK** Schaltfläche.

![](images/Macro_Install_HowTo_37.png ) 
*align=center|Umleitung der Python-Ausgabe in die Berichtsansicht.*

![](images/Macro_Install_HowTo_38.png ) 
*align=center|Python Befehle zum Drucken von Informationen in die Berichtsansicht.*


</div>


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > How to install macros/de
