# History/de
\_\_FORCETOC\_\_

## Geschichte

<img alt="Frühes FreeCAD, Version unbekannt" src=images/Screenshot_mesh.jpg  style="width:300px;"> <img alt="FreeCAD Version 0.7 von 2009" src=images/Part_BooleanOperations.png  style="width:300px;">

### Wie alles begann 

FreeCAD begann im Januar 2001, als [Jürgen Riegel](User_Jriegel.md) mit der Arbeit an dem Cas.CADE Projekt begann. Cas.CADE war ein kommerzielles Softwareentwicklungsrahmenwerk, das einen [geometrischen Modellierungskern](Glossary#Geometric_modeling_kernel.md) (oder CAD Kernel) enthielt: Es wurde im Jahr 2000 unter einer Open-Source Lizenz veröffentlicht und in [OpenCASCADE](OpenCASCADE/de.md) umbenannt. Dies ermöglichte die Realisierung eines quelloffenen 3D CAD Programms, da die Programmierung eines CAD Kerns von Grund auf einen enormen Arbeitsaufwand bedeutet hätte.

In Jürgens eigenen Worten:


{{Quote|text=''Ich begann mit dem FreeCAD-Projekt im Jahr 2001, als einem sogenannten GOM (grafischer Objektmodellierer), mit der Idee, Qt, Python und Cas.CADE zu verwenden, einem kommerziellen CAD-Kern, den ich zu der Zeit im Daimler-Projekt benutzte. Cas.CADE wurde kurz vorher Open-Source, so dass es die richtige Zeit schien, den zu der Zeit freien Raum eines Open-Source-CAD zu besetzen. Ich hatte zwei Jahre Erfahrung mit OpenCascade in einem Projekt namens QSpect, in dem ich zum Schluss der Haupt-Software-Designer war. Ich habe eine Menge über 3D und CAD-Programmierung gelernt. Ich war auch beeinflusst von Catia V5 und dessen sehr ungewöhnlichen Benutzer- und Programmieroberfläche. Am 17. März 2002 habe ich während des OpenCasCade-Projektes die Software als FreeCAD registriert. Mir fiel kein besserer Name ein, ich bin sehr schlecht bei Namen. Im April 2003 wechselte Werner Mayer, einer den Kollegen im QSpect-Projekt, zu einer Firma namens Imetric. Der Kontakt zu Imetric war vielversprechend, denn sie suchten nach einer 3D-Software-Plattform für ihre 3D-Sensoren. Imetric spendete im Jahr 2005 das Meiste des Mesh-Moduls an FreeCAD und die Open-Source-Community und verwendeten seitdem FreeCAD als Basis für ihre Sensorsystem-Software. Seit dieser Zeit ist Werner Mayer ein sehr aktiver FreeCAD-Entwickler. Nach einem Jahr Anstrengungen habe ich 2005 entschieden, das OpenCasCade-Dokument-Gerüst herauszutrennen und durch eine Eigenentwicklung zu ersetzen. Schlussendlich benutzen wir nur den CAD-Kern von OpenCasCade und nicht den Rest des Gerüstes. 2007 war ein weiterer interessanter Meilenstein. Wir wechselten zu Qt4 und dadurch zur LGPL. Zu der Zeit haben wir viel Arbeit geleistet, hauptsächlich Werner''.
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[http://forum.freecadweb.org/viewtopic.php?f=8&t=295 Wer steckt hinter FreeCad?]''}}

Das Projekt wurde der Öffentlichkeit 2003 im [OpenCascade Forum](https://dev.opencascade.org/forums) vorgestellt:


{{Quote|text=''Hallo zusammen, mein Name ist Jürgen Riegel und heute möchte ich ein OpenCasCade-Projekt ankündigen, FreeCAD. Es ist ein Open-Source CAx RAD, basierend auf OpenCasCade, Qt und Python. Es bietet einige wichtige Ideen wie Makroaufzeichnung, Arbeitsbereiche, die Möglichkeit als Server zu arbeiten und als eine dynamisch ladbare Anwendungserweiterung, und es soll plattformunabhängig sein. Obwohl es in einer frühen Phase und weder für Anwender noch für Entwickler benutzbar ist - die erste Benutzerausgabe ist für Ende 2003 geplant -, möchte ich gerne etwas Feedback über die Richtung und das Design von FreeCAD haben. Die Benutzeroberfläche ist fast fertig und wir, mein Co-Entwickler Werner Mayer und ich, haben damit angefangen, die ersten CAD-Funktionen hinzufügen. FreeCAD kann als ein Allzweck-CAD-System angesehen werden, aber die erste Zielgruppe, denke ich, werden CAx-Entwickler sein, die eine Grundlage für die eigene Entwicklung benötigen''.
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[https://dev.opencascade.org/content/announcing-freecad-project Ankündigung FreeCAD Projekt am Sun, 08/17/2003 - 19:23]''}}

### Werner Mayer 

Werner Mayer trat dem Projekt bei, sobald es als Open Source Projekt angekündigt wurde (vor der Ankündigung war das Projekt ein privates Projekt von Jürgen). Siehe diesen Forumsbeitrag von Werner auf Deutsch: <https://forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>

Mit der Zeit gewann das Projekt an Zugkraft und es kamen neue wichtige Mitwirkende in der Gemeinschaft hinzu.

-   **Linux Anfang**


{{Quote|text=''Eine lustige Tatsache ist, dass er eine Open-Source CAD Software hauptsächlich für Linux haben wollte, weil es zu dieser Zeit eigentlich nichts für diese Plattform gab. Von Anfang an entwickelten wir jedoch für die nächsten 1,5 Jahre ausschließlich unter Windows. Dann leistete ein Tscheche einen Beitrag, um den Code des Core Builds auf Linux zu bringen: https://github.com/berndhahnebach/All_FreeCAD/commit/9fd2e27c95ba3dc84778d92e2564cd094793ce2f#diff-480477e89f9b6ddafb30c4383dcdd705''}}


{{Quote|text=''Ein halbes Jahr später habe ich den Linux Build weitergeführt: https://github.com/berndhahnebach/All_FreeCAD/commit/35b962d7d751dd80f7c7781df60f93bc9a3da992''}}

**F:** Kannst du mitteilen, wie die ersten 1,5 Jahre verliefen? Habt ihr euch persönlich oder online getroffen?


{{Quote|text=''Nun, damals waren wir Kollegen (bis 2005), so dass wir Dinge von Angesicht zu Angesicht besprechen konnten. Danach hatten wir noch einige persönliche Treffen, aber die meisten Dinge haben wir per E-Mail oder Telefon besprochen.''}}


{{Quote|text=''Als dritter Kernentwickler kam Yorik Ende 2007 hinzu, aber es dauerte weitere 3 oder 4 Jahre, bis die Gemeinschaft und die Zahl der Mitwirkenden deutlich zu wachsen begannen.''}}

**F:** Habt ihr die Aufgaben aufgeteilt oder an konkurrierenden Implementierungen gearbeitet?


{{Quote|text=''Ja. Jürgen entwarf und implementierte den größten Teil der Anwendung und Dokumentenlogik, und ich kümmerte mich um die Grundlagen der Benutzeroberfläche.''}}


{{Quote|text=''Dies war jedoch kein allmählicher Prozess, sondern wir haben zu Beginn mit vielen Dingen experimentiert. In der ersten Version nutzten wir beispielsweise das OCC Dokumenten Rahmenwerk OCAF und seinen Betrachter, aber nach ein oder zwei Jahren gerieten wir in eine Sackgasse, weil die Dokumentation zu OCC sehr dürftig war und wir es nicht hinbekamen, OCAF um unsere eigenen Funktionstypen zu erweitern. Also beschlossen wir, nur die Modellierungskapazitäten von OCC zu nutzen, aber unser eigenes Anwendung/Dokumenten Rahmenwerk zu entwickeln.''}}

**F:** Hättest du damals gedacht, dass FreeCAD dort stehen würde, wo es heute ist?


{{Quote|text=''Wir wussten es nicht, aber wir hofften es. Natürlich konnten wir nicht vorhersehen, wie genau FreeCAD heute aussehen wird.<br>Die wichtigsten Gestaltungsentscheidungen waren, es auf allen wichtigen Plattformen verfügbar zu machen und die gesamte SW so zugänglich wie möglich zu gestalten, d.h. alle wichtigen Funktionen in Python zu implementieren, damit Hauptanwender FreeCAD mit eigenen Funktionen erweitern können. Auf diese Weise hofften wir, ein breites Publikum zu erreichen.''}}

(Siehe diesen Forumsbeitrag von Werner [Re: FreeCAD Geschichte](https://forum.freecadweb.org/viewtopic.php?f=8&t=47703#p411612))

### Yorik trat dem Projekt bei 

[Yorik van Havre](User_Yorik.md) trat dem Projekt 2008 bei und begann mit der Arbeit am [Entwurfsmodul](Draft_Workbench/de.md). Vor diesem Zeitpunkt gab es keine Möglichkeit, 2D Geometrie mit dem [GUI](Glossary/de#GUI.md) zu erstellen. Dieses Modul wurde vollständig in Python programmiert und nicht in C++, der in FreeCAD verwendeten Kernprogrammiersprache. Der neue Entwurf Arbeitsbereich bewies, dass die Python Integration ein Erfolg war und dazu genutzt werden konnte, die Fähigkeiten von FreeCAD zu erweitern oder anzupassen. Zusätzlich zu seiner Arbeit am Entwurfsmodul arbeitete Yorik an der Erweiterung der FreeCAD Dokumentation und wurde zum *de facto*\"Artdirektor\" von FreeCAD, der viele Symbole für die FreeCAD GUI und [ihren Stil definieren](Artwork/de.md) erstellte.

FreeCAD Version 0.7 wurde im April 2009 veröffentlicht und war die erste mit dem Draft-Modul. Das Part-Modul enthielt einen einfachen [CSG](Glossary/de#Constructive_Solid_Geometry.md)-Arbeitsablauf mit der Erstellung von primitiven Formen und Booleschen Operationen über das Part-Menu. Extrusion von 2D-Profiles und Verrundung was ebenfalls möglich.

Version 0.8 wurde im Juli 2009 veröffentlicht und enthielt weitere Arbeit am Draft-Modul, darunter ein neues Bemaßungswerkzeug. Das Part-Modul profitierte von einer neuen Werkzeugleiste zusammen mit neuen Werkzeugen, Drehen und Schnitt.

Gegen Ende 2009 wurde FreeCAD als Debian-Paket in den Debian-Repositories akzeptiert. FreeCAD wurde 2010 in den Ubuntu 10.04-Repositories hinzugefügt.

### Das Projekt geht weiter 

Version 0.10 wurde im Juli 2010 veröffentlicht und führte die [Arbeitsbereich Skizzierer](Sketcher_Workbench/de.md) ein, die auf Sketchsolve basiert, einem beschränkungsbasierten Löser zur Erstellung von 2D Geometrie. Die erste Version war begrenzt auf die Erstellung von Rechtecken und Linien.

Anfang 2011, die Gelegenheit nutzend, die die [Launchpad](https://launchpad.net) Online Plattform gibt, wurde das [FreeCAD Instandhalter Team](https://launchpad.net/~freecad-maintainers) ins Leben gerufen, um den Benutzern des Ubuntu Betriebssystems frische stabile Ausgaben zusammen mit täglichen Build Paketen von FreeCAD bereitzustellen.

Version 0.11 wurde im Mai 2011 veröffentlicht und führte den Part Design Arbeitsbereich ein, der Werkzeuge wie Tasche, Verrundung und Fase umfasste. Der Draft Arbeitsbereich erhielt Verbesserungen und neue Werkzeuge, wie BSpline. Der Roboter Arbeitsbereich bekam weitere GUI Werkzeuge.

Version 0.12 wurde im Januar 2012 veröffentlicht und enthielt einen vollständigeren Skizzierer Arbeitsbereich. Sie enthielt einen völlig neu geschriebenen Löser, FreeGCS. Es war das Ergebnis monatelanger Arbeit der FreeCAD Hauptentwickler zusammen mit den Neueinsteigern logari81 (der den Löser programmiert hat) und mrlukeparry. Weitere Werkzeuge wurden dem PartDesign PartDesign-Arbeitsbereich hinzugefügt.

### Vergrößerung des Kern Entwickler Teams 

Im April 2019 wurde das Team der Kernentwickler erweitert: Zu Jürgen, Werner und Yorik gesellten sich Abdullah, Bernd, sliptonic und WandererFan

## Interessante Beiträge im Forum 

-   über PartDesignNext und andere Gestaltungsentscheidungen: <https://forum.freecadweb.org/viewtopic.php?f=8&t=34923&start=130#p297074>
-   über die Geschichte des Forums: <https://forum.freecadweb.org/viewtopic.php?f=8&t=7448&start=200#p287106>
-   über die Projektgeschichte: <https://forum.freecadweb.org/viewtopic.php?f=8&t=47703>
-   über die Code Historie: <https://forum.freecadweb.org/viewtopic.php?f=10&t=46733&start=10#p405068> BTW: der erste Code-Checkin war am 18. März 2002 (vielleicht ist das der Geburtstag?)
-   über das Projekt, das OpenSource werden soll: <https://forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>
-   über die Historie der Veröffentlichungs Commits: <https://forum.freecadweb.org/viewtopic.php?f=8&t=23695#p184940>
-   über Wer steckt hinter FreeCAD: <http://forum.freecadweb.org/viewtopic.php?f=8&t=295>
-   über die FEM Geschichte: <https://forum.freecadweb.org/viewtopic.php?f=18&t=48646#p416389>
-   über die Geschichte der FEM Polygonnetzbildner: <https://forum.freecadweb.org/viewtopic.php?f=18&t=48733#p417627>

## Veröffentlichungshistorie

#### Überblick

  Version   Veröffentlichungsname   Veröffentlichungsdatum   Veröffentlichungsverpflichtung                              Veröffentlichungszweig
      
  1.0       \-                      in Entwicklung           [Versionshinweise 1.0](Release_notes_1.0/de.md)     [head master](https://github.com/FreeCAD/FreeCAD/commits/master)
  0.20      \-                      2022-06-14               [Versionshinweise 0.20](Release_notes_0.20/de.md)   [release commit 0.20](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-20)
  0.19      \-                      2021-03-20               [Versionshinweise 0.19](Release_notes_0.19/de.md)   [release commit 0.19](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-19)
  0.18      \-                      2019-03-12               [Versionshinweise 0.18](Release_notes_0.18/de.md)   [release commit 0.18](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-18)
  0.17      Roland                  2018-04-06               [Versionshinweise 0.17](Release_notes_0.17/de.md)   [release commit 0.17](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-17)
  0.16      \-                      2016-04-18               [Versionshinweise 0.16](Release_notes_0.16/de.md)   [release commit 0.16](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-16)
  0.15      \-                      2015-04-08               [Versionshinweise 0.15](Release_notes_0.15/de.md)   [release commit 0.15](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-15)
  0.14      \-                      2014-07-01               [Versionshinweise 0.14](Release_notes_0.14/de.md)   [release commit 0.14](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-14)
  0.13      \-                      2013-01-29               [Versionshinweise 0.13](Release_notes_0.13/de.md)   [release commit 0.13](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-13)
  0.12      \-                      2011-12-20               [Versionshinweise 0.12](Release_notes_0.12.md)      
  0.11      \-                      2011-05-03               [Versionshinweise 0.11](Release_notes_0.11/de.md)   
  0.10      \-                      2010-07-24                                                                           
  0.9       \-                      2010-01-16                                                                           
  0.8       \-                      2009-07-10                                                                           
  0.7       \-                      2009-04-24                                                                           
  0.6       \-                      2007-02-27                                                                           
  0.5       \-                      2006-10-05                                                                           
  0.4       \-                      2006-01-15                                                                           
  0.3       \-                      2005-10-31                                                                           
  0.2       \-                      2005-08-09                                                                           
  0.1       \-                      2003-01-27                                                                           
  0.0.1     \-                      2002-10-29               Initial Upload of a version                                 

#### Legende

  Farbe   Versionstyp
   
          Zukünftige Veröffentlichung
          Letzte Vorschauversion
          **Letzte Version**
          Ältere Version, noch unterstützt
          Alte Version
          

## Externe Verweise 

-   [SourceForge Bereich Dateien](http://sourceforge.net/projects/free-cad/files/)
-   [SourceForge Bereich Alte Dateien](http://sourceforge.net/projects/free-cad/files/OldFiles/)
-   [Ankündigung des FreeCAD Projekts](http://www.opencascade.org/org/forum/thread_6572/?forum=11) im OpenCascade Forum



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > History/de
