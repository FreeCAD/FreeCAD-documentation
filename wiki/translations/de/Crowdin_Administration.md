# Crowdin Administration/de
{{TOCright}}

## Rollen

-   Übersetzer/in
    -   Kann Übersetzungen in einer Sprache vorschlagen und darüber abstimmen.
    -   Kann Zusammenhänge/Verständlichkeit erfragen, Fehler in der zu übersetzenden Passage melden, einen aktuellen Übersetzungsbeitrag diskutieren, etc\...

-   Korrekturleser/in
    -   Verwaltet die Übersetzungen, die Übersetzer vorgeschlagen/erstellt haben. Die Übersetzung wird von der Korrekturleser/in akzeptiert/zurückgewiesen.
    -   Ein weiterer Schritt wird benötigt, um die abschließende Bestätigung zu erteilen. Weil die \'Bestätigung\' einer Übersetzung ein erneutes Lesen und das Setzen eines Kontrollvermerks erfordert, bietet es eine Art von \"Qualitätssicherungsebene\". Sobald eine Übersetzung bestätigt wurde, wird die Zeichenkette grün markiert und der grüne Anteil des Statusbalkens der Sprache wird wachsen. Der grüne Anteil kann die \'Gesundheit\' der zu übersetzenden Sprache anzeigen. Es erlaubt den Entwicklern eine zusätzliche Flexibilität, nur Übersetzungen zu übernehmen, denen zugestimmt wurde.
    -   Befasst sich mit den Fragen der Übersetzer innerhalb der Crowdin-Oberfläche. Wenn z.B. mehr Angaben zum Kontext benötigt werden, wenn die zu übersetzende Passage Fehler enthält, falls über eine Übersetzung diskutiert wird, die schon bestätigt wurde usw\...
    -   Meldet relevante Themen, die Änderungen am Quell-Code erfordern usw., an die Entwickler.

## Zeichenketten filtern 

<img alt="" src=images/Crowdin_Filter_Strings.png  style="width:500px;">

Das Filtern von Zeichenfolgen ist eine nützliche Eigenschaft von Korrekturlesern und Verwaltern. Sie bietet die Möglichkeit, viele Übersetzungszeichenfolgen effektiv zu sortieren, um z.B. nur Zeichenfolgen anzuzeigen, die als \"fehlende weitere Kontextinformationen\" oder \"falscher Quellzeichenfolge\" markiert wurden. Dieser Dienst, den die Übersetzer für FreeCAD erbringen, bietet eine zusätzliche Ebene von QA Tests. Viele Tippfehler, Grammatikprobleme und sogar Programmierfehler können durch die Prüfung von Übersetzungszeichenfolgen aufgedeckt werden. Und so markieren die Nutzer diese besagten problematischen Zeichenfolgen, damit wir darauf reagieren und sie schließlich \'beheben\' können.

## Tastaturkürzel

<img alt="" src=images/Crowdin_keyboard_shortcuts.png  style="width:300px;">

Die Verwendung von Tastaturkürzeln ist ein wichtiger Beitrag zur Zeitersparnis und Effizienz. Es lohnt sich zu lernen, wenn du ein Übersetzer, Korrekturleser oder Verwalter bist. Es ist möglich, die Liste der Tastaturkürzel anzuzeigen, indem du auf das Tastatursymbol im oberen rechten Teil der Crowdin Benutzeroberfläche drückst.

**Wichtiger Hinweis:** Bitte achte sorgfältig darauf, keine Fehler in Übersetzungszeichenfolgen einzuführen, die durch unsachgemäße Tastendrücke erzeugt wurden, die als Tastenkürzel gedacht waren.

**Oft genutzte Tastaturkürzel:**

-   Copy source translation: **Alt**+**C**
-   Übersetzung speichern: **Ctrl**+**Enter**
-   Übersetzung bestätigen: **Alt**+**L** (relevant für Kurrekturlesende)

## Überstzungsprobleme beheben 

If you notice a string in the FreeCAD UI that is not translated do the following:

1.  If you are not sure to which workbench the string belongs, first locate it in the FreeCAD source code. On Linux you can use {{Incode|grep -r "English text" *}}.
2.  For example, if the string is {{Incode|"Solver Calculix Standard"}} you will find this file: **src/Mod/Fem/femcommands/commands.py**, and you will know that the string belongs to the FEM workbench.
3.  Now search for this string on Crowdin. If your language is French visit <https://crowdin.com/project/freecad/fr>, go to the FEM workbench, and check if it is there and translated.
4.  There two possibilities:
    1.  The string is not on Crowdin because it has not been picked up by the script that gathers strings from the FreeCAD source code and packs them into **.ts** files. There can be two reasons for this:
        -   The string is not properly handled by {{Incode|translate()}} code (or {{Incode|QT_TRANSLATE_NOOP()}} code for special cases like command names), that means there is a problem that must be solved in the source code.
        -   Everything seems normal, but the gathering script has a problem with that specific string, which can happen as it has many bugs.
    2.  The string is on Crowdin. There are several possibilities then:
        -   It might be that the latest Crowdin strings have not yet been merged. You can check if that\'s the case by searching for the string (see above), and check if it appears in the translated **.ts** files. In our example {{Incode|"Solver Calculix Standard"}} would then be found in **src/Mod/Fem/Gui/Resources/translations/Fem_fr.ts**. This indicates that the translated string is in the FreeCAD source and everything should be fine in the next build.
        -   If the string is still missing in the next build, the problem is more complex and we\'ll need to do some debugging:
            1.  Check in the source file if the original string is handled by {{Incode|translate()}} or {{Incode|QT_TRANSLATE_NOOP()}}.
            2.  Verify that the context matches what is on Crowdin.
            3.  In case of {{Incode|QT_TRANSLATE_NOOP()}}, there are several particular cases. For commands, the context must be the exact command name, the same as used in {{Incode|FreeCADGui.runCommand()}}. For properties it must be {{Incode|"App::Property"}}. For the names of menus and toolbars it must be {{Incode|"Workbench"}}.

## Verweise

-   [Lokalisierung](Localisation/de.md)
-   [Crowdin Skripte](Crowdin_Scripts/de.md)
-   [Freigabeprozess](Release_process.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Administration](Category_Administration.md) > Crowdin Administration/de
