 \_\_FORCETOC\_\_


<div class="mw-translate-fuzzy">

## Geschichte

<img alt="Frühes FreeCAD, Version unbekannt" src=images/Screenshot_mesh.jpg  style="width:300px;"> <img alt="FreeCAD Version 0.7 von 2009" src=images/Part_BooleanOperations.png  style="width:300px;">


</div>


<div class="mw-translate-fuzzy">

### Wie alles begann {#wie_alles_begann}

Die Geschichte von FreeCAD startete im Januar 2001, als [Jürgen Riegel](User:Jriegel.md) begann, am Cas.CADE-Projekt mitzuarbeiten, einem kommerziellen Software-Entwicklungsgerüst mit einem [geometrischen Modellierungskern](Glossary#Geometric_modeling_kernel.md) (oder CAD-Kern), das im Jahr 2000 unter einer Open-Source-Lizenz veröffentlicht und in [Open Cascade](Glossary#Open_CASCADE.md) umbenannt wurde. Dies machte die Realisierung eines Open-Source-3D-CAD-Programms möglich, denn einen CAD-Kern von Grund auf zu erstellen, hätte eine Riesenmenge an Arbeit bedeutet.


</div>

In Jürgens eigenen Worten:


{{Quote|text=''Ich begann mit dem FreeCAD-Projekt im Jahr 2001, als einem sogenannten GOM (grafischer Objektmodellierer), mit der Idee, Qt, Python und Cas.CADE zu verwenden, einem kommerziellen CAD-Kern, den ich zu der Zeit im Daimler-Projekt benutzte. Cas.CADE wurde kurz vorher Open-Source, so dass es die richtige Zeit schien, den zu der Zeit freien Raum eines Open-Source-CAD zu besetzen. Ich hatte zwei Jahre Erfahrung mit OpenCascade in einem Projekt namens QSpect, in dem ich zum Schluss der Haupt-Software-Designer war. Ich habe eine Menge über 3D und CAD-Programmierung gelernt. Ich war auch beeinflusst von Catia V5 und dessen sehr ungewöhnlichen Benutzer- und Programmieroberfläche. Am 17. März 2002 habe ich während des OpenCasCade-Projektes die Software als FreeCAD registriert. Mir fiel kein besserer Name ein, ich bin sehr schlecht bei Namen. Im April 2003 wechselte Werner Mayer, einer den Kollegen im QSpect-Projekt, zu einer Firma namens Imetric. Der Kontakt zu Imetric war vielversprechend, denn sie suchten nach einer 3D-Software-Plattform für ihre 3D-Sensoren. Imetric spendete im Jahr 2005 das Meiste des Mesh-Moduls an FreeCAD und die Open-Source-Community und verwendeten seitdem FreeCAD als Basis für ihre Sensorsystem-Software. Seit dieser Zeit ist Werner Mayer ein sehr aktiver FreeCAD-Entwickler. Nach einem Jahr Anstrengungen habe ich 2005 entschieden, das OpenCasCade-Dokument-Gerüst herauszutrennen und durch eine Eigenentwicklung zu ersetzen. Schlussendlich benutzen wir nur den CAD-Kern von OpenCasCade und nicht den Rest des Gerüstes. 2007 war ein weiterer interessanter Meilenstein. Wir wechselten zu Qt4 und dadurch zur LGPL. Zu der Zeit haben wir viel Arbeit geleistet, hauptsächlich Werner''.
|sign=[Jürgen Riegel](User:Jriegel.md)|source=''[http://forum.freecadweb.org/viewtopic.php?f=8&t=295 Wer steckt hinter FreeCad?]''}}


<div class="mw-translate-fuzzy">

Das Projekt wurde der Öffentlichkeit 2003 im [OpenCascade Forum](http://www.opencascade.org/org/forum) vorgestellt. Wieder in Jürgens Worten:


</div>


<div class="mw-translate-fuzzy">


{{Quote|text=''Hallo zusammen, mein Name ist Jürgen Riegel und heute möchte ich ein OpenCasCade-Projekt ankündigen, FreeCAD. Es ist ein Open-Source CAx RAD, basierend auf OpenCasCade, Qt und Python. Es bietet einige wichtige Ideen wie Makroaufzeichnung, Arbeitsbereiche, die Möglichkeit als Server zu arbeiten und als eine dynamisch ladbare Anwendungserweiterung, und es soll plattformunabhängig sein. Obwohl es in einer frühen Phase und weder für Anwender noch für Entwickler benutzbar ist - die erste Benutzerausgabe ist für Ende 2003 geplant -, möchte ich gerne etwas Feedback über die Richtung und das Design von FreeCAD haben. Die Benutzeroberfläche ist fast fertig und wir, mein Co-Entwickler Werner Mayer und ich, haben damit angefangen, die ersten CAD-Funktionen hinzufügen. FreeCAD kann als ein Allzweck-CAD-System angesehen werden, aber die erste Zielgruppe, denke ich, werden CAx-Entwickler sein, die eine Grundlage für die eigene Entwicklung benötigen''.
|sign=[Jürgen Riegel](User:Jriegel.md)|source=''[http://www.opencascade.org/org/forum/thread_6572/?forum=11 Announcing FreeCAD Project]''}}


</div>


<div class="mw-translate-fuzzy">

### Werner Mayer {#werner_mayer}

Nach seinen eigenen Worten ist er vom ersten Tag an im Projekt, an dem das Projekt angekündigt wurde und betriebsunterstützend. Vor diesem Tag war das Projekt ein privates Projekt (Spielwiese?) von Jürgen. Siehe Forenbeitrag von Werner auf Deutsch: <https://forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>


</div>


<div class="mw-translate-fuzzy">

Schließlich nahm das Projekt Fahrt auf und neue Schlüsselentwickler kamen in der Gemeinschaft hinzu.


</div>

-   **Linux beginning**


{{Quote|text=''A fun fact is that he wanted to have an open-source CAD software mainly for Linux because at that time there existed actually nothing for this platform. However, from the beginning on we exclusively developed on Windows for the next 1.5 years. Then a Czech guy made a contribution to make the code of the core build on Linux: https://github.com/berndhahnebach/All_FreeCAD/commit/9fd2e27c95ba3dc84778d92e2564cd094793ce2f#diff-480477e89f9b6ddafb30c4383dcdd705''}}


{{Quote|text=''Half a year later I continued the Linux build: https://github.com/berndhahnebach/All_FreeCAD/commit/35b962d7d751dd80f7c7781df60f93bc9a3da992''}}

**Q:** Could you share how that first 1.5 years went? Were you meeting in person or online?


{{Quote|text=''Well, at that time we were colleagues (until 2005) so we could discuss things face to face. After that time we still had some personal meetings but discussed most things by email or phone.''}}


{{Quote|text=''As third core developer Yorik joined around end of 2007 but it took another 3 or 4 years until the community and number of contributors started to grow significantly.''}}

**Q:** Did you divide the tasks or work on competing implementations?


{{Quote|text=''Yes. Jürgen was designing and implementing most of the application and document logic and I was doing the basics of the GUI.''}}


{{Quote|text=''However, this wasn't a gradual process but we have experimented with many things at the beginning. For example, in the initial version we used OCC's document framework OCAF and its viewer but after a year or two we got into a dead end because documentation about OCC was very poor and we couldn't get it to work to extend OCAF with our own feature types. So, we decided to only use OCC's modeling capacities but develop our own application/document framework.''}}

**Q:** At the time did you think FreeCAD would be where it is today?


{{Quote|text=''We didn't know but we hoped. Of course we couldn't anticipate how exactly FreeCAD will look today.<br>The most important design decisions were to make it available on all major platforms and make the whole SW as accessible as possible, i.e. to impose all important functions to Python so that (power) users are able to extend FreeCAD with own functions. This way we hoped to get a broad audience.''}}

(See this forum post from Werner [Re: FreeCAD History](https://forum.freecadweb.org/viewtopic.php?f=8&t=47703#p411612))


<div class="mw-translate-fuzzy">

### Yorik trat dem Projekt bei {#yorik_trat_dem_projekt_bei}

[Yorik van Havre](User:Yorik.md) trat dem Projekt 2008 bei und begann mit der Arbeit am [Entwurfsmodul](Draft_Module/de.md). Vor diesem Zeitpunkt gab es keine Möglichkeit, 2D-Geometrie mit dem [GUI](Glossary/de#GUI.md) zu erstellen. Dieses Modul wurde vollständig in Python programmiert und nicht in C++, der in FreeCAD verwendeten Kernprogrammiersprache. Dies bewies, dass die Python Integration ein Erfolg war und dazu genutzt werden konnte, die Fähigkeiten von FreeCAD zu erweitern oder anzupassen. Zusätzlich zu seiner Arbeit am Entwurfsmodul arbeitete Yorik an der Erweiterung der FreeCAD Dokumentation und wurde zum *de facto*\"Art Director\" von FreeCAD, der viele Symbole für die FreeCAD GUI und [Stildefinition](Artwork/de.md) erstellte.


</div>

FreeCAD Version 0.7 wurde im April 2009 veröffentlicht und war die erste mit dem Draft-Modul. Das Part-Modul enthielt einen einfachen [CSG](Glossary/de#Constructive_Solid_Geometry.md)-Arbeitsablauf mit der Erstellung von primitiven Formen und Booleschen Operationen über das Part-Menu. Extrusion von 2D-Profiles und Verrundung was ebenfalls möglich.

Version 0.8 wurde im Juli 2009 veröffentlicht und enthielt weitere Arbeit am Draft-Modul, darunter ein neues Bemaßungswerkzeug. Das Part-Modul profitierte von einer neuen Werkzeugleiste zusammen mit neuen Werkzeugen, Drehen und Schnitt.

Gegen Ende 2009 wurde FreeCAD als Debian-Paket in den Debian-Repositories akzeptiert. FreeCAD wurde 2010 in den Ubuntu 10.04-Repositories hinzugefügt.


<div class="mw-translate-fuzzy">

### Das Projekt geht weiter {#das_projekt_geht_weiter}

Die im Juli 2010 veröffentlichte Version 0.10 führte die [Arbeitsbereich Skizze](Sketcher_Workbench/de.md) ein, die auf Sketchsolve basiert, einem beschränkungsbasierten Löser zur Erstellung von 2D-Geometrien. Die erste Version war beschränkt auf die Erstellung von Rechtecken und Linien.


</div>

Das Angebot der [Launchpad](https://launchpad.net) Online-Plattform nutzend, wurde Anfang des Jahres 2011 das [FreeCAD Maintainers Team](https://launchpad.net/~freecad-maintainers) gegründet, um Nutzern des Ubuntu-Betriebssystems frische stabile Ausgaben zusammen mit täglichen Build-Paketen von FreeCAD zu bieten.


<div class="mw-translate-fuzzy">

Die im Mai 2011 veröffentlichte Version 0.11 führte den Part Design-Arbeitsbereich ein, der u.a. die Werkzeuge Block, Tasche, Verrundung und Fase umfasste. Der Draft-Arbeitsbereich erhielt Erweiterungen und neue Werkzeuge wie BSpline. Der Robot-Arbeitsbereich bekam weitere GUI-Werkzeuge.


</div>


<div class="mw-translate-fuzzy">

Die im Januar 2012 veröffentlichte Version 0.12 bot einen kompletteren Sketcher-Arbeitsbereich. Er enthielt einen komplett überarbeiteten Solver, FreeGCS. Das war das Ergebnis monatelanger Arbeit der Hauptentwickler zusammen mit den Neueinsteigern logari81 (der den Solver programmierte) und mrlukeparry. Der PartDesign-Arbeitsbereich wurde um weitere Werkzeuge erweitert.


</div>


<div class="mw-translate-fuzzy">

### Vergrößerung des Kern-Entwickler-Teams {#vergrößerung_des_kern_entwickler_teams}

Das Team der Kern-Entwickler wird von den drei alten Hasen Jürgen, Werner und Yorik am 3. April 2019 um Abdullah, Bernd, sliptonic und WandererFan erweitert (siehe [coredeveloper](https://github.com/orgs/FreeCAD/teams/core-developers/members)).


</div>


<div class="mw-translate-fuzzy">

## Interessante Beiträge im Forum {#interessante_beiträge_im_forum}

=

-   zu PartDesignNext und anderen Design-Entscheidungen: <https://forum.freecadweb.org/viewtopic.php?f=8&t=34923&start=130#p297074>
-   zur Forum-Geschichte: <https://forum.freecadweb.org/viewtopic.php?f=8&t=7448&start=200#p287106>


</div>

## Veröffentlichungshistorie


<div class="mw-translate-fuzzy">

#### Überblick

  Version   Veröffentlichungsname   Veröffentlichungsdatum   Versionshinweise                                            Quellcode
  --------- ----------------------- ------------------------ ----------------------------------------------------------- -------------------------------------------------------------------------------
  0.19      ?                       in Entwicklung           [Versionshinweise 0.19](Release_notes_0.19/de.md)   [head master](https://github.com/FreeCAD/FreeCAD/commits/master)
  0.18      \-                      2019-03-12               [Versionshinweise 0.18](Release_notes_0.18/de.md)   [head 0.18](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-18)
  0.17      Roland                  2018-04-06               [Versionshinweise 0.17](Release_notes_0.17/de.md)   [head 0.17](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-17)
  0.16      \-                      2016-04-18               [Versionshinweise 0.16](Release_notes_0.16/de.md)   [head 0.16](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-16)
  0.15      \-                      2015-04-08               [Versionshinweise 0.15](Release_notes_0.15/de.md)   [head 0.15](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-15)
  0.14      \-                      2014-07-01               [Versionshinweise 0.14](Release_notes_0.14.md)      [head 0.14](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-14)
  0.13      \-                      2013-01-29               [Versionshinweise 0.13](Release_notes_013.md)       [head 0.13](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-13)
  0.12      \-                      2011-12-20               [Versionshinweise 0.12](Release_notes_012.md)       
  0.11      \-                      2011-05-03               [Versionshinweise 0.11](Release_notes_011.md)       
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
  0.0.1     \-                      2002-10-29               Erstes Hochladen \--\> Die Geburt von FreeCAD               
                                                                                                                         


</div>

#### Legende

  Farbe   Versionstyp
  ------- ---------------------------------
          Zukünftige Veröffentlichung
          Letzte Vorschauversion
          **Letzte Version**
          Älter Version, noch unterstützt
          Alte Version
          


<div class="mw-translate-fuzzy">

## Verweise

-   [GitHub-Repositories](https://github.com/freecad)
-   [SourceForge Files section](http://sourceforge.net/projects/free-cad/files/)
-   [SourceForge Old Files section](http://sourceforge.net/projects/free-cad/files/OldFiles/)
-   [Who is behind FreeCad?](http://forum.freecadweb.org/viewtopic.php?f=8&t=295) topic on the FreeCAD forum
-   [Announcing FreeCAD Project](http://www.opencascade.org/org/forum/thread_6572/?forum=11) on the OpenCascade forum


</div>



[Category:News{{\#translation:}}](Category:News.md)
