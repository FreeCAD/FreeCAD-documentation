# Interface Customization/de







{{TOCright}}

## Einführung

Die FreeCAD Oberfläche basiert auf dem modernen [Qt](http://en.wikipedia.org/wiki/Qt_(toolkit)) Werkzeugsatz und hat einen Aufbau nach Stand der Technik. Einige Aspekte der Oberfläche können angepasst werden. Du kannst z.B. benutzerdefinierte Werkzeugleisten hinzufügen, mit Werkzeugen von mehreren Arbeitsbereichen oder in Makros festgelegten Werkzeugen, und du kannst eigene Tastaturkürzel erstellen. Die Menüs und Standardwerkzeugleisten, die mit FreeCAD und seinen Arbeitsbereichen geliefert werden, können jedoch nicht geändert werden.

![](images/Std_DlgCustomize_tab_Toolbars.png ) *Das Dialogfeld Anpassen*

## Anwendung

1.  Die im Dialogfeld Anpassen verfügbaren Befehle hängen von den Arbeitsbereichen ab, die in der aktuellen FreeCAD Sitzung geladen wurden. Du solltest also zunächst alle Arbeitsbereiche laden, auf deren Befehle du Zugriff haben möchtest.
2.  Es gibt mehrere Wege, das Dialogfeld <img alt="" src=images/Std_DlgCustomize.svg  style="width:16px;"> [Std DlgAnpassen](Std_DlgCustomize/de.md) aufzurufen:
    -   Wähle die {{MenuCommand/de|Werkzeuge → <img src="images/Std_DlgCustomize.svg" width=16px> Anpassen...}} Option aus dem Menü.
    -   Rechtsklicke einen Werkzeugleistenbereich und wähle **<img src="images/Std_DlgCustomize.svg" width=16px> Anpaasen...** aus dem Kontextmenü.
3.  Ein Dialogfeld Anpassen öffnet sich. Für weitere Informationen siehe [Optionen](#Optionen.md).
4.  Die **Hilfe** Schaltfläche funktioniert zur Zeit nicht.
5.  Drücke die **Schließen** Schaltfläche um das Dialogfeld zu schließen.

## Optionen

Im Dialogfeld Anpassen sind die folgenden Reiter verfügbar:

### Befehle

![](images/Std_DlgCustomize_tab_Commands.png ) *Der Befehlsreiter*

Auf diesem Reiter kannst Du die verfügbaren Befehle durchsuchen.

#### Befehle durchsuchen 

1.  Wähle eine Befehlskategorie im **Kategorie** Paneel auf der linken Seite. Einige Kategorien entsprechen Menüeinträgen.
2.  Die in der gewählten Kategorie verfügbaren Werkzeuge werden im Paneel auf der rechten Seite angezeigt.
3.  Bewege den Mauszeiger über einen Befehl: Seine Werkzeugspitze wird angezeigt.
4.  Wähle einen Befehl aus: Sein Statusleistentext wird unterhalb der beiden Paneele angezeigt.


{{Top}}

### Tastatur

![](images/Std_DlgCustomize_tab_Keyboard.png ) *Der Tastaturreiter*

Auf diesem Reiter können benutzerdefinierte Tastaturkürzel definiert werden. Tastaturkürzel für Makrobefehle können auf dem [Makros](#Makros.md) Reiter definiert werden.

#### Hinzufügen eines benutzerdefinierten Tastenkürzels 

1.  Wähle eine Befehlskategorie aus der Aufklappliste **Kategorie**.
2.  Wähle einen Befehl aus dem **Befehle** Paneel.
3.  Das Feld **Aktuelles Tastenkürzel** zeigt das aktuelle Tastenkürzel an, falls vorhanden.
4.  Gib ein neues Tastaturkürzel in das Eingabefeld **Drücke neues Tastaturkürzel** ein. Tastenkombinationen können bis zu 4 Eingaben lang sein. Jede Eingabe ist entweder ein einzelnes Zeichen, eine Kombination aus einer oder mehreren Sondertasten oder eine Kombination aus einer oder mehreren Sondertasten und einem Zeichen. Verwende **Zurück**, um Fehler zu korrigieren.
5.  Wenn das Tastenkürzel bereits verwendet wird, wirst du in einem Dialogfeld gefragt, ob du es überschreiben möchtest, und der Befehl, dem das Tastenkürzel zugewiesen ist, wird im Feld **Aktuell zugewiesen an** angezeigt.
6.  Drücke die Taste **Zuweisen**, um das neue Tastenkürzel zuzuweisen.
7.  Drücke die Schaltfläche **Löschen**, um das eingegebenen Tastenkürzel zu entfernen. Dadurch wird auch der Inhalt des Feldes **Aktuelle Tastenkombination** entfernt. Beachte, dass Standardverknüpfungen nicht dauerhaft entfernt werden. Sie werden beim Neustart von FreeCAD wiederhergestellt.

#### Entfernen eines benutzerdefinierten Tastenkürzels 

1.  Wähle eine Befehlskategorie aus der Ausklappliste **Kategorie**.
2.  Wähle einen Befehl aus dem **Befehle** Paneel.
3.  Drücke die **Zurücksetzen** Taste.

#### Alle benutzerdefinierten Tastenkürzel entfernen 

1.  Drücke die **Alles Zurücksetzen** Schaltfläche.

#### Hinweise (Tastatur) 

-   Tastenkürzel funktionieren nur, wenn ihre Befehle im Standardmenü oder im Menü eines Arbeitsbereichs erscheinen, die in der aktuellen FreeCAD Sitzung geladen wurde, oder wenn ihre Befehle in einer *sichtbaren* Werkzeugleiste erscheinen.

-   In V0.19 gibt es ein Problem mit einigen Entwurf Befehlen. Ihre Standard Tastenkürzel funktionieren nicht und/oder ihnen können keine benutzerdefinierten Tastenkürzel zugewiesen werden.
-   Um eine Standard Tastenkürzel neu zuzuweisen, muss zuerst ein neues Tastenkürzel dem ursprünglichen Befehl zugewiesen werden.


{{Top}}

### Arbeitsbereiche

![](images/Std_DlgCustomize_tab_Workbenches.png ) *Der Arbeitsbereiche Reiter*

Auf diesem Reiter kann die [Arbeitsbereichswählerliste](Std_Workbench/de.md) geändert werden. Die Liste **Aktivierte Arbeitsbereiche** zeigt die Arbeitsbereiche, wie sie in der Arbeitsbereichsauswahl erscheinen werden.

#### Deaktivieren eines Arbeitsbereichs 

1.  Wähle einen Arbeitsbereich in der Liste **Aktivierte Arbeitsbereiche** aus.
2.  Drücke die **<img src="images/Button_left.svg" width=16px>** Taste.
3.  Der Arbeitsbereich wird in die Liste **Deaktivierte Arbeitsbereiche** verschoben.

#### Wieder-aktiviere einen Arbeitsbereich 

1.  Wähle einen Arbeitsbereich in der Liste **Deaktivierte Arbeitsbereiche** aus.
2.  Drücke die Taste **<img src="images/Button_right.svg" width=16px>**.
3.  Der Arbeitsbereich wird in die Liste **Aktivierte Arbeitsbereiche** verschoben.

#### Wieder-aktiviere alle Arbeitsbereiche 

1.  Drücke die **<img src="images/Button_add_all.svg" width=16px>** Schaltfläche.

#### Ändern einer Arbeitsbereichsposition 

1.  Wähle einen Arbeitsbereich in der Liste \"aktive Arbeitsbereiche\" aus.
2.  Drücke die Taste **<img src="images/Button_up.svg" width=16px>** oder **<img src="images/Button_down.svg" width=16px>**.
3.  Wiederhole bis sich der Arbeitsbereich in der richtigen Position befindet.

#### Arbeitsbereiche alphabetisch sortieren 

1.  Drücke die **<img src="images/Button_sort.svg" width=16px>** Schaltfläche.


{{Top}}

### Werkzeugleisten

![](images/Std_DlgCustomize_tab_Toolbars.png ) *Der Werkzeugleistenreiter*

Auf diesem Reiter können benutzerdefinierte Werkzeugleisten erstellt und geändert werden.

#### Wählen des Arbeitsbereichs 

1.  Wähle in der Dropdown-Liste auf der rechten Seite den Arbeitsbereich dessen Werkzeugleiste du verändern möchtest. Die Option {{Value|Global}} ist für Toolbars, die in allen Arbeitsbereichen zur Verfügung stehen sollen.

#### Werkzeugleiste erstellen 

1.  Drücke die Taste **New...**.
2.  Gib deiner neuen Werkzeugleiste einen Namen in der Dialog-Box, die sich öffnet.
3.  Drücke die Taste **OK**.
4.  Die neue Werkzeugleiste erscheint in der Liste auf der rechten Seite.

#### Umbenennen einer Werkzeugleiste 

1.  Wähle eine Werkzeugleiste in der Liste auf der rechten Seite.
2.  Drücke die Taste **Rename...**.
3.  Gib einen neuen Namen in der Dialog-Box, die sich öffnet, ein.
4.  Drücke die Taste **OK**.

#### Löschen einer Werkzeugleiste 

1.  Wähle eine Werkzeugleiste in der rechten Liste.
2.  Drücke die Taste **Delete**.

#### Werkzeugleiste deaktivieren 

1.  Entferne das Häkchen vor der Werkzeugleiste in der rechten Liste.

Eine inaktive Werkzeugleiste wird im FreeCAD Userinterface nicht angezeigt.

#### Einen Befehl hinzufügen 

1.  Mindestens eine benutzerdefinierte Symbolleiste ist erforderlich. Siehe [Werkzeugleiste Erstellen](#Werkzeugleiste_erstellen.md).
2.  Wähle die entsprechende Werkzeugleiste in der Liste auf der rechten Seite aus. Wenn keine Werkzeugleiste ausgewählt ist, wird dein neues Kommando zur ersten Werkzeugleiste in der Liste hinzugefügt.
3.  Wähle eine Kategorie aus der linken Liste. Macro-Kommandos, die im Tab [Macros](#Macros.md) eingerichtet wurden, erscheinen in der \'Macros\'-Kategorie.
4.  Wähle ein Kommando aus der linken Liste.
5.  Oder wähle \'\' um einen Abstandshalter hinzuzufügen (eine Trennlinie).
6.  Drücke die Schaltfläche **<img src="images/Button_right.svg" width=16px>**.

#### Entfernen eines Befehls 

1.  Falls erforderlich erweitere die Werkzeugleiste auf der rechten Seite.
2.  Wähle die Schaltfläche aus, die du entfernen möchtest.
3.  Drücke die Schaltfläche **<img src="images/Button_left.svg" width=16px>**.

#### Ändern einer Befehlsposition 

1.  Falls notwendig öffne die Werkzeugleiste in der rechten Liste.
2.  Wähle eine Schaltfläche aus.
3.  Drücke die Taste **<img src="images/Button_up.svg" width=16px>** oder **<img src="images/Button_down.svg" width=16px>**.
4.  Wiederhole das bis die Schaltfläche an der richtigen Position erscheint.

#### Hinweise (Werkzeugleisten) 

-   Werkzeugleisten, die zum aktuellen Arbeitsbereich gehören, werden sofort aktualisiert. Aber nach einer Aktivierung oder Deaktivierung einer Werkzeugleiste muss zunächst irgend ein anderer Arbeitsbereich ausgewählt werden um die Darstellung zu aktualisieren.
-   Das Gleiche gilt für globale Werkzeugleisten. Auch hier muss erst ein anderer Arbeitsbereich aufgerufen werden um Änderungen (Hinzufügen oder Entfernen von Schaltflächen) zu aktualisieren. Falls die Reihenfolge von globalen Werkzeugleisten geändert wurde oder diese umbenannt wurden, braucht es sogar einen Neustart um die Änderungen anzuzeigen.

-   In der version 0.19 gibt es ein Problem mit manchen neuen (\'Draft\') Kommandos. Nachdem sie zu einer Werkzeugleiste hinzugefügt wurden müssen sie noch manuell im File {{FileName|user.cfg}} bearbeitet werden. Dazu muss man zunächst das Programm schließen. Suche dann in dem File die entsprechende Werkzeugleiste und ändere in diesem Abschnitt den Inhalt der `FCText`-Elemente, die mit `gui_` beginnen, auf `DraftTools`.


{{Top}}

### Makros

![](images/Std_DlgCustomize_tab_Macros.png ) *Der Reiter Makros*

Auf diesem Tab können Makro-Kommandos eingerichtet werden. Sobald sie eingerichtet wurden, können sie einer Werkzeugleiste hinzugefügt werden. FreeCAD verwendet einen speziellen Ordner für User-Makros und nur Makros in diesem Folder können eingerichtet werden. Verwende die Kommandos <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:16px;"> [Std DlgMacroExecute](Std_DlgMacroExecute.md) um diesen Ordner auf deinem System zu finden.

Wenn du ein Makro mit <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Addon Manager](Std_AddonMgr.md) herunterladest, vergiss nicht auch das zugehörige Icon-File herunterzuladen. Die meisten Makros haben einen Link auf ein Bild das im Addon Manager dargestellt wird. Du kannst dieses Bild z.B. in den Ordner für User-Makros legen.

Wenn du Makros aus einer anderen Quelle verwenden willst, musst du sie manuell installieren. Dazu findest du mehr Informationen unter [How to install macros](How_to_install_macros.md).

#### Hinzufügen eines Makrobefehls 

1.  Wähle ein Makro in der \"Makro\"-Dropdownliste.
2.  Gib einen \"Menu text\" ein. Das ist der Name des Makros der auch in Werkzeugleisten angezeigt wird, wenn kein zugehöriges Icon vorhanden ist.
3.  Vergib einen \"Tool tip\". Dieser Hilfstext erscheint in der Nähe der Maus, wenn du mit dieser über der Schaltfläche verharrst.
4.  Vergib einen \"Status text\". Dieser wird im [status bar](Status_bar.md) angezeigt, wenn du mit der Maus über die Schaltfläche fährst.
5.  Vergib (falls vorhanden) einen Link auf eine Wiki-Seite für das Makro im \"What\'s this\"-Eingabefeld. Gib dort den Namen der Seite an - nicht die ganze URL!
6.  Vergib (falls gewünscht) ein Tastenkürzel im \"Accelerator\"-Eingabefeld. Mehr dazu unter: [Keyboard](#Keyboard.md)
7.  Um ein Icon hinzuzufügen:
    1.  Drücke die \"Pixmap\"- **...** - Schaltfläche.
    2.  Es öffnet sich ein Dialogfenster um ein Icon auszuwählen.
    3.  Falls erforderlich, drücke die Schaltfläche **Icon folders...** um einen Icon-Ordner hinzuzufügen.
    4.  Wähle ein Icon aus. (Daraufhin schließt sich das Dialogfenster.)
8.  Drücke die Schaltfläche **Add**.
9.  Daraufhin erscheint das Makro in der linken Liste.
10. Jetzt kann das Makro im [Toolbars](#Toolbars.md)-Tab ausgewählt werden.

#### Entfernen eines Makrobefehls 

1.  Wähle ein Makro in der linken Liste aus.
2.  Drücke die Schaltfläche **Remove**.

#### Ändern eines Makrobefehls 

1.  Dopple-Klicke den Makrobefehl im Bedienfeld zur Linken.
2.  Mach die erforderlichen Änderungen. Beachte, daß du Symbole nicht entfernen kannst. Du kannst sie nur ersetzen.
3.  Drücke die **Ersetzen** Taste.


{{Top}}

### Spaceball Bewegung 

Wenn kein Spaceball erkannt wurde ist dieser Reiter leer. Siehe: [3DVerbindung Eingabegeräte](3Dconnexion_input_devices/de.md). {{Top}}

### Spaceball Tasten 

Wenn kein Spaceball erkannt wurde ist dieser Tab leer. Siehe: [3Dconnexion input devices](3Dconnexion_input_devices.md). {{Top}}

## Themen

FreeCAD unterstützt die vollständige Themensetzung der Oberfläche über .qss stylesheets. Das [qss Format](https://doc.qt.io/qt-5/stylesheet-syntax.html) ist dem in Webseiten verwendeten [css Format](https://en.wikipedia.org/wiki/CSS) sehr ähnlich, es fügt im Grunde Methoden hinzu, um die verschiedenen Widgets und Elemente der Qt Oberfläche zu referenzieren. Du kannst das Standardthema (das einfach den von deinem Desktopsystem definierten Stil übernimmt) ändern, indem du ein **Stylesheet** in den [FreeCAD Voreinstellungen](Preferences_Editor/de#Allgemein.md) auswählst.

Du kannst auch ein eigenes Thema erstellen, wenn du mit den Themen, die mit FreeCAD mitgeliefert werden, nicht zufrieden bist, z.B. indem du ein [existierende Gestaltungsbögen](https://github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets) bearbeitest. Ihre neue Grstaltung muss in einem bestimmten Ordner abgelegt werden, damit er von FreeCAD gefunden wird:

-    {{Dateiname|%APPDATA%/FreeCAD/Gui/Stylesheets}}(unter Windows). Der Ordner {{Dateiname|%APPDATA%}} kann durch Eingabe von {{Incode|App.getUserAppDataDir()}} in der [Python-Konsole](Python_console.md) abgerufen werden.

-    {{FileName|$HOME/.FreeCAD/Gui/Stylesheets}}(unter Linux).

-    {{Dateiname|$HOME/Library/Preferences/FreeCAD/Gui/Stylesheets}}(unter MacOS).


{{Top}}

## Erweiterungen

Erweiterungen bieten eine weitere Möglichkeit, die Benutzeroberfläche anzupassen. Nachfolgend sind einige von Anwendern erstellte Erweiterungen aus der FreeCAD Gemeinschaft. Sie können über den <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Addon Manager](Std_AddonMgr.md) heruntergeladen werden (Hinweis: Sie sind auf dem Arbeitsbereiche Reiter aufgeführt).

### KubusMenü

-   Github Repositorium: <https://github.com/triplus/CubeMenu>

### Glass

-   Github Repositorium: <https://github.com/triplus/Glass>.

### SymbolGestaltung

-   Github Repositorium: <https://github.com/triplus/IconThemes>

### Startprogramm

-   Github Repositorium: <https://github.com/triplus/Launcher>.

### PieMenü

-   Github Repositorium: <https://github.com/triplus/PieMenu>.

### RemBench

-   Github Repositorium: <https://github.com/triplus/RemBench>.

### TastenKürzel

-   Github Repositorium: <https://github.com/triplus/ShortCuts>.


{{Top}}





{{Std Base navi

}} {{Interface navi}} 
