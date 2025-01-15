# WikiPages/de
Diese Seite ist eine Erweiterung der Seite [Hilfe:Editieren](Help_Editing.md) und gibt allgemeine Richtlinien für das Schreiben und Aktualisieren der FreeCAD-Wiki-Dokumentation. Sie ist eine Zusammenfassung einiger Diskussionen und Sitzungen zur Ideenfindung



## Vor dem Beginn 

-   Diese Wiki-Dokumentation basiert auf [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki), derselben Software, die auch [Wikipedia](https://de.wikipedia.org/wiki/Wikipedia:Hauptseite) nutzt. Wenn du bereits Beiträge zu Wikipedia geleistet hast, sollte das Bearbeiten von FreeCAD-Wiki-Seiten einfach sein.
-   Im Gegensatz zu Wikipedia ist das FreeCAD-Wiki schreibgeschützt, um Spam zu vermeiden. Du kannst [im Forum](http://forum.freecadweb.org/viewtopic.php?f=21&t=6830) beantragen, dass ein Konto für dich angelegt wird.
-   Wenn du noch nie Wiki-Software verwendet hast, gehe zu [Hilfe:Bearbeitung](Help_Editing.md), um dich mit dem Markup vertraut zu machen, das zur Bearbeitung von Seiten verwendet wird.
-   Für fortgeschrittene Anwendung der Wiki-Software siehe [MediaWiki Hilfe:Übersicht](https://www.mediawiki.org/wiki/Help:Contents/de). Nicht alle Funktionen von MediaWiki sind in diesem FreeCAD-Wiki verfügbar, aber viele von ihnen sind es.
-   Wir möchten, dass die Dokumentation einfach zu lesen ist, vermeide also die Verwendung komplexer Funktionen. Halte es einfach.
-   Verwende einen Sandkasten, um deinen Code zu testen, z.B. [FreeCADDocu:Sandbox](FreeCADDocu_Sandbox.md) oder eine bestimmte Seite mit deinem Namen [Sandbox:DeinName](Sandbox_DeinName.md). Sandkasten-Seiten müssen der Sandbox-Kategorie gelistet werden. Dies geschieht durch hinzufügen von [[Category:Sandbox]] am Ende des Wiki-Codes.
-   Bitte beachte die Übersetzungen. Das FreeCAD-Wiki verwendet eine automatische Übersetzungsunterstützung, um Seiten in vielen Sprachen bereitzustellen. Jede Seite kann in mehreren Sprachversionen existieren. Auf vielen Seiten sieht man (Bereichs-) Markierungen wie <translate>...</translate> und viele einzelne Markierungen wie . Letztere kennzeichnen sogenannte Übersetzungseinheiten (translation units) und werden durch das Übersetzungssystem erstellt; sie sollten nie manuell erstellt werden. Sie verbinden die Überschriften und Absätze mit ihren übersetzten Versionen. Du solltest sie nicht ändern, denn das würde diese Verweise zerstören. Es ist aber in Ordnung, Absätze zu verschieben oder den Wortlaut zu ändern, solange die zugehörigen Kennzeichen beibehalten werden. Wenn du eine Überschrift oder einen Absatz löschst, solltest du auch die zugehörigen Kennzeichen löschen. Bitte sei dir bewusst, dass sich das Ändern von existierenden Überschriften und Absätze auch auf bestehende Übersetzungen auswirkt. Das gilt nicht beim Hinzufügen von neuem Material, weil das System nach deinen Änderungen automatisch neue Kennzeichen hinzufügt. Mehr Informationen findest du unter [Lokalisierung](Localisation/de.md) und den Original-Seiten [Mediawiki:Extension:Translate page](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example).



## Allgemeine Richtlinien 



### Präzise Beschreibungen 

Bei der Beschreibung von FreeCAD sollte man präzise formulieren, auf den Punkt kommen und Wiederholungen vermeiden. Beschreibe, was FreeCAD *macht*, nicht was FreeCAD *nicht macht*. Umgangssprachliche Ausdrücken wie \"ein paar\" sollten vermieden werden; besser ist es, dass man \"mehrere\" verwendet, wenn es sich um eine unbestimmte Anzahl handelt, oder dass man die korrekte Menge angibt.

Schlechte Beschreibung
:   Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md): Der PartDesign-Arbeitsbereich ist ein Arbeitsbereich zur Teilekonstruktion, der darauf abzielt, Werkzeuge für die Modellierung komplexer Festkörperkörperteile bereitzustellen.





Gute Beschreibung
:   Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md): Zielt darauf ab, Werkzeuge für die Modellierung komplexer Festkörperteile bereitzustellen.



### Zentralisierte Informationen 

Vermeide es, die gleichen Informationen an verschiedenen Orten zu duplizieren. Füge die Informationen in eine neue Seite ein und verweise von anderen Seiten, die diese Informationen benötigen, auf diese Seite.

Verwende keine [Transklusion](https://de.wikipedia.org/wiki/Transklusion) von (ganzen) Seiten ([Templates_and_transcluding_pages](Help:Editing#Templates_and_transcluding_pages.md), Vorlagen und Transklusion von Seiten, leider nur engl.), da dies die Übersetzung des Wikis erschwert. Verwende nur die unten unter [Vorlagen](#Vorlagen.md) beschriebenen Vorlagen (Templates).



### Gestaltung

Für die Gestaltung der Hilfeseiten werden Vorlagen (Templates) eingesetzt. Sie sorgen für ein einheitliches Aussehen der Dokumentation und eine einheitliche Benutzerführung. Es gibt eine Vorlage für Menübefehle, wie **Datei → Speichern**, eine Vorlage zum Darstellen von zu drückenden Tasten, wie **Shift**, eine zum Anzeigen eines booleschen Wertes `True` usw. Bitte mache dich vor dem Schreiben von Hilfeseiten mit dem Abschnitt [Vorlagen](#Vorlagen.md) vertraut.



### Temporäre Hinweise 

Wird an einer großen Seite gearbeitet, empfiehlt es sich, die Seite entweder als *in Arbeit* oder als *unfertig* zu kennzeichnen. Dadurch wird sichergestellt, dass die Wiki-Administratoren die Seite nicht als *fertig zur Übersetzung* markieren, während sie noch häufig geändert wird.

Um eine Seite zu kennzeichnen, kann entweder  (Seite in Bearbeitung) oder  (unfertige Dokumentation) als erste Zeile eingefügt werden. Mit  werden andere eingeladen, die Seite mit dir zusammen fertigzustellen, während  anzeigt, dass du die Arbeit selbst erledigen wirst und andere dir etwas Zeit geben sollen.

Wenn die Arbeit erledigt ist, vergiss bitte nicht, die Hinweise zu entfernen!



## Beispiele

Um dich schnell mit der Struktur und dem Stil des FreeCAD-Wikis vertraut zu machen, schaue dir die Modell-Seite an: [GuiBefehl Modell](GuiCommand_model/de.md).


<div class="mw-collapsible mw-collapsed toccolours">



## Struktur


<div class="mw-collapsible-content">

Das [Anwenderzentrum](User_hub/de.md) enthält ein [Inhaltsverzeichnis](Online_Help_Toc/de.md). Dies wird als Hauptreferenz für die automatische Erstellung der Offline-Hilfe, die du von FreeCAD aus erreichen kannst, sowie der Offline-PDF-Dokumentation verwendet.

Die Vorlage [Template:Docnav](Template_Docnav.md) dient dem sequentiellen Verknüpfen von Seiten, entsprechend der Struktur des der [Inhaltsverzeichnisses](Online_Help_Toc/de.md). Siehe Tabelle [Vorlagen](#Vorlagen.md) für eine Liste aller Vorlagen.



### Seitennamen

Seitennamen sollten kurz sein, und sie sollten \"Title Case\" verwenden: Jedes Wort sollte mit einem Großbuchstaben beginnen, es sei denn, es handelt sich um Artikel (articles), Verhältniswörter (prepositions), Bindewörter (conjunctions) oder Partikel (grammatical particles), wie z.B. \"of\", \"on\", \"in\", \"a\", \"an\", \"and\".

Schlechter Seitenname:
:   Construction of AeroCompany airplanes





Guter Seitenname:
:   Construction of AeroCompany Airplanes

Die Namen der Seiten für die obersten Ebene der Arbeitsbereiche muss das Format XYZ Workbench haben, wobei XYZ der Name des Arbeitsbereichs ist, zum Beispiel [PartDesign Workbench](PartDesign_Workbench.md) (Übersetzt: Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md)). Und die Namen der Seiten, die die Befehle (oder Werkzeuge) beschreiben, die zu einem Arbeitsbereich gehören, müssen dieses Format haben: XYZ Command, zum Beispiel [PartDesign Pad](PartDesign_Pad.md) (Übersetzt: [PartDesign Block](PartDesign_Pad/de.md)). Dabei ist zu beachten, dass der Befehlsname so, wie er im Quellcode vorkommt, geschrieben wird.



### Überschriften

Absatzüberschriften sollten kurz sein und \"Sentence Case\" verwenden: Alle Wörter, außer dem ersten und Namen (proper names), sollten kleingeschrieben werden. Es sollten keine H1-Überschriften (= Überschrift =) als Wiki-Textauszeichnung verwendet werden, da der Seitentitel automatisch als Hauptüberschrift H1 hinzugefügt wird.



### Verweise

Nach Möglichkeit sollte für einen Verweis der Name des ursprünglichen Verweises verwendet werden, um die referenzierte Seite in der gedruckten oder der netzunabhängigen Dokumentation deutlich hervorzuheben. Die Verwendung von nicht aussagekräftigen Wörtern für den Verweis sollte vermieden werden..

Schlechter Verweis
:   Für weitere Informationen zum Zeichnen von 2D-Objekten klicke [hier](Draft_Workbench/de.md).





Guter Verweis
:   Weitere Informationen zum Zeichnen von 2D-Objekten finden sich im Arbeitsbereich [Draft](Draft_Workbench/de.md).

Das bevorzugte Format für einen Verweis ist:

[Name of Page](Name_of_Page.md)

Übersetzt:

[Name der Seite](Name_of_Page/de.md)

Dabei ist zu beachten, dass der Teil vor dem |-Zeichen, der eigentliche Verweis ist, für den Groß- und Kleinschreibung relevant sind. Lautet der Seitenname Name_of_page, wird der Verweis fehlschlagen, wenn Name_of_Page (Großbuchstabe P) eingegeben wird. Vor dem Zeichen | sollten alle Leerzeichen durch Unterstriche (_) ersetzt werden. Dies dient der Unterstützung von Übersetzern, die eine Übersetzungssoftware verwenden. Ohne die Unterstriche würde der Verweis von der Software übersetzt werden, was nicht erwünscht ist.

Um zu einem bestimmten Abschnitt zu verweisen, wird ein #-Zeichen und die zugehörige Überschrift zum Seitennamen hinzugefügt. Beispiel:

[WikiPages](WikiPages#Links.md)

Übersetzt:

[WikiSeiten](WikiPages/de#Verweise.md)

Innerhalb derselben Seite kannst der Seitenname weggelassen werden. Beispiel:

[Verweise](#Verweise.md)

Um einen Verweis zum Anfang der Seite zu erstellen, lässt sich Folgendes verwenden:

</translate>{{Top}}<translate>

Diese Vorlage sollte, abhängig von der Sprache der Seite, automatisch den richtigen Text anzeigen. Ein Verweis zum Seitenanfang ist besonders nützlich für lange Seiten, da er dem Benutzer erlaubt, schnell zum Inhaltsverzeichnis zurückzuspringen. Er kann an das Ende eines jeden Absatzes gesetzt werden. Es ist zu beachten, dass sich vor und nach der Vorlage eine Leerzeile befindet.

Bildverweis

:   <img alt="Optionaler Text, der beim Schweben über dem Bild angezeigt wird\|link=Draft_Wire" src=images/Draft_Wire.svg  style="width:24px;">

Um ein Bild als Verweis zu benutzen:

![](images/)

Bildverweis + Textverweis
:   <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Linienzug](Draft_Wire/de.md)

Wird der optionale Text weggelassen, wird der Verweis selbst beim Schweben über dem Bild angezeigt; dies ist vorzuziehen. Es sollte auch ein Textverweis nach dem Bildverweis hinzugefügt werden:

![](images/)_[Linienzug](Draft_Wire/de.md)



### Seiten der Arbeitsbereiche 

Die oberste Seite eines Arbeitsbereichs sollte beginnen mit

-   einer Beschreibung wofür der Arbeitsbereich eingesetzt wird.
-   einer Abbildung, die die Beschreibung bildlich darstellt.

Siehe [Bildschirmaufnahme](#Bildschirmaufnahme.md) für Wissenswertes zum Einfügen von Bildern.



### Befehlsseiten

Die Befehlsseiten, die die Werkzeuge eines Arbeitsbereichs beschreiben, sollten nicht zu lang sein, sie sollten nur erklären, was ein Befehl tun kann und was nicht, und wie er eingesetzt wird. Bilder und Beispiele sollten auf ein Minimum reduziert bleiben; Anleitungen können weitere Einzelheiten zur Anwendung des Werkzeugs sowie detaillierte Schritt-für-Schritt-Beschreibungen liefern.

Auf der Seite [GuiGUIBefehl Modell](GuiCommand_model/de.md) finden sich weitere Einzelheiten.



### Anleitungen

Eine gut geschriebene Anleitung (Tutorial) sollte den Benutzer lehren, bestimmte praktische Ergebnisse schnell zu erreichen. Sie sollte nicht zu lang sein, aber sie sollte eine ausreichende Anzahl von Schritt-für-Schritt-Beschreibungen und Bildern enthalten, die dem Benutzer die Verwendung der verschiedenen Werkzeuge erklären.

Beispiele findet man auf der Seite [Tutorien](Tutorials/de.md) (Anleitungen).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Vorlagen


<div class="mw-collapsible-content">

Das Gestalten der FreeCAD-Wiki-Seiten wird durch die Verwendung von Vorlagen (Templates) erreicht (Siehe [Help:Editing#Templates_and_transcluding_pages](Help:Editing#Templates_and_transcluding_pages.md), leider nur auf Englisch). Sie sorgen für ein einheitliches Erscheinungsbild aller Seiten und ermöglichen auch, das Wiki neu zu gestalten. Die komplette Liste der definierten Vorlagen findet man unter [Special:PrefixIndex/Template:](Special:PrefixIndex/Template:.md) (Alle Seiten (mit Präfix)). Aber bitte nur die in den Tabellen unten aufgeführten Vorlagen einsetzen. Nur in ganz besonderen Fällen sollten die HTML-Kennzeichen direkt verwendet werden.

Auf den Verweis zur Vorlage klicken, um die Gebrauchsanleitung für eine Vorlage anzusehen und zu sehen, wie sie aufgebaut ist. Vorlagen sind eine leistungsstarke Funktion der MediaWiki-Software; Du solltest ein erfahrener Wiki-Benutzer sein, wenn du Ergänzungen und Änderungen an bestehenden Vorlagen vorschlagen möchtest. Wenn Vorlagen falsch aufgebaut sind, erschweren sie die Übersetzung von Seiten in andere Sprachen; daher sollte ihr Einsatz auf Textformatierung beschränkt werden und die Transklusion von Seiten sollte vermieden werden. Siehe [MediaWiki Hilfe:Templates (Vorlagen)](https://www.mediawiki.org/wiki/Help:Templates/de)



### Einfache Vorlagen 

Diese Vorlagen akzeptieren einen einfachen Textparameter und formatieren ihn in einem bestimmten Stil.

++++
| Vorlage                                                                                                       | Erscheinungsbild                           | Beschreibung                                                                                                                                                                                                                                                                                                           |
+===============================================================================================================+============================================+========================================================================================================================================================================================================================================================================================================================+
| [Top](Template_Top.md)                                                                                |                             | Wird eingesetzt, um einen Verweis zum Anfang der Seite hinzuzufügen.                                                                                                                                                                                                                                                   |
|                                                                                                               | {{Top}}                                    |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [Emphasis](Template_Emphasis.md)                                                                      |                             | Wird verwendet, um ein Textabschnitt hervorzuheben.                                                                                                                                                                                                                                                                    |
|                                                                                                               | **Hervorhebung**                  |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [KEY](Template_KEY.md)                                                                                |                             | Wird eingesetzt, um eine Taste anzugeben, die gedrückt werden soll.                                                                                                                                                                                                                                                    |
|                                                                                                               | **Alt**                                |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [ASCII](Template_ASCII.md)                                                                            |                             | Wird eingesetzt, um eine ASCII-Taste in einem Bild (.svg) anzugeben, die gedrückt werden soll. Das gewünschte Zeichen oder die Nummer des ASCII-Codes des Zeichens muss angegeben werden.                                                                                                                              |
|                                                                                                               | {{ASCII|A}}                                |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [Button](Template_Button.md)                                                                          |                             | Wird eingesetzt, um eine Schaltfläche der grafischen Benutzeroberfläche darzustellen, die gedrückt werden soll.                                                                                                                                                                                                        |
|                                                                                                               | **Abbrechen**                       |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [RadioButton](Template_RadioButton.md)                                                                |                             | Wird eingesetzt, um einen Auswahlknopf der grafischen Benutzeroberfläche darzustellen, der {{RadioButton|TRUE|Aktiviert}} oder {{RadioButton|FALSE|Deaktiviert}} werden soll.                                                                                                              |
|                                                                                                               | {{RadioButton|Option}}                     |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [CheckBox](Template_CheckBox.md)                                                                      |                             | Wird eingesetzt, um ein Kontrollkästchen der grafischen Benutzeroberfläche darzustellen, das {{CheckBox|TRUE|Aktiviert}} oder {{CheckBox|FALSE|Deaktiviert}} werden soll.                                                                                                                  |
|                                                                                                               | {{CheckBox|Option}}                        |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [SpinBox](Template_SpinBox.md)                                                                        |                             | Wird eingesetzt, um eine Spinbox der grafischen Benutzeroberfläche darzustellen, die geändert werden soll.                                                                                                                                                                                                             |
|                                                                                                               | {{SpinBox|1.50}}                           |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [ComboBox](Template_ComboBox.md)                                                                      |                             | Wird eingesetzt, um eine ComboBox der grafischen Benutzeroberfläche darzustellen, die geändert werden soll.                                                                                                                                                                                                            |
|                                                                                                               | {{ComboBox|Menu 1}}                        |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [LineEdit](Template_LineEdit.md)                                                                      |                             | Wird eingesetzt, um ein Texteingabefeld (LineEdit-Widget) der grafischen Benutzerschnittstelle darzustellen, das eine Eingabe erfordert.                                                                                                                                                                               |
|                                                                                                               | {{LineEdit|Metal Nickel (Ni)}}             |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [FALSE](Template_FALSE.md), [false](Template_false.md)                                        |                             | Wird eingesetzt, um den booleschen Wert falsch darzustellen, z.B. als Eigenschaft im [Eigenschafteneditor](property_editor/de.md). Dies ist eine Abkürzung. Da es sich um einen Wert handelt, sollte die Vorlage [Value](Template_Value.md) {{Value|false}} bevorzugt werden.            |
|                                                                                                               | `False`                                  |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               | , {{false}}                  |                                                                                                                                                                                                                                                                                                                        |
++++
| [TRUE](Template_TRUE.md), [true](Template_true.md)                                            |                             | Wird eingesetzt, um den booleschen Wert wahr darzustellen, z.B. als Eigenschaft im [Eigenschafteneditor](property_editor/de.md). Dies ist eine Abkürzung. Da es sich um einen Wert handelt, sollte die Vorlage [Value](Template_Value.md) {{Value|true}} bevorzugt werden.               |
|                                                                                                               | `True`                                   |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               | , {{true}}                   |                                                                                                                                                                                                                                                                                                                        |
++++
| [MenuCommand](Template_MenuCommand.md)                                                                |                             | Wird eingesetzt, um die Lage eines Befehls innerhalb eines bestimmten Menüs anzugeben.                                                                                                                                                                                                                                 |
|                                                                                                               | **Datei → Speichern**          |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [FileName](Template_FileName.md)                                                                      |                             | Wird eingesetzt, um den Namen einer Datei oder eines Verzeichnisses anzugeben.                                                                                                                                                                                                                                         |
|                                                                                                               | **Dateiname**                     |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [SystemInput](Template_SystemInput.md)                                                                |                             | Wird eingesetzt, um einen vom Benutzer einzugebenden Text darzustellen.                                                                                                                                                                                                                                                |
|                                                                                                               | {{SystemInput|Gib diesen Text ein}}        |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [SystemOutput](Template_SystemOutput.md)                                                              |                             | Wird eingesetzt, um eine Textausgabe des Systems darzustellen.                                                                                                                                                                                                                                                         |
|                                                                                                               | {{SystemOutput|Ausgabetext}}               |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [Incode](Template_Incode.md)                                                                          |                             | Wird eingesetzt, um Inline-Quellcode mit einer Monospace-Schriftart einzubinden. Er sollte in eine Zeile passen.                                                                                                                                                                                                       |
|                                                                                                               | `import FreeCAD`                  |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [PropertyView](Template_PropertyView.md)                                                              |                             | Wird eingesetzt, um eine Ansicht-Eigenschaft im [Eigenschafteneditor](property_editor/de.md) darzustellen. Ansicht-Eigenschaften sind z.B. {{emphasis|Linienfarbe}}, {{emphasis|Linienbreite}}, {{emphasis|Punktfarbe}}, {{emphasis|Punktgröße}}, usw. |
| [PropertyView/de](Template:PropertyView/de.md)                                                        | **Farbe**                     |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               | {{PropertyView/de|Farbe}}    |                                                                                                                                                                                                                                                                                                                        |
++++
| [PropertyData](Template_PropertyData.md)                                                              |                             | Wird eingesetzt, um eine Daten-Eigenschaft im [Eigenschafteneditor](property_editor/de.md) darzustellen. Daten-Eigenschaften sind für verschiedene Objekttypen unterschiedlich.                                                                                                                                |
| [PropertyData/de](Template:PropertyData/de.md)                                                        | **Position**                  |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               | {{PropertyData/de|Position}} |                                                                                                                                                                                                                                                                                                                        |
++++
| [Properties Title](Template_Properties_Title.md) / [TitleProperty](Template_TitleProperty.md) |                             | Wird eingesetzt, um die Benennung einer Eigenschaftengruppe im [Eigenschafteneditor](property_editor/de.md) darzustellen. Die Benennung wird nicht in das automatische Inhaltsverzeichnis aufgenommen.                                                                                                         |
|                                                                                                               | {{Properties_Title|Basis}}                 |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [Obsolete](Template_Obsolete.md)                                                                      |                             | Wird eingesetzt, um darzustellen, dass eine bestimmte Funktion ab einer bestimmten FreeCAD-Version veraltet ist.                                                                                                                                                                                                       |
|                                                                                                               | {{Obsolete/de|0.19}}                       |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [Version](Template_Version.md)                                                                        |                             | Wird eingesetzt, um darzustellen, dass eine Funktion mit einer bestimmten FreeCAD-Version eingeführt wurde.                                                                                                                                                                                                            |
|                                                                                                               | {{Version/de|0.18}}                        |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [VersionMinus](Template_VersionMinus.md)                                                              |                             | Wird eingesetzt, um darzustellen, dass eine Funktion bis zu einer bestimmten FreeCAD-Version zur Verfügung stand.                                                                                                                                                                                                      |
|                                                                                                               | {{VersionMinus/de|0.16}}                   |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [VersionPlus](Template_VersionPlus.md)                                                                |                             | Wird eingesetzt, um darzustellen, dass eine Funktion seit einer bestimmten FreeCAD Version zur Verfügung steht.                                                                                                                                                                                                        |
|                                                                                                               | {{VersionPlus/de|0.17}}                    |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [ColoredText](Template_ColoredText.md)                                                                |                             | Diese Vorlage wird eingesetzt, um den Hintergrund, den Text oder Hintergrund und Text einzufärben. (Die Seite [FarbigerText](Template_ColoredText.md) enthält weitere Beispiele)                                                                                                                               |
|                                                                                                               | {{ColoredText|Farbiger Text}}              |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++
| [ColoredParagraph](Template_ColoredParagraph.md)                                                      |                             | Diese Vorlage wird eingesetzt, um den Hintergrund, den Text oder Hintergrund und Text eines ganzen Absatzes einzufärben. (Die Seite [ColoredParagraph](Template_ColoredParagraph.md) enthält weitere Beispiele)                                                                                                |
|                                                                                                               | {{ColoredParagraph|Farbiger Absatz}}       |                                                                                                                                                                                                                                                                                                                        |
|                                                                                                               |                                         |                                                                                                                                                                                                                                                                                                                        |
++++



### Komplexe Vorlagen 

Diese Vorlagen erfordern mehr Eingabeparameter oder erzeugen einen Textblock mit einem bestimmten Format.

++++
| Vorlage                                                                                          | Erscheinungsbild                                                                                                                        | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                    |
+==================================================================================================+=========================================================================================================================================+=================================================================================================================================================================================================================================================================================================================================================================================================+
| [Prettytable](Template_Prettytable.md)                                                   | Diese Tabelle                                                                                                                           | Wird eingesetzt, um Tabellen wie diese zu formatieren. Es können zusätzliche Tabelleneigenschaften hinzugefügt werden.                                                                                                                                                                                                                                                                          |
++++
| [Caption](Template_Caption.md)                                                           |                                                                                                                               | Wird eingesetzt, um eine Bildunterschriift hinzuzufügen. Sie kann linksbündig oder mittig ausgerichtet sein.                                                                                                                                                                                                                                                                                    |
|                                                                                                  | <div style="width:400px;">                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  | 
*Erläuterung zu einer Abbildung*                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  | </div>                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                 |
++++
| [Clear](Template_Clear.md)                                                               |                                                                                                                                         | Wird eingesetzt, um Spalten zu löschen. Die Definition der Vorlage enthält einen Verweis zu einer detaillierten Erklärung. Die Vorlage wird oft verwendet, um zu verhindern, dass ein Text Bilder umfließt, die in keinem Zusammenhang mit dem Text stehen.                                                                                                                                     |
++++
| [Code](Template_Code.md)                                                                 |                                                                                                                          | Wird eingesetzt, um mehrzeilige Code-Beispiele mit einer Monospace-Schriftart einzubinden. Die Standardsprache ist Python, es können aber auch andere Sprachen angegeben werden.                                                                                                                                                                                                                |
|                                                                                                  | {{Code|Code=import FreeCAD}}                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      | [Python](Python/de.md)-Code sollte sich an die allgemeinen Empfehlungen halten, die im [PEP8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) (Stil-Leitfaden für Python-Code) aufgestellt wurden. Insbesondere sollten Klammern unmittelbar auf den Funktionsnamen folgen, und auf ein Komma sollte ein Leerzeichen folgen. Dies macht den Code besser lesbar. |
++++
| [CodeDownload](Template_CodeDownload.md)                                                 |                                                                                                                          | Wird eingesetzt, um eine Verknüpfung zu einer [Makro](Macros/de.md)-Seite zu erstellen.                                                                                                                                                                                                                                                                                                 |
|                                                                                                  | {{CodeDownload|https://wiki.freecad.org/Main_Page|Eine Benennung}}                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                 |
++++
| [Codeextralink](Template_Codeextralink.md)                                               |                                                                                                                          | Wird eingesetzt, wenn der Code eines [Makros](Macros/de.md) zu umfangreich ist, um im Wiki bereitgestellt zu werden. Der Code kann dann woanders bereitgestellt werden und der nackte Verweis dorthin wird in dieser Vorlage angegeben. Der [Addon-Manager](Std_AddonMgr/de.md) verwendet diesen Verweis.                                                                       |
|                                                                                                  | {{Codeextralink|https://wiki.freecad.org/Main_Page}}                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                 |
++++
| [Unechte Überschrift](Template_Fake_heading.md)                                          |                                                                                                                          | Wird eingesetzt, um eine Überschrift zu erstellen, die nicht automatisch in das für die Offline-Dokumentation verwendete Inhaltsverzeichnis aufgenommen wird.                                                                                                                                                                                                                                   |
|                                                                                                  | {{Fake heading|Heading|2}}                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                 |
++++
| [GuiCommand](Template_GuiCommand.md)                                                     | Siehe [Gui-Befehl](Gui_Command/de.md) und [GuiBefehl Modell](GuiCommand_model/de.md)                                    | Wird eingesetzt, um einen Kasten mit nützlichen Informationen für die Dokumentation von Befehlen (Werkzeugen) eines Arbeitsbereichs zu erstellen.                                                                                                                                                                                                                                               |
++++
| [TutorialInfo](Template_TutorialInfo.md)                                                 | Siehe als Beispiel [Basic modeling tutorial](Basic_modeling_tutorial.md)                                                        | Wird eingesetzt, um einen Kasten mit nützlichen Informationen für die Dokumentation von [Anleitungen](Tutorials/de.md) zu erstellen.                                                                                                                                                                                                                                                    |
++++
| [Macro](Template_Macro.md)                                                               | Siehe Beispiel [Makro FlattenWire](Macro_FlattenWire/de.md)                                                                     | Wird eingesetzt, um eine Box mit nützlichen Informationen für die Dokumentation von [Makros](macros/de.md) zu erstellen.                                                                                                                                                                                                                                                                |
++++
| [Docnav](Template_Docnav.md)                                                             |                                                                                                                          | Wird eingesetzt, um eine Leiste mit Pfeilen und den entsprechenden Verweisen zu erstellen, was nützlich ist, um Seiten in eine bestimmte Reihenfolge zu bringen.                                                                                                                                                                                                                                |
|                                                                                                  |                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                 |
++++
| [VeryImportantMessage](Template_VeryImportantMessage.md)                                 |                                                                                                                          | Wird eingesetzt, um einen hervorgehobenen Kasten mit einer sehr wichtigen Nachricht zu erstellen. Die Vorlage solltes sparsam eingesetzt werden und nur um auf größere Probleme in der Funktionalität der Software, Abkündigungen von Werkzeugen und Ähnliches hinzuweisen.                                                                                                                     |
|                                                                                                  | **Important Message**                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                 |
++++
| [Page in progress](Template_Page_in_progress.md)                                         |                                                                                                                          | Wird eingesetzt auf Seiten, die noch in Arbeit sind oder gerade überarbeitet werden. Vergiss nicht, dies zu entfernen, wenn die Seite fertig ist.                                                                                                                                                                                                                                               |
|                                                                                                  | {{Page in progress|Page in progress}}                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                 |
++++
| [UnfinishedDocu](Template_UnfinishedDocu.md)                                             |                                                                                                                          | Wird eingesetzt, um ein hervorgehobenes Feld zu erstellen, das eine unfertige Dokumentationsseite anzeigt.                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                 |
++++
| [Softredirect](Template_Softredirect.md)                                                 |                                                                                                                                         | Wird anstelle der normalen Umleitung (Redirect) eingesetzt, wenn auf eine spezielle Seite (z.B. Media: oder Category:) umgeleitet wird; in solchen Fällen ist die normale Umleitung deaktiviert.                                                                                                                                                                                                |
++++
| [Quote](Template_Quote.md)                                                               |                                                                                                                          | Wird eingesetzt, um einen Textkasten mit einem wörtlichen Zitat und einer Referenz zu erstellen.                                                                                                                                                                                                                                                                                                |
|                                                                                                  | {{Quote|text=Rufe "Verwüstung" und lass die Hunde des Krieges los.|sign=William Shakespeare|source=''Julius Cäsar'', Akt III, Szene I}} |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                 |
++++
| [Userdocnavi](Template_Userdocnavi.md), [Powerdocnavi](Template_Powerdocnavi.md) |                                                                                                                                         | Werden eingesetzt, um Navigationsboxen für die jeweilige Dokumentation für Benutzer, erfahrene Nutzer und Entwickler zu erstellen. Dies ermöglicht ein schnelles Springen zwischen verschiedenen Abschnitten der Dokumentation. Außerdem ordnen sie die entsprechende Seite der richtigen Kategorie zu.                                                                                         |
++++


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Grafiken


<div class="mw-collapsible-content">

Abbildungen und Bildschirmaufnahmen sind wichtig, um eine vollständige Dokumentation von FreeCAD zu erstellen. Sie sind besonders nützlich, um Beispiele und Anleitungen zu illustrieren. Abbildungen sollten in ihrer Originalgröße angezeigt werden, damit sie genügend Details zeigen und lesbar sind, wenn sie Text enthalten. [Bitmap](Bitmap/de.md)-Bilder sollten nicht in der Größe verändert werden.

Animierte Bilder (GIF) sollten in den allgemeinen Hilfeseiten vermieden werden. Animationen und Videos sollten Anleitungen vorbehalten bleiben, die nicht als Offline-PDF-Dokumentation verwendet werden sollen.

Abbildungen können über die Seite [Special:Upload](Special_Upload.md) hochgeladen werden.



### Namen

Abbildungen sollten einen aussagekräftigen Namen erhalten. Stellt das Bild Merkmale eines bestimmten Befehls dar, sollte der originale, englische Name des Befehls mit angehängtem `_example` verwendet werden.

-   Für den Befehl [Draft Offset](Draft_Offset.md) sollte das Bild also `Draft_Offset_example.png` heißen.



### Bildschirmaufnahme

Empfohlene Größen für Bildschirmaufnahmen sind:

-   Normale 400x200 (oder Breite = 400 und Höhe \<= 200), für [GUI-Befehl](Gui_Command/de.md)-Seiten, damit das Bild in den linken Teil der Seite passt, und für andere Standard-Schnappschüsse.
-   Normale 600x400 (oder Breite = 600 und Höhe \<= 400), für [GUI-Befehl](Gui_Command/de.md)-Seiten, wenn wirklich ein größeres Bild benötigt wird und das Bild trotzdem in den linken Teil der Seite passen soll, und für andere Standard-Schnappschüsse.
-   Normale 1024x768 (oder Breite=1024 und Höhe\<=768), nur für Aufnahmen des kompletten Bildschirms.
-   Für Darstellungen von Details sind kleinere Größen möglich.
-   Abbildungen mit größeren Auflösungen sollten vermieden werden, da sie sich schlecht auf andere Arten der Darstellung oder in gedruckte PDF-Dokumentation übertragen lassen.

Es sollten von Desktop- oder Betriebssystemkonfiguration unabhängige Einstellungen für Bildschirmaufnahmen verwendet werden, wenn möglich, die visuellen Voreinstellungen der FreeCAD-Oberfläche.

Um eine Bildschirmaufnahme zu erstellen, können vom Betriebssystem bereitgestellte Werkzeuge verwendet werden oder eines dieser Makros: <img alt="" src=images/Snip.png  style="width:24px;"> [Makro Snip](Macro_Snip/de.md) und <img alt="" src=images/Macro_Screen_Wiki.png  style="width:24px;"> [Makro Bildschirm Wiki](Macro_Screen_Wiki/de.md).



### Text

Um die Übersetzung der Dokumentation zu erleichtern, solllten Bildschirmaufnahmen, die Text enthalten, vermieden werden. Ist dies nicht möglich, sollte man sich überlegen, separate Bilder von Benutzeroberfläche und [3D-Ansicht](3D_view.md) zu machen. Das Bild der 3D-Ansicht kann in allen Übersetzungen weiterverwendet werden, während ein Übersetzer bei Bedarf eine Bildschirmaufnahme der lokalisierten Benutzeroberfläche machen kann.



### Symbole und Grafiken 

Von der Seite [Grafik](Artwork/de.md) ausgehend findet man alle Illustrationen und Symbole, die für FreeCAD erstellt wurden, die auch in den Dokumentationsseiten eingesetzt werden können. Wenn du Symbole beitragen möchtest, lies bitte die [Illustrationsrichtlinien](Artwork_Guidelines/de.md).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Übersetzungen


<div class="mw-collapsible-content">

Gemäß der allgemeinen Übereinkunft ist die englische Seite die Referenzseite im Wiki und muß zuerst erstellt werden. Soll der Inhalt einer Seite geändert werden oder etwas hinzugefügt werden, muß dies zuerst auf der englischen Seite erfolgen und kann, sobald die Aktualisierung abgeschlossen ist, auf die übersetzte Seite übertragen werden.

Das FreeCAD-Wiki unterstützt eine Übersetzungserweiterung, die es ermöglicht, Übersetzungen zwischen Seiten einfacher zu verwalten; Für Einzelheiten siehe [FreeCAD-Wiki übersetzen](Localisation/de#Übersetze_das_FreeCAD_Wiki.md).

Weitere nützliche Quellen sind:

-   [ISO language codes](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes): Zusammenstellung der ISO-Sprachcodes mit zwei Buchstaben, um die zu übersetzende Sprache zu benennen/identifizieren.
-   [Google Translate](http://translate.google.com/): zur Unterstützung beim Übersetzen.
-   [Deepl translator](https://www.deepl.com/translator): zur Unterstützung beim Übersetzen.



## Einige Hinweise für Übersetzer 



### GUI-Befehl übersetzen 

    {{GuiCommand
    |Name=FEM EquationFlux
    |MenuLocation=Solve → Flux equation
    |Workbenches=[FEM](FEM_Workbench.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM tutorial](FEM_tutorial.md)
    }}

Übersetzt:

    {{GuiCommand/fr
    |Name=FEM EquationFlux
    |Name/fr=FEM Équation d'écoulement
    |MenuLocation=Solveur → Équation de flux
    |Workbenches=[Atelier FEM](FEM_Workbench/fr.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM Tutoriel](FEM_tutorial/fr.md)
    }}



### Navi übersetzen 

    {{FEM_Tools_navi}}

Übersetzt:

    {{FEM_Tools_navi/fr}}



### Verweis übersetzen 

    [Part Workbench](Part_Workbench.md)

Übersetzt:

    [Atelier Part](Part_Workbench/fr.md)



### Docnav übersetzen 

    

Übersetzt:

    

Beispiel mit Symbolen:

    

Übersetzt:

    


</div>


</div>



## Seiten erstellen, umbenennen und löschen 



### Seiten erstellen 

Vor dem Erstellen einer neuen Seiten sollte überprüft werden, ob bereits eine ähnliche Seite existiert. Sollte das der Fall sein, ist es meist besser, die vorhandene Seite zu ändern. Im Zweifel bitte zuerst ein neues Thema im [Wiki-Forum](https://forum.freecadweb.org/viewforum.php?f=21) öffnen.

Um eine neue Seite zu erstellen, hat man folgende Möglichkeiten:

-   Die URL mit dem gewünschten Seitennamen aufrufen, z.B.: https://wiki.freecadweb.org/Meine_Neue_Seite/de, und auf \'Erstellen\' klicken.
-   Eine Wiki-Suche nach dem Seitennamen durchführen und auf den roten Text in \'Erstelle die Seite \"Meine Neue Seite\" in diesem Wiki.\' klicken.



### Seiten umbenennen 

Da FreeCAD ein Projekt ist, das ständig weiterentwickelt wird, ist es manchmal notwendig, den Inhalt des Wikis zu überarbeiten. Wenn die Namen von Befehlen im Quellcode geändert werden, müssen die Wiki-Seiten, die sie dokumentieren, ebenfalls umbenannt werden. Dies kann nur von den Wiki-Administratoren durchgeführt werden. Um diese zu informieren, eröffne ein Thema im [Wiki-Forum](https://forum.freecadweb.org/viewforum.php?f=21) und liste den notwendigen Umbenennungsvorgang in diesem Formular auf:

    old name         new name
    Old_page_name_1  New_page_name_1
    Old_page_name_2  New_page_name_2
    ...



### Dateien und Seiten löschen 

Soll eine Datei gelöscht werden, wechselt man auf ihre Seite (https://www.freecadweb.org/wiki/File:***.***) und bearbeitet sie. Unabhängig davon, ob die Seite leer ist oder nicht, wird {{Delete}} als erstes Element der Seite eingefügt und unmittelbar darunter beschrieben, warum die Seite gelöscht werden soll. Zusätzlich wird ein Thema im [Wiki-Forum](https://forum.freecadweb.org/viewforum.php?f=21) eröffnet.

Für Seiten ist das Verfahren dasselbe.



## Diskussion

Das Unterforum [Development/Wiki](http://forum.freecadweb.org/viewforum.php?f=21) im [FreeCAD-Forum](https://forum.freecadweb.org) bietet einen speziellen Raum für die Diskussion von Wiki-Themen, des Wiki-Erscheinungsbildes und alles andere im Zusammenhang mit dem Wiki. Dort kann man Fragen stellen und Vorschläge anbringen.



## Terminologie - Benennungspolitik 



### Englisch

Siehe [Glossar](Glossary.md)



### Andere Sprachen 

-   [Italienisch](Italian_Translation.md)
-   [Französisch](French_Translation.md)
-   [Deutsch](German_Translation.md)
-   [Polnisch](Polish_Translation.md)
-   [Spanisch](Spanish_Translation.md)



---
⏵ [documentation index](../README.md) > [Documentation](Category_Documentation.md) > [Wiki](Category_Wiki.md) > [Wiki Documentation](Category_Wiki%20Documentation.md) > [Administration](Category_Administration.md) > WikiPages/de
