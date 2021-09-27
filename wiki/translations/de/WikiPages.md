# WikiPages/de
{{TOCright}}

Diese Seite ist eine Erweiterung der _ Seite und gibt allgemeine Richtlinien für das Schreiben und Aktualisieren der FreeCAD Wiki Dokumentation. Es fasst mehrere Diskussionen und Ideenfindungssitzungen zusammen

## Vor dem Beginn 

-   Diese Wiki Dokumentation basiert auf [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki), derselben Software, die auch [Wikipedia](https://de.wikipedia.org/wiki/Wikipedia:Hauptseite) nutzt. Wenn du bereits Beiträge zu Wikipedia geleistet hast, sollte das Bearbeiten von FreeCAD Wiki Seiten einfach sein.
-   Im Gegensatz zu Wikipedia ist das FreeCAD Wiki schreibgeschützt, um Spam zu vermeiden. Du musst beantragen, dass ein Konto für dich [im Forum](http://forum.freecadweb.org/viewtopic.php?f=21&t=6830) erstellt wird.
-   Wenn du noch nie Wiki Software verwendet hast, gehe zu _, um dich mit dem Markup vertraut zu machen, das zur Bearbeitung von Seiten verwendet wird.
-   Für fortgeschrittene Anwendung der Wiki Software siehe [MediaWiki Hilfe:Übersicht](https://www.mediawiki.org/wiki/Help:Contents/de). Nicht alle Funktionen von MediaWiki sind in diesem FreeCAD Wiki verfügbar, aber viele von ihnen sind es.
-   Wir möchten, dass die Dokumentation einfach zu lesen ist, vermeide also die Verwendung komplexer Funktionen. Halte es einfach.
-   Verwende einen Sandkasten, um deinen Code zu testen, z.B. _ oder eine bestimmte Seite mit deinem Namen _. Sandkasten-Seiten müssen in der Sandkasten-Kategorie platziert werden. Dies geschieht durch hinzufügen von [[Category:Sandbox]] am Ende des Wiki-Codes.
-   Bitte beachte die Übersetzungen. Das FreeCAD Wiki verwendet automatische Übersetzungsunterstützung, um Seiten in vielen Sprachen anzubieten. Es ist wie eine 3. Dimension: jede Seite kann in mehreren Sprachversionen existieren. Auf vielen Seiten wirst du Markierungen sehen wie <translate>...</translate> und viele Kennzeichnungen wie . Letztere werden durch das Übersetzungssystem erstellt, du solltest sie nie manuell erstellen. Sie verbinden die Überschriften und Paragrafen durch ihre übersetzten Versionen. Du solltest sie nicht ändern, denn das würde diese Verweise zerstören. Es wäre trotzdem in Ordnung, Paragrafen zu verschieben oder den Wortlaut zu ändern, solange die zugehörigen Kennzeichen beibehalten werden. Wenn du eine Überschrift oder einen Paragrafen löschst, solltest du auch die zugehörigen Kennzeichen löschen. Bitte sei dir bewusst, dass sich das Ändern von existierenden Überschriften und Paragrafen auch auf bestehende Übersetzungen auswirkt. Das gilt nicht beim Hinzufügen von neuem Material, weil das System nach deinen Änderungen automatisch neue Kennzeichen hinzufügt. Mehr Informationen findest du unter [Lokalisierung](Localisation/de.md) und den Original-Seiten [Mediawiki:Extension:Translate page](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example).

## Allgemeine Richtlinien 

### Präzise Beschreibungen 

Versuche bei der Beschreibung der FreeCAD Funktionalität prägnant und auf den Punkt zu kommen. Beschreibe, was FreeCAD *tut*, nicht was FreeCAD *nicht tut*. Es könnte Ausnahmen geben, um zu rechtfertigen, warum FreeCAD eine bestimmte Funktionalität nicht unterstützt, z.B. zu klären wie sich FreeCAD von anderen CAD Systemen unterscheidet.

Schlechte Beschreibung
:   [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md): der PartDesign Arbeitsbereich ist ein Arbeitsbereich zur Teilekonstruktion die Werkzeuge für die Modellierung komplexer Volumenkörperteile bereitstellen soll.





Gute Beschreibung

[PartDesign Arbeitsbereich](PartDesign_Workbench/de.md): zielt darauf ab, Werkzeuge für die Modellierung komplexer Festkörperteile bereitzustellen.

### Zentralisierte Informationen 

Vermeide es, die gleichen Informationen an verschiedenen Orten zu duplizieren. Füge die Informationen in eine neue Seite ein und verknüpfe diese Seite von anderen Seiten aus, die diese Informationen benötigen.

Verwende keine Transklusion von Seiten (_), da dies die Übersetzung des Wikis erschwert. Verwende nur die unten unter [\#Vorlagen](#Templates/de.md) beschriebenen Vorlagen.

### Formgestaltung

Vorlagen werden zum Gestalten der Hilfeseiten verwendet. Sie geben der Dokumentation ein einheitliches Aussehen und Gefühl. Es gibt eine Vorlage für Menübefehle, wie **Datei → Speichern**, eine Vorlage zum Gestalten von zu drückenden Tasten, wie **Shift**, eine weitere Vorlage zum Anzeigen eines booleschen Wertes `True` usw. Bitte mache dich mit dem Abschnitt [\#Templates](#Templates.md) vertraut, vor dem Schreiben von Hilfeseiten.

### Temporäre Merker 

Wenn man an einer großen Seite arbeitet, empfiehlt es sich, die Seite entweder als In-Arbeit oder als Unfertig zu kennzeichnen. Dadurch wird sichergestellt, dass die Wiki Administratoren die Seite nicht als Fertig zur Übersetzung markieren, während sie noch häufig geändert wird.

Um eine Seite zu kennzeichnen, füge entweder {{Seite in Bearbeitung}} oder  als erste Zeile ein. Mit  lädst du andere ein, mit dir zusammen die Seite fertigzustellen, während {{Seite in Bearbeitung}} anzeigt, dass du die Arbeit selbst erledigen wirst und andere dir etwas Zeit geben sollen.

Wenn die Arbeit getan ist, vergesse bitte nicht, die Markierungen zu entfernen!

## Beispiele

Um dich schnell mit der Struktur und dem Stil des FreeCAD Wikis vertraut zu machen, schaue dir die Modell Seite an: [GuiBefehl Modell](GuiCommand_model/de.md).


<div class="mw-collapsible mw-collapsed toccolours">

## Struktur


<div class="mw-collapsible-content">

Der [Anlaufstelle für Anwender](User_hub/de.md) bietet ein [Inhaltsverzeichnis](Online_Help_Toc/de.md). Dies wird als Hauptreferenz für die automatische Erstellung der Hilfe ohne Internetverbindung, die du von FreeCAD aus erreichen kannst, sowie der PDF Dokumentation ohne Internetverbindung verwendet.

Die _ dient dem sequentiellen Verweis von Seiten, entsprechend der Struktur des [Inhaltsverzeichnisses](Online_Help_Toc/de.md). Siehe [\#Vorlagen](#Vorlagen.md) für eine Liste aller Vorlagen.

### Seitennamen

Die Seitennamen sollten kurz sein, und sie sollten \"Satzfall\" statt \"Titelfall\" verwenden. Dies ist der [von Wikipedia verwendete Stil](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Capital_letters#Headings,_headers,_and_captions) für deine Artikel.

Schlechter Seitenname:
:   Konstruktion von LuftfahrtUnternehmensflugzeugen





Guter Seitenname:
:   Konstruktion von LuftfahrtUnternehmensflugzeugen

Die Arbeitsbereichsseite der obersten Ebene muss das Format XYZ Arbeitsbereich haben, wobei XYZ der Name des Arbeitsbereichs ist, zum Beispiel _. Beachte, dass du den Befehlsnamen so verwenden solltest, wie er im Quellcode vorkommt.

Eine frühere Konvention sah die Verwendung des Titelfalles vor; jedes Wort sollte mit einem Großbuchstaben beginnen, es sei denn, es handelt sich um Artikel, Präpositionen, Konjunktionen oder andere grammatikalische Partikel, d.h. \"von, auf, in, a, an, und\" usw. Es gibt viele Seiten, die diesen Stil verwenden, aber davon wird bei neuen Seiten abgeraten. Dies wird im Forumsbeitrag diskutiert [(Verweise in Kleinbuchstaben) Verwende einen kleingeschriebenen Titel für eine Wiki Seite](https://forum.freecadweb.org/viewtopic.php?p=266029#p266029).

### Oberbegriffe

Wie die Seitennamen sollten auch die Absatzüberschriften kurz sein und Groß- und Kleinschreibung verwenden. Du solltest keine H1 Überschriften (= Überschrift =) in feinem Wiki Markup verwenden, da der Seitentitel automatisch als Hauptüberschrift H1 hinzugefügt wird.

### Verweise

Du solltest nach Möglichkeit den ursprünglichen Verweisnamen für die Verweise verwenden. Dies verdeutlicht die referenzierte Seite in der gedruckten oder Dokumentation ohne Internetzugang. Du musst die Verwendung von nicht aussagekräftigen Wörtern für den Verweis vermeiden.

Schlechter Verweis
:   Weitere Informationen zum entwerfen von 2D Objekten klicke [hier](Draft_Workbench/de.md).





Guter Verweis
:   Für weitere Informationen zum entwerfen von 2D Objekten beziehe dich auf den [Entwurf Arbeitsbereich](Draft_Workbench/de.md).

Das bevorzugte Format für einen Verweis ist:

[Seitenname](Name_of_page/de.md)

Übersetzt:

[nom de la page](Name_of_page/fr.md)

Beachte, dass für den Teil vor dem | Zeichen, der eigentliche Verweis, die Groß-/Kleinschreibung relevant ist. Wenn dein Seitenname Name_der_Seite lautet, wird der Verweis fehlschlagen, wenn du Name_der_Seite (Großbuchstabe P) eingibst. Vor dem Zeichen | sollten alle Leerzeichen durch Unterstriche (_) ersetzt werden. Dies dient der Unterstützung von Übersetzern, die eine Übersetzungssoftware verwenden. Ohne die Unterstriche würde der Verweis von der Software übersetzt werden, was unerwünscht ist.

Um zu einem bestimmten Abschnitt zu verweisen füge ein # Zeichen und seinen Oberbegriff dem Seitennamen hinzu. Beispiel:

[WikiSeiten](WikiPages/de#Verweise.md)

Übersetzt:

[WikiPages](WikiPages/fr#Liens.md)

Innerhalb der gleichen Seite kannst du den Seitennamen weglassen. Beispiel:

[Verweise](#Verweise.md)

Um einen Verweis zum Anfang der Seite zu erstellen, kannst du verwenden:

</translate>{{Top}}<translate>

Diese Vorlage sollte automatisch den richtigen Text abhängig von der Sprache der Seite anzeigen. Ein Verweis oben auf die Seite ist besonders nützlich für lange Seiten, da er dem Benutzer erlaubt, schnell zum Inhaltsverzeichnis zurückzuspringen. Du kannst ihn an das Ende eines jeden Absatzes setzen. Achte darauf, dass sich vor und nach der Vorlage eine Leerzeile befindet.

Image link
:   <img alt="Optionaler Text, der beim Schweben über dem Bild angezeigt wird\|link=Draft\_Wire" src=images/Draft_Wire.svg  style="width:24px;">

Um ein Bild als Verweis zu benutzen:

![](images/)

Image link + text link
:   <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Linienzug](Draft_Wire/de.md)

Wenn du den optionalen Text weglässt, wird der Verweis selbst beim Schweben über dem Bild angezeigt, was vorzuziehen ist, und du solltest zusätzlich einen Textverweis nach dem Bildverweis hinzufügen:

![](images/)_[Linienzug](Draft_Wire/de.md)

### Arbeitsbereichsseiten

Jede Seite eines Arbeitsbereichs sollte mit

-   dem Namen des Arbeitsbereichs,
-   ein Bild des Aussehens der Arbeitsbereichs (Menü und Werkzeugleiste in deiner Standardposition), und
-   eine Beschreibung dessen, wofür der Arbeitsbereich verwendet wird

Siehe [\#Screen capture](#Screen_capture.md) für Konventionen zum Einbeziehen von Bildern.

### Befehlsseiten

Die Befehlsseiten, die die Arbeitsbereichswerkzeuge beschrieben werden, sollten nicht zu lang sein, sie sollten nur erklären, was ein Befehl tun kann und was nicht, und wie man ihn benutzt. Du solltest Bilder und Beispiele auf ein Minimum beschränken; Tutorien können die Anwendung des Werkzeugs erweitern und Schritt für Schritt Details liefern.

Bitte beziehe dich auf die [GuiBefehlsmodell](GuiCommand_model/de.md) seite für weitere Details.

### Tutorien

Ein gut geschriebenes Tutorium sollte dem Benutzer vermitteln, wie er bestimmte praktische Ergebnisse schnell erreichen kann. Es sollte nicht extrem lang sein, aber es sollte eine ausreichende Anzahl von Schritt-für-Schritt Anleitungen und Bildern enthalten, die den Benutzer bei der Verwendung der verschiedenen Werkzeuge anleiten.

Für Beispiele besuche die [Tutorien](Tutorials/de.md) Seite.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Vorlagen


<div class="mw-collapsible-content">

Das Gestalten der FreeCAD Wiki Seiten wird durch die Verwendung von Vorlagen (_) erreicht. Sie sorgen für ein einheitliches Erscheinungsbild aller Seiten und ermöglichen es auch, das Wiki neu zu gestalten. Die komplette Liste der definierten Vorlagen kannst du unter _ einsehen. Bitte verwende aber nur die in den Tabellen unten aufgeführten Vorlagen. Nur in ganz speziellen Fällen solltest du HTML Kennzeichen direkt verwenden.

Klicke auf den Vorlagenverweis, um die Gebrauchsanweisungen für eine Vorlage und ihre Einführung zu sehen. Vorlagen sind eine leistungsstarke Funktion der MediaWiki Software; Du solltest ein erfahrener Wiki Benutzer sein, wenn du Ergänzungen und Änderungen an bestehenden Vorlagen vorschlagen möchtest. Wenn Vorlagen falsch implementiert sind, erschweren sie die Übersetzung von Seiten in andere Sprachen, so dass ihre Verwendung auf die Textformatierung beschränkt werden sollte; Seitentransklusion sollte vermieden werden. Siehe [MediaWiki Hilfe:Vorlagen](https://www.mediawiki.org/wiki/Help:Templates), um mehr zu erfahren.

### Einfache Vorlagen 

Diese Vorlagen akzeptieren einen einfachen Textparameter und formatieren es mit einem bestimmten Stil.

+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Vorlage                                                                                                       | Erscheinungsbild                     | Beschreibung                                                                                                                                                                                                                                                                                                   |
+===============================================================================================================+======================================+================================================================================================================================================================================================================================================================================================================+
| _                                                                                |                       | Benutze sie, um einen Verweis auf den Anfang der Seite hinzuzufügen.                                                                                                                                                                                                                                           |
|                                                                                                               | {{Top}}                              |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                      |                       | Verwende es, um ein Stück Text hervorzuheben.                                                                                                                                                                                                                                                                  |
|                                                                                                               | **Hervorhebung**            |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                                |                       | Verwende es, um eine Tastaturtaste anzugeben, die gedrückt werden muss.                                                                                                                                                                                                                                        |
|                                                                                                               | **Alt**                          |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                            |                       | Verwende es, um eine ascii Taste in einem Bild (.svg) anzugeben, die gedrückt werden muss. Du musst das gewünschte Zeichen oder die Nummer des ascii Codes des Zeichens angeben.                                                                                                                               |
|                                                                                                               | {{ASCII|A}}                          |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                          |                       | Verwende es, um eine Schaltfläche in der grafischen Benutzeroberfläche anzuzeigen, die gedrückt werden muss.                                                                                                                                                                                                   |
|                                                                                                               | **Abbrechen**                 |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                |                       | Verwende es, um einen Auswahlknopf in der grafischen Benutzeroberfläche anzugeben, der {{RadioButton|TRUE|Gewählt}} oder {{RadioButton|FALSE|Nicht}} werden muß.                                                                                                                   |
|                                                                                                               | {{RadioButton|Option}}               |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                      |                       | Verwende es, um ein Kontrollkästchen in der grafischen Benutzeroberfläche anzuzeigen, das {{CheckBox|TRUE|Angehakt}} oder {{CheckBox|FALSE|Nicht}} werden muß.                                                                                                                     |
|                                                                                                               | {{CheckBox|Option}}                  |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                        |                       | Verwende es, um eine Spinbox in der grafischen Benutzeroberfläche anzuzeigen, die geändert werden muss.                                                                                                                                                                                                        |
|                                                                                                               | {{SpinBox|1.50}}                     |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                      |                       | Verwende es, um eine ComboBox in der grafischen Benutzeroberfläche anzuzeigen, die geändert werden muss.                                                                                                                                                                                                       |
|                                                                                                               | {{ComboBox|Menu 1}}                  |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _, _                                        |                       | Verwende es, um z.B. einen falschen booleschen Wert als Eigenschaft im _ {{Value|falsch}}                           |
|                                                                                                               | `False`                            |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               | , {{false}}            |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _, _                                            |                       | Verwende es, um z.B. einen Wahren booleschen Wert als Eigenschaft im _ {{Value|wahr}}                               |
|                                                                                                               | `True`                             |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               | , {{true}}             |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                |                       | Verwende es, um die Lage eines Befehls innerhalb eines bestimmten Menüs anzugeben.                                                                                                                                                                                                                             |
|                                                                                                               | **Datei → Speichern**    |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                      |                       | Verwende es, um den Namen einer Datei oder eines Verzeichnisses anzugeben.                                                                                                                                                                                                                                     |
|                                                                                                               | {{FileName|Dateiname}}               |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                |                       | Verwende es, um vom Benutzer eingegebenen Eingabetext anzuzeigen.                                                                                                                                                                                                                                              |
|                                                                                                               | {{SystemInput|Gib diesen Text ein}}  |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                              |                       | Verwende es, um Textausgaben aus dem System anzuzeigen.                                                                                                                                                                                                                                                        |
|                                                                                                               | {{SystemOutput|Ausgabetext}}         |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                          |                       | Verwende es, um Inline Quellcode mit einer Monospace Schriftart einzubinden. Er sollte in eine Zeile passen.                                                                                                                                                                                                   |
|                                                                                                               | `import FreeCAD`            |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                              |                       | Verwende es, um eine Ansichtseigenschaft im [Eigenschaftseditor](property_editor/de.md) anzuzeigen. Ansichtseigenschaften sind wie {{emphasis|Linienfarbe}}, {{emphasis|Linienbreite}}, {{emphasis|Punktfarbe}}, {{emphasis|Punktgröße}}, usw. |
|                                                                                                               | {{PropertyView/de|Farbe}}            |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                              |                       | Verwende es, um eine Dateneigenschaft im [Eigenschaftseditor](property_editor/de.md) anzugeben. Dateneigenschaften sind für verschiedene Objekttypen unterschiedlich.                                                                                                                                  |
|                                                                                                               | {{PropertyData/de|Position}}         |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _ / _ |                       | Verwende es, um den Titel einer Eigenschaftsgruppe im [Eigenschaftseditor](property_editor/de.md) anzugeben. Der Titel wird nicht in das automatische Inhaltsverzeichnis aufgenommen.                                                                                                                  |
|                                                                                                               | {{Properties_Title|Basis}}           |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                      |                       | Verwende es, um anzuzeigen, dass eine bestimmte Funktion ab einer bestimmten FreeCAD Version veraltet ist.                                                                                                                                                                                                     |
|                                                                                                               | {{Obsolete/de|0.19}}                 |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                        |                       | Verwende es, um anzuzeigen, dass eine bestimmte Funktion erst ab einer bestimmten FreeCAD Version verfügbar ist.                                                                                                                                                                                               |
|                                                                                                               | {{Version/de|0.18}}                  |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                              |                       | Verwende es, um anzuzeigen, dass eine bestimmte Funktion nachfolgend mit einer bestimmten FreeCAD Version anfängt.                                                                                                                                                                                             |
|                                                                                                               | {{VersionMinus/de|0.16}}             |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                |                       | Verwende es, um anzuzeigen, dass eine bestimmte Funktion oben ist, die mit einer bestimmten FreeCAD Version anfängt.                                                                                                                                                                                           |
|                                                                                                               | {{VersionPlus/de|0.17}}              |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                |                       | Verwende diese Vorlage, um den Hintergrund, den Text oder Hintergrund und Text einzufärben. (_ Seite für weitere Beispiele)                                                                                                                                   |
|                                                                                                               | {{ColoredText|Farbiger Text}}        |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                      |                       | Verwende diese Vorlage, um den Hintergrund, den Text oder Hintergrund und Text über die gesamte Länge der Seite einzufärben. (_ Seite für weitere Beispiele)                                                                                         |
|                                                                                                               | {{ColoredParagraph|Farbiger Absatz}} |                                                                                                                                                                                                                                                                                                                |
|                                                                                                               |                                   |                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Komplexere Vorlagen 

Diese Vorlagen erfordern mehr Eingabeparameter oder erzeugen einen Textblock mit einem bestimmten Format.

+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Vorlage                                                                                          | Erscheinungsbild                                                                                                                        | Beschreibung                                                                                                                                                                                                                                                                                                                                    |
+==================================================================================================+=========================================================================================================================================+=================================================================================================================================================================================================================================================================================================================================================+
| _                                                   | Diese Tabelle                                                                                                                           | Benutze es, um Tabellen wie diese zu formatieren. Es können zusätzliche Tabelleneigenschaften hinzugefügt werden.                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                           |                                                                                                                               | Verwenden Sie es, um eine Erklärung unter einem Bild hinzuzufügen. Sie kann linksbündig oder mittig ausgerichtet sein.                                                                                                                                                                                                                          |
|                                                                                                  | <div style="width:400px;">                                                                                                              |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  | *Beschriftung für ein Bild*                                                                                                   |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  | </div>                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                               |                                                                                                                                         | Verwende es, um Spalten zu löschen. Folge der Definition der Vorlage, um eine detaillierte Erklärung zu erhalten. Sie wird oft verwendet, um zu verhindern, dass Text neben nicht verwandten Bildern fließt.                                                                                                                                    |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                                 |                                                                                                                          | Verwende ihn, um mehrzeilige Code Beispiele mit einer Monospace Schriftart einzubinden. Die Standardsprache ist Python, es können aber auch andere Sprachen angegeben werden.                                                                                                                                                                   |
|                                                                                                  | {{Code|Code=import FreeCAD}}                                                                                                            |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      | [Python](Python/de.md) Code sollte sich an die allgemeinen Empfehlungen halten, die von [PEP8: Stil Leitfaden für Python Code](https://www.python.org/dev/peps/pep-0008/). Insbesondere sollten Klammern unmittelbar auf den Funktionsnamen folgen, und auf ein Komma sollte ein Leerzeichen folgen. Dies macht den Code besser lesbar. |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                          |                                                                                                                          | Verwende es, um eine Überschrift zu erstellen, die nicht automatisch in das für die Offline Dokumentation verwendete Inhaltsverzeichnis aufgenommen wird.                                                                                                                                                                                       |
|                                                                                                  | {{Fake heading|Heading|2}}                                                                                                              |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                     | Siehe [Gui Befehl](Gui_Command/de.md) und [GuiCommand Modell](GuiCommand_model/de.md)                                   | Benutze es, um einen Kasten mit nützlichen Informationen zu Dokument Arbeitsbereichsbefehlen (werkzeuge) zu erstellen.                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                 | See for example [Basic modeling tutorial](Basic_modeling_tutorial.md)                                                           | Verwende es, um einen Kasten mit nützlichen Informationen zur Dokumentation von [Tutorien](Tutorials/de.md) zu erstellen.                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                               | Siehe Beispiel [Makro FlattenWire](Macro_FlattenWire/de.md)                                                                     | Verwende es, um eine Box mit nützlichen Informationen zur Dokumentation zu erstellen [Makros](macros/de.md).                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                             |                                                                                                                          | Verwende es, um eine Leiste mit den Wörtern \"next\", \"previous\" und \"index\" und Links zu den entsprechenden Verweisen zu erstellen, was nützlich ist, um Seiten in eine bestimmte Reihenfolge zu bringen.                                                                                                                                  |
|                                                                                                  |                                                                                            |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                 |                                                                                                                          | Verwenden es, um einen hervorgehobenen Kasten mit einer sehr wichtigen Nachricht zu erstellen. Verwende es sparsam, nur um auf größere Probleme in der Funktionalität der Software, Abkündigungen von Werkzeugen und Ähnliches hinzuweisen.                                                                                                     |
|                                                                                                  | **Important Message**                                                                                              |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                         |                                                                                                                          | Verwende dies für Seiten, die noch in Arbeit sind oder gerade überarbeitet werden. Vergiss nicht, dies zu entfernen, wenn die Seite fertig ist.                                                                                                                                                                                                 |
|                                                                                                  | {{Page in progress|Page in progress}}                                                                                                   |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                             |                                                                                                                          | Verwende es, um ein hervorgehobenes Feld zu erzeugen, das eine unfertige Dokumentationsseite anzeigt.                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                 |                                                                                                                                         | Verwende es anstelle der normalen Umleitung, wenn du auf eine spezielle Seite (z. B. Media: oder Category:) umleitest, in deren Fällen die normale Umleitung deaktiviert ist.                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _                                                               |                                                                                                                          | Verwende es, um einen Textkasten mit einem wörtlichen Zitat und einer Referenz zu erstellen.                                                                                                                                                                                                                                                    |
|                                                                                                  | {{Quote|Text=Rufe "Verwüstung" und lass die Hunde des Krieges los.|sign=William Shakespeare|source=''Julius Cäsar'', Akt III, Szene I}} |                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| _, _ |                                                                                                                                         | Verwende diese, um Navigationsboxen für die Benutzerdokumentation, die Dokumentation für erfahrene Nutzer und die Entwicklerdokumentation zu erstellen. Dies ermöglicht ein schnelles Springen zwischen verschiedenen Abschnitten der Dokumentation. Außerdem platzieren sie die entsprechende Seite in der richtigen Kategorie.                |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Grafiken


<div class="mw-collapsible-content">

Bilder und Bildschirmfotos sind notwendig, um eine vollständige Dokumentation von FreeCAD zu erstellen. Sie sind besonders nützlich, um Beispiele und Tutorien zu illustrieren. Bilder sollten in ihrer Originalgröße angezeigt werden, damit sie genügend Details zeigen und lesbar sind, wenn sie Text enthalten. [Bitmap](Bitmap/de.md) Bilder sollten nicht in der Größe verändert werden.

Vermeide animierte Bilder (GIF) in den allgemeinen Hilfeseiten. Animationen und Videos sollten für Tutorien reserviert werden, die nicht als PDF Dokumentation ohne Internetverbindung verwendet werden sollen.

Bilder müssen über die _ Seite hochgeladen werden.

### Namen

Gib deinem Bild einen aussagekräftigen Namen. Wenn du ein Bild hast, das die Merkmale eines bestimmten Befehls präsentiert, solltest du den gleichen Namen wie der Befehl mit `_example` am Ende verwenden.

-   Für den Befehl _ heißen.
-   Für den Befehl _ heißen.

### Bildschirmerfassung

Empfohlene Größen für Bildschirmfotos sind:

-   Natürliches 400x200 (oder Breite=400 und Höhe\<=200), für [Gui Befehl](Gui_Command//de.md) Seiten, damit das Bild in den linken Teil der Seite passt, und für andere Standard-Schnappschüsse.
-   Natürliches 600x400 (oder Breite=600 und Höhe\<=400), für [Gui Befehl](Gui_Command/de.md) Seiten, wenn du wirklich ein größeres Bild benötigst und das Bild trotzdem in den linken Teil der Seite passen soll, und für andere Standard Schnappschüsse.
-   Natürliches 1024x768 (oder Breite=1024 und Höhe\<=768), nur für Vollbildschirm Bilder.
-   Kleinere Größen sind bei der Darstellung von Details möglich, verwende jedoch die natürliche Auflösung, keine Größenänderung oder Miniaturbilder, es sei denn, du hast einen sehr guten Grund dafür.
-   Größere Auflösungen sollten vermieden werden, da sie für andere Arten der Darstellung oder in der gedruckten PDF Dokumentation nicht sehr übertragbar sind.

Du solltest nicht von einer bestimmten Konfiguration deines Desktops oder Betriebssystems abhängig sein, wenn du Bildschirmfotos erstellst ich nd du solltest, wo immer möglich, visuelle Voreinstellungen der FreeCAD Oberfläche verwenden.

Um einen Bildschirmphoto zu erstellen, kannst du die von deinem Betriebssystem bereitgestellten Optionen oder eines dieser Makros verwenden: <img alt="" src=images/Snip.png  style="width:24px;"> _.

### Text

Um die Übersetzung der Dokumentation zu erleichtern, machen Sie separate Bilder von der Benutzeroberfläche und dem 3D-Modell-Viewport. Das Bild des 3D-Modells kann bei jeder Übersetzung wiederverwendet werden, während ein Übersetzer bei Bedarf ein Bild der lokalisierten Oberfläche machen kann.

### Symbole und Grafiken 

Verweise auf die [Illustrationen](Artwork/de.md) Seite für alle Illustrationen und Symbole, die für FreeCAD erstellt wurden und die sofort in den Dokumentationsseiten wiederverwendet werden können. Wenn du mit Symbolen beitragen möchtest, lies bitte die [Richtlinien für Illustrationen](Artwork_Guidelines/de.md).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Übersetzungen


<div class="mw-collapsible-content">

Gemäß der allgemeinen Übereinkunft ist die englische Seite die Referenzseite im Wiki und muß zuerst erstellt werden. Wenn der Inhalt einer Seite geändert wird oder etwas hinzugefügt werden soll, muß dies zuerst auf der englischen Seite geschehen und erst danach die Änderung auf die übersetzte Seite übertragen werden.

Das FreeCAD Wiki unterstützt eine Übersetzungserweiterung, die es ermöglicht, Übersetzungen zwischen Seiten einfacher zu verwalten; Details hierzu unter [Lokalisierung Übersetzung des Wiki](Localisation/de#Übersetze_das_FreeCAD_Wiki.md).

Weitere hilfreiche Quellen sind:

-   [ISO language codes](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes): ein ISO Sprachcode mit zwei Buchstaben um die zu übersetzende Sprache zu benennen/identifizieren.
-   [Google Translate](http://translate.google.com/): zur Hilfe beim Übersetzen.
-   [Deepl translator](https://www.deepl.com/translator): zur Hilfe beim Übersetzen.

## Einige Hinweise für Übersetzer 

### GUIBefehl Übersetzen 

    {{GuiCommand
    |Name=FEM EquationFluxsolver
    |MenuLocation=Solve → Equation fluxsolver
    |Workbenches=[FEM](Fem_Workbench.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM tutorial](FEM_tutorial.md)
    }}

Übersetzt:

    {{GuiCommand/fr
    |Name=FEM EquationFluxsolver
    |Name/fr=FEM EquationFluxsolver
    |MenuLocation=Solveur → Equation fluxsolver
    |Workbenches=[Atelier FEM](Fem_Workbench/fr.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM tutoriel](FEM_tutorial/fr.md)
    }}

### Navi Übersetzen 

    {{FEM_Tools_navi}}

Übersetzt:

    {{FEM_Tools_navi/fr}}

### Verweis Übersetzen 

    [Part Module](Part_Module.md)

Übersetzt:

    [Atelier Pièces](Part_Module/fr.md)

### Docnav Übersetzen 

    

Übersetzt:

    

Beispiel mit Symbolen:

    

Übersetzt:

    


</div>


</div>

## Erstellen, umbenennen und löschen von Seiten 

### Seiten erstellen 

Vor dem Erstellen einer neuen Seiten solltest du zuerst prüfen, ob bereits eine ähnliche Seite existiert. Sollte das der Fall sein, ist es meist besser, die vorhandene Seite zu ändern. Im Zweifel öffne bitte zuerst ein neues Thema im [Wiki-Forum](https://forum.freecadweb.org/viewforum.php?f=21).

Um eine neue Seite zu erstellen, tue eins der folgenden Dinge:

-   Besuche die URL mit dem gewünschten Seitennamen, z.B.: https://wiki.freecadweb.org/MeineNeueSeite/de, und klicke auf \'Erstellen\'.
-   Führe eine Wiki-Suche nach dem Seitennamen durch und klicke auf den roten Text in \'Erstelle die Seite \"MeineneueSeite\" in diesem Wiki.\'.

### Seiten umbenennen 

Da FreeCAD ein Projekt ist, das ständig weiterentwickelt wird, ist es manchmal notwendig, den Inhalt des Wikis zu überarbeiten. Wenn die Namen von Befehlen im Quellcode geändert werden, müssen die Wiki Seiten, die sie dokumentieren, ebenfalls umbenannt werden. Dies kann nur von den Wiki Administratoren durchgeführt werden. Um diese zu informieren, eröffne ein Thema im [Wiki Forum](https://forum.freecadweb.org/viewforum.php?f=21) und liste den notwendigen Umbenennungsvorgang in diesem Formular auf:

    old name         new name
    Old_page_name_1  New_page_name_1
    Old_page_name_2  New_page_name_2
    ...

### Löschen von Dateien und Seiten 

Falls du eine Datei löschen musst, gehe auf seine Seite (https://www.freecadweb.org/wiki/File:***.***) und bearbeite sie. Unabhängig davon, ob die Seite leer ist oder nicht, füge diesen Befehl als erstes Element der Seite hinzu: {{Delete}} und beschreibe unmittelbar darunter, warum die Seite gelöscht werden soll. Zusätzlich eröffne ein Thema im [Wiki Forum](https://forum.freecadweb.org/viewforum.php?f=21).

Für Seiten ist das Verfahren dasselbe.

## Diskussion

Das [Entwicklung/Wiki Unterforum](http://forum.freecadweb.org/viewforum.php?f=21) im [FreeCAD Forum](https://forum.freecadweb.org) bietet einen speziellen Raum für die Diskussion von Verbesserungen der Wiki Themen und des Erscheinungsbildes. Dort kann man Fragen stellen und Vorschläge anbringen.

## Terminologie - Benennungspolitik 

### Englisch

Siehe [Glossar](Glossary/de.md)

### Andere Sprachen 

-   [Italienisch](Italian_Translation.md)
-   [Französisch](French_Translation.md)
-   [Deutsch](German_Translation.md)

_ _ _ _

---
[documentation index](../README.md) > [Documentation](Category_Documentation.md) > WikiPages/de
