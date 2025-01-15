# License/de
## In FreeCAD benutzte Lizenzen 

FreeCAD verwendet zwei verschiedene Lizenzen, eine für die Anwendung selbst und eine für die Dokumentation:

**[Lesser General Public License, Version 2 oder höher (LGPL2+)](wikipedia_LGPL.md)** Für den gesamten FreeCAD-Quellcode im [offiziellen Git-Repository](https://github.com/FreeCAD). Das + heißt, dass man FreeCAD auch wahlweise unter den Bedingungen einer neueren Version der Lizenz, wie z.B. LGPL3, einsetzen kann.

**[Creative Commons Attribution 3.0 License (CC-BY-3.0)](http://creativecommons.org/licenses/by/3.0/)** Für die [Dokumentation](https://wiki.freecad.org) und Die [Webseite](https://www.freecad.org).

Lesen Sie FreeCAD\'s [debian copyright file](https://github.com/FreeCAD/FreeCAD/blob/master/package/debian/copyright) für mehr Details über die in den verschiedenen FreeCAD-Open-Source-Komponenten angewendeten Lizenzen



## Auswirkungen der Lizenzen 

Nachfolgend eine freundlichere Erklärung dessen, was die LPGL-Lizenz für Sie bedeutet:



#### Alle Anwender 

Jeder kann **FreeCAD unentgeltlich herunterladen, benutzen und weiterverteilen**, ohne jede Beschränkung. Ihre Kopie von FreeCAD gehört wirklich Ihnen, ebenso wie die Dateien, die Sie damit erstellen. Sie werden nicht gezwungen, FreeCAD nach einer bestimmten Zeit zu aktualisieren oder Ihre Nutzung von FreeCAD zu ändern. Die Verwendung von FreeCAD bindet Sie nicht an irgendeine Art von Vertrag oder Verpflichtung. Der FreeCAD-Quellcode ist öffentlich und kann untersucht werden, so dass es möglich ist, zu überprüfen, dass er keine Dinge ohne Ihr Wissen tut, wie etwa Ihre private Daten irgendwo hin zu senden.



#### Professionelle Nutzer 

FreeCAD kann **frei für jeden Zweck genutzt werden**, sei es privat, kommerziell oder instituionell. Jede Version von FreeCAD kann in jeder Anzahl überall eingesetzt und installiert werden. Sie können FreeCAD auch ohne Einschränkung ändern oder an Ihre eigenen Zweck anpassen. Allerdings können Sie die FreeCAD-Entwickler nicht für mögliche Schäden oder geschäftliche Verluste durch die Nutzung von FreeCAD haftbar machen.



#### Open-Source-Software-Entwickler 

FreeCAD kann als eine Basis zur Entwicklung einer eigenen Anwendung genutzt oder einfach mit neuen Modulen erweitert werden. Wenn FreeCAD in Ihrer eigenen Anwendung eingebettet ist, können Sie entweder die GPL- oder LGPL-Lizenz nutzen oder jede andere, die kompatibel zur LPGL ist, um die Nutzung Ihrer Arbeit in proprietärer Software zu erlauben oder nicht. Wenn Sie ein Modul entwickeln, das als Erweiterung genutzt werden soll und keinen FreeCAD-Code enthält, dann können Sie jede beliebige Lizenz wählen. Wenn Sie allerdings möchten, dass Ihr Modul eines Tages in FreeCAD integriert wird, dann ist es eine gute Idee, dieselbe LGPL-Lizenz wie FreeCAD zu benutzen, da FreeCAD nur Code mit LPGL-, MIT- oder BSD-Lizenzen akzeptieren wird.



#### Close-Source-Software-Entwickler 

Die LPGL-Lizenz ermöglicht, FreeCAD als Komponente für eine eigene Anwendung zu nutzen, the dass man gezwungen wird, die Anwendung selbst als Open-Source veröffentlicht werden muss. Sie werden Unterstützung von den FreeCAD-Entwicklern bekommen, solange das keine \'Einbahnstraße\' ist. Die Lizenz enthält allerdings zwei wichtige Bedingungen:

1\) You must clearly **inform your users that your application is using FreeCAD** and that FreeCAD is LGPL.

2\) The LGPL license also stipulate your users must be able to swap your modified FreeCAD component with the original FreeCAD equivalent. That is would be done by dynamically linking to the FreeCAD components, so users are allowed to change it. However, this is often hard to achieve by today\'s requirements. At FreeCAD, we understand that the important point here is to not restrict the freedom given to FreeCAD users by the LGPL license. So an equivalent to dynamic linking is to offer the choice to your users, by **making your users aware of the possibility to use FreeCAD for free**. This can be done in a number of ways.

If any of the two conditions above are unacceptable to you or cannot be implemented, then you must make your FreeCAD component LGPL too and release the source code with all the modifications you made to it.

There is a special case called **derivatives**, which is when you publish basically a \"rebranded\" version of FreeCAD. Derivatives which are not open-source are prohibited by the LGPL license. The FreeCAD community is active and efficient in finding rebranded versions, reporting them to the platforms where they were found and exposing them until they are taken down.



#### Dateien

Die Modelle und andere mit FreeCAD produzierte Dateien sind weder Gegenstand einer der oben genannten Lizenzen noch an irgendeine Beschränkung oder Besitzrecht gebunden. Ihre Dateien gehören Ihnen. Sie können den Besitzer der Datei setzen und Ihre eigenen Lizenzbedingungen für die von Ihnen erstellten Dateien angeben, in FreeCAD selbst über Datei → Projektinformationen.

## Logo

The FreeCAD logo is a [trademark owned by the FPA (FreeCAD project association)](https://fpa.freecad.org/documents/Trademark.pdf). This means the [FPA](https://fpa.freecad.org) is the sole body authorized to say who has the right to use the FreeCAD logo or not. The logo files, which are part of the FreeCAD source code or available elsewhere, for example on this wiki, are still all under the same licenses as the rest of FreeCAD (LGPL for the source code and Creative Commons for this wiki). You are still free to use the FreeCAD logo anywhere, on the same terms as the rest of FreeCAD, which means, basically, that you must use it to reference FreeCAD, and not use it, for example, for your own product, or any other way that is not referencing FreeCAD.



## Erklärung des Hauptentwicklers 

Ich weiß, dass die Diskussion der **\'richtigen**\' Lizenz für Open-Source einen beträchtlichen Teil an Internet-Bandbreite belegt hatte und deshalb hier, warum - meiner Meinung nach - FreeCAD diese haben sollte.

Ich habe die [LPGL](https://de.wikipedia.org/wiki/GNU_Lesser_General_Public_License) für das Projekt gewählt und ich kenne die Vor- und Nachteile der LPGL und werde Ihnen einige Gründe für diese Entscheidung geben.

FreeCAD ist eine Mischung einer Bibliothek und einer Anwendung, so dass die [GPL](https://de.wikipedia.org/wiki/GNU_General_Public_License) ein wenig zu stark dafür wäre. Es würde das Schreiben von kommerziellen Modulen für FreeCAD verhindern, weil es die Verbindung mit den FreeCAD-Basisbibliotheken verhindern würde. Dafür ist Linux ein gutes Beispiel. Wäre Linux so erfolgreich, wenn die GNU-C-Bibliothek GPL wäre und deshalb die Verbindung mit nicht-GPL-Anwendungen verhindert? Und obwohl ich die Freiheit von Linux liebe, möchte ich auch die sehr guten NVIDIA-3D-Grafiktreiber nutzen können. Ich verstehe und akzeptiere den Grund, dass NVIDIA den Treiber-(Quell)Code nicht hergeben möchte. Wir arbeiten alle für Firmen und brauchen Bezahlung oder wenigstens Nahrung. Deshalb ist für mich die Koexistenz von Open-Source und Closed-Source keine schlechte Sache, wenn die Regeln von LGPL beachtet werden. Ich würde gerne jemand sehen, der einen Catia Import-/Export-Prozessor für FreeCAD schreibt und ihn umsonst oder gegen wenig Geld vertreibt. Ich würde ihn nicht zwingen, mehr zu geben als er bereit ist. Das wäre weder für ihn noch für FreeCAD gut.

Gleichwohl betrifft diese Entscheidung lediglich das Core-System von FreeCAD. Jeder Schreiber eines Anwendungsmoduls kann seine eigene Entscheidung treffen.


{{Quote|Jürgen Riegel|15. Oktober 2006}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > License/de
