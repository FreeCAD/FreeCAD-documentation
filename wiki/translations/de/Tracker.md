# Tracker/de
{{TOCright}}

![](images/Mantis_logo_262x90.png )

Der [FreeCAD FehlerVerfolger](https://www.freecadweb.org/tracker) ist der Ort umː Fehler zu melden, Funktionsanfragen zu übermitteln, Änderungssätze einzureichen oder deine Verzweigung zusammenführen zu können, wenn du etwas unter Verwendung von Git entwickelt hast. Der Verfolger ist in \'Arbeitsbereiche\' unterteilt, also sei bitte präzise und reiche deine Anfrage in dem entsprechenden Unterabschnitt ein. Im Zweifelsfall belasse sie im Abschnitt \"FreeCAD\".

## Empfohlener Arbeitsablauf 

![](images/Bugreport-workflow.png )

Wie im obigen Flussdiagramm dargestellt, durchsuche bitte vor dem Erstellen von Tickets immer zuerst die Foren und den Fehlerverfolger, um herauszufinden, ob dein Problem ein bekanntes Problem ist. Dies erspart Entwicklern und Freiwilligen eine Menge Zeit/Arbeit, die diese Zeit damit verbringen könnte, FreeCAD noch fantastischer zu machen.

## Fehler melden 

Wenn du glaubst, einen Fehler gefunden zu haben, kannst du ihn gerne melden, solange du unsere Schritt-für-Schritt-Richtlinien befolgt hast.

-   Stelle sicher, dass du die aktuellste Version von FreeCAD verwendest. **ANMERKUNGː** Dein Fehler ist möglicherweise in der (instabilen) Entwicklungsversion behoben. Der durchschnittliche Benutzer verwendet die stabile Version von FC.
-   Stelle sicher, dass dein Fehler wirklich ein Fehler ist, d.h. etwas, das funktionieren sollte, es aber nicht tut. **Stelle sicher, dass derselbe Fehler nicht schon einmal gemeldet wurde, indem du zuerst den Fehlerverfolger und das Forum durchsuchst**.
    -   Bedenkeː Wenn du dir nicht sicher ist, zögere bitte nicht, dein Problem/Fehler im [Hilfeforum](http://forum.freecadweb.org/viewforum.php?f=3) zu erklären und zu fragen, was zu tun ist.
    -   **Hinweis**\'ː Bevor ein Beitrag fürs Forum verfasst wird, lies bitte die [Forumsrichtlinien](https://forum.freecadweb.org/viewtopic.php?f=3&t=2264).
-   Beschreibe so klar wie möglich das Problem und wie es reproduziert werden kann. Wenn wir den Fehler nicht verifizieren können, sind wir möglicherweise nicht in der Lage, ihn zu beheben.
    -   Das bedeutet *\'Berichterstattung in einer klaren, gut formatierten, Schritt-für-Schritt Art und Weise*, so dass selbst ein Amateuranwender den Fehler reproduzieren kann.
    -   Empfohlenː **Bildschirmfotos** des Fehlers sind ebenfalls sehr hilfreich einzufügen. Windowsanwender: Bitte füge keine Bildschirmfotos im Word oder PDF Format bei. Verwende das Windows Snipping Werkzeug, um dein Aufnahme als PNG Bild zu speichern.
    -   Empfohlenː Noch besser, ein **Animiertes Gif oder Screencast** würde auch die Wahrscheinlichkeit erhöhen, das Problem zu reproduzieren.
-   **Füge eine Beispiel FreeCAD Datei hinzu** (.FCStd Datei), damit Entwickler/Tester den Fehler schnell reproduzieren können.
    -   Bitte packe deine \*.FCStd-Datei nicht, sie ist bereits gepackt.
    -   Dateianhänge sind in der Größe begrenzt. Wenn deine \*.FCStd Datei zu groß ist, um sie anzuhängen, kannst du einen Online Speicherdienst nutzen (viele sind kostenlos wie Google Drive, Microsoft OneDrive, Dropbox).
-   Füge alle Informationen aus der Schaltfläche \"In die Zwischenablage kopieren\" in den Dialog **Hilfe (Menü) -\> Über FreeCAD**\' ein. Stelle sicher, dass deine Daten deine OCC oder OCE Version enthält.
-   Bitte reiche für jeden Fehler einen separaten Bericht ein.
-   Wenn dein Fehler einen Absturz in FreeCAD verursacht und du dich auf einem System befindest, das dies unterstützt, kannst du versuchen, einen **debug backtrace** auszuführen und diesen Trace an das Ticket anzuhängen. Dies kann Entwicklern viel Zeit ersparen, die Quelle des Absturzes zu lokalisieren. Siehe [Fehlerdiagnose](Debugging/de.md) für weitere Einzelheiten.

## Anfordern von Funktionen 

Wenn du möchtest, dass etwas in FreeCAD erscheint, das noch nicht implementiert ist, es handelt sich nicht um einen Fehler, sondern um eine Funktionsanfrage.

1.  **WICHTIGː** Bevor ein potentielle Funktionsanfrage gestellt wird, **stelle bitte sicher, dass du der erstebist, der dies tut, indem du die Foren und den Fehlerverfolger durchsuchst**. Wenn du zu dem Schluss gekommen bist, dass es keine bereits existierenden Tickets / Diskussionen gibt, ist der nächste Schrittː
2.  Starte einen Forumsbeitrag, um deinen Funktionsanfrage mit der Gemeinschaft über das [Diskussionsforum öffnen](http://forum.freecadweb.org/viewforum.php?f=8) zu diskutieren.
3.  Sobald die Gemeinschaft damit einverstanden ist, dass es sich um ein gültige Funktion handelt, kannst du ein Ticket auf dem Fehlerverfolger öffnen (legen es unter *Funktionsanfrage* statt *Fehler* ab).

-   **ANMERKUNG \#1** Um die Dinge in Ordnung zu halten, denke bitte daran, die URL des Forumsbeitrag in das Ticket und die Ticketnummer (als Verknüpfung) in den Forumbeitrag zu verknüpfen.
-   **ANMERKUNG \#2** Beachte bitte, dass es keine Garantien gibt, dass dein Wunsch erfüllt wird.

![FreeCAD Fehlerverfolger-Berichtsseite - verwende die Auswahlliste, um korrekt zu bestimmen, was das Ticket ist](images/MantisBT-setting-Feature-Request.jpg )

## Einreichen von Änderungssätzen 


<div class="mw-translate-fuzzy">

Falls du eine Fehlerbehebung, eine Erweiterung oder etwas anderes programmiert hast, das in FreeCAD von öffentlichem Nutzen sein kann, erstelle einen Änderungssatz mit dem Git diff Werkzeug und sende ihn auf demselben Fehlerverfolger (Datei als *Patch* ablegen).


</div>

## Zusammenführen anfragen 

(Dieselben Richtlinien wie [Einreichen von Änderungssätzen](https://www.freecadweb.org/wiki/Tracker#Submitting_patches))

Wenn du einen Git Zweig erstellt hast, der Änderungen enthält, die du gerne im FreeCAD Code zusammengeführt sehen möchtest, kannst du dort darum bitten, dass dein Zweig überprüft und zusammengeführt wird, wenn die FreeCAD Entwickler damit einverstanden sind. Du musst zuerst deinen Zweig in einem öffentlichen Git Repositorium (github, gitlab, bitbucket, sourceforge etc\...) veröffentlichen und dann die URL deines Zweiges in deiner Zusammenführungsanfrage angeben.

## MantisBT Tips und Tricks 

### MantisBT Kennzeichnungen 

MantisBT (Mantis Bug Tracker) hat seine eigene einzigartige Kennzeichnung.

-   **@**mention - funktioniert genau wie bei GitHub, wo, wenn du dem Benutzernamen von jemandem ein \'@\' voranstellen, dieser eine E-Mail erhält, dass er in einem Ticket Beitrag \'erwähnt\' wurde.

<img alt="" src=images/mantisbt-mention-example.jpg  style="width:600px;">

-   **\#**1234 - Durch Hinzufügen eines Hashtags vor einer Nummer wird eine Verknüpfung zu einem anderen Ticket innerhalb von MantisBT angezeigt.

    :   **Hinweis**\': wenn du der Maus über ein Ticket fährst, wird dir die Zusammenfassung angezeigt + wenn das Ticket geschlossen ist, wird es durchgestrichen wie \#1234.

<img alt="" src=images/mantisbt-ticket-shortcut-example.jpg  style="width:600px;">

-   **\~**5678 - eine Abkürzung, die auf einen Fehlerhinweis innerhalb eines Tickets verweist. Dies kann verwendet werden, um auf die Antwort von jemandem innerhalb des Beitrags zu verweisen. Jede Person, die einen Beitrag verfasst, zeigt eine eindeutige Nummer \~\#\#\#\# neben ihrem Benutzernamen. Wenn du dir das Bild im Beispiel ansiehst, siehst du, dass die Abkürzung auf die *Ticketnummer:Kommentarnummer* des besagten Tickets verweist

<img alt="" src=images/mantisbt-comment-shortcut-example.jpg  style="width:600px;">

-   **\<del\>\</del\>** - Die Verwendung dieser Tags wird Text durchstreichen.

<img alt="" src=images/mantisbt-strikeout-text-example.jpg  style="width:600px;">

-   **\<code\>\</code\>** - Um eine Zeile oder einen Code Block zu präsentieren, verwende diesen Tag, und er wird ihn elegant einfärben und differenzieren.

<img alt="" src=images/mantisbt-colorized-code-example.jpg  style="width:600px;">

### MantisBT BBCode 

Zusätzlich zu dem obigen [MantisBT Kennzeichnung](Tracker/de#MantisBT_Markup.md) hat man auch die Möglichkeit, das BBCode Format zu verwenden. Für eine umfassende Liste siehe die [BBCode plus Plugin Seite](https://github.com/mantisbt-plugins/BBCodePlus#supported-bbcode-tags). Hier ist eine Liste der unterstützten BBCode tagsː 
[img][/img] - Bilder
[url][/url] - Verweise
[email][/email] - E-Mail Adressen
[color=red][/color] - Farbiger Text
[highlight=yellow][/highlight] - Hervorgehobener Text
[size][/size] - Schriftgröße
[list][/list] - Listen
[list=1][/list] - Nummerierte Listen (Zahl ist die Startnummer)
[*] - Punkte auflisten
[b][/b] - Fett
[u][/u] - Unterstreichen
[i][/i] - Kursiv
[s][/s] - Durchgestrichen
[left][/left] - Linksbündig
[center][/center] - Zentriert
[right][/right] - Rechtsbündig
[justify][/justify] - Blockanordnung
[hr] - Horizontale Regel
[sub][/sub] - tiefgestellt
[sup][/sup] - Hochgestellt
[Tabelle][/Tabelle] - Tabelle
[table=1][/table] - Tabelle mit Rahmen der angegebenen Breite
[tr][/tr] - Tabellenzeile
[td][/td] - Tabellenspalte
[code][/code] - Code Block
[code=sql][/code] - Codeblock mit Sprachdefinition
[code start=3][/code] - Codeblock mit Zeilennummern, die mit der Zahl beginnen
[quote][/quote] - Zitat von *einem* (kein Name)
[quote=name][/quote] - Zitat nach *Name*


=== MantisBT \<=\> GitHub Kennzeichnung === Unten sind spezielle MantisBT Quellcode Integrations Zusatzmodul Schlüsselwörter, die mit dem FreeCAD GitHub Repo verknüpfen. Siehe [GitHubd und MantisBT](Tracker#GitHub_and_MantisBT.md).

-   **c:FreeCAD:git commit hash:** - **c** steht für \'commit\'. FreeCAD steht für das FreeCAD GitHub Repo. \'git commit hash\' ist der spezifische Git Commit Hash, auf den verwiesen wird. Hinweis: Der abschließende Doppelpunkt ist notwendig. Beispielː cːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **d:FreeCAD:git commit hash:** - Ähnlich zum oberen \"d\" steht für \"diff\", was eine Diff Ansicht der commit liefert. Beispielː dːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **p:FreeCAD:pullrequest:** - Ähnlich zum oberen, **p** steht für Pull Request. Beispielː pːFreeCADː498ː

<img alt="" src=images/mantisbt-source-integration-markup.jpg  style="width:600px;"> 

## GitHub und MantisBT 

Der FreeCAD Fehlerverfolger verfügt über ein ZUsatzprogramm namens [Quellintegration](https://github.com/mantisbt-plugins/source-integration), das im Wesentlichen sowohl das FreeCAD GitHub Repo als auch unseren MantisBT Fehlerverolger verbindet. Es macht es einfacher, Git Verpflichtungen zu verfolgen und mit ihren jeweiligen MantisBT Tickets zu verknüpfen. **Das Quellintegrationszusatzprogramm durchsucht die Git Verpflichtungsnachrichten nach bestimmten Schlüsselwörtern, um die folgenden Aktionen auszuführen:**

**Hinweis** Die folgenden Schlüsselwörter müssen in der git commit message und nicht im PR Thema hinzugefügt werden

### Fernreferenzierung eines Tickets 

Durch die Verwendung dieses Musters wird ein Git Commit automatisch einem Ticket zugeordnet (**Hinweis:**\' dies wird das Ticket nicht schließen). Das Format wird von MantisBT erkannt: The format MantisBT will recognize:

-   bug \#1234
-   bugs \#1234, \#5678
-   issue \#1234
-   issues \#1234, \#5678
-   report \#1234
-   reports \#1234, \#5678

Für die Neugierigen hier ist die regex, die MantisBT für diese Operation verwendet:


### Ferngesteuerte Lösung eines Tickets 

Das Format wird von MantisBT erkannt:\* fix \#1234

-   fixed \#1234
-   fixes \#1234
-   fixed \#1234, \#5678
-   fixes \#1234, \#5678
-   resolve \#1234
-   resolved \#1234
-   resolves \#1234
-   resolved \#1234, \#5678
-   resolves \#1234, \#5678

Für die Neugierigen hier ist die regex, die MantisBT für diese Operation verwendet:


## Verwandtes

-   [Fehlersichtung](Bug_Triage/de.md)
-   [Quellcodeverwaltung](Source_Code_Management/de.md)







[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Administration](Category_Administration.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Tracker/de
