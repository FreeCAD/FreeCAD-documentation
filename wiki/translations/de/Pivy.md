# Pivy/de
{{TOCright}}



## Einführung

[Pivy](Pivy/de.md) ist eine [Python](Python/de.md) Bindungsbibliothek für [Coin](https://github.com/coin3d), die 3D Rendering Bibliothek, die in FreeCAD verwendet wird, um Dinge in einer [3D Ansicht](3D_view/de.md) anzuzeigen. Coin ist eine quelloffene Implementierung der \"Open Inventor\" Spezifikation zur Handhabung von Grafiken. Daher beziehen sich in FreeCAD die Begriffe \"Pivy\", \"Coin\" oder \"Open Inventor\" im Wesentlichen auf die gleiche Sache.

Wenn in einen laufenden Python-Interpreter importiert, erlaubt Pivy direkt mit jedem laufenden Coin-[Szenengraph](Scenegraph/de.md), wie z.B. der [3D-Ansicht](3D_view/de.md) zu kommunizieren, oder sogar neue zu erstellen. Pivy ist nicht erforderlich, um FreeCAD zu kompilieren, aber es wird zur Laufzeit benötigt, wenn auf Python basierende Arbeitsbereiche ausgeführt werden, die Formen auf dem Bildschirm erstellen, wie die Arbeitsbereiche [Draft](Draft_Workbench/de.md) und [Arch](Arch_Workbench/de.md). Aus diesem Grund wird Pivy normalerweise installiert, wenn eine Distribution von FreeCAD installiert wird.

Die Coin Bibliothek ist in mehrere Teile unterteilt, Coin selbst zur Manipulation von Szenegraphen und Bindungen für verschiedene GUI Systeme wie Windows und Qt. Falls auf dem System vorhanden, sind diese Module auch für Pivy verfügbar. Das Coin Modul ist immer vorhanden, und wir werden es sowieso verwenden, da wir uns nicht darum kümmern müssen, unsere 3D Darstellung in irgendeiner Schnittstelle zu verankern, was bereits von FreeCAD getan wird. Alles, was wir tun müssen, ist dies:


```python
from pivy import coin
```



## Szenengraph

Wir haben auf der [Szenengraph](Scenegraph/de.md) Seite gesehen, wie eine typische Coin szene organisiert ist. Alles, was in einer [3D Ansicht](3D_view/de.md) erscheint, ist ein Coin Szenegraph, der auf die gleiche Weise organisiert ist. Wir haben einen Wurzelknoten, und alle Objekte auf dem Bildschirm sind seine Kinder.

FreeCAD hat eine einfache Möglichkeit, auf den Root-Knoten eines 3D-Ansicht Szenengraph zugreifen:


```python
sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
print(sg)
```

Dies gibt den Root-Knoten aus:


```python
<pivy.coin.SoSelection; proxy of <Swig Object of type 'SoSelection *' at 0x360cb60> >
```

Wir können die unmittelbaren Kinder unserer Szene untersuchen:


```python
for node in sg.getChildren():
    print(node)
```

Einige dieser Knoten, wie `SoSeparator` oder `SoGroup`, können selbst Kinder haben. Die vollständige Liste der verfügbaren Coin Objekte findest du in der offiziellen Coin Dokumentation.

Lasst uns versuchen, jetzt etwas zu unserem Szenengraph hinzuzufügen. Wir fügen einen schönen roten Würfel ein:


```python
col = coin.SoBaseColor()
col.rgb = (1, 0, 0)
cub = coin.SoCube()
myCustomNode = coin.SoSeparator()
myCustomNode.addChild(col)
myCustomNode.addChild(cub)
sg.addChild(myCustomNode)
```

Versuchen wir Folgendes:


```python
col.rgb = (1, 1, 0)
```

Wie du siehst, ist alles nach wie vor zugänglich und gleichzeitig veränderbar. Du musst nichts neu berechnen oder neu zeichnen, Coin kümmert sich um alles. Du kannst deinem Szenegraphen Sachen hinzufügen, Eigenschaften ändern, Sachen ausblenden, temporäre Objekte anzeigen, alles. Dies betrifft natürlich nur die Darstellung in der 3D Ansicht. Diese Anzeige wird von FreeCAD bei geöffneter Datei neu berechnet, und wenn ein Objekt neu berechnet werden muss. Wenn du also den Aspekt eines bestehenden FreeCAD Objekts änderst, gehen diese Änderungen verloren, wenn das Objekt neu berechnet wird oder wenn du die Datei erneut öffnest.

Wie bereits erwähnt, ist in einer openInventor Szenografie die Reihenfolge wichtig. Ein Knoten beeinflusst, was als nächstes kommt. Wenn wir zum Beispiel die Möglichkeit haben wollen, unseren Würfel zu bewegen, müssen wir einen `SoTranslation` Knoten **before** dem Würfel hinzufügen


```python
col = coin.SoBaseColor()
col.rgb = (1, 0, 0)
trans = coin.SoTranslation()
trans.translation.setValue([0, 0, 0])
cub = coin.SoCube()
myCustomNode = coin.SoSeparator()
myCustomNode.addChild(col)
myCustomNode.addChild(trans)
myCustomNode.addChild(cub)
sg.addChild(myCustomNode)
```

Um unseren Würfel zu bewegen, können wir jetzt folgendes tun:


```python
trans.translation.setValue([2, 0, 0])
```

Zum Schluß etwas entfernen wird ausgeführt mit:


```python
sg.removeChild(myCustomNode)
```


{{Top}}



## Rückrufe

Ein [callback mechanism](http://en.wikipedia.org/wiki/Callback_%28computer_science%29) ist ein System, das es einer Bibliothek, wie z.B. unserer Coin Bibliothek, erlaubt, Sie zurückzurufen, d.h. eine bestimmte Funktion von deinem aktuell laufenden Python Objekt aus aufzurufen. Auf diese Weise kann Coin dich darüber informieren, dass ein bestimmtes Ereignis in der Szene aufgetreten ist. Coin kann sehr unterschiedliche Dinge beobachten, wie z.B. Mausposition, Mausklicks, das Drücken von Tasten auf der Tastatur und vieles mehr.

FreeCAD bietet eine einfache Möglichkeit, solche Rückrufe zu verwenden:


```python
from pivy import coin

class ButtonTest:
    def __init__(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.callback = self.view.addEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.getMouseClick) 

    def getMouseClick(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == coin.SoMouseButtonEvent.DOWN:
            print("Alert!!! A mouse button has been improperly clicked!!!")
            self.view.removeEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.callback)

ButtonTest()
```

Die Rückmeldung muss von einem Objekt initiiert werden, da dieses Objekt zum Zeitpunkt der Rückmeldung noch laufen muss. Siehe auch die [komplette Liste](Code_snippets#Observe_mouse_events_in_the_3D_viewer_via_Python.md) von möglichen Ereignissen und deren Parametern, oder die offizielle Coin-Dokumentation. 

## Dokumentation

Leider verfügt Pivy nicht über eine eigene Dokumentation. Da es sich jedoch um einen genauen Wrapper der Coin Bibliothek handelt, kannst du zur Information die C++ Referenz lesen. In diesem Fall musst du den C++ Klassennamensstil in Python Stil übersetzen.

In C++:


```python
SoFile::getClassTypeId()
```

In Pivy:


```python
SoFile.getClassId()
```

-   [Coin3D](https://github.com/coin3d) Startseite.
-   [Pivy](https://github.com/coin3d/pivy) Startseite.
-   [Coin3D wiki](https://github.com/coin3d/coin/wiki), auf GitHub.
-   [Coin3D wiki documentation](https://github.com/coin3d/coin/wiki/Documentation), auf GitHub.
-   [Coin3D Documentation](https://coin3d.github.io/Coin/html/), die neueste automatisch generierte Doxygen-Dokumentation.
-   [(Open)Inventor Mentor](https://webdocs.cs.ualberta.ca/~graphics/books/mentor.pdf) - empfohlen.



### Ältere

These links provide reference documentation for Coin v3.x. The differences with v4.x are minimal, so they may still be useful.

-   [Coin3D Documentation](https://coin3d.bitbucket.io/Coin/index.html), at BitBucket.
-   [Coin3D Documentation](https://grey.colorado.edu/coin3d/index.html), at University of Colorado.
-   [Open Inventor Reference Documentation](https://mevislabdownloads.mevis.de/docs/current/MeVis/ThirdParty/Documentation/Publish/OpenInventorReference/index.html), by MeVisLab.


{{Top}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Pivy/de
