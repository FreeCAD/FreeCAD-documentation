# Localisation/de
## Überblick

**Lokalisierung** ist im Allgemeinen der Prozess der Bereitstellung einer Software mit einer mehrsprachigen Benutzeroberfläche. In FreeCAD kannst du die Sprache der Benutzeroberfläche unter **Bearbeiten → Einstellungen → Allgemein** einstellen. FreeCAD verwendet [Qt](wikipedia:Qt_(Bibliothek).md), um die Unterstützung mehrerer Sprachen zu ermöglichen. Auf Unix/Linux-Systemen verwendet FreeCAD standardmäßig die aktuellen Gebietsschemaeinstellungen deines Systems.



## Helfen, FreeCAD zu übersetzen 

Eines der sehr wichtigen Dinge, die Benutzer zu FreeCAD beitragen können (wenn sie z.B. keine Programmierfähigkeiten haben), ist es, die verschiedenen Aspekte (Quellcode, Wiki, Website, Dokumentation usw\....) in eine andere Sprache zu übersetzen. Hier sind die Möglichkeiten, dies zu tun.



## Übersetze den FreeCAD Quellcode 

FreeCAD verwendet ein gemeinschaftlich genutztes Online Übersetzungssystem von Drittanbietern namens [Crowdin](https://crowdin.net).

<img alt="" src=images/Logo-crowdin.png  style="width:320px;">

Es ist geschützte Software, aber kostenlos für [FOSS](https://en.wikipedia.org/wiki/Free_and_open-source_software)-Projekte. Nachfolgend sind Anweisungen wie es verwendet wird:

-   Gehe zur [FreeCAD Übersetzungsprojektseite auf Crowdin](http://crowdin.net/project/freecad)
-   Melde Dich an, indem Du ein neues Profil erstellst oder ein Drittanbieterkonto verwendest (GitHub, GitLab, GMail usw\....)
-   Klicke auf die Sprache, die Du übersetzen möchtest.
-   Beginne mit dem Übersetzen, indem Sie auf die Schaltfläche **Übersetzen** neben einer der Dateien klickst. Beispielsweise enthält **FreeCAD.ts** die Textzeichenketten für die FreeCAD Haupt GUI.
-   Du kannst für bestehende Übersetzungen stimmen oder eigene erstellen.

{{Message|Wenn Du aktiv an der Übersetzung von FreeCAD teilnimmst und informiert werden möchtest, bevor die nächste Version herauskommt, melde Dich bitte bei einem der Crowdin FreeCAD Übersetzungsteams an, damit Du Zeit hast, Deine Übersetzung zu überprüfen. }}


**Hinweis:**

Details zur Verwendung von Crowdin findest du auf der Seite [Crowdin Verwaltung](Crowdin_Administration/de.md).



## Übersetzung externer Arbeitsbereiche 

-   Besuche [Übersetzen eines externen Arbeitsbereichs](Translating_an_external_workbench/de.md)



## FreeCAD-Voreinstellungen für Übersetzer 

Seit der FreeCAD 0.20 können folgende Variablen manuell in den Abschnitt BaseApp/Preferences/General der Datei user.cfg hinzugefügt werden, um die Erarbeitung neuer Übersetzungen zu unterstützen:

**AdditionalLanguageDomainEntries** - zum Hinzufügen völlig neuer Sprachen zu FreeCAD, die bisher nicht durch den Quellkode unterstützt werden. Diese Benutzereinstellung kann man verwenden, um die Liste der verfügbaren Sprachen zu erweitern. Das Format für die Sprachen ist \"Language Name\"=\"code\"; zum Beispiel:

    <FCText Name="AdditionalLanguageDomainEntries">"Esperanto"="eo";"French"="fr";</FCText>

**AdditionalTranslationsDirectory** - Hinzufügen eines zusätzlichen Verzeichnisses, in dem FreeCAD nach \*.qm-Dateien suchen kann. Dieser Speicherort bekommt den Vorzug vor \$userAppDataDir/translations und \$resourceDir/translations. Zum Beispiel:

    <FCText Name="AdditionalTranslationsDirectory">C:/Users/FreeCADUser/TestTranslations</FCText>



## Übersetze das FreeCAD Wiki 

Dieses Wiki beherbergt viele Inhalte, von denen die meisten das Handbuch bilden. Du kannst die Dokumentation von der [Hauptseite](Main_Page/de.md) aus durchsuchen, oder einen Blick in das Benutzerhandbuch [Online Hilfe Inhaltsverzeichnis](Online_Help_Toc/de.md) werfen.

Um das Wiki zu übersetzen, musst Du über Wiki Bearbeitungsrechte verfügen; siehe [Wie kann ich Bearbeitungsrechte für das Wiki erhalten?](Frequently_asked_questions/de#Wie_kann_ich_Bearbeitungsrechte_für_das_Wiki_erhalten?.md).

Du solltest auch genügend Kenntnisse über den Wikistil haben und die allgemeinen Gestaltungsrichtlinien befolgen, die unter [WikiSeiten](WikiPages/de.md) beschrieben sind.



### Mediawiki Übersetzungserweiterung 

Als das Wiki von SourceForge wegging, installierte [Yorik](User_Yorik.md) [MediaWiki\'s Translation Extension](http://www.mediawiki.org/wiki/Help:Extension:Translate), was die Übersetzung von Seiten erleichtert. Die Übersetzungserweiterung hat den Vorteil, dass der Seitentitel nun übersetzt werden kann, dass sie die Übersetzungen verfolgt, dass dich benachrichtigt, ob die Originalseite aktualisiert wurde, und dass die Übersetzungen synchron mit der englischen Originalseite verwaltet.

Das Werkzeug ist in [Help:Extension:Translate](http://www.mediawiki.org/wiki/Help:Extension:Translate) dokumentiert und ist ein Teil eines [Mediawiki Spracherweiterungsbündels](http://www.mediawiki.org/wiki/MediaWiki_Language_Extension_Bundle).

Um schnell mit der Vorbereitung einer Seite für die Übersetzung zu beginnen, bitte das Beispiel [Seitenübersetzungsbeispiel](http://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example) lesen. Ein Tag-Paar muss die gesamte Seite umklammern, um das Übersetzungssystem zu aktivieren.

    &lt;translate&gt; ... &lt;/translate&gt;

Die Seite muss außerdem für die Übersetzung markiert werden.

Um ein Beispiel für die Funktionsweise des Übersetzungswerkzeugs zu sehen, besuche die [Hauptseite](Main_Page/de.md). Du wirst oben eine automatisch generierte Sprachleiste sehen. Klicke auf [Deutsch](Main_Page/de.md) (deutsch), es bringt dich zu [Main Page/de](Main_Page/de.md). Direkt unter dem Titel \"Hauptseite\" (engl. \"Main Page\") kannst du lesen , wobei XX der aktuelle Prozentsatz der Übersetzung ist. Klicke oben auf der Seite auf \"Übersetzen\", um das Übersetzungsprogramm zu starten, mit dem Du die bestehende Übersetzung aktualisieren, korrigieren und überprüfen kannst.

Wechselt man zur [Hauptseite](Main_Page/de.md), wird man feststellen, dass die Seite nicht mehr direkt bearbeitet werden kann, indem man auf die Verknüpfungen \[Bearbeiten\] klickt, und die obere Verknüpfung \"Bearbeiten\" wurde durch die Verknüpfung \"Übersetzen\" ersetzt, die das Übersetzungsprogramm öffnet.

Wenn ein neuer Inhalt hinzugefügt wird, sollte die englische Seite zuerst erstellt und dann in eine andere Sprache übersetzt werden. Wenn ein Inhalt geändert oder ergänzt werden soll, sollte das zuerst in der englischen Seite gemacht werden.

Wenn Du Dir nicht sicher bist, wie Du mit den Übersetzungen vorgehen sollst, zögere nicht, Dich im Unterforum [Entwicklung → Wiki Unterforum](https://forum.freecadweb.org/viewforum.php?f=21) oder im Unterforum [Unterforum spezifische Sprache](https://forum.freecadweb.org/viewforum.php?f=11) im FreeCAD-Forum[FreeCAD Forum](http://forum.freecadweb.org) um Hilfe zu bitten.



### Wichtige Anmerkungen 

Jeder Wiki Benutzer der *Editor* Berechtigungen hat, kann das Übersetzungshilfsprogramm aufrufen, um Übersetzungen zu schreiben, zu speichern und zu überprüfen.

Allerdings können nur Benutzer mit *Administrator* Berechtigungen Seiten für die Übersetzung markieren. Eine Seite, die nicht für die Übersetzung freigegeben ist, kann die Übersetzungserweiterung nicht nutzen und wird nicht korrekt mit den englischen Informationen synchronisiert.

Die linke Seitenleiste ist ebenfalls übersetzbar, aber nur Administratoren können dieses Element der Webseite ändern. Bitte folge den zugehörigen Anweisungen auf [Lokalisierungs Seitenleiste](Localisation_Sidebar/de.md).

Wenn du zum ersten Mal auf das neue Übersetzungssystem wechselst, verliert es alle seine alten \"manuellen\" Übersetzungen. Um eine Übersetzung wiederherzustellen, solltest du eine Offline Kopie des alten Textes vor dem Wechsel speichern. Dann kannst du diesen alten übersetzten Text verwenden, um die Übersetzungseinheiten im neuen System auszufüllen. Du kannst auch eine frühere Version aus der Historie öffnen und so den alten Text erhalten. Dies muss für jede Sprache erfolgen, die eine übersetzte Seite hatte.



### Übersetze die FreeCAD Dokumentation 

Nach allgemeinem Konsens ist die Referenzseite im Wiki die englische Seite, die zuerst erstellt werden sollte. Wenn du Inhalte zu einer Seite ändern oder hinzufügen möchtest, solltest du dies zuerst auf der englischen Seite tun, und erst wenn das Update abgeschlossen ist, die Änderung auf die übersetzte Seite portieren.



### Alte Übersetzungsanweisungen 

++
| Diese Anleitung gilt nur für den historischen Hintergrund. Übersetzungen sollten das neue System mit der oben beschriebenen [#Mediawiki Translation Extension](#Mediawiki_Translation_Extension.md) verwenden.                                                                                                                                                                                                                                                                                                                                                                                                                       |
++
| Der erste Schritt besteht also darin, zu überprüfen, ob die manuelle Übersetzung für deine Sprache bereits gestartet wurde**(siehe linke Seitenleiste, unter \"Handbuch\").                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Wenn nicht, gehe zum [Forum](http://forum.freecadweb.org/) und sage, dass du eine neue Übersetzung beginnen möchtest, wir erstellen das Basis Setup für die Sprache, an der du arbeiten möchtest.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Du musst dann [Wiki Bearbeitungsrechte erhalten](Frequently_asked_questions/de#Wie_kann_ich_Bearbeitungsrechte_für_das_Wiki_erhalten?.3F.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Wenn deine Sprache bereits aufgeführt ist, siehst du, welche Seiten noch eine Übersetzung vermissen lassen (sie werden rot angezeigt). Die Technik ist einfach:**\'go into a red page, and copy/paste the contents of the corresponding English page, and start translating**\'.                                                                                                                                                                                                                                                                                                                                                             |
| Vergiss nicht, alle Tags und Vorlagen von der englischen Originalseite einzubinden. Einige dieser Vorlagen haben eine Entsprechung in deiner Sprache (z.B. gibt es eine französische DocnavnVorlage namens Docnav/fr). Du solltest**a Schrägstrich und deinen Sprachcode\'\'\'\' in fast allen Verweisen verwenden. Schau dir andere bereits übersetzte Seiten an, um zu sehen, wie sie es gemacht haben.                                                                                                                                                                                                                                    |
| Füge einen Schrägstrich und deinen Sprachcode in die Kategorien ein, wie \[\[Category:Developer Documentation/fr\]\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Und wenn du unsicher bist, gehe ins Forum und bitte die Leute, zu überprüfen, was du getan hast und sage dir, ob es richtig ist oder nicht. Vier Vorlagen werden häufig in Handbuchseiten verwendet. Diese 4 Vorlagen haben lokalisierte Versionen (Template:Docnav/fr, Template:fr, etc\....).                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -   [Template:GuiCommand](Template_GuiCommand.md) : ist der Gui Command Informationsblock oben rechts in der Befehlsdokumentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -   [Template:Docnav](Template_Docnav.md) : Es ist die Navigationsleiste am unteren Rand der Seiten, die vorherige und nächste Seiten anzeigt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -   [Template:Userdocnavi](Template_Userdocnavi.md) : gibt direkte Links zu den wichtigsten Basisseiten                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| \'**\' Seitenbenennungskonvention**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Bitte beachte, dass wir aufgrund von Einschränkungen in der Sourceforge Implementierung der MediaWiki Engine verlangen, dass deine Seiten alle den Namen deines ursprünglichen englischen Gegenübers behalten, indem du einen Schrägstrich und deinen Sprachcode anhängst. Beispielsweise sollte die übersetzte Seite für About FreeCAD About Freecad/es für spanisch, About FreeCAD/pl für polnisch, usw. sein. Der Grund ist einfach: Damit die Administratoren des Wikis, die nicht alle Sprachen sprechen, wissen, wofür diese Seiten gedacht sind, wenn Übersetzer weggehen. Dies erleichtert die Wartung und vermeidet Seitenverluste. |
| Wenn du möchtest, dass die Docnav Vorlage verknüpfte Seiten in deiner Sprache anzeigt, kannst du **\'redirect pages** verwenden. Sie sind im Grunde genommen Verknüpfungen zur eigentlichen Seite. Hier ist ein Beispiel mit der französischen Seite für About FreeCAD.                                                                                                                                                                                                                                                                                                                                                                      |
| \* Die Seite About FreeCAD/fr ist die Seite mit dem Inhalt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -   Die Seite À propos de FreeCAD enthält diesen Code:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| #REDIRECT [[Über_FreeCAD/fr]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -   Auf der Seite About FreeCAD/fr sieht der Docnav Code so aus:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| {{docnav/fr|[Bienvenue dans l'aide en ligne de FreeCAD](Online_Hilfe_Startseite/fr.md)|[Funktionnalités](Feature_list/fr.md)}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Die Seite \"Bienvenue dans l\'aide en ligne de FreeCAD\" verweist auf Online_Help_Startseite/fr, und die Seite \"Fonctionnalités\" verweist auf Feature_list/fr.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
++



## Übersetze die FreeCAD Webseite 

Die Übersetzung der FreeCAD Webseite erfolgt nun über [Crowdin](https://crowdin.com/translate/freecad/561/en-en). Die Datei hat den Namen **homepage.po**.



## Entwicklung - Wie man Lokalisierung hinzufügt 

Dieser Abschnitt ist für Entwickler, die ihrem Code eine Lokalisierung hinzufügen möchten.



### Vorbereitung deiner FreeCAD/Master Module für die Übersetzung 

Dies sind die Schritte für den FreeCAD Übersetzungsprozess:

-   entnehmen der Textzeichenfolgen aus dem Quellcode in \*.ts Dateien
-   lade .ts Dateien in [FreeCAD Crowdin](http://crowdin.net/project/freecad) hoch
-   Übersetzung der Zeichenfolgen in Crowdin
-   entnehmen geänderter/neuer \*.ts Dateien aus Crowdin
-   Umwandeln der \*.ts Dateien in \*.qm Dateien und aktualisieren jeder \*.qrc Datei der Module
-   aktualisieren des FreeCAD Master

Alle der oberen Schritte werden von den *Übersetzungsskripten* durchgeführt, die periodisch durch einen Administrator ausgeführt werden.

Die Vorbereitung deines Moduls auf die Übersetzung ist ganz einfach. Zuerst musst du sicherstellen, dass du ein Verzeichnis \"translations\" in **myModule/Gui/Resources** hast. Öffne dann ein Terminalfenster (oder ein Windows/OSX Äquivalent) in Deinem Verzeichnis \"Übersetzungen\" und gib den folgenden Befehl ein: 
```pythonlupdate -ts myModule.ts```

Dies erzeugt eine leere Übersetzungsdatei. Sobald dies geschehen ist, muss sichergestellt sein, dass die Übersetzungsskripte in [pull request](https://github.com/FreeCAD/FreeCAD/pull/810) aktualisiert sind.

Alles danach, soweit es einen Entwickler betrifft, wird automatisch durchgeführt. Der Administrator wird die Texte entnehmen, die Übersetzer werden sie übersetzen und der Administrator wird die Übersetzungen wieder entnehmen und FreeCAD/master aktualisieren.



### Vorbereitung deines Drittanbieter Moduls oder Makros für die Übersetzung 

Drittanbietermodule oder Makros von werden in ähnlicher Weise übersetzt, nur daß du einen Teil der Arbeit selbst erledigen musst. Diese [Forumsdiskussion](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) beschreibt die Details.

-   \* Aktualisierung: Siehe [Übersetzen eines externen Arbeitsbereichs](Translating_an_external_workbench/de.md)



## Automatisieren von Crowdin Übersetzungsaktualisierungen 

Derzeit verwenden FreeCAD Betreuer die Crowdin API über [Crowdin Skripte](Crowdin_Scripts/de.md), um Übersetzungen in Crowdin und zurück in den Github Repo zu ziehen und zu verschieben. Die Crowdin API gibt FreeCAD Betreuern die Möglichkeit, Aspekte des Übersetzungsarbeitsablaufs des Projekts zu automatisieren, weitere Informationen findest Du in der [Crowdin API Dokumentation](https://support.crowdin.com/api/api-integration-setup/).



## Verwandte Seiten 

-   [Crowdin Verwaltung](Crowdin_Administration/de.md)
-   [Crowdin Skripte](Crowdin_Scripts/de.md)



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um eine Übersetzungsliste einer Sprache, die die FreeCAD-Schnittstelle unterstützt, zu erhalten, benutzt man die Methode `supportedLocales` des Moduls `FreeCADGui`.


```python
locales = FreeCADGui.supportedLocales()
```

Nach der Ausführung enthält `locales`:


```python
{'English': 'en', 'Afrikaans': 'af', 'Arabic': 'ar', 'Basque': 'eu', 'Catalan': 'ca', 'Chinese Simplified': 'zh-CN', 'Chinese Traditional': 'zh-TW', 'Croatian': 'hr', 'Czech': 'cs', 'Dutch': 'nl', 'Filipino': 'fil', 'Finnish': 'fi', 'French': 'fr', 'Galician': 'gl', 'German': 'de', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Kabyle': 'kab', 'Korean': 'ko', 'Lithuanian': 'lt', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt-PT', 'Portuguese, Brazilian': 'pt-BR', 'Romanian': 'ro', 'Russian': 'ru', 'Slovak': 'sk', 'Slovenian': 'sl', 'Spanish': 'es-ES', 'Swedish': 'sv-SE', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Valencian': 'val-ES', 'Vietnamese': 'vi'}
```

Um die aktuelle Schnittstellensprache herauszufinden, benutzt man die Methode `getLocale` desselben Moduls:


```python
locale = FreeCADGui.getLocale()
```

Ist die aktuelle Sprache Englisch, enthält `locale`:


```python
'English'
```

Um das dazugehörige [Sprachkürzel](https://support.crowdin.com/api/language-codes/) zu erhalten, verwendet man:


```python
locale = FreeCADGui.supportedLocales()[Gui.getLocale()]
```

Wenn die aktuelle Sprache Englisch ist, ist das Ergebnis:


```python
'en'
```

Um die aktuelle Sprache der Benutzerschnittstelle zu ändern, verwendet man die Methode `setLocale` desselben Moduls. Man kann hier die Sprache oder das Sprachkürzel angeben:


```python
FreeCADGui.setLocale('Russian')
FreeCADGui.setLocale('ru')
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Wiki](Category_Wiki.md) > Localisation/de
