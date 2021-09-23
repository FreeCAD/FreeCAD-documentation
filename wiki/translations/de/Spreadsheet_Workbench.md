# Spreadsheet Workbench/de
{{Page_in_progress}}






<img alt="Tabellenkalkulation Arbeitsbereichssymbol" src=images/Workbench_Spreadsheet.svg  style="width:128px;">

## Einführung

Der <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> [Arbeitsbereich Tabellenkalkulation](Spreadsheet_Workbench/de.md) ermöglicht die Erstellung und Bearbeitung von Tabellen, Daten aus der Tabellenkalkulation als Parameter in einem Modell zu verwenden, die Tabellenkalkulation mit aus einem Modell abgerufenen Daten zu füllen, Berechnungen durchzuführen und die Daten in andere Tabellenkalkulationsprogramme wie LibreOffice oder Microsoft Excel zu exportieren.


{{TOCright}}

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:600px;"> 
*Eine Tabellenblatt mit bestimmten Zellen, die mit Text und Mengen gefüllt sind*

## Werkzeuge

-   <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:24px;"> [Blatt erstellen](Spreadsheet_CreateSheet/de.md): Erstelle ein neues Arbeitsblatt.

-   <img alt="" src=images/Spreadsheet_Import.svg  style="width:24px;"> [Import](Spreadsheet_Import/de.md): eine Tabulator-getrennte Werte Datei in ein Tabellenblatt importieren.
-   <img alt="" src=images/Spreadsheet_Export.svg  style="width:24px;"> [Export](Spreadsheet_Export/de.md): eine Tabulator-getrennte Werte Datei aus einem Tabellenblatt exportieren.

-   <img alt="" src=images/Spreadsheet_MergeCells.svg  style="width:24px;"> [Zellen zusammenführen](Spreadsheet_MergeCells/de.md): ausgewählte Zellen zusammenführen.
-   <img alt="" src=images/Spreadsheet_SplitCell.svg  style="width:24px;"> [Zelle teilen](Spreadsheet_SplitCell/de.md): zuvor zusammengeführte Zellen teilen.

-   <img alt="" src=images/Spreadsheet_AlignLeft.svg  style="width:24px;"> [Linksbündig ausrichten](Spreadsheet_AlignLeft/de.md): den Inhalt der gewählten Zelle auf links ausrichten.
-   <img alt="" src=images/Spreadsheet_AlignCenter.svg  style="width:24px;"> [Mittig ausrichten](Spreadsheet_AlignCenter/de.md): den Inhalt der gewählten Zelle auf mittig horizontal ausrichten.
-   <img alt="" src=images/Spreadsheet_AlignRight.svg  style="width:24px;"> [Rechtsbündig ausrichten](Spreadsheet_AlignRight/de.md): den Inhalt der gewählten Zelle auf rechts ausrichten.
-   <img alt="" src=images/Spreadsheet_AlignTop.svg  style="width:24px;"> [Nach oben ausrichten](Spreadsheet_AlignTop/de.md): den Inhalt der gewählten Zelle oben ausrichten.
-   <img alt="" src=images/Spreadsheet_AlignVCenter.svg  style="width:24px;"> [Vertikal ausrichten center](Spreadsheet_AlignVCenter/de.md): den Inhalt der gewählten Zelle mittig vertikal ausrichten.
-   <img alt="" src=images/Spreadsheet_AlignBottom.svg  style="width:24px;"> [Nach unten ausrichten](Spreadsheet_AlignBottom/de.md): den Inhalt der gewählten Zelle unten ausrichten.

-   <img alt="" src=images/Spreadsheet_StyleBold.svg  style="width:24px;"> [Stil Fett](Spreadsheet_StyleBold/de.md): den Inhalt der gewählten Zelle auf fett stellen.
-   <img alt="" src=images/Spreadsheet_StyleItalic.svg  style="width:24px;"> [Stil Kursiv](Spreadsheet_StyleItalic/de.md): den Inhalt der gewählten Zelle auf kursiv stellen.
-   <img alt="" src=images/Spreadsheet_StyleUnderline.svg  style="width:24px;"> [Stil Unterstrichen](Spreadsheet_StyleUnderline/de.md): den Inhalt der gewählten Zelle auf unterstrichen stellen.

-   <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> [Setze Alias](Spreadsheet_SetAlias/de.md): die ausgewählte Zelle mit einem Alias benennen.

-    **Schwarz**und **Weiß** bestimmen die Vorder- und den Hintergrundfarbe der gewählten Zellen.

-   Kontextmenü der Tabellenzeilen und -spalten: Klicke mit der rechten Maustaste auf den Kopf einer Zeile oder Spalte, um darüber eine neue Zeile oder links eine neue Spalte einzufügen, oder um die aktuelle Zeile/Spalte zu löschen. Du kannst auch mehrere Zeilen oder Spalten markieren, um sie zu löschen.{{Version/de|0.20}} Du kannst auch auswählen, wo die neuen Zeilen/Spalten eingefügt werden sollen. Um z.B. 3 neue Spalten auf einmal einzufügen, markiere 3 Spalten und verwende das Kontextmenü, das nun das Einfügen von 3 Spalten anbietet.

## Spreadsheet editing 

As noted above under Tools, right click on a row or column header produces a pulldown menu that allows you to delete the row/column or insert a new blank one. Formula references to cells that get moved by these operations get patched to refer to the new location, You will get a warning and a request to confirm if a row or column deletion would abolish a reference that\'s used in your model.

Cut/copy/paste can be used to edit data. Cut and copy will both operate on single cells, rows, columns, rectangles, or indeed any selection group of cells you set up. Cut clears the content of selected cells; both cut and copy stash the cell content in an internal paste buffer. A paste operation writes the buffered data in such a way that the content of the uppermost-leftmost cell of the buffered set is dropped in the cell where the cursor is when you paste; other buffered content is dropped where it will have the same relationship to that target as it originally did to the upper-left cell of your cut/paste set.

An important caveat: Cut/copy/paste operations do *not* fix up formula references. If you move the content of a cell, formulas which referred to the old location will break. If the old location becomes empty, the breakage will become visible as the expression evaluator will display \#ERR in dependent cells. Properties are also not carried along.

The Undo key can be use to back out any of these operations. However, it undoes a cell at a time - thus, multiple Undos may be requited to back out a single copy or paste.

## Zelleigenschaften

Die Eigenschaften der Kalkulationstabellenzelle können mit einem Rechtsklick auf einer Zelle geändert werden. Der folgende Dialog klappt auf:

![](images/SpreadsheetCellPropDialog.png )

Wie in den Reitern angezeigt können die folgenden Eigenschaften geändert werden:

-   Farbe: Text- und Hintergrundfarbe
-   Ausrichtung: horizontale und vertikale Textausrichtung
-   Stil: Textstil: fett, kursiv, unterstrichen
-   Einheiten:  Anzeigeeinheiten für diese Zelle. Den Abschnitt [Einheiten](Spreadsheet_Workbench/de#Einheiten.md) unten beachten.
-   Alias:  Einen [alias](Spreadsheet_SetAlias.md) für diese Zelle festlegen. Dieser Alias kann in den Zellformeln und auch in allgemeinen [ Ausdrücken](Expressions/de.md) verwendet werden; siehe Abschnitt [Tabellenkalkulationsdaten in Ausdrücken](#Spreadsheet_data_in_expressions/de.md) für weitere Informationen.

## Zellausdrücke

Eine Tabellenzelle kann beliebigen Text oder einen Ausdruck enthalten. Technisch gesehen müssen Ausdrücke mit einem Gleichheitszeichen \'=\' beginnen. Die Tabellenkalkulation versucht jedoch, intelligent zu sein; wenn du etwas eingibst, das wie ein Ausdruck aussieht, ohne das führende \'=\', wird automatisch eines hinzugefügt.

Zellausdrücke können Zahlen, Funktionen, Verweise auf andere Zellen und Verweise auf Eigenschaften des Modells enthalten (Siehe aber [Aktuelle Begrenzungen](#Current_Limitations/de.md) unten). Zellen werden durch ihre Spalte (GROSSBUCHSTABEN) und Zeile (Zahl) referenziert. Eine Zelle kann auch durch ihren [Aliasnamen](#alias_name/de.md) (siehe unten) referenziert werden. Beispiel: B4 + A6

**Anmerkung:** Zellausdrücke werden von FreeCAD als Programmiercode behandelt. Wenn Sie also den Inhalt einer Zelle bearbeiten, sehen Sie, dass der Inhalt nicht Ihren Anzeigeeinstellungen folgt:

-   das Dezimaltrennzeichen ist immer ein Punkt
-   die Anzahl der angezeigten Dezimalstellen kann von Ihren [Vorzugseinstellungs](Preferences_Editor#Units.md) abweichen

Referenzen zu Objekten im Modell werden unter [Referenzen auf CAD-Daten](#References_to_CAD-data/de.md) unten erklärt. Die Verwendung von Tabellenkalkulationszellenwerten zur Definition von Modelleigenschaften wird unter [Tabellenkalkulationsdaten in Ausdrücken](#Spreadsheet_data_in_Expressions/de.md) weiter unten erläutert. Weitere Besonderheiten zur Bildung von Ausdrücken findest du unter [Ausdrücke](Expressions/de.md).

## Wechselwirkung zwischen Kalkulationstabellen und dem CAD Modell 

Daten in den Zellen einer Kalkulationstabelle können in CAD Modellparameterausdrücken verwendet werden. So kann eine Tabellenkalkulationstabelle als Quelle für Parameterwerte verwendet werden, die im gesamten Modell verwendet werden, die Werte effektiv an einem Ort zu sammeln. Wenn Werte in der Kalkulationstabelle geändert werden, werden sie im ganzen Modell übertragen.

In ähnlicher Weise können Eigenschaften von CAD Modellobjekten in Ausdrücken in Kalkulationstabellenzellen verwendet werden. Dies ermöglicht die Verwendung von Objekteigenschaften wie Volumen oder Fläche in der Kalkulationstabelle. Wenn der Name eines Objekts im CAD Modell geändert wird, wird die Änderung automatisch auf alle Referenzen in Kalkulationstabellenausdrücken mit dem geänderten Namen übertragen.

In einem Dokument kann mehr als eine Kalkulationstabelle verwendet werden. Eine Kalkulationstabelle kann entweder über ihren Namen oder ihre Beschriftung identifiziert werden.

FreeCAD vergibt automatisch einen eindeutigen Namen für eine Kalkulationstabelle, wenn es erstellt wird. Diese Namen folgen dem Muster `Spreadsheet`, `Spreadsheet001`, `Spreadsheet002` und so weiter. Der Name kann nicht manuell geändert werden, und er ist in den Eigenschaften des Arbeitsblatts nicht sichtbar. Er kann verwendet werden, um auf das Arbeitsblatt in einem [Ausdruck](Expressions/de.md) zu verweisen (siehe [Arbeitsblattdaten in Ausdrücken](#Spreadsheet_data_in_expressions.md) unten).

Die Beschriftung eines Kalkulationstabellenblatts wird bei der Erstellung automatisch auf den Namen des Kalkulationstabellenblatts gesetzt. Im Gegensatz zum Namen kann die Beschriftung geändert werden, z. B. in der Eigenschaftsleiste oder über die Kontextmenüaktion Umbenennen. Beachten Sie, dass die Beschriftung eines Tabellenblatts innerhalb eines Dokuments eindeutig sein muss; wenn Sie versuchen, die Beschriftung in eine Beschriftung zu ändern, die bereits von einem anderen Kalkulationstabellenblatt verwendet wird, akzeptiert FreeCAD die neue Beschriftung nicht.

FreeCAD prüft auf zyklische Abhängigkeiten. Siehe [Aktuelle Begrenzungen](Spreadsheet_Workbench/de#Aktuelle_Begrenzungen.md).

### Referenzen auf CAD-Daten 

Wie oben angegeben, kann man in Kalkulationstabellenausdrücken auf Daten aus dem CAD Modell verweisen.

Berechnete Ausdrücke in Rechenblattzellen beginnen mit einem Gleichheitszeichen (\'=\'). Der Eingabe-Mechanismus der Tabellenkalkulation versucht jedoch, intelligent zu sein. Ein Ausdruck kann ohne das führende \'=\' eingegeben werden; wenn die eingegebene Zeichenkette ein gültiger Ausdruck ist, wird automatisch ein \'=\' hinzugefügt, wenn die letzte **Enter** eingegeben wird. Wenn die eingegebene Zeichenkette kein gültiger Ausdruck ist (oft das Ergebnis einer Eingabe mit falscher Groß- und Kleinschreibung, z. B. \"MyCube.length\" statt \"MyCube.Length\"), wird kein führendes \'=\' hinzugefügt und die Zeichenkette wird einfach als Text behandelt.

**Anmerkung:** Das obige Verhalten (automatisches Einfügen von \'=\') hat einige unangenehme Auswirkungen:

-   Wenn du eine Spalte mit Namen, die dem [alias-names](#alias_name.md) in einer angrenzenden Spalte mit Werten entspricht, beibehalten wollen, musst du den Namen in der Bezeichnungsspalte *vorher* eingeben und der Zelle in der Wertspalte ihren Alias Namen geben. Anderenfalls nimmt das Kalkulationstabellenblatt bei der Eingabe des Alias Namens in der Beschriftungsspalte an, dass es sich um einen Ausdruck handelt und ändert ihn in \"=\"; und der angezeigte Text ist der Wert aus der Zelle .
-   Wenn du bei der Eingabe des Namens in der Beschriftungsspalte einen Fehler machst und diesen korrigieren möchtest, kannst du ihn nicht einfach in den Alias Namen ändern. Stattdessen musst du zuerst den Alias Namen in etwas anderes ändern, dann den Textnamen in der Beschriftungsspalte korrigieren und dann den Alias Namen in der Wertspalte wieder in seinen ursprünglichen Namen ändern.

Eine Weise, diese Probleme zu umgehen, besteht darin, den Textbeschriftungen, die den Alias-Namen entsprechen, eine feste Zeichenfolge voranzustellen und sie dadurch zu unterscheiden. Beachte, dass \"\_\" nicht funktioniert, da es in \"=\" umgewandelt wird. Ein Leerzeichen ist zwar unsichtbar, funktioniert aber.

Die folgende Tabelle zeigt einige Beispiele unter der Annahme, dass das Modell über eine Funktion namens \"MeinWürfel\" verfügt:

  CAD-Daten                                                     Zelle im Tabellenblatt             Ergebnis
  ------------------------------------------------------------- ---------------------------------- -----------------------------------
  Parametrische Länge eines Würfels des Arbeitsbereiches Part   =MeinWürfel.Length                 Länge mit den Einheiten mm
  Volumen des Würfels                                           =MeinWürfel.Shape.Volume           Volumen in mm³ ohne Einheiten
  Typ des Würfel-\"Shapes\"                                     =MeinWürfel.Shape.ShapeType        String: Solid
  Beschriftung des Würfels                                      =MeinWürfel.Label                  String: MeinWürfel
  x-Koordinate des Massenschwerpunktes des Würfels              =MeinWürfel.Shape.CenterOfMass.x   x-Koordinate in mm ohne Einheiten

### Kalkulationstabellendaten in Ausdrücken 

Um Kalkulationstabellendaten in anderen Teilen von FreeCAD zu verwenden, wirst du normalerweise einen [Ausdruck](Expressions/de.md) erstellen, der sich auf die Kalkulationstabelle und die Zelle bezieht, die die Daten enthält, die du verwenden möchtest. Du kannst Kalkulationstabellen über den Namen oder die Beschriftung identifizieren, und du kannst die Zellen über die Position oder über einen Alias identifizieren. Die Autovervollständigung ist für alle Formen des Verweises verfügbar.

+---------------------+-----------------------------------------------------+--------------------------------------------------------+
|                     | Kalkulationstabelle nach Name                       | Kalkulationstabelle nach Beschriftung                  |
+=====================+=====================================================+========================================================+
| Zelle nach Position |                                      |                                         |
|                     | `<nowiki>=Spreadsheet042.B5</nowiki>`      | `<nowiki>=<<MySpreadsheet>>.B5</nowiki>`      |
|                     |                                                  |                                                     |
+---------------------+-----------------------------------------------------+--------------------------------------------------------+
| Zelle nach Alias    |                                      |                                         |
|                     | `<nowiki>=Spreadsheet042.MyAlias</nowiki>` | `<nowiki>=<<MySpreadsheet>>.MyAlias</nowiki>` |
|                     |                                                  |                                                     |
+---------------------+-----------------------------------------------------+--------------------------------------------------------+


<div class="mw-collapsible mw-collapsed">

Die empfohlene Art, auf Kalkulationstabellenblattdaten zu verweisen, ist die Verwendung der Kalkulationstabellenbeschriftung und des Zellaliasnamens. Eine ausführlichere Erklärung der Vor- und Nachteile der Adressierungsmodi findest du im erweiterten Abschnitt unten.


<div class="mw-collapsible-content">

Die Verwendung der Kalkulationstabellenbeschriftung hat den Vorteil, dass sie frei geändert werden kann, um den Inhalt der Kalkulationstabelle zu beschreiben. Es ist auch einfacher, die verwendete Kalkulationstabelle zu identifizieren, da der Text im Ausdruck mit der in der Modell- und Eigenschaftsansicht angezeigten Beschriftung übereinstimmt. Wenn du dich entscheidesz, die Beschriftung einer Kalkulationstabelle zu ändern, werden bestehende Verweise auf den Inhalt der Kalkulationstabelle aktualisiert, sodass du deine Ausdrücke nicht durch Umbenennen der Kalkulationstabelle zerstörst. Der interne Name der Kalkulationstabelle ist nur im Ausdruckseditor verfügbar. Wenn du also den internen Namen verwendest und später die Kalkulationstabellen umbenennst, kannst du deine Ausdrucksdaten nur schwer zu deiner Quelle zurückverfolgen.

Beachte, dass beim Anlegen eines neuen Kalkulationstabellenblatts der Name und die Beschriftung identisch sind, so dass es leicht passieren kann, dass du versehentlich den Namen des Kalkulationstabellenblatts statt der Beschriftung verwendest. Eine einfache Möglichkeit, dies zu vermeiden, besteht darin, der Kalkulationstabelle einen aussagekräftigen Namen zu geben, bevor du sie in Ausdrücken verwendest.

Du kannst zwar die Zeilen- und Spaltennummer in einem Ausdruck verwenden, um auf eine Zelle zu verweisen, aber am besten ist es, der Zelle einen Aliasnamen zu geben und diesen zu verwenden. Siehe [Zelleneigenschaften](#Cell_Properties.md) oben, wie du den Alias festlegst. Wenn die Daten in Zelle B1 beispielsweise den Längenparameter für ein Objekt enthalten, würde ein Alias-Name von `MyObject_Length` ermöglichen, dass der Wert als `<<MyParams>>.MyObject_Length` anstelle von `Spreadsheet.B1` referenziert wird. Alias-Namen sind nicht nur viel einfacher zu lesen und zu verstehen, sie lassen sich auch viel leichter ändern, wenn du dich entscheidest, die Struktur deines Arbeitsblatts anzupassen. Die Verwendung eines Alias hat auch den Vorteil, dass es einfacher ist zu sehen, welche Zellen verwendet werden, um andere Teile des Dokuments zu steuern. Beachte, dass FreeCAD die Positionsbezüge in Ausdrücken automatisch anpasst, wenn du Zeilen und Spalten in der Tabelle einfügst oder entfernst. Das heißt, auch wenn du Zeilen- und Spaltennummern in einem Ausdruck verwendest, kannst du Zeilen und Spalten einfügen, ohne die Bezüge zu den umgebenden Zellen zu unterbrechen.


</div>


</div>

### Komplexe Modelle und Neuberechnungen 

Das Bearbeiten einer Kalkulationstabelle löst eine Neuberechnung des 3D Modells aus, auch wenn die Änderungen keine Auswirkungen auf das Modell haben. Bei einem komplexen Modell kann eine Neuberechnung sehr lange dauern, und nach jeder einzelnen Bearbeitung warten zu müssen, ist natürlich ziemlich lästig.


<div class="mw-translate-fuzzy">

Es gibt drei Lösungen, um dies zu beheben:

\#\* Überspringe vorübergehend die Neuberechnungen:

\#\* Klicke mit der rechten Maustaste in der [Baumansicht](Tree_view/de.md) <img alt="" src=images/Document.svg  style="width:24px;"> das Dokument, das die Tabelle enthält an.

\#\* Wähle die Option **Überspringe Neuberechnen** aus dem Kontextmenü.

\#\* Diese Lösung hat einen großen Nachteil. Neue Werte, die in die Tabelle eingegeben werden, werden nicht angezeigt, bis das Dokument neu berechnet wird. Stattdessen wird `#PENDING` angezeigt.

\#\* Du kannst entweder manuell neu berechnen, indem du den Befehl [Std Aktualisieren](Std_Refresh/de.md) verwendest, oder du deaktivierst **Überspringe Neuberechnen**, wenn du mit der Bearbeitung fertig bist.

\#\* Verwende ein Makro, um Neuberechnungen während der Bearbeitung einer Kalkulationstabelle automatisch zu überspringen:

\#\* Lade [skipSheet.FCMacro](https://forum.freecadweb.org/viewtopic.php?f=8&t=48600#p419301) herunter und führe es aus.

\#\* Diese Lösung spart ein paar Schritte im Vergleich zur ersten Lösung, hat aber auch den genannten Nachteil.

1.  Lege die Kalkulationstabelle in einer separaten Datei ab:
    -   Du kannst Kalkulationstabellendaten aus einer externen Datei mit dieser Syntax referenzieren: `<nowiki>=NameOfFile#<<MySpreadsheet>>.MyAlias</nowiki>`.
    -   Der Vorteil, das Tabellenblatt in einer anderen Datei zu haben, gegenüber dem Ausschalten der Neuberechnung ist, dass die Kalkulationstabelle selbst neu berechnet wird.
    -   Der Nachteil ist, dass das Modell nach Änderungen an der Tabelle nicht automatisch neu berechnet wird.
    -   In dem Szenario, in dem du zuerst die \'Kalkulationstabelle\' Datei öffnen, einen oder mehrere Werte ändern und dann die \'Modell\' Datei öffnen, wird es keinen Hinweis darauf geben, dass das Modell neu berechnet werden muss. Wenn jedoch beide Dateien geöffnet sind, wird das Symbol [Std Aktualisieren](Std_Refresh/de.md) für die \'Modell\' Datei nach Änderungen in der \'Kalkulationstabelle\' Datei korrekt aktualisiert.


</div>

## Einheiten

Die Kalkulationstabelle hat eine Vorstellung von Dimension (Einheiten), die mit Zellwerten verbunden ist. Eine Zahl, die ohne eine zugehörige Einheit eingegeben wird, hat keine Dimension. Die Einheit sollte direkt nach dem Zahlenwert eingegeben werden, ohne Leerzeichen dazwischen. Wenn eine Zahl eine zugehörige Einheit hat, wird diese Einheit in allen Berechnungen verwendet. Zum Beispiel ergibt die Multiplikation von zwei Längen mit der Einheit mm eine Fläche mit der Einheit mm².

Wenn eine Zelle einen Wert enthält, der eine Dimension darstellt, sollte dieser mit der zugehörigen Einheit eingegeben werden. Während man in vielen einfachen Fällen mit einem dimensionslosen Wert auskommen kann, ist es unklug, die Einheit nicht einzugeben. Wenn ein Wert, der eine Bemaßung repräsentiert, ohne die zugehörige Einheit eingegeben wird, gibt es einige Sequenzen von Operationen, die FreeCAD veranlassen, sich über inkompatible Einheiten in einem Ausdruck zu beschweren, obwohl der Ausdruck eigentlich gültig sein sollte. (Dies kann besser durch anschauen [dieser Forumsbeitrag](https://forum.freecadweb.org/viewtopic.php?f=3&t=34713&p=292455#p292438) in den FreeCAD Foren verstanden werden.)

Du kannst die für einen Zellenwert angezeigten Einheiten über den Eigenschaftendialog [units tab](#units_tab/de.md) (oben) ändern. (oben). Dadurch wird der in der Zelle enthaltene Wert nicht geändert; es wird lediglich der vorhandene Wert für die Anzeige umgewandelt. Der Wert, der für Berechnungen verwendet wird, ändert sich nicht, und die Ergebnisse von Formeln, die den Wert verwenden, ändern sich nicht. Beispielsweise kann eine Zelle, die den Wert \"5,08cm\" enthält, als \"2in\" angezeigt werden, indem der Wert der Einheitenreiters in \"in\" geändert wird.

Eine dimensionslose Zahl kann im Zelleigenschaftendialog nicht in eine Zahl mit einer Einheit geändert werden. Man kann zwar eine Zeichenfolge für die Einheit eingeben, und diese Zeichenfolge wird angezeigt, aber die Zelle enthält immer noch eine dimensionslose Zahl. Um einen dimensionslosen Wert in einen Wert mit einer Dimension zu ändern, muss der Wert selbst mit seiner zugehörigen Einheit neu eingegeben werden.

Manchmal ist es notwendig, die Einheit von einer Zahl zu entfernen. Dies kann durch die Multiplikation einer 1 mit der reziproken Einheit erreicht werden.

## Importieren und Exportieren 

Tabellen können im CSV-Format[1](https://de.wikipedia.org/wiki/CSV_(Dateiformat)) importiert und exportiert werden. Dieses Format kann von den meisten anderen Tabellenkalkulationsprogrammen wie Microsoft Excel oder LibreOffice Calc gelesen und geschrieben werden. Wenn Dateien nach FreeCAD importiert werden, muss das Trennzeichen, welches die Spalten trennt, das TAB-Zeichen sein. Dies kann üblicherweise in den Tabellenkalkulationsprogrammen vor dem Export eingestellt werden. Der Import einer CSV-Datei ist über das Menü **Spreadsheet → Kalkulationstabelle importieren** oder durch einen Klick auf das Symbol <img alt="" src=images/SpreadsheetImport.svg  style="width:24px;"> möglich. Diese Import-Funktion öffnet keine Excel-Dateien oder andere Tabellenkalkulationsformate.

Tabellen im Excelformat \"xlsx\" können über das Menü **Datei → Importieren...** importiert werden. Exceltabellen können auch durch den Menübefehl **Datei → Öffnen...** oder mit einem Klick auf das Symbol <img alt="" src=images/Document-open.svg  style="width:24px;"> geöffnet werden. In diesem Fall wird ein neues Dokument mit einer Tabelle erzeugt. Es werden die folgenden Funktionen unterstützt:

-   alle Funktionen, die auch in der FreeCAD Tabellenblatt verfügbar sind. Andere Funktionen führen nach dem Import zu einem Fehler in der entsprechenden Zelle.
-   Alias Namen für Zellen
-   Mehr als ein \"Blatt\" im Tabellenblatt. In diesem Fall wird für jede Excel-Tabelle eine FreeCAD Tabelle erstellt.

Andere Funktionalität wird nicht in die FreeCAD Tabellenblätter importiert. Der Excel-Import ist <small>(v0.17)</small>  von FreeCAD.

## Drucken

Um die erforderlichen Seiteneinstellungen für den Druck von FreeCAD-Tabellen einzurichten, werden diese in eine [TechDraw Tabellenansicht](TechDraw_SpreadsheetView/de.md) eingefügt.

## Aktuelle Begrenzungen 

FreeCAD prüft auf zyklische Abhängigkeiten. Nach dem Entwurf endet diese Prüfung auf der Ebene des Tabellenkalkulationsobjekts. Infolgedessen solltest du keine Tabellenkalkulation haben, die beides enthält Zellen, deren Werte zur Angabe von Parametern für das Modell verwendet werden, und Zellen, deren Werte die Ausgabe aus dem Modell verwenden. Du kannst z.B. keine Zellen haben, die die Länge, Breite und Höhe eines Objekts festlegen, und eine weitere Zelle, die das Gesamtvolumen der resultierenden Form referenziert. Diese Einschränkung kann durch zwei Tabellenkalkulationen überwunden werden: eine, die als Datenquelle für die Eingabeparameter des Modells dient und die andere verwendet für Berechnungen auf der Grundlage der resultierenden Geometriedaten.

## Grundlagen Skripterstellung 


```python
import Spreadsheet
sheet = App.ActiveDocument.addObject("Spreadsheet::Sheet","MySpreadsheet")
sheet.Label = "Dimensions"

sheet.set('A1','10mm')
sheet.recompute()
sheet.get('A1')

sheet.setAlias('B1','Diameter')
sheet.set('Diameter','20mm')
sheet.recompute()
sheet.get('Diameter')
```





{{Spreadsheet_Tools_navi

}} 

[Category:Workbenches](Category:Workbenches.md)

---
[documentation index](../README.md) > Spreadsheet Workbench/de
