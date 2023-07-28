# Frequently asked questions/de
Diese Seite versucht, die häufigsten Fragen zu beantworten, die in den FreeCAD Foren gestellt werden. Wenn Du ein Problem oder eine Frage zu FreeCAD hast, schau zuerst unten nach. Wenn Du dann keine Antwort auf deine spezielle Frage findest, gehe zum [FreeCAD Forum](http://forum.freecadweb.org/viewforum.php?f=3)!



## Einrichtung



### Was ist der einfachste Weg, FreeCAD auf meinem Rechner zu installieren ? 

Wenn du unter Windows oder macOS arbeitest, ist der einfachste Weg zum [Herunterladen](Download/de.md), auf die Seite zu gehen, wo du mehrere installationsbereite Pakete findest. Wenn du auf Debian, Fedora oder Ubuntu und einigen anderen Distributionen bist, ist FreeCAD bereits in den Standard-Software-Repositorien enthalten und du kannst es einfach mit dem Software-Manager installieren. Unter Ubuntu unterhält das FreeCAD-Team auch eigene [PPA-Repositorien](Installing_on_Linux/de#Stable_PPA.md). Weitere Details zur Installation findest du auf der Installationsseite für dein Betriebssystem ([Windows](Installing_on_Windows/de.md), [Linux](Installing_on_Linux/de.md) oder [macOS](Installing_on_Mac/de.md)).



### Was sind die Voraussetzungen um FreeCAD auszuführen 

Im Gegensatz zu den meisten 3D CAD Programmen kann FreeCAD problemlos auf den einfachsten Computern laufen - es ist bekannt, dass es auf Pentium IV und Intel Core2 Solo CPUs läuft. Wenn auf deinem Computer ein aktuelles Betriebssystem läuft, stehen die Chancen gut, dass FreeCAD läuft. Die einzige Voraussetzung ist, dass deine Grafikkarte oder dein Chipsatz [OpenGL](https://en.wikipedia.org/wiki/OpenGL) unterstützen muss, vorzugsweise nicht älter als v2.0. Bei Problemen lies bitte den Abschnitt [Fehlerbehebung](Frequently_asked_questions/de#Fehlerbehebung.md) dieser FAQ.

#### Multithreading

FreeCADs zugrunde liegender geometrischer Modellierungskern, die [OpenCASCADE Technologie](http://en.wikipedia.org/wiki/Open_Cascade_Technology) (OCCT) Drittanbieterbibliothek, [hat derzeit nur teilweise Multi-Threading Unterstützung](https://forum.freecadweb.org/viewtopic.php?f=4&t=17501&p=173095&hilit=Multithread#p173095). Siehe die [multithreading](multithreading/de.md) Seite für weitere Einzelheiten.



#### Für Mac Nutzer 

Es wird nur die MacIntel Architektur unterstützt. Für die PowerPC Architektur sind keine Builds verfügbar.



### Was, wenn ich FreeCAD selbst kompilieren möchte? 

Der Quellcode von FreeCAD ist immer im Projekt-Quellcode-Repositorium verfügbar. Wenn du FreeCAD selbst kompilierst, kannst du die neuesten Funktionen verwenden, die gerade entwickelt werden, erfordert aber ein wenig Computerkenntnisse, obwohl das Verfahren ziemlich einfach ist. Der Zugriff auf den Quellcode wird erklärt [hier](Compile_on_Linux/de#Abruf_der_Quelle.md), und wir haben detaillierte Anweisungen zum Kompilieren auf [Windows](Compile_on_Windows/de.md), [Linux](Compile_on_Linux/de.md) und [macOS](Compile_on_MacOS/de.md).



### FreeCAD meldet, dass einige Module oder Anwendungen fehlen 

FreeCAD hängt von vielen Dingen ab, um seine gesamte Funktionalität anzubieten. Alle wichtigen benötigten Komponenten sind normalerweise in deiner FreeCAD Installation enthalten oder werden von deinem Paketmanager bereitgestellt, so dass du dir normalerweise keine Sorgen machen musst. Wenn du FreeCAD jedoch aus inoffiziellen Quellen installiert hast oder FreeCAD selbst kompiliert hast, könnten einige Teile fehlen, die für FreeCAD selbst nicht kritisch sind, aber dazu führen können, dass einige Funktionen nicht verfügbar sind. Einige spezifische Dateiformate wie Collada oder DWG benötigen auch zusätzliche Komponenten, die nicht in FreeCAD gebündelt sind und von dir selbst separat installiert werden müssen.

Alle diese Komponenten und das empfohlende Vorgehen zu deren Installation sind auf der [Zusätzliche Python Module](Extra_python_modules/de.md) Seite aufgeführt.



## Fehlersuche



### FreeCAD startet überhaupt nicht 

Dafür kann es eine Menge Gründe geben, am wahrscheinlichsten fehlen einige Bibliotheken. Versuche FreeCAD von einem Terminal zu starten (schreibe {{SystemInput|freecad}} an der Eingabeaufforderung, {{SystemInput|FreeCAD}} auf einigen Systemen), um hier zu sehen, ob Fehlermeldungen erscheinen. Lies auch den Rest der dieser HGF, da es dir weitere Anhaltspunkte geben kann, um die Ursache des Problems aufzuspüren. Wenn nichts hilft, berichte darüber im [Forum](http://forum.freecadweb.org/) davon, dort findet sich sicher jemand, der helfen kann.

Auf einigen älteren Windows XP Systemen erhälst du möglicherweise eine Fehlermeldung wie diese: **Die Anwendung kann nicht gestartet werden, da die Side-by-Side Konfiguration falsch ist. Die Neuinstallation der Anwendung kann das Problem lösen.** Der Grund für dieses Problem ist, dass auf Ihrem System entweder die CRT Laufzeitbibliotheken fehlen oder die installierte Version zu alt ist, weil FreeCAD mit einer neueren Version verknüpft wurde. In diesem Fall musst du das **Microsoft Visual C++ Redistributable Package** installieren, das du bei Microsoft findest. Siehe auch den entsprechenden [Forenbeitrag](http://forum.freecadweb.org/viewtopic.php?f=3&t=1298&p=9961).



### FreeCAD startet normal, aber nicht alle Symbole werden angezeigt. Einige werden durch ein schwarzes \'X\' ersetzt. 

Einige Teile von FreeCAD hängen von dem externen Pythonmodul, genannt Pivy ab. Unter Windows ist Pivy in der FreeCAD Installation enthalten. Auf Debian/Ubuntu Systemen ist das python-pivy Paket Teil der Standardsoftware Repositorien. Auf anderen Systemen muss pivy derzeit selbst kompiliert werden. Auf anderen Systemen musst du pivy im Moment eventuell selbst kompilieren. Beachte, dass zwar einige Werkzeuge ohne pivy nicht verfügbar sind, der Rest von FreeCAD aber normal funktioniert.



### Ich habe Anzeigeprobleme, die 3D Ansicht verhält sich nicht korrekt, es gibt Müll, wenn ich die Ansicht bewege/drehe, usw. 

FreeCAD ist für die Anzeige von 3D Inhalten abhängig von OpenGL und benötigt daher eine funktionierende OpenGL Umgebung. Auf einigen Systemen ist OpenGL nicht standardmäßig aktiviert, und du musst möglicherweise deine Grafiktreiber installieren oder aktualisieren. Dieses Problem tritt am häufigsten auf Linux Systemen oder auf virtuellen Systemen auf. Wenn du dich auf einem Linuxbasierten System befindest, versuche die folgenden Schritte:

-   Überprüfe, ob dein Computer eine 3D-fähige Grafikkarte hat
-   gib {{SystemInput|glxinfo}} in ein Terminalfenster ein und überprüfe in der Ausgabe, ob Direct Rendering auf \"yes\" gesetzt ist und ob der OpenGL Anbieter/Renderer/die Version mit deiner Grafikkarte übereinstimmt.
-   Installiere andere OpenGL-basierte Software ([Blender](http://www.blender.org), zum Beispiel) und prüfe, ob sie korrekt läuft und angezeigt wird.



### FreeCAD stürzt beim Start ab 

Ein Absturz könnte eine ernsthafteren Fehler andeuten oder ein Problem in deiner Konfiguration. Die meisten Abstürze treten aus einem der beiden folgenden Gründe auf:



#### Die OpenGL Treiber sind nicht installiert oder funktionieren nicht ordnungsgemäß 

Dies ist eine sehr häufige Ursache für das Problem. Die Symptome sind einfach, dass FreeCAD beim Start abstürzt, oder immer dann, wenn du eine 3D Ansicht öffnest (z.B. durch Erstellen eines neuen Dokuments). Versuche herauszufinden, was für einen Grafikchip du hast, dann finde heraus, ob er [OpenGL](https://en.wikipedia.org/wiki/OpenGL) unterstützt (die meisten neueren Chips tun das), dann finde den richtigen Treiber und installieren ihn. Eine gute Möglichkeit, um zu überprüfen, ob OpenGL verfügbar ist, ist der Versuch, eine andere OpenGL Anwendung wie [blender](http://www.blender.org) zu starten.

Und als allgemeiner Tip, um mehr Informationen über Abstürze mit FreeCAD zu erhalten, kannst du es mit dem Programmparameter {{SystemInput|--write-log}} starten. Dadurch wird die Datei **FreeCAD.log** in **$XDG_CONFIG_HOME/FreeCAD** ({{VersionPlus/de|0.20}}) oder **$HOME/.FreeCAD** ({{VersionMinus/de|0.19}}) auf Linux, in**$HOME/Library/Preferences/FreeCAD** unter macOS oder **%APPDATA%/FreeCAD** auf Windows-Systemen erstellt.

In einigen seltenen Fällen hast Du vielleicht einen Grafiktreiber installiert, der nicht zu Deiner Grafikkarte passt. Wir hatten einen Fall, wo im Laptop des Benutzer eine Intel on-board Grafik verbaut war, aber einige ATI Treiber installiert waren. Siehe ([FreeCAD startet nicht](http://forum.freecadweb.org/viewtopic.php?f=13&t=5160&start=10#p41042)). Nach dem Entfernen der Dateien und der Neuinstallation des richtigen Treibers begann FreeCAD zu arbeiten.



#### Eine Bibliothek, die von FreeCAD benötigt wird, ist nicht auf Ihrem System vorhanden oder wurde von FreeCAD nicht gefunden 

Es kann zwei Wege zu diesem Problem geben: entweder fehlt einfach eine Bibliothek und FreeCAD weigert sich deshalb zu starten, oder die Bibliothek ist zwar vorhanden, aber es ist eine ältere Version als die, die FreeCAD erwartet, so dass ein Absturz auftritt, wenn FreeCAD versucht, eine fehlende Funktion dieser Bibliothek zu verwenden. Ein häufiges Beispiel ist, wenn du Qt3 und Qt4 auf deinem System installiert hast. FreeCAD könnte Qt4 erkennen, aber wenn deine Qt Installation nicht richtig konfiguriert ist, könnten einige Teile von Qt3 noch verwendet werden, was Abstürze provoziert.

Bitte überprüfe die Installationsprozedur ([Windows](Installing_on_Windows/de.md), [Linux](Installing_on_Linux/de.md) oder [Mac](Installing_on_Mac.md)), stelle sicher, dass du alle erforderlichen Bibliotheken installiert hast (auf den meisten Linux Systemen geschieht dies automatisch), und überprüfe, was die minimale Versionsnummer für jede der Komponenten ist.

Wenn alles richtig aussieht, beschreibe das Problen im [Forum](http://forum.freecadweb.org/) oder [Einen Fehler über-Mitteln](Tracker/de.md). Wenn Du auf einem Linux-System bist, ist es einfach, eine Fehlerrückverfolung zu erstellen, der für die Entwickler sehr wichtige Informationen über den Absturz liefert:

-   Tippe in einem Terminal {{SystemInput|gdb freecad}} (vorausgesetzt, das gdb Paket ist installiert)
-   In gdb, tippe {{SystemInput|run}}
-   Nach dem Absturz tippe {{SystemInput|bt}}, um die Rückverfolung zu erhalten, so dass Du ihn an deinen Fehlerbericht anfügen kannst.



### FreeCAD friert nach dem Hochfahren ein 

Beim Starten von FreeCAD erscheint die GUI fast augenblicklich, aber die GUI ist eingefroren und die CPU Auslastung bei ungefähr 99%. Das kann auf dem KDE Desktop passieren, wenn man das Oxygen Theme benutzt. Das ist ein Fehler im Oxygen Theme und die Wahl eines anderen Themes sollte das Problem lösen.



### FreeCAD stürzt beim Erstellen eines neuen Dokuments oder Öffnen einer Datei ab 

Wenn FreeCAD beim Erstellen einer neuen 3D Ansicht abstürzt, versuche, FreeCAD über ein Terminal zu starten. Wenn beim Absturz eine Fehlermeldung erscheint, die {{SystemOutput|Assertion Failed}} und einen Komponentennamen, der mit \"So\" beginnt ({{SystemOutput|SoBase}}, {{SystemOutput|SoFieldContainer}}, usw.), erwähnt, ist die Wahrscheinlichkeit sehr hoch, besonders wenn du unter Linux arbeitest, dass FreeCAD versucht, zwei verschiedene Versionen der Coin Bibliothek zu verwenden, was den Absturz verursacht. Um zu überprüfen, ob dies tatsächlich das Problem ist, versuche Folgendes:

-   Suche die ausführbare Datei von FreeCAD (normalerweise in **/usr/lib/FreeCAD/bin**)
-   Führe den Befehl {{SystemInput|ldd FreeCAD}} in einem Terminal aus
-   Notiere dir die Version der Bibliothek **libCoin.so**, die FreeCAD verwendet (zum Beispiel **libCoin.so.60**)
-   Suche die Bibliothek **libSoQt.so** (normalerweise in **/usr/lib**)
-   Führe {{SystemInput|ldd libSoQt.so}} aus und prüfe, ob es auf die gleiche Coin Version wie FreeCAD verweist.

Wenn es einen Unterschied gibt, muss entweder FreeCAD oder SoQt neu kompiliert werden (besser ist es, dasjenige neu zu kompilieren, das die älteste Coin Version verwendet). Normalerweise sollte man versuchen, die Leute zu kontaktieren, die für das Paketieren von SoQt oder FreeCAD verantwortlich sind, und sie freundlich bitten, eine Neukompilierung in Betracht zu ziehen. Wenn du diesen Schritt selbst unternehmen willst, und es nicht möglich ist, SoQt neu zu kompilieren, weil es andere Anwendungen auf deinem System kaputt macht, kannst du FreeCAD mit {{SystemInput|<nowiki>./configure --with-coin=DIR</nowiki>}} zwingen, mit der benötigten Coin Version zu kompilieren. Du musst aber sicherstellen, dass das richtige Entwicklungspaket dieser Coin Version installiert ist.



### FreeCAD stürzt nach Bearbeiten → Ausrichtung ab 

Ein Segmentierungsfehler tritt bei {{SystemOutput|vbo_save_playback_vertex_list()}} auf. Dies bedeutet, dass die Implementierung von VBO im Grafiktreiber schlecht ist. Um das Zwischenspeichern von OpenGL Aufrufen zu vermeiden, kannst du versuchen, die Umgebungsvariable {{SystemInput|<nowiki>IV_SEPARATOR_MAX_CACHES=0</nowiki>}} zu setzen und FreeCAD neu zu starten.



### Ich habe Schwierigkeiten bei der Ausführung von FreeCAD auf macOS 

Die Mac Plattform ist weniger einfach zu unterstützen als Windows oder Linux, da keiner der Hauptentwickler einen Mac besitzt. Die macOS Pakete werden von freiwilligen FreeCAD Benutzern kompiliert, und es kann sein, dass sie auf Ihrem Rechner nicht richtig funktionieren, je nach System. Deine beste Chance ist wahrscheinlich, in die Foren zu gehen, nach macOS-bezogenen Beiträgen zu suchen und dein Problem dort zu diskutieren oder zu sehen, ob jemand anderes eine Lösung gefunden hat.



### Ich kann keine numerischen Werte in den Eigenschaftenfeldern von FreeCAD ändern 

<img alt="Sprachoptionen" src=images/Jj62l.png  style="width:480px;">

Höchstwahrscheinlich hast du die regionalen Einstellungen von Windows falsch eingestellt. Bitte prüfe, ob du in deinen Ländereinstellungen das gleiche Symbol für das Dezimaltrennzeichen und das Symbol für die Zifferngruppierung hast. Wenn ja, [passe deine Systemeinstellungen an](http://forum.freecadweb.org/viewtopic.php?f=4&t=2655&p=20046#p20041), um unterschiedliche Zeichen für das Zifferngruppensymbol und das Dezimaltrennzeichen zu verwenden. Beachte, dass der Punkt als Dezimaltrennzeichen nicht zwingend erforderlich ist. Es ist zwingend erforderlich, in diesen beiden Einstellungen unterschiedliche Symbole zu verwenden. 



### FreeCAD lief normal, aber plötzlich startet es nicht mehr 

Dies kann auch passieren, wenn du eine ältere Version von FreeCAD installiert hattest und auf eine neuere Version aktualisiert hast. Bei diesem Prozeß könnten die Konfigurationsdateien von FreeCAD aus irgendeinem Grund beschädigt worden sein, und nun kann FreeCAD sie nicht mehr lesen und startet nicht mehr. Die Lösung ist einfach, diese Konfigurationsdateien zu löschen, so dass FreeCAD sie beim ersten Lauf neu erstellt.

-   Auf Windows: Öffne den Datei Explorer und schreibe **%APPDATA%\FreeCAD** als Dateipfad. Dort angekommen, lösche dort die Dateien **user.cfg** und **system.cfg**
-   Auf Linux: Navigiere zu **/home/USERNAME/.local/share/FreeCAD** ({{VersionPlus/de|0.20}}) oder **/home/USERNAME/.FreeCAD** ({{VersionMinus/de|0.19}}) und lösche dort die Dateien **user.cfg** und **system.cfg**
-   Auf Mac: Navigiere zu **/Users/USERNAME/Library/Preferences/FreeCAD** und lösche dort die Dateien **user.cfg** und **system.cfg**

FreeCAD sollte nun wieder normal, mit allen Einstellungen zurückgesetzt, starten.

Es gibt ein [Makro findeKonfigDateien](Macro_findConfigFiles/de.md), das beim Auffinden deiner Konfigurationsdateien hilft Es kann über den Addon-Manager im Menü Extras installiert werden. **Werkzeuge → Addon-Manager → Makros → findConfigFiles**. Das Makro findet deinen Konfigurationsdateiordner, kopiert ihn in die Zwischenablage und (versucht), diesen Ort mit deinem Standard-Dateibrowser zu öffnen. Es nimmt keine Änderungen an deinen Dateien oder Einstellungen vor.



## FreeCAD benutzen 



### Ist FreeCAD wirklich kostenlos? Sogar für kommerzielle Nutzung? 

FreeCAD ist [Open-Source Software](https://de.wikipedia.org/wiki/Open_Source) und ist nicht nur frei, um es für sich selbst oder für kommerzielle Zwecke zu nutzen, sondern auch, um es zu verteilen, zu modifizieren oder sogar in einer Closed-Source Anwendung zu verwenden. Zusammenfassend, du bist frei (fast) alles damit machen zu können, was du willst. Siehe die [Lizenz](Licence/de.md) Seite für weitere Details.



### Wie drehe ich die 3D Ansicht? 


<center>

Image:Style_of_navigation.png\|Von der **right button** Maus Image:Style of navigation menu.png\|Vom Menü **Bearbeiten → Einstellungen →**


</center>




FreeCAD verfügt über mehrere verschiedene [Navigationsmodi](Mouse_navigation/de.md), die man im Einstellungsdialog einstellen oder durch einen Rechtsklick in der 3D Ansicht ändern kann. Ausführliche Informationen zu den Modi finden sich auf der Seite [Mausnavigation](Mouse_navigation/de.md). 



### Was kann ich mit FreeCAD tun? Wo soll ich anfangen? 

Mach dich auf zur [Erste Schritte](Getting_started/de.md) Seite für eine kurze Beschreibung der Werkzeuge, die du verwenden kannst. Es gibt auch einen neuen Abschnitt [Tutorien](Tutorials/de.md) mit einigen Ressourcen. Der [Anwenderzentrums](User_hub/de.md) Abschnitt enthält detailliertere Informationen über die verschiedenen Arbeitsbereiche von FreeCAD. Da FreeCAD relativ neu ist, ist die Benutzeroberfläche noch sehr kahl und bietet nicht viele Werkzeuge. Aber viel mehr fortgeschrittene Funktionalität steht dir bereits über [Python Skripten](Power_users_hub/de.md) zur Verfügung.



### Gibt es Dokumentation für Neueinsteiger? Wie kann ich die Benutzung von FreeCAD lernen? 

Es gibt eine Menge Dokumentation, die an verschiedenen Stellen verteilt ist, sowohl auf der FreeCAD Webseite als auch außerhalb. Du solltest mit der Seite [Erste Schritte](Getting_started/de.md) beginnen. Der Bereich [Tutorien](Tutorials/de.md) enthält viele spezialisierte Tutorienseiten, die dir den Einstieg in die verschiedenen Arbeitsbereiche erleichtern. Das [Handbuch:Einführung](Manual:Introduction/de.md) ist eine allgemeine, vollständige, benutzerorientierte Anleitung zu FreeCAD. Der [Anwenderzentrums](User_hub/de.md) Abschnitt dieses Wikis listet alle Seiten auf, die sich an Endanwender richten. Auf externen Seiten wie z.B. [Youtube](https://www.youtube.com/results?search_query=freecad) findest du auch eine Menge von Video Tutorien, die von Benutzern erstellt wurden. Und nicht zuletzt enthält das [Forum](https://forum.freecadweb.org) eine Menge Antworten auf Fragen, die von anderen Neulingen gestellt wurden.



### Ich möchte Daten im XYZ Format nach/von FreeCAD im-/exportieren. Wie mache ich das? 

Bitte nutze die Seite [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md). Vielleicht werden Deine Fragen dort bereits beantwortet.

### Where can I find workarounds for features that FreeCAD currently does not support? 

Please refer to the [Workarounds](Workarounds.md) page.



## Arbeiten mit Part Geometrie 



### Wie extrudiere ich Sachen in Festkörper? Ich erhalte nicht das richtige Ergebnis 

The theory is simple: Lines (or wires), when extruded, form faces. Faces, when extruded, form solids.

Wenn du etwas extrudierst und das Ergebnis kein Festkörper ist, dann war das Etwas keine Fläche. Wenn du Linien hast und daraus einen Festkörper extrudieren willst, musst du zuerst Linien auswählen, die einen geschlossenen Umriss bilden (wähle mehrere Objekte durch Drücken von **Ctrl** aus), verbinde sie zu einem Draht (Werkzeug [Draft Heraufstufen](Draft_Upgrade/de.md)) und mache dann aus diesem Draht eine Fläche (nochmals Werkzeug<img alt="" src=images/Draft_Upgrade.svg  style="width:16px;"> [Draft Heraufstufen](Draft_Upgrade/de.md)). So, wenn alles gut gegangen ist, kannst du jetzt zu einem Festkörper extrudieren.

Nun kann es viele kleine Verdrehungen geben, die dazu führen, dass du das falsche Ergebnis erhälst. Der beste Weg, um sicher zu gehen, ist zu überprüfen, was sich im Inneren des Objekts befindet, das du extrudierst. Der Inhalt von Objekten kann mit Python leicht erforscht werden. Angenommen, du hast ein Objekt mit dem Namen \"Wire\", dann könntest du dies in die Python Konsole eingeben:


{{code|code=
obj = FreeCAD.ActiveDocument.Wire
shp = obj.Shape
print shp.Faces
print shp.Wires
if shp.Wires:
    for w in shp.Wires:
        print w.isClosed()
}}

Der obige Code ruft die Form von einem Objekt ab, zeigt die Flächen und Drähte an, die dein Objekt hat (falls vorhanden), und druckt, wenn Drähte vorhanden sind, ob diese Drähte geschlossen sind. Wenn du keine Fläche hast, erhälst du keinen Festkörper. Wenn es keinen geschlossenen Draht gibt, wird er nicht zu einer Fläche. Wenn du daran interessiert bist, gibt es auf der Seite [Part Skripten](Topological_data_scripting/de.md) mehr Informationen darüber, was du mit Python überprüfen kannst. Wenn du mehrere Linien nicht zu einem Draht zusammenfügen kannst, ist die wahrscheinlichste Ursache, dass sich deine Endpunkte nicht treffen, es müssen kleine Lücken zwischen (einigen) von ihnen sein. Da wäre es meiner Erfahrung nach am schnellsten, einen Draht darüber neu zu zeichnen.



### Meine booleschen Operationen schlagen fehl oder liefern merkwürdige Ergebnisse 

Der [Open CASCADE](https://en.wikipedia.org/wiki/Open_CASCADE_Technology) Geometriemodellierungs Kernel, der in FreeCAD für die Teilegeometrie verwendet wird, hat, obwohl er wahrscheinlich der beste verfügbare Open-Source Geometrie Kernel ist, seine Schwächen und Begrenzungen. In der Tat sind die booleschen Operationen (Verschmelzen, Subtraktion, Schnittmenge) nicht seine besten Eigenschaften und liefern oft seltsame Ergebnisse. Dies ist eine Begrenzung, die wir derzeit nicht lösen können, daher ist es am besten, wenn du versuchst, das gewünschte Ergebnis durch eine andere Art der Modellierung zu erhalten. Zum Beispiel können Probleme mit Grundelementen wie Zylindern oft gelöst werden, indem man stattdessen einen extrudierten Kreis verwendet. Koplanare Flächen zwischen Teilen können Probleme verursachen, ebenso wie Flächentangentialität. Als allgemeine Regel gilt: Wenn eine Form nicht funktioniert, versuche, sie auf eine andere Weise umzuformen. In 99 % der Fälle wirsr du am Ende das gewünschte Ergebnis erzielen.



### Wenn ich mein Modell exportiere (oder anzeige), werden die Löcher ausgefüllt 

Verwende nicht **Strg** + **A** (Alles auswählen), um alles aus dem Hierarchiebaum zu exportieren. Wenn das Modell aus einem einzigen Element besteht, versuche, nur das neueste Element (normalerweise das letzte) im Hierarchiebaum auszuwählen.

Wenn wir ein Modell im Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) erstellen, nimmt jedes Formelement die Form des letzten an und fügt etwas hinzu oder entfernt etwas, wodurch lineare Abhängigkeiten von Formelement zu Formelement entstehen, während das Modell erstellt wird. Ein \"Schnitt\" Formelement ist also nicht nur das Schnittloch selbst, sondern das ganze Teil mit dem Schnitt. Aus diesem Grund sollte der Benutzer in der Regel nur das neueste Element (Formelement) im Modellbaum sichtbar haben, da sich sonst die Phasen des Modells überlagern und Löcher von den früheren Modell-Formelementen ausgefüllt werden.

Um die Sichtbarkeit eines Objekts ein- oder auszuschalten, wähle es im Hierarchiebaum aus und drücke die **Leertaste** auf deiner Tastatur. Normalerweise sollte alles bis auf das letzte Element im Hierarchiebaum ausgegraut und damit in der [3D-Ansicht](3D_view/de.md) nicht sichtbar sein.



### Meine parametrischen Objekte gehen kaputt, wenn ich ihre Basisskizzen ändere 

Du hast das (un)berühmte Toponaming Problem getroffen. Dies ist derzeit ein großes Problem in FreeCAD für Neueinsteiger. Es ist in ganz FreeCAD vorhanden, tritt aber bei der Verwendung von [Skizzen](Sketcher_Workbench/de.md) stärker hervor. Die Erklärung ist einfach: Beim Neuberechnen einer Skizze werden die geometrischen Elemente (Kanten, Flächen\...) in einer anderen Reihenfolge neu aufgebaut, abhängig von der Priorität der Beschränkungen. Sie erhalten dann einen anderen Namen (Kante1, Kante2, Fläche1, Fläche2\...). Die meisten nachfolgenden Operationen hängen von diesen Namen ab, um zu identifizieren, an welcher Unterkomponente sie arbeiten. Wenn die Skizze neu erstellt wird, kann es daher vorkommen, dass Formelemente, die auf solchen Unterkomponenten basieren, plötzlich ihre Basisgeometrie geändert bekommen und ein falsches Ergebnis liefern.

Dies ist ein sehr schwer zu überwindendes Problem (das [Topologisches Benennungsprojekt](Topological_Naming_Project/de.md) hat sich zum Ziel gesetzt, es zu lösen). Es gibt jedoch viele Umgehungsmöglichkeiten, um das Problem zu entschärfen, und fortgeschrittene Benutzer schaffen es in der Regel, es komplett zu vermeiden. Ein paar Strategien sind:

-   Du musst wissen, dass Skizzen sehr empfindlich auf das Problem reagieren. Das Referenzieren einer bestimmten Kante einer Skizze oder einer Fläche eines Objekts, das auf einer Skizze aufgebaut ist, wie z. B. ein [PartDesign Polster](PartDesign_Pad/de.md), ist gefährlich, es sei denn, du bist dir ziemlich sicher, dass sich diese Skizzen im Laufe der Zeit nicht ändern werden oder die Skizze sehr einfach ist. Ein Polster, das auf einer einfachen rechteckigen Skizze aufgebaut ist, ist z. B. wahrscheinlich sicher, da es nur eine Fläche erzeugt, so dass es kein Ordnungsproblem gibt.
-   Bevorzuge andere Arten von Objekten wie [Part](Part_Workbench/de.md) oder [Entwurf](Draft_Workbench/de.md), wenn möglich. Diese Objekte werden immer auf die gleiche Art und Weise gebaut, und daher folgen ihre geometrischen Komponenten normalerweise jedes Mal der gleichen Reihenfolge, wenn sie neu gebaut werden. Sie sind viel weniger anfällig für Topobenennung Probleme.
-   Um weitere Objekte an die Flächen von skizzenbasierter Geometrie anzuhängen, verwende vorzugsweise [Bezugsgeometrie](PartDesign_Plane/de.md). Diese unsichtbaren \"Hilfsobjekte\" sind nicht von der Skizzengeometrie abhängig und bleiben daher über die Zeit stabil.



## Zu FreeCAD beitragen 



### FreeCAD ist so ein tolles Programm! Wie kann ich helfen? 

Es gibt viele verschiedene Möglichkeiten zu helfen, auch wenn du kein Programmierer bist. Hier sind ein paar Dinge, die du tun kannst:

-   Gib den FreeCAD Entwicklern eine Rückmeldung: Es ist immer nützlich zu wissen, was die Leute denken, was sie gut fanden, was sie vermissen, etc. Schreibe eine Notiz im [Forum](http://forum.freecadweb.org/) und teile deine Meinung mit oder stelle eine Anfrage auf unserem [Themennachverfolger](https://tracker.freecadweb.org/main_page.php)!
-   Hilf beim Schreiben der Dokumentation: Die Dokumentation, die wir hier auf dieser Seite haben, ist manchmal sehr begrenzt. Wenn du etwas entdeckt hast, das nicht gut dokumentiert ist, füge dein Wissen dort hinzu!
-   Hilf anderen Neulingen: Hänge im Forum herum und hilf Neulingen, grundlegende Fragen zu lösen, wie z.B. wie installiere ich, wie füge ich einen Würfel hinzu, usw.
-   [Übersetze die Dokumentation](Help_FreeCAD/de#Übersetze_die_Dokumentation.md) in deine eigene Sprache
-   [Übersetze FreeCAD](Help_FreeCAD/de#Übersetzen_FreeCAD.md) in deine eigene Sprache
-   Schreibe [Tutorien](Tutorials/de.md), oder nehme Videotutorien auf: Tutorien sind ein sehr einfacher Weg für Neulinge, eine neue Software zu erlernen. Wenn du etwas Schönes gemacht hast, warum zeigst du es nicht anderen Leuten, wie es geht?
-   Trage mit Aktivposten und Beispielen bei: Wir vermissen immer noch gute Beispieldateien in FreeCAD. Wenn du etwas Gutes erstellt hast, teile es mit uns!
-   [Fehler einreichen](Tracker/de.md): Es ist sehr wichtig, dass alle möglichen Fehler behoben werden. Wenn Du einen findest, melde ihn so deutlich wie möglich, damit wir genau verstehen können, was passiert ist.
-   Versuche, etwas in Python zu programmieren: Du hast noch nie programmiert, aber du willst es versuchen? Python ist einfach. Lies unsere [Einführung in Python](Introduction_to_Python/de.md), aber Vorsicht, du könntest schnell süchtig werden!
-   Siehe die [Hilf FreeCAD](Help_FreeCAD/de.md) Seite für weitere Details, wie du beitragen kannst.



### Wie kann ich Bearbeitungsrechte für das Wiki erhalten? 

Siehe den [Arbeiten an der Dokumentation](Help_FreeCAD/de#Arbeiten_an_der_Dokumentation.md) Abschnitt der Seite für weitere Details, wie beigetragen werden kann.



### Nimmt FreeCAD am \"Google Summer of Code\" teil? 

Ja. Seit 2016 nimmt FreeCAD am Google Summer of Code teil. Siehe [Google Summer of Code 2020](Google_Summer_of_Code_2020.md) für Informationen zu vergangenen Ausgaben und [Google Summer Of Code 2016](http://forum.freecadweb.org/viewtopic.php?f=8&t=13838) im Forum für die ursprüngliche Ankündigung.



### Ich möchte anfangen, das Wiki in meine Sprache zu übersetzen. Was muss ich tun? 

Dieses Wiki beherbergt eine Vielzahl von Inhalten. Das aktuellste und interessanteste Material ist im [Handbuch](Online_Help_Toc/de.md) gesammelt.

Siehe den [Dokumentation übersetzen](Help_FreeCAD/de#Bearbeiten_der_Dokumentation.md) Abschnitt der Seite für weitere Details, wie man das Wiki übersetzt.

### Can I buy swag? 

FreeCAD doesn\'t offer swag you can order to support the project. But you can create your own. See our [Swag](Swag.md) page for instructions.



## Lizenzierung, kopieren und Wiederverwendung 



### Muss ich etwas bezahlen, um FreeCAD nutzen zu können? 

Nein. FreeCAD ist völlig kostenlos zu verwenden, herunterzuladen, weiterzugeben oder zu modifizieren. Es ist [open-source software](https://en.wikipedia.org/wiki/Open_source), veröffentlicht unter den Bedingungen der [GNU Lesser General Public License 2.1](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), die Dir diese Freiheiten garantiert und, was noch wichtiger ist, Dir garantiert, dass Dir diese Freiheiten nie genommen werden.



### Kann ich einen beliebigen Teil der FreeCAD Illustrationen oder Teile der Webseite wiederverwenden? 

Sicher. Alle Illustrationen (Symbole, Banner, usw.) von FreeCAD sind LGPL lizenziert, ebenso wie der FreeCAD Code. Bediene dich auf der Seite [Artwork](Artwork/de.md). Die Website ist eine Standard MediaWiki Seite, alle grafischen Elemente können frei wiederverwendet werden, und wenn Du neugierig bist, wie wir die MediaWiki Software optimiert haben, suche nach den speziellen Common css- und js Seiten.



### Kann ich Teile von FreeCAD in anderen Anwendungen wiederverwenden? 

Ja, du kannst die Kernteile von FreeCAD in anderen Anwendungen verwenden, solange du die Bedingungen der LGPL einhältst. Bibliotheken von Drittanbietern, [externe Arbeitsbereiche](External_workbenches/de.md) und [Makros](Macros/de.md) können ihren eigenen Lizenzbedingungen unterliegen, also wende dich bitte an ihre Autoren. Weitere Informationen findest Du auf der [Lizenz](Licence/de.md) Seite.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Documentation](Category_Documentation.md) > Frequently asked questions/de
