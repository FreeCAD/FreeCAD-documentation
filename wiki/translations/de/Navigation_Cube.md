# Navigation Cube/de
{{TOCright}}

Die Navigationswürfelsteuerung, oder **Navigationswürfel**, ist eine grafische Hilfe der Benutzeroberfläche zur Neuausrichtung der 3D Ansicht. Standardmäßig ist es sichtbar und befindet sich in der oberen rechten Ecke der 3D Anzeige. Wenn Du dir die Standard 3D Ansicht ansiehst, sieht es wie folgt aus:

![](images/FreeCAD-v0-18-NavCube_Axonometric.png )

Der Navigationswürfel besteht aus einer Anzahl mehrerer Teile:

-   Richtungspfeile
-   Hauptnavigationswürfel
-   Mini-Würfel Menü

Schweben des Mauszeigers über eine Funktion des Navigationswürfels, macht das Merkmal hellblau; durch Klicken wird die 3D Ansicht neu ausgerichtet, wie durch die Funktion angezeigt. Im nachfolgenden Beispiel wurde die 3D Ansicht um eine [Mausgeste](Mouse_Model/de.md) in eine \"nicht-standardisierte\" Ausrichtung gedreht. Der Zeiger befindet sich über einer Ecke (angezeigt durch die blaue Farbe); Anklicken richtet die 3D Ansicht zu einer axonometrische Standardansicht neu aus, wobei diese Ecke zu die zeigt.

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

## Richtungspfeile

Es gibt sechs Richtungspfeile: vier dreieckige Pfeilspitzen, eine oben, unten, links und rechts; und zwei gebogene Pfeile, eine auf beiden Seiten des oberen Pfeils.

Durch Anklicken der dreieckigen Pfeile wird die 3D Ansicht um 45 Grad um eine Linie senkrecht zur Pfeilrichtung gedreht. Wenn Du auf die gekrümmten Pfeile klickst, wird die 3D Ansicht um eine Linie gedreht, die auf Dich zeigt. \<Hinweis: Die Drehachsen sind nicht richtig definiert; jede ist der Schnittpunkt von zwei Ebenen, aber ich kann nicht herausfinden, wie ich sie beschreiben soll \--\>

## Hauptnavigationswürfel

Der Hauptnavigationswürfel (im weiteren Verlauf dieses Abschnitts \"Navigationswürfel\" genannt) verfolgt die Ausrichtung des eigentlichen Objekts im Hauptteil der 3D Ansicht. Jede Handlung, die die 3D Hauptansicht neu ausrichtet, richtet auch den Navigationswürfel neu aus.

Der Navigationswürfel ist im Wesentlichen eine 3D-Ansicht eines Würfels, dessen drei Hauptkomponententypen (Flächen, Kanten und Ecken) vergrößert wurden, sodass sie mit dem Zeiger leicht angeklickt werden können. Durch Klicken auf eine bestimmte Komponente wird die 3D-Ansicht so eingestellt, dass diese Komponente zentriert ist und dir zugewandt ist. Der Navigationswürfel ist etwas \"gequetscht\", als ob das von dir am weitesten entfernte Element größer wäre als das Element, das dir direkt zugewandt ist. Auf diese Weise können die Elemente neben dem Element, das dir zugewandt ist, angezeigt und folglich ausgewählt werden. Wenn beispielsweise in einer \"normalen\" Ansicht eines normalen Würfels eine Seite dir zugewandt ist, kannst du auch die vier Kanten dieser Fläche und die vier Ecken dieser Fläche sehen. In dem \"gequetschten\" Navigationswürfel kannst du auch Merkmale sehen, die jede der benachbarten Flächen darstellen, wobei die vier Kanten die Ecken der Ihnen zugewandten Fläche mit der gegenüberliegenden Fläche und die Ecken der gegenüberliegenden Fläche verbinden. Auf diese Weise kannst du eine der möglichen Standardansichten mit Ausnahme der gegenüberliegenden Fläche und ihrer Kanten auswählen (21 von 26 möglichen Ansichten):

-   Die dir zugewandte Fläche (führt nichts aus, da dies die aktuelle Ansicht ist)
-   Die vier Kanten der aktuellen Ansichtsfläche
-   Die vier Ecken der aktuellen Fläche
-   Die vier benachbarten Flächen
-   Die vier Kanten, die zur gegenüberliegenden Fläche führen
-   Die vier Ecken der gegenüberliegenden Fläche

Nicht sichtbar:

-   Die gegenüberliegende Fläche
-   Die Kanten der gegenüberliegenden Fläche

Anmerkung: Zum Zeitpunkt dieser Beschreibung (v 0.18) gibt es einige Probleme mit dem Navigationswürfel; derzeit sind nicht alle Funktionen wählbar. Insbesondere sind die Ränder nicht wählbar, ebenso wenig wie die vier Ecken der unmittelbar gegenüberliegenden Fläche.

### Oberflächenauswahl

Durch Klicken auf eine Fläche wird die 3D-Ansicht so ausgerichtet, dass die jeweilige Fläche dir zugewandt ist. In der Flächenansicht stehen andere Auswahlpunkte zur Verfügung, wie oben angegeben. An jeder der Außenkanten befinden sich vier dünne \"Balken\", die die vier benachbarten Flächen darstellen. Wenn du darauf klickst, wird die Ansicht ausgewählt, die der angrenzenden Fläche entspricht. Es gibt vier runde Ecken, mit denen die entsprechende axonometrische Ansicht eingestellt werden kann. Es gibt auch einen inneren Satz von Kanten und Ecken, die derzeit nicht funktionsfähig ist.

### Kantenauswahl

Leider ist die Kantenauswahl derzeit fehlerhaft. Wenn du versuchst, eine Kante auszuwählen, wird die Fläche ausgewählt, die dahinter liegt. Wenn du auf eine Kante klickst, sollte diese Kante so zentriert sein, dass sie dir zugewandt ist.

### Eckenauswahl

Wenn du auf eine der Ecken klickst, erhältst du eine axonometrische Ansicht von dieser Ecke aus. Wie oben erwähnt, können derzeit, wenn eine Fläche direkt auf dich gerichtet ist, die Ecken dieser Fläche nicht ausgewählt werden.

## Miniwürfelmenü

In unteren rechten Ecke des Navigationswürfels befindet sich ein kleiner Würfel. Der Typ der Ansicht (orthographic, perspektivisch oder isometrisch) kann in einem Menü geändert werden, wenn man auf diesen Würfel klickt. Damit wird auch die Ansicht auf die Fenstergröße angepasst.

## Verschieben der Navigationswürfeldarstellung 

Du kannst die gesamte Navigationswürfelkontrollstruktur an eine andere Stelle in der 3D Darstellung verschieben, indem du die Maus an einer beliebigen Stelle im Hauptnavigationswürfels drückst und ziehst. Die Struktur beginnt sich erst dann zu bewegen, wenn der Mauszeiger den Rand des Hauptnavigationswürfels hinter sich gelassen hat.

## Konfiguration

Der Navigationswürfel ist konfigurierbar, einschließlich der Anpassung seiner Größe: **Bearbeiten → Einstellungen... → Anzeige → Navigation → Navigationswürfel** {{Version/de|0.19}}.

Für eine erweiterte Konfiguration beziehe dich auf das [WürfelMenü](Interface_Customization/de#CubeMenu.md) [externe Arbeitsbereiche](External_workbenches/de.md).







_

---
[documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/de
