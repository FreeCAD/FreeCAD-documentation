# Interface Customization/de
## Einleitung

Die FreeCAD-Oberfläche basiert auf dem modernen [Qt](http://en.wikipedia.org/wiki/Qt_(toolkit))-Werkzeugsatz und ist dem Stand der Technik entsprechend aufgebaut. Einige Bestandteile der Oberfläche können angepasst werden. Es können z.B. benutzerdefinierte Symbolleisten mit Werkzeugen aus verschiedenen Arbeitsbereichen oder mit auf Makros basierenden Werkzeuge hinzugefügt werden, und es können eigene Tastaturkürzel erstellt werden. Die Menüs und Standardsymbolleisten, die von FreeCAD und seinen Arbeitsbereichen mitgeliefert werden, können jedoch nicht geändert werden.

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*Das Dialogfeld Benutzerdefiniert*



## Anwendung

1.  Die im Dialogfeld Benutzerdefiniert verfügbaren Befehle hängen von den Arbeitsbereichen ab, die in der aktuellen FreeCAD-Sitzung geladen wurden. Es sollten also zunächst alle Arbeitsbereiche geladen werden, auf deren Befehle zugegriffen werden soll.
2.  Es gibt mehrere Wege, das Dialogfeld [Benutzerdefiniert](Std_DlgCustomize/de.md) aufzurufen:
    -   Den Menüeintrag **Werkzeuge → <img src="images/Std_DlgCustomize.svg" width=16px> Benutzerdefiniert...** auswählen.
    -   Einen Werkzeugleistenbereich mit der rechten Maustaste anklicken und im Kontextmenü **<img src="images/Std_DlgCustomize.svg" width=16px> Benutzerdefiniert...** auswählen.
3.  Das Dialogfeld **Anpassen** öffnet sich. Für weitere Informationen siehe [Optionen](#Optionen.md).
4.  Die Schaltfläche **Hilfe** funktioniert zurzeit nicht.
5.  Die Schaltfläche **Schließen** drücken, um das Dialogfeld zu schließen.



## Optionen

Im Dialogfeld Benutzerdefiniert sind die folgenden Reiter verfügbar:



### Tastatur

![](images/Std_DlgCustomize_tab_Keyboard.png ) 
*Der Reiter Tastatur*

Auf diesem Reiter können benutzerdefinierte Tastaturkürzel festgelegt werden. Tastaturkürzel für Makrobefehle können auf dem Reiter [Makros](#Makros.md) definiert werden.



#### Suchen

Man kann nach Befehlen suchen, indem man mindestens 3 Zeichen eines Menütextes oder eines Namens in das Suchfeld eingibt. Die Suche unterscheidet nicht zwischen Groß- und Kleinschreibung.

Auch das Suchen nach Tastaturkürzeln ist möglich:

-   Im Suchfeld müssen spezielle Tasten in Tastaturkürzeln als Zeichenkette eingegeben werden. So gibt man beispielsweise für Befehle mit einem **Ctrl** im Kürzel {{Value|ctrl}} ein (4 Buchstaben).
-   Mit Klammern sucht man nach Kürzeln mit nur einem Zeichen, z.B. {{Value|(c)}}.
-   Mit Komma und Leerzeichen zwischen den Zeichen sucht man nach Kürzeln, die aus mehreren Zeichen bestehen, z.B. {{Value|g, b, b}}.



#### Ein Tastaturkürzel hinzufügen 

1.  Eine Befehlskategorie in der Auswahlliste **Kategorie** auswählen.
2.  Einen Befehl aus der **Befehle**-Tabelle auswählen.
    -   Wahlweise eine der Spaltenüberschriften {{Value|Befehl}}, {{Value|Tastaturkürzel}} oder {{Value|Standard}} anklicken, um die Sortierreihenfolge der Tabelle zu ändern.
    -   Wahlweise den Trenner nach rechts ziehen, um die Tabellenansicht zu erweitern.
3.  Das Feld **Aktuell verwendete Tastenkombination** zeigt das aktuelle Tastaturkürzel an, falls vorhanden.
4.  Ein neues Tastaturkürzel in das Eingabefeld **Neue Tastenkombination** eingeben. Tastaturkürzel können aus bis zu 4 Eingaben bestehen. Jede Eingabe ist entweder ein einzelnes Zeichen, eine Kombination aus einer oder mehreren Sondertasten oder eine Kombination aus einer oder mehreren Sondertasten und einem Zeichen. **Zurück**-Taste (Backspace) drücken, um Fehler zu korrigieren.
5.  Andere aktive Befehle (siehe [Hinweise](#Hinweise.md)), die dasselbe Tastaturkürzel verwenden, sind in der **Prioritätenliste für Tastenkombinationen** aufgelistet.
6.  Die Schaltfläche **Zuweisen** drücken, um das neue Tastaturkürzel zuzuweisen.
7.  Enthält die **Prioritätenliste für Tastenkombinationen** mehr als einen Befehl: Wahlweise die Reihenfolge anpassen, indem einzelne Befehle ausgewählt und durch Drücken der Schaltflächen **Hoch** oder **Runter** verschoben werden. Verwenden mehrere aktive Befehle dasselbe Tastaturkürzel, wird der Befehl ausgeführt, der an der obersten Stelle gelistet ist.



#### Ein Tastaturkürzel entfernen 

1.  Eine Befehlskategorie in der Auswahlliste **Kategorie** auswählen.
2.  Einen Befehl aus der **Befehle**-Tabelle auswählen.
3.  Die Schaltfläche **Löschen** drücken.



#### Ein Standard-Tastaturkürzel wiederherstellen 

1.  Wähle eine Befehlskategorie aus der Ausklappliste **Kategorie**.
2.  Wähle einen Befehl aus dem **Befehle** Paneel.
3.  Drücke die **Zurücksetzen** Taste.



#### Alle Standard-Tastaturkürzel wiederherstellen 

1.  Die Schaltfläche **Alles Zurücksetzen** drücken.



#### Hinweise

-   Tastaturkürzel funktionieren nur für aktive Befehle. Aktive Befehle sind solche, die im Standardmenü oder im Menü des aktiven Arbeitsbereichs angezeigt werden oder Befehle einer *sichtbaren* Symbolleiste.


{{Top}}



### Symbolleisten

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*Der Reiter Symbolleisten*

Auf diesem Reiter können benutzerdefinierte Symbolleisten erstellt und geändert werden.



#### Suchen 

Siehe [Tastatur](#Suche.md).



#### Einen Arbeitsbereich auswählen 

1.  In der Ausklappliste auf der rechten Seite den Arbeitsbereich auswählen, dessen Symbolleiste geändert werden soll. Die Option {{Value|Global}} ist für Symbolleisten, die in allen Arbeitsbereichen zur Verfügung stehen sollen.



#### Eine Symbolleiste erstellen 

1.  Die Schaltfläche **New...** drücken.
2.  Einen Namen in der Dialog-Box eingeben, die geöffnet wird.
3.  Die Schaltfläche **OK** drücken.
4.  Die neue Symbolleiste erscheint in der Liste auf der rechten Seite.



#### Eine Symbolleiste umbenennen 

1.  Eine symbolleiste in der Liste auf der rechten Seite auswählen.
2.  Die Schaltfläche **Umbenennen...** drücken.
3.  Einen neuen Namen in der Dialog-Box eingeben, die geöffnet wird.
4.  Die Schaltfläche **OK** drücken.



#### Eine Symbolleiste löschen 

1.  eine Symbolleiste in der rechten Liste auswählen.
2.  Die Schaltfläche **Löschen** drücken.



#### Eine Symbolleiste deaktivieren 

1.  Die Checkbox vor dem Namen der Symbolleiste in der rechten Liste deaktivieren.
2.  Eine deaktivierte Symbolleiste wird auf der FreeCAD-Oberfläche nicht angezeigt.



#### Einen Befehl hinzufügen 

1.  Es ist mindestens eine benutzerdefinierte Symbolleiste erforderlich. Siehe [Werkzeugleiste Erstellen](#Werkzeugleiste_erstellen.md).
2.  Die entsprechende Symbolleiste in der Liste auf der rechten Seite auswählen. Wenn keine Symbolleiste ausgewählt ist, wird der neue Befehl zur ersten Symbolleiste in der Liste hinzugefügt.
3.  Eine Befehlskategorie in der Auswahlliste **Kategorie** auswählen. Makro-Befehle, die im Reiter [Makros](#Makros.md) eingerichtet wurden, erscheinen in der Kategorie {{Value|Makros}}.
4.  Einen Befehl aus der **Befehle**-Tabelle auswählen oder {{Value|<Trennlinie>}} auswählen, um eine Trennlinie zwischen zwei Schaltflächen einzufügen.
    -   Wahlweise den Trenner nach rechts ziehen, um die Tabellenansicht zu erweitern.
5.  Die Schaltfläche **<img src="images/Button_right.svg" width=16px>** drücken.



#### Einen Befehl entfernen 

1.  Falls erforderlich, die Symbolleiste im Feld auf der rechten Seite aufklappen.
2.  Die Schaltfläche auswählen, die entfernt werden soll.
3.  Die Schaltfläche **<img src="images/Button_left.svg" width=16px>** drücken.



#### Die Position eines Befehls ändern 

Falls erforderlich, die Symbolleiste im Feld auf der rechten Seite aufklappen.

1.  Einen Befehl auswählen.
2.  Die Schaltfläche **<img src="images/Button_up.svg" width=16px>** oder **<img src="images/Button_down.svg" width=16px>** drücken.
3.  Wahlweise wiederholen, bis sich der Befehl an der richtigen Position befindet.



#### Hinweise 

-   Symbolleisten, die zum aktuellen Arbeitsbereich gehören, werden sofort aktualisiert. Aber nach dem Aktivieren oder Deaktivieren einer Symbolleiste muss zunächst zu irgend einem anderen Arbeitsbereich und zurück gewechselt werden, um die Darstellung zu aktualisieren.
-   Das Gleiche gilt für globale Symbolleisten nach dem Hinzufügen oder Entfernen von Schaltflächen. Auch hier muss zu einem anderen Arbeitsbereich und zurück gewechselt werden zu aktualisieren. Falls die Reihenfolge von globalen Symbolleisten geändert wurde oder eine Symbolleiste umbenannt wurde, ist ein Neustart erforderlich.


{{Top}}



### Makros

![](images/Std_DlgCustomize_tab_Macros.png ) 
*Der Reiter Makros*

Auf diesem Reiter können Makro-Befehle angelegt werden. Eimal angelegt, können sie zu benutzerdefinierten Symbolleisten hinzugefügt werden. Makros, die mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden, werden automatisch angelegt und zu einer Symbolleiste {{Value|Global}} hinzugefügt (siehe [Symbolleisten](#Symbolleisten.md)), wenn während des Installationsprozesses der Dialog **Schaltfläche hinzufügen** bestätigt wird.

Soll ein Makro aus einer anderen Quelle geladen werden, muss es manuell installiert werden. Siehe [Wie man Makros installiert](How_to_install_macros/de.md) für weitere informationen. Man beachte, dass FreeCAD einen besonderen Ordner für Makros verwendet und nur Makros aus diesem Ordner (als Schaltfläche) angelegt werden können. Mit dem Befehl <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:16px;"> [Std DialogMakroAusführen](Std_DlgMacroExecute/de.md) kann dieser Ordner im System des Benutzers gefunden werden.



#### Einen Makrobefehl hinzufügen 

1.  Ein Makro in der Auswahlliste \"Makro\" auswählen.
2.  Einen \"Menütext\" eingeben. Das ist der Name des Makros der auch in Symbolleisten angezeigt wird, wenn kein zugehöriges Symbol vorhanden ist.
3.  Wahlweise eine \"Quick-Info\" eingeben. Dieser Hilfstext erscheint in der Nähe des Mauszeigers, wenn er sich über der Schaltfläche befindet.
4.  Wahlweise einen \"Statustext\". Dieser wird in der [Statuszeile](Status_bar/de.md) angezeigt, wenn sich der Mauszeiger über der Schaltfläche befindet.
5.  Wahlweise (falls vorhanden) die zum Makro gehörende Wiki-Seite im Eingabefeld \"Direkthilfe\" eintragen; nur den Namen der Seite - nicht die ganze URL!
6.  Wahlweise ein Tastaturkürzel im Eingabefeld \"Tastenbelegung\" anlegen. Mehr dazu unter: [Tastatur](#Tastatur.md)
7.  Um ein Symbol hinzuzufügen:
    1.  Die Schaltfläche **Symbol** **...** drücken.
    2.  Das Dialogfenster **Symbol auswählen** wird geöffnet.
    3.  Falls erforderlich, die Schaltfläche **Symbol-Ordner...** drücken, um einen Symbol-Ordner hinzuzufügen.
    4.  Ein Symbol aus dem Fenster auswählen. Das Dialogfenster **Symbol auswählen** wird automatisch geschlossen.
8.  Die Schaltfläche **Hinzufügen** drücken.
9.  Der Makro-Befehl erscheint in der linken Liste.
10. Jetzt kann der Makro-Befehl im Reiter [Symbolleisten](#Symbolleisten.md) ausgewählt werden.



#### Einen Makrobefehl entfernen 

1.  Ein Makro in der linken Liste auswählen.
2.  Die Schaltfläche **Entfernen** drücken.



#### Einen Makrobefehl ändern 

1.  Den Makrobefehl in der linken Liste mit Doppelklick auswählen.
2.  Die erforderlichen Änderungen ausführen. Man beachte, daß die Symbole nicht entfernt wreden können; sie können nur ersetzt werden.
3.  Die Schaltfläche **Ersetzen** drücken.


{{Top}}



### Spaceball Bewegung 

Wenn kein Spaceball erkannt wurde ist dieser Reiter leer. Siehe: [3Dconnexion-Eingabegeräte](3Dconnexion_input_devices/de.md). 

### Spaceball Tasten 

Wenn kein Spaceball erkannt wurde, ist dieser Reiter leer. Siehe: [3Dconnexion-Eingabegeräte](3Dconnexion_input_devices/de.md). 

## Themen

FreeCAD unterstützt die vollständige Individualisierung der Oberfläche durch .qss-Stylesheets. Das [qss-Format](https://doc.qt.io/qt-5/stylesheet-syntax.html) ist dem in Webseiten verwendeten [css-Format](https://en.wikipedia.org/wiki/CSS) sehr ähnlich, es fügt im Grunde Methoden hinzu, um die verschiedenen Widgets und Elemente der Qt-Oberfläche zu referenzieren. Das Standardthema (das einfach den vom Desktopsystem definierten Stil übernimmt) kann angepasst werden, indem ein **Stylesheet** in den [FreeCAD-Voreinstellungen](Preferences_Editor/de#Allgemein.md) ausgewählt wird.

Es kann auch ein eigenes Thema erstellt werden, wenn man mit den Themen, die FreeCAD mitgeliefert, nicht zufrieden ist, z.B. indem ein [existierendes Stylesheet](https://github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets) bearbeitet wird. Das neue Aussehen (style) muss in einem bestimmten Ordner abgelegt werden, damit es von FreeCAD gefunden wird:

-    **%APPDATA%/FreeCAD/Gui/Stylesheets**(unter Windows). Der Ordner **%APPDATA%** kann durch Eingabe von {{Incode|App.getUserAppDataDir()}} in der [Python-Konsole](Python_console/de.md) abgerufen werden.

-    **$HOME/.FreeCAD/Gui/Stylesheets**(unter Linux).

-    **$HOME/Library/Application Support/FreeCAD/Gui/Stylesheets**(unter macOS).


{{Top}}



## Erweiterungen

Mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Addon-Manager](Std_AddonMgr/de.md) installierte Addons (Erweiterungen) bieten eine weitere Möglichkeit, die Benutzeroberfläche anzupassen. Es stehen einige spezielle [externe Arbeitsbereiche](External_workbenches/de.md) und [Voreinstellungspakete](Preference_Packs/de.md) zur Verfügung. {{Top}}





{{Std Base navi

}} {{Interface navi}}



---
⏵ [documentation index](../README.md) > Interface Customization/de
