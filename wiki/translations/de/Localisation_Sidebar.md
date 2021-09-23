# Localisation Sidebar/de
[Lokalisierung](Localisation/de.md) ist der Prozess der Bereitstellung von Software mit einer mehrsprachigen Benutzeroberfläche. Das Dokumentations-Wiki kann auch lokalisiert werden, wie im Abschnitt [Übersetze das FreeCAD Wiki](Localisation#Translate_the_FreeCAD_wiki/de.md) beschrieben.

Die Seitenleiste ist ein wichtiges Navigationswerkzeug in der Wiki Welt, siehe [1](https://www.mediawiki.org/wiki/Manual:Interface/Sidebar/de) für weitere Informationen.

## Übersetzen der Seitenleiste 

Die Seitenleiste ist nun vollständig übersetzbar mit der [Hilfe:Erweiterung:Übersetzen](https://www.mediawiki.org/wiki/Help:Extension:Translate/de) die für alle Wikiseiten verfügbar ist.

Im FreeCAD Wiki ist die Seitenleiste mit Hilfe von Vorlagen realisiert, die den Text abhängig von der gewählten Sprache ändern. Technische Details, wie diese Funktion realisiert wurde, sind im Forumsbeitrag [Wiki navigation / translation](http://forum.freecadweb.org/viewtopic.php?f=21&t=9687&start=10#p80441) beschrieben.

### Anweisungen

Du kannst auf die Sonderseite [Special:Translate/wiki-sidebar](Special:Translate/wiki-sidebar.md) gehen, um mit der Übersetzung zu beginnen.

Es gibt einen Fehler auf der Herunterladeseite. Du kannst den Verweis nicht auf \"Download/fr\", oder \"Download/de\", etc. umleiten. Stattdessen wird der Verweis auf die tatsächliche Übersetzung von \"Download\" in deiner Sprache verknüpft. Am besten ist es, diese neue Seite zu erstellen und eine Umleitung auf die richtige Seite einzurichten. Mehr über Umleitungen auf [Help:Editing/de](Help:Editing/de.md).

### Wichtige Anmerkungen 

Meistens gibt es zwei Zeichenfolgen für jeden Punkt in der Seitenleiste.

** {{int:sidebar-faq-target}}|sidebar-faq

Der Linke stellt das Ziel des Verweises und der Rechte den Text, der in der Seitenleiste angezeigt wird.

Man erkennt den Unterschied der beiden oben in der \'Übersetzungsbox\', in der der Name der Variablen steht. Wenn der Variablenname mit \"-target\" endet, bedeutet das, dass der Zeiger der Verknüpfung übersetzt wird. Das dient dazu, dass der Übersetzer die Verknüpfung auf die übersetzte Seite lenken kann, z.B. durch hinzufügen von \"/de\" hinter dem Namen der Seite für die deutsche Übersetzung.

NICHT \"/de\" (/fr, /es, \...) mit einfügen, wenn die Übersetzungseite in der Übersetzungsprache nicht existiert. Das wird die Verknüpfung auflösen. NICHTS weiteres eintragen, als den Namen der Seite. Das wird die Verknüpfung auflösen.

![Wo sieht man nach?](images/Translate-sidebar-instruction.png )



[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Wiki](Category:Wiki.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Localisation Sidebar/de
