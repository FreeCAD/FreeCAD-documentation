# Translating an external workbench/de
In den folgenden Hinweisen sollte `"context"` der Name Deiner Erweiterung oder Deines Arbeitsbereichs sein, z.B. `"MySuperAddon"` oder `"DraftPlus"`, oder was auch immer. Dieser Kontext macht es so, dass die gesamte Übersetzung deines Codes unter dem gleichen Namen zusammengefasst wird, um von den Übersetzern leichter identifiziert werden zu können. Das heißt, sie wissen genau, zu welcher Erweiterung oder welchem Arbeitsbereich eine bestimmte Zeichenkette gehört.

**Hinweis**: Hier ist ein Multifunktionsskript, das den kompletten unten beschriebenen Ablauf automatisiert (es wird angeraten, dass du trotzdem die Beschreibung liest, um zu wissen, was das Skrikt sollte): <https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>

## Vorbereiten der Quellen 

### Allgemeines

-   Füge einen Ordner {`translations/`} hinzu. Du kannst es nach etwas anderem benennen, aber das wird einfacher sein, da es in FreeCAD gleich ist. In diesem Ordner werden die Dateien `.ts` (die \"Quell\" Übersetzungsdateien) und {`.qm`} Dateien (kompilierte Übersetzungsdateien) abgelegt.
-   Es sollte nur der Text übersetzt werden, der dem Benutzer in der FreeCAD Benutzeroberfläche angezeigt wird. Text, der nur in der Python Konsole angezeigt wird, sollte nicht übersetzt werden.
-   Text, der auf die `FreeCAD.Console` gedruckt wird, wird in der \"Reportansicht\" angezeigt und sollte daher übersetzt werden. Die \"Reportansicht\" unterscheidet sich von der Python Konsole.

### In jeder Python .py-Datei 

-   In jeder Datei, in der Du Text übersetzen musst, musst Du eine `translate()` Funktion definieren. Eine einfache Möglichkeit ist die Verwendung derjenigen aus dem [Entwurf Arbeitsbereich](Draft_Workbench/de.md):


```python
from DraftTools import translate
```

Ab FreeCAD 0.19 definiert das FreeCAD-Modul auch eine translate()-Funktion, es ist am besten, diese zu verwenden: 
```python
from FreeCAD.Qt import translate
```

-   Alle zu übersetzenden Texte müssen über die Funktion {`translate()`} übergeben werden.


```python
print("Mein Text")
```

wird zu 
```python
print(translate("context", "My text"))
```

Dies kann überall verwendet werden: in `print()`, in `FreeCAD.Console.PrintMessage()`}, in Qt Dialogen, etc. Die Funktionen `FreeCAD.Console` fügen das Zeilenumbruchzeichen (`\n`) nicht automatisch hinzu, so dass dieses bei Bedarf am Ende hinzugefügt werden muss. Dieses Zeichen benötigt auch keine Übersetzung, so dass es außerhalb der Übersetzungsfunktion liegen kann: {{Code|code|code=
FreeCAD.Console.PrintMessage(translate("context", "My text") + "\n")
}}

-   Wenn Du {`.ui`} Dateien verwendest, die mit dem QtDesigner erstellt wurden, muss nichts Besonderes mit ihnen gemacht werden.
-   Beim Erstellen neuer Objekte darf der \"Name\" des Objekts nicht übersetzt werden. Übersetze vielmehr die \"Beschriftung\" des Objekts. Der Unterschied besteht darin, dass ein \"Name\" einzigartig ist; er bleibt über die gesamte Lebensdauer des Objekts gleich; andererseits kann eine \"Beschriftung\" vom Benutzer beliebig geändert werden.
-   Wenn Sie Eigenschaften für deine Objekte erstellst, übersetze den Eigenschaftsnamen nicht. Aber platziere die Beschreibung in {`QT_TRANSLATE_NOOP`}:


{{Code|code|code=
obj.addProperty("App::PropertyBool", "MyProperty", "PropertyGroup", QT_TRANSLATE_NOOP((("App::Property", "Das ist es, was meine Eigenschaft tut"))))
}}

Verwende in diesem speziellen Fall nicht Deine eigenen {`"context"`}. Behalte {`"App::Property"`}.

-   Übersetze nicht den Text von Dokumenttransaktionen, die mit {`Document.openTransaction()`} durchgeführt wurden.{

### In InitGui.py 

-   Füge die folgende Zeile hinzu, die sich am Anfang der Datei befindet:


{{Code|code|code=
def QT_TRANSLATE_NOOP(Umfang, Text):
    Rückgabewert
}}

-   Um Menünamen zu übersetzen:


{{Code|code|code=
self.appendMenu(QT_TRANSLATE_NOOP("context", "My menu"), [list of commands, ....]))
}}

-   Das Makro {`QT_TRANSLATE_NOOP`} macht nichts, aber es markiert Texte, die später vom Dienstprogramm `lupdate`} aufgenommen werden. Da es eigentlich nichts bewirkt, verwenden wir es nur in Sonderfällen, in denen FreeCAD sich selbst um alles kümmert.
-   Füge den Pfad zu deinem Ordner `translations/` in der Funktion Initialized hinzu:


{{Code|code|code=
FreeCADGui.addLanguagePath("/path/to/translations")
}}

Die Datei {`InitGui.py`} hat kein Attribut **file**\', so dass es nicht einfach ist, die relative Position des Übersetzungsordners zu finden. Eine einfache Möglichkeit, dies zu umgehen, besteht darin, dass es eine andere Datei aus dem gleichen Ordner importiert und in dieser Datei Folgendes tut {{{Code|code|code=
FreeCADGui.addLanguagePath(os.path.join(os.path.dirname(((__file__), "translations")))
}}

=== Innerhalb jeder FreeCAD-Befehlsklasse ===

* Füge die folgende Zeile hinzu, die sich am Anfang der Datei befindet:
{{Code|code|code=
def QT_TRANSLATE_NOOP(Kontext, Text):
     return text
}}
* Übersetze den {`'MenuText'`} und {`'Tooltip'`} des Befehls wie folgt:


```python
def GetResources(self):
    return {'Pixmap'  : "path/to/icon.svg"),
            'MenuText': QT_TRANSLATE_NOOP("CommandName", "My Command"),
            'ToolTip' : QT_TRANSLATE_NOOP("CommandName", "Describes what the command does"),
            'Accel'   : "Shift+A"
    }
```

wobei {`"CommandName"`} der Name des Befehls ist, definiert durch {{Code|code|code=
FreeCADGui.addCommand('CommandName', My_Command_Class())
}}

## Sammle alle Zeichenketten von deinem Modul 

-   Du benötigst die {`lupdate`}, {`lconvert`}, {`lrelease`} und {`pylupdate`} Werkzeuge auf Deinem System. In Linux Distributionen gibt es sie in der Regel in Paketen mit den Namen {`pyside-tools`} oder {`pyside2-tools`}. Auf einigen Systemen wird {`lupdate`} `lupdate4` oder {`lupdate5`} oder {`lupdateqt4`} oder ähnlich genannt. Das Gleiche gilt für die anderen Werkzeuge. Du kannst die Qt4- oder Qt5 Version nach Wahl verwenden.
-   Wenn du {`.ui`} Dateien hast, musst du sie zuerst {`lupdate`} ausführen:


{{Code|code|code=
lupdate *.ui -ts Übersetzungen/uifiles.ts
}}

Dies ist rekursiv und findet {`.ui`} Dateien in deiner gesamten Verzeichnisstruktur.

-   Wenn du {`.py`} Dateien hast, musst du sie auch {`pylupdate`} ausführen:


{{Code|code|code=
pylupdate *.py -ts Übersetzungen/Pyfiles.ts
}}

-   Wenn Du beide Operationen ausgeführt hast, musst Du nun diese beiden Dateien zu einer einzigen vereinheitlichen:


{{Code|code|code=
lconvert -i Übersetzungen/uifiles.ts Übersetzungen/Pyfiles.ts -o Übersetzungen/MyModule.ts
}}

-   Überprüfe den Inhalt der drei `.ts` Dateien, um sicherzustellen, dass sie die Zeichenketten enthalten, dann kannst Du sowohl `pyfiles.ts` als auch {`uifiles.ts`} löschen.
-   Du kannst alles in einem Bash Skript wie diesem machen:


```python
#!/bin/sh
lupdate *.ui -ts translations/uifiles.ts
pylupdate *.py -ts translations/pyfiles.ts
lconvert -i translations/uifiles.ts translations/pyfiles.ts -o translations/MyModule.ts
rm translations/pyfiles.ts
rm translations/uifiles.ts
```

## Sende die .ts Datei an eine Übersetzungsplattform 

Es ist an der Zeit, Deine {`.ts`} Datei übersetzen zu lassen. Du kannst ein Konto auf einer öffentlichen Übersetzungsplattform wie [Crowdin](https://crowdin.com/) oder [Transifex](https://www.transifex.com/) einrichten, oder Du kannst von unserem bestehenden [FreeCAD-Addons-Konto bei Crowdin](https://crowdin.com/project/freecad-addons) profitieren, das bereits viele Benutzer hat und somit die Chance hat, Deine Datei schnell und von Leuten, die FreeCAD kennen, übersetzen zu lassen.

Wenn Du Deine Datei auf dem FreeCAD Crowdin Konto unterbringen möchtest, wende Dich an [Yorik](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68) im [FreeCAD-Forum](https://forum.freecadweb.org/).


**Note:**

Einige Plattformen wie Crowdin können sich in GitHub integrieren und den gesamten Prozess von Punkt 2, 3 und 4 automatisch durchführen. Dazu kannst Du das FreeCAD Crowdin Konto nicht verwenden; Du musst Dein eigenes Konto einrichten.

## Übersetzungen zusammenführen 

Sobald deine `.ts` Datei übersetzt wurde, wenn auch nur teilweise, kannst du die Übersetzungen von der Internetseite herunterladen:

-   Du wirst normalerweise eine `.zip` Datei herunterladen, die eine `.ts` pro Sprache enthält.
-   Platziere alle übersetzten `.ts` Dateien zusammen mit Deiner Basisdatei `.ts` im `translations/` Ordner.

## Kompiliere die Übersetzungen 

Führe nun das `lrelease` Programm auf jede Datei aus, die Du hast. 
```python
lrelease "translations/Draft_de.ts"
lrelease "translations/Draft_fr.ts"
lrelease "translations/Draft_pt-BR.ts"
```

Du kannst den Prozess automatisieren. 
```python
for f in translations/*_*.ts
do
    lrelease "translations/$f"
done
```

Du solltest eine `.qm` Datei für jede übersetzte `.ts` Datei finden. Die `.qm` Dateien sind das, was von Qt und FreeCAD zur Laufzeit verwendet wird.

Das ist alles, was du brauchst. Beachte, dass bestimmte Teile Deines Arbeitsbereichs nicht sofort übersetzt werden können, wenn Du dich für einen Sprachenwechsel entscheidest. Wenn dies der Fall ist, musst Du FreeCAD neu starten, damit die neue Sprache wirksam wird.

## Übersetzungen testen 

1.  Wechsle in FreeCAD zu einer Sprache, in die du übersetzt hast (z.B. Deutsch)
2.  Lade die Übersetzung in FreeCAD, z.B. `FreeCADGui.addTranslationPath("/Pfad/zum/Verzeichnis/mit/qmfile")`
3.  Teste etwas, z.B. `FreeCAD.Qt.translate("dein Kontext","etwas Text")`

Ergebnis: Dies sollte die deutsche Übersetzung liefern. Wenn das funktioniert, ist die Basiseinstellung OK. Dann können wir etwas anderes ansehen. Bspw. sollten Befehlsnamen einen speziellen Kontext benutzen, das ist der in FreeCAD eingetragene Befehlsname.

### Wichtige Anmerkungen 

-   Stelle sicher, dass du einen \*context\* und \*string\* verwendest, der tatsächlich in der ts/qm-Datei vorhanden ist.

## Convenience script 

Yorik maintains a convenience script for the BIM workbench, that can gather, upload and download ts files. You can just copy and adapt that script for your workbench:

<https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>

## Wichtige Verweise 

-   Warum und wie man `openCommand()` Funktionen übersetzen sollte ([forum thread](https://forum.freecadweb.org/viewtopic.php?f=10&t=55869))

## Verwandte Seiten 

-   [Externe Arbeitsbereiche](External_Workbenches/de.md)
-   [Lokalisierung](Localisation/de.md)
-   Für weitere Informationen stelle deine Anfragen hier [Übersetzen externer Arbeitsbereiche](https://forum.freecadweb.org/viewtopic.php?f=10&t=36413)


 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Translating an external workbench/de
