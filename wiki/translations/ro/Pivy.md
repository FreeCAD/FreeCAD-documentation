# Pivy/ro




{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

[Pivy](http://pivy.coin3d.org/) este o bibliotecă de coduri care servește drept punte între Python și coin [Coin3d](http://www.coin3d.org), biblioteca de randare 3D utilizată de către FreeCAD. Atunci când este importat într-un interpretor python care rulează, Pivy permite dialogul direct și imediat cu orice procedură Coin3d care rulează [scenegraphs](Scenegraph.md), ca dexemplu vizualizările FreeCAD 3D , sau chiar creare unora noi. Pivy este inclus în pachetul standard de instalare FreeCAD .


</div>

When imported in a running Python interpreter, Pivy allows us to communicate directly with any running Coin [scenegraph](Scenegraph.md), such as the [3D view](3D_view.md), or even to create new ones. Pivy is not required to compile FreeCAD, but it is required at runtime when running Python-based workbenches that create shapes on screen, like [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md). Because of this, Pivy is normally installed when installing a distribution of FreeCAD.


<div class="mw-translate-fuzzy">

Biblioteca coin este împărțită în mai multe piese, coin însuși, este pentru manipularea scripturilor și legăturilor pentru mai multe sisteme GUI, cum ar fi ferestrele sau, ca în cazul nostru, qt. Modulele respective sunt disponibile și pentru piv, în funcție de situația în care sunt prezente în sistem. Modulul coin este întotdeauna prezent și este ceea ce vom folosi oricum, deoarece nu va trebui să ne pese de ancorarea afișajului nostru 3D în orice interfață, deoarece este deja făcută de cpătre FreeCAD. Tot ce trebuie să facem este:


</div>


```python
from pivy import coin
```


<div class="mw-translate-fuzzy">

## Accesarea și modificarea unui scene grafice 3D 


</div>


<div class="mw-translate-fuzzy">

Am văzut în pagina [Scenegraph](Scenegraph.md) cum Coin organizează o scenă tipică. Tot ce este afișat 3D în FreeCAD este construit și festionat de către Coin. Avem o rădăcină, iar toate obiectele de pe ecran sunt copiii lui.legat prin noduri


</div>

Free cad are un mod facil de a accede la radacina unei scene 3D:


```python
sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
print(sg)
```

Radăcina scenei va fi :


```python
<pivy.coin.SoSelection; proxy of <Swig Object of type 'SoSelection *' at 0x360cb60> >
```

Putrem inspecta imediat copii scenei noastre:


```python
for node in sg.getChildren():
    print(node)
```


<div class="mw-translate-fuzzy">

Unele dintre aceste noduri, cum ar fi SoSeparators sau SoGroups, pot avea proprii copii. Lista completă a obiectelor disponibile pentru programul Coin poate fi găsită în [official coin documentation](http://coin3d.bitbucket.org/Coin/classes.html).


</div>

Acum să încercăm să adăugăm ceva la scenă (proiect). Vom adăuga un frumos cub roșu:


```python
col = coin.SoBaseColor()
col.rgb = (1, 0, 0)
cub = coin.SoCube()
myCustomNode = coin.SoSeparator()
myCustomNode.addChild(col)
myCustomNode.addChild(cub)
sg.addChild(myCustomNode)
```


<div class="mw-translate-fuzzy">

și aici este (frumosul ) nostru cub roșu. Acum. hai să încerca aceasta:


</div>


```python
col.rgb = (1, 1, 0)
```


<div class="mw-translate-fuzzy">

Ai văzut? Totul este încă accesibil și editabil din voleu. Nu este nevoie să recalculați sau să reproiectați nimic, Coin are grijă de tot. Puteți adăuga ceea ce doriți la scenă (proiectul), schimbați proprietățile, ascundeți obiecte, expuneți temporar obiecte, faceți ceva. Desigur, acest lucru afectează numai afișarea vizualizării 3D. Afișarea documentului deschis este recalculată de FreeCAD și recalculează un obiect atunci când trebuie să fie. Deci, dacă modificați aspectul unui obiect existent în FreeCAD, aceste modificări se vor pierde dacă obiectul este recalculat sau când redeschideți fișierul.


</div>


<div class="mw-translate-fuzzy">

Un lucru, pentru a lucra cu scripturile în scenariile tale, poți, când este necesar, să accesezi câteva proprietăți ale nodurilor pe care le-ai adăugat. De exemplu, dacă vrem să mutăm cubul, am fi adăugat un nod SoTranslation la nodul nostru personalizat și,el ar fi arătat astfel:


</div>


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


<div class="mw-translate-fuzzy">

Rețineți că într-un scenariu openInventor, ordinea este importantă. Un nod afectează ceea ce urmează, astfel încât să puteți spune ceva de genul: culoarea roșie, cubul, culoarea galbenă, sfera și veți obține un cub roșu și o sferă galbenă. Dacă am adăugat traducerea la nodul nostru personalizat existent, acesta va veni după cub și nu îl va afecta. Dacă am fi introdus-o


</div>


```python
trans.translation.setValue([2, 0, 0])
```


<div class="mw-translate-fuzzy">

Și cubul nostru ar sări 2 unități la dreapta. În cele din urmă, eliminarea a ceva se face cu:


</div>


```python
sg.removeChild(myCustomNode)
```

[top](#top.md)


<div class="mw-translate-fuzzy">

## Utilizarea mecanismului de trecere în argument a unei alte funcții 


</div>


<div class="mw-translate-fuzzy">

La [callback mechanism](http://en.wikipedia.org/wiki/Callback_%28computer_science%29), Un mecanism de Callback este sistem care permite unei bilbioteci pe caer o utilizați , ca de ex bilbioteca Coin de a trece în argumente a unei alte funcții pentru l\'Objet Python în curs de execuție. Acest lucru este extrem de util, deoarece în acest mod coin vă poate avertiza dacă un anumit eveniment apare în scenă. Coin poate vedea lucruri foarte diferite, cum ar fi poziția mouse-ului, clicurile pe un buton al mouse-ului, tastele de tastatură care sunt apăsate și multe alte lucruri.


</div>

FreeCAD are o modalitate ușoară de a utiliza aceste callbacks:


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


<div class="mw-translate-fuzzy">

Callback-ul a fost pornit de la un obiect, deoarece obiectul trebuie să ruleze în continuare când apare apelul invers. Vezi de asemenea [complete list](Code_snippets#Observing_mouse_events_in_the_3D_viewer_via_Python.md) a posibilelor evenimente și parametrii lor, sau în [official coin documentation](http://doc.coin3d.org/Coin/classes.html).


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

## Documentație


</div>


<div class="mw-translate-fuzzy">

Din păcate, pivy nu dispune încă de o documentație potrivită, dar deoarece există o traducere exactă a lui coin, puteți utilizat în toată securitatea documetația de referință a lui coin, și utilizați stilul Python în locul stilului c ++ ( par exemple SoFile::getClassTypeId() en c++, serait SoFile.getClassId() en pivy ) c++ style (for example SoFile::getClassTypeId() would in pivy be SoFile.getClassId())


</div>

In C++:


```python
SoFile::getClassTypeId()
```

In Pivy:


```python
SoFile.getClassId()
```

-   [Coin3D](https://github.com/coin3d) homepage.
-   [Pivy](https://github.com/coin3d/pivy) homepage.
-   [Coin3D wiki](https://github.com/coin3d/coin/wiki), at GitHub.
-   [Coin3D wiki documentation](https://github.com/coin3d/coin/wiki/Documentation), at GitHub.
-   [Coin3D Documentation](https://coin3d.github.io/Coin/html/), latest automatically generated Doxygen documentation.

### Older

These links provide reference documentation for Coin v3.x. The differences with v4.x are minimal, so they may still be useful.

-   [Coin3D Documentation](https://coin3d.bitbucket.io/Coin/index.html), at BitBucket.
-   [Coin3D Documentation](https://grey.colorado.edu/coin3d/index.html), at University of Colorado.
-   [Open Inventor Reference Documentation](https://mevislabdownloads.mevis.de/docs/current/MeVis/ThirdParty/Documentation/Publish/OpenInventorReference/index.html), by MeVisLab.

[top](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
