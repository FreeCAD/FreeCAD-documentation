# <img alt="Tabellenkalkulation Arbeitsbereichssymbol" src=images/Workbench_Spreadsheet.svg  style="width   *64px;"> Spreadsheet Workbench/de

## Einführung

Der <img alt="" src=images/Workbench_Spreadsheet.svg  style="width   *24px;"> [Arbeitsbereich Tabellenkalkulation](Spreadsheet_Workbench/de.md) ermöglicht die Erstellung und Bearbeitung von Tabellen, Daten aus der Tabellenkalkulation als Parameter in einem Modell zu verwenden, die Tabellenkalkulation mit aus einem Modell abgerufenen Daten zu füllen, Berechnungen durchzuführen und die Daten in andere Tabellenkalkulationsprogramme wie LibreOffice oder Microsoft Excel zu exportieren.


{{TOCright}}

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width   *600px;"> 
*Eine Tabellenblatt mit bestimmten Zellen, die mit Text und Mengen gefüllt sind*

## Werkzeuge

-   <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width   *24px;"> [Blatt erstellen](Spreadsheet_CreateSheet/de.md)   * Erstelle ein neues Tabellenblatt.

-   <img alt="" src=images/Spreadsheet_Import.svg  style="width   *24px;"> [Importieren](Spreadsheet_Import/de.md)   * eine CSV Datei in ein Tabellenblatt importieren.

-   <img alt="" src=images/Spreadsheet_Export.svg  style="width   *24px;"> [Exportieren](Spreadsheet_Export/de.md)   * eine CSV Datei aus einem Tabellenblatt exportieren.

-   <img alt="" src=images/Spreadsheet_MergeCells.svg  style="width   *24px;"> [Zellen zusammenführen](Spreadsheet_MergeCells/de.md)   * Markierte Zellen zusammenführen.

-   <img alt="" src=images/Spreadsheet_SplitCell.svg  style="width   *24px;"> [Zelle teilen](Spreadsheet_SplitCell/de.md)   * teilt zuvor zusammengeführte Zellen.

-   <img alt="" src=images/Spreadsheet_AlignLeft.svg  style="width   *24px;"> [Links ausrichten](Spreadsheet_AlignLeft/de.md)   * Richtet den Inhalt der ausgewählten Zellen links aus.

-   <img alt="" src=images/Spreadsheet_AlignCenter.svg  style="width   *24px;"> [Zentriert ausrichten](Spreadsheet_AlignCenter/de.md)   * Richtet den Inhalt der ausgewählten Zellen horizontal zur Mitte aus.

-   <img alt="" src=images/Spreadsheet_AlignRight.svg  style="width   *24px;"> [Rechts ausrichten](Spreadsheet_AlignRight/de.md)   * Richtet den Inhalt der markierten Zellen nach rechts aus.

-   <img alt="" src=images/Spreadsheet_AlignTop.svg  style="width   *24px;"> [Oben ausrichten](Spreadsheet_AlignTop/de.md)   * Richtet den Inhalt der markierten Zellen nach oberen aus.

-   <img alt="" src=images/Spreadsheet_AlignVCenter.svg  style="width   *24px;"> [Vertikale Mittig ausrichten](Spreadsheet_AlignVCenter/de.md)   * Richtet die Inhalte der ausgewählten Zellen vertikal zur Mitte aus.

-   <img alt="" src=images/Spreadsheet_AlignBottom.svg  style="width   *24px;"> [Unten ausrichten](Spreadsheet_AlignBottom/de.md)   * Richtet den Inhalt der markierten Zellen nach unten aus.

-   <img alt="" src=images/Spreadsheet_StyleBold.svg  style="width   *24px;"> [Stil fett](Spreadsheet_StyleBold/de.md)   * Der Inhalt der ausgewählten Zellen wird fett dargestellt.

-   <img alt="" src=images/Spreadsheet_StyleItalic.svg  style="width   *24px;"> [Stil kursiv](Spreadsheet_StyleItalic/de.md)   * setzt den Inhalt der ausgewählten Zellen kursiv.

-   <img alt="" src=images/Spreadsheet_StyleUnderline.svg  style="width   *24px;"> [Stil Unterstreichen](Spreadsheet_StyleUnderline/de.md)   * Der Inhalt der ausgewählten Zellen wird unterstrichen.

-   <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width   *24px;"> [Setze Alias](Spreadsheet_SetAlias/de.md)   * legen den Alias für eine ausgewählte Zelle fest.

-    **Schwarz**und **Weiß** legen die Vorder- und Hintergrundfarben der ausgewählten Zellen fest.

## Einstellungen

-   <img alt="" src=images/Preferences-spreadsheet.svg  style="width   *32px;"> [Einstellungen](Spreadsheet_Preferences/de.md)   * die Einstellungen für den Arbeitsbereich Tabellenkalkulation. {{Version/de|0.20}}

## Einfügen und Entfernen von Zeilen und Spalten 

Rows and columns can be inserted or removed by right-clicking a row or column header and selecting the appropriate option from the contex menu. It is possible to select multiple rows or columns first. Either by holding down the **Ctrl** key while selecting the headers, or by holding down the left mouse button and dragging.

In FreeCAD version 0.19 and earlier rows are inserted above the selected rows, and colomns on the left of the selected columns. In FreeCAD version 0.20 you can specify the insertion side.

Note that removing rows or columns with data can break the spreadsheet and your model if it relies on the spreadheet. You are not prewarned if this happens.

## Zellen ausschneiden und einfügen 

Cut and copy-paste operations can be used on cells in FreeCAD spreadsheets. You can use the normal shortcuts for these operations   * **Ctrl**+**X**, **Ctrl**+**C** and **Ctrl**+**V** respectively. To select multiple cells hold down the **Ctrl** key while selecting, or hold down the left mouse button and drag to select a rectangular cell range.

The cut and copy operations store the contents and properties of the cells on the Clipboard. The paste operation writes the data in such a way that the content of the top left cell of the stored data is dropped in the active cell. Other stored content is placed relative to that cell. Formulas are updated accordingly.

Note that removing cells with data can break the spreadsheet and your model if it relies on the spreadheet. You are not prewarned if this happens.

In FreeCAD version 0.19 and earlier there is a bug that can cause FreeCAD to hang if a non-rectangular cell range is pasted. It is advisable to save your work before performing any paste operations.

## Zelleigenschaften


<div class="mw-translate-fuzzy">

Die Eigenschaften der Kalkulationstabellenzelle können mit einem Rechtsklick auf einer Zelle geändert werden. Der folgende Dialog klappt auf   *


</div>

![](images/SpreadsheetCellPropDialog.png )

Wie in den Reitern angezeigt können die folgenden Eigenschaften geändert werden   *

-   Farbe   * Text- und Hintergrundfarbe
-   Ausrichtung   * horizontale und vertikale Textausrichtung
-   Stil   * Textstil   * fett, kursiv, unterstrichen
-   Einheiten   *  Anzeigeeinheiten für diese Zelle. Den Abschnitt [Einheiten](Spreadsheet_Workbench/de#Einheiten.md) unten beachten.
-   Alias   *  Einen [alias](Spreadsheet_SetAlias.md) für diese Zelle festlegen. Dieser Alias kann in den Zellformeln und auch in allgemeinen [ Ausdrücken](Expressions/de.md) verwendet werden; siehe Abschnitt [Tabellenkalkulationsdaten in Ausdrücken](#Spreadsheet_data_in_expressions/de.md) für weitere Informationen.

## Zellausdrücke

Eine Tabellenzelle kann beliebigen Text oder einen Ausdruck enthalten. Technisch gesehen müssen Ausdrücke mit einem Gleichheitszeichen \'=\' beginnen. Die Tabellenkalkulation versucht jedoch, intelligent zu sein; wenn du etwas eingibst, das wie ein Ausdruck aussieht, ohne das führende \'=\', wird automatisch eines hinzugefügt.


<div class="mw-translate-fuzzy">

Zellausdrücke können Zahlen, Funktionen, Verweise auf andere Zellen und Verweise auf Eigenschaften des Modells enthalten (Siehe aber [Aktuelle Begrenzungen](#Current_Limitations/de.md) unten). Zellen werden durch ihre Spalte (GROSSBUCHSTABEN) und Zeile (Zahl) referenziert. Eine Zelle kann auch durch ihren [Aliasnamen](#alias_name/de.md) (siehe unten) referenziert werden. Beispiel   * B4 + A6


</div>

**Anmerkung   *** Zellausdrücke werden von FreeCAD als Programmiercode behandelt. Wenn Sie also den Inhalt einer Zelle bearbeiten, sehen Sie, dass der Inhalt nicht Ihren Anzeigeeinstellungen folgt   *

-   das Dezimaltrennzeichen ist immer ein Punkt
-   die Anzahl der angezeigten Dezimalstellen kann von Ihren [Vorzugseinstellungs](Preferences_Editor#Units.md) abweichen

Referenzen zu Objekten im Modell werden unter [Referenzen auf CAD-Daten](#References_to_CAD-data/de.md) unten erklärt. Die Verwendung von Tabellenkalkulationszellenwerten zur Definition von Modelleigenschaften wird unter [Tabellenkalkulationsdaten in Ausdrücken](#Spreadsheet_data_in_Expressions/de.md) weiter unten erläutert. Weitere Besonderheiten zur Bildung von Ausdrücken findest du unter [Ausdrücke](Expressions/de.md).

## Wechselwirkung zwischen Kalkulationstabellen und dem CAD Modell 

Daten in den Zellen einer Kalkulationstabelle können in CAD Modellparameterausdrücken verwendet werden. So kann eine Tabellenkalkulationstabelle als Quelle für Parameterwerte verwendet werden, die im gesamten Modell verwendet werden, die Werte effektiv an einem Ort zu sammeln. Wenn Werte in der Kalkulationstabelle geändert werden, werden sie im ganzen Modell übertragen.

In ähnlicher Weise können Eigenschaften von CAD Modellobjekten in Ausdrücken in Kalkulationstabellenzellen verwendet werden. Dies ermöglicht die Verwendung von Objekteigenschaften wie Volumen oder Fläche in der Kalkulationstabelle. Wenn der Name eines Objekts im CAD Modell geändert wird, wird die Änderung automatisch auf alle Referenzen in Kalkulationstabellenausdrücken mit dem geänderten Namen übertragen.

In einem Dokument kann mehr als eine Kalkulationstabelle verwendet werden. Eine Kalkulationstabelle kann entweder über ihren Namen oder ihre Beschriftung identifiziert werden.

FreeCAD vergibt automatisch einen eindeutigen Namen für eine Kalkulationstabelle, wenn es erstellt wird. Diese Namen folgen dem Muster `Spreadsheet`, `Spreadsheet001`, `Spreadsheet002` und so weiter. Der Name kann nicht manuell geändert werden, und er ist in den Eigenschaften des Arbeitsblatts nicht sichtbar. Er kann verwendet werden, um auf das Arbeitsblatt in einem [Ausdruck](Expressions/de.md) zu verweisen (siehe [Arbeitsblattdaten in Ausdrücken](#Spreadsheet_data_in_expressions.md) unten).

Die Beschriftung eines Kalkulationstabellenblatts wird bei der Erstellung automatisch auf den Namen des Kalkulationstabellenblatts gesetzt. Im Gegensatz zum Namen kann die Beschriftung geändert werden, z. B. in der Eigenschaftsleiste oder über die Kontextmenüaktion Umbenennen. Beachten Sie, dass die Beschriftung eines Tabellenblatts innerhalb eines Dokuments eindeutig sein muss; wenn Sie versuchen, die Beschriftung in eine Beschriftung zu ändern, die bereits von einem anderen Kalkulationstabellenblatt verwendet wird, akzeptiert FreeCAD die neue Beschriftung nicht.


<div class="mw-translate-fuzzy">

FreeCAD prüft auf zyklische Abhängigkeiten. Siehe [Aktuelle Begrenzungen](Spreadsheet_Workbench/de#Aktuelle_Begrenzungen.md).


</div>

### Referenzen auf CAD-Daten 

Wie oben angegeben, kann man in Kalkulationstabellenausdrücken auf Daten aus dem CAD Modell verweisen.

Berechnete Ausdrücke in Rechenblattzellen beginnen mit einem Gleichheitszeichen (\'=\'). Der Eingabe-Mechanismus der Tabellenkalkulation versucht jedoch, intelligent zu sein. Ein Ausdruck kann ohne das führende \'=\' eingegeben werden; wenn die eingegebene Zeichenkette ein gültiger Ausdruck ist, wird automatisch ein \'=\' hinzugefügt, wenn die letzte **Enter** eingegeben wird. Wenn die eingegebene Zeichenkette kein gültiger Ausdruck ist (oft das Ergebnis einer Eingabe mit falscher Groß- und Kleinschreibung, z. B. \"MyCube.length\" statt \"MyCube.Length\"), wird kein führendes \'=\' hinzugefügt und die Zeichenkette wird einfach als Text behandelt.

**Anmerkung   *** Das obige Verhalten (automatisches Einfügen von \'=\') hat einige unangenehme Auswirkungen   *

-   Wenn du eine Spalte mit Namen, die dem [alias-names](#alias_name.md) in einer angrenzenden Spalte mit Werten entspricht, beibehalten wollen, musst du den Namen in der Bezeichnungsspalte *vorher* eingeben und der Zelle in der Wertspalte ihren Alias Namen geben. Anderenfalls nimmt das Kalkulationstabellenblatt bei der Eingabe des Alias Namens in der Beschriftungsspalte an, dass es sich um einen Ausdruck handelt und ändert ihn in \"=\"; und der angezeigte Text ist der Wert aus der Zelle .
-   Wenn du bei der Eingabe des Namens in der Beschriftungsspalte einen Fehler machst und diesen korrigieren möchtest, kannst du ihn nicht einfach in den Alias Namen ändern. Stattdessen musst du zuerst den Alias Namen in etwas anderes ändern, dann den Textnamen in der Beschriftungsspalte korrigieren und dann den Alias Namen in der Wertspalte wieder in seinen ursprünglichen Namen ändern.

Eine Weise, diese Probleme zu umgehen, besteht darin, den Textbeschriftungen, die den Alias-Namen entsprechen, eine feste Zeichenfolge voranzustellen und sie dadurch zu unterscheiden. Beachte, dass \"\_\" nicht funktioniert, da es in \"=\" umgewandelt wird. Ein Leerzeichen ist zwar unsichtbar, funktioniert aber.

Die folgende Tabelle zeigt einige Beispiele unter der Annahme, dass das Modell über eine Funktion namens \"MeinWürfel\" verfügt   *

  CAD-Daten                                                     Zelle im Tabellenblatt             Ergebnis
    
  Parametrische Länge eines Würfels des Arbeitsbereiches Part   =MeinWürfel.Length                 Länge mit den Einheiten mm
  Volumen des Würfels                                           =MeinWürfel.Shape.Volume           Volumen in mm³ ohne Einheiten
  Typ des Würfel-\"Shapes\"                                     =MeinWürfel.Shape.ShapeType        String   * Solid
  Beschriftung des Würfels                                      =MeinWürfel.Label                  String   * MeinWürfel
  x-Koordinate des Massenschwerpunktes des Würfels              =MeinWürfel.Shape.CenterOfMass.x   x-Koordinate in mm ohne Einheiten

### Kalkulationstabellendaten in Ausdrücken 


<div class="mw-translate-fuzzy">

Um Kalkulationstabellendaten in anderen Teilen von FreeCAD zu verwenden, wirst du normalerweise einen [Ausdruck](Expressions/de.md) erstellen, der sich auf die Kalkulationstabelle und die Zelle bezieht, die die Daten enthält, die du verwenden möchtest. Du kannst Kalkulationstabellen über den Namen oder die Beschriftung identifizieren, und du kannst die Zellen über die Position oder über einen Alias identifizieren. Die Autovervollständigung ist für alle Formen des Verweises verfügbar.


</div>


<div class="mw-translate-fuzzy">

++++
|                     | Kalkulationstabelle nach Name                       | Kalkulationstabelle nach Beschriftung                  |
+=====================+=====================================================+========================================================+
| Zelle nach Position |                                      |                                         |
|                     | `<nowiki>=Spreadsheet042.B5</nowiki>`      | `<nowiki>=<<MySpreadsheet>>.B5</nowiki>`      |
|                     |                                                  |                                                     |
++++
| Zelle nach Alias    |                                      |                                         |
|                     | `<nowiki>=Spreadsheet042.MyAlias</nowiki>` | `<nowiki>=<<MySpreadsheet>>.MyAlias</nowiki>` |
|                     |                                                  |                                                     |
++++


</div>


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

Es gibt drei Lösungen, die sich damit beschäftigen   *

1.  Überspringe vorübergehend Neuberechnungen   *
    -   In der [Baumansicht](Tree_view/de.md) das <img alt="" src=images/Document.svg  style="width   *24px;"> Dokument rechtsklicken, das die Kalkulationstabelle enthält.
    -   Wähle die Option **Überspringe Neuberechnen** aus dem Kontextmenü.
    -   Diese Lösung hat einen großen Nachteil. Neue Werte, die in das Arbeitsblatt eingegeben werden, werden nicht angezeigt, bis das Dokument neu berechnet wird. Stattdessen wird `#PENDING` angezeigt.
    -   Du kannst entweder manuell neu berechnen, durch verwenden des [Std Aktualisieren](Std_Refresh/de.md) Befehls, oder deaktivieren von**Überspringe Neuberechnen**, wenn du mit der Bearbeitung fertig bist.
2.  Verwende ein Makro, um Neuberechnungen während der Bearbeitung eines Tabellenblatts automatisch zu überspringen   *
    -   Lade [skipSheet.FCMacro](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=48600#p419301) herunter und führe es aus.
    -   Diese Lösung spart ein paar Schritte im Vergleich zur ersten Lösung, hat aber auch den erwähnten Nachteil.
3.  Lege das Tabellenblatt in eine separate [FreeCAD Datei](File_Format_FCStd/de.md)   *
    -   Du kannst Tabellenkalkulationsdaten aus einer externen **.FCStd** Datei mit dieser Syntax referenzieren   * `<nowiki>=NameOfFile#<<MySpreadsheet>>.MyAlias</nowiki>`.
    -   Der Vorteil, das Tabellenblatt in einer anderen Datei zu haben, gegenüber dem Ausschalten der Neuberechnung, ist, dass das Arbeitsblatt selbst neu berechnet wird.
    -   Der Nachteil ist, dass das Modell nach Änderungen am Tabellenblatt nicht automatisch neu berechnet wird.
    -   In dem Szenario, in dem du zuerst die \'Tabellenblatt\' Datei öffnest, einen oder mehrere Werte änderst und dann die \'Modell\' Datei öffnest, wird es keinen Hinweis geben, dass das Modell neu berechnet werden muss. Wenn jedoch beide Dateien geöffnet sind, wird das [Std Aktualisieren](Std_Refresh/de.md) Symbol für die \"Modell\" Datei nach Änderungen in der \"Tabellenblatt\" Datei korrekt aktualisiert.

## Einheiten

Die Kalkulationstabelle hat eine Vorstellung von Dimension (Einheiten), die mit Zellwerten verbunden ist. Eine Zahl, die ohne eine zugehörige Einheit eingegeben wird, hat keine Dimension. Die Einheit sollte direkt nach dem Zahlenwert eingegeben werden, ohne Leerzeichen dazwischen. Wenn eine Zahl eine zugehörige Einheit hat, wird diese Einheit in allen Berechnungen verwendet. Zum Beispiel ergibt die Multiplikation von zwei Längen mit der Einheit mm eine Fläche mit der Einheit mm².

Wenn eine Zelle einen Wert enthält, der eine Dimension darstellt, sollte dieser mit der zugehörigen Einheit eingegeben werden. Während man in vielen einfachen Fällen mit einem dimensionslosen Wert auskommen kann, ist es unklug, die Einheit nicht einzugeben. Wenn ein Wert, der eine Bemaßung repräsentiert, ohne die zugehörige Einheit eingegeben wird, gibt es einige Sequenzen von Operationen, die FreeCAD veranlassen, sich über inkompatible Einheiten in einem Ausdruck zu beschweren, obwohl der Ausdruck eigentlich gültig sein sollte. (Dies kann besser durch anschauen [dieser Forumsbeitrag](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=34713&p=292455#p292438) in den FreeCAD Foren verstanden werden.)

Du kannst die für einen Zellenwert angezeigten Einheiten über den Eigenschaftendialog [units tab](#units_tab/de.md) (oben) ändern. (oben). Dadurch wird der in der Zelle enthaltene Wert nicht geändert; es wird lediglich der vorhandene Wert für die Anzeige umgewandelt. Der Wert, der für Berechnungen verwendet wird, ändert sich nicht, und die Ergebnisse von Formeln, die den Wert verwenden, ändern sich nicht. Beispielsweise kann eine Zelle, die den Wert \"5,08cm\" enthält, als \"2in\" angezeigt werden, indem der Wert der Einheitenreiters in \"in\" geändert wird.

Eine dimensionslose Zahl kann im Zelleigenschaftendialog nicht in eine Zahl mit einer Einheit geändert werden. Man kann zwar eine Zeichenfolge für die Einheit eingeben, und diese Zeichenfolge wird angezeigt, aber die Zelle enthält immer noch eine dimensionslose Zahl. Um einen dimensionslosen Wert in einen Wert mit einer Dimension zu ändern, muss der Wert selbst mit seiner zugehörigen Einheit neu eingegeben werden.

Manchmal ist es notwendig, die Einheit von einer Zahl zu entfernen. Dies kann durch die Multiplikation einer 1 mit der reziproken Einheit erreicht werden.

## Importieren und Exportieren 

### CSV Format 

FreeCAD Tabellenblätter können im [1](https   *//de.wikipedia.org/wiki/CSV_(Dateiformat)) Format importiert und exportiert werden, welches auch von den meisten anderen Tabellenkalkulationsanwendungen wie Microsoft Excel oder LibreOffice Calc gelesen und geschrieben werden kann. Siehe [Tabellenblatt Import](Spreadsheet_Import/de.md) und [Tabellenblatt Export](Spreadsheet_Export/de.md) für weitere Informationen.

### XLSX Format 

Tabellenblätter im Excel-Format XLSX können mit dem Befehl [Std Import](Std_Import/de.md) oder dem Befehl [Std Öffnen](Std_Open/de.md) importiert werden. Die folgenden Funktionen werden unterstützt   *

-   alle Funktionen, die auch in der FreeCAD Tabellenblatt verfügbar sind. Andere Funktionen führen nach dem Import zu einem Fehler in der entsprechenden Zelle.
-   Alias Namen für Zellen
-   Mehr als ein Blatt im Excel-Tabellenblatt. In diesem Fall wird für jedes Excel Blatt eine FreeCAD Tabelle erstellt.

Andere Funktionalität wird nicht in das FreeCAD Tabellenblatt importiert.

## Drucken

Um die erforderlichen Seiteneinstellungen für den Druck von FreeCAD-Tabellen einzurichten, werden diese in eine [TechDraw Tabellenansicht](TechDraw_SpreadsheetView/de.md) eingefügt.

## Aktuelle Begrenzungen 


<div class="mw-translate-fuzzy">

FreeCAD prüft auf zyklische Abhängigkeiten. Nach dem Entwurf endet diese Prüfung auf der Ebene des Tabellenkalkulationsobjekts. Infolgedessen solltest du keine Tabellenkalkulation haben, die beides enthält Zellen, deren Werte zur Angabe von Parametern für das Modell verwendet werden, und Zellen, deren Werte die Ausgabe aus dem Modell verwenden. Du kannst z.B. keine Zellen haben, die die Länge, Breite und Höhe eines Objekts festlegen, und eine weitere Zelle, die das Gesamtvolumen der resultierenden Form referenziert. Diese Einschränkung kann durch zwei Tabellenkalkulationen überwunden werden   * eine, die als Datenquelle für die Eingabeparameter des Modells dient und die andere verwendet für Berechnungen auf der Grundlage der resultierenden Geometriedaten.


</div>

## Cell binding 


<small>(v0.20)</small> 

It is possible to bind the content of cells to other spreadsheet cells. This can be useful when dealing with large tables or to get cell content from another spreadsheet.

### Create binding 

To bind, for example, the cell range A3-C4 to the cell range B1-D2   *

1.  Select the cell range A3-C4.
2.  Right-click and select **Bind...** from the context menu.
3.  The **Bind Spreadsheet Cells** dialog opens.
4.  Set the range B1-D2 for the **To cells**   *
    ![](images/Spreadsheet_binding-dialog.png )
5.  Press **OK**.
6.  Bound cells have a blue border to highlight the binding.
7.  If you now enter something in cell C1, the same will immediately appear in cell B3.

![](images/Spreadsheet_binding-result.png ) 
*The spreadsheet may now look like this*

### Change binding 

1.  Right-click a bound cell (there is no need to highlight the whole bound range) and select **Bind...** from the context menu.
2.  The **Bind Spreadsheet Cells** dialog opens.
3.  Change one or more options. Note that the **Bind cells**, the bound cell range, cannot be changed.
4.  Press **OK**.

### Remove binding 

1.  Right-click a bound cell (there is no need to highlight the whole bound range) and select **Bind...** from the context menu.
2.  The **Bind Spreadsheet Cells** dialog opens.
3.  Press **Unbind**.

### Notes

-   The **Hide dependency of binding** option can be used to prevent problems with cyclic dependencies between spreadsheets. Selecting it is necessary when, for example, cells in *Spreadsheet A* are bound to *Spreadsheet B*, while cells in *Spreadsheet B*, in turn, are bound to some other cells in *Spreadsheet A*. This option should be used with caution   *
    -   Hiding dependencies can be dangerous because broken dependencies can damage your FreeCAD file. For example, when you delete a spreadsheet you will not be warned about hidden dependencies.
    -   When you open a document with a spreadsheet containing a hidden dependency, you will get the spreadsheet marked to be recomputed. This is because a cyclic dependency cannot be recomputed automatically. To recompute the [Std Refresh](Std_Refresh.md) tool must be used.
-   The cell binding has a range check and warns you about mismatched ranges. For example binding 1x3 cells to 3x2 cells cannot work because it is unknown which 3 cells of the original 6 cells should be used.
-   You cannot change the cell range of an existing binding. You must first unbind the cells and then create a new binding.
-   The frame color indicating the binding cannot be changed yet.

## Configuration tables 


<small>(v0.20)</small> 

You can use Spreadsheets to create configuration tables with sets of predefined parameters for your model, and then dynamically change which configuration to use. See [this Forum post](https   *//forum.freecadweb.org/viewtopic.php?f=17&t=42183) if you want to know more about the inner workings of this feature.


<div class="mw-collapsible mw-collapsed toccolours">

Expand this section for a brief tutorial on creating a configuration table.


<div class="mw-collapsible-content">

1.  In a new document, first create a [Std Part](Std_Part.md), then create a [Part Box](Part_Box.md), a [Part Cylinder](Part_Cylinder.md) and a Spreadsheet.
2.  The Box and the Cylinder are automatically placed in the [Std Part](Std_Part.md) container. Manually put the Spreadsheet in the container as well.
3.  In the Spreadsheet enter the content as shown below. Set the alias for B2 as {{Value|width}}, C2 as {{Value|length}} and D2 as {{Value|radius}}   *
    ![](images/Spreadsheet_configuration_table_screenshot_4.png )
4.  Bind the [expressions](Expressions.md) {{Value|Spreadsheet.width}} and {{Value|Spreadsheet.length}} to the Box\'s properties **Width** and **Length**, respectively   *
    ![](images/Spreadsheet_configuration_table_screenshot_2.png )
5.  Bind the expression {{Value|Spreadsheet.radius}} to the Cylinder\'s property **Radius**. Also change the **Height** of the Cylinder to {{Value|5 mm}} so that it is lower than the Box.
6.  Right-click the cell A2 in the Spreadsheet and select **Configuration table...** from the context menu.
7.  The **Setup Configuration Table** dialog opens.
8.  Enter the following   *
    ![](images/Spreadsheet_configuration_table_screenshot_5.png )
9.  Press **OK**.
10. A new property called **Configuration** is be added to the [Std Part](Std_Part.md) container to choose the configuration as shown below   *
    ![](images/Spreadsheet_configuration_table_screenshot_6.png )

You can use either a [Std Link](Std_LinkMake.md) or a [PartDesign SubShapeBinder](PartDesign_SubShapeBinder.md) to instantiate a [Variant Instance](https   *//forum.freecadweb.org/viewtopic.php?f=17&t=42183&p=532130#p532130) of a configurable object with the following steps   *

1.  Create a [Std Link](Std_LinkMake.md) to the [Std Part](Std_Part.md) container and set its **Link Copy On Change** property to {{Value|Enabled}}.
2.  Move the Link to a new place by changing its **Placement** so that it is easier to distinguish from the original object.
3.  Select a different **Configuration** for the Link to create a variant instance.

Similar steps apply to a [PartDesign SubShapeBinder](PartDesign_SubShapeBinder.md), except that its property for activating a variant instance is called **Binder Copy On Change**.


</div>


</div>

## Grundlagen Skripten 


```python
import Spreadsheet
sheet = App.ActiveDocument.addObject("Spreadsheet   *   *Sheet","MySpreadsheet")
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

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Spreadsheet Workbench/de
