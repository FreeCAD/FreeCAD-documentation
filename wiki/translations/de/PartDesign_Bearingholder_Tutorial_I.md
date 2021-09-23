# PartDesign Bearingholder Tutorial I/de




{{TutorialInfo/de
|Topic=Modellierung
|Level=Erfahrene Anwender
|Author=NormanC
|FCVersion=0.19.23300 oder höher
}}


**Dieses Tutorium wurde ursprünglich für eine inzwischen veraltete Entwicklungsversion von FreeCAD geschrieben. Dieses Tutorium muss komplett neu geschrieben werden, um es an die Änderungen im PartDesign anzupassen, die in der kommenden Version 0.17 vorgenommen werden. Das Neuschreiben wurde in [NormandC](Sandbox:PartDesign_Bearingholder_Tutorial_I]]_begonnen. Wenn du teilnehmen möchtest, schreibe bitte einen Beitrag im Wiki Bereich des [http://forum.freecadweb.org Forum]. - [[Benutzer:Normandc.md)**

![Lagergehäuse Tutorium - Fertiges Lagergehäuse (oben)\|thumb\|right\|400px](images/HolderTop1-1.jpg )

~~Wie der Warnhinweis oben auf der Seite bereits andeutet, funktioniert dieses **Tutorium NICHT, es sei denn, du kompilierst einen speziellen, sehr experimentellen Zweig aus dem FreeCAD Quellcode** und ist ein einführendes Tutorium zur Modellierung mit dem PartDesign Arbeitsbereich in FreeCAD **unter Verwendung von Datumsebenen, die in den meisten FreeCAD Versionen noch nicht vorhanden sind**.~~

## Kurze Zweckbestimmung 

Der Zweck des Tutoriums ist es, dich in zwei verschiedene Arbeitsabläufe zur Erstellung eines Gussteils mit Entwürfen und Verrundungen einzuführen. Je nachdem, welche anderen CAD-Programme du bisher verwendet hast, könnte dir das eine oder das andere vertraut sein. Als Arbeitsbeispiel werden wir ein einfaches Lagergehäuse modellieren.

Dies ist der erste Teil des Tutoriums. Es wird der so genannte \"Ein Körper\" Arbeitsablauf verwendet, wobei der (einfachere) obere Teil des Gehäuses als Beispiel dient.

Um dieses Tutorium durcharbeiten zu können musst du offensichtlich den PartDesign Arbeitsbereich aktivieren.

~~Du findest meine Version des von diesem Tutorium erstellten Teils [http://ubuntuone.com/5gok0J4dye3Fo4BKWMGWVa hier](http://ubuntuone.com/5gok0J4dye3Fo4BKWMGWVa_hier.md).~~ *Die Datei ist nicht mehr verfügbar, eine neue wird zu einem späteren Zeitpunkt bereitgestellt werden*.

## Konstruktionsdaten

Das Gehäuse sollte in der Lage sein, ein Lager mit einem Durchmesser von 90 mm und einer Breite von bis zu 33 mm aufzunehmen (z.B. DIN 630 Typ 2308). Das Lager erfordert eine Schulterhöhe von mindestens 4,5 mm im Halter (und auf der Welle). Der obere Teil des Halters wird mit zwei 12mm Schrauben an der Unterseite verschraubt. Auf beiden Seiten des Lagers sollte eine Nut vorhanden sein, die einen Standard Wellendichtring DIN 3760 aufnehmen kann: 38x55x7 oder 40x55x7 auf der einen Seite, 50x68x8 auf der anderen Seite.

Das Gehäuse wird ein Sandguss mit einer Mindestwandstärke von 5 mm, einem Entformungswinkel von 2 Grad und einem minimalen Verrundungsradius von 3 mm sein.

== Einrichten der Skelettgeometrie ==

![Lagergehäuse mit den beiden wichtigsten Skelettebenen\|thumb\|right\|text-top\|400px](images/HolderTop1-2.jpg )

Die Idee der Skelettgeometrie besteht darin, die grundlegenden Konstruktionsabmessungen in einem einzigen Bezugselement (z.B. einer Ebene oder einer Achse) zu erfassen. Wenn sich die Konstruktionsbemaßung ändert, muss nur das Skelettelement geändert werden. Wenn das Modell gut aufgebaut ist, werden alle seine Formelemente neu berechnet, um die Konstruktionsänderung widerzuspiegeln. Dadurch wird die Gefahr verringert, dass du in einem komplexen Modell, in dem die grundlegenden Konstruktionsbemaßungen an mehreren Stellen verwendet werden, vergisst, sie irgendwo zu ändern.

Die Alternative zur Skelettgeometrie besteht darin, eine Tabelle mit den grundlegenden Bemaßungen des Entwurfs zu haben, die jeder Bemaßung einen symbolischen Namen zuweist, und dann den symbolischen Namen überall dort zu verwenden, wo die Bemaßung für den Bau des Modells erforderlich ist. FreeCAD erlaubt diesen Ansatz noch nicht.

![Basisebenen und alle Bezugsebenen\|thumb\|right\|text-top\|400px](images/HolderTop1-3.jpg )

Für den Fall des Lagergehäusese sind die beiden wichtigsten Konstruktionsmaße der Abstand zwischen den Schrauben (was die Größe des einsetzbaren Lagers begrenzt) und die Höhe der Schraubenköpfe. Die gewählten Abmessungen sind

-   Abstand zwischen den Schrauben: Radius des Lagers (45) + Wanddicke (5) plus Radius der Bohrung für den Schrauben ( 7 ) = 57 mm, so dass die vertikale Ebene um 57 mm von der YZ Ebene versetzt ist. Um diese Bezugsebene zu erzeugen, wähle die YZ Ebene und wähle dann eine neue Bezugsebene. Gib den Versatz in den Dialog ein, der sich öffnet
-   Höhe der Schraubenköpfe: Dies wurde als ein Versatz von 28 mm von der XZ Ebene gewählt.

Der Einfachheit halber können zwei weitere Bezugsebenen erstellt werden, die die Materialmenge widerspiegeln, die von den Seiten des Lagergehäuses weggeschnitten werden muss. Sie sind um +22 und -22 von der XY-Ebene versetzt.

Es ist ratsam, der Skelettgeometrie klare Namen zu geben. Meistens wirst du die Sichtbarkeit für Bezugsebenen ausschalten wollen, weil sie den Bildschirm überladen, und wenn die Ebenen selbsterklärende Namen haben, kannst du sie einfach nach Namen statt nach dem Bildschirm auswählen.

## Die Volumenkörpergeometrie 

<img alt="Skizze des ersten Blocks" src=images/HolderTop1-4.jpg  style="width:400px;"> Jetzt ist es an der Zeit, mit der Erstellung einer echten Geometrie zu beginnen. Die Skizze für den ersten Block ist auf der rechten Seite abgebildet. Er wird auf der XY Ebene platziert. Es gibt nur drei Dimensionen: Der Innenradius (22,5 mm), die Bearbeitungszugabe (3 mm) an der Basis als Versatz zur XZ Ebene und der Abstand von der Bezugsebene, die die Schraubenachse darstellt (7 mm). Das bedeutet, wenn du später die Bezugsebene verschiebst, passt der Block automatisch seinen Außenradius an. Denke daran, dass du die Bezugsebene, bevor du sie zur Bemaßung verwenden kannst, als Außengeometrie in den Skizzierer einfügen musst.

Du fragst dich wahrscheinlich, warum sich am Ende jedes Bogens ein kleines gerades Segment befindet. Dieses Segment sorgt dafür, dass auf den Bögen ein Entwurfswinkel von 2 Grad entsteht. Das mag nach viel Arbeit für einen sehr kleinen Nutzen aussehen, aber viele CAD Programme (und vielleicht eines Tages auch FreeCAD) haben Werkzeuge, die ein Volumenmodell in verschiedenen Farben hervorheben und dir sofort alle Flächen anzeigt, bei denen der Entwurfswinkel nicht korrekt ist. Du willst doch nicht, dass das mit deinem Modell passiert, besonders nachdem du viele Verrundungen angebracht hast!

Wenn du die Skizze erstellt hast (was wegen der 2-Grad-Tangentiallinien etwas knifflig ist), polstere sie einfach symmetrisch zur Skizzierebene mit einer Länge von 62 mm auf: 34 mm für das Lager, 2x 9 mm für die Dichtungsringe, 2x 5 mm für die Wandstärke.
<img alt="Skizze des Ausschnitts an der Seite des Blocks" src=images/HolderTop1-5.jpg  style="width:400px;"> Als nächstes wollen wir an den Stellen, an denen sich die Dichtungsringe befinden, etwas Material wegschneiden, da ihr Außendurchmesser viel kleiner ist als der des Lagers. Der einfachste Weg, die Skizzen zu erstellen, besteht darin, die Skizze des Blocks auszuwählen und dann \"Auswahl duplizieren\" aus dem Bearbeitungsmenü zu wählen. Du kannst dann die Skizze auf die Seite des Blocks umordnen und sie wie im Bild gezeigt modifizieren.

Die beiden einzigen wichtigen Maße in der Skizze sind 3 mm Bearbeitungszugabe am Boden und ein Innendurchmesser von 78 mm: 68 mm für den Außendurchmesser des Dichtrings + 2x 5 mm Wandstärke. Da der Dichtring auf der anderen Seite nur einen Durchmesser von 55 mm haben wird, kann der Ausschnitt hier 65 mm betragen.

Nachdem du die Skizze erstellt hast, koffere sie bis zu der Bezugsebene aus, die die Lagerseite plus 5 mm Wandstärke markiert. Wenn du den Halter modifizieren möchtest, um breitere Lager aufnehmen zu können, musst du nur die Abmessungen dieser Bezugsebenen ändern, und die Ausschnitttiefe folgt dementsprechend.
<img alt="Skizze des Ausschnitts im Inneren des Blocks" src=images/HolderTop1-6.jpg  style="width:400px;"> Um den Bearbeitungsaufwand zu reduzieren, wollen wir auch etwas Material im Inneren des Halters wegschneiden. Auch hier ist es praktisch, die Skizze des ersten Polsters zu duplizieren. Es muss noch nicht einmal nachgebildet werden. Auch hier sind die einzigen wichtigen Abmessungen die Bearbeitungszugabe (3 mm) und die Außendurchmesser: 84 mm für die Stelle, an der sich das Lager befinden wird (90 mm - 2x Bearbeitungszugabe), 49 mm für den kleineren Dichtring (55 mm - 2x 3 mm) und 62 mm für den größeren Dichtring.

Nachdem du die Skizzen erstellt hast, koffere sie aus: Symetrisch 28mm für den Lagerausschnitt (34mm - 2x Bearbeitungszugabe) und einseitig 23mm für die Ausschnitte für die Dichtringe: 34 mm / 2 für die halbe Lagerbreite + 9 mm für die Dichtringe - 3 mm Bearbeitungszugabe.
<img alt="Hauptgeometrie des Gehäuses oben" src=images/HolderTop1-7.jpg  style="width:400px;"> Dein Teil sollte nun wie auf dem Bild rechts aussehen. Beachte, wie die verschiedenen Ausschnitte zusammen eine fast gleichmäßige Wandstärke ergeben, wodurch das Gießen einfacher und porenärmer wird.
<img alt="Skizze mit Entwurf, wo die Schrauben sein werden" src=images/HolderTop1-8.jpg  style="width:400px;"> Jetzt muss nur noch etwas Material für die Schrauben hergestellt werden, damit sie durchgehen können. Du kannst versucht sein, diese als Kreis zu skizzieren und sie dann aufzufüllen, aber das wird Ihnen Schwierigkeiten bereiten, wenn du später versuchst, den Entwurf darauf zu setzen (ich nehme an, das ist eine Schwäche von OpenCascade). Um die Probleme zu umgehen, ist es also besser, eine Skizze mit dem eingeschlossenen Entwurfswinkel zu erstellen und diese dann um 360 Grad zu drehen.

Auch hier kommen wieder die Skelettebenen zum Einsatz. Als Außengeometrie benötigst du die Schraubenachsenebene und die Schraubenkopfebene. Erstelle dann eine gerade Linie für die Rotationsachse und stelle sicher, dass sie an die Schraubenachsenebenen Referenz gebunden ist. Schalte sie als Konstruktionsgeometrie ein. Skizziere dann den Rest der Kontur. Die wichtigen Maße sind die Bearbeitungszugabe oben und unten und der Radius von 12 mm: 7 mm für den Lochradius + 5 mm Wandstärke.
<img alt="Fertige Geometrie der Gehäuseoberseite (ohne Entwurf und Verrundungen)" src=images/HolderTop1-9.jpg  style="width:400px;"> Erstelle ein Rotations Formelement von der Skizze und spiegle es dann auf der YZ Ebene. Dies ist die gesamte Volumenkörpergeometrie, die wir zum Modellieren benötigen. Der Rest sind Entwurf und Verrundungen.

## Anwenden des Entwurfs auf die Seitenflächen 

<img alt="Die neutrale Ebene für die Erstellung von Entwürfen" src=images/HolderTop1-10.jpg  style="width:400px;"> Der nächste Schritt ist die Anwendung von Entwürfen auf alle Seiten. Dabei ist es wichtig, die Lage der neutralen Ebene zu berücksichtigen, d.h. der Ebene, um die die Fläche \"gedreht\" wird. Wenn wir als neutrale Ebene die Unterseite des Gehäuses wählen, dann haben wir ein Problem mit der Wandstärke im oberen Teil des Halters. Daher erstellen wir eine Bezugsebene mit einem Versatz von 40 mm von der XZ Ebene als Kompromiss zwischen der Oberseite des Halters, die zu dünn und der Unterseite, die zu breit wird.
<img alt="Anwenden des Entwurfs auf die Seitenflächen des Gehäuses" src=images/HolderTop1-11.jpg  style="width:400px;"> Um einen Entwurf auf eine Fläche zu legen, wähle diese Fläche aus und erstelle das Entwurf Formelement. Du kannst dann weitere Flächen auswählen, auf die der Entwurf angewendet werden soll. Wenn du ein großes Teil hast, ist es ratsam, jeweils nur eine Fläche zu entwerfen. Das bedeutet, dass wenn du die Geometrie änderst und ein Entwurf fehlschlägt, nur dieses eine Formelement fehlschlägt, wohingegen, wenn du alle Flächen in ein Entwurfs Formelement setzt, das gesamte Formelement fehlschlagen kann, weil eine Fläche fehlschlägt. Für ein kleines Teil wie das Lagergehäuse reicht es aus, zwei Entwurf Formelemente zu erzeugen: Eines für die vier Außenflächen und eines für die Innenflächen.

Der Dialog zwingt dich, vor dem Abschluss eine neutrale Ebene auszuwählen. Du kannst die Zugrichtung leer lassen, in diesem Fall ist sie normal zur neutralen Ebene. Vergiss nicht, den Entwurfswinkel auf 2 Grad einzustellen.

## Verrundung des Gehäuses 

<img alt="Ausrundung, wo die Schrauben hinkommen" src=images/HolderTop1-13.jpg  style="width:400px;"> Wir können das Teil nun verrunden. Das Bild zeigt den ersten Satz Verrundungen. Beginne mit den kleinen kreisförmigen Verrundungen und mache sie mit einem Radius von 4 mm. Obwohl 3 mm laut Spezifikation des Teils ausreichen würden, bedeutet ein Radius von 4 mm, dass nach der Bearbeitung 1 mm der Verrundung übrig bleibt, wodurch die durch die Bearbeitung erzeugte scharfe Kante reduziert wird. Die großen Verrundungen haben einen Radius von 6 mm, um die Verteilung der Kraft von den Schrauben auf den Rest des Teils zu erleichtern. Es wäre schön, diesen Radius noch größer zu machen, aber leider kann OpenCascade noch nicht mit überlappenden Verrundungen umgehen.

Wie bei Entwürfen solltest du in einem komplexen Teil nur eine Kante auf einmal verrunden, um unnötige Fehler zu vermeiden, wenn sich die Grundgeometrie ändert.
<img alt="Verrundung der Außenseite des Gehäuses" src=images/HolderTop1-12.jpg  style="width:400px;"> Die restlichen Verrundungen haben einfach 3mm Radius. Wenn man sich das Bild rechts anschaut, könnten die beiden hervorgehobenen Verrundungen tatsächlich mit 5 mm verrundet werden, um eine gleichmäßigere Wandstärke für das Gussteil zu erreichen. Nach der Bearbeitung würde die Mindestwandstärke von 5 mm immer noch eingehalten werden. Aber auch hier hindert uns die Tatsache, dass OpenCascade keine überlappenden Verrundungen verarbeiten kann, daran, dies für die innere der beiden hervorgehobenen Verrundungen zu tun.
<img alt="Verrundung der Innenseite des Gehäuses - problematische Kante" src=images/HolderTop1-14.jpg  style="width:400px;"> Das Ausfüllen der Innenseite des Teils stellt uns vor eine Schwierigkeit, die mit den aktuellen Werkzeugen im PartDesign Arbeitsbereich nicht gelöst werden kann. Die hervorgehobene Kante kann überhaupt nicht verrundet werden, wiederum weil sich die Runden überlappen würden. Dies könnte umgangen werden, indem eine Austragung anstelle einer Verrundung erstellt wird, mit der Ausnahme, dass Austragungen in PartDesign noch nicht implementiert sind. Vorläufig sind wir gezwungen, die Kante so zu belassen, wie sie ist.
<img alt="Das verrundeten Teil (mit Ausnahme der unmöglichen Kante)" src=images/HolderTop1-15.jpg  style="width:400px;"> Das Bild rechts zeigt das fertige Teil in dem Zustand, in dem es sich vor der Bearbeitung befinden wird (mit Ausnahme der einen Kante, die nicht verrundet werden kann). Du wirst feststellen, dass eine Kante, die um das gesamte Teil herum verläuft, absichtlich nicht ausgefüllt wurde. Dies ist die Kante, an der sich die Unterseite und die Oberseite der Form treffen. Hier ist keine Verrundung möglich (und wird auch nicht benötigt).

## Spanende Bearbeitung 

<img alt="Spanende Bearbeitung der Ober- und Unterseite des Gehäuses" src=images/HolderTop1-16.jpg  style="width:400px;"> <img alt="Spanende Bearbeitung der Innenseite des Lagergehäuses" src=images/HolderTop1-17.jpg  style="width:400px;"> Jetzt können wir das zu bearbeitende Material vom rohen Gussteil wegschneiden. Dies ist sehr einfach, wenn die Skelettgeometrie definiert ist. Die Idee besteht darin, alle Bearbeitungsmerkmale (Taschen und Nuten) nur mit Bezugsformelementen zu erzeugen. Das bedeutet, dass sie völlig unabhängig von der Volumengeometrie des Lagergehäuses sind, was uns einige große Vorteile bringt:

-   Unabhängig davon, wie du die Volumenkörpergeometrie änderst, können die Formelemente für die Bearbeitung nie versagen.
-   Du kannst die Bearbeitungsgeometrie vor der Fertigstellung des Solids erstellen, was dir eine nützliche visuelle Rückmeldung gibt.
-   Wenn du die Bezugsebenen des Skeletts verschiebst, passen sich sowohl die Volumenkörpergeometrie als auch die Bearbeitung automatisch an.
-   Wenn du einen Fehler in deiner Festkörpergeometrie machst, ist die Bearbeitung immer noch in der richtigen Position, und sehr wahrscheinlich wird der Fehler deutlich sichtbar (z.B. eine Wandstärke von 2 mm statt 5 mm). Wenn du dagegen die Bearbeitung auf die Festkörpergeometrie beziehst, wird sie sich an den Fehler im Festkörper anpassen und z.B. die 5mm Wandstärke beibehalten, nur an der falschen Stelle, an der sich der Festkörper befindet.

Bevor auf der Bearbeitungsgeometrie begonnen wird, möchte ich einen Bezugspunkt im Baum platzieren und ihm einen Namen geben, etwa \"Bearbeitung\_beginnt\_hier\". Dies ist nützlich, wenn du zwischen dem Roh- und dem Bearbeitungszustand des Werkstücks wechseln möchtest, da du auf einen Blick siehst, wohin du den Einfügepunkt verschieben musst, um den Rohzustand zu erhalten.

Um die Unterseite des Gehäuses zu bearbeiten, skizziere einfach ein großes Rechteck auf der XZ Ebene und koffere es aus. Für die Oberseite skizziere einen Kreis auf der Bezugsebene, der die Position des Schraubenkopfes definiert, und spiegle dann die Tasche auf der YZ Ebene. Auf die gleiche Weise erzeugst du eine Tasche für die Bohrung, durch die die Schraube hindurchgehen soll, und spiegeln diese. Um die Innenseite des Gehäuses zu bearbeiten, erstelle eine Skizze auf der YZ Ebene und nute sie ein.
<img alt="Fertiges Teil" src=images/HolderTop1-1.jpg  style="width:400px;"> Nachdem du die Bearbeitung durchgeführt hast, kannst du einen schönen visuellen Effekt erzielen, indem du alle bearbeiteten Flächen einfärbst, so dass du auf einen Blick erkennen kannst, welche Teile roh gegossen und welche nach dem Gießen bearbeitet werden.

## Schlussbemerkungen

Wir haben die Oberseite des Lagergehäuses mit den Abmessungen modelliert, die er nach dem Gießen haben wird. Um die Gussform zu erstellen, musst du dein Teil schrumpfen lassen, denn nach dem Gießen, wenn das heiße Metall abkühlt, wird es um einige Prozent schrumpfen (je nach Material). In der Regel ist es am besten, die Anwendung der Schrumpfung der Gießerei zu überlassen, die das Teil herstellt, da sie über die erforderlichen Spezialkenntnisse verfügt. Du solltest Ihnen auch sagen, ob dein Teil problematische Bereiche aufweist, z.B. sehr dicke Wände, die sich plötzlich mit sehr dünnen Abschnitten verbinden, ohne dass dazwischen ein richtig verjüngter Abschnitt liegt.

## Teil Zwei 

[PartDesign Lagergehäuse Tutorium II](PartDesign_Bearingholder_Tutorial_II/de.md)



[Category:Tutorials](Category:Tutorials.md)
