# Crowdin Administration/de
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

Findet man einen Eintrag in der FreeCAD-Benutzeroberfläche, der nicht übersetzt ist, hat man folgende Möglichkeit:

1.  Ist nicht sicher zu welchem Arbeitsbereicht ein Eintrag gehört, wird dieser zuerst im Quellcode geortet. Unter linux kann dafür {{Incode|grep -r "English text" *}} vervendet werden.
2.  Lautet der Eintrag beispielsweise {{Incode|"Solver Calculix Standard"}} findet man diese Datei: **src/Mod/Fem/femcommands/commands.py** und weiß dann, dass der Eintrag zum Arbeitsbereich FEM gehört.
3.  Jetzt wird der Eintrag auf Crowdin gesucht. Ist die gesuchte Sprache Deutsch, wird <https://crowdin.com/project/freecad/de> aufgerufen und Fem.ts ausgewählt und überprüft, ob der Eintrag vorhanden und übersetzt ist.
4.  Jetzt gibt es zwei Möglichkeiten:
    1.  Der Eintrag existiert nicht auf Crowdin, da er nicht von dem Skript erfasst wurde, das die Einträge im FreeCAD-Quellcode sammelt und in den **.ts**-Dateien zusammenstellt. Dafür kann es zwei Gründe geben:
        -   Der Eintrag wurde nicht ordentlich durch den Code von {{Incode|translate()}} erfasst (oder {{Incode|QT_TRANSLATE_NOOP()}} für besondere Fälle wie Befehlsnamen), was bedeutet, dass ein Problem in Quellcode behoben werden muss.
        -   Alles sieht normal aus, aber das Erfassungsskript hat ein Problem mit einer bestimmten Zeichenkette; dies kann passieren, da es viele Fehler enthält.
    2.  Der Eintrag existiert auf Crowdin. Dafür gibt es dann mehrere Möglichkeiten:
        -   Es kann sein, dass die neuesten Crowdin-Einträge noch nicht hinzugefügt wurden. Diese lässt sich überprüfen, indem nach dem Eintrag gesucht wird (siehe oben) und überprüft wird, ob er in den übersetzten **.ts**-Dateien auftaucht. In unserem Beispiel könnte man {{Incode|"Solver Calculix Standard"}} in **src/Mod/Fem/Gui/Resources/translations/Fem_de.ts** finden. Dies zeigt an, dass die Übersetzung im FreeCAD-Quellcode enthalten ist und in der nächsten Version alles in Ordnung sein sollte.
        -   Fehlt der Eintrag in der nächsten Version noch immer, iste das Problem komplizierter und wir müssen etwas Fehlersuche betreiben:
            1.  Im Quellcode überprüfen, ob der originale Eintrag von {{Incode|translate()}} oder {{Incode|QT_TRANSLATE_NOOP()}} verarbeitet wird.
            2.  Sicherstellen, dass der Eintrag den Zusammenhang auf Crowdin entspricht.
            3.  Im Falle von {{Incode|QT_TRANSLATE_NOOP()}} gibt es einige besondere Anwendungsfälle. Für Befehle muss der Zusammenhang exakt dem Befehlsnamen entsprechen, demselben, der von {{Incode|FreeCADGui.runCommand()}} verwendet wird. Für Eigenschaften muss es {{Incode|"App::Property"}} sein. Für die Namen von Menüs und Symbolleisten muss es {{Incode|"Workbench"}} sein.



## Verweise

-   [Lokalisierung](Localisation/de.md)
-   [Crowdin-Skripte](Crowdin_Scripts/de.md)
-   [Freigabeprozess](Release_process.md)



---
⏵ [documentation index](../README.md) > [Administration](Category_Administration.md) > Crowdin Administration/de
