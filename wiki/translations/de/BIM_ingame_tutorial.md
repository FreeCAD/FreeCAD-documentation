# <img alt="" src=images/BIM_tutorial_screenshot.png  style="width:1024px;"> BIM ingame tutorial/de


{{BIMTutorialAction/de|descr=Dies ist die anwendungsinterne Anleitung des Arbeitsbereichs [BIM](BIM_Workbench/de.md). Sie ist nicht dafür gedacht, hier im Wiki gelesen zu werden, sondern wird aus FreeCAD heraus im Arbeitsbereich BIM, unter dem Menü '''Hilfe → BIM-Anleitung''' gestartet. Sie enthält eine Reihe von Schritten, die vom Benutzer auszuführen sind. Jeder Schritt wird durch eine Instanz der Vorlage [<nowiki>{{BIMTutorialAction/de|descr|goal1|test1|goal2|test2}}</nowiki>](Template:BIMTutorialAction/de.md) abgeschlossen, die über die Bedingung informiert, die erfüllt werden muss. Bilder sollten 300px breit sein. Auf dieser Seite sollten keine SVG-Bilder verwendet werden, da sie vom QTextBrowser-Widget nicht unterstützt werden}}



### Willkommen im Arbeitsbereich BIM! 

<img alt="" src=images/BIM_Tutorial_title.jpg  style="width:300px;">

Diese Anleitung führt den Anwender durch die verschiedenen Funktionalitäten des Arbeitsbereichs [BIM](BIM_Workbench/de.md) und hilft, durch die Modellierung eines sehr einfachen Pavillongebäudes, den richtigen Weg zu finden. Die komplette Bearbeitung sollte je nach Vorkenntnissen im Umgang mit 3D-Anwendungen zwischen einer und zwei Stunden dauern.

Sie kann jederzeit angehalten und später fortgesetzt werden, indem der Menüeintrag **Hilfe → BIM-Anleitung** ausgewählt wird.

Einige Schritte dieser Anleitung erfordern die Mitarbeit den Anwenders. Dazu werden unter diesem Textfeld Aufgaben angezeigt, mit einem Symbol, das anzeigt, ob eine Aufgabe abgeschlossen wurde oder nicht. Aber da wir hier bei FreeCAD gute Menschen sind, ist es nicht zwingend erforderlich, die Aufgaben abzuschließen, um durch diese Seiten zu gelangen. Die Anleitung kann einfach durchgeblättert und die Aufgaben nach Belieben übersprungen werden.



#### Über FreeCAD-Versionen 

Diese Anleitung ist für die aktuellste verfügbare Entwicklungsversion von FreeCAD geschrieben. (derzeit 1.1.0dev). Der Arbeitsbereich BIM ist jedoch so konzipiert, dass er mit jeder Version von FreeCAD kompatibel ist. Wird eine ältere FreeCAD-Version als die hier angegebene verwendet, könnten einige BIM-Werkzeuge anders aussehen, anders funktionieren oder sogar nicht verfügbar sein. Im Zweifelsfall hilft das Lesen der [Dokumentation](BIM_Workbench/de.md), um mehr zu erfahren.



#### Hinweis

An dieser Anleitung wird noch geschrieben, sie ist daher **unvollständig**! Wenn du Vorschläge hast oder Dinge, die du unklar findest, dann hilf uns doch im [FreeCAD-Forum](https://forum.freecad.org/viewforum.php?f=23), sie zu verbessern!


{{BIMTutorialAction/de|descr=Keine Aktion für diesen Schritt ausführen}}



### FreeCAD einrichten 

FreeCAD hat ein umfangreiches Voreinstellungssystem mit vielen Optionen, die unter dem Menü **Bearbeiten → Einstellungen** zu finden sind. Jeder zusätzliche Arbeitsbereich kann weitere Einstellungsseiten hinzufügen, was es sehr komplex macht.

Der Arbeitsbereich BIM stellt ein [vereinfachtes Einrichtungsfenster](BIM_Setup/de.md) zur Verfügung, mit dem schnell einige der nützlichsten Einstellungen für die BIM-Arbeit vorgenommen werden können. Das Fenster **BIM-Einstellungen** befindet sich unter dem Menüeintrag **Verwalten → BIM einrichten\...** (Es kann auch die entsprechende Schaltfläche in der Symbolleiste \"Werkzeuge verwalten\" angeklickt werden):

<img alt="" src=images/BIM_Tutorial_01.jpg  style="width:300px;">

Öffne nun den Dialog BIM Setup und lege die verschiedenen Optionen nach deinem Geschmack fest.

Im Bedarfsfall bewegen die Maus über eine beliebige Option oder Einstellung, um eine Beschreibung zu sehen, wofür sie verwendet wird:

<img alt="" src=images/BIM_Tutorial_02.jpg  style="width:300px;">

In dieser Anleitung werden wir in Zentimetern arbeiten. Wir empfehlen daher, die bevorzugten Einheiten auf **Zentimeter** und die Standardgröße eines Rasterquadrats auf **10 cm** einzustellen. Diese Einstellungen können jederzeit über die Schaltfläche für die Auswahl der Arbeitsebene in der Hauptsymbolleiste und die Einheitenanzeige in der Statusleiste (unten rechts) geändert werden:

<img alt="" src=images/BIM_tutorial_14.jpg  style="width:300px;">


{{BIMTutorialAction/de
|goal1=Den Dialog BIM Setup öffnen 
|test1=True if hasattr(FreeCADGui,"BIMSetupDialog") else False
|goal2=Set preferred working units to centimeters and the default size of a grid square to 10 cm
|test2=True if ((FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema",0) == 4) and (FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Draft").GetString("gridSpacing") == '10.00 cm')) else False}}



### Neues Dokument erstellen 

Wurde FreeCAD eben erst installiert, wird wahrscheinlich gerade die **FreeCAD-Startseite** angezeigt:

<img alt="" src=images/BIM_tutorial_13.jpg  style="width:300px;">

Die Startseite zeigt die Dokumente an, an denen zu letzt gearbeitet wurde und erklärt auf verschiedenen Registerkarten wie man Hilfe erhält. Um jedoch mit der Arbeit zu beginnen, müssen wir ein neues, leeres Dokument erstellen. Falls dies noch nicht geschehen ist, wird jetzt ein neues Dokument erstellt, indem das Element \"Leere Datei\" auf der Startseite verwendet wird oder über der Menüeintrag \"Datei → Neu\" ausgewählt wird:

<img alt="" src=images/BIM_tutorial_09.jpg  style="width:300px;">

Sie befinden sich dann im 3D-Raum von FreeCAD und sind bereit mit der Arbeit zu beginnen.

<img alt="" src=images/BIM_tutorial_10.jpg  style="width:300px;">


{{BIMTutorialAction/de
|goal1=Ein neues Dokument erstellen
|test1=True if FreeCAD.ActiveDocument else False
}}



### In der 3D-Ansicht navigieren 

Es gibt mehrere Möglichkeiten, wie Sie mit der Maus in FreeCAD interagieren können. Diese werden als [Navigationsstile](Mouse_navigation.md) bezeichnet. Sie können den aktuellen Navigationsstil jederzeit ändern, indem Sie auf die Schaltfläche für den Navigationsstil in der Statusleiste klicken. Wenn Sie die Maus über diese Schaltfläche bewegen, wird Ihnen auch angezeigt, welche Funktionen jeder Mausbutton hat. Einige von ihnen sind so gestaltet, dass sie zu anderen bekannten Anwendungen passen. Wählen Sie einen Stil, mit dem Sie vertraut sind.

<img alt="" src=images/BIM_Tutorial_03.jpg  style="width:300px;">

Die Kontrolle darüber, wie Sie Ihr Modell in der 3D-Ansicht betrachten, kann auf verschiedene Arten erfolgen: Verwenden der Maus (abhängig vom gewählten Navigationsstil), der Tastatur (bitte lesen Sie den Inhalt des Ansicht-Menüs, um mehr zu erfahren) oder des [Navigationswürfels](Navigation_Cube.md) (Klicken Sie auf die verschiedenen Pfeile und Flächen des Würfels, um die Ansicht auszurichten).

<img alt="" src=images/BIM_Tutorial_04.jpg  style="width:300px;">


{{BIMTutorialAction/de
|goal1=Einen Navigationsstil auswählen
|test1=True
|goal2=In die Draufsicht wechseln
|test2=True if FreeCADGui.ActiveDocument.ActiveView.getViewDirection().getAngle(FreeCAD.Vector(0,0,-1)) < 0.01 else False
}}



### Umorganisieren der Oberfläche 

Alle Fenster und Werkzeugleisten in FreeCAD können bewegt und neu organisiert werden. Größere Anzeigetafeln können durch Ziehen und fallen lassen mit anderen zusammen gefügt werden. Wenn dein Bildschirm zu klein ist um alle Werkzeugleisten und deren Inhalt anzuzeigen, (abgeschnittene Werkzeugleisten werden mit einem \>\> Zeichen angezeigt) ist es eine gute Idee sie an eine bessere Position zu bewegen.

<img alt="" src=images/BIM_Tutorial_05.jpg  style="width:300px;">

Werkzeugleisten und Fenster können mit dem **Ansicht** Menü ein- und ausgeschaltet werden.

Der Arbeitsbereich BIM bietet in der Statusleiste Schaltflächen, welche zusätzliche Fenster wie Selection View, Report View und Python console ein- und ausschalten. Diese Fenster sind beim Arbeiten mit FreeCAD oft nützlich, aber sie verbrauchen wertvolle Bildschirmfläche. Du kannst für gewöhnlich alles ausschalten bis du es benötigst. Erinnere dich, dass Fehlermeldungen im Report View angezeigt werden, wenn etwas falsch läuft, schaue dort nach.

<img alt="" src=images/BIM_tutorial_17.jpg  style="width:300px;">


{{BIMTutorialAction/de
|descr=Keine Aktion für diesen Schritt ausführen
}}



### Die Werkzeuge des Arbeitsbereichs BIM 

Der [Arbeitsbereich BIM](BIM_Workbench.md) enthält sowohl Werkzeuge die aus anderen Arbeitsbereichen wie [Draft](Draft_Workbench.md) oder [Part](Part_Workbench.md), ausgeborgt sind, als auch eigene Werkzeuge. Sie sind in mehreren Bereichen organisiert. Jeder Bereich hat ein Menü und eine Werkzeugleiste. Nimm dir einen Moment Zeit und erforsche den Inhalt der unten beschriebenen Menüs.



#### 2D-Zeichnen 

Diese Werkzeuge ermöglichen, ebene Objekte, wie Linien, Linienzüge, Rechtecke, Kreisbögen usw\... zu zeichnen, welche als Basis für BIM-Objekte eingesetzt werden. Zum Beispiel kann ein Linienzug als Umriss einer Mauer, oder ein Rechteck als Profil für einen Balken verwendet werden. Alle 2D-Objekte werden auf der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) erzeugt.

<img alt="" src=images/BIM_Tutorial_35.jpg  style="width:300px;">



#### 3D/BIM

Diese Gruppe enthält Werkzege zum Erzeugen von BIM Objekten wie [Wand](Arch_Wall.md) oder [Fenster](Arch_Window.md), und generisch, nicht-BIM Objekte wie Quader, die du später in BIM Objekte wandeln kannst. Das Ergebnis ist unterschiedlich je nachdem ob du das Werkzeug mit einem ausgewählten Objekt verwendest oder nicht. Falls nicht, wird ein Erzeugungsfenster angezeigt. Falls du vor dem Ablauf des Werkzeuges ein Objekt ausgewählt hast, dann wird unter Verwendung des gewählten Objektes ein Objekt der entsprechenden Type erzeugt.

<img alt="" src=images/BIM_Tutorial_33.jpg  style="width:300px;">

Ein typisches Beispiel ist die [Wand](Arch_Wall.md) Schaltfläche zu betätigen während eine [Linie](Draft_Line.md) oder ein [Linienzug](Draft_Wire.md) ausgewählt ist. Es wird automatisch eine Wand erzeugt, wobei die Linie oder der Linienzug als Basis verwendet wird.

Nicht-BIM Objekte, eingeschlossen Objekte die in anderen Arbeitsbereichen erzeugt wurden, könne jederzeit in BIM Objekte verwandelt werden, indem sie ausgewählt werden und eine BIM Schaltfläche gedrückt wird.



#### Beschriften

Diese Werkzeuge erstellen Beschriftungsobjekte wie z.B. Maße, Texte, Hinweise oder Raster, die nicht zum Modellieren eingesetzt werden, sondern zum Beschriften der Modelle und zum Erstellen verständlicher Zeichnungen.

<img alt="" src=images/BIM_Tutorial_34.jpg  style="width:300px;">



#### Einrasten

Diese Werkzeuge schalten das [Einrasten](Draft_Snap/de.md) an Positionen ein/aus. Wie bei den meisten BIM Anwendungen, benötigt jedes Einrasten an Positionen beim Zeichnen Berechnungszeit, deshalb ist es am Besten dies nur wenn notwendig eingeschaltet lassen.



#### Ändern

Diese Werkzeuge verändern bestehende Objekte. Sie beinhalten gewöhnlich Werkzeuge zur Transformation wie Bewegen oder Drehen, zusätzlich andere die nur bei speziellen Objekten arbeiten.



#### Verwalten

Diese Gruppe enthält generelle Management Werkzeuge. Die meisten erlauben es Eigenschaften einer großen Gruppe von BIM Objekten gleichzeitig zu ändern, ohne dass einzelne ausgewählt werden müssen.

Jedes Werkzeug, dass in diesen Menüs enthalten ist, hat seine eigene Dokumentationsseite, die im Detail beschreibt, wie es arbeitet und welche Optionen zur Verfügung stehen. Sie werden auf der Dokumentationsseite des Arbeitsbereichs [BIM](BIM_Workbench/de.md) aufgelistet, die auch über das Menü **Hilfe** erreichbar ist, oder durch Auswählen des Menüeintrags **Hilfe → Direkthilfe** und Anklicken einer beliebigen Schaltfläche einer Werkzeugleiste.


{{BIMTutorialAction/de
|descr=Keine Aktion für diesen Schritt ausführen
}}



### Bereite deinen Arbeitsbereich vor 

Es gibt viele Wege um in FreeCAD BIM-Objekte zu erstellen. Man kann die [BIM-Werkzeuge](BIM_Workbench/de.md) dieses Arbeitsbereiches verwenden, oder jedes andere Werkzeug aus anderen [Arbeitsbereichen](Workbenches/de.md). Beide, die Werkzeuge für *2D-Zeichnen* und *3D-BIM* dieses Arbeitsbereichs, verwenden, anders als andere Arbeitsbereiche wie Part Design, weitgehend die **Arbeitsebene** und das **Einrasten**.

Die [Arbeitsfläche](Draft_SelectPlane.md) ist dort wo die Objekte erzeugt werden. Man kann sie auf eine der rechtwinkeligen Basisebenen (Boden, Vorderseite, Seite) legen, oder man kann jede ausgewählte Fläche zum Festlegen verwenden. Man kann auch [Arbeitsflächen Proxies](Draft_WorkingPlaneProxy/de.md) aus den Menü **Werkzeuge** verwenden, um eine spezielle Lage der Arbeitsfläche im Modell zu speichern. [Teile Erzeugen](Arch_BuildingPart/de.md) enthält eine implizierte Positionierung der Arbeitsfläche. Die aktuelle Arbeitsfläche wird durch Betätigen der Arbeitsflächen Schaltfläche in der BIM Werkzeugleiste gewechselt. Der **Raster** zeigt immer wo die Arbeitsfläche ist.

Wie du schon bemerkt hast, sind der Blickwinkel und die Arbeitsfläche nicht miteinander verknüpft. Man kann auf der Arbeitsfläche aus jedem beliebigen Blickwinkel arbeiten.

Setze jetzt die Arbeitsfläche in den \"Oben\" Modus:

<img alt="" src=images/BIM_Tutorial_06.jpg  style="width:300px;">

Die [snapping tools](Draft_Snap/de.md) erlauben es neue Objekte und Punkte genau an die vorhandene Geometrie anzuhängen. Wie auch immer, viele Einrast Orte können die Zeichenoperationen langsam machen, deshalb ist es günstig nur notwendige Einrast Werkzeuge zu erlauben. Überlege eine Moment was jedes von ihnen macht, dann wirst du erkennen welches deaktiviert werden kann.

<img alt="" src=images/BIM_Tutorial_07.jpg  style="width:300px;">

Beachte besonders das letzte, das **Arbeitsflächen Einrast** Werkzeug, denn dieses zwingt jeden Punkt auf der Arbeitsfläche zu liegen, somit wird verhindert dass oberhalb oder unterhalb der Arbeitsfläche eingerastet wird. Es wird, abhängig von der durchgeführten Operation, oft notwendig sein dieses ein- oder auszuschalten.


{{BIMTutorialAction/de
|goal1=Die Arbeitsebene in den Modus "Draufsicht" (XY) versetzen
|test1=True if ((FreeCAD.DraftWorkingPlane.axis.getAngle(FreeCAD.Vector(0,0,1)) < 0.01) and (FreeCAD.DraftWorkingPlane.weak == False)) else False
|goal2=Nochmals die unterschiedlichen Einrastwerkzeuge betrachten
|test2=True
}}



### Zeichnen einer ersten Wand 

Starten wir mit dem Erbauen unseres Pavillion mit dem Erzeugen einiger Wände. Wände können entweder direkt mit dem [Wand](Arch_Wall/de.md), oder durch zuerst Zeichnen von 2D Objekten wie [Linie](Draft_Line/de.md), [Linienzug](Draft_Wire/de.md) (Polylinien) oder [Skizzen](Sketcher_NewSketch/de.md), welche die Grundlinie unserer Wände definieren, erzeugt werden. Wenn ein Grundlinien Element ausgewählt ist wird es durch Betätigen des Wand Werkzeuges automatisch in eine Wand umgewandelt.

Zoome zuerst hinaus bis der Großteil oder der gesamte Raster sichtbar ist. Das macht es viel einfacher zu sehen was wir machen:

<img alt="" src=images/BIM_tutorial_15.jpg  style="width:300px;">

Dann die Schaltfläche <img alt="" src=images/Arch_Wall.png  style="width:16px;"> **Wand** in der Symbolleiste drücken (oder den Menüeintrag **3D/BIM → Wand** auswählen). Auf dem Raster zwei vertikal ausgerichtete Punkte mit **300 cm** Abstand anklicken. Das Drücken der SHIFT-Taste nach dem Anklicken des ersten Punktes hilft die Wand horizontal oder vertikal ausgerichtet zu lassen. Das seitliche Fenster zeigt während des Zeichnens die Länge der Wand an.

<img alt="" src=images/BIM_tutorial_16.jpg  style="width:300px;">

Falls eine falsche Wand erstellt wurde, keine Sorge! Einfach die Wand löschen oder die Erstellung rückgängig machen (Menüeintrag **Bearbeiten → Rückgängig**) und erneut versuchen.


{{BIMTutorialAction/de
|goal1=Eine Wand erstellen
|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList]) == 1)
}}



### Zeichnen einer zweiten Wand 

Erzeuge eine zweite, horizontale Wand die 4 Meter (oder 400 cm) lang ist. Wähle wieder das <img alt="" src=images/Arch_Wall.png  style="width:16px;"> **Wand** Werkzeug, verschiebe oder zoome bis du einen guten Teilbereich des Rasters siehst, und klicke zwei Punkte um den Start- und Endpunkt der neuen Wand festzulegen:

<img alt="" src=images/BIM_tutorial_11.jpg  style="width:300px;">

Wähle, nachdem sie erzeugt wurden, beide Wände durch drücken von CTRL und anklicken beider in der 3D Ansicht oder im [Modellbaum](Document_structure/de.md), und stelle ihre Eigenschaft **Höhe** auf 2.5 Meter, und **Breite** auf 20 cm (oder jedes andere Maß mit dem du vertraut bist, falls du mit anderen Einheiten arbeitest) ein. Dann sehen sie so aus (Verwende die Maus um die Ansicht gemäß dem verwendeten Navigations Style zu drehen):

<img alt="" src=images/BIM_tutorial_08.jpg  style="width:300px;">

Du kannst immer, nachdem eine Wand oder ein anderes BIM Objekt erzeugt wurde, die Eigenschaften ausbessern oder ändern. Durch erweitern des Wand Objektes im Modellbaum, und anschließendes Doppelklicken der Basislinie der Wand, kann man auch sein 2D Basisobjekt verändern. Die Meisten BIM Objekte basieren auf anderen Objekten wie Basislinien oder Profilen.

<img alt="" src=images/BIM_tutorial_12.jpg  style="width:300px;">



#### Wichtiger Hinweis 

Du wirst bemerken, dass einige Änderungen von Eigenschaften in FreeCAD nicht sofort in der 3D Ansicht erscheinen. Statt dessen wird das Objekt im Modellbaum blau als \"muss neu berechnet werden\" markiert:

<img alt="" src=images/BIM_Tutorial_20.jpg  style="width:300px;">

Der Grund ist, dass ein FreeCAD-Dokument eine sehr komplexe Kette von untereinander abhängigen Objekten sein kann. Das Aktualisieren eines Objekts kann das Aktualisieren vieler anderer Objekte auslösen, und sehr viel Zeit erfordern. Um dies zu vermeiden, markieren einige Vorgänge das Objekt einfach als neu zu berechnen und der Anwender löst die Neuberechnung selbst aus, durch das Auswählen des Menüeintrags **Bearbeiten → Aktualisieren** oder durch Drücken von **Ctrl + R**.


{{BIMTutorialAction/de
|goal1=Zwei rechtwinklige Wände (wall objects) erstellen
|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList]) == 2)
|goal2=Ihre höhe auf 2.50 m and ihre Breite auf 20 cm festlegen
|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList and o.Height.Value == 2500 and o.Width.Value == 200]) == 2)
}}



### Nicht vergessen, die Datei regelmäßig zu speichern! 

Wie jede andere Computeranwendung, ist FreeCAD anfällig dafür zu versagen oder abzustürzen, besonders, wenn wir wenig Erfahrung mit ihm haben. Häufiges Sichern einer Datei ist gute Angewohnheit, an die man sich schon frühzeitig gewöhnen sollte. FeeCAD besitzt auch einen Mechanismus zum automatischen Speichern, den man im Menü **Bearbeiten → Einstellungen → Allgemein → Dokument** einstellen kann.

Jetzt die Datei speichern mit **Datei → Speichern**.


{{BIMTutorialAction/de
|goal1=Die Datei sichern
|test1=bool(FreeCAD.ActiveDocument.FileName)
}}



### Zeichnen einer Dachfläche 

Wir werden jetzt eine Dachplatte oben auf unsere Wände platzieren. Anstatt die Platte, wie wir es mit den Wänden gemacht haben, direkt zu zeichnen werden wir hier zuerst ein Rechteck zeichnen, dass wir dann in eine Platte verwandeln. Wir werden jetzt zwei Methoden erforschen, um das zu machen. Es ist nützlich beide zu kennen. Wir versuchen zuerst die eine, dann löschen wir (oder neu Laden der Datei), und dann versuchen wir die Andere.



#### Methode 1: Zeichne die Scheibe auf dem Boden an und bringen Sie sie dann in Position 

Es ist oft bequem die obere XY Ebene (die Grundebene) als eine Art von \"Zeichenebene\" aufzufassen, auf der wir unsere Objekte erzeugen, die wir anschließend zu ihren richtigen Positionen verschieben. Es gibt hier den zusätzlichen Vorteil, dass die Arbeitsebene sich schon im \"Oben\" Modus befindet, wir sie also nicht verändern müssen.

Jetzt in die Draufsicht wechseln, etwas heraus-zoomen, bis beide Wände zu sehen sind, und ein Rechteck zeichnen das beide beinhaltet. Die Schaltfläche <img alt="" src=images/Draft_Rectangle.png  style="width:16px;"> **Rechteck** in der Symbolleiste drücken (oder den Menüeintrag **2D-Zeichnen → Rechteck** auswählen):

<img alt="" src=images/BIM_Tutorial_18.jpg  style="width:300px;">

Drehe deine Ansicht um die Resultate zu begutachten. Als Standard ist das Rechteck mit einer Fläche gefüllt. Das kann durch Ändern der **Make Face** Eigenschaft unseres Rechteckes auf False geändert werden. Für die Platte die wir erzeugen werden hat das keinen Einfluss, aber für andere Arten von Objekten kann es einen Unterschied machen ob das Basisobjekt ein Linienzug oder eine Fläche ist.

<img alt="" src=images/BIM_Tutorial_19.jpg  style="width:300px;">

Der nächste Schritt ist das Erstellen der Platte durch *Extrudieren* , mit unserem Rechteck als *Basisprofil*. In FreeCAD werden Strukturobjekte wie Säulen, Balken oder Platten mit dem gleichen Objekt, welches **Struktur** genannt wird, erstellt. Nachdem ein Strukturobjekt erstellt wurde, genügt es um seine Art zu Ändern seine Eigenschaft **IFC Typ** auf die gewünschte Art (Säule, Platte usw\...) einzustellen.

Sicherstellen, dass unser Rechteck ausgewählt ist, dann die Schaltfläche <img alt="" src=images/BIM_Slab.png  style="width:16px;"> **Platte** in der Symbolleiste drücken (oder den Menüeintrag **3D/BIM → Platte** auswählen). Wie vorher angegeben, kann das auch mit den Stützen- oder Balkenwerkzeugen ausgeführt werden, da alle dieselbe Art Objekt erstelle. Nachdem unser Objekt erzeugt wurde, müssen wir seine Eigenschaften wie folgt ändern:

-   Setze seine **Höhe** auf **20 cm**
-   Überprüfe ob sein **IFC Type** auf **Platte** gesetzt ist

Jetzt müssen wir unsere Dachplatte an die richtige Position verschieben, das ist oberhalb der Wände. Wir müssen sie aufwärts, in Z Richtung, um 250 cm was die Höhe unserer Wände ist, bewegen. Wir können einfach die **Placement** Eigenschaft unserer Platte editieren, ihr **Position** Attribut öffnen und den Wert von **z** auf 250 cm setzen. unsere Platte befindet sich jetzt am richtigen Ort:

<img alt="" src=images/BIM_Tutorial_21.jpg  style="width:300px;">

Eine andere Möglichkeit um unsere Platte in die richtige Position zu bewegen ist das <img alt="" src=images/Draft_Move.png  style="width:16px;"> **Verschieben** Werkzeug im Menü **Modifizieren**. Dazu müssen wir zuerst die Arbeitsfläche in eine vertikale Fläche setzen, indem wir die <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> **Arbeitsfläche** Schaltfläche drücken (stelle sicher, dass keine andere Fläche ausgewählt ist) und sie auf **XZ (Vorderfront)** setzen. Indem wir uns selbst in die Vorderansicht setzen (drücke Taste **1**) können wir jetzt die Platte wählen, die <img alt="" src=images/Draft_Move.png  style="width:16px;"> **Bewegen** Schaltfläche drücken, und die Platte durch klicken eines Basispunktes und mit gedrückter **Shift** Taste die Bewegung als vertikal einschränkend, einen Punkt an der Oberseite der Wände klicken, bewegen:

<img alt="" src=images/BIM_Tutorial_23.jpg  style="width:300px;">



#### Method 2: Zeichne die Platte direkt in der richtigen Ebene 

Eine andere nützliche Methode arbeitet direkt auf der vorgesehenen Ebene. Wir können die Arbeitsebene auf die Oberseite der Wände setzen, dort wo wir unsere Platte wünschen. Auswählen einer Fläche und und drücken der <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> **Arbeitsflächen** Schaltfläche setzt die Arbeitsfläche auf die gewählte Fläche. Wähle die Deckfläche einer Wand und setze die aktuelle Arbeitsfläche. Das Platzierung des Rasters bewegt sich, um die aktuelle Arbeitsfläche zu zeigen.

<img alt="" src=images/BIM_Tutorial_22.jpg  style="width:300px;">

Alles was wir von jetzt an zeichnen erfolgt auf dieser Fläche. Wenn du möchtest kannst du dich jetzt in die Deckfläche setzen, aber das ist nicht notwendig. Wenn die Arbeitsfläche einmal gesetzt ist und **Einrasten** aktiviert ist, kann man in jeder 3D Ansicht direkt zeichnen.

Sobald unser rechteckiges *Profil* gezeichnet ist, können wir zum Erzeugen der Platte die gleiche Methode wie in der ersten Methode verwenden (auswählen, drücken der **Struktur** Schaltfläche, einstellen der Eigenschaften).


{{BIMTutorialAction/de
|goal1=Ein Rechteck erstellen
|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Rectangle" in o.Name]) == 1)
|goal2=Eine 20 cm dicke Platte erstellen
|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "IfcType" in o.PropertiesList and o.IfcType == "Slab" and o.Height.Value == 200]) == 1)
}}



### Eine Metallsäule erstellen 

Lass uns zu Unterstützung der Platte eine Säule aus Metall hinzufügen. Stelle sicher, dass die Arbeitsebene im Oben Modus ist. Wir beginnen damit, dass wir uns in den Ansicht von Oben Modus (drücke die Taste **2**) stellen und die Platte ausblenden, so dass wir besser sehen was sich darunter befindet. Wähle die Platte aus, und drücke die **Leertaste** sodass ihre Anzeige ausgeblendet wird.

In FreeCAD ist es sehr einfach Objekte oder Gruppen ein- oder auszublenden, und der Modellbaum zeigt eindeutig was zu sehen ist und was verborgen ist. Verwende dies oftmals!

Das Werkzeug **Stütze** (ebenso das Werkzeug Balken) hat ein paar eingebaute Profile die wir jetzt verwenden werden. Sicherstellen, dass nichts ausgewählt ist, dann die Schaltfläche Säule drücken. In den **Strukturoptionen** die Kategorie **CHS** (für \"Hohler Kreisquerschnitt\"; RHS \"Hohler Rechteckquerschnitt\", HEA, HEB, usw. sind verschiedene \"H\"-Querschnitte usw.):

<img alt="" src=images/BIM_Tutorial_24.jpg  style="width:300px;">

Und klicke einen Punkt an um die Säule zu platzieren mehr oder weniger an dieser Position. Stelle sicher, dass die neue Säule den IFC Typ \"Säule\" hat, und gib ihr die Höhe 250 cm damit sie gleiche Höhe wie die Wände hat.

<img alt="" src=images/BIM_Tutorial_25.jpg  style="width:300px;">

Der Standard-Durchmesser der Einstellung CHS ist mit 21,3 mm sehr klein und damit zu dünn, um eine Dachplatte aus Beton zu unterstützen. Zum Glück, da alles parametrisch ist, ist es einfach den Durchmesser zu ändern. Das neue Strukturobjekt wird in der Baumansicht erweitert und wir sehen sein Profilobjekt mit dem Namen CHS21.3x2.6\_. Seinen Durchmesser ändern wir auf 12 cm und seine Wandstärke auf 8 mm. Jetzt haben wir eine Stütze mit ausreichender Festigkeit. Man beachte, dass die Einheiten während der Eingabe (on the fly) eingestellt werden können und dass der Wechsel zwischen 0,8 cm und 8 mm problemlos erfolgt. FreeCAD kümmert sich um die Umwandlung.



#### Trägerplatte hinzufügen 

Wir brauchen noch einen Weg um unsere Metallsäule an der Betonplatte zu befestigen. Dafür fügen wir an ihrem Oberteil eine Platte an, die an die Betonplatte angeschraubt werden kann. Dies erklärt wie einfach man BIM Objekte ändern kann, um genau die benötigten zu erzeugen.

Wir beginnen mit dem Ändern der Höhe der Säule von 250 cm auf 249 cm, damit wir Platz für eine 1cm starke Platte bekommen. Dann zeichnen wir ein 20 cm x 20 cm großes Rechteck, entweder auf der Bodenebne, oder indem wir die Deckelfläche der Stütze als aktuelle Arbeitsfläche festlegen, was wir in einem vorherigen Schritt gelernt haben. Das Werkzeug **Verschieben**, mit Einrasten auf Mittelpunkt und Einrasten auf Kantenmitte aktiviert, wird verwendet, um das Rechteck über der Mitte der Säule zu zentrieren.

Das Werkzeug Platte wird erneut verwendet, um aus dem Rechteck ein Strukturobjekt zu erstellen, das die Höhe 1 cm erhält und auf eine Höhe von 249 cm verschoben wird:

<img alt="" src=images/BIM_Tutorial_26.jpg  style="width:300px;">

Jetzt fügen wir die Platte an die Säule an. In FreeCAD haben BIM Objekte zwei Eigenschaften namens **Addition** und **Subtraktion** die Objekte, welche miteinander vereinigt oder voneinander subtrahiert werden, erhalten können. Um die Platte mit der Säule zu vereinigen, wähle die Platte, dann, mit gedrückter **CTRL**, wähle die Säule und verwende das<img alt="" src=images/Arch_Add.png  style="width:16px;"> **Union** Werkzeug aus dem **Modifizieren** Menü. unsere Platte ist jetzt ein Teil der Säule:

<img alt="" src=images/BIM_Tutorial_27.jpg  style="width:300px;">

Ausgehend von einfachen Formen wie **Profilen**, und dem Hinzufügen oder Heraustrennen von Objekten, können wir sehr schnell komplizierte BIM-Objekte erstellen. Dabei ist zu beachten, dass das Hinzufügen und Heraustrennen eines vorhandenen BIM-Objektes einfach geändert werden kann, indem es in der Baumansicht doppelt angeklickt und dort die Schaltflächen Hinzufügen und Entfernen verwendet werden. Dasselbe Objekt kann auch zu mehreren anderen Objekte hinzugefügt oder aus ihnen herausgetrennt werden.

<img alt="" src=images/BIM_Tutorial_28.jpg  style="width:300px;">


{{BIMTutorialAction/de
|goal1=Eine röhrenförmige CHS-Säule erstellen
|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "CHS" in o.Label]) == 1)
|goal2=Eine 20 cm x 20 cm große Platte zur Stütze hinzufügen
|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Shape" in o.PropertiesList and (FreeCAD.Units.Quantity("300 cm^3") < o.Shape.Volume < FreeCAD.Units.Quantity("500 cm^3"))]) == 1)}}



### Eine Tür hinzufügen 

Wie Stützen und Balken werden Türen und Fenster in FreeCAD aus demselben [Fenster](Arch_Window/de.md)-Objekt erzeugt. Nur ihr IFC-Typ ändert sich. Sie können unabhängig sein, oder wenn während das Werkzeug arbeitet ein Objekt ausgewählt ist, in ein anderes BIM-Objekt eingefügt werden; im letzteren Fall erzeugen sie automatisch ein Loch in diesem.

Lasst uns in eine unserer Wände eine 80 cm x 210 cm große Glastür einfügen. Wir starten mit dem Positionieren der Arbeitsebene auf einer Fläche der Wand, wodurch das genaue anbringen unserer Tür einfacher wird.

<img alt="" src=images/BIM_Tutorial_29.jpg  style="width:300px;">

Danach, während eine Wand ausgewählt ist, Im **BIM**-Menü **Tür** auswählen. Die Voreinstellong **Glastür** auswählen und für die **Breite** 80 cm sowie für die **Höhe** 210 cm eingeben. Wenn gewünscht, können auch die anderen Werte angepasst werden:

<img alt="" src=images/BIM_Tutorial_30.jpg  style="width:300px;">

Klicke dort wo du die Türe anbringen möchtest einen Punkt auf der Unterkante der Wand. Das kann schwierig sein, weil die Rasterlinien nicht unbedingt auf den Kanten der Wand liegen. Drücke die Taste **Q** während ein Gitterpunkt des Rasters eingefangen ist, und drücke sie wieder wenn die Unterkante der Wand eingefangen ist. FreeCAD erzeugt am Schnitt ihrer horizontalen/vertikalen Achsen einen neuen Fangpunkt. Verwende das, um einen geeigneten Punkt zu finden:

<img alt="" src=images/BIM_Tutorial_31.jpg  style="width:300px;">

Falls deine Türe nicht richtig platziert wurde, versuche sie mit dem **Verschieben** Werkzeug an die Richtige Position zu bewegen. Andernfalls verwende Rückgängig oder Löschen im Modellbaum und versuche es noch einmal.

Wenn alles ausgeführt wurde, solltest du eine richtig in die Wand eingefügte Türe erhalten.

<img alt="" src=images/BIM_Tutorial_32.jpg  style="width:300px;">


{{BIMTutorialAction/de
|goal1=Eine Glastür erstellen
|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Window" in o.Name]) == 1)}}



### Organisieren unseres Modells 

In unserem Modell haben wir jetzt eine schnell wachsende Sammlung von BIM Objekten. Es ist Zeit aufzuräumen. Das Erzeugen von gut organisierten Modellen, die für andere leicht verständlich sind, ist ein wichtiger Teil beim Anfertigen von qualitätsvollen BIM Modellen.

Eine erste einfache und sehr nützliche Angewohnheit ist es, unseren Objekten sinnvolle und aussagekräftige **Namen** zu geben, sodass wir sie später in der Baumansicht leicht erkennen können. Um ein Objekt umzubenennen, wird es mit der rechten Maustaste angeklickt und **Umbenennen** ausgewählt. Ein Modell, in dem die Komponenten für Andere leicht erkennbar sind, ist ein wichtiger Teil dessen, was ein gutes BIM-Modell ausmacht.

Eine andere interessante Sache ist das **Gruppieren**. Gruppen erlauben es deine Objekte im Modellbaum wie Dateien und Inhaltsverzeichnisse zu organisieren. Jedes Objekt kann nur zu einer Gruppe gehören. Gruppen werden durch Rechtsklick der Dokumentwurzel oder einer anderen Gruppe im Modellbaum und wählen von **Gruppe erstellen** aktiviert. Man kann Objekte in Gruppen hinein oder heraus ziehen.

Ein dritter Weg, um Dinge zu organisieren, ist das Verwenden von **Ebenen** (Layer). Ebenen sind unabhängig von Gruppen und wir können, wenn wir möchten, beide (Ordnungs-) Systeme gleichzeitig verwenden. Wie Gruppen erlauben auch Ebenen das einfache ein- und ausblenden einer Serie von Objekten, aber anders als Gruppen können sie nicht ineinander geschachtelt werden. Sie ermöglichen auch visuelle Einstellungen wie Farbe oder Strichbreite ihrer Kind-Objekte zu überschreiben. Ebenen werden mit dem Werkzeug Ebenen-Manager erzeugt und verwaltet, das über den Menüeintrag **Verwalten → Ebenen verwalten\...** erreicht wird. Objekte werden in Ebenen eingefügt oder daraus entfernt, indem sie in die Baumansicht hinein- oder aus ihr herausgezogen werden. Der **Ebenen-Manager** in der Hauptsymbolleiste lässt uns die aktuelle Ebene auswählen. Nach erfolgter Auswahl, wird jedes neue 2D- oder BIM-Objekt automatisch in dieser Ebene abgelegt.

Schließlich ermöglichen BIM-Anwendungen Objekte in **Stockwerken** und **Gebäuden** zu gruppieren. FreeCAD stellt diese Werkzeuge im Menü **3D/BIM** bereit. Wie Balken und Säulen verwenden Stockwerke und Gebäude dieselbe Objektart, die [Gebäudeteil](Arch_BuildingPart/de.md) genannt wird, aber mit unterschiedlichen IFC-Typen. Sie arbeiten genau so wie Gruppen. Sobald sie erzeugt sind kann man Objekte hinein- oder herausziehen. Gebäudeteile sind kompatibel mit Gruppen; man kann Gruppen darin ablegen.

<img alt="" src=images/BIM_Tutorial_36.jpg  style="width:300px;">

Für Gebäude Teile gibt es viele andere Verwendungsmöglichkeiten, erfahre mehr in der[Dokumentation](Arch_BuildingPart/de.md).

Zum Erstellen eines Gebäudeteils wird **Stockwerk** im Menü **3D/BIM** ausgewählt. Wir überprüfen, ob sein IFC-Typ auf **Building Storey** gestellt ist, und ziehen alle BIM-Wurzel-Objekte hinein (nicht nötig für eingeschlossene Objekte wie die Tür oder die Platte), also die zwei Wände, die Dachplatte und die Metallsäule.

Beachte, dass du weil Gebäude Teile in FreeCAD allgemeine Gebäude Komponenten sind, nicht gezwungen bist dein Modell in Stockwerken zu organisieren. Du kannst dich auch entscheiden deine Elemente anders zusammenzufassen. Aber das IFC Format erwartet, dass die Dinge in Stockwerken gruppiert sind. Wenn du also planst dieses Format zu verwenden, dann ist es am Besten deine Gebäude Teile als Stockwerke aufzufassen.


{{BIMTutorialAction/de
|goal1=Ein Stockwerk (level) erstellen
|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "BuildingPart" in o.Name]) == 1)
|goal2=Die vier anderen BIM-Grundobjekte zu ihm hinzufügen
|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "BuildingPart" in o.Name and (len(o.Group) == 4)]) == 1)}}



### Hinzufügen von Schnittebenen 

Eine der häufigsten Tätigkeiten, die mit einem BIM-Modell durchgeführt werden, ist das Ableiten von 2D-Zeichnungen mit Ansichten wie Grundrissen und Aufrissen. In FreeCAD gibt es, abhängig vom erwarteten Ergebnis, mehrere Möglichkeiten dies zu tun. Prinzipiell kann man wählen, zwischen dem Erzeugen von 2D-Ergebnissen im 3D-Raum, dies ist sinnvoll, wenn dort geändert oder weiterentwickelt werden soll oder wenn man mehr Kontrolle über die Exportvorgänge in die Formate wie [DXF](Draft_DXF/de.md) oder [DWG](FreeCAD_and_DWG_Import/de.md) haben möchte und dem Erstellen von 2D-Ansichten auf einem TechDraw Zeichnungsblatt, das besser zum Ausdrucken geeignet ist oder zum Export als PDF. In beiden Fällen startet man mit dem Positionieren einer [Schnittebene](Arch_SectionPlane/de.md) in dem Modell:

In beiden Fällen beginnen wir mit dem Positionieren einer [Schnittebene](Arch_SectionPlane/de.md) in unserem Modell:

<img alt="" src=images/BIM_Tutorial_37.jpg  style="width:300px;">

1.  Das Stockwerk-Objekt auswählen, das die im letzten Schritt erzeugten Objekte enthält.
2.  Eine Schnittebene einfügen, durch Auswählen des Menüeintrags **Anmerkung → Schnittebene**

Schnittebenen schneiden nicht durch das gesamte Modell, sondern nur durch Dinge die Bestandteile ihrer **Objekte** sind. Du kannst zu jeder Zeit die Schnittebene auswählen um die Bestandteile zu überprüfen und zu ändern.

Als Standard wird, um einen Grundriss zu erzeugen, die neue Schnittebene in der Mitte des gewählten Objektes oder ihrer Inhalte platziert, Blickrichtung nach unten. Aber die Schnittebene ist ein Objekt wie jedes andere und kann so wie du es benötigst verschoben oder gedreht werden. Platziere sie horizontal um einen Grundriss zu erzeugen, vertikal innerhalb des Modells um einen Schnitt zu erzeugen, oder außerhalb des Modells um einen Fasadenplan zu erzeugen.


{{BIMTutorialAction/de
|goal1=Den Haupt-Gebäudeteil auswählen
|test1=bool(len([o for o in FreeCADGui.Selection.getSelection() if "BuildingPart" in o.Name]) == 1)
|goal2=Eine Schnittebene erstellen
|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Section" in o.Name and (len(o.Objects) == 1) and ("BuildingPart" in o.Objects[0].Name)]) == 1)}}



### 2D Ansichten als Geometrie extrahieren 

Sobald deine Schnittebene platziert ist können wir aus dem was sie zeigt mit dem [Form2DAnsicht](Draft_Shape2DView/de.md) Werkzeug eine 2D Geometrie erzeugen:

<img alt="" src=images/BIM_Tutorial_38.jpg  style="width:300px;">

1.  Die Schnittebene auswählen.
2.  Eine 2D-Formansicht erstellen, durch Verwenden von **Anmerkung → Formbasierte Ansicht**
3.  Unser Objekt ist hinter den Wänden verborgen. Zum Ausblenden des Stockwerkes und der Schnittebene, werden beide in der Baumansicht ausgewählt und die **Leertaste** gedrückt; so können wir unser Ergebnis besser sehen.

<img alt="" src=images/BIM_Tutorial_39.jpg  style="width:300px;">

Die 2D-Ansicht, die wir erzeugt haben, ist ein alles-in-einem 2D-Objekt und wird im Nullpunkt (0,0) auf der Basisebene im Modell positioniert. Sie kann bewegt werden, und wird wenn sich das Modell ändert neu berechnet.

Um breitere Linien für geschnittene Flächen zu erhalten, kannst du noch eine Shape 2D Ansicht erzeugen, setze seine **Projection Mode** Eigenschaft auf \"Cutlines\" oder \"Cutfaces\" und seine **In Place** Eigenschaft auf \"Falsch\". Du wirst dann zwei Objekte haben, eines für die sichtbaren Linien und eines für die Schnittlinien, für die du unterschiedliche Linienbreiten einstellen kannst.


{{BIMTutorialAction/de
|goal1=Die Schnittebene auswählen
|test1=bool(len([o for o in FreeCADGui.Selection.getSelection() if "Section" in o.Name]) == 1)
|goal2=Eine 2D-Ansicht erstellen
|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Shape2DView" in o.Name]) == 1)
}}



### Beschriften und in 2D-CAD-Formate exportieren 

Du kannst [Text](Draft_Text/de.md), [Hinweise](Draft_Label/de.md) (Text mit Linie und Pfeil), [Maß](Draft_Dimension/de.md) auf alles im Modellraum platzieren: Entweder direkt im 3D Modell, oder in der 2D Ansicht die wir im obigem Schritt erzeugt haben. Die Wahl liegt bei dir, abhängig davon was du erzielen möchtest.

![](images/BIM_Tutorial_34.jpg )

Anmerkungen (Texte, Hinweise, Bemaßungen) werden in der aktuellen **Arbeitsebene** platziert. Stelle sicher, dass deine Arbeitsebene dort platziert ist wo du die Anmerkungen haben möchtest. So kannst du Anmerkungen in jeder Ebene des 3D Raumes platzieren: Horizontal oder vertikal. Du kannst sie nach dem Erzeugen auch verschieben und drehen.

Lass uns ein horizontales Maß zwischen den Endpunkten unserer Wände platzieren:

![](images/BIM_Tutorial_40.jpg )

1.  Die **Arbeitsebene** auf **Draufsicht** einstellen.
2.  Die Ansicht so ausrichten, dass die Basis beider Wände zu sehen sind.
3.  Den Menüeintrag **Anmerkung** → <img alt="" src=images/Draft_Dimension.png  style="width:16px;"> [Maß](Draft_Dimension/de.md) auswählen.
4.  Einen ersten Punkt am Endpunkt der linken Wand anklicken.
5.  Die **SHIFT**-Taste drücken, um das Maß horizontal oder vertikal festzulegen.
6.  Einen zweiten Punkt am Endpunkt der rechten Wand anklicken.
7.  Einen dritten Punkt anklicken, um zu zeigen wo die Maßlinie verlaufen soll.

[Maße](Draft_Dimension/de.md) haben viele Einstellungen für die Feinabstimmung ihres Aussehens sowie der Größe und Art von Texten und Pfeilen. Bevorzugte Standardwerte können unter **Bearbeiten → Einstellungen → Draft → Texte und Bemaßungen** eingestellt werden.

Lass uns jetzt einen Text hinzufügen:

![](images/BIM_Tutorial_41.jpg )

1.  Den Menüeintrag **Anmerkungen** → <img alt="" src=images/Draft_Text.png  style="width:16px;"> [Text](Draft_Text/de.md) auswählen.
2.  Eine Stelle in der 3D-Ansicht anklicken, um den Text zu positionieren.
3.  Den gewünschten Text schreiben, zum Beispiel **Pavillon**, dann die Schaltfläche **Text erstellen** anklicken oder zweimal die Eingabetaste drücken.

Es ist eine gute Idee für unterschiedliche Sätze von Anmerkungen (Pläne, Schnitte, unterschiedliche Maßstäbe, usw\...) **Gruppen** zu erzeugen:

1.  Erzeuge eine Gruppe durch Rechtsklick auf die Wurzel des Dokumentes und wähle **Erzeuge Gruppe**, benenne sie um auf \"Anmerkungen\"
2.  Wähle die vorher erzeugten Anmerkungen im Modellbaum und ziehe sie in die Gruppe



#### Exportieren nach DXF 

2D objekte wie Linien oder Kreise oder 2D Ansichten wie wir sie oben erzeugt haben oder Anmerkungen sind gut geeignet um sie in traditionelle CAD Formate wie [DXF oder DWG](Draft_DXF/de.md). Das DWG Format erfordert eine zusätzliche Software die in deinem System installiert werden muss, überprüfe die [Anleitungen](Draft_DXF/de.md) um das Notwendige zu machen.

Versuchen wir unsere 2D Arbeit nach DXF zu exportieren:

1.  Die 2D-Ansicht, das Maß und den Text auswählen
2.  Den Menüeintrag **Datei → Exportieren** auswählen, dann das **Autodesk DXFformat** auswählen, einen Dateinamen eingeben und **Exportieren** drücken.

Falls du kein anderes 2D CAD Programm verwendest, gibt es mehrere freie und open-source Anwendungen die DXF Dateien öffnen können (abgesehen natürlich von FreeCAD!) wie etwa [LibreCAD](https://librecad.org/) und [QCAD CE](https://qcad.org/).

![](images/BIM_Tutorial_42.jpg )


{{BIMTutorialAction/de
|goal1=Ein Maß erstellen
|test1=bool(len([obj for obj in FreeCAD.ActiveDocument.Objects if "Dimension" in obj.Name]))
|goal2=Einen Text erstellen
|test2=bool(len([obj for obj in FreeCAD.ActiveDocument.Objects if "Text" in obj.Name]))
}}



### 2D-Geometrie auf einem druckbaren Zeichnungsblatt erstellen 

Druckbare Zeichnungsblätter werden im Arbeitsbereich [TechDraw Workbench](TechDraw_Workbench.md) erstellt und verwaltet. Lasst uns ein neues Blatt erstellen und darauf eine Ansicht auf unser Modell anlegen:

1.  In den Arbeitsbereich **TechDraw** wechseln.
2.  Ein neues leeres Zeichnungsblatt erstellen, indem der Menüeintrag **TechDraw → Seite → Neues Zeichnungsblatt aus der Standardvorlage erstellen** ausgewählt wird.
3.  Die Schnittebene auswählen und auf dem Blatt mit **TechDraw → Ansichten von anderen Arbeitsbereichen → Objekt des Arbeitsbereichs BIM einfügen** eine Ansicht einfügen.
4.  Die Eigenschaft **Maßstab** der Arch-Ansicht ändern.

\... Fortsetzen


{{BIMTutorialAction/de
|descr=Keine Aktion für diesen Schritt ausführen
}}



### Eine IFC-Datei exportieren 

[Industry Foundation Classes](https://de.wikipedia.org/wiki/Industry_Foundation_Classes) oder kurz IFC bezeichnet ein Protokoll- und Dateiformat, zum Austauschen von BIM-Modellen zwischen Anwendungen. Wird ein Modell als IFC-Datei abgespeichert, kann es in den meisten oder sogar allen Open-Source- oder Urheberrechtlich geschützten BIM-Anwendungen geöffnet werden.

Vorgänge für IFC-Import bzw. IFC-Export werden in FreeCAD durch eine externe Software namens [IfcOpenShell](http://www.ifcopenshell.org/) ausgeführt. Auf der Seite [Arch IFC](Arch_IFC/de.md) gibt es mehr Informationen zum Installationsvorgang.

Sobald IfcOpenShell installiert ist, ist der Export eines Modells so einfach wie das Auswählen des Objektes, das exportiert werden soll oder nur des obersten Behälters (Gruppe oder Gebäudeteil), der alle weiteren Objekte enthält, die exportiert werden sollen sowie das Verwenden von **Datei → Exportieren** und dem Auswählen des IFC-Dateiformats.

Schließlich, wenn die IFC-Datei exportiert wurde, ist es immer eine gute Idee, sie vor dem Versenden an andere Personen zu überprüfen, um sicher zu sein, dass das Modell gut aussieht und keine Objekte vergessen wurden. Im Internet gibt es für viele Plattformen freie IFC Betrachter. Ein guter open-source Betrachter, der auf allen Platformen arbeitet ist [IFC++](http://ifcquery.com/). Soll die IFC-Datei weiterbearbeitet werden, könnte [Bonsai](https://bonsaibim.org) nützlich sein.

Um die Struktur und die Gültigkeit eines Modells für den IFC-Export zu testen, wird das Werkzeug **Verwalten → Überprüfungen bevorzugen\...** verwendet. Dies wird im nächsten Abschnitt besprochen.


{{BIMTutorialAction/de
|goal1=Das Werkzeug BIM Preflight öffnen und alle Tests ausführen
|test1=True if (hasattr(FreeCADGui,"BIMPreflightDone") and (FreeCADGui.BIMPreflightDone == True)) else False
}}



### BIM-Eigenschaften verwalten 

Ein Großteil dessen was ein gute BIM Modell ausmacht sind nicht geometrische Eigenschaften wie Type, Material oder spezielle Eigenschaften für einen Typ, die du deinen Objekten zuweisen kannst. Zum Beispiel eine Wand kann als tragend oder nicht tragend markiert werden. Oder als Außen- oder Innenwand. Das [IFC format](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) Format ist in dieser Hinsicht sehr vielfältig. Die Menge an Baubeschreibungen und Eigenschaften die du deinen Objekten zuteilen möchtest hängt meist von deinen Bedürfnissen ab, und wie du mit Anderen zusammenarbeitest, und welche Inhalte diese in deinem BIM Modell erwarten.

Eines ist wichtig im Kopf zu behalten: Alle BIM-/Arch-Objekte in FreeCAD unterstützen den gesamten Satz der IFC-Eigenschaften. Andere FreeCAD-Objekte, wie solche die mit anderen Arbeitsbereichen modelliert wurden, werden auch als IFC exportiert, aber es können keine ihrer IFC-Eigenschaften geändert werden. Es kann aber jedes FreeCAD-Objekt in ein BIM-Objekt umgewandelt werden, indem das Objekt ausgewählt und **3D/BIM → Komponente** verwendet wird.

Die Hauptteile an Informationen die du deinen Objekten geben kannst sind:



#### Name und Beschreibung 

Das scheint offensichtlich, aber der einfachste Weg um dein Modell für andere verständlich zu machen ist deine Objekte genau zu benennen, und, wenn sachdienlich eine Beschreibung hinzuzufügen. Dies kann man einfach machen, indem ein Objekt gewählt wird, und durch drücken von **F2** oder ändern seiner **Marken** Eigenschaft umbenannt wird.



#### Der BIM-/IFC-Typ 

Dies ist der wesentliche Teil der Information. In FreeCAD wird für jedes Objekt, dass mit dem Wand Werkzeug erzeugt wurde der IFC Typ als Standard auf \"Wand\" gesetzt. Aber du kannst das jederzeit ändern. So kann man zum Beispiel das Wand Werkzeug zum modellieren eines Balkens verwenden. Du musst nach dem Erzeugen nur seinen IFC Typ ändern. Um den IFC Typ eines Objektes zu ändern, wähle es aus, finde seinen **IFC Typ** in seinen Eigenschaften heraus, und wechsle zu einem anderen Typ aus der Aufklappliste.

Durch verwenden des IFC-Element-Managers unter dem Menüeintrag **Verwalten → IFC-Elemente verwalten** können gleichzeitig Namen, Typen und Materialien mehrerer Objekte verwaltet werden.



#### Materialien

Jedes Objekt einer Konstruktion hat ein Material. Daher ist es sinnvoll jedem Objekt eines Modells ein passendes Material, wie Beton oder Holz, zuzuordnen. Um einem Objekt ein Material zuzuweisen, wähle das Objekt, und verwende [Material Verwaltung](Arch_SetMaterial/de.md) aus dem Menü **Verwalten → Material**.



#### Eigenschaften

Jedes BIM-Objekt kann auch zusätzliche Eigenschaften erhalten, zum Beispiel um zu zeigen, dass eine Wand tragend ist oder nicht. IFC erlaubt es maßgeschneiderte Eigenschaften zu fast allem zuzuordnen, aber die meisten Typen wie Wände oder Balken haben spezielle, vordefinierte Sätze von Eigenschaften, die für gewöhnlich als Pset_WallCommon oder Pset_BeamCommon bezeichnet werden. Du kannst diese Sätze zu deinen Objekten hinzufügen, Werte von Eigenschaften in den Sätzen ändern, oder maßgeschneiderte Eigenschaften hinzufügen. Das Verwalten von IFC-Eigenschaften eines ausgewählten Objektes, oder das gleichzeitige gemeinsame Bearbeiten der Eigenschaften mehrerer Objekte wird mit dem Eigenschaften-Verwalter unter dem Menüeintrag **Verwalten → IFC-Eigenschaften verwalten\...** durchgeführt.



#### Größen

Größen wie Länge, Breite oder Höhe einer Wand können auch extra in eine IFC-Datei geschrieben werden. Sie sind nicht mit der Geometrie des Objektes verknüpft, somit gibt es keine Garantie, dass sie sich auf die aktuelle Geometrie des Objektes beziehen, wenn man diese Größen in der IFC-Datei antrifft. Allerdings erlauben diese Größen Programmen, welche die Geometrie nicht verarbeiten können, wie etwa Tabellenkalkulationen, die Hauptmaße zu erkennen. Durch Verwenden des Größen-Verwalters unter dem Menüeintrag **Verwalten → IFC-Mengen verwalten\...** lässt sich überprüfen, welche Größen nach IFC exportiert werden.

#### BIM Preflight tool 

Das IFC Format hat viele Besonderheiten, und manchmal wird die Anwendung mit der du deine IFC Datei öffnen wirst, oder die Person die deine IFC Datei empfangen wird, weitere Anforderungen haben. Ein geübter BIM Modellierer zu werden bedeutet oft mit allen diesen Besonderheiten, und damit welche Anforderungen an dein BIM Modell angefügt oder vorgegeben werden müssen, vertraut zu werden. Der BIM Arbeitsbereich von FreeCAD bietet ein BIM Überprüfungen Werkzeug, welches es dir erlaubt den Modell auf mehrere dieser Besonderheiten und meist üblichen Anforderungen zu überprüfen, und dir hilft zu entscheiden was dein Modell enthalten soll oder nicht.


{{BIMTutorialAction/de
|descr=Keine Aktion für diesen Schritt ausführen
}}



### Erkunde andere BIM Werkzeuge und andere Arbeitsbereiche 

Nimm dir einen Augenblick Zeit, um andere vorhandene BIM Werkzeuge zu erkunden. Denke daran, dass einige noch nicht fertig gestellt sind, und nicht alles machen was du von ihnen erwartest. Verwende die \"Was ist das?\" Schaltfläche, im Menü **Hilfe** zum Öffnen der Hilfe Seite jedes Werkzeuges. Das [FreeCAD forum](https://forum.freecadweb.org) ist auch ein guter Ort zum suchen oder fragen bei speziellen Problemen die du nicht lösen kannst.

FreeCAD ist eine große Familie von Arbeitsbereichen, und Werkzeuge von anderen Arbeitsbereichen sind oft praktisch. Wie wir oben gesehen haben, kann fast jedes in einem anderen Arbeitsbereich erzeugte Objekt einfach durch das Werkzeug **3D/BIM → Generische 3D-Werkzeuge → Komponente** und Angabe des richtigen IFC-Typs in ein gültiges BIM-Objekt verwandelt werden.

Es gibt im [Tutorien](Tutorials/de.md) Abschnitt der [FreeCAD documentation](https://wiki.freecadweb.org) mehr Tutorien über BIM und andere Arbeitsbereiche, und eine vollständige Video Serie von [BIM tutorials](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU) auf Youtube.


{{BIMTutorialAction/de
|descr=Keine Aktion für diesen Schritt ausführen
}}



### Hilf FreeCAD, ein besseres Werkzeug zu werden! 

FreeCAD ist eine freie Software, die von einer enthusiastischen Gemeinschaft von Anwendern entwickelt wird. Einige von ihnen entwickeln Code, und viele andere tragen in der einen oder anderen Form dazu bei, die Software zu verbessern, indem sie Dokumentation schreiben, Fehler finden und melden, Ideen einreichen, Anleitungen schreiben und viele andere Dinge. Je mehr und je aktiver wir sind, desto schneller wird die Software weiterentwickelt. Warum nicht bei uns mitmachen? Ein guter Ort, um damit anzufangen, ist der [BIM-Bereich im FreeCAD-Forum](https://forum.freecadweb.org/viewforum.php?f=23). Wir sehen uns dort!


{{BIMTutorialAction/de
|descr=Keine Aktion für diesen Schritt ausführen
}}



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [BIM](BIM_Workbench.md) > BIM ingame tutorial/de
