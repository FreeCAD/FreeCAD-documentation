# Pivy/pl
## Wprowadzenie

[Pivy](Pivy/pl.md) jest biblioteką wiążącą [Python](Python/pl.md) do [Coin](https://github.com/coin3d), biblioteką renderowania 3D używaną w FreeCAD do wyświetlania obiektów w oknie [widoku 3D](3D_view/pl.md). Coin jest otwartą implementacją specyfikacji \"Open Inventor\" do obsługi grafiki. Dlatego w środowisku FreeCAD terminy *Pivy*, *Coin* lub *Open Inventor* odnoszą się zasadniczo do tego samego.

Po zaimportowaniu do działającego interpretera Python, Pivy pozwala nam na bezpośrednią komunikację z dowolnym działającym [scenegrafem](Scenegraph/pl.md) Coin, takim jak [widok 3D](3D_view/pl.md), a nawet na tworzenie nowych. Pivy nie jest wymagany do kompilacji FreeCAD, ale jest wymagany podczas uruchamiania opartych na Pythonie środowisk pracy, które tworzą kształty na ekranie, takich jak [Rysunek Roboczy](Draft_Workbench/pl.md) i [Architektura](Arch_Workbench/pl.md). Z tego powodu, Pivy jest zwykle instalowany podczas instalacji programu FreeCAD.

Biblioteka Coin jest podzielona na kilka części, sam Coin do manipulowania scenegrafami oraz wiązania dla kilku systemów GUI, takich jak Windows i Qt. Jeśli są obecne w systemie, moduły te są również dostępne dla Pivy. Moduł Coin jest zawsze obecny i to właśnie z niego będziemy korzystać, ponieważ nie będziemy musieli dbać o zakotwiczenie naszego wyświetlacza 3D w jakimkolwiek interfejsie, to już robi FreeCAD. Jedyne co musimy zrobić to:


```python
from pivy import coin
```

## Scenograf

Na stronie [Scenogram](Scenegraph/pl.md) zobaczyliśmy, jak zorganizowana jest typowa scena Coin. Wszystko, co pojawia się w oknie [widoku 3D](3D_view/pl.md) jest scenegrafem Coin, zorganizowanym w ten sam sposób. Mamy jeden węzeł główny, a wszystkie obiekty na ekranie są jego produktami pochodnymi.

FreeCAD posiada łatwy sposób dostępu do węzła głównego scenegrafu widoku 3D:


```python
sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
print(sg)
```

Spowoduje to zwrócenie węzła głównego:


```python
<pivy.coin.SoSelection; proxy of <Swig Object of type 'SoSelection *' at 0x360cb60> >
```

Możemy skontrolować bezpośrednie obiekty pochodne naszej sceny:


```python
for node in sg.getChildren():
    print(node)
```

Niektóre z tych węzłów, takie jak `SoSeparator` czy `SoGroup`, mogą mieć same elementy pochodne. Pełną listę dostępnych obiektów Coin można znaleźć w oficjalnej dokumentacji Coin.

Spróbujmy teraz dodać coś do naszego scenegrafu. Dodamy ładny czerwony sześcian:


```python
col = coin.SoBaseColor()
col.rgb = (1, 0, 0)
cub = coin.SoCube()
myCustomNode = coin.SoSeparator()
myCustomNode.addChild(col)
myCustomNode.addChild(cub)
sg.addChild(myCustomNode)
```

A teraz spróbujmy tego:


```python
col.rgb = (1, 1, 0)
```

Jak widać wszystko jest nadal dostępne i modyfikowalne w locie. Nie trzeba niczego rekompilować ani przerysowywać, Coin zajmuje się wszystkim. Możesz dodawać obiekty do swojego scenegrafu, zmieniać właściwości, ukrywać je, pokazywać obiekty tymczasowe, cokolwiek zechcesz. Oczywiście, dotyczy to tylko wyświetlania w widoku 3D. Ten widok jest ponownie obliczany przez FreeCAD przy otwieraniu pliku, oraz gdy obiekt wymaga ponownego obliczenia. Tak więc, jeśli zmienisz aspekt istniejącego obiektu FreeCAD, zmiany te zostaną utracone, gdy obiekt zostanie ponownie obliczony lub gdy ponownie otworzysz plik.

Jak już wspomniano, w scenegrafie OpenInventor kolejność jest ważna. Węzeł wpływa na to, co będzie następne. Przykładowo, jeśli chcemy mieć możliwość przesuwania naszego sześcianu, będziemy musieli dodać węzeł `SoTranslation` **przed** sześcianem:


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

Aby przesunąć nasz sześcian możemy teraz zrobić:


```python
trans.translation.setValue([2, 0, 0])
```

Wreszcie usunięcie czegoś jest załatwione:


```python
sg.removeChild(myCustomNode)
```


{{Top}}

## Informacje zwrotne 

Mechanizm [callback](http://en.wikipedia.org/wiki/Callback_%28computer_science%29) to system, który pozwala bibliotece, takiej jak nasza biblioteka Coin, na odpowiadanie, czyli wywoływanie określonej funkcji z aktualnie uruchomionego obiektu Python. W ten sposób Coin może powiadomić Cię, że w scenie wystąpiło jakieś konkretne zdarzenie. Coin może obserwować bardzo różne rzeczy, takie jak pozycja myszy, kliknięcia przycisków myszy, wciśnięte klawisze klawiatury i wiele innych.

FreeCAD posiada łatwy sposób na wykorzystanie takich wywołań zwrotnych:


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

Wywołanie zwrotne musi być zainicjowane z obiektu, ponieważ ten obiekt musi być nadal uruchomiony, gdy nastąpi wywołanie zwrotne. Zobacz także [kompletną listę](Code_snippets/pl#Obserwowanie_zdarze.C5.84_myszy_w_przegl.C4.85darce_3D_za_pomoc.C4.85_.C5.9Brodowiska_Python.md) możliwych zdarzeń i ich parametrów, lub oficjalną dokumentację Coin. {{Top}}

## Dokumentacja

Niestety, Pivy nie ma własnej dokumentacji. Ponieważ jednak jest to dokładny wrapper biblioteki Coin, możesz przeczytać referencję C ++ w celu uzyskania informacji. W tym przypadku musisz przetłumaczyć styl nazewnictwa klas C ++ na styl Pythona.

W C++


```python
SoFile::getClassTypeId()
```

W Pivy:


```python
SoFile.getClassId()
```

-   [Coin3D](https://github.com/coin3d) strona domowa.
-   [Pivy](https://github.com/coin3d/pivy) strona domowa.
-   [Coin3D wiki](https://github.com/coin3d/coin/wiki), na GitHubie.
-   [dokumentacja Wiki dla Coin3D](https://github.com/coin3d/coin/wiki/Documentation), na GitHubie.
-   [Coin3D Documentation](https://coin3d.github.io/Coin/html/), najnowsza, automatycznie generowana dokumentacja Doxygen.
-   [(Open)Inventor Mentor](https://webdocs.cs.ualberta.ca/~graphics/books/mentor.pdf) - zalecane.

### Starsze

Te linki dostarczają dokumentacji referencyjnej dla Coin v3.x. Różnice w stosunku do v4.x są minimalne, więc nadal mogą one być przydatne.

-   [dokumentacja Coin3D](https://coin3d.bitbucket.io/Coin/index.html), na BitBucket.
-   [dokumentacja Coin3D](https://grey.colorado.edu/coin3d/index.html), na University of Colorado.
-   [Open Inventor Reference Documentation](https://mevislabdownloads.mevis.de/docs/current/MeVis/ThirdParty/Documentation/Publish/OpenInventorReference/index.html), publikacja: MeVisLab.


{{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Pivy/pl
