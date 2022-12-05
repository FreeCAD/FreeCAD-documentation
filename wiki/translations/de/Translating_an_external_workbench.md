# Translating an external workbench/de
In den folgenden Hinweisen sollte `"context"` der Name Deiner Erweiterung oder Deines Arbeitsbereichs sein, z.B. `"MySuperAddon"` oder `"DraftPlus"`, oder was auch immer. Groß- und Kleinschreibung wird hier unterschieden: So ist z.B. `"Context"` ist nicht dasselbe wie `"context"`. Dieser Zusammenhang sorgt dafür, dass die gesamte Übersetzung des Codes unter demselben Namen zusammengefasst wird, um von den Übersetzern leichter erkannt werden zu können. Das heißt, sie wissen genau, zu welcher Erweiterung oder welchem Arbeitsbereich eine bestimmte Zeichenkette gehört.

**Hinweis**: Hier ist ein Multifunktionsskript, das den kompletten unten beschriebenen Ablauf automatisiert (Es wird trotzdem empfohlen, die Beschreibung zu lesen, um zu wissen, was das Skript erledigen soll): <https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>

## Vorbereiten der Quellen 

### Allgemeines

-   Einen Ordner `translations/` hinzufügen. Dieser kann auch gänzlich anders benannt werden, aber so ist es einfacher, da er in allen Bereichen von FreeCAD gleich ist. In diesem Ordner werden die `.ts`-Dateien (die \"Quell-\"Übersetzungsdateien) und `.qm`-Dateien (kompilierte Übersetzungsdateien) abgelegt.
-   Es sollte nur der Text übersetzt werden, der dem Benutzer in der FreeCAD-Benutzeroberfläche angezeigt wird. Text, der nur in der Python-Konsole angezeigt wird, sollte nicht übersetzt werden.
-   Text, der über `FreeCAD.Console` ausgegeben wird, wird im \"Ausgabefenster\" angezeigt und sollte daher übersetzt werden. Das \"Ausgabefenster\" unterscheidet sich von der Python-Konsole.

### In jeder Python .py-Datei 

-   In jeder Datei, in der Text übersetzt werden soll, braucht man eine definierte `translate()`-Funktion. Sie muss exakt `translate` benannt werden: Der Zeichenkettenausleser hängt von der exakten Benennung ab. Man kann den vollständigen Namen von Qt verwenden, aber die Verwendung des Folgenden ist etwas sauberer:

:   
    
```python
    import FreeCAD
    translate = FreeCAD.Qt.translate
    
```
    

-   Alle Texte, die übersetzt werden sollen, müssen durch die Funktion `translate()` übergeben werden:

:   
    
```python
    print("My text")
    
```
    





:   wird zu:





:   
    
```python
    print(translate("context", "My text"))
    
```
    





:   Man darf nicht vergessen, dass `translate()` nicht nur eine normale Funktion ist, sondern auch als \"Tag\" für das `lupdate` Textverabeitungs-Dienstprogramm dient und deshalb exakt \"translate\" heißen muss. Das Programm `lupdate` ist eine einfache Textverarbeitung; es führt keinen Code aus. Zeichenketteninhalte müssen direkt an die Funktion `translate()` übergeben werden: Es können keine Variablen, Konstanten usw. übergeben werden. Ein Beispiel:





:   
    
```python
    # This works:
    FreeCAD.Console.PrintMessage(translate("context", "My text") + "\n")

    # This does not, lupdate only sees the word "a_variable", and doesn't know what that is:
    a_variable = "My text"
    FreeCAD.Console.PrintMessage(translate("context", a_variable ) + "\n")

    # But this works -- a_variable will contain the translated string:
    a_variable = translate("context", "My text")
    FreeCAD.Console.PrintMessage(a_variable  + "\n")
    
```
    





:   Dies kann überall verwendet werden: In `print()`, in `FreeCAD.Console.PrintMessage()`, in Qt-Dialogen, etc. Die `FreeCAD.Console`-Funktionen fügen das Zeichen für den Zeilenumbruch (`\n`) nicht automatisch hinzu, so dass dieses bei Bedarf am Ende hinzugefügt werden muss. Dieses Zeichen benötigt auch keine Übersetzung, so dass es außerhalb der Übersetzungsfunktion liegen kann:





:   
    
```python
    FreeCAD.Console.PrintMessage(translate("context", "My text") + "\n")
    
```
    

-   Werden `.ui`-Dateien verwendet, die mit dem QtDesigner erstellt wurden, muss nichts Besonderes mit ihnen gemacht werden.
-   Beim Erstellen neuer Objekte darf der \"Name\" des Objekts nicht übersetzt werden. Übersetzt wird vielmehr die \"Benennung\" (das Label) des Objekts. Der Unterschied besteht darin, dass ein \"Name\" einzigartig ist; er bleibt über die gesamte Lebensdauer des Objekts derselbe; andererseits kann eine \"Benennung\" vom Benutzer beliebig geändert werden.
-   Wenn man Eigenschaften für eigene Objekte erstellt, werden die Namen der Eigenschaften nicht übersetzt. Aber die Beschreibung wird in `QT_TRANSLATE_NOOP` eingebettet:

:   
    
```python
    obj.addProperty("App::PropertyBool", "MyProperty", "PropertyGroup", QT_TRANSLATE_NOOP("App::Property", "This is what My Property does"))
    
```
    





:   Man verwendet in diesem speziellen Fall keinen eigenen `"context"`, sondern behält `"App::Property"` bei.

### In InitGui.py 

-   Die folgende Zeile im oberen Bereich der Datei hinzufügen:

:   
    
```python
    def QT_TRANSLATE_NOOP(context, text):
        return text
    
```
    





:   Das Makro `QT_TRANSLATE_NOOP` macht nichts außer, dass es Texte markiert, die später vom Dienstprogramm `lupdate` aufgesammelt werden. Es wird nur in Sonderfällen verwendet, in denen sich FreeCAD selbst um alles kümmert.

-   Um Namen von Menüs und Symboleisten zu übersetzen, verwendet man das Wort `"Workbench"` als Kontext:

:   
    
```python
    self.appendMenu(QT_TRANSLATE_NOOP("Workbench", "My menu"), [list of commands, ...])
    self.appendToolbar(QT_TRANSLATE_NOOP("Workbench", "My toolbar"), [list of commands, ...])
    
```
    

-   Den Pfad zum eigenen Ordner `translations/` in der Initialisierten Funktion hinzufügen:

:   
    
```python
    FreeCADGui.addLanguagePath("/path/to/translations")
    
```
    

Die Datei {`InitGui.py`} hat kein Attribut **file**, so dass es nicht einfach ist, die relative Position des Übersetzungsordners zu finden. Eine einfache Möglichkeit, dies zu umgehen, besteht darin, eine andere Datei aus demselben Ordner zu importieren und in dieser Datei Folgendes zu tun:

:   
    
```python
    FreeCADGui.addLanguagePath(os.path.join(os.path.dirname(__file__), "translations"))
    
```
    

### Innerhalb jeder FreeCAD-Befehlsklasse 

-   Folgende Zeile am Anfang der Datei hinzufügen:

:   
    
```python
    def QT_TRANSLATE_NOOP(context, text):
        return text
    
```
    

-    `'MenuText'`und `'Tooltip'` des Befehls übersetzt man wie folgt:

:   
    
```python
    def GetResources(self):
        return {'Pixmap'  : "path/to/icon.svg"),
                'MenuText': QT_TRANSLATE_NOOP("CommandName", "My Command"),
                'ToolTip' : QT_TRANSLATE_NOOP("CommandName", "Describes what the command does"),
                'Accel'   : "Shift+A"
        }
    
```
    





:   wobei {`"CommandName"`} der Name des Befehls ist, definiert durch:





:   
    
```python
    FreeCADGui.addCommand('CommandName', My_Command_Class())
    
```
    

## Alle Zeichenketten des eigenen Moduls sammeln 

-   Die Werkzeuge `lupdate`, `lconvert`, `lrelease` und `pylupdate` müssen auf dem eigenen System installiert sein. In Linux-Distributionen sind sie in der Regel in Paketen mit den Namen `pyside-tools` oder `pyside2-tools` enthalten. Auf einigen Systemen wird `lupdate` auch `lupdate4`, `lupdate5`,`lupdateqt4` oder ähnlich genannt. Das Gleiche gilt für die anderen Werkzeuge. Die Versionen Qt4 oder Qt5 können nach Wahl verwendet werden. In Qt6 gibt es kein eigenständiges Übersetzungssystem für Python-Dateien, `lupdate` wird zum Extrahieren der Zeichenketten aus allen Arten von Quelldateien verwendet.
-   Sind `.ui`-Dateien vorhanden, muss zuerst `lupdate` ausgeführt werden:

:   
    
```python
    lupdate *.ui -ts translations/uifiles.ts
    
```
    





:   Dies ist rekursiv und findet `.ui`-Dateien in der gesamten Verzeichnisstruktur.

-   Sind `.py`-Dateien vorhanden, muss auch `pylupdate` ausgeführt werden:

:   
    
```python
    pylupdate *.py -ts translations/pyfiles.ts
    
```
    

-   Wurden beide Operationen ausgeführt, müssen nun die beiden Dateien zu einer einzigen zusammengefeasst werden:

:   
    
```python
    lconvert -i translations/uifiles.ts translations/pyfiles.ts -o translations/MyModule.ts
    
```
    

-   Die Inhalte der drei `.ts`-Dateien überprüfen, um sicherzustellen, dass sie die Zeichenketten enthalten, danach können `pyfiles.ts` und `uifiles.ts` gelöscht werden.
-   Das alles kann auch mit einem Bash-Skript wie diesem ausgeführt werden:

:   
    
```python
    #!/bin/sh
    lupdate *.ui -ts translations/uifiles.ts
    pylupdate *.py -ts translations/pyfiles.ts
    lconvert -i translations/uifiles.ts translations/pyfiles.ts -o translations/MyModule.ts
    rm translations/pyfiles.ts
    rm translations/uifiles.ts
    
```
    

## Sende die .ts Datei an eine Übersetzungsplattform 

Es ist an der Zeit, die {`.ts`}-Datei übersetzen zu lassen. Dafür kann man ein Konto auf einer öffentlichen Übersetzungsplattform wie [Crowdin](https://crowdin.com/) oder [Transifex](https://www.transifex.com/) einrichten, oder unser bestehendes [FreeCAD-Addons-Konto bei Crowdin](https://crowdin.com/project/freecad-addons) nutzen, das bereits viele Benutzer hat und somit eine größere Chance, die Datei schnell übersetzen zu lassen, von Leuten, die FreeCAD kennen.

Soll die Datei auf dem FreeCAD-Crowdin-Konto untergebracht werden, hilft [Yorik](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68) im [FreeCAD-Forum](https://forum.freecadweb.org/) gerne weiter.


**Hinweis:**

Einige Plattformen wie Crowdin können sich in GitHub integrieren und den gesamten Prozess von Punkt 2, 3 und 4 automatisch durchführen. Dafür kann das FreeCAD-Crowdin-Konto nicht verwendet werden; Man muss sein eigenes Konto einrichten.

## Übersetzungen zusammenführen 

Sobald deine `.ts` Datei übersetzt wurde, wenn auch nur teilweise, kannst du die Übersetzungen von der Internetseite herunterladen:

-   Du wirst normalerweise eine `.zip` Datei herunterladen, die eine `.ts` pro Sprache enthält.
-   Platziere alle übersetzten `.ts` Dateien zusammen mit Deiner Basisdatei `.ts` im `translations/` Ordner.

## Kompiliere die Übersetzungen 

Nun wird das Programm `lrelease` auf jede vorhandene Datei angewendet:


```python
lrelease "translations/Draft_de.ts"
lrelease "translations/Draft_fr.ts"
lrelease "translations/Draft_pt-BR.ts"
```

Der Prozess lässt sich automatisieren:


```python
for f in translations/*_*.ts
do
    lrelease "translations/$f"
done
```

Es sollte jetzt eine `.qm`-Datei für jede übersetzte `.ts`-Datei vorhanden sein. Die `.qm`-Dateien sind die, die von Qt und FreeCAD zur Laufzeit verwendet werden.

Das ist alles, was gebraucht wird. Man beachte, dass bestimmte Teile des eigenen Arbeitsbereichs nicht sofort übersetzt werden können, wenn man sich für einen Wechsel der Sprache entscheidet. In diesem Fall muss FreeCAD neu gestartet werden, damit die neue Sprache verwendet wird.

## Übersetzungen testen 

1.  In FreeCAD zu einer Sprache wechseln, die man übersetzt hat (z.B. Deutsch)
2.  Die Übersetzung in FreeCAD laden, z.B. `FreeCADGui.addTranslationPath("/Pfad/zum/Verzeichnis/mit/qmfile")`
3.  Eine Zeichenkette testen, z.B. `FreeCAD.Qt.translate("dein Kontext","Eine Zeichenkette")`

Ergebnis: Dies sollte die deutsche Übersetzung liefern. Wenn das funktioniert, ist die Basiseinstellung OK. Dann können wir uns etwas anderes ansehen. Beispielsweise sollten Befehlsnamen einen speziellen Kontext benutzen, das ist der in FreeCAD eingetragene Befehlsname.

### Wichtige Hinweise 

-   Stelle sicher, dass du einen \*context\* und \*string\* verwendest, der tatsächlich in der ts/qm-Datei vorhanden ist.

## Convenience script 

Yorik maintains a convenience script for the BIM workbench, that can gather, upload and download ts files. You can just copy and adapt that script for your workbench:

<https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>

## Technical details and advanced usage 

In the above examples there are two separate functions being used: `translate()` and `QT_TRANSLATE_NOOP`. You may also run across `tr()` and `QT_TR_NOOP`, which automatically provide the \"context\" argument based on their calling location. These two pairs of functions are fundamentally different.


`translate()`

and `tr()` accomplish two separate tasks: at runtime they perform the actual translation from the string passed into them to the final translated string. This is true whether they are provided a literal string, or a variable, or a constant: the lookup is dynamic and real-time during the run of the code. However, they provide an additional non-runtime function: they are recognized by the `pylupdate` utility. If (and only if) they contain a string literal, that literal is extracted by the utility. ONLY string literals are extracted by `pylupdate` \-- if a variable is passed it is ignored by the `pylupdate` utility. Qt will attempt to provide a translation at runtime, but this will only work if some other piece of code called one of the translation functions with the literal string that needs to be translated, so that `pylupdate` can extract it. Note that the code with the string literal need not actually ever execute, it must simply exist as a line of code in a file somewhere: `pylupdate` performs no analysis or code execution, it is simply performing a string search and extraction.

In contrast, `QT_TRANSLATE_NOOP` and `QT_TR_NOOP` do nothing at all at runtime: they are literal \"no-ops\", and are completely ignored by running code. Their only use is to mark a literal string for extraction by `pylupdate`: it never makes sense to place a variable within a call to one of these functions, it will have no effect. They are used in circumstances where `translate()` or `tr()` will be called with a variable containing the text to translate. For example, any code that is used to create a Command or a Property will use a NOOP-type function around the command menu text or tooltip, or the property docstring: at runtime when FreeCAD displays these items to the user it calls `translate()`: the literal strings must have been extracted by `pylupdate` at the point of creation, for example:


```python
def GetResources(self):
    return {'Pixmap'  : "path/to/icon.svg",
            'MenuText': QT_TRANSLATE_NOOP("CommandName", "My Command"),
            'ToolTip' : QT_TRANSLATE_NOOP("CommandName", "Describes what the command does"),
            'Accel'   : "Shift+A"
    }
```

In this usage, at runtime the dictionary returned by this function is literally:


```python
{ 
    'Pixmap'  : "path/to/icon.svg",
    'MenuText': "My Command",
    'ToolTip' : "Describes what the command does",
    'Accel'   : "Shift+A"
}
```

There is no reference to any type of translation information. When FreeCAD actually displays this information to the user, the pseudo-code is:


```python
for command in commands:
    resources = command.GetResources()
    menu_text = translate(resources['MenuText'])
```

In this case, `lupdate` cannot extract any string from the call to `translate()` because it refers to a variable. So `lupdate` ignores that call, but at runtime Qt searches for the string that\'s passed to it. As long as someplace in the code there is a call to one of the translation functions with a matching literal string (in this case, in the `GetResources()` function), this translation call will succeed.

To verify that the expected strings are being extracted, you can manually run the `pylupdate` command:


```python
pylupdate myfile.py -ts outfile.ts
```

The file `outfile.ts` will contain the set of strings that are uploaded to CrowdIn for translation.

## Wichtige Verweise 

-   Warum und wie man `openCommand()` Funktionen übersetzen sollte ([forum thread](https://forum.freecadweb.org/viewtopic.php?f=10&t=55869))

## Verwandte Seiten 

-   [Externe Arbeitsbereiche](External_workbenches/de.md)
-   [Lokalisierung](Localisation/de.md)
-   Eigene Anfragen nach weitere Informationen können hier gestellt werden:[Translating external workbenches](https://forum.freecadweb.org/viewtopic.php?f=10&t=36413) (engl.).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Translating an external workbench/de
