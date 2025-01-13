---
 TutorialInfo:e
   Topic: Modellierung
   Level: Anfänger
   Author: heda
   Time: 2 hours
   FCVersion: 0.19 or above
   Files: 
   SeeAlso: Creating_a_simple_part_with_PartDesign/de, Creating_a_simple_part_with_Draft_and_Part_WB/de
---

# Creating a simple part with Part WB/de







## Einleitung

Dieses Tutorial soll als erste Einführung in die 3D-Modellierung mit der [Part Workbench](Part_Workbench/de.md) ![](images/Switch_PartWorkbench.JPG ) von FreeCAD dienen. Nach Abschluss dieses Tutorials solltest du in der Lage sein, einfache 3D-Modelle mithilfe von Grundelementen wie Würfeln, Zylindern usw. mit einer Technik namens [Constructive Solid Geometry](https://en.wikipedia.org/wiki/Constructive_solid_geometry), kurz **CSG**-Modellierung, zu erstellen. Eine andere Möglichkeit zum Erstellen von 3D-Modellen besteht darin, eine 2D-Form zu verwenden, indem man die 2D-Form beispielsweise im 3D-Raum extrudiert oder dreht. Für eine Einführung in diese Technik folge bitte dem Schwester-Tutorial *[Erstellen eines einfachen Teils mit PartDesign](Creating_a_simple_part_with_PartDesign/de.md)*. In den beiden Tutorials wird absichtlich genau dasselbe Modell generiert, sodass der Anfänger praktische Erfahrung mit den beiden verschiedenen Techniken und ihrer Implementierung in FreeCAD erhält. Die Definition der beiden Techniken kann aus semantischer Sicht als streng getrennt angesehen werden, es gibt jedoch nichts, was einer Mischung der Techniken bei der Erstellung von Modellen direkt im Wege steht. Beim Mischen von Modellierungstechniken sind einige Einschränkungen zu beachten, die hauptsächlich mit Aspekten der Programmierung von FreeCAD zusammenhängen. Es gibt ein [drittes Tutorial](Creating_a_simple_part_with_Draft_and_Part_WB/de.md), das als erste Einführung in ein Beispiel für gemischte Modellierung gedacht ist. Dieses Tutorial verwendet den **Draft Workbench**, um ein 2D-Profil zu erstellen, das zum Extrudieren eines Festkörpers im **Part Workbench** verwendet wird, um dasselbe Modell wie in diesem Tutorial zu erstellen.

Bevor du beginnst, schau dir bitte an, wie du im 3D-Raum **[navigierst](Mouse_navigation/de.md)**. Wenn du mit der Maus über den Mausmodellwähler in der unteren rechten Ecke des FreeCAD-Fensters fahrst, wird ein Spickzettel des aktuellen Mausmodells angezeigt, wie im Bild unten.

![](images/T101pwb00-01_navi.png )

Viele CAD-Neulinge kommen beim Erlernen der Software nicht weiter. Wenn dir das passiert, suche bitte im Wiki oder Forum nach weiteren Informationen. Es ist wahrscheinlich, dass auch andere in der Vergangenheit bei der gleichen Sache nicht weitergekommen sind, sodass es bereits eine Antwort auf deine spezielle Frage gibt. Oder poste im Forum deine Fragen oder Erkenntnisse. Das Forum verfügt über mehrere Threads, in denen Benutzern bei der Erledigung aller möglichen Aufgaben geholfen wird. Diese Threads ähneln häufig Tutorials und enthalten häufig spezielle Abbildungen.



### Das Tutorial umfasst 

-   Das zu erstellende Modell
-   Verwenden des Part Workbench zum Erstellen und Bearbeiten der primitiven Bausteine
-   ​​Ändern von Farbe und Transparenz
-   Eine andere Möglichkeit, das Loch zu lokalisieren
-   Das Loch zu einem Senkloch machen
-   Ein hohles Stück herstellen
-   Eine andere Möglichkeit, die Fase zu positionieren
-   Abmessungen bearbeiten
-   Den Baum etwas anders organisieren
-   Zusammenfassung



## Das zu erstellende Modell 

<img alt="" src=images/GGTuto1_Vue.PNG  style="width:372px;">

![](images/T101pwb01-02_dims.png )



## Verwenden des Part Workbench zum Erstellen und Bearbeiten der primitiven Bausteine 

Erstelle ein neues Dokument und speichere es direkt unter einem neuen Namen. Es empfiehlt sich, das Dokument in regelmäßigen Abständen oder kurz vor größeren Vorgängen zu speichern. Wechsle dann zum **[Part Workbench](Part_Workbench/de.md)**, indem du entweder den [Workbench-Selektor](Getting_started#Exploring_the_interface/de.md) (im verlinkten Bild mit 10 gekennzeichnet) oder das Menü **View → Workbench** aufrufst. FreeCAD startet mit Symbolleisten oben, der Kombinationsansicht links und der 3D-Ansicht rechts.



### Erstelle den Hauptblock 

Drücke <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Box](Part_Box/de.md), um einen standardmäßigen festen Würfel zu erstellen. Der Würfel erscheint in der [3D-Ansicht](3D_view/de.md) und auch als neues Objekt in der [Baumansicht](Tree_view/de.md) in der Seitenleiste.

Drücke <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> [Isometric](Std_ViewIsometric/de.md), um den Würfel in 3D anzuzeigen.

![](images/T101pwb01-03_cube1.png )

Wähle den Würfel in der [Baumansicht](Tree_view/de.md) aus. In der 3D-Ansicht wird er grün. Unter der Baumansicht siehst du nun, dass der Würfel standardmäßig mit den Abmessungen **Länge x Breite x Höhe** als *10 x 10 x 10 mm* erstellt wird. Ändere diese Abmessungen gemäß der ursprünglichen Zeichnung des Modells in **100 x 30 x 50**.

![](images/T101pwb01-04_cubedims.png )

Wenn du eine Eigenschaft wie „Länge" über die Spinbox änderst, kannst du die Werte entweder eingeben oder mit dem Scrollrad nach oben oder unten verschieben. Die Pfeile zum Verschieben von Werten nach oben oder unten können natürlich auch verwendet werden. Im Bild ganz rechts oben befindet sich die Eigenschaft „Höhe" im Bearbeitungsmodus. Wenn du mit der Maus über dieser Zelle bist und das Scrollrad drehst, wird der Wert um eins nach oben oder unten verschoben.

Klicke auf <img alt="" src=images/Std_ViewFitAll.svg  style="width:24px;"> **[Alles anpassen](Std_ViewFitAll/de.md)**, um den gesamten Würfel anzuzeigen.

![](images/T101pwb01-05_cube2.png )



### Erstelle die Rundung 

Um die abgerundete Kante zu erstellen, drücke in der Symbolleiste auf <img alt="" src=images/Part_Fillet.svg  style="width:24px;"> **[Abrunden](Part_Fillet/de.md)**, wodurch das *Aufgabenfenster* für Abrundungen in der [Kombinationsansicht](Combo_view/de.md) an der Seite geöffnet wird. Ändere den Spinbox *Radius* auf 20 mm, wähle dann in der 3D-Ansicht die Breitenkante oben rechts aus und klicke auf **OK**.

![](images/T101pwb01-06_filletrad.png )

Das „Aufgabenfenster" wird geschlossen und du gelangst zurück zur Strukturansicht, die jetzt ein Filetobjekt anstelle des früheren Würfels aufweist.



### Sichtbarkeit von Kindern 

Klicke auf das Pluszeichen/\'\>\'-Zeichen, um die untergeordneten Elemente des Filets zu erweitern. In diesem Fall handelt es sich dabei um den „Würfel", den wir zuvor erstellt haben, der jedoch ausgegraut ist. Wähle den Würfel aus und drücke die Leertaste. Dadurch wird die Sichtbarkeit umgeschaltet, sodass der Würfel nun wieder sichtbar ist und das Symbol nicht mehr ausgegraut ist. Um die Auswahl des Würfels aufzuheben, klicke in einen leeren Bereich in der Strukturansicht oder der 3D-Ansicht.

![](images/T101pwb01-07_fillet.png )



### Fase erstellen 

Als nächstes erstellen wir die 30-Grad-Fase. Schalte zunächst die Sichtbarkeit des untergeordneten Würfels der Rundung um. In [Part Workbench](Part_Workbench/de.md) gibt es ein Fasenwerkzeug, aber anstatt es zu verwenden, erstellen wir die Fase mit einem anderen Block und einem booleschen Schnitt.

Erstelle eine neue <img alt="" src=images/Part_Box.svg  style="width:24px;"> **[Box](Part_Box/de.md)** mit den Abmessungen 60 x 30 x 30. Ändere den **Platzierungswinkel** auf -30 Grad.

![](images/T101pwb01-08_chamfer1.png )

Der Platzierungswinkel verwendet den **Platzierungsvektor** (Achse) als Rotationsachse. Die Standardeinstellung ist die Z-Achse, die nicht mit unserer Zielrichtung übereinstimmt. Durch Ändern des Platzierungsvektors auf die **Y-Achse** wird die gewünschte Ausrichtung des Schneidwerkzeugs für die Fase erzeugt.

![](images/T101pwb01-09_chamfer2.png )

Die gleiche Platzierung kann auch mit anderen Werten erreicht werden, das einfachste alternative Beispiel für eine gleiche Platzierung ist ein Winkel von +30 Grad und eine Y-Achse von -1.



#### Python-Konsole 

Außerdem muss die Position angepasst werden. Wenn man sich die Zeichnung des fertigen Teils ansieht, gibt es keine direkte Dimension, die für die beabsichtigte Verschiebung nach oben verwendet werden kann. Da die Aufwärtsdimension die benötigte ist, müssen wir sie berechnen. Lass uns für diese Berechnungen die integrierte **[Python-Konsole](Python_console/de.md)** verwenden, es handelt sich um grundlegende Trigonometrie. Wenn die FreeCAD Python-Konsole für dich nicht sichtbar ist, klicke einfach mit der rechten Maustaste auf einen leeren Bereich im Symbolleistenbereich und aktiviere die *Python-Konsole*. Sie sollte dann im Arbeitsbereich erscheinen. Wenn du dort bist, solltest du auch die **[Berichtsansicht](Report_view/de.md)** hinzufügen, falls sie nicht bereits sichtbar ist. Die *Berichtsansicht* bietet meistens nützliche Informationen oder sogar Hinweise, was als Nächstes für verschiedene Befehle zu tun ist.

![](images/T101pwb01-10_pyconsole.png )

Nach dem Importieren des Moduls **[math](https://docs.python.org/3/library/math.html#module-math)** aus den Standardbibliotheken in Python können wir die Formel *(50 - math.tan(math.radians(30)) \* 50)* verwenden, um die Distanz in Z-Richtung zu ermitteln, um die der Block verschoben werden soll. Kopiere das Ergebnis der Formel aus der Python-Konsole und füge es in die Z-Position für **Cube001** ein. Das für den Fasenschnitt zu verwendende *Werkzeug* ist jetzt richtig ausgerichtet und positioniert.

![](images/T101pwb01-11_chamfer3.png )



#### Ausdrücke

Man muss nicht unbedingt die Python-Konsole verwenden, um die Berechnung durchzuführen. In den meisten Fällen, wenn es um numerische Parameterwerte geht, hat FreeCAD eine Abkürzung zu einem eingebauten Rechner. Dieser heißt in FreeCAD **[Ausdrücke](Expressions/de.md)**. Du kannst den *Ausdrucksmodus* aufrufen, indem du zuerst in die Spinbox für die Z-Position klickst. Auf der rechten Seite erscheint ein kleines bläuliches kreisförmiges Symbol.

![](images/T101pwb01-12_expression1.png )

Wenn du auf dieses Symbol klickst, wird ein neues Fenster „Formeleditor" geöffnet, in dem du Formeln und Ausdrücke wie unten gezeigt eingeben kannst. Die Verwendung von Ausdrücken ist ein leistungsstarkes Werkzeug, da du auf Parameter aus dem Modell zugreifen kannst, wodurch alle Parameter im Modell effektiv als Variablen verfügbar werden, die beim Erstellen eines Ausdrucks verwendet werden können. Kurz gesagt, in unserer Formel könnten wir im Formeleditor statt der Zahl 50 einen „benannten Parameter" eingeben, der den Wert 50 aus dem Würfel enthält, mit dem Vorteil, dass die Position der Fase automatisch angepasst wird, wenn wir die „Höhe" des Würfels ändern. Der Wert 50 im aktuellen Modell wird als „Cube.Length" bezeichnet, d. h. die Eigenschaft „Länge" der Feature „Cube". Weitere Informationen hierzu findest du im Wiki.

![](images/T101pwb01-13_expression2.png )

Um den Schnitt auszuführen, wähle bei gedrückter **Ctrl**-Taste zuerst die **Rundung** in der Strukturansicht und dann den zuletzt erstellten Würfel (mit dem Namen **Cube001**) und drücke schließlich in der Symbolleiste die Schaltfläche <img alt="" src=images/Part_Cut.svg  style="width:24px;"> **[Schnitt](Part_Cut/de.md)**. Deine Strukturansicht sollte nun wieder ein einzelnes Objekt in der Wurzel mit dem Namen **Cut** sein.

![](images/T101pwb01-14_model1.png )



#### Die Symbolleisten 

Eine Randbemerkung zu den Symbolleisten, da sie der typische Weg sind, Befehle aufzurufen. Obwohl es eine Grundeinstellung für das Layout der Symbolleisten gibt, kann sich das tatsächliche Layout auf deinem Computer als weniger als ideal erweisen. In solchen Fällen lässt es sich leicht anpassen. Betrachte den oberen Abschnitt des folgenden Bildes. Es gibt zwei Reihen von Symbolleisten und nur eine begrenzte Anzahl der Symbolleistenschaltflächen von [Part Workbench](Part_Workbench/de.md) ist sichtbar. Der einfachste Weg, mehr Symbolleistenschaltflächen anzuzeigen, besteht darin, das FreeCAD-Fenster zu maximieren, sofern es natürlich nicht bereits maximiert ist.

Üblicher ist es, das Layout der Symbolleisten an deine Bedürfnisse und deinen Computer anzupassen. Die Neupositionierung erfolgt über den Griff links neben jeder Symbolleiste. Du kannst einfach auf den Griff klicken und ihn an eine neue Position ziehen. Im unteren Abschnitt des folgenden Bildes wurden die Symbolleistenpositionen angepasst, sodass ihr vollständiger Inhalt angezeigt wird. Änderungen an den Symbolleistenpositionen bleiben über Sitzungen hinweg bestehen.

![](images/T101pwb01-141_toolbars.png )



#### Das Messwerkzeug 

Mit dem **[Messwerkzeug](Part_Workbench#Measure/de.md)** im **Part Workbench** kannst du überprüfen, ob unsere Berechnung und Platzierung der Fase korrekt ist. Drücke die Schaltfläche <img alt="" src=images/Part_Measure_Linear.svg  style="width:24px;"> **[Lineares Messen](Part_Measure_Linear/de.md)** und ein *Aufgabenfenster* wird geöffnet. Wähle dann die beiden Endpunkte einer Seite der Fase aus.

![](images/T101pwb01-15_model1measure1.png )

Es wird mit einer X-Dimension von 50 mm ausgemessen. Lösche die Messung und schließe den Dialog.



### Loch erstellen 

Um das Loch zu machen, drücke die Schaltfläche <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> **[Zylinder](Part_Cylinder/de.md)**, stelle den *Radius* auf 5 mm und die *Höhe* auf 50 mm ein.

![](images/T101pwb01-16_cyl1.png )

Als nächstes müssen wir das Loch entsprechend den Abmessungen in der Zeichnung positionieren. Ändere die Ansicht in die Ansicht <img alt="" src=images/Std_ViewTop.svg  style="width:24px;"> **[Top](Std_ViewTop/de.md)**, klicke dann in der Strukturansicht mit der rechten Maustaste auf den **Zylinder** und wähle im Popup-Menü **Transformieren** aus.

![](images/T101pwb01-17_cyl1translate.png )

Ändere das *Translationsinkrement* auf 5 und verwende den roten und grünen Pfeil, um den Zylinder in die richtige Position zu bringen. Verschiebe ihn 15 mm in y-Richtung und 65 mm in x-Richtung, indem du die Pfeilenden mit der Maus ziehst. Klicke auf **OK**, um das Dialogfeld *Transformieren* zu schließen. Um das Loch zu machen, drücke die Taste **Strg** und wähle in der Strukturansicht **Schnitt** und **Zylinder** aus. Drücke dann in der Symbolleiste die Schaltfläche <img alt="" src=images/Part_Cut.svg  style="width:24px;"> **[Schnitt](Part_Cut/de.md)**. Deine Strukturansicht sollte wieder ein einzelnes Objekt in der Wurzel mit dem Namen **Cut001** haben.

Herzlichen Glückwunsch, das Modell ist nun fertig.

![](images/T101pwb01-18_model1complete.png )

Lasse uns nun, nachdem das Basismodell fertig ist, verschiedene Möglichkeiten zur Änderung dieses Modells erkunden. Einige Beispiele beziehen sich auf das Erscheinungsbild, zusätzliche Funktionen oder einfach eine andere Möglichkeit, dasselbe zu tun.



## Ändern der Farbe und Transparenz 

Es gibt verschiedene Möglichkeiten, das Erscheinungsbild von Objekten zu ändern. In diesem Fall verwenden wir die Registerkarte „Ansicht" im Eigenschaftenbereich der Kombinationsansicht. Wähle zunächst das Objekt in der Strukturansicht aus und bearbeite dann über die Registerkarte „Ansicht" (unten in der Kombinationsansicht) beliebige Eigenschaften wie Linienfarbe, Formfarbe oder Transparenz.

![](images/T101pwb02-01_appearance1.png )

Leider ist es etwas schwierig zu erkennen, wie das Objekt nach der Anpassung des neuen Erscheinungsbilds aussehen wird, wenn es ausgewählt ist. Um das Endergebnis zu sehen, muss das Objekt abgewählt werden. Hier ist das neue Erscheinungsbild des Modells, bei dem man das Durchgangsloch jetzt auch in der Iso-Ansicht sehen kann. Eine weitere Möglichkeit, das Erscheinungsbild zu bearbeiten, ist über das Menü **Ansicht → ![](images/)_Erscheinungsbild**.

![](images/T101pwb02-02_appearance2.png )



## Eine andere Möglichkeit, das Loch zu lokalisieren 

Führe einen „Speichern unter" unter einem neuen Namen durch. Lösche dann den Schnitt, der das Loch hinzugefügt hat, und verschiebe den Zylinder zurück in die Nullposition. Dein Modell sollte wie im Bild unten aussehen, das der Ausgangspunkt für die Verwendung einer anderen Technik ist, um das Loch in der Mitte der oberen Fläche zu lokalisieren. Beachte, dass die Farbe wieder zum Standardgrau zurückgekehrt ist. Die Änderung im Erscheinungsbild betraf das ausgeschnittene Objekt, das jetzt gelöscht ist.

![](images/T101pwb03-01_cyl.png )

Dieses Mal wird der <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> **[Draft Workbench](Draft_Workbench/de.md)** verwendet, um das Loch zu lokalisieren. Das Loch muss wie zuvor in der Mitte der oberen Fläche liegen, was dem Mittelpunkt der Diagonale der oberen Fläche entspricht.

Beginnen Sie damit, die Workbench auf **Draft** umzustellen. Möglicherweise erscheint in der 3D-Ansicht ein *Raster*. Die Sichtbarkeit des Rasters kann mit <img alt="" src=images/Draft_ToggleGrid.svg  style="width:24px;"> [Raster umschalten](Draft_ToggleGrid/de.md) in der Symbolleiste umgeschaltet werden. Wenn du die **[Fang](Draft_Snap.md)**-Funktionalität in der **Entwurfs-Workbench** verwendest, ist es hilfreich, nur die gewünschten *Fangarten* aktiviert zu haben. Diesmal reicht es aus, *Endpunkt, Mittelpunkt und Kreiszentrum aktiviert* zu lassen, sodass die Einstellungen für das Fangen ungefähr wie unten aussehen sollten.

![](images/T101pwb03-02_snap.png )

Der Punkt, an dem die Mitte des Zylinders platziert werden soll, lässt sich finden, indem man eine Diagonale als Hilfslinie erstellt und die Mitte des Zylinders und den Mittelpunkt der Diagonale verwendet, um die Punkte zu identifizieren, zwischen denen man sich bewegen möchte. Es stellt sich jedoch heraus, dass wir nicht einmal Hilfslinien erstellen müssen, sondern auf bereits vorhandene Volumengeometrie zurückgreifen können.

Wähle den **Zylinder** in der Strukturansicht aus (er wird in der 3D-Ansicht grün) und drücke die Schaltfläche <img alt="" src=images/Draft_Move.svg  style="width:24px;"> **[Verschieben](Draft_Move/de.md)** in der Symbolleiste. Ein *Aufgabenfenster* zum Verschieben von Objekten wird geöffnet. Stelle sicher, dass *Kopieren* nicht aktiviert ist.

![](images/T101pwb03-03_move.png )

Bewege dann die Maus auf die Oberseite des Zylinders, so dass du in der Mitte des Kreises einen „weißen Punkt" siehst, wie im linken Bild unten. Zusammen mit dem Zentrumssymbol neben dem Mauszeiger bedeutet dies, dass ein Mausklick mit der linken Taste zum weißen Punkt führt.

![](images/T101pwb03-04_snapselect.png )

Wenn du den weißen Punkt auf der oberen Fläche hast, klicke mit der linken Maustaste und wiederhole dies für die obere quadratische Fläche des Hauptkörpers, wie im rechten Bild oben, und bestätige die Auswahl mit einem Klick mit der linken Maustaste. Die Fangfunktion verwendet den „Massenmittelpunkt" für jede Art von Fläche, und in diesem Fall ist der Massenmittelpunkt derselbe wie der gesuchte geometrische Mittelpunkt. Du wirst inzwischen bemerkt haben, dass die Bewegung des Zylinders animiert ist, sodass du immer siehst, was passieren wird.

Durch erneutes Wiederholen des Schritts des **Boolescher Schnitt** von vorhin wird das Durchgangsloch erstellt, das das Modell vervollständigt. Mithilfe des **linearen Messwerkzeugs** im Part Workbench wird überprüft, ob das Loch richtig platziert ist. Die Messung kann nur zwischen *Punkten*\' durchgeführt werden, daher wird die Messung vom Nullpunkt des Hauptkörpers bis zum Nahtpunkt des Zylinders durchgeführt. Dies bedeutet, dass der richtige Abstand 70 mm beträgt und nicht die 65 mm, die in der Zeichnung angegeben sind, um den zusätzlichen Radius zu berücksichtigen, der im Abstand enthalten ist.

![](images/T101pwb03-05_modelmeasure.png )



## Das Loch als Senkloch erzeugen 

Wechsle zurück zum [Part Workbench](Part_Workbench/de.md) und erstelle einen *Kegel*, indem du in der Symbolleiste auf die Schaltfläche <img alt="" src=images/Part_Cone.svg  style="width:24px;"> **[Kegel](Part_Cone/de.md)** klickst. Ändere *radius1* auf 0 mm und *radius2* auf 7 mm -- dies ergibt eine 2 mm *Senkung* am Radius. Wenn die *Höhe* des Kegels 7 mm beträgt, ergibt sich ein oberer Winkel des Kegels von 90 Grad bzw. ein Senkwinkel von 45 Grad. Erwähnenswert ist, dass man auch hier wieder die Operation <img alt="" src=images/Part_Chamfer.svg  style="width:24px;"> [Fase](Part_Chamfer/de.md) verwenden könnte.

Wenn du mit FreeCAD arbeitest, wirst du ständig mit mehreren verschiedenen Möglichkeiten konfrontiert, scheinbar dasselbe Ergebnis zu erzielen. Es gibt kaum eine absolute Wahrheit darüber, was der richtige Weg ist, um ein bestimmtes Endergebnis zu erzielen. Wenn du es jedoch in einem bestimmten Kontext betrachtest, kann ein bestimmter Arbeitsablauf flexibler sein, die tatsächliche Verwendung späterer Funktionen ermöglichen usw. Die Art und Weise, wie du 3D-Modelle erstellst, wird sich im Laufe der Zeit weiterentwickeln, während du im Laufe der Zeit immer mehr über die Funktionen und Möglichkeiten von FreeCAD lernst.

![](images/T101pwb04-01_cone.png )

Verschiebe den Kegel so, dass er „konzentrisch" zum Loch und „koplanar" zur oberen Hauptfläche ist. Verwende dazu eine der zuvor in diesem Tutorial beschriebenen Methoden.

Im Bild unten wird die Bewegung mit *Transform* und einer *Inkrement*-Einstellung von 1 mm vorgenommen, da der Kegel eine charakteristische Abmessung von 7 mm hat, was bedeutet, dass die frühere Inkrementeinstellung von 5 mm keine korrekte Positionierung ermöglicht. Die Darstellung <img alt="" src=images/Std_DrawStyleWireFrame.svg  style="width:24px;"> **[Wireframe](Std_DrawStyle#Wireframe/de.md)** wird verwendet, um leichter zu erkennen, dass sich der Kegel in der richtigen Position befindet.

![](images/T101pwb04-02_conetranslate.png )

Um das Modell zu vervollständigen, verwenden wir den Befehl <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> **[Boolean](Part_Boolean/de.md)**, anstatt zuerst Objekte auszuwählen, und wenden eine bestimmte Boolesche Operation an. Drücke die Symbolleistenschaltfläche und ein „Aufgabenfenster" wird wie im folgenden Bild links geöffnet.

![](images/T101pwb04-03_boolean.png )

Drei Elemente müssen angegeben werden: der „Operationstyp", die „erste Form" und die „zweite Form". Der Kegel soll geschnitten werden, dies wird in diesem Befehl „Differenz" genannt, statt „Schnitt". Die erste Form ist unser „Cut001" und wird unter „Verbindungen" aufgeführt, da sie aus mehreren Festkörpern besteht. Die zweite Form ist der „Kegel". Sobald die richtigen Einstellungen für den Befehl vorgenommen wurden, klicke auf die Schaltfläche **Übernehmen**, um die Operation auszuführen. Dies wurde alles im Bild rechts durchgeführt, und dort kann man auch sehen, dass jetzt eine „Verbindung" „Cut002" aufgeführt ist, dies ist unsere endgültige Modellform. Nachdem wir das Erscheinungsbild geändert haben, sieht das endgültige Modell so aus.

![](images/T101pwb04-04_modelcomplete.png )



## Ein hohles Stück herstellen 

Führe „Speichern unter" unter einem neuen Namen durch. FreeCAD verfügt über alle typischen Operationen eines 3D-Modellierers, eine davon ist <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> **[Thickness](Part_Thickness/de.md)**, die zum „Aushöhlen" von Teilen verwendet wird.

Drehe die Ansicht, sodass die Unterseite des Modells sichtbar ist.

![](images/T101pwb05-01_frombottom.png )

Wähle die *Unterseite* des Modells aus, wähle dann im [Part Workbench](Part_Workbench/de.md) <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> **[Dicke](Part_Thickness.md)** und der Bildschirm sollte wie unten aussehen.

![](images/T101pwb05-02_thickness_cmd.png )

Klicke auf **OK**. Wie du siehst, befindet sich jetzt ein „Radius" auf dem ausgehöhlten Teil.

![](images/T101pwb05-03_thickness_dimension.png )

Außerdem beträgt die Breite des Teils jetzt 32 mm, sodass die „Dicke" nach „außen" angewendet wurde. Lass uns das bearbeiten, doppelklicke in der Strukturansicht auf das Modell und ändere die Einstellungen für „Verbindungstyp" in „Schnittpunkt" und die Einstellung für „Dicke" auf -1.

![](images/T101pwb05-04_thickness_modify.png )

Jetzt beträgt die Außenbreite des Teils wie zuvor 30 mm und die Ecken sind alle scharfe Ecken.

![](images/T101pwb05-05_thickness_modified.png )



## Eine andere Möglichkeit, die Fase zu positionieren 

Führe einen „Speichern unter" unter einem neuen Namen durch. Lösche dann die Features, sodass das Modell wie unten dargestellt aussieht.

![](images/T101pwb06-01_startingpoint.png )

Erstelle einen **Würfel** mit den Abmessungen **30 x 30 x 60**, der wie unten dargestellt aussieht.

![](images/T101pwb06-02_with_cube.png )

Ändere die **Platzierung**, indem du zuerst eine Drehung um -120 Grad um die Y-Achse durchführst.

![](images/T101pwb06-03_rotated_cube.png )

Ändere abschließend die Position auf **X=50** und **Z=50** und führe den *Schnitt* aus, um dasselbe Ergebnis wie zuvor zu erzielen.

![](images/T101pwb06-04_cube_cut.png )

Dies unterstreicht einmal mehr, dass es immer mehrere Möglichkeiten gibt, dasselbe Ergebnis zu erzielen, was bei der 3D-Modellierung ein wiederkehrendes Thema ist. Wenn es um grundlegende Geometrien oder Festkörper geht, kann man in FreeCAD verschiedene Arbeitsbereiche sowie verschiedene Befehle verwenden und trotzdem die gleiche äußere Form eines Festkörpers erhalten. Du musst einfach deinen eigenen Weg zu einer Reihe bevorzugter Werkzeuge und Arbeitsabläufe finden, mit denen du vertraut bist. Die Modellierung in parametrischem 3D ist ein Prozess des ständigen Lernens und erfordert Übung, um sie zu beherrschen.



## Bearbeiten von Abmessungen, Oberflächenfarben und TNP 

FreeCAD ist ein parametrischer 3D-Modellierer, mit dem du jede „Platzierung" oder „Dimension" ändern kannst und das Modell entsprechend aktualisiert wird. Im Allgemeinen funktioniert dies, aber es ist möglich, dass ein Modell beim Bearbeiten beschädigt wird -- beispielsweise, wenn eine Rundung auf einer Kante basiert, die aufgrund der Bearbeitung nicht mehr existiert. Wenn ein Modell während der Bearbeitung beschädigt wird, wird dies als „TNP, [Topologisches Benennungsproblem](Topological_naming_problem/de.md)" bezeichnet.

Experimentiere mit der Änderung von Abmessungen und Platzierungen, um zu sehen, ob du das Modell beschädigen kannst. Vergiss nicht, das Modell nach Änderungen bei Bedarf neu zu berechnen. Dies kannst du mit der Schaltfläche <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Aktualisieren](Std_Refresh/de.md) in der Symbolleiste tun. Wenn das Symbol ausgegraut ist, muss das Objekt nicht aktualisiert werden.



### Zylinder neu positionieren 

Hier siehst du ein Beispiel für einen Zylinder, der mithilfe der Funktion „Transformieren" von der Mitte auf eine Seite des Hauptkörpers verschoben wurde. Wie auf dem Bild zu sehen ist, befindet sich der Kegel noch immer in seiner ursprünglichen Position und wird durch die Verschiebung des Zylinders nicht beeinflusst.

![](images/T101pwb07-01_cylindermoved.png )

Wenn du den Zylinder bewegst und die Außenfläche durchbrichst, verlierst du in Version 0.19 einen Teil der Farbeinstellungen deines Modells. FreeCAD kehrt in der 3D-Ansicht zu den benutzerdefinierten Standardeinstellungen für Formfarben und Transparenz zurück. Die Form **Cut002** zeigt jedoch immer noch die Farben und Transparenz, die sie vorher hatte, wie im Bild unten zu sehen.



### Farben korrigieren 

![](images/T101pwb07-02_wrongcolor.png )

So kannst du die Transparenz wiederherstellen. Ändere zunächst die Transparenz um einen Punkt nach oben oder unten und dann zurück, um die Transparenz wiederherzustellen. Den gleichen Trick kannst du mit der Formfarbe anwenden. Eine andere Möglichkeit, die Farbe wiederherzustellen, besteht darin, in der Strukturansicht mit der rechten Maustaste auf Cut002 zu klicken und im Kontextmenü Farben festlegen auszuwählen. Klicke im angezeigten Aufgabenfenster auf **Auf Standard festlegen**, um die Farbe auf die in den Ansichtseigenschaften festgelegte Farbe zurückzusetzen.

![](images/T101pwb07-03_set_colors.png )

Mit dem Befehl **Farben festlegen** kannst du einzelne Flächen einer Form auswählen und für die ausgewählten Flächen eine eindeutige Farbe festlegen.



### Mehrere Festkörper 

Ein weiteres Beispiel, bei dem der Würfel, der die Fase bildet, verschoben und gedreht wurde.

![](images/T101pwb07-04_3solids.png )

Wie man beim Neupositionieren der Fase auf diese Weise sehen kann, sind das Endergebnis „3 disjunkte Festkörper". [Part Workbench](Part_Workbench/de.md) lässt dies zu, [PartDesign Workbench](PartDesign_Workbench/de.md) nicht. Entweder erhälst du einen „Fehler wegen mehrerer Festkörper" oder es werden einfach nicht alle Festkörper dargestellt.

### TNP

Kehren wir zum ursprünglichen, fertigen Modell zurück und sehen wir uns an, wie die Flächen benannt sind.

Hier wurde die **[Auswahlansicht](Selection_view/de.md)** aktiviert, um deutlich zu zeigen, was ausgewählt ist und was nicht. Außerdem wurde die Farbgebung angepasst, sodass die Auswahl leichter zu erkennen ist.

![](images/T101pwb07-05_face2and9.png )

Wenn du eine Seitenfläche und die Zylinderinnenfläche auswählst, werden diese intern als Fläche „2" und „9" bezeichnet, wobei Fläche „2" die Seitenfläche ist. Die Nummerierung der Flächen kann bei dir anders sein.

Durch Verschieben des Zylinders, sodass die Aushöhlung auf der Seitenfläche endet, und Auswählen der Flächen erhält man jetzt eine andere Nummer für die zylindrische Fläche.

![](images/T101pwb07-06_newfacenumbers.png )

Fläche 2 ist die rechte Seite der ursprünglichen Fläche 2, die linke Seite der früheren Fläche 2 ist jetzt Fläche 8. Der zylindrische Teil war Fläche 9, ist jetzt aber Fläche 7. FreeCAD weist die Nummerierung neu zu und die Reihenfolge bleibt nicht unbedingt erhalten. Die Gesamtzahl der Flächen im ersten Modell beträgt 10, in der Version mit der zylindrischen Fläche, die die Seitenfläche durchstößt, beträgt die Gesamtzahl der Flächen 11. Daher muss die Flächennummerierung offensichtlich geändert werden, wenn sich die sogenannte „Topologie" ändert. Dies fühlt sich wahrscheinlich wie ein winziges Detail an, erweist sich aber als ziemlich wichtig in parametrischem 3D-CAD. Stelle dir vor, du hast die zylindrische Fläche als Referenz für ein anderes Feature verwendet, sie hieß früher Fläche 9, heißt jetzt aber Fläche 8. Der Verweis auf die beabsichtigte zylindrische Oberfläche geht verloren. Da FreeCAD, zumindest in den aktuell veröffentlichten Versionen, die „beabsichtigte Fläche" nicht verfolgt, sondern nur die „nummerierte Fläche", bricht ein Modell zusammen, wenn auf eine Fläche verwiesen wird, die später neu nummeriert wird. Dies wird als **TNP, [Topologisches Benennungsproblem](Topological_naming_problem/de.md)** bezeichnet.

Du wirst ermutigt, zu lernen, wie du durch TNP beschädigte Modelle vermeiden kannst. Weitere Informationen findst du [an anderer Stelle im Wiki](Topological_naming_problem/de.md), wo es hauptsächlich um einen „skizzengesteuerten" Workflow geht. Der zugrunde liegende Mechanismus ist jedoch derselbe. Die hier für Flächen beschriebene Neunummerierung gilt für alle geometrischen Objekte, Flächen, Kanten und Eckpunkte.



## Den Baum etwas anders organisieren 

Führe ein „Speichern unter" unter einem neuen Namen durch. Lösche dann alle Schnitte, sodass am Ende ein Modell wie unten abgebildet entsteht.

![](images/T101pwb08-01_primitives.png )

Wenn du den **Part Workbench** verwendest und funktionsreiche Festkörper modellierst, kann die Baumstruktur eines Festkörpers schwer zu durchschauen sein. Bisher haben wir ein Primitiv/Feature erstellt und eine Boolesche Operation angewendet. Im Part Workbench kannst du Primitive in einer Booleschen Operation bündeln. In unserem Fall haben wir den Zylinder, den Kegel und den Würfel, die alle eine geschnittene Boolesche Operation sind.

Anstatt für jedes Grundelement einen Schnitt vorzunehmen, können wir zunächst eine Boolesche Vereinigung anwenden, <img alt="" src=images/Part_Fuse.svg  style="width:24px;"> **[Fuse](Part_Fuse/de.md)** die für den Booleschen Schnitt vorgesehenen Grundelemente verschmelzen und dann den *Schnitt* zwischen der **Rundung** und der **Fusion** vornehmen.

Bei diesem Ansatz sieht die Strukturansicht wie unten aus. Dabei handelt es sich lediglich um eine andere Möglichkeit, dasselbe Modell zu erstellen. Vergleiche dies mit der ursprünglichen Strukturansicht. Keine ist besser als die andere. Bei der Erstellung komplexerer Modelle kann jedoch ein Ansatz gegenüber dem anderen Vorteile hinsichtlich der einfacheren Änderung/Neuorganisation des Modells haben, falls erforderlich.

![](images/T101pwb08-02_fused.png )



## Zusammenfassung

Nachdem du das Tutorial durchgearbeitet hast, bist du nun etwas mit der Benutzeroberfläche von FreeCAD vertraut und hast die Grundlagen der Verwendung des **Part Workbench** gelernt. Du solltest nun in der Lage sein, einfache Modelle nach deinen eigenen Wünschen zu erstellen. Der **Part Workbench** ist eine der Workbenches, die zum Erstellen von Festkörpern verwendet werden können, der **PartDesign Workbench** ist ein anderer. Die verschiedenen Workbenches haben unterschiedliche Fähigkeiten und Arbeitsabläufe. Das vollständige Erlernen von FreeCAD, insbesondere unter Berücksichtigung aller Add-Ons und Makros, dauert Jahre, also erkunde weiterhin neue und andere Möglichkeiten zum Erstellen von Modellen -- nimm an verschiedenen Tutorials im Wiki teil, das Lernen hört nie auf, wenn du mit FreeCAD arbeitest. Es wird empfohlen, dass du als Nächstes *Skizzen* und die **PartDesign Workbench** lernst, wenn dein Schwerpunkt auf dem Erstellen von Festkörpern liegt. Wenn dein Schwerpunkt auf dem Modellieren von Gebäuden liegt, solltest du als Nächstes die Workbenches **Draft** und **Arch** lernen.

Schließlich wird FreeCAD von Freiwilligen in ihrer Freizeit entwickelt. Wenn du die Fähigkeiten von FreeCAD weiter verbessern möchtest, kannst du [zu FreeCAD beitragen](Help_FreeCAD/de.md), beispielsweise durch die Verbesserung der Dokumentation.



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > Creating a simple part with Part WB/de
