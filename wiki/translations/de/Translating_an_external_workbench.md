# Translating an external workbench/de
In den folgenden Hinweisen sollte `"context"` der Name Deiner Erweiterung oder Deines Arbeitsbereichs sein, z.B. `"MySuperAddon"` oder `"DraftPlus"`, oder was auch immer. Dieser Kontext macht es so, dass die gesamte Übersetzung deines Codes unter dem gleichen Namen zusammengefasst wird, um von den Übersetzern leichter identifiziert werden zu können. Das heißt, sie wissen genau, zu welcher Erweiterung oder welchem Arbeitsbereich eine bestimmte Zeichenkette gehört.

**Hinweis**: Hier ist ein Multifunktionsskript, das den kompletten unten beschriebenen Ablauf automatisiert (es wird angeraten, dass du trotzdem die Beschreibung liest, um zu wissen, was das Skrikt sollte): <https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>

## Vorbereiten der Quellen 

### Allgemeines

-   Füge einen Ordner {`translations/`} hinzu. Du kannst es nach etwas anderem benennen, aber das wird einfacher sein, da es in FreeCAD gleich ist. In diesem Ordner werden die Dateien `.ts` (die \"Quell\" Übersetzungsdateien) und {`.qm`} Dateien (kompilierte Übersetzungsdateien) abgelegt.
-   Es sollte nur der Text übersetzt werden, der dem Benutzer in der FreeCAD Benutzeroberfläche angezeigt wird. Text, der nur in der Python Konsole angezeigt wird, sollte nicht übersetzt werden.
-   Text, der auf die `FreeCAD.Console` gedruckt wird, wird in der \"Reportansicht\" angezeigt und sollte daher übersetzt werden. Die \"Reportansicht\" unterscheidet sich von der Python Konsole.

### In jeder Python .py-Datei 


<div class="mw-translate-fuzzy">

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


</div>


:   
    
```python
    import FreeCAD
    translate = FreeCAD.Qt.translate
    
```
    

-   All text that must be translated must be passed through the `translate()` function:

:   
    
```python
    print("My text")
    
```
    





:   becomes:





:   
    
```python
    print(translate("context", "My text"))
    
```
    





:   Be aware that `translate()` is not just a normal function: it also serves as a \"tag\" for the `lupdate` text-processing utility, so must be named exactly \"translate\". The `lupdate` program is a simple text processor, it does not execute your code. You must pass string literals directly to the `translate()` function: you cannot pass variables, constants, etc. For example:





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
    


<div class="mw-translate-fuzzy">

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


</div>


:   
    
```python
    FreeCAD.Console.PrintMessage(translate("context", "My text") + "\n")
    
```
    

-   If you are using `.ui` files made with QtDesigner, nothing special needs to be done with them.
-   When creating new objects, do not translate the object\'s \"Name\". Rather, translate the object\'s \"Label\". The difference is that a \"Name\" is unique; it stays the same throughout the life of the object; on the other hand, a \"Label\" can be changed by the user as desired.
-   When creating properties for your objects, don\'t translate the property name. But place the description inside `QT_TRANSLATE_NOOP`:

:   
    
```python
    obj.addProperty("App::PropertyBool", "MyProperty", "PropertyGroup", QT_TRANSLATE_NOOP("App::Property", "This is what My Property does"))
    
```
    





:   Don\'t use your own `"context"` in this specific case. Keep `"App::Property"`.

-   Do not translate the text of document transactions made with `Document.openTransaction()`

### In InitGui.py 


<div class="mw-translate-fuzzy">

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
</div>

: 
```python
def QT_TRANSLATE_NOOP(scope, text):
    return text
```

* To translate menu names:

: 
```python
self.appendMenu(QT_TRANSLATE_NOOP("context", "My menu"), [list of commands, ...])
```

* The `QT_TRANSLATE_NOOP` macro doesn't do anything, but it marks texts to be picked up by the `lupdate` utility later on. Since it doesn't actually do anything, we only use it in special cases where FreeCAD itself takes care of everything.
* Add the path to your `translations/` folder in the Initialized function:

: 
```python
FreeCADGui.addLanguagePath("/path/to/translations")
```

: The `InitGui.py` file has no '''file''' attribute, so it is not easy to find the translations folder's relative location. An easy way to work around this is to make it import another file from the same folder, and in that file do:

: 
```python
FreeCADGui.addLanguagePath(os.path.join(os.path.dirname(__file__), "translations"))
```

=== Innerhalb jeder FreeCAD-Befehlsklasse ===

<div class="mw-translate-fuzzy">
* Füge die folgende Zeile hinzu, die sich am Anfang der Datei befindet:
{{Code|code|code=
def QT_TRANSLATE_NOOP(Kontext, Text):
     return text
}}
* Übersetze den {`'MenuText'`} und {`'Tooltip'`} des Befehls wie folgt:


</div>


:   
    
```python
    def QT_TRANSLATE_NOOP(context, text):
        return text
    
```
    

-   Translate the `'MenuText'` and `'Tooltip'` of the command like this:

:   
    
```python
    def GetResources(self):
        return {'Pixmap'  : "path/to/icon.svg"),
                'MenuText': QT_TRANSLATE_NOOP("CommandName", "My Command"),
                'ToolTip' : QT_TRANSLATE_NOOP("CommandName", "Describes what the command does"),
                'Accel'   : "Shift+A"
        }
    
```
    


<div class="mw-translate-fuzzy">

wobei {`"CommandName"`} der Name des Befehls ist, definiert durch {{Code|code|code=
FreeCADGui.addCommand('CommandName', My_Command_Class())
}}


</div>


:   
    
```python
    FreeCADGui.addCommand('CommandName', My_Command_Class())
    
```
    

## Sammle alle Zeichenketten von deinem Modul 


<div class="mw-translate-fuzzy">

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


</div>


:   
    
```python
    lupdate *.ui -ts translations/uifiles.ts
    
```
    





:   This is recursive and will find `.ui` files inside your whole directory structure.

-   If you have `.py` files, you need to run `pylupdate` too:

:   
    
```python
    pylupdate *.py -ts translations/pyfiles.ts
    
```
    

-   If you ran both operations, you now need to unify these two files into one:

:   
    
```python
    lconvert -i translations/uifiles.ts translations/pyfiles.ts -o translations/MyModule.ts
    
```
    

-   Check the contents of the three `.ts` files to make sure that they contain the strings, then you can delete both `pyfiles.ts` and `uifiles.ts`.
-   You can do it all in one bash script like this:

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

Es ist an der Zeit, Deine {`.ts`} Datei übersetzen zu lassen. Du kannst ein Konto auf einer öffentlichen Übersetzungsplattform wie [Crowdin](https://crowdin.com/) oder [Transifex](https://www.transifex.com/) einrichten, oder Du kannst von unserem bestehenden [FreeCAD-Addons-Konto bei Crowdin](https://crowdin.com/project/freecad-addons) profitieren, das bereits viele Benutzer hat und somit die Chance hat, Deine Datei schnell und von Leuten, die FreeCAD kennen, übersetzen zu lassen.

Wenn Du Deine Datei auf dem FreeCAD Crowdin Konto unterbringen möchtest, wende Dich an [Yorik](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68) im [FreeCAD-Forum](https://forum.freecadweb.org/).


<div class="mw-translate-fuzzy">


**Note:**

Einige Plattformen wie Crowdin können sich in GitHub integrieren und den gesamten Prozess von Punkt 2, 3 und 4 automatisch durchführen. Dazu kannst Du das FreeCAD Crowdin Konto nicht verwenden; Du musst Dein eigenes Konto einrichten.


</div>

## Übersetzungen zusammenführen 

Sobald deine `.ts` Datei übersetzt wurde, wenn auch nur teilweise, kannst du die Übersetzungen von der Internetseite herunterladen:

-   Du wirst normalerweise eine `.zip` Datei herunterladen, die eine `.ts` pro Sprache enthält.
-   Platziere alle übersetzten `.ts` Dateien zusammen mit Deiner Basisdatei `.ts` im `translations/` Ordner.

## Kompiliere die Übersetzungen 


<div class="mw-translate-fuzzy">

Führe nun das `lrelease` Programm auf jede Datei aus, die Du hast.


</div>


```python
lrelease "translations/Draft_de.ts"
lrelease "translations/Draft_fr.ts"
lrelease "translations/Draft_pt-BR.ts"
```


<div class="mw-translate-fuzzy">

Du kannst den Prozess automatisieren.


</div>


```python
for f in translations/*_*.ts
do
    lrelease "translations/$f"
done
```

Du solltest eine `.qm` Datei für jede übersetzte `.ts` Datei finden. Die `.qm` Dateien sind das, was von Qt und FreeCAD zur Laufzeit verwendet wird.

Das ist alles, was du brauchst. Beachte, dass bestimmte Teile Deines Arbeitsbereichs nicht sofort übersetzt werden können, wenn Du dich für einen Sprachenwechsel entscheidest. Wenn dies der Fall ist, musst Du FreeCAD neu starten, damit die neue Sprache wirksam wird.

## Übersetzungen testen 


<div class="mw-translate-fuzzy">

1.  Wechsle in FreeCAD zu einer Sprache, in die du übersetzt hast (z.B. Deutsch)
2.  Lade die Übersetzung in FreeCAD, z.B. `FreeCADGui.addTranslationPath("/Pfad/zum/Verzeichnis/mit/qmfile")`
3.  Teste etwas, z.B. `FreeCAD.Qt.translate("dein Kontext","etwas Text")`


</div>


<div class="mw-translate-fuzzy">

Ergebnis: Dies sollte die deutsche Übersetzung liefern. Wenn das funktioniert, ist die Basiseinstellung OK. Dann können wir etwas anderes ansehen. Bspw. sollten Befehlsnamen einen speziellen Kontext benutzen, das ist der in FreeCAD eingetragene Befehlsname.


</div>

### Wichtige Anmerkungen 

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

## Related Pages 


<div class="mw-translate-fuzzy">

## Verwandte Seiten 

-   [Externe Arbeitsbereiche](External_workbenches/de.md)
-   [Lokalisierung](Localisation/de.md)
-   Für weitere Informationen stelle deine Anfragen hier [Übersetzen externer Arbeitsbereiche](https://forum.freecadweb.org/viewtopic.php?f=10&t=36413)


</div>




_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Translating an external workbench/de
