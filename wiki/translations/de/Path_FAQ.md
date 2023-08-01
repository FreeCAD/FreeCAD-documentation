# Path FAQ/de
## Wie viele Achsen kann der Pfad Arbeitsbereich handhaben? 

Zur Zeit kann die Version 0.18, Pfad Arbeitsbereich bis zu 3 Achsen Fräsen handhaben. Derzeit wird die 4. Achsen Fähigkeiten für die nächste offizielle Version entwickelt, wobei einige Pfad Arbeitsbereich Abläufe bereits auf den grundlegenden 4. Achsen Status aufgerüstet wurden.

[Anfang](#top.md)

## Warum scheint es, dass der Pfad Arbeitsbereich in manchen Fällen mehr als einen Weg bietet, einen Ablauf festzulegen? 

Der Pfad Arbeitsbereich bietet vorhandene Werkzeuge für viele Fräsbearbeitungen, weitere sind in Arbeit, und da FreeCAD quelloffen ist, steht dem Anwender nichts im Wege, seine eigene Funktionalität zu erstellen.

Wie bei der 3D Modellierung stehen oft mehrere Methoden zur Verfügung, die für verschiedene Arbeitsgänge von Vorteil sein können. In einigen Fällen werden Kombinationen von Bearbeitungen verwendet, um eine vollständige Bearbeitung des Materials zu ermöglichen.

Ein gängiges Beispiel ist, dass ein Konturschnitt aus Kanten oder Flächen erzeugt werden kann. In einigen Fällen ist eine geometrische Eingabe gegenüber einer anderen vorteilhaft.

[Anfang](#top.md)

## Warum ändert das Aufbereiten eines Arbeitsvorgangswechsel die Position im Auftragsarbeitsablauf, angezeigt in der Liste der Arbeitsgänge? 

Alle Ergänzungen zum Arbeitsauftrag\--einschließlich Änderungen und Arbeitsgangskopien\--werden am Ende des Auftrags Arbeitsablaufs angehängt. Wenn das die korrekte Arbeitsauftragsfolge zerreißt, muß sie im Arbeitsauftragseditor-\>Arbeitsablauf Reiter neu geordnet werden.

[Anfang](#top.md)

## Was ist der Unterschied zwischen der lichten Höhe und der sicheren Höhe? 

Genauere Informationen ist unter [Tiefen und Höhen](Template:Depths/Heights.md) verfügbar.

[Anfang](#top.md)

## Was ist die typische Anwendung des EinrichtungsBlatts? 

Das EinrichtungsBlatt ist ein spezielles Tabellenblatt, das in einem Auftrag enthalten ist, in der Eigenschaftsansicht geändert wird und nur über die Pfad Arbeitsbereich zugänglich ist. Es bietet einen Mechanismus für erfahrene Benutzer, um Aspekte ihres Auftrags zu konfigurieren, indem sie Werte und Ausdrücke verwenden, die im EinrichtungsBlatt enthalten sind.

Die aktuellen Eingaben für Tiefen-, Höhen- und Werkzeugsteuerungen umfassen:

1.  Endtiefe Ausdruck \-- OpFinalDepth
2.  Anfangstiefe Ausdruck \-- OpStartDepth
3.  Step Down Ausdruck \-- Standardmäßig OpToolDiameter. Dieser Ausdruck wird für jeden Arbeitsgang verwendet, um den Standardabstiegswert zu berechnen, der auf dem Durchmesser des Werkzeugs basiert, der in der zugehörigen Werkzeugsteuerung definiert ist.
4.  Lichte Höhe Ausdruck \-- StartDepth+SetupSheet.ClearanceHeightOffset
5.  Lichte Höhe Versatz Wert \-- Enthält den in Ausdrücken verwendeten Wert.
6.  Sichere Höhe Ausdruck \-- StartDepth+SetupSheet.SafeHeightOffset
7.  Sichere Höhe Versatz Wert \-- Enthält den in den Ausdrücken verwendeten Wert.
8.  Horizontaler Eilwert\-- Stellt den Standardwert bereit, mit dem die horizontale Eilgeschwindigkeit für alle Werkzeugsteuerungen anfänglich ausgefüllt wird.
9.  Vertikaler Eilwert\-- Stellt den Standardwert bereit, mit dem der vertikale Eilvorschub für alle Werkzeug Steuerungen anfänglich gefüllt wird.

Dies bietet Flexibilität. Beispielsweise werden Standardausdrücke bereitgestellt, die jedoch vom Benutzer überschrieben werden können. Die Änderung kann sogar die Standardgleichung auf einen Wert reduzieren, wenn dies dem Benutzer passt.

[Anfang](#top.md)

## Was ist die typische Anwendung der Arbeitsauftragsvorlagen? 

Auftragsvorlagen erlauben häufig verwendete Auftragsdefinitionen aus einem Auftrag zu speichern, um sie für nachfolgende, ähnlich konfigurierte Aufträge zu verwenden.

[Anfang](#top.md)

## Wie viele Basisobjekte unterstützt der Pfad Arbeitsbereich? 

Unterstützung gibt es nur für ein einziges Basisobjekt. Um Pfade für mehrere Festkörper in einem einzigen Auftrag zu erstellen, kkannst du diese zu einem Verbund zusammenfassen und diesen als Basisobjekt für den Auftrag verwenden.

[Anfang](#top.md)

## Warum erzeugt eine Bearbeitung keine brauchbare Ausgabe? 

Es gibt eine Vielzahl von Gründen, die dazu führen können, dass eine einzelne Bearbeitung kein Ergebnis erzeugt.

Ein häufiger Grund ist, dass die Werkzeuggeometrie, die in der für den Arbeitsgang ausgewählten Werkzeugsteuerung definiert ist, zu groß ist, um in die für den Arbeitsgang ausgewählte Geometrie des 3D Modells zu passen.

Beachte, dass dies in der Regel als eine Bewegung im Eiltempo zu dem Ort, an dem die Bearbeitung beginnt, erfolgt, ergänzt durch eine Bewegung im Eiltempo Z zu der Geometrie, die zur Definition der Bearbeitung ausgewählt wurde, und dann eine Rückkehr zur Eiltempo Zwischenhöhe.

Ein weiteres häufiges Missverständnis ist, dass ein Konturbearbeitung keine Pfade ausgibt, wenn die Kontureditorbearbeitung-\>Schnittseite auf \"Innen\" steht, die Standardeinstellung, und das Umschalten der 3D Modellierbarkeit es ermöglicht, sie zu sehen.

[Anfang](#top.md)

## Kann der Pfad Arbeitsbereich 3D Oberflächen Fräsen? 

Ja, Pfad stellt 3D Oberflächenfräsbearbeitungen bereit. Es erfordert die Installation von OpenCamLibrary\--einem quelloffenen Modul eines Drittanbieters, im Makro Dateipfad.

OpenCamLibrary ist nicht in FreeCAD eingebunden, um sicherzustellen, dass keine Lizenzverstöße auftreten.

[Anfang](#top.md)

## Was kann ich tun, wenn die Standardbearbeitungsstrategien nicht meinen Anforderungen entsprechen? 

Bei Taschenbearbeitungen ist der Startpunkt standardmäßig auf XYZ = 000 eingestellt und immer aktiviert, aber auch er kann im Eigenschaftsansichtsfenster konfiguriert werden. Taschen- und Planfräsbearbeitungen bieten auf dem Bearbeitungsreiter eine explizite Angabe des Steig- und des konventionellen Schnittmodus.

Für Konturstil Bearbeitungen verfügt der Bearbeitungsreiter über einen \"Richtung\" Eingang , der als CW (Uhrzeigersinn) oder CCW (Gegenuhrzeigersinn) konfiguriert werden kann und die Schnittrichtung definiert. Als Referenz:

1.  Cut Side = Außen, Schnittrichtung = CCW, Steigungsschnitt
2.  Cut Side = Außen, Schnittrichtung = CW, Konventioneller Schnitt
3.  Cut Side = Innen, Schnittrichtung = CW, konventioneller Schnitt

Cut Side = Innen, Schnittrichtung = CCW, Steigschnitt

Startpunkte können im Eigenschaften Fenster aktiviert und konfiguriert werden.

In Flächenfräsbearbeitungen können Materialzugaben festgelegt werden, die bei positiven Werten eine Überschneidung und bei negativen Werten eine Unterschneidung ermöglichen.

Bei Kontur- und Taschenoperationen dient der Extra Versatz demselben Zweck.

Diese Eingaben sind wertvoll und erlauben unter anderem folgende Funktionalität:

1.  Definition von Schruppdurchgängen, in Verbindung mit den Tiefen Eingabefeldern.
2.  Spezifizierung von Überschnitten für Plandreharbeiten.
3.  Formelemente kleiner als der Werkzeugdurchmesser, die es zu bewältigen gilt, können davon profitieren, dass ein Außenkonturschnitt mit einem negativen Zusatzversatzwert festgelegt wird.

Vorsicht ist geboten wenn Angabe von Materialzugaben und Versätzen angegeben werden, auf die Gefahr hin, dass unerwünschte Einschnitte in den Schaft vorgenommen werden.

[Anfang](#top.md)

## Was mache ich, wenn ein Arbeitsgang mehr vertikale Bewegungen erzeugt, als mein Arbeitauftrag vertragen kann? 

Bearbeitungen wie [3D Tasche](Path_Pocket_3D/de.md), [Taschen Form](Path_Pocket_Shape/de.md), und [FlächenFräsen](Path_MillFace/de.md), aber nicht Konturbearbeitungen, haben eine Konfigurationsoption, um das Werkzeug unten zu halten, auf dem Datenreiter in der Eigenschaftsansicht.

[Anfang](#top.md)

## Wie kann ich Laschen zum Spannen meiner Fräsarbeiten belassen? 

Pfad Arbeitsbereich bietet eine [Aufbereitungskennzeichnung](Path_DressupTag/de.md) für genau diesen Zweck.

[Anfang](#top.md)

## Was ist ein Postprozessor? 

Der [Postprozessor](Path_Post/de.md) wird verwendet, um den Ausgabecode für CNC Steuerungen für verschiedene Maschinen in ihrem G-Code Dialekt anzupassen.

[Anfang](#top.md)

## Kann ich einen bestehenden Postprozessor ändern oder einen eigenen Postprozessor erstellen? 

Postprozessoren sind Python Skripte, die im Makro Dateipfad gespeichert werden. Sie sind dazu gedacht, geändert zu werden oder als Vorlage für die weitere Entwicklung von Postprozessoren zu dienen.

[Anfang](#top.md)

## Ich möchte nur einen Postprozessor verwenden\--kann ich ihn als Standard festlegen oder andere Optionen ausblenden? 

Ja, in den [Pfadeinstellungen](Path_Preferences/de.md) gibt es einen Abschnitt für Postprozessoren, in dem du auswählen kannst, welche Postprozessoren angezeigt werden sollen, und einen Standardpostprozessor auswählen kannst.

[Anfang](#top.md)

## Wie kann ich metrische/zöllige Einheiten für mein Pfadobjekt festlegen? 

Die 3D Modell Einheiten werden im Bearbeiten-\>Einstellungen\...\>Allgemein-\>Einheiten Reiter des Aufklappmenü des Nutzersystems definiert.

Die Einheiten Einstellung, die festlegt, wie die Zielfräse den Auftrags G-Code interpretiert, wird im Ausgabe Postprozessor festgelegt, der einen G20 oder einen G21 G-Code Befehl einfügt, um Zoll bzw. Millimeter anzugeben.

Der Postprozessor kann auch für Einheiten/Sekunde oder Einheiten/Minute konfiguriert werden. Bei der Einstellung Einheiten/Minute wird die interne G-Code Dialekt Vorschubrate der Pfad Arbeitsbereich mit 60 multipliziert.

Unstimmigkeiten zwischen dem 3D Modell und den Postprozessor Einstellungen sind wahrscheinlich die Ursache für Fehler mit einem Faktor von 60 bei der Vorschubgeschwindigkeit und einem Faktor von 25,4 bei der Entfernung.

[Anfang](#top.md)

## Wie kann ich meine Frässtrategien simulieren? 

Ein volumetrischer Simulator wird bereitgestellt, um das Ergebnis des Schneidens der in den Auftragsbearbeitungen enthaltenen Werkzeuggeometrien gegen das Rohmaterial zu betrachten.

Wenn die Pfadlinien das Simulationsergebnis verdecken, sollte ihre Sichtbarkeit vor der Simulation ausgeschaltet werden.

[Anfang](#top.md)

## Welche Bedeutung haben die Farben der Pfadlinien? 

Die Farben der Pfadlinien werden in der Bearbeiten -\> Einstellungen -\> Pfad-\>GUI-\>Standard Pfadfarben festgelegt. Die Standardfarben schließen ein:

1.  Grün für normale Pfade.
2.  Rot für schnelle Pfade.
3.  Gelb für Sondierungspfade.

[Anfang](#top.md)

## Wie kann ich die Sichtbarkeit von Pfadlinien aktivieren/deaktivieren? 

Der Pfad Arbeitsbereich ermöglicht die Kontrolle über die Anzeige von Pfadlinien, indem die Sichtbarkeit des Auftrags durch Auswahl in der [Comboansicht](Combo_view/de.md) umgeschaltet wird. Die Sichtbarkeit einzelner Vorgänge oder Gruppen von Vorgängen wird dann in der Comboansicht umgeschaltet.

[Anfang](#top.md)

## Wie prüfe ich, ob meine G-Code Sequenz korrekt ist? 

Standardmäßig wird die Postprozessorausgabe vor dem Speichern in einem Fenster angezeigt. Dies\--Zusammen mit dem Pfad CAM Simulator bietet eine Möglichkeit, den Auftrag zu prüfen, bevor er auf einer CNC Maschine verarbeitet wird. Das G-Code Inspektionswerkzeug erlaubt dir den internen Pfad G-Code für jede Bearbeitung prüfen, um festzustellen, ob die Ausgabe des Postprozessors dem entspricht, was in der Bearbeitung definiert ist.

Die Bearbeitungsliste in der Comboansicht zeigt die Reihenfolge an, in der die Bearbeitungen im Auftrag verarbeitet werden. Wenn die Bearbeitungen zwar korrekt sind, aber nicht in der gewünschten Reihenfolge, kann dies durch Doppelklicken auf die Bearbeitungsliste und Ziehen der Bearbeitungen an die richtige Stelle korrigiert werden, oder durch Doppelklicken auf den Auftragseditor und Auswählen des Arbeitsablauf Reiters und anschließendes Sortieren der ausgewählten Bearbeitungen mit den Pfeilen nach oben/unten.

[Anfang](#top.md)

## Warum erhalte ich von meinem Postprozessor keine korrekte G-Code Ausgabe für Operationen, die mit dem Teilweise Befehl-\>Benutzerdefiniert Befehl eingefügt wurden? 

Da das Format des benutzerdefinierten G-Code Befehls immer in Einheiten/Sekunde angegeben wird, kann er bei CNC Maschinen, die in Einheiten/Minute arbeiten, Fehler mit dem Faktor 60 verursachen.

[Anfang](#top.md)

## Warum scheinen Änderungen an Positionierungswerten in der Eigenschaftsansicht im Pfad Arbeitsbereich nicht korrekt zu funktionieren? 

\"Die Pfad Funktion besitzt auch eine Eigenschaft Positionierung. Ändern des Wertes dieser Positionierung , ändert die Position der Funktion in der 3D Ansicht, obwohl die Pfadinformationen selbst nicht verändert werden. Die Transformation ist rein visuell. Auf diese Weise kannst du zum Beispiel einen Pfad um eine Fläche herum erstellen, die eine bestimmte Ausrichtung auf deinem Modell hat, die nicht die gleiche Ausrichtung ist, die dein Schneidmaterial auf der CNC Maschine haben wird.

Pfadverbünde können jedoch die Positionierung ihrer Kinder nutzen (siehe unten).\"

[Pfad Skripten](Path_scripting/de.md)

[Anfang](#top.md)

## Warum scheint die Pfad Arbeitsbereich auf meinem Computer Funktionalität zu vermissen, die ich in den Forenbeiträgen anderer Benutzer sehe? 

Standardmäßig ist Experimentelle Funktionalität im Pfad Arbeitsbereich ausgeblendet.

[Anfang](#top.md)

## Warum erscheinen Youtube Videos, die von Pfad Arbeitsbereich Entwicklern veröffentlicht werden, nicht synchron mit dem Pfad Arbeitsbereich? 

Der Pfad Arbeitsbereich hat sich von FreeCAD v0.16 auf v0.17 drastisch verändert, und alle Videos, die vor dem 1. Januar 2018 veröffentlicht wurden, enthalten höchstwahrscheinlich Informationen, die nicht mehr mit der Version 0.17 des Pfad Arbeitsbereichs übereinstimmen.

[Anfang](#top.md)

## Warum sind Bögen nicht rund, sondern bestehen aus einer Reihe von geraden Linien? 

Dabei geht es nur um die Anzeige des Pfades. Du kannst dies in den Einstellungen ändern: Lade Pfad Arbeitsbereich.

1.  Öffne Einstellungen -\>Pfad-\>Auftragseinstellungen
2.  Setze die Werte für *Standard Geometrietoleranz* und *Standard Kurvengenauigkeit* auf kleine Werte, aber nicht auf 0, z.B. auf 0.01mm.
3.  Bestätige die Änderung.
4.  Starte FreeCAD neu.

[Anfang](#top.md)





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path FAQ/de
