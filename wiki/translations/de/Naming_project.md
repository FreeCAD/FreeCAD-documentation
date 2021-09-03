


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

Diese Vorlage ist der Leitfaden für ein FreeCAD Entwicklungsprojekt. Sie folgt den Regeln des [Getting Things Done (GTD)](http://de.wikipedia.org/wiki/Getting_Things_Done#Methodology) Prozesses. Die Projekte sind im [Entwicklungsfahrplan](Development_roadmap/de.md) zusammengefasst.

## Zweck und Prinzipien 

Dies ist ein Entwicklungs- und Gestaltungsversuch zur Umsetzungung einer robusten topologischen Benennung in FreeCAD.

Weitere Einzelheiten zur topologischen Benennung in **[Topologisches Benennungsproblem](Topological_naming_problem/de.md)**.

## Ergebnis

1.  **Schnittstelle** in (Part::TopoShape), um (Namens)formen und Unterformen (Flächen, Kanten, Knoten) durch eine Zeichenfolge (Unterelementname wie \"Fläche1\") robust zu referenzieren
    Hier benötigen wir eine Schnittstelle, um Part::TopoShape mit allen Informationen zu versorgen, die für die Benennung benötigt werden, z.B. NewShape, zusätzliche Informationen aus einem Algos wie gelöschte Flächen, Modellierungsschritt (für 2.) und \...
2.  **Verband** von Modellierungsschritten mit den resultierenden Flächen/Kanten.
    Im Falle eines großen Modells ist der Anwender verloren, wenn er hunderte von Verrundungen oder Bohrungen hat. Wenn die Flächen/Kanten also wüssten, welcher Modellierungsschritt erzeugt wurde, könnten wir einen Doppelklick auf Kante/Fläche implementieren, der das richtige Funktionsmerkmal öffnet!
3.  Ein **Algorithmus**, um die Benennung während Änderungen in der Modellierungshistorie hinweg stabil zu halten, wie das Aufteilen von Kanten/Flächen und das Verschieben von Knoten
    ![](images/NamingExample.jpg )
4.  (optional) **speicheroptimierte Datenstruktur**, um nur geänderte Flächen/Kanten in jeder Modellierungsfunktion zu behalten.
    Dies wird wichtig, wenn die Modelle größer werden. Es ist nicht effizient, den größten Teil der Form einfach durchzukopieren. Es wäre viel effektiver, die unveränderten Flächen/Kanten zwischen den Merkmalen zu teilen und nur das zu kopieren, was sich geändert hat.

## Ideenfindung

Vieles wurde diskutiert in der [\"Robust References\" Veröffentlichung](http://forum.freecadweb.org/viewtopic.php?f=10&t=2656) von jrheinlaender.

### Weitere

-   [Catia V5 Topology and Generic Naming](http://www.maruf.ca/files/caadoc/CAATopTechArticles/JournalMethodology.htm#Definition) and [Catia V5 Objectives of Generic Naming](http://www.maruf.ca/files/caadoc/CAAMmrTechArticles/CAAMmrGenericNaming.htm#Objectives%20of%20GN)
-   [Topological naming in OCAF (Open CASCADE Application Framework)](https://www.opencascade.com/doc/occt-7.4.0/overview/html/occt_user_guides__ocaf.html#occt_ocaf_5_6)

### Literatur & Aufsätze 

-   J Kripac, \"A mechanism for persistently naming topological entities in history-based parametric solid modelsSymposion über Festkörpermodellierung und Anwendungen 1995, S.21-30\"

:   Beschreibt eine Methode, um die ersten drei Punkte in der Liste zu erledigen. Würde sagen, das ist der Ansatz, der von Catia und OCC-TNaming verwendet wird. Zumindest sieht das Interface gleich aus. Das Papier war nirgendwo herunterzuladen. Ich musste es kaufen. Wenn jemand interessiert ist, kann ich es per E-Mail schicken.

-   [Dago AGBODAN, David MARCHEIX and Guy PIERRA, \"PERSISTENT NAMING FOR PARAMETRIC MODELS, 2000\"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.29.2836&rep=rep1&type=pdf)

:   Interessanter Ansatz über Shell Graphen, geht den vierten Punkt der Liste an, indem er nicht veränderte Flächen/Kanten wiederverwendet.

-   [Duhwan Mun and Soonhung Han, \"Identification of Topological Entities and Naming Mapping for Parametric CAD Model Exchanges, INTERNATIONAL JOURNAL OF CAD/CAM, 2005, p 69-82\"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.3087&rep=rep1&type=pdf)

:   Sehr gute Übersicht und Beispiele

-   [Farjana, S.H., Han, S. \"Mechanisms of Persistent Identification of Topological Entities in CAD Systems: A Review\", Alexandria Engineering Journal, Volume 57, Issue 4, December 2018, Pages 2837-2849](https://research-management.mq.edu.au/ws/portalfiles/portal/100931773/Publisher_version_open_access_.pdf)

-   [Assembly Solving for Neutral Re-Imported Product Models Tahir A. Jauhar, Soonhung Han, Soonjo Kwon , p.108-123 , CAD Journal 2020, Volume 17 Number 1](http://www.cad-journal.net/files/vol_17/CAD_17(1)_2020_108-123.pdf)

### Zusammenfassung der bisherigen Arbeit 

Mit Stand 13. Juni 2016 ist hier eine Zusammenfassung der Arbeiten, die für dieses Projekt geleistet wurden:

-   jrheinlaender produzierte 2012 eine Menge Code, der sich stark auf den Skizzierer Arbeitsbereich verlässt, um \"Robuste Referenzen\" aufzulösen.
-   Ickby hatte einen Versuch unternommen, einige oder jrheinländische Codes in die moderne Freecad zu integrieren. [Dieser Beitrag](http://forum.freecadweb.org/viewtopic.php?f=10&t=2656&start=60#p124844) hat einen Link zu seinem Github-Repo.
-   Im Jahr 2016 hat Ezzieyguywuf jrheinlaenders Thread wiederbelebt und anschließend seinen eigenen gestartet. Ihr könnt ihn [hier](http://forum.freecadweb.org/viewtopic.php?f=10&t=15847) sehen.
-   ezzieyguywuf hat ein \"leichtes\" Open Cascade Programm entwickelt, um das Problem der topologischen Benennung zu duplizieren und mögliche Lösungen zu testen. Siehe sein github-Repo [freecadTopoTesting hier](https://github.com/ezzieyguywuf/freecadTopoTesting)
-   ezzieyguywuf hat das opencascade TNaming Werkzeugsatz in seinen Testcode integriert und gezeigt, wie dies helfen könnte, einige der Topologischen Benennungsprobleme zu lösen. Siehe das github Repo
-   [Topological Naming](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming) github Repositorium von realthunder
-   [Topological Naming Algorithm](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming-Algorithm) github Repositorium von realthunder

## Organisieren

### Information über TNaming 

Siehe [hier](https://github.com/ezzieyguywuf/freecadTopoTesting/blob/master/TNaming_Writeup.md) für einen anständigen Bericht über ezzieyguywufs github Repo. Hier sind einige Höhepunkte:

-   opencascade\'s TNaming basiert auf dem [TDF\_Data Datenframework](https://dev.opencascade.org/doc/occt-7.5.0/refman/html/class_t_d_f___reference.html#details).
-   TDF\_Data ist eine Schlüsselkomponente der opencascade OCAF-Sache, kann aber unabhängig davon verwendet werden
-   TDF\_Data ist im Wesentlichen ein Baum, in dem Daten hinzugefügt und dann zu einem späteren Zeitpunkt gelesen werden
-   Immer wenn ein TNaming\_NamedShape-Attribut zu einem Knoten im TDF\_Data-Baum hinzugefügt wird, wird ein TNaming\_UsedShapes-Attribut zur Wurzel des Baumes hinzugefügt.
    -   **\'HINWEIS:** dieses TNaming\_UsedShapes Attribut ist entscheidend für den Nutzen des TNaming Toolkits. Es enthält eine Historie aller TopoDS\_Shape, die während der \'Historie\' des Teils verwendet wurden.
-   TNaming\_Builder wird verwendet, um Informationen zum TDF\_Data-Baum hinzuzufügen. Es fügt ein TNaming\_NamedShape zu einem gegebenen Knoten im Baum hinzu und aktualisiert die TNaming\_UsedShapes-Datenbank, wenn nötig.
-   Jedes Mal, wenn das TopoDS\_Shape geändert wird, muss es in der TDF\_Data-Struktur protokolliert werden.
    -   Auch hier wird TNaming\_Builder verwendet.
    -   Siehe [hier](http://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__ocaf.html#occt_ocaf_5_6_1) in der opencascade-Dokumentation für eine Tabelle, die auflistet, was in der Datenbank gespeichert werden muss. **HINWEIS:** diese Tabelle scheint unvollständig zu sein. Einige zusätzliche Tests können notwendig sein
    -   Kurz gesagt, jedes Mal, wenn der TopoDS\_Shape geändert wird, müssen alle geänderten/erzeugten/gelöschten Features protokolliert werden. Da wir es mit Solids zu tun haben, bedeutet dies, dass wir die modifizierten/generierten/gelöschten Faces auf dem Solid protokollieren müssen.
-   Die TNaming\_Selector Klasse wird verwendet, um ein Feature \"auszuwählen\", das im TDF\_Data Baum verfolgt wird.
    -   ein \"ausgewähltes\" Feature ist eines, auf das der TNaming-Algorithmus von opencascade unabhängig von topologischen Änderungen einen konstanten Bezug auf

## Nächste Aktionen 

-   Festlegung des Umfangs
-   Python Testfälle
-   Schnittstelle im Teil::TopoShape (+ Pythonbindung)

### Nächste Schritte (ab 13. Juni 2016) 

1.  Ermittle, ob der opencascade TNaming Werkzeugsatz das Problem der topologischen Benennung in FreeCAD vollständig löst
    -   Was sind alle Belegstellen wo Topologische Benennung ein Problem ist?
    -   Was sind komplexe Szenarien, in denen dieser Ansatz funktionieren muss?
2.  TNaming Code in FreeCAD einbinden
    1.  Beginne mit einem Bare-Bones Ansatz, d.h. Mache einen Würfel und einen Zylinder, verschmelze Sie, verrunde ihn und passe dann die Größe des Zylinders an. Die Verrundung sollte sich nicht bewegen
    2.  Allmählich mehr Funktionalität hinzufügen
3.  Bestimme , ob TNaming langfristig die Lösung sein wird
4.  Unabhängig davon, ob TNaming die langfristige Lösung ist oder nicht, finde einen Weg, die Daten, die TNaming für die Beständigkeit über Sitzungen hinweg verwendet, zu \'serialisieren/deserialisieren\'.




[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
