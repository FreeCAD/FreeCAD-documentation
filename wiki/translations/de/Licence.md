# Licence/de







{{TOCright}}

## In FreeCAD benutzte Lizenzen 

FreeCAD verwendet zwei verschiedene Lizenzen, eine für die Anwendung selbst und eine für die Dokumentation:

**[Lesser General Public Licence, Version 2 oder höher (LGPL2+)](wikipedia:LGPL.md)** Für den gesamten FreeCAD-Quellcode im [offiziellen Git Repository](https://github.com/FreeCAD)

**[Creative Commons Attribution 3.0 License (CC-BY-3.0)](http://creativecommons.org/licenses/by/3.0/)** Für die Dokumentation auf <https://www.freecadweb.org>

Lesen Sie FreeCAD\'s [debian copyright file](https://github.com/FreeCAD/FreeCAD/blob/master/package/debian/copyright) für mehr Details über die in den verschiedenen FreeCAD-Open-Source-Komponenten angewendeten Lizenzen

## Auswirkungen der Lizenzen 

Nachfolgend eine freundlichere Erklärung dessen, was die LPGL-Lizenz für Sie bedeutet:

#### Alle Nutzer 

Jeder kann FreeCAD unentgeltlich herunterladen, benutzen und weiter verteilen, ohne jede Beschränkung. Ihre Kopie von FreeCAD gehört wirklich Ihnen, ebenso wie die Dateien, die Sie damit erstellen. Sie werden nicht gezwungen, FreeCAD nach einer bestimmten Zeit zu aktualisieren oder Ihre Nutzung von FreeCAD zu ändern. Die Verwendung von FreeCAD bindet Sie nicht an irgendeine Art von Vertrag oder Verpflichtung. Der FreeCAD-Quellcode ist öffentlich und kann untersucht werden, so dass es möglich ist, zu überprüfen, dass er keine Dinge ohne Ihr Wissen tut, wie etwa Ihre private Daten irgendwo hin zu senden.

#### Professionelle Nutzer 

FreeCAD kann frei für jede Art von Zweck genutzt werden, sei es privat, kommerziell oder instituionell. Jede Version von FreeCAD kann in jeder Anzahl überall eingesetzt und installiert werden. Sie können FreeCAD auch ohne Einschränkung ändern oder an Ihre eigenen Zweck anpassen. Allerdings können Sie die FreeCAD-Entwickler nicht für mögliche Schäden oder geschäftliche Verluste durch die Nutzung von FreeCAD haftbar machen.

#### Open-Source Software-Entwickler 

Sie können FreeCAD als eine Basis zur Entwicklung Ihrer eigenen Anwendung nutzen oder sie einfach mit neuen Modulen erweitern. Wenn FreeCAD in Ihrer eigenen Anwendung eingebettet ist, können Sie entweder die GPL- oder LGPL-Lizenz nutzen oder jede andere, die kompatibel zur LPGL ist, um die Nutzung Ihrer Arbeit in proprietärer Software zu erlauben oder nicht. Wenn Sie ein Modul entwickeln, das als Erweiterung genutzt werden soll und keinen FreeCAD-Code enthält, dann können Sie jede beliebige Lizenz wählen. Wenn Sie allerdings möchten, dass Ihr Modul so oft wie möglich genutzt wird, dann ist es eine gute Idee, die selbe LGPL-Lizenz wie FreeCAD zu benutzen, so dass Teile Ihres Codes einfacher in zukünftigen Modulen oder FreeCAD selbst wiederverwendet werden können.

#### Close-Source Software-Entwickler 

Sie können FreeCAD als Basis für Ihre eigene Anwendung nutzen und sind nicht gezwungen, Ihre Anwendung zu Open-Source zu machen. Die LGPL verlangt allerdings zwei grundlegende Dinge: 1) dass Sie Ihre Benutzer deutlich darüber informieren, dass Ihre Anwendung FreeCAD benutzt und dass FreeCAD die LGPL-Lizenz verwendet, und 2) dass Sie Ihre Anwendung deutlich von den FreeCAD-Komponenten trennen. Das passiert normalerweise durch dynamisches Linken an die FreeCAD-Komponenten, so dass es den Benutzern erlaubt ist, das zu ändern, oder dadurch, den Benutzern den FreeCAD-Code mitsamt der von Ihnen durchgeführten Änderungen zur Verfügung zu stellen. Sie werden Unterstützung von den FreeCAD-Entwicklern bekommen, solange das keine \'Einbahnstraße\' ist.

#### Dateien

Die Modelle und andere mit FreeCAD produzierte Dateien sind weder Gegenstand einer der oben genannten Lizenzen noch an irgendeine Beschränkung oder Besitzrecht gebunden. Ihre Dateien gehören Ihnen. Sie können den Besitzer der Datei setzen und Ihre eigenen Lizenzbedingungen für die von Ihnen erstellten Dateien angeben, in FreeCAD selbst über Datei → Projektinformationen.

## Erklärung des Hauptentwicklers 

Ich weiß, dass die Diskussion der **\'richtigen**\' Lizenz für Open-Source einen beträchtlichen Teil an Internet-Bandbreite belegt hatte und deshalb hier, warum - meiner Meinung nach - FreeCAD diese haben sollte.

Ich habe die [LPGL](https://de.wikipedia.org/wiki/GNU_Lesser_General_Public_License) für das Projekt gewählt und ich kenne die Vor- und Nachteile der LPGL und werde Ihnen einige Gründe für diese Entscheidung geben.

FreeCAD ist eine Mischung einer Bibliothek und einer Anwendung, so dass die [GPL](https://de.wikipedia.org/wiki/GNU_General_Public_License) ein wenig zu stark dafür wäre. Es würde das Schreiben von kommerziellen Modulen für FreeCAD verhindern, weil es die Verbindung mit den FreeCAD-Basisbibliotheken verhindern würde. Dafür ist Linux ein gutes Beispiel. Wäre Linux so erfolgreich, wenn die GNU-C-Bibliothek GPL wäre und deshalb die Verbindung mit nicht-GPL-Anwendungen verhindert? Und obwohl ich die Freiheit von Linux liebe, möchte ich auch die sehr guten NVIDIA-3D-Grafiktreiber nutzen können. Ich verstehe und akzeptiere den Grund, dass NVIDIA den Treiber-(Quell)Code nicht hergeben möchte. Wir arbeiten alle für Firmen und brauchen Bezahlung oder wenigstens Nahrung. Deshalb ist für mich die Koexistenz von Open-Source und Closed-Source keine schlechte Sache, wenn die Regeln von LGPL beachtet werden. Ich würde gerne jemand sehen, der einen Catia Import-/Export-Prozessor für FreeCAD schreibt und ihn umsonst oder gegen wenig Geld vertreibt. Ich würde ihn nicht zwingen, mehr zu geben als er bereit ist. Das wäre weder für ihn noch für FreeCAD gut.

Gleichwohl betrifft diese Entscheidung lediglich das Core-System von FreeCAD. Jeder Schreiber eines Anwendungsmoduls kann seine eigene Entscheidung treffen.


{{Quote|Jürgen Riegel|15. Oktober 2006}}





 

[Category:Developer Documentation](Category:Developer_Documentation.md)
