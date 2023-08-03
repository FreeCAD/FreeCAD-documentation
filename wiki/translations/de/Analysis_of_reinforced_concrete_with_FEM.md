# Analysis of reinforced concrete with FEM/de
---
 TutorialInfo:e
   Topic:  Stahlbeton mit FEM
   Level:  Geübte
   Time :  60 Minuten
   Author: User: HarryvL   HarryvL,https://forum.freecadweb.org/memberlist.php?mode: viewprofile&u=18062 HarryvL
   FCVersion: 0.19.xxxxx oder neuer
   Files: 
}}



## Hintergrund

Der FEM Arbeitsbereich ist in der Lage, das Ausmaß der Bewehrung abzuschätzen, die in einer Betonstruktur erforderlich ist, um sprödes Versagen unter Zug oder Scherung zu verhindern.

!{width="700"}

Dies geschieht mit der in \"Berechnung der Bewehrung für Vollbeton\", P.C.J. Hoogenboom und A. de Boer, HERON Vol. 53  Nr. 4 beschriebenen Methode. Im Wesentlichen handelt es sich dabei um eine Nachbearbeitungsroutine für Calculix, die die wichtigsten Zugspannungen im Beton aus einer elastischen Analyse berechnet und diese verwendet, um die Mindestbewehrung in den drei Koordinatenrichtungen zu bestimmen, die erforderlich ist, um ein Versagen zu verhindern. Bei der Analyse wird davon ausgegangen, dass das Betonmaterial keine Zugspannungen tragen kann, während der Stahl bis zu seiner maximalen Kapazität ausgenutzt wird .

Die erforderliche Bewehrung wird in Form eines Bewehrungsverhältnisses ausgedrückt. Dies ist das Verhältnis von Stahl zur Betonfläche. Zum Beispiel bedeutet ein Bewehrungsverhältnis von 0,01 in x Richtung , dass die Gesamtquerschnittsfläche von Bewehrungsstäben, die in x Richtung verlaufen, 1% der Betonquerschnittsfläche betragen sollte, die sie durchqueren. Ein hypothetischer Querschnitt von 1mx1m sollte in diesem Fall 0,01 m2 Stahl enthalten, was durch die Verwendung von 90 Bewehrungsstäben mit jeweils 12 mm Durchmesser erreicht werden könnte \^2/4=0,0102 m\^2). Wenn der erforderliche Bewehrungsgrad über diesen Betonquerschnitt einheitlich ist, könnten die Stäbe in einem äquidistanten 9x10 Raster mit einem Achsabstand von etwa 10 cm angeordnet werden. Dies ist immer noch eine praktische Zahl, bei der genügend Platz zwischen den Stäben bleibt, damit der Beton durchlaufen und eine qualitativ hochwertige Abdeckung gewährleistet werden kann. Viel höhere Werte würden zu einem sehr dichten Bewehrungsgitter mit potenziellen Qualitätsproblemen führen, während viel niedrigere Werte zu großen Spannungsrissen im Querschnitt zwischen den Stäben führen könnten. Ein typischer Bereich in der Praxis liegt zwischen 0,002 und 0,02 . Weitere Hinweise sind in den Bemessungsnormen zu finden.

Wenn das erforderliche Bewehrungsverhältnis über den gesamten Querschnitt nicht einheitlich ist, kann der Querschnitt in pragmatische Unterabschnitte mit mehr oder weniger einheitlichem Verhältnis und der auf diese Querschnitte aufgebrachten Bewehrung unterteilt werden. Ein Beispiel wird später angegeben.

Als ein Wort der Vorsicht sei gesagt, dass es für den Entwurf einer sicheren und dauerhaften Betonstruktur viel mehr braucht, als das, was die FEM Arbeitsbereich derzeit leisten kann. Die Methode berechnet beispielsweise keine Rissbreite , keine genauen Verformungen  und berücksichtigt auch nicht die Anforderungen an die Bewehrungsverankerung . Es werden auch keine Betonquetschungen vorhergesagt , was bedeuten könnte, dass der Beton versagt, bevor die Bewehrung nachgibt, was zu sprödem Versagen der Gesamtstruktur führt. Diese und andere Einschränkungen bedeuten, dass die FEM Betonfunktionalität nur zur Beurteilung von Konzeptentwürfen verwendet werden kann, während detaillierte Entwurfsentscheidungen, die für die Sicherheit und Leistung entscheidend sind, qualifizierten Fachleuten überlassen werden sollten.

## Modellgeometrie, Lasten und Stützen 

Obwohl die FEM Betonroutine keine zusätzlichen Anforderungen an Geometrie, Lasten und Stützen stellt, ist zu bedenken, dass scharfe Ecken und eine Stütze an einer Kante oder einem Knoten Spannungskonzentrationen erzeugen können, die an oder in der Nähe dieser Stellen zu extrem hohen und unrealistischen Bewehrungsverhältnissen führen.

## Werkstoff Parameter 

Der FEM Arbeitsbereich hat ein spezielles Materialobjekt für verstärkte Materialien, das ein Matrixmaterial  und ein Verstärkungsmaterial  kombiniert. Für die Analyse von Stahlbeton mit der FEM müssen mindestens die folgenden Parameter angegeben werden:

für Beton:

   - Elastizitätsmodul 
   - Poissonzahl 
   - uniaxiale Druckfestigkeit 
   - Reibungswinkel 

für Stahl:

   - Streckgrenze 

Bitte beachte, dass drei Arten von Analysen durchgeführt werden: 1) Eine elastische Analyse mit Calculix ; 2) Ein Nachbearbeitungsschritt zur Analyse der erforderlichen Bewehrung  und 3) Berechnung der Mohr Coulomb Spannung . Die Mohr Coulomb Spannung kann in der VTK Pipeline überprüft werden.

## Anwendung

Im weiteren Verlauf dieses Artikels werden einige praktische Fälle analysiert, um die Anwendung der Methode zu diskutieren.

### Einfach gelagerter Träger mit gleichmäßiger Belastung 

Ein 4,0x0,1x0,3 m langer Betonbalken wird durch Eigengewicht und eine verteilte Last von 100 kN  belastet.

Die Materialparameter sind wie folgt:

für Beton:

   - Elastizitätsmodul = 32 GPa 
   - Poissonzahl = 0,17 
   - uniaxiale Druckfestigkeit = 30 MPa 
   - Reibungswinkel = 30 Grad

für Stahl:

   - Streckgrenze = 500 MPa

Das spezifische Gewicht des Betons wird angenommen mit 24kN/m\^3

Die erforderliche Bewehrung in x Richtung ist sehr hoch  und überschreitet typische, nach den Normen zulässige Höchstprozentsätze, um sprödes Versagen zu verhindern. Die hohen Schubspannungen an den Stützen führen ebenfalls zu der Forderung nach einer hohen Bewehrung:

!{width="700"}

Das Mohr Coulomb Diagramm zeigt, dass der Balken tatsächlich anfällig für Quetschungen auf der Druckseite ist , wie bei einem sehr hohen Bewehrungsprozentsatz zu erwarten wäre:

!{width="700"}

Sowohl das Verstärkungsverhältnis als auch die Mohr Coulomb Spannung deuten darauf hin, dass wir ein Problem haben und dass wir unseren konzeptionellen Entwurf überdenken müssen. Mögliche Lösungen sind die Vergrößerung der Balkenabmessungen oder die Verwendung von Spannbeton. Weitere Einzelheiten findest du im folgenden Beitrag: <https://forum.freecadweb.org/viewtopic.php?f=18&t=28821&start=10#p235003>

### Träger mit Halbspannweitenstützen 

Ein 8,0x0,2x0,4 m langer Betonbalken wird durch Eigengewicht und eine verteilte Last von 160 kN  belastet.

Die Materialparameter sind wie folgt:

für Beton:

   - Elastizitätsmodul = 32 GPa 
   - Poissonzahl = 0,17 
   - uniaxiale Druckfestigkeit = 25 MPa 
   - Reibungswinkel = 30 Grad

für Stahl:

   - Streckgrenze = 286 MPa 

Das spezifische Gewicht des Betons wird angenommen mit 24kN/m\^3

Das ParaView Diagramm der exportierten VTK Datei zeigt, dass der Bewehrungsbedarf am oberen Ende des Trägers in der Nähe der Mittelstütze am größten ist. Hier tritt das höchste Biegemoment auf. Der maximale Bewehrungsgrad liegt mit 0,02 am oberen Ende des zuvor genannten praktischen Bereichs:

!{width="700"}

Die erforderliche Stahlfläche an der zentralen Stütze kann mit einem ParaView Integrationsfilter erreicht werden, der auf den mittleren Abschnitt des Trägers angewendet wird:

!{width="700"}

Die Platte unten in diesem Bild zeigt, dass die gesamte erforderliche Stahlfläche bei diesem Querschnitt 389,6 mm\^2 beträgt. Da ein Bewehrungsstab mit einem Durchmesser von 12 mm eine Querschnittsfläche von 113 mm\^2 hat, bedeutet dies, dass 4 Stäbe erforderlich wären, was eine Querschnittsfläche von 452 mm\^2 ergibt. Diese müssten in der Nähe der Oberkante des Balkens platziert werden, wobei eine ausreichende Betondeckung erhalten bleiben müsste. Der theoretische Schwerpunkt für die Bewehrung kann durch Integration ermittelt werden:

   CoG_y = Integrate  / Integrate     
   
   CoG_z = Integrate  / Integrate 

Diese Integrale können auch mit ParaView bestimmt und für den vorliegenden Fall angegeben werden :

   CoG_y = 38961 / 389.6 = 100.0 mm
   
   CoG_z = 134917 / 389.6 = 346.3 mm

die erwartungsgemäß in der Mitte und nahe der Spitze liegt.

Die oben gefundene Verstärkungsanforderung stimmt gut mit derjenigen überein, die mit herkömmlichen Methoden erreicht wird:

<https://forum.freecadweb.org/viewtopic.php?f=18&t=28821&start=20#p235063>

Schließlich sollte ein Mohr Coulomb Spannungsnachweis durchgeführt werden, um eine potenzielle Quetschung des Betons zu überprüfen. Für diesen Nachweis sollte die charakteristische Druckfestigkeit des Betons  durch einen geeigneten Materialfaktor  geteilt werden.

### Scherwand mit gleichmäßiger Belastung 

Eine 4,0x2,0x0,15 m hohe Wand wird von zwei 0,5 m breiten Säulen getragen. Die Wand wird durch Eigengewicht und eine verteilte Last von 1,0 MN an der Oberseite belastet.

Die Materialparameter sind wie folgt:

für Beton:

   - Elastizitätsmodul = 32 GPa 
   - Poissonzahl = 0,17 
   - uniaxiale Druckfestigkeit = 20 MPa
   - Reibungswinkel = 30 Grad

für Stahl:

   - Streckgrenze = 286 MPa

Das spezifische Gewicht des Betons wird angenommen mit 24kN/m\^3

Der horizontale Bewehrungsgrad erreicht seinen Höchstwert bei 0,014  in der Nähe des unteren Mittelteils der Wand und der vertikale Bewehrungsgrad liegt bei maximal 0,008  in der Nähe der Ecken der Wand mit den Stützen, wo die Schubspannungen am höchsten sind:

!{width="1000"}

Das obige Bild zeigt mögliche Zonen mit konstantem Bewehrungsverhältnis für den Bewehrungsentwurf. Obwohl ein Mindestbewehrungsgrad von 0,2% gewählt wird, wird es in der Praxis schwierig sein, einen so niedrigen Wert zu erreichen, da der Abstand eine praktische Grenze  nicht überschreiten sollte. Selbst bei einem leichten Bewehrungsgitter aus 10mm Stäben  würde der Bewehrungsgrad dann 2 \* 78 /  = 0,0035  betragen. . Wenn wir einen weiteren Stab zum Gitter hinzufügen , würde sich das Bewehrungsverhältnis auf 0,7% verdoppeln, und ein weiterer Stab würde ungefähr 1% ergeben. Der größte Teil der erforderlichen Bewehrung könnte also erreicht werden, indem man mit einem Gitter von d=10mm im Abstand von 300x300mm beginnt und je nach Bedarf Stäbe in horizontaler oder vertikaler Richtung hinzufügt. Dies würde alle Anforderungen bis auf die Anforderung an der Unterseite der Wand abdecken, wo wir 3 Stäbe d=12mm hinzufügen könnten, was ein horizontales Bewehrungsverhältnis von 3 \* 113mm\^2 /  = 0,015  ergeben würde. Hier wird angenommen, dass die Höhe der unteren Zone 150 mm beträgt. Alternativ könnten wir 2 Stäbe mit einem Durchmesser von 16 mm wählen, die das gleiche Verstärkungsverhältnis für eine Zone von 180 mm Höhe erreichen würden.

Schließlich zeigt eine Überprüfung der Mohr Coulomb Spannung, dass keine Betonzertrümmerung in der Wand zu erwarten ist. <https://forum.freecadweb.org/viewtopic.php?f=18&t=28821&start=10#p234673>

### Tiefer Träger mit Öffnung 

Der FIB Praktiker Leitfaden für Finite Element Modellierung von Stahlbetonstrukturen enthält ein Konstruktionsbeispiel eines tiefen Betonbalkens mit Öffnung. Das Beispiel wird in diesem Bericht verwendet, um die \"Druckstab-und-Zugstab\" Methode zu demonstrieren. Hier werden die Ergebnisse mit denen verglichen, die mit der FreeCAD FEM Arbeitsbereich erzielt wurden.

Die Trägerabmessungen sind 11,0x4,0x0,6 m, und er wird oben mit einer verteilten Last von 120 kN/m und einer Last von 5000 kN belastet, die von einer 1 m breiten Säule eingeleitet wird. Die rechnerische Druckfestigkeit des Betons beträgt 0,75 x 0,6 x fc = 0,45 \* 35 = 15,8 MPa und die rechnerische Streckgrenze des Bewehrungsstahls 315 MPa.

Die mit FreeCAD abgeleiteten Bewehrungsverhältnisse und Hauptbetonspannungen  sind unten dargestellt:

!{width="1000"}

Die erforderliche horizontale Bewehrung  wird durch Integration des horizontalen Bewehrungsverhältnisses über die interessierenden vertikalen Schnitte  ermittelt. Dies geschieht mit Hilfe eines Paraview Integrationsfilters.

!.jpg "FIB_Reinforcement.jpg"){width="700"}

Die Einfügung in die obige Abbildung zeigt einen Vergleich der mit FreeCAD ermittelten Bewehrungsanforderungen  mit denen im FIB Bericht.

Im Folgenden wird gezeigt, wie die Integration über die Interessenslinien in Paraview funktioniert:

!{width="700"}

Schließlich ein Diagramm der Druck- und Zugspannungen, um zu zeigen, wie die Spannungen durch den Träger fließen.

!{width="700"}

Das Zugspannungsmuster legt ein alternatives Konstruktionskonzept unter Verwendung von Vorspannkabeln  nahe. Dieses Konzept wird im folgenden Beitrag weiter ausgearbeitet: <https://forum.freecadweb.org/viewtopic.php?f=18&t=33049>



## Verwandt

-   FEM Beton


{{FEM Tools navi

}} {{Userdocnavi
---



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > Analysis of reinforced concrete with FEM/de
