# Pivy/sv
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

[Pivy](http://pivy.coin3d.org/) är ett python bindnings bibliotek för [Coin3d](http://www.coin3d.org), det 3D-renderingsbibliotek som används av FreeCAD. när det importeras i en körande python tolk, så kan du föra en direkt dialog med alla körande [scengrafer](Scenegraph/sv.md), som FreeCAD\'s 3D vyer, eller att även skapa nya. Pivy följer med i en standard FreeCAD installation.


</div>

When imported in a running Python interpreter, Pivy allows us to communicate directly with any running Coin [scenegraph](Scenegraph.md), such as the [3D view](3D_view.md), or even to create new ones. Pivy is not required to compile FreeCAD, but it is required at runtime when running Python-based workbenches that create shapes on screen, like [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md). Because of this, Pivy is normally installed when installing a distribution of FreeCAD.


<div class="mw-translate-fuzzy">

Coin biblioteket är uppdelat i flera delar, själva coin, för manipulation av scengrafer och bindningar för flera GUI system, som windows, eller som i vårt fall, qt. Dessa moduler är även tillgängliga för pivy, beroende på om de finns i systemet. Coin modulen finns alltid, och det är vad vi kommer att använda i alla fall, eftersom vi inte behöver bry oss om att förankra vårt 3D fönster i något gränssnitt, det görs redan av FreeCAD själv. Allt vi behöver göra är detta:


</div>


```python
from pivy import coin
```


<div class="mw-translate-fuzzy">

## Komma åt och ändra scengrafen 


</div>


<div class="mw-translate-fuzzy">

Vi såg i [Scengraf](scenegraph/sv.md) sidan hur en typisk Coin scen är organiserad. Allt som syns i en FreeCAD 3D vy är en coin scengraf, organiserad på samma sätt. Vi har en rotnod, och alla objekt på skärmen är dess barn.


</div>

FreeCAD har ett lätt sätt att komma åt 3D vy scengrafens rotnod:


```python
sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
print(sg)
```

Detta kommer att returnera rotnoden:


```python
<pivy.coin.SoSelection; proxy of <Swig Object of type 'SoSelection *' at 0x360cb60> >
```

Vi kan inspektera vår scen\'s närmaste barn:


```python
for node in sg.getChildren():
    print(node)
```


<div class="mw-translate-fuzzy">

En del av dessa noder, som SoSeparators eller SoGroups, kan själva ha barn. Den kompletta listan på de tillgängliga coin objekten kan återfinnas på [official coin documentation](http://coin3d.bitbucket.org/Coin/classes.html).


</div>

Låt oss försöka lägga till något till vår scengraf nu. Vi lägger till en snygg röd kub:


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

och här är vår (snygga) röda kub. Låt os nu försöka detta:


</div>


```python
col.rgb = (1, 1, 0)
```


<div class="mw-translate-fuzzy">

Se? Allt är fortfarande åtkomligt och förändringsbart direkt. Inget behov av omberäkningar eller omritningar, coin tar hand om allt. Du kan lägga till saker till din scengraf, ändra egenskaper, gömma saker, visa temporära objekt, allting. Detta gäller förstås endast visningen i 3D vyn. Den visningen beräknas om av FreeCAD när filen öppnas, och när ett objekt behöver omberäknas. Så om du ändrar en aspekt på ett existerande FreeCAD objekt, så kommer dessa ändringar att förloras om objektet beräknas om eller när du öppnar filen igen.


</div>


<div class="mw-translate-fuzzy">

En nyckel till arbete med scengrafer i dina skript är att kunna komma åt vissa egenskaper på de noder som du vid behov lägger till. Till exempel, om vi skulle vilja flytta vår kub, så skulle vil ha lagt till en SoTranslation nod till vår anpassade nod, och det skulle ha sett ut så här:


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

Kom ihåg att i en openInventor scengraf, så är ordningen viktig. en nod påverkar efterkommande saker, så du kan säga något som : färg röd, kub, färg gul, sfär, och du kommer att få en röd kub och en gul sfär. Om vi lade till förflyttning till vår existerande anpassade nod, så skulle den komma efter kuben, och inte påverka den. Om vi hade satt in den när vi skapade den, som här ovan, så skulle vi nu kunna göra:


</div>


```python
trans.translation.setValue([2, 0, 0])
```


<div class="mw-translate-fuzzy">

Och vår kub skulle hoppa 2 enheter åt höger. Slutligen, att ta bort något görs med:


</div>


```python
sg.removeChild(myCustomNode)
```


{{Top}}


<div class="mw-translate-fuzzy">

## Använda återanropsmekanismer 


</div>


<div class="mw-translate-fuzzy">

En [återanropsmekanism](http://en.wikipedia.org/wiki/Callback_%28computer_science%29) är ett system som tillåter ett bibliotek som du använder, som vårt coin bibliotek, att anropa tillbaka, vilket innebär att anropa en viss funktion från ditt för närvarande körande python objekt. Detta är väldigt användbart, därför att på det sättet så kan coin meddela python objektet om någon specifik händelse uppstår i scenen. Coin kan övervaka väldigt olika saker, som musposition, musklick, tangentbordsnedtryckningar, och många andra saker.


</div>

FreeCAD erbjuder ett lätt sätt att använda sådana återanrop:


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

Återanropet måste initieras från ett objekt, därför så måste det objektet fortfarande köras när återanropet uppstår.

Se även [den kompletta listan](Code_snippets#Observing_mouse_events_in_the_3D_viewer_via_Python/sv.md) för möjliga händelser och dess parametrar, eller [i den officiella coin dokumentationen](http://doc.coin3d.org/Coin/classes.html).


</div>


{{Top}}


<div class="mw-translate-fuzzy">

## Dokumentation


</div>


<div class="mw-translate-fuzzy">

Olyckligtvis har pivy själv ingen ordentlig dokumentation, men eftersom det är en riktig översättning av coin, så kan du med säkerhet använda coin dokumentationen som referens, och använda python stil istället för c++ stil (till exempel SoFile::getClassTypeId() skulle i pivy bli SoFile.getClassId())


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
-   [(Open)Inventor Mentor](https://webdocs.cs.ualberta.ca/~graphics/books/mentor.pdf) - recommended.

### Older

These links provide reference documentation for Coin v3.x. The differences with v4.x are minimal, so they may still be useful.

-   [Coin3D Documentation](https://coin3d.bitbucket.io/Coin/index.html), at BitBucket.
-   [Coin3D Documentation](https://grey.colorado.edu/coin3d/index.html), at University of Colorado.
-   [Open Inventor Reference Documentation](https://mevislabdownloads.mevis.de/docs/current/MeVis/ThirdParty/Documentation/Publish/OpenInventorReference/index.html), by MeVisLab.


{{Top}}


<div class="mw-translate-fuzzy">


{{docnav/sv|Scenegraph/sv|PySide/sv}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Pivy/sv
