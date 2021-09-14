# PartDesign Bearingholder Tutorial II/de





{{TutorialInfo
|Topic=Modeling
|Level=Experienced User
|Author=NormandC
|Time=
|FCVersion=0.19.23300 or higher
|Files=
}}


{{VeryImportantMessage|Dieses Tutorial wurde ursprünglich für eine inzwischen veraltete Entwicklungsversion von FreeCAD geschrieben. Seit April 2016 sind diese Funktionen in die Vorentwicklungsversion 0.17 integriert, die [https://github.com/FreeCAD/FreeCAD/releases/tag/0.17_pre hier] verfügbar ist.
<br />
Bitte beachte, dass sich diese Version von FreeCAD noch in einem frühen Entwicklungsstadium befindet. Außerdem muss dieses Tutorium möglicherweise aktualisiert werden. Wenn du an der Überprüfung und Aktualisierung teilnehmen möchtest, poste bitte in den Wiki Abschnitt des [http://forum.freecadweb.org forum].}}

![Lagergehäuse Tutorium - Fertiges Lagergehäuse (oben)\|thumb\|right\|400px](images/HolderTop2-19.jpg )


<div class="mw-translate-fuzzy">

Wie der Warnhinweis oben auf der Seite bereits andeutet, funktioniert dieses **Tutorial NICHT, es sei denn, du kompilierst einen speziellen, sehr experimentellen Zweig aus dem FreeCAD Quellcode** und ist ein einführendes Tutorial zur Modellierung mit dem PartDesign Arbeitsbereich in FreeCAD **unter Verwendung von Datumsebenen, die in den meisten FreeCAD Versionen noch nicht vorhanden sind**. Der Zweck des Tutoriums ist es, dich in zwei verschiedene Arbeitsabläufe zur Erstellung eines Gussteils mit Entwürfen und Verrundungen einzuführen. Je nachdem, welche anderen CAD Programme du bisher verwendet hast, könnte dir das eine oder das andere vertraut sein. Als Arbeitsbeispiel werden wir ein einfaches Lagergehäuse modellieren.


</div>

## Purpose in Brief 

The purpose of the tutorial is to introduce you to two different work flows for creating a cast part with drafts and fillets. Depending on what other CAD programs you have been using, one or the other might be familiar to you. As a working example we will be modeling a simple bearing holder.

Dies ist der zweite Teil des Tutoriums. Es wird der so genannte \"Multikörper\" Arbeitsablauf verwendet, wobei der (einfachere) obere Teil des Gehäuses als Beispiel dient.

Selbstverständlich musst du zum Durcharbeiten dieses Tutorials den PartDesign Arbeitsbereich aktivieren.

~~Du findest meine Version des von diesem Tutorium erstellten Teils [http://ubuntuone.com/39PTZ3Y3LUnmZzpZQPcJT4 hier](http://ubuntuone.com/39PTZ3Y3LUnmZzpZQPcJT4_hier.md).~~ *Die Datei ist nicht mehr verfügbar, eine neue wird zu einem späteren Zeitpunkt bereitgestellt werden*.

## Konstruktionsdaten

Das Gehäuse sollte in der Lage sein, ein Lager mit einem Durchmesser von 90 mm und einer Breite von bis zu 33 mm aufzunehmen (z.B. DIN 630 Typ 2308 mit einem Innendurchmesser von 40 mm). Das Lager erfordert eine Schulterhöhe von mindestens 4,5 mm im Halter (und auf der Welle). Der obere Teil des Gehäuses wird mit zwei 12mm Schrauben an der Unterseite verschraubt. Der Kopf einer solchen Schraube benötigt einen Freiraum von mindestens 20 mm Durchmesser. Auf beiden Seiten des Lagers sollte eine Nut vorhanden sein, die einen Standard-Wellendichtring DIN 3760 aufnehmen kann: 38x55x7 oder 40x55x7 auf der einen Seite, 50x68x8 auf der anderen Seite.

Das Gehäuse wird ein Sandguss mit einer Mindestwandstärke von 5 mm, einem Entformungswinkel von 2 Grad und einem minimalen Verrundungsradius von 3 mm sein.

## Einrichten der Skelettgeometrie 

![Skizze der Skelettgeometrie\|thumb\|right\|400px](images/HolderTop2-2.png ) Erstelle im PartDesign Arbeitsbereich ein neues Teil. Benenne den standardmäßig erstellten Körper in Skeleton um. Dieser Körper ist wahrscheinlich bereits aktiviert, was du an der blauen Hintergrundfarbe im Formelementebaum erkennen kannst. Erstelle eine neue Skizze auf der YZ Ebene, die den Umriss der Welle, des Lagers und der Dichtungsringe enthält. Nachdem du die Skizze fertiggestellt hast, erstelle daraus ein Rotations Formelement. Dieses Skelettformelement wird später dazu verwendet, die reale Geometrie darauf zu beziehen. Das bedeutet, dass du, wenn du irgendwelche Bemaßungen ändern möchtest, nur die Bemaßungen des Skelettformelements anpassen musst, und der Rest des Teils wird entsprechend aktualisiert. ![Die Skelettgeometrie\|thumb\|right\|400px](images/HolderTop2-2-1.jpg )

## Der Hauptkörper 

![Skizze des ersten Polsters\|thumb\|right\|400px](images/HolderTop2-3.jpg ) Erstelle einen neuen Körper und mache ihn aktiv. Die Skizze für den ersten Block ist rechts abgebildet. Er wird auf einer Bezugsebene mit einem Versatz von 5 mm (Wandstärke) von der Skelettfläche platziert, die die Seite eines der tragenden Dichtungsringe markiert. Da alle wichtigen Maße vom Skelett abgenommen werden, gibt es nur drei Maße: Die Bearbeitungszugabe (3 mm) an der Basis als Versatz zur XY Ebene, die 5 mm Wanddicke vom Außendurchmesser des Skeletts und der Entformungswinkel von zwei Grad. Zwei erzeugen die 5mm Bemaßung, du musst zuerst den Außenkreis (Radius 45mm) der Skelettgeometrie als Außengeometrie im Skizzierer auswählen und dann eine tangential zu diesem Kreis und in einem Winkel von zwei Grad gebundene Konstruktionslinie einfügen.

Du fragst dich wahrscheinlich, warum sich am unteren Ende jedes Bogens dieses kleine gerade Segment befindet. Dieses Segment sorgt dafür, dass auf den Bögen ein Entformungswinkel von 2 Grad entsteht. Das mag nach viel Arbeit für einen sehr kleinen Nutzen aussehen, aber viele CAD Programme (und vielleicht eines Tages auch FreeCAD) haben Werkzeuge, die ein Volumenmodell in verschiedenen Farben hervorheben und dir sofort alle Flächen anzeigt, bei denen der Entformungswinkel nicht korrekt ist. Du willst nicht, dass das mit deinem Modell passiert, besonders nachdem du viele Verrundungen angebracht hast!
![Das erste Polster\|thumb\|right\|400px](images/HolderTop2-4.jpg ) Wenn du die Skizze angefertigt hast (was wegen der 2 Grad Tangentiallinien etwas knifflig ist), erstelle daraus ein Polster, das sich bis zur anderen Seite der Skelettgeometrie erstreckt, wiederum mit einem Versatz von 5 mm zur Seitenfläche. du brauchst diesmal keine Bezugsebene zu erzeugen, der \"bis zur Fläche\" Modus des Polster Dialogs bietet die Eingabe eines Versatzes an.
![Skizze für Polsterausschnitt\|thumb\|right\|400px](images/HolderTop2-5.jpg ) Als Nächstes werden wir an beiden Enden des Polsters etwas Material wegschneiden, da es für Gussteile immer ideal ist, eine möglichst gleichmäßige Wandstärke zu haben. Erstelle eine Skizze auf jeder der Stirnseiten des Polsters und bemaße sie um 5 mm versetzt zu dem Kreis, der den Lagerdichtring darstellt (Radius 27,5 mm auf der einen Seite und 34 mm auf der anderen). Erstelle für das untere Liniensegment der Skizze eine weitere externe Geometrie vom Polster und binde diese an das Polster. So hat die Skizze nur ein einziges Maß, die 5 mm Wandstärke (die Maße 150 mm und 75 mm sind nicht wichtig, solange sie groß genug sind, um sicherzustellen, dass alles weggeschnitten wird).
![Das Polster mit Ausschnitten zur Erzielung einer gleichmäßigen Wandstärke\|thumb\|right\|400px](images/HolderTop2-6.jpg ) Erstelle mit der von dir erstellten Skizze eine Tasche und erweitere diese auf die Fläche der Skelettgeometrie, die das Lager darstellt, minus 5 mm Versatz für die Wanddicke. Für die zweite Tasche kannst du die Option \"Ausgewähltes Objekt duplizieren\" aus dem Menü Bearbeiten verwenden, um die bereits erstellte Skizze zu duplizieren (wähle, dass abhängige Objekte nicht dupliziert werden sollen, wenn die Frage auftaucht). Wähle dann die Fläche aus, auf die du diese Skizze verschieben möchtest, und weise FreeCAD an, die Skizze auf diese Fläche abzubilden (dies ist ein Punkt im Menü \"PartDesign\"). Nachdem du die zweite Tasche erstellt hast, kannst du das Ergebnis von unten betrachten, um zu prüfen, ob du eine einheitliche Wandstärke von 5 mm um die Kontur der Skelettgeometrie herum haben.
![Neutrale Ebene für die Anwendung des Entwurfs\|thumb\|right\|400px](images/HolderTop2-7.jpg ) Jetzt ist es an der Zeit, Entwurf und Verrundungen zu erstellen. Das Entwurfsformelement erfordert eine neutrale Ebene, was bedeutet, dass die Geometrie, die von dieser Ebene geschnitten wird, an ihrem Platz bleibt, während der Rest der Fläche um den Entformungswinkel geneigt wird. Die Verwendung der Unterseite des Polsters für diesen Zweck ist keine gute Idee, da die Wandstärke im oberen Teil des Halters weniger als 5 mm betragen würde. Wir erstellen also zu diesem Zweck eine Bezugsebene, die um etwa 35 mm vom XY versetzt ist. Aktiviere den Skelettkörper und erzeuge die Ebene dort, denn wir werden sie brauchen, um den Entwurf auch auf andere Körper anzuwenden.
![Erster Körper mit Entwurf und Verrundungen\|thumb\|right\|400px](images/HolderTop2-8.jpg ) Das Bild rechts zeigt den fertigen ersten Körper mit Entwurf und applizierten Verrundungen. Beachte, dass die äusseren (konkaven) Kanten einen grösseren Verrundungsradius von 5mm haben, wiederum mit dem Ziel, eine gleichmässigere Wandstärke zu erzeugen (mehr als 5mm ist nicht möglich, da dann nach der Bearbeitung der Innenseite des Halters die Wandstärke weniger als 5mm betragen würde).

## Hinzufügen der Körper für die Schrauben 

![Die Skizze für den Körper für die Schrauben\|thumb\|right\|400px](images/HolderTop2-13.jpg ) Die Schrauben benötigen zwei zylindrische Körper auf beiden Seiten des Hauptkörpers. Am besten ist es, den 2 Grad Entformungswinkel in die Skizze aufzunehmen. Ich habe versucht, einen Zylinder zu drehen und später einen Entwurf anzuwenden, aber nach dem Spiegeln passierten seltsame Dinge, und ich konnte keine Verrundungen anbringen, weil die Oberfläche irgendwie verzogen war.

Die Skizze ist so bemaßt, dass die Rotationsachse 12 mm Abstand zum Außendurchmesser des Skelettkörpers hat, 7 mm für den Radius der Bohrung plus 5 mm für die Wanddicke. Um ein vollparametrisches Teil zu erhalten, ist es eine gute Idee, dem Skelett eine Ebene etwa 25 mm über der XY Ebene hinzuzufügen, um die Oberseite der Zylinder zu markieren. Da dies bearbeitet werden soll, wird die Skizze 3mm darüber bemaßt.

![Der Körper für die Schrauben\|thumb\|right\|400px](images/HolderTop2-14.jpg ) Erstelle aus der Skizze eine Drehung und bringe an der Oberseite eine Verrundung von 4 mm an. Das bedeutet, dass nach dem Wegfräsen von 3 mm ein leichter Radius verbleibt, der hilft, eine scharfe Kante zu vermeiden, an der sich jemand beim Anziehen der Schraube in die Hand schneiden könnte.
![Der Hauptkörper mit den beiden Körpern für die Schrauben\|thumb\|right\|400px](images/HolderTop2-16.jpg ) Erstelle ein boolesches Formelement, um den Hauptkörper und den Schraubenkörper zu verschmelzen. Erstelle dann einen neuen Körper für die andere Seite. Dupliziere die Skizze der Drehung, verschiebe sie auf diesen Körper und erstelle den zweiten Körper für die Schrauben (das Spiegeln eines Körpers wird noch nicht unterstützt, so dass Sie den größten Teil davon neu ausführen müssen). Verschmelze dann auch diesen zweiten Körper mit dem Hauptkörper. Abschließend bringe eine große Verrundung an der Kante an, die durch die boolesche Verschmelzungsoperation erzeugt wurde. Die größte Verrundung, die ich erreichen konnte, war 4 mm.

## Aushöhlung des Hauptkörpers 

![Das erste Polster des ausgeschnittenen Körpers im Inneren des Hauptkörpers\|thumb\|right\|300px](images/HolderTop2-9.jpg ) Wir werden nun an der Innenseite des Halters arbeiten und ihn aushöhlen, um Platz für die Lager- und Dichtungsringe zu schaffen. Dabei müssen wir natürlich die 3 mm Bearbeitungszugabe berücksichtigen. Da dieses Tutorial die Multi-körpermethode lehrt, werden wir die Innengeometrie als separaten Körper erstellen und dann mit einer boolschen Operation aus dem Hauptkörper herausschneiden.

Erstelle einen neuen Körper und mache ihn aktiv. Zuerst benötigen wir eine um 3 mm versetzte Bezugsebene innerhalb der Skelettfläche, die die Seite des Lagers zeigt. Dann dupliziere die Skizze des ersten Polsters des Hauptkörpers. Sie wird dem Hauptkörper hinzugefügt, also klicke mit der rechten Maustaste darauf und wähle, um sie in den neu erstellten Körper zu verschieben (diese Option ist nur im Kontextmenü verfügbar, wenn der PartDesign Arbeitsbereich aktiv ist). Bilde die Skizze auf die Bezugsebene ab (wenn die Skizze nach dem Zuordnen auf den Kopf gestellt wird, verschiebe die Bezugsebene auf die andere Seite des Lagers, neben die Stelle, an der sich die duplizierte Skizze befindet). Modifiziere die Skizze nun so, dass der Durchmesser 3 mm kleiner ist als der Außendurchmesser der Skelettgeometrie, die das Lager darstellt. Du musst nur die 5 mm Bemaßung entfernen, die Skizze innerhalb des Referenzkreises ziehen und eine neue 3 mm Bemaßung erstellen.
![Der ausgeschnittene Körper im Inneren des Skelettkörpers\|thumb\|right\|400px](images/HolderTop2-10.jpg ) Als nächstes wollen wir zwei weitere Polster, um den Platz für die Dichtungsringe auszuhöhlen. Dupliziere die Skizze des ersten Polsters des ausgeschnittenen Körpers und ordne es der XZ Ebene zu. Bearbeite die Skizze und ersetze die externe Referenz durch den Außendurchmesser des Lagerdichtrings. Extrudiere diese Skizze bis zu einem Versatz von 3 mm von der Seite des Dichtungsrings. Wiederhole den gesamten Vorgang für den Dichtungsring auf der anderen Seite.

Danach wollen wir zwei weitere Polster wie die letzten beiden erzeugen, um der Welle einen Freiraum (z.B. 3mm) innerhalb des Gehäuses zu geben.
![Der komplette ausgeschnittene Körper (abzüglich unmöglicher Ausrundungen)\|thumb\|right\|400px](images/HolderTop2-11.jpg ) Jetzt müssen nur noch die ebenen Seitenflächen mit der gleichen neutralen Ebene wie der Hauptkörper mit dem Entwurf versehen und verrundet werden. Wende an allen Kanten eine allgemeine Verrundung von 3 mm an. Du wirst feststellen, dass es mehrere Kanten gibt, die nicht verrundet werden können\... dies ist ein Defekt des zugrunde liegenden geometrischen Kerns, den FreeCAD verwendet.
![Das fertige Rohteil des Halters (ohne spanende Bearbeitung)\|thumb\|right\|400px](images/HolderTop2-15.jpg ) Wir sind bereit, den Hauptkörper auszuhöhlen. Wähle ihn aus und wähle eine neue Boolesche Operation zu erstellen. Füge den ausgeschnittenen Körper dem Listenfenster hinzu und setze die Operation auf \"Ausschneiden\". Lege eine Verrundung von 3 mm auf die beiden Kanten, die sich aus dem Ausschneiden ergeben (auch hier bleiben einige Kanten übrig, die \"unverrundet\" sind). Das Ergebnis sollte wie auf dem Bild rechts aussehen.

Das Rohteil ist nun fertiggestellt. So wird der Halter vor der Bearbeitung aussehen. Beachte, dass die Kante zwischen diesen beiden nicht verrundet werden kann, da die Form eine obere und eine untere Hälfte haben wird. Auch wenn du dieses Modell an eine Gießerei verschenkst, musst du darauf hinweisen, dass es die Abmessungen nach dem Gießen hat. Die Gießerei muss dann einen bestimmten Prozentsatz der Schrumpfung auf das Modell anwenden (das digitale Modell, das zur Herstellung der Form verwendet wird, muss größer gemacht werden, damit das Metall nach dem Gießen beim Abkühlen und Schrumpfen die richtige Größe hat).

## Spanende Bearbeitung 

![Skizze zum \"Bohren\" des Lochs für die Schrauben.\|thumb\|right\|400px](images/HolderTop2-17.jpg ) Um das Material für die Bearbeitung der Innenseite des Gehäuses zu entfernen, können wir sehr bequem den Skelettkörper selbst verwenden. Wenn du das nicht willst, weil dann das Skelett irgendwo tief im Baum versteckt wird, kannst du auch die Skizze des Skelett Umdrehungsformelements duplizieren und die Umdrehung in einem anderen Körper nachbilden. Dies ist jedoch nicht vollständig parametrisch, da die duplizierte Skizze unabhängig vom Original ist, so dass du an beiden arbeiten musst, wenn du eine Bemaßung änderst. Abhängige duplizierte Formelemente könnten in der Zukunft irgendwann unterstützt werden.

Für den Rest der soaneneden Bearbeitung erzeuge einen neuen Körper. Der Boden des Gehäuses wird mit einem auf der XY Ebene skizzierten Polster bearbeitet, das sich nach unten erstreckt. Als nächstes skizziere eine Umdrehung, um ein Loch für die Schrauben herzustellen. Du musst auf der XZ Ebene skizzieren und diese drehen, damit du den Außendurchmesser des Skelettkörpers als externe Referenz wählen kannst. Der obere Teil der Skizze dient dazu, eine flache Stelle für den Kopf der Schraube zu bearbeiten. Er ist so bemessen, dass mindestens 5 mm Wandstärke in der Halterung verbleiben. Wenn dies nicht genug Platz für den Schraubenkopf bietet, kannst du die Bezugsebene nach oben verschieben. Natürlich kannst du diese Logik in das Skelett einbauen, was dem Leser als Übung überlassen bleibt!
![Der Bearbeitungskörper\|thumb\|right\|400px](images/HolderTop2-18.jpg ) Du kannst die Umdrehung auf der YZ Achse spiegeln. Das Bild rechts zeigt den \"Bearbeitungs\" Körper. Natürlich sind die meisten Abmessungen der Polster und Umdrehungen nicht wichtig, solange es viele Überlappungen gibt.
![Der fertige Halter mit Bearbeitung\|thumb\|right\|400px](images/HolderTop2-19.jpg ) Erstelle schließlich eine boolesche Operation, um den bearbeitenden Körper aus dem Hauptkörper herauszuschneiden. Wenn du einen schönen visuellen Effekt wünschst, kannst du die bearbeiteten Flächen anders einfärben als den Rest des Werkstücks. Dies ist auch eine nützliche optische Rückmeldung, die dir anzeigt, ob du irgendwo vergessen hast, zu bearbeiten.

## Teil Eins 

[PartDesign Lagergehäuse Tutorium I](PartDesign_Bearingholder_Tutorial_I/de.md)



[Category:Tutorials](Category:Tutorials.md)
