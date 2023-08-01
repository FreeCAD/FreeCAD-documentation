# Scenegraph/de
## Einführung

Die Geometrie, die in den [3D-Ansichten](3D_view/de.md) von FreeCAD erscheint, wird von der [Coin3D-Bibliothek](https://en.wikipedia.org/wiki/Coin3D) gerendert. Coin3D ist eine Implementierung des [Open Inventor-Standards](https://en.wikipedia.org/wiki/Open_Inventor). Die [OpenCASCADE-Software](https://en.wikipedia.org/wiki/Open_Cascade_Technology) bietet ebenfalls die gleiche Funktionalität, aber es wurde in der sehr frühen Phase von FreeCAD entschieden, nicht den eingebauten OpenCASCADE-Betrachter zu verwenden, sondern auf die leistungsfähigere Coin3D-Software umzusteigen. Eine gute Möglichkeit, diese Bibliothek kennenzulernen, ist das Buch [Open Inventor Mentor](http://www-evasion.imag.fr/Membres/Francois.Faure/doc/inventorMentor/sgi_html/).



## Beschreibung

[Open Inventor](https://en.wikipedia.org/wiki/Open_Inventor) ist eine 3D-Szenenbeschreibungssprache. Die in Open Inventor beschriebene Szene wird dann in OpenGL auf dem Bildschirm gerendert. Coin3D kümmert sich darum, so dass Programmierer sich nicht mit komplexen OpenGL Aufrufen befassen müssen, sondern nur gültigen Open Inventor-Code zur Verfügung stellen müssen. Der große Vorteil ist, dass Open Inventor ein sehr bekannter und gut dokumentierter Standard ist.

Eine der großen Aufgaben, die FreeCAD für dich übernimmt, ist die Übersetzung von OpenCASCADE Geometrieinformationen in die Open Inventor-Sprache.

Open Inventor beschreibt eine 3D-Szene in Form eines [Szenengraphen](https://de.wikipedia.org/wiki/Szenengraph), wie dem folgenden:

![](images/Scenegraph.gif ) 
*Bild entnommen aus [https://web.archive.org/web/20190807185912/http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/ Inventor mentor]*

Ein Open Inventor-Szenengraph beschreibt alles, was zu einer 3D-Szene gehört, wie Geometrie, Farben, Materialien, Licht, usw. und organisiert all diese Daten in einer praktischen und übersichtlichen Struktur. Alles kann in Unterstrukturen gruppiert werden, so dass Du deine Szeneninhalte so gestalten kannst, wie Du es willst. Hier ist ein Beispiel für eine Open Inventor-Datei:


{{Code|lang=bash|code=
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

Wie man sieht, ist die Struktur sehr einfach. Es werden Unterteilungen (separators) verwendet, um Daten in Blöcken zu organisieren; ein wenig wie Dateien in Ordnern zu organisieren. Jede Anweisung wirkt sich auf das aus, was als nächstes kommt, z.B. sind die ersten beiden Elemente unseres Wurzel-Elements (root separator) eine Drehung (Rotation) und eine Verschiebung (Translation); Beide wirken sich auf das nächste Element aus, das eine weitere Unterteilung (separator) ist. In dieser Unterteilung wird ein Material definiert und eine weitere Transformation. Unser Zylinder ist daher von beiden Transformationen betroffen, von der einen, die direkt auf ihn angewendet wurde, und von der anderen, die auf sein übergeordnetes Unterteilungselement angewendet wurde.

Wir haben auch viele andere Arten von Elementen, um unsere Szene zu organisieren, wie Gruppen, Schalter oder Anmerkungen. Wir können sehr komplexe Materialien für unsere Objekte definieren, mit Farbe, Texturen, Schattierungsmodi und Transparenz. Wir können auch Lichter, Kameras und sogar Bewegungen definieren. Es ist sogar möglich, Skriptteile in Open Inventor-Dateien einzubetten, um komplexere Verhaltensweisen zu definieren.

Mehr über Open Inventor erfährt man unter seiner bekanntesten Referenz: [Inventor mentor](http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/).

In FreeCAD müssen wir normalerweise nicht direkt mit dem Open Inventor-Szenengraph interagieren. Jedes Objekt in einem FreeCAD-Dokument, sei es ein Netz, eine Part-Form oder etwas anderes, wird automatisch in Open Inventor-Code konvertiert und in den Haupt-Szenengraphen eingefügt, der in einer [3D-Ansicht](3D_view/de.md) dargestellt wird. Dieser Szenengraph wird kontinuierlich aktualisiert, wenn Objekte geändert, hinzugefügt oder entfernt werden. Tatsächlich hat jedes Objekt (im App-Raum) einen Viewprovider (ein entsprechendes Objekt im Gui-Raum), der für die Ausgabe von Open Inventor-Code verantwortlich ist.

Es hat jedoch viele Vorteile, direkt auf den Szenengraph zuzugreifen. So können wir beispielsweise vorübergehend das Aussehen eines Objekts ändern oder Objekte zur Szene hinzufügen, die im FreeCAD-Dokument nicht wirklich existieren, wie z.B. Konstruktionsgeometrie, Hilfselemente, grafische Hinweise oder Werkzeuge wie Manipulatoren oder Bildschirminformationen.

FreeCAD selbst verfügt über mehrere Werkzeuge, um Open Inventor-Code anzusehen oder zu ändern. Der folgende Python-Code zeigt beispielsweise die Open Inventor-Darstellung eines ausgewählten Objekts:


```python
obj = FreeCAD.ActiveDocument.ActiveObject
viewprovider = obj.ViewObject
print viewprovider.toString()

```

Aber wir haben auch ein Python-Modul, das den vollständigen Zugriff auf alles ermöglicht, was von Coin3D verwaltet wird, wie z.B. unser FreeCAD-Szenengraph. Mehr dazu unter [Pivy](Pivy/de.md).



## Code-Beispiele 

Siehe [Coin3d snippets](Coin3d_snippets/de.md) mit freundlicher Genehmigung von MariwanJ\'s research für den Arbeitsbereich [Design456](Design456_Workbench.md). The code repository can be found at <https://github.com/MariwanJ/COIN3D_Snippet>. {{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Scenegraph/de
