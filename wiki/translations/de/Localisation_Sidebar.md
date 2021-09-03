 [Lokalisierung](Localisation/de.md) ist allgemein der Vorgang Software mit einer Benutzeroberfläche mit mehreren Sprachen zu versehen. Das Dokumentations-Wiki kann auch lokalisiert werden, wie im Abschnitt [Übersetze das FreeCAD-Wiki](Localisation#Translate_the_FreeCAD_wiki/de.md) beschrieben.

Die Seitenleiste (sidebar) ist ein wichtiges Navigationswerkzeug, das [hier](https://www.mediawiki.org/wiki/Manual:Interface/Sidebar/de) dokumentiert ist.

## Die Navigationsleiste übersetzen {#die_navigationsleiste_übersetzen}

Die Navigationsleiste ist nun vollständig übersetzbar mit der [Softwareerweiterung zur Übersetzung](http://www.mediawiki.org/wiki/Help:Extension:Translate) die für alle Wikiseiten verfügbar ist.

Im FreeCAD-Wiki besteht die Seitenleiste aus Vorlagen (templates), die den Text abhängig von der ausgewählten Sprache ändern. Technische Details, wie dieses Merkmal implementiert wurde, sind in diesem [Forums-Post](http://forum.freecadweb.org/viewtopic.php?f=21&t=9687&start=10#p80441) beschrieben.

### Beschreibungen

Um die Übersetzung zu beginnen, ist die Seite [Special:Translate/wiki-sidebar](Special:Translate/wiki-sidebar.md) zu öffnen.

Es gibt einen Fehler auf der Seite Herunterladen (download). Die Verknüpfung kann nicht zu \"Download/de\" (/fr, /es, \...) geändert werden. Stattdessen, zeigt die Verknüpfung auf die aktuelle Übersetzung von \"Herunterladen\" in Ihrer Sprache. Am Besten ist es dann eine neue Seite zu erstellen und darin die Verknüpfung richtig einzutragen. Mehr über die Umleitung der Verknüpfung, siehe[Help:Editing/de](Help:Editing/de.md).

### Wichtige Anmerkungen {#wichtige_anmerkungen}

Meistens gibt es zwei Texte für jeden Punkt im Menü.

** {{int:sidebar-faq-target}}|sidebar-faq

Der linke repäsentiert das Ziel des Verweises und der rechte den Text, der in der Seitenleiste angezeigt wird.

Man erkennt den Unterschied der beiden oben in der \'Übersetzungsbox\', in der der Name der Variablen steht. Wenn der Variablenname mit \"-target\" endet, bedeutet das, dass der Zeiger der Verknüpfung übersetzt wird. Das dient dazu, dass der Übersetzer die Verknüpfung auf die übersetzte Seite lenken kann, z.B. durch hinzufügen von \"/de\" hinter dem Namen der Seite für die deutsche Übersetzung.

NICHT \"/de\" (/fr, /es, \...) mit einfügen, wenn die Übersetzungseite in der Übersetzungsprache nicht existiert. Das wird die Verknüpfung auflösen. NICHTS weiteres eintragen, als den Namen der Seite. Das wird die Verknüpfung auflösen.

![Wo sieht man nach?](images/Translate-sidebar-instruction.png )



[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Wiki{{\#translation:}}](Category:Wiki.md)
