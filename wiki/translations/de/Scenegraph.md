# Scenegraph/de




{{TOCright}}

## Einführung

Die Geometrie, die in den [3D Ansichten](3D_view/de.md) von FreeCAD erscheint, wird von der [Coin3D](https://en.wikipedia.org/wiki/Coin3D) Bibliothek gerendert. Coin3D ist eine Implementierung des [OpenInventor](https://en.wikipedia.org/wiki/Open_Inventor) Standards. Die [OpenCASCADE](https://en.wikipedia.org/wiki/Open_Cascade_Technology) Software bietet ebenfalls die gleiche Funktionalität, aber es wurde in der sehr frühen Phase von FreeCAD entschieden, nicht den eingebauten OpenCASCADE Betrachter zu verwenden, sondern auf die leistungsfähigere Coin3D Software umzusteigen. Eine gute Möglichkeit, diese Bibliothek kennenzulernen, ist das Buch [Open Inventor Mentor](http://www-evasion.imag.fr/Membres/Francois.Faure/doc/inventorMentor/sgi_html/).

## Beschreibung

[OpenInventor](https://en.wikipedia.org/wiki/Open_Inventor) ist eine 3D Szenenbeschreibungssprache. Die in OpenInventor beschriebene Szene wird dann in OpenGL auf deinem Bildschirm gerendert. Coin3D kümmert sich darum, so dass Programmierer sich nicht mit komplexen OpenGL Aufrufen befassen müssen, sondern einfach gültigen OpenInventor Code zur Verfügung stellen können. Der große Vorteil ist, dass OpenInventor ein sehr bekannter und gut dokumentierter Standard ist.

Eine der großen Aufgaben, die FreeCAD für dich übernimmt, ist die Übersetzung von OpenCASCADE Geometrieinformationen in die OpenInventor Sprache.

OpenInventor beschreibt eine 3D Szene in Form einer [Szenengraph](https://de.wikipedia.org/wiki/Szenengraph), wie die folgende:

![](images/Scenegraph.gif )


<div class="mw-translate-fuzzy">


*Bild entnommen aus [http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/ Inventor mentor]*


</div>

Ein OpenInventor Szenengraph beschreibt alles, was zu einer 3D Szene gehört, wie Geometrie, Farben, Materialien, Licht, usw. und organisiert all diese Daten in einer komfortablen und übersichtlichen Struktur. Alles kann in Unterstrukturen gruppiert werden, so dass Du Deine Szeneninhalte so gestalten kannst, wie Du es willst. Hier ist ein Beispiel für eine OpenInventor Datei: {{Code|lang=bash|code=
#Inventor V2.0 ascii
 
Separator { 
    RotationXYZ {   
       axis Z
       angle 0
    }
    Transform {
       translation 0 0 0.5
    }
    Separator { 
       Material {
          diffuseColor 0.05 0.05 0.05
       }
       Transform {
          rotation 1 0 0 1.5708
          scaleFactor 0.2 0.5 0.2
       }
       Cylinder {
       }
    }
}
}}

Wie man sieht, ist die Struktur sehr einfach. Es werden Trennzeichen verwendet, um Daten in Blöcken zu organisieren. Ein wenig wie Dateien in Ordnern organisieren würden. Jede Anweisung wirkt sich auf das aus, was als nächstes kommt, z.B. sind die ersten beiden Elemente unseres Wurzel Trennzeichens eine Rotation und eine Translation. Beide wirken sich auf das nächste Element aus, das ein Trennzeichen ist. In diesem Trennzeichen wird ein Material definiert und eine weitere Transformation durchgeführt. Unser Zylinder wird daher von beiden Umwandlungen betroffen sein, von der einen, die direkt auf ihn angewendet wurde, und von der anderen, die auf sein übergeordnetes Trennelement angewendet wurde.

Wir haben auch viele andere Arten von Elementen, um unsere Szene zu organisieren, wie Gruppen, Schalter oder Anmerkungen. Wir können sehr komplexe Materialien für unsere Objekte definieren, mit Farbe, Texturen, Schattierungsmodi und Transparenz. Wir können auch Lichter, Kameras und sogar Bewegungen definieren. Es ist sogar möglich, Skriptteile in openInventor Dateien einzubetten, um komplexere Verhaltensweisen zu definieren.

Wenn du mehr über openInventor erfahren möchtest, gehe direkt zu seiner bekanntesten Referenz: der [Inventor mentor](http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/).

In FreeCAD müssen wir normalerweise nicht direkt mit dem openInventor Szenengraph interagieren. Jedes Objekt in einem FreeCAD Dokument, sei es ein Netz, eine Teilform oder etwas anderes, wird automatisch in openInventor Code konvertiert und in den Hauptszenengraphen eingefügt, den du in einer [3D Ansicht](3D_view/de.md) siehst. Dieser Szenegraph wird kontinuierlich aktualisiert, wenndu Objekte änderst, hinzufügst oder entfernst. Tatsächlich hat jedes Objekt (im Applikationsraum) einen Ansichtsanbieter (ein entsprechendes Objekt im Gui Raum), der für die Ausgabe von openInventor Code verantwortlich ist.

Es gibt jedoch viele Vorteile, um direkt auf die Szenegrafik zugreifen zu können. So können wir beispielsweise das Aussehen eines Objekts vorübergehend ändern oder Objekte zur Szene hinzufügen, die im FreeCAD Dokument nicht wirklich existieren, wie z.B. Konstruktionsgeometrie, Helfer, grafische Hinweise oder Werkzeuge wie Manipulatoren oder Bildschirminformationen.

FreeCAD selbst verfügt über mehrere Werkzeuge, um openInventor-Code zu sehen oder zu ändern. Der folgende Python Code zeigt beispielsweise die openInventor Darstellung eines ausgewählten Objekts: 
```python
obj = FreeCAD.ActiveDocument.ActiveObject
viewprovider = obj.ViewObject
print viewprovider.toString()

``` Aber wir haben auch ein Python-Modul, das den vollständigen Zugriff auf alles, was von Coin3D verwaltet wird, ermöglicht, wie z.B. unsere FreeCAD-Szenengrafik. Also, lies weiter mit [Pivy](Pivy/de.md).

## Coding examples 

See [Coin3d snippets](Coin3d_snippets.md) courtesy of MariwanJ\'s research for the [Design456 Workbench](Design456_Workbench.md). The code repository of said examples can be found at <https://github.com/MariwanJ/COIN3D_Examples>.

[Anfang](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md)
