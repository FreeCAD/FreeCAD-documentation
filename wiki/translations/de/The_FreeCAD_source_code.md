# The FreeCAD source code/de
Der [FreeCAD Quellcode](https   *//github.com/FreeCAD/FreeCAD) wird mit git verwaltet, und ist öffentlich, offen und unter der [LGPL Lizenz](https   *//en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) verfügbar. Er kann von jedem kopiert, heruntergeladen, gelesen, analysiert, weiterverbreitet und modifiziert werden. Wenn du planst, Änderungen vorzunehmen, die du im offiziellen Code selbst sehen möchtest, denke daran, dass deine Änderungen von den FreeCAD Entwicklern genehmigt werden müssen. Daher ist es ratsam, deine Absichten und Ideen zuerst im [Forum](http   *//forum.freecadweb.org) zu diskutieren, um das Risiko zu vermeiden, dass deine Änderungen aus einem nicht vorhersehbaren Grund abgelehnt werden.

Im Folgenden findest Du einige Hinweise und nützliche Informationen, um Dich auf den richtigen Weg zu bringen, wenn Du daran interessiert bist, den FreeCAD Code zu erforschen.

-   Der FreeCAD Code ist hauptsächlich in **C++** programmiert, stützt sich aber stark auf **Python**. Ein sehr großer Teil seiner Funktionalität bietet zugehörige Python Bindungen, und es ist Teil der Kernphilosophie der FreeCAD Entwicklung, stets Python Zugriff auf jede neue, in C++ implementierte Funktion zu bieten. Um dies zu erreichen, wird CPython (die von Python selbst zur Verfügung gestellten C Schnittstellenwerkzeuge) und insbesondere [PyCXX](http   *//cxx.sourceforge.net/) in FreeCAD stark genutzt. Viele Vorlagen und benutzerdefinierte Werkzeuge werden auch im FreeCAD Code selbst zur Verfügung gestellt, um das Erstellen der zugehörigen Python Bindungen sehr einfach zu machen. Einige weitere Spitzenbestandteile des FreeCAD Codes sind vollständig in Python geschrieben.

-   Der FreeCAD Quellcode ist vollständig *\'plattformübergreifend*, und es wird große Sorgfalt darauf verwendet, die Anwendung auf einer größtmöglichen Anzahl von Plattformen und Konfigurationen einsetzen zu können und bestehende Benutzer nicht in schwierige Situationen zu bringen. Daher werden neue Versionen der benötigten Komponenten so weit wie möglich vermieden, solange sie nicht auf allen Plattformen allgemein und leicht verfügbar sind, und die Abwärtskompatibilität (die Möglichkeit, eine mit einer alten Version von FreeCAD erstellte Datei auf einer neueren Version zu öffnen) ist eine wichtige Priorität.

-   Fast die gesamte Funktionalität von FreeCAD ist in zwei verschiedene Teile aufgeteilt, die **App** und **Gui** (Abkürzung; engl.   * Application and Graphical User Interface = Anwendung und Grafische Benutzeroberfläche) genannt werden.

Abk. GUI von englisch graphical user interface Diese Trennung spiegelt sich überall in der Dateistruktur des Quellcodes wider. Die Anwendung enthält die gesamte Funktionalität, die im reinen Konsolenmodus (ohne Grafische Benutzeroberfläche) laufen muss. Da FreeCAD ohne seine grafische Benutzeroberfläche kompiliert und ausgeführt werden kann, ist der Code in der Anwendung unabhängig von jeder GUI-bezogenen Bibliothek. Gui enthält den gesamten Code, der für die Ausführung im GUI Modus benötigt wird und ist um die App Funktionalität herum aufgebaut.

-   Der Grossteil der FreeCAD Funktionalität ist in **Modulen** umgesetzt. FreeCAD ohne seine Module ist ein einfaches Container Fenster, das einfach eine Datei öffnen und speichern kann. Alle Geometriewerkzeuge und Arbeitsbereiche sind in Modulen umgesetzt. Module können in C++, in Python oder in einer Kombination aus dem Besten aus beiden Welten geschrieben werden. Es kann sich um hybride C++/Python Module handeln, bei denen die feste Kernfunktionalität in C++ programmiert ist und die Endbenutzerwerkzeuge in Python geschrieben sind, so dass sie von FreeCAD Anwendern leichter erweitert und angepasst werden können. Jedes Modul definiert und erzeugt normalerweise eine **Arbeitsbereich** in der FreeCAD Oberfläche, wenn es im GUI Modus verwendet wird, normalerweise mit dem gleichen Namen, aber es ist nicht zwingend erforderlich, dass die Module einen Arbeitsbereich enthalten.

-   FreeCAD Module sind oft **abhängig von anderen Modulen**. Die meisten Module, die Festkörpergeometrie verwenden, hängen von dem **Formteil** Modul ab, welches das grundlegendste Modul von FreeCAD ist und die meisten Schnittstellen mit OpenCascade umsetzt. Obwohl andere Module die OpenCascade Funktionalität direkt nutzen können, verlassen sie sich oft auf übergeordnete Funktionen, die von Part zur Verfügung gestellt werden.

-   Module sind immer **initialisiert** durch Python. Auch wenn sie vollständig in C++ geschrieben sind, enthalten sie immer eine minimale Python/CPython-Struktur.

-   FreeCAD ist ein begeisterter Nutzer von **anderen Quelloffenen Bibliotheken**. Neben Python und Qt, die vom Kern und fast allen Modulen verwendet werden, sind die beiden schwergewichtigen Bibliotheken, die in den meisten Modulen verwendet werden, [OpenCascade Technologie](https   *//en.wikipedia.org/wiki/Open_Cascade_Technology) (OCCT) und [Coin3D](http   *//www.coin3d.org/). OpenCascade wird verwendet, um die gesamte Festkörpergeometrie von FreeCAD zu erstellen und zu verwalten, während Coin3D für die Verwaltung der 3D Ansicht verwendet wird. OpenCascade wird hauptsächlich in der App Welt verwendet, und coin3D ausschließlich in der Gui Welt. Ein grundsätzliches Verständnis von OpenCascade ist wesentlich, um jede geometriebezogene Arbeit mit FreeCAD durchzuführen. Spezifischere Module nutzen spezifischere Bibliotheken, und da es in diesem Punkt normalerweise keine Einschränkungen gibt, abgesehen davon, dass diese Bibliotheken auf allen Plattformen leicht verfügbar sind, kann die Liste der Abhängigkeiten einer vollständigen FreeCAD Installation mit all ihren Modulen ziemlich groß sein.

-   FreeCADs **Dokument Objekte**, welche alle die Objekte sind, die in einem FreeCAD Dokument enthalten sind, sind das, was in der Baumansicht in der GUI und in FreeCAD.ActiveDocument.Objects() in Python erscheint. Sie können, müssen aber keine geometrischen Daten haben und können, müssen aber nicht, in der 3D Ansicht angezeigt werden. Sie sind immer in App und Gui Teile getrennt. Der Gui Teil wird nicht geladen, wenn er im Konsolenmodus ausgeführt wird. Bei geometrischen Standardobjekten, wie z.B. in Part oder PartDesign, wird die OpenCascade basierte Geometrie in der App definiert, während das Gui Gegenstück (auch \"Ansichtslieferant\" genannt) für die Erstellung einer Coin3D Repräsentation dieser Geometrie verantwortlich ist, die in den Haupt Coin3D Szenendiagramm der 3D Ansicht eingefügt wird.

-   Die grundlegende Verzeichnisstruktur des Quellcodes ist wie folgt organisiert   *
    -   **App**   * enthält die FreeCAD Konsolen Anwendung, definiert grundlegende Strukturen und Basisklassen für Dokumentobjekte, die von Modulen zur Erstellung eigener Objekte verwendet werden.
    -   **Basis**   * enthält die Kernfunktionalität, die üblicherweise in FreeCAD verwendet wird   * 3D Vektoren, Einheiten, Matrizen, Platzierungen, etc.
    -   **Gui**   * enthält die FreeCAD GUI Modus Anwendung, definiert die 3D Ansicht, enthält viele Werkzeuge und Funktionen, die von den Arbeitsbereichen zur Interaktion mit der Schnittstelle und mit der 3D Ansicht verwendet werden können, definiert Basisklassen für Ansichtsanbieter.
    -   **Doc**   * enthält hauptsächlich eine alles in einem Qt Hilfedatei, die aus diesem Wiki generiert wurde.
    -   **Mod**   * enthält alle Module, selbst weiter getrennt in App und Gui (außer Python Module, die nicht immer so klar dieser Regel folgen).

### Verwandtes

-   [Quellcodeverwaltung](Source_code_management/de.md)
-   Das [Hauptanwenderzentrum](Power_users_hub/de.md) enthält eine Menge Dokumentation über Module, OpenCascade und Coin3D, hauptsächlich für den Python Programmierer. Da die Funktionalität jedoch ähnlich ist, sind diese Seiten auch für den C++ Programmierer von Interesse.
-   [FCStd](File_Format_FCStd.md) - Das FreeCAD-Dateiformat

[Category   *Developer Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > The FreeCAD source code/de
