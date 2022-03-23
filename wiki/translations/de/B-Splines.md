# B-Splines/de
{{TOCright}}

Diese Seite beschreibt, wie man B-Splines in FreeCAD verwendet. Sie gibt auch Hintergrundinformationen, was B-Splines sind und für welche Anwendungen sie nützlich sind.

## Motivation

Wenn du bereits über B-Splines und deren Anwendung Bescheid weisst, kannst du direkt mit dem Abschnitt [B-Splines in FreeCAD](#B-splines_in_FreeCAD/de.md) fortfahren.

Nehmen wir an, Du willst ein Teil entwerfen, das mit einem 3D Drucker hergestellt werden soll. Das Teil muss so eine Kante haben:

<img alt="" src=images/B-splines_Motivation-start.png  style="width:450px;">

Du musst das Teil in Richtung der Unterseite der Skizze nach oben drucken. Äußere Stützstrukturen sind möglicherweise keine Option. Daher musst Du eine Stütze direkt an deinem Teil anbringen. Welche Möglichkeiten hast du?

-   Option 1: du kannst eine Linie vom Punkt (20, 0) zum Punkt (80, 40) hinzufügen:

<img alt="" src=images/B-splines_Motivation-line.png  style="width:450px;">

Allerdings benötigt diese Lösung viel Volumen, also Gewicht und Material.

-   Option 2: du kannst die beiden Punkte mit einem Kreisbogen verbinden. Um Volumen zu sparen, sollte der Bogen tangential im Punkt (80,40) enden. Dann sieht deine Lösung wie folgt aus:

<img alt="" src=images/B-splines_Motivation-circle.png  style="width:450px;">

GUT. Aber ganz unten brauchst du keine sofortige Unterstützung.

-   Option 3: du kannst noch mehr Volumen einsparen, wenn die Verbindung zwischen den beiden Punkten eine Kurve wäre, die tangential bei (0, 20) beginnt und tangential bei (80, 40) endet:

<img alt="" src=images/B-splines_Motivation-bezier.png  style="width:450px;">

So kann eine Kurve, mit der du zwei Punkte tangential zu einem Bezugspunkt verbinden kannst, sehr nützlich für Konstruktionen sein. Bézierkurven bieten diese Möglichkeit.

## Bézierkurven

### Herleitung

Bézierkurven sind Polynome zur Beschreibung der Verbindung zwischen 2 Punkten. Das einfachste Polynom, das 2 Punkte verbindet, ist eine Gerade ($A*x^1+B$), daher sind auch lineare Bézierkurven linear:

![](images/Bezier_linear_anim.gif ) 
*Animation 1: Lineare Bézierkurve.*

Ein Polynom wird jedoch erst dann nützlich, wenn wir es kontrollieren können. Es sollte also einen Punkt zwischen den beiden Endpunkten geben, der es uns erlaubt zu definieren, wie die Endpunkte verbunden sind. Wie im obigen Beispiel, Option 3, ist die Kurve hilfreich, wenn sie tangential zu Linien beginnt und endet, die die Endpunkte kreuzen. Und das ist ein Hauptmerkmal von Bézierkurven. Fügen wir also einen Kontrollpunkt zwischen den 2 Endpunkten ein. Die Kurve beginnt tangential zu diesem Kontrollpunkt, d. h. sie verläuft tangential zu der Linie, die wir zwischen dem Startpunkt und dem Kontrollpunkt ziehen können. Wenn man vom Endpunkt aus rückwärts geht, verläuft die Kurve ebenfalls tangential zu der Linie, die wir zwischen dem Kontrollpunkt und dem Endpunkt zeichnen können. Animation 2 zeigt, wie eine solche Kurve aussieht.

![](images/Bezier_quadratic_anim.gif ) 
*Animation 2: Quadratische Bézierkurve. P1 ist hierbei der Kontrollpunkt.*

Die Animation verdeutlicht, worum es sich bei der Kurve im Grunde handelt - um einen Übergang von P0 zu P2, indem die Linie P0-P1 in die Linie P1-P2 gedreht wird. Dadurch erhalten wir das schöne tangentiale Anfang/Ende Merkmal.

Eine solche Kurve kann nur durch ein quadratisches Polynom beschrieben werden. (Die Anzahl der Links-/Rechtsdrehungen + 1 ist die erforderliche Polynomordnung. Ein quadratisches Polynom hat eine einzige Windung, ein kubisches Polynom hat zwei Windungen usw.) Daher ist eine Bézierkurve mit einem Kontrollpunkt eine quadratische Bézierkurve (zweiter Ordnung).

Ein einziger Kontrollpunkt ist oft nicht ausreichend. Nimm das obige Motivationsbeispiel. Bei der Option 3 endet die Kurve tangential in x-Richtung. Aber wie kann man die Punkte (20, 0) und (80, 40) so verbinden, dass die Kurve tangential in y-Richtung endet? Dazu braucht man erst eine Rechts- und dann eine Linkskurve, also ein kubisches Polynom (dritter Ordnung). Und das bedeutet für eine Bézierkurve, dass wir einen zweiten Kontrollpunkt brauchen (oder man kann sagen, wir gewinnen). Animation 3 zeigt eine kubische Bézierkurve.

![](images/Bezier_cubic_anim.gif ) 
*Animation 3: Kubische Bézierkurve.*

Um die Frage zu beantworten: Die Lösung mit dem tangentialen Ende in y-Richtung für das Beispiel ist diese:

<img alt="" src=images/B-splines_Motivation-cubic-bezier.png  style="width:450px;">

### Mathe

Wenn du an den mathematischen Hintergründen interessiert bist, hier sind die Grundlagen.

Eine Bézierkurve wird mit dieser Formel berechnet:

$\quad
\textrm{Bezier}(n,t)=\sum_{i=0}^{n}\underbrace{\binom{n}{i}}_{\text{Polynomausdruck}}\underbrace{\left(1-t\right)^{n-i}t^{i}}_{\text{Polynomausdruck}}\; \underbrace{P_{i}}_{\text{Punktkoordinate}}$

Dabei ist *n* der Grad der Kurve. Eine Bézierkurve vom Grad *n* ist also ein Polygon der Ordnung *n*. Die Faktoren $P_{i}$ sind dabei die Koordinaten der Kontrollpunkte der Bézierkurven. Zur Veranschaulichung siehe [Steuerung von Bézierkurven](https://pomax.github.io/bezierinfo/#control).

Wenn du weiter interessiert bist, sieh dir [Die Mathematik der Bézierkurven](https://pomax.github.io/bezierinfo/#explanation) mit einer schön animierten Herleitung der Mathematik der Bézierkurven an.

### Regeln

Im obigen Text sind dir vielleicht schon einige \"Regeln\" für Bézierkurven aufgefallen:

-   Der Polynomgrad ist auch der Grad der Kurven.
-   Wenn du $n$ Krümmungen benötigst, benötigst du mindestens eine Bézierkurve vom Grad $n+1$.
-   Eine Bézierkurve beginnt immer tangential zu der Linie zwischen dem Startpunkt und dem ersten Kontrollpunkt (und endet tangential zu der Linie zwischen dem letzten Kontrollpunkt und dem Endpunkt).

## B-Splines 

### Grundlagen

[Dieses Video](https://www.youtube.com/watch?v=bE1MrrqBAl8) listet zu Beginn die praktischen Probleme mit Bézierkurven auf. Zum Beispiel, dass das Hinzufügen oder Ändern eines Kontrollpunktes die gesamte Kurve verändert. Diese Probleme können gelöst werden, indem man mehrere Bézierkurven miteinander verbindet. Das Ergebnis ist ein sogenannter Spline, insbesondere ein B-Spline (Basis Spline). Das Video erklärt auch, dass eine Vereinigung von quadratischen Bézierkurven einen uniformen quadratischen B-Spline und eine Vereinigung von kubischen Bézierkurven einen uniformen kubischen B-Spline bildet.

Aus den Videos können wir nützliche \"Regeln\" für B-Splines entnehmen:

-   Der erste und letzte Kontrollpunkt ist der End/Startpunkt des Splines.
-   Wie bei Bézierkurven beginnen Splines immer tangential zur Linie zwischen dem Startpunkt und dem ersten Kontrollpunkt (und enden tangential zur Linie zwischen dem letzten Kontrollpunkt und dem Endpunkt).
-   Eine Vereinigung von $S$ Bézierkurven mit dem Grad $D$ hat $S+D$ Kontrollpunkte.
    -   Da man in den meisten Fällen mit kubischen B-Splines arbeitet, kann man sagen, dass $N$ Kontrollpunkte zu $N-3$ Béziersegmenten und diese wiederum zu $N-4$ Segment-Knotenpunkten führen.
-   Ein B-Spline mit dem Grad $D$ bietet in jedem Punkt eine stetige Ableitung $D-1$ der Ordnung.
    -   Für einen kubischen B-Spline bedeutet dies, dass sich die Krümmung (Ableitung zweiter Ordnung) nicht ändert, wenn man von einem Segment zum nächsten reist. Dies ist eine sehr nützliche Eigenschaft, wie wir später sehen werden.

Wenn du an weiteren Details über die Eigenschaften von B-Splines interessiert bist, dann schau dir das Video [MOOC Curves 8.2: Eigenschaften von B-Spline Kurven](https://www.youtube.com/watch?v=xXJylM2S72s) an.

### Grundlage

Der Name *B-Spline* steht für *Basis Spline*. Anstatt den Spline als eine Kombination von Bézierkurven zu bilden, besteht der Ansatz darin, **denselben Spline** auf eine andere Weise zu modellieren. Die Idee ist hierbei, einen anderen Satz von Polynomen als Basis zu verwenden. Eine Linearkombination dieser Basispolynome $B_D(t)$ mit der Ordnung $D$ bildet den B-Spline. [Dieses Video](https://www.youtube.com/watch?v=dPPTCy4L4rY) erklärt den Übergang von den Bézier Kontrollpunkten zu den polynomialen Basisfunktionen, die den Spline beschreiben. Mathematisch können wir einen B-Spline mit dieser Formel beschreiben:

$\quad
c(t)=\sum_{k=0}^{N}p_{k}B_{k, D}(t)$

Dabei ist $p_k$ der $k$-te Kontrollpunkt des B-Splines und zugleich ein Faktor für das $k$-te Basispolynom $B_{k, D}(t)$. Jedes Basispolynom beschreibt den Spline in einem bestimmten Bereich und daher wirkt sich das Verschieben eines Kontrollpunktes nicht auf den gesamten Spline aus. Um dies zu verstehen, empfiehlt es sich, einen Blick auf [this video](https://www.youtube.com/watch?v=vjTyWIKviNc) ab Minute 2:23 zu werfen.

Wie im Video erklärt, sind die Basispolynome Bernstein Polynome. Die Menge der Basispolynome für einen bestimmten B-Spline kann auf diese Weise veranschaulicht werden:

![](images/Bernstein_Polynomials.svg ) 
*Ein Satz von Bernstein Polynomen der Ordnung 4. Sie beschreiben einen B-Spline 4. Ordnung mit 5 Kontrollpunkten.*

An jeder Spline Position $t$ ist die Summe der Polynome 1 (gekennzeichnet durch die orangefarbene Linie). Am Anfang hat nur das rote Polynom einen Einfluss, da alle anderen Polynome dort 0 sind. Bei größerem $t$ wird der Spline durch eine Linearkombination von verschiedenen Basispolynomen beschrieben. In der obigen Abbildung ist jedes Polynom größer als 1 für den gesamten Bereich $0 < t < 1$. Dies ist nicht unbedingt der Fall. Wie im Video gezeigt, sind die Basispolynome grundsätzlich nur für einen bestimmten Bereich der Splineposition größer als 0. Das Intervall, in dem ein Basispolynom größer als 0 ist, wird durch den *Knotenvektor* beschrieben. Wenn du mehr über den Knotenvektor erfahren möchtest, schau dir [dieses Video](https://www.youtube.com/watch?v=ni5NNPCVvDY) an.

### Nicht-uniforme B-Splines 

Eine Eigenschaft der Bernstein Polynome ist, dass bei Betrachtung der verschiedenen S-Spline Bézier Teile die Pfadlänge jedes Teils gleich ist. (Die Pfadlänge wird oft als \"Laufzeit\" bezeichnet). Wie Sie sich vorstellen können, kann es nützlich sein, B-Splines zu haben, deren Bézier Teile unterschiedliche Pfadlängen haben. Dies kann durch Gewichtung der verschiedenen Polynome erreicht werden:


<div class="mw-translate-fuzzy">

$\quad
c(t)=\sum_{k=0}^{N}d_{k}B_{k, D}(t)w_k$


</div>

$w_k$ ist dabei das Gewicht des $k$-ten Kontrollpunktes. Wenn die Gewichte nicht gleich sind, nennt man den B-Spline **nicht-uniform**.

Vor allem wenn B-Splines für die 3D Modellierung verwendet werden sollen, sind normalisierte, nicht-uniforme B-Splines erforderlich. Die Normalisierung erfolgt durch eine Division durch die gewichteten Basisfunktionen. Wenn also alle $w_k$ gleich sind, erhält man einen einheitlichen B-Spline, unabhängig von der Gewichtung selbst:


<div class="mw-translate-fuzzy">

$\quad
c(t)=\cfrac{\sum_{k=0}^{N}d_{k}B_{k, D}(t)w_k}{\sum_{k=0}^{N}B_{k, D}(t)w_k}$


</div>

Diese nicht-uniformen und rationalen (wegen der Division) B-Splines werden oft **NURBS** genannt. Ein Blick auf die Formel zeigt, dass es sich tatsächlich um einen B-Spline mit einer gewichteten Basis $R_{k, D}(t)$ handelt:


<div class="mw-translate-fuzzy">

$\quad
c(t)=\sum_{k=0}^{N}d_{k}R_{k, D}(t)$


</div>

wohingegen

$\quad
R_{k, D}=\cfrac{B_{k,D}(u)w_k}{\sum_{l=1}^N B_{l,D}(t)w_l}$

## B-splines in FreeCAD 

FreeCAD bietet die Möglichkeit, uniforme oder nicht-uniforme B-Splines beliebigen Grades in 2D über die [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) zu erstellen.

### Erstellung

Um B-Splines zu erstellen, gehe in eine Skizze und verwende die Werkzeugleistenschaltfläche **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [B-spline erstellen](Sketcher_CreateBSpline/de.md)**. Dann Linksklick um einen Kontrollpunkt zu setzen, bewege die Maus Linksklick, um den nächsten Kontrollpunkt zu setzen und so weiter. Abschließend Rechtsklick, um die Definition abzuschließen und den B-Spline zu erstellen.

Standardmäßig werden gleichmäßige kubische Splines erstellt, es sei denn, es gibt nicht genügend Kontrollpunkte, um dies zu tun. Wenn du also einen B-Spline mit nur 2 Kontrollpunkten erstellst, erhältst du natürlich einen Spline, der eine einzelne lineare Bézierkurve ist, für 3 Kontrollpunkte erhältst du eine quadratische Bézierkurve, erst mit 5 Kontrollpunkten erhältst du einen kubischen B-Spline, der aus 2 Béziersegmenten besteht.

Um periodische B-Splines (B-Splines, die eine geschlossene Kurve bilden) zu erstellen, verwende die Werkzeugleistenschaltfläche **[<img src=images/Sketcher_CreatePeriodicBSpline.svg style="width:16px"> [Periodische B-spline](Sketcher_CreatePeriodicBSpline/de.md)**. Es ist nicht notwendig, den letzten Kontrollpunkt auf den ersten zu setzen, da der B-Spline automatisch geschlossen wird:

![](images/Sketcher_Periodic-B-spline-creation.gif )

B-Splines können auch aus bestehenden Skizzen Segmenten erzeugt werden. Markiere dazu die Elemente und drücke den Werkzeugleistenknopfltfläche **[<img src=images/Sketcher_BSplineApproximate.svg style="width:24px"> [Geometrie in B-Spline umwandeln](Sketcher_BSplineApproximate/de.md)**.

While creating a B-spline, its degree can be specified by pressing the **D** key. With this, the default to create a cubic B-spline if possible, can be overridden. <small>(v0.20)</small> 

### Ändern des Grads 

Um den Grad zu ändern, wähle den B-Spline und verwende entweder die Werkzeugleistenschaltfläche **[<img src=images/Sketcher_BSplineIncreaseDegree.svg style="width:24px"> [B-Spline-Grad erhöhen](Sketcher_BSplineIncreaseDegree.md)** oder **[<img src=images/Sketcher_BSplineDecreaseDegree.svg style="width:24px"> [B-Spline-Grad vermindern](Sketcher_BSplineDecreaseDegree/de.md)**.

**Hinweis:** Das Verringern des Grads kann eine vorherige Erhöhung des Grads nicht rückgängig machen, siehe die Wiki Seite [B-spline Grad vermindern](Sketcher_BSplineDecreaseDegree/de.md) für eine Erklärung.

### Ändern der Knotenvielfalt 

Die Punkte, an denen zwei Bézierkurven miteinander verbunden werden, um den B-Spline zu bilden, werden Knoten genannt. Die Knotenmultiplikation bestimmt, wie die Bézier Teile verbunden werden, siehe die Wiki Seite [Knotenvielfalt erhöhen](Sketcher_BSplineIncreaseKnotMultiplicity/de.md) für Details.

Um die Knotenvielfalt zu ändern, verwende die Werkzeugleistenschaltflächen in der **[<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:24px"> [B-spline Knotenvielfalt erhöhen](Sketcher_BSplineIncreaseKnotMultiplicity/de.md)** oder **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:24px"> [B-spline Knotenvielfalt vermindern](Sketcher_BSplineDecreaseKnotMultiplicity/de.md)**.

**Hinweis:** Das Erstellen von zwei B-Splines, die miteinander verbunden sind, wird sich nicht zu einem einzigen neuen B-Spline vereinigen. Ihr Verbindungspunkt ist also kein Knoten. Die einzige Möglichkeit, einen neuen Knoten in einem bestehenden B-Spline zu erhalten, besteht darin, den Grad zu verringern. Dabei können jedoch viele neue Knoten entstehen. Daher ist es besser, den B-Spline mit mehr Kontrollpunkten neu zu zeichnen.

### Ändern des Gewichts 

Um jeden Kontrollpunkt herum siehst du einen dunkelgelben Kreis. Sein Radius legt das Gewicht für den entsprechenden Kontrollpunkt fest. Standardmäßig haben alle Kreise den Radius *1*. Dies wird durch eine Radiusbeschränkung für den ersten Kontrollpunktkreis angezeigt.

Um einen nicht-uniformen B-Spline zu erzeugen, müssen die Gewichte ungleichmäßig sein. Um dies zu erreichen, kannst du entweder die [Radiusbeschränkung](Sketcher_ConstrainRadius/de.md) des ersten Kontrollpunktkreises ändern:

![](images/Sketcher_Changing-control-point-weigth-constraint.gif )

oder du löschst die Beschränkung, dass alle Kreise gleich sind, und legst dann verschiedene Radiusbeschränkungen für die Kreise fest.

Wenn keine Radiusbeschränkung festgelegt ist, kannst du den Radius auch durch Ziehen ändern:

![](images/Sketcher_Changing-control-point-weigth-dragging.gif )

Am Beispiel des Ziehens siehst du, dass ein hohes Gewicht die Kurve zum Kontrollpunkt zieht, während ein sehr niedriges Gewicht die Kurve so verändert, als ob der Kontrollpunkt fast nicht existiert.

Wenn du dir die [Erstellungsfunktion](#Nicht-uniforme_B-splines.md) für nicht-uniformee rationale B-Splines ansehst, siehst du, dass ein Gewicht von Null zu einer Division durch Null führen würde. Daher kannst du nur Gewichte größer als Null angeben.

### Editing Knots 

New knots can be added using the **[<img src=images/Sketcher_BSplineInsertKnot.svg style="width:24px"> [B-spline insert knot](Sketcher_BSplineInsertKnot.md)** button. <small>(v0.20)</small> 

Deleting knots is not yet possible, see section [Limitations](#Limitations.md).

### Informationen anzeigen 

Da die Form eines B-Splines nicht viel über seine Eigenschaften aussagt, bietet FreeCAD [verschiedene Werkzeuge](Sketcher_Workbench/de#Skizzierer_B-spline_Werkzeuge.md), um die Eigenschaften anzuzeigen:

+++
| Eigenschaft         | Werkzeugleistenschaltfläche                                                                                                                        |
+++
| **Grad**            |                                                                                                                                     |
|                     | **[<img src=images/Sketcher_BSplineDegree.svg style="width:16px"> [B-Spline-Grad anzeigen/ausblenden](Sketcher_BSplineDegree/de.md)**                                |
|                     |                                                                                                                                                 |
+++
| **Kontrollpolygon** |                                                                                                                                     |
|                     | **[<img src=images/Sketcher_BSplinePolygon.svg style="width:16px"> [Kontrollpolygon für B-Spline anzeigen/ausblenden](Sketcher_BSplinePolygon/de.md)**               |
|                     |                                                                                                                                                 |
+++
| **Krümmungskamm**   |                                                                                                                                     |
|                     | **[<img src=images/Sketcher_BSplineComb.svg style="width:16px"> [B-Spline Krümmungskamm anzeigen/ausblenden](Sketcher_BSplineComb/de.md)**                           |
|                     |                                                                                                                                                 |
+++
| **Knotenvielfalt**  |                                                                                                                                     |
|                     | **[<img src=images/Sketcher_BSplineKnotMultiplicity.svg style="width:16px"> [B-Spline Knotenvielfalt anzeigen/ausblendenn](Sketcher_BSplineKnotMultiplicity/de.md)** |
|                     |                                                                                                                                                 |
+++
| **Gewichte**        |                                                                                                                                     |
|                     | **[<img src=images/Sketcher_BSplinePoleWeight.svg style="width:16px"> [Gewicht des B-Spline Kontrollpunkts anzeigen/ausblenden](Sketcher_BSplinePoleWeight/de.md)**  |
|                     |                                                                                                                                                 |
+++

### Begrenzungen

Im Augenblick (FreeCAD 0.19) gibt es einige Begrenzungen bei der Verwendung von Splines, die du kennen solltest:

1.  Du kannst keine tangentialen Beschränkungen festlegen. In diesem Beispiel <img alt="" src=images/Sketcher_spline-limit-tangential.png  style="width:450px;"> willst du sicherstellen, dass der Spline die blaue Kurve 2 mal tangential berührt. Dies ist sinnvoll, da die blaue Linie z.B. die räumliche Grenze für deinen Entwurf sein könnte.
2.  Du kannst keinen neuen Kontrollpunkt zwischen zwei ausgewählten bestehenden Kontrollpunkten einfügen. Es gibt keine andere Möglichkeit, als den Spline neu zu zeichnen.
3.  Du kannst einen Kontrollpunkt nicht löschen. Auch in diesem Fall musst du den Spline neu zeichnen.
4.  Du kannst keine Versatzkurve für einen B-Spline mit dem Werkzeug [Entwurf Versatz](Draft_Offset/de.md) erstellen.

## Typische Anwendungsfälle 

Entsprechend den Eigenschaften von B-Splines gibt es 3 Hauptanwendungsfälle:

1.  Kurven, die tangential zu einer bestimmten Richtung beginnen/enden. Ein Beispiel hierfür ist das Motivationsbeispiel [oben](#Motivation.md).
2.  Kurven, die größere Entwürfe beschreiben und die Freiheit lokaler Änderungen bieten. Siehe [dieses Beispiel](#Gestaltung.md) unten.
3.  Kurven, die eine gewisse Stetigkeit (Ableitung) bieten. Siehe [dieses Beispiel](#Stetigkeit_an_geometrischen_Übergängen.md) unten.

### Gestaltung

Nimm zum Beispiel den Fall, dass du ein Gehäuse für eine Küchenmaschine entwirfst. Die gewünschte Form sollte wie diese aussehen:

![](images/Sketcher_spline-exmple-mixer-shell.png )

Für die Definition der äußeren Form ist es vorteilhaft, einen B-Spline zu verwenden, denn wenn du einen Kontrollpunkt änderst, um die Krümmung an der Unterseite zu ändern, wird die Krümmung an den Seiten und oben nicht geändert:

![](images/Sketcher_spline-exmple-mixer-sketch.gif )

### Stetigkeit an geometrischen Übergängen 

Es gibt mehrere Fälle, in denen es physikalisch notwendig ist, an geometrischen Übergängen eine gewisse Oberflächenkontinuität zu haben. Nimm zum Beispiel die Innenwände eines Flüssigkeitskanals. Wenn sich der Durchmesser des Kanals ändert, möchte man keine Kante haben, da Kanten zu Turbulenzen führen würden. Daher verwendet man, wie im Motivationsbeispiel [oben](#Motivation.md), Splines für diesen Zweck.

Auslöser für die Entwicklung der Bézierkurven war zunächst die französische Autoindustrie. Neben der Einsparung von Material und der Verringerung des Luftwiderstands sollte auch das Aussehen der Autos verbessert werden. Und wenn man sich das schicke Design französischer Autos aus den 60er und 70er Jahren anschaut, sieht man, dass die Bézierkurven dem Autodesign einen Schub gegeben haben.

Nehmen wir zum Beispiel diese Aufgabe bei der Gestaltung von Autos: Der Autokotflügel soll \"schön\" aussehen. Hier ist eine grundlegende Skizze unserer Aufgabe:

<img alt="" src=images/Spline-Fender-sketch1.svg  style="width:250px;">

\"Schön aussehen\" bedeutet, dass der (potenzielle) Kunde den Kotflügel betrachtet und keine unerwarteten Lichtreflexe und auch keine plötzlichen Veränderungen in der Reflexion des Autolacks sieht. Was brauchst du also, um Veränderungen in den Reflexionen zu vermeiden? Genaues Hinsehen auf den Kotflügel:

<img alt="" src=images/Spline-Fender-sketch2.svg  style="width:300px;"> 
*Im räumlichen Bereich oberhalb der Kante ist die Intensität des reflektierten Lichts gering (gekennzeichnet durch die rote Ellipse), da kein Licht direkt in die Richtung von der Kante zum Auge reflektiert wird.*

Du siehst, wenn es eine Kante gibt, gibt es einen räumlichen Bereich, in dem das reflektierte Licht eine geringere Intensität hat, und das ist es, was du beim Betrachten des Kotflügels bemerken wirst. Um dies zu vermeiden, brauchst du eine kontinuierliche Änderung der Neigung deiner Oberflächenelemente. Die Steigung ist die Ableitung erster Ordnung und wie im Abschnitt [Grundlagen](#Grundlagen.md) erklärt, bietet ein B-Spline zweiten Grades (quadratisch) an jedem Punkt eine kontinuierliche Ableitung erster Ordnung.

Aber ist das wirklich ausreichend? Am Punkt des geometrischen Übergangs haben wir nun auf beiden Seiten die gleiche Steigung, aber die Steigung kann sich auf beiden Seiten unterschiedlich verändern. Dann haben wir diese Situation:

<img alt="" src=images/Spline-Fender-sketch3.svg  style="width:300px;">

Wir haben also auch räumliche Bereiche, in denen die Intensität des reflektierten Lichts unterschiedlich ist. Um dies zu vermeiden, benötigen wir am geometrischen Übergangspunkt auch eine Stetigkeit der Ableitung zweiter Ordnung und damit einen kubischen B-Spline.



---
![](images/Right_arrow.png) [documentation index](../README.md) > B-Splines/de
