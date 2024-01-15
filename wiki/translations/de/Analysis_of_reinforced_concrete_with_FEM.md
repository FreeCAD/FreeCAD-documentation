---
 TutorialInfo:e
   Topic:  Stahlbeton mit FEM
   Level:  Geübte
   Time :  60 Minuten
   Author: User: HarryvL   HarryvL,https://forum.freecadweb.org/memberlist.php?mode: viewprofile&u=18062 HarryvL
   FCVersion: 0.19.xxxxx oder neuer
   Files: 
---

# Analysis of reinforced concrete with FEM/de







## Hintergrund


<div class="mw-translate-fuzzy">

Der FEM Arbeitsbereich ist in der Lage, das Ausmaß der Bewehrung abzuschätzen, die in einer Betonstruktur erforderlich ist, um sprödes Versagen unter Zug oder Scherung zu verhindern.


</div>

<img alt="" src=images/Femconcrete_Wall_3D_rx_PSS.png  style="width:700px;">


<div class="mw-translate-fuzzy">

Dies geschieht mit der in [\"Berechnung der Bewehrung für Vollbeton\", P.C.J. Hoogenboom und A. de Boer, HERON Vol. 53 (2008) Nr. 4](http://heronjournal.nl/53-4/3.pdf) beschriebenen Methode. Im Wesentlichen handelt es sich dabei um eine Nachbearbeitungsroutine für Calculix, die die wichtigsten Zugspannungen im Beton aus einer elastischen Analyse berechnet und diese verwendet, um die Mindestbewehrung in den drei Koordinatenrichtungen zu bestimmen, die erforderlich ist, um ein Versagen zu verhindern. Bei der Analyse wird davon ausgegangen, dass das Betonmaterial keine Zugspannungen tragen kann, während der Stahl bis zu seiner maximalen Kapazität ausgenutzt wird (d.h. die Streckgrenze erreicht).


</div>


<div class="mw-translate-fuzzy">

Die erforderliche Bewehrung wird in Form eines Bewehrungsverhältnisses ausgedrückt. Dies ist das Verhältnis von Stahl zur Betonfläche. Zum Beispiel bedeutet ein Bewehrungsverhältnis von 0,01 in x Richtung (rx=0,01), dass die Gesamtquerschnittsfläche von Bewehrungsstäben, die in x Richtung verlaufen, 1% der Betonquerschnittsfläche betragen sollte, die sie durchqueren. Ein hypothetischer Querschnitt von 1mx1m sollte in diesem Fall 0,01 m2 Stahl enthalten, was durch die Verwendung von 90 Bewehrungsstäben mit jeweils 12 mm Durchmesser erreicht werden könnte (Stahlfläche = 90\*PI\*(0,012)\^2/4=0,0102 m\^2). Wenn der erforderliche Bewehrungsgrad über diesen Betonquerschnitt einheitlich ist, könnten die Stäbe in einem äquidistanten 9x10 Raster mit einem Achsabstand von etwa 10 cm angeordnet werden. Dies ist immer noch eine praktische Zahl, bei der genügend Platz zwischen den Stäben bleibt, damit der Beton durchlaufen und eine qualitativ hochwertige Abdeckung gewährleistet werden kann. Viel höhere Werte würden zu einem sehr dichten Bewehrungsgitter mit potenziellen Qualitätsproblemen führen, während viel niedrigere Werte zu großen Spannungsrissen im Querschnitt zwischen den Stäben führen könnten. Ein typischer Bereich in der Praxis liegt zwischen 0,002 und 0,02 (= 0,2% bis 2%). Weitere Hinweise sind in den Bemessungsnormen zu finden.


</div>


<div class="mw-translate-fuzzy">

Wenn das erforderliche Bewehrungsverhältnis über den gesamten Querschnitt nicht einheitlich ist, kann der Querschnitt in pragmatische Unterabschnitte mit mehr oder weniger einheitlichem Verhältnis und der auf diese Querschnitte aufgebrachten Bewehrung unterteilt werden. Ein Beispiel wird später angegeben.


</div>


<div class="mw-translate-fuzzy">

Als ein Wort der Vorsicht sei gesagt, dass es für den Entwurf einer sicheren und dauerhaften Betonstruktur viel mehr braucht, als das, was die FEM Arbeitsbereich derzeit leisten kann. Die Methode berechnet beispielsweise keine Rissbreite (wichtig für Dauerhaftigkeit und Funktionalität), keine genauen Verformungen (FEM Ergebnisse für Beton sind einfach linear-elastisch) und berücksichtigt auch nicht die Anforderungen an die Bewehrungsverankerung (was zu einer Erhöhung der erforderlichen Bewehrungsverhältnisse in den Verankerungszonen führt). Es werden auch keine Betonquetschungen vorhergesagt (obwohl ein Hinweis darauf durch Auftragen der Mohr Coulomb Spannung erhalten werden kann - siehe weiter unten), was bedeuten könnte, dass der Beton versagt, bevor die Bewehrung nachgibt, was zu sprödem Versagen der Gesamtstruktur führt. Diese und andere Einschränkungen bedeuten, dass die FEM Betonfunktionalität nur zur Beurteilung von Konzeptentwürfen verwendet werden kann, während detaillierte Entwurfsentscheidungen, die für die Sicherheit und Leistung entscheidend sind, qualifizierten Fachleuten überlassen werden sollten.


</div>

## Model geometry, loads and supports 


<div class="mw-translate-fuzzy">

## Modellgeometrie, Lasten und Stützen 

Obwohl die FEM Betonroutine keine zusätzlichen Anforderungen an Geometrie, Lasten und Stützen stellt, ist zu bedenken, dass scharfe Ecken und eine Stütze an einer Kante oder einem Knoten Spannungskonzentrationen erzeugen können, die an oder in der Nähe dieser Stellen zu extrem hohen und unrealistischen Bewehrungsverhältnissen führen.


</div>

## Material Parameters 


<div class="mw-translate-fuzzy">

## Werkstoff Parameter 

Der FEM Arbeitsbereich hat ein spezielles Materialobjekt für verstärkte Materialien, das ein Matrixmaterial (z.B. Beton) und ein Verstärkungsmaterial (z.B. Stahl) kombiniert. Für die Analyse von Stahlbeton mit der FEM müssen mindestens die folgenden Parameter angegeben werden:


</div>

für Beton:


<div class="mw-translate-fuzzy">

\- Elastizitätsmodul (wird in der Calculix Analyse zur Berechnung elastischer Verformungen und Spannungen verwendet)

   - Poissonzahl (gleich)
   - uniaxiale Druckfestigkeit (wird bei der Nachbearbeitung in der FEM zur Berechnung der Mohr Coulomb Spannung als Indikator für Quetsch- oder Scherversagen im Beton verwendet)
   - Reibungswinkel (gleich)


</div>

für Stahl:


<div class="mw-translate-fuzzy">

\- Streckgrenze (wird bei der Nachbearbeitung in der FEM zur Berechnung von Bewehrungsverhältnissen verwendet)


</div>


<div class="mw-translate-fuzzy">

Bitte beachte, dass drei Arten von Analysen durchgeführt werden: 1) Eine elastische Analyse mit Calculix (nur unter Verwendung der elastischen Parameter von Beton); 2) Ein Nachbearbeitungsschritt zur Analyse der erforderlichen Bewehrung (nur unter Verwendung der Streckgrenze von Stahl) und 3) Berechnung der Mohr Coulomb Spannung (nur unter Verwendung der Festigkeitsparameter von Beton, d.h. einachsige Druckfestigkeit und Reibungswinkel). Die Mohr Coulomb Spannung kann in der VTK Pipeline überprüft werden.


</div>

## Application


<div class="mw-translate-fuzzy">

## Anwendung

Im weiteren Verlauf dieses Artikels werden einige praktische Fälle analysiert, um die Anwendung der Methode zu diskutieren.


</div>

### Simply supported beam with uniform load 


<div class="mw-translate-fuzzy">

### Einfach gelagerter Träger mit gleichmäßiger Belastung 

Ein 4,0x0,1x0,3 m langer Betonbalken wird durch Eigengewicht und eine verteilte Last von 100 kN (25 kN/m) belastet.


</div>

Die Materialparameter sind wie folgt:

für Beton:


<div class="mw-translate-fuzzy">

\- Elastizitätsmodul = 32 GPa (gemäß der Calculix Vorgabe für Beton)

   - Poissonzahl = 0,17 (gemäß der Calculix Vorgabe für Beton)
   - uniaxiale Druckfestigkeit = 30 MPa (Betontyp C30/37)
   - Reibungswinkel = 30 Grad


</div>

für Stahl:


<div class="mw-translate-fuzzy">

\- Streckgrenze = 500 MPa


</div>

Das spezifische Gewicht des Betons wird angenommen mit 24kN/m\^3


<div class="mw-translate-fuzzy">

Die erforderliche Bewehrung in x Richtung ist sehr hoch (5,4 %) und überschreitet typische, nach den Normen zulässige Höchstprozentsätze, um sprödes Versagen zu verhindern. Die hohen Schubspannungen an den Stützen führen ebenfalls zu der Forderung nach einer hohen Bewehrung:


</div>

<img alt="" src=images/Pre_Stressed_Beam_2_Weight_Load_RR_x_0.054.jpg  style="width:700px;">


<div class="mw-translate-fuzzy">

Das Mohr Coulomb Diagramm zeigt, dass der Balken tatsächlich anfällig für Quetschungen auf der Druckseite ist (Mohr Coulomb Spannung \> 0,0), wie bei einem sehr hohen Bewehrungsprozentsatz zu erwarten wäre:


</div>

<img alt="" src=images/Pre_Stressed_Beam_2_Weight_Load_MC.jpg  style="width:700px;">


<div class="mw-translate-fuzzy">

Sowohl das Verstärkungsverhältnis als auch die Mohr Coulomb Spannung deuten darauf hin, dass wir ein Problem haben und dass wir unseren konzeptionellen Entwurf überdenken müssen. Mögliche Lösungen sind die Vergrößerung der Balkenabmessungen oder die Verwendung von Spannbeton. Weitere Einzelheiten findest du im folgenden Beitrag:


</div>

<https://forum.freecadweb.org/viewtopic.php?f=18&t=28821&start=10#p235003>

### Beam with mid-span support 


<div class="mw-translate-fuzzy">

### Träger mit Halbspannweitenstützen 

Ein 8,0x0,2x0,4 m langer Betonbalken wird durch Eigengewicht und eine verteilte Last von 160 kN (20 kN/m) belastet.


</div>

Die Materialparameter sind wie folgt:

für Beton:


<div class="mw-translate-fuzzy">

\- Elastizitätsmodul = 32 GPa (gemäß der Calculix Vorgabe für Beton)

   - Poissonzahl = 0,17 (gemäß der Calculix Vorgabe für Beton)
   - uniaxiale Druckfestigkeit = 25 MPa (Betontyp B25)
   - Reibungswinkel = 30 Grad


</div>

für Stahl:


<div class="mw-translate-fuzzy">

\- Streckgrenze = 286 MPa (reduziert von 500 MPa, um einen Sicherheitsfaktor von 1,75 zu berücksichtigen)


</div>

Das spezifische Gewicht des Betons wird angenommen mit 24kN/m\^3


<div class="mw-translate-fuzzy">

Das ParaView Diagramm der exportierten VTK Datei zeigt, dass der Bewehrungsbedarf am oberen Ende des Trägers in der Nähe der Mittelstütze am größten ist. Hier tritt das höchste Biegemoment auf. Der maximale Bewehrungsgrad liegt mit 0,02 am oberen Ende des zuvor genannten praktischen Bereichs:


</div>

<img alt="" src=images/Beam_with_Central_Support_rx_full.png  style="width:700px;">


<div class="mw-translate-fuzzy">

Die erforderliche Stahlfläche an der zentralen Stütze kann mit einem ParaView Integrationsfilter erreicht werden, der auf den mittleren Abschnitt des Trägers angewendet wird:


</div>

<img alt="" src=images/CoG_Reinforcement.png  style="width:700px;">


<div class="mw-translate-fuzzy">

Die Platte unten in diesem Bild zeigt, dass die gesamte erforderliche Stahlfläche bei diesem Querschnitt 389,6 mm\^2 beträgt. Da ein Bewehrungsstab mit einem Durchmesser von 12 mm eine Querschnittsfläche von 113 mm\^2 hat, bedeutet dies, dass 4 Stäbe erforderlich wären, was eine Querschnittsfläche von 452 mm\^2 ergibt. Diese müssten in der Nähe der Oberkante des Balkens platziert werden, wobei eine ausreichende Betondeckung erhalten bleiben müsste. Der theoretische Schwerpunkt für die Bewehrung kann durch Integration ermittelt werden:


</div>


<div class="mw-translate-fuzzy">

CoG_y = Integrate (rx \* y dy dz) / Integrate (rx dy dz)

   CoG_z = Integrate (rx * z dy dz) / Integrate (rx dy dz)


</div>

CoG_z = Integrate (rx \* z dy dz) / Integrate (rx dy dz)

Diese Integrale können auch mit ParaView bestimmt und für den vorliegenden Fall angegeben werden (siehe untere Platten in der obigen Abbildung):


<div class="mw-translate-fuzzy">

CoG_y = 38961 / 389.6 = 100.0 mm

   CoG_z = 134917 / 389.6 = 346.3 mm


</div>

CoG_z = 134917 / 389.6 = 346.3 mm

die erwartungsgemäß in der Mitte und nahe der Spitze liegt.

Die oben gefundene Verstärkungsanforderung stimmt gut mit derjenigen überein, die mit herkömmlichen Methoden erreicht wird:

<https://forum.freecadweb.org/viewtopic.php?f=18&t=28821&start=20#p235063>


<div class="mw-translate-fuzzy">

Schließlich sollte ein Mohr Coulomb Spannungsnachweis durchgeführt werden, um eine potenzielle Quetschung des Betons zu überprüfen. Für diesen Nachweis sollte die charakteristische Druckfestigkeit des Betons (25MPa) durch einen geeigneten Materialfaktor (\>1,0) geteilt werden.


</div>

### Shear wall with uniform load 


<div class="mw-translate-fuzzy">

### Scherwand mit gleichmäßiger Belastung 

Eine 4,0x2,0x0,15 m hohe Wand wird von zwei 0,5 m breiten Säulen getragen. Die Wand wird durch Eigengewicht und eine verteilte Last von 1,0 MN an der Oberseite belastet.


</div>

Die Materialparameter sind wie folgt:

für Beton:


<div class="mw-translate-fuzzy">

\- Elastizitätsmodul = 32 GPa (gemäß der Calculix Vorgabe für Beton)

   - Poissonzahl = 0,17 (gemäß der Calculix Vorgabe für Beton)
   - uniaxiale Druckfestigkeit = 20 MPa
   - Reibungswinkel = 30 Grad


</div>

für Stahl:


<div class="mw-translate-fuzzy">

\- Streckgrenze = 286 MPa


</div>

Das spezifische Gewicht des Betons wird angenommen mit 24kN/m\^3

Der horizontale Bewehrungsgrad erreicht seinen Höchstwert bei 0,014 (1,4%) in der Nähe des unteren Mittelteils der Wand und der vertikale Bewehrungsgrad liegt bei maximal 0,008 (0,8%) in der Nähe der Ecken der Wand mit den Stützen, wo die Schubspannungen am höchsten sind:

<img alt="" src=images/Wall_3D.jpg  style="width:1000px;">


<div class="mw-translate-fuzzy">

Das obige Bild zeigt mögliche Zonen mit konstantem Bewehrungsverhältnis für den Bewehrungsentwurf. Obwohl ein Mindestbewehrungsgrad von 0,2% gewählt wird, wird es in der Praxis schwierig sein, einen so niedrigen Wert zu erreichen, da der Abstand eine praktische Grenze (sagen wir 300mm) nicht überschreiten sollte. Selbst bei einem leichten Bewehrungsgitter aus 10mm Stäben (Querschnittsfläche = 78mm\^2) würde der Bewehrungsgrad dann 2 \* 78 / (150 \* 300) = 0,0035 (0,35%) betragen. (Anmerkung: Der Faktor 2 ergibt sich aus der Tatsache, dass das Gitter auf beiden Seiten der Wand angebracht wird). Wenn wir einen weiteren Stab zum Gitter hinzufügen (und damit den Abstand halbieren), würde sich das Bewehrungsverhältnis auf 0,7% verdoppeln, und ein weiterer Stab würde ungefähr 1% ergeben. Der größte Teil der erforderlichen Bewehrung könnte also erreicht werden, indem man mit einem Gitter von d=10mm im Abstand von 300x300mm beginnt und je nach Bedarf Stäbe in horizontaler oder vertikaler Richtung hinzufügt. Dies würde alle Anforderungen bis auf die Anforderung an der Unterseite der Wand abdecken, wo wir 3 Stäbe d=12mm hinzufügen könnten, was ein horizontales Bewehrungsverhältnis von 3 \* 113mm\^2 / (150mm \* 150mm) = 0,015 (1,5%) ergeben würde. Hier wird angenommen, dass die Höhe der unteren Zone 150 mm beträgt. Alternativ könnten wir 2 Stäbe mit einem Durchmesser von 16 mm wählen, die das gleiche Verstärkungsverhältnis für eine Zone von 180 mm Höhe erreichen würden.


</div>


<div class="mw-translate-fuzzy">

Schließlich zeigt eine Überprüfung der Mohr Coulomb Spannung, dass keine Betonzertrümmerung in der Wand zu erwarten ist.


</div>

<https://forum.freecadweb.org/viewtopic.php?f=18&t=28821&start=10#p234673>

### Deep beam with opening 


<div class="mw-translate-fuzzy">

### Tiefer Träger mit Öffnung 

Der FIB Praktiker Leitfaden für Finite Element Modellierung von Stahlbetonstrukturen enthält ein Konstruktionsbeispiel eines tiefen Betonbalkens mit Öffnung. Das Beispiel wird in diesem Bericht verwendet, um die \"Druckstab-und-Zugstab\" Methode zu demonstrieren. Hier werden die Ergebnisse mit denen verglichen, die mit der FreeCAD FEM Arbeitsbereich erzielt wurden.


</div>

Die Trägerabmessungen sind 11,0x4,0x0,6 m, und er wird oben mit einer verteilten Last von 120 kN/m und einer Last von 5000 kN belastet, die von einer 1 m breiten Säule eingeleitet wird. Die rechnerische Druckfestigkeit des Betons beträgt 0,75 x 0,6 x fc = 0,45 \* 35 = 15,8 MPa und die rechnerische Streckgrenze des Bewehrungsstahls 315 MPa.

Die mit FreeCAD abgeleiteten Bewehrungsverhältnisse und Hauptbetonspannungen (nur Druck) sind unten dargestellt:

<img alt="" src=images/FIB_Deep_Concrete_Beam_1.png  style="width:1000px;">

Die erforderliche horizontale Bewehrung (unten in rot) wird durch Integration des horizontalen Bewehrungsverhältnisses über die interessierenden vertikalen Schnitte (unten in schwarz) ermittelt. Dies geschieht mit Hilfe eines Paraview Integrationsfilters.

<img alt="" src=images/FIB_Reinforcement(2).jpg  style="width:700px;">

Die Einfügung in die obige Abbildung zeigt einen Vergleich der mit FreeCAD ermittelten Bewehrungsanforderungen (in mm\^2 Stahl) mit denen im FIB Bericht.

Im Folgenden wird gezeigt, wie die Integration über die Interessenslinien in Paraview funktioniert:

<img alt="" src=images/FIB_Reinforcement_ry.jpg  style="width:700px;">


<div class="mw-translate-fuzzy">

Schließlich ein Diagramm der Druck- und Zugspannungen, um zu zeigen, wie die Spannungen durch den Träger fließen.


</div>

<img alt="" src=images/FIB_Beam_Stresses_and_Cables.jpg  style="width:700px;">

Das Zugspannungsmuster legt ein alternatives Konstruktionskonzept unter Verwendung von Vorspannkabeln (weiß überlagert) nahe. Dieses Konzept wird im folgenden Beitrag weiter ausgearbeitet: <https://forum.freecadweb.org/viewtopic.php?f=18&t=33049>



## Verwandt


<div class="mw-translate-fuzzy">

-   [FEM Beton](FEM_Concrete/de.md)


</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > Analysis of reinforced concrete with FEM/de
