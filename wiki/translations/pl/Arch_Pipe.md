---
 GuiCommand:
   Name: Arch Pipe
   Name/pl: BIM: Rura
   MenuLocation: 3D / BIM , Rura
   Workbenches: BIM_Workbench/pl
   Shortcut: **P** **I**
   Version: 0.17
   SeeAlso: 
---

# Arch Pipe/pl



## Opis

Narzędzie **Rura** umożliwia tworzenie rur od podstaw lub z wybranych obiektów. Wybrane obiekty muszą być oparte na obiektach środowiska Część *(szkic, szkic itp.)* i zawierać jedną i tylko jedną otwartą polilinię.



## Użycie

Opcjonalnie wybierz liniowy kształt [Części](Part_Workbench/pl.md), taki jak [linia](Draft_Line/pl.md), [polilinia](Draft_Wire/pl.md) środowiska Rysunek Roboczy lub otwarty [szkic](Sketcher_NewSketch/pl.md).

1.  Polecenie to można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Arch_Pipe.svg" width=16px> [Rura](Arch_Pipe/pl.md)** na pasku narzędzi.

    -   Naciśnij **P**, a następnie **I** skrót klawiaturowy.

    -   
        **3D / BIM → Rura**
        
        z menu głównego.



## Opcje

-   Obiekty Rur dzielą wspólne właściwości i zachowania wszystkich [komponentów](Arch_Component/pl.md) środowiska Architektura.



## Właściwości



### Dane


{{TitleProperty|Komponent}}

-    **Base|Link**: Polilinia bazowa tej rury, jeśli istnieje.

Informacje o innych właściwościach w tej grupie można znaleźć na stronie [Komponent](Arch_Component/pl#Właściwości.md).


{{TitleProperty|Rura}}

-    **Średnica|Length**: Średnica tej rury, jeśli jej **Typ profilu** to {{Value|Okrąg}}.

-    **Wysokość|Length**: Wysokość tej rury, jeśli jej **Typ profilu** to {{Value|Prostokąt}}.

-    **Długość|Length**: Długość tej rury, jeśli nie jest oparta na polilinii.

-    **Offset End|Length**: Przesunięcie od punktu końcowego rury. Automatycznie ustawiane, jeśli w tym punkcie zostanie dodana [Kształtka](Arch_PipeConnector/pl.md), aby dopasować rurę do łącznika. Zobacz [Typowy przepływ pracy](#Typowy_przepływ_pracy.md) poniżej.

-    **Początek odsunięcia|Length**: Przesunięcie od punktu początkowego rury. Jak wyżej.

-    **Profil|Link**: Bazowy profil tej rury. Jeśli nie jest ustawiony, profil rury jest określany przez **Typ profilu**.

-    **Typ profilu|Enumeration**: Profil tej rury. Używany tylko, jeśli **Profil** nie jest ustawiony. Opcje to: {{Value|Okrąg}}, {{Value|Kwadrat}} lub {{Value|Prostokąt}}.

-    **Grubość ściany|Length**: Grubość ściany tej rury.

-    **Szerokość|Length**: Szerokość tej rury, jeśli jej **Typ profilu** to {{Value|Kwadrat}} lub {{Value|Prostokąt}}.



## Typowy przepływ pracy 

-   Zacznij od umieszczenia urządzeń sanitarnych / hydraulicznych *(poniżej znajduje się zaimportowany plik step)*. Obiekty te można przekształcić w wyposażenie Architektury, wybierając je i naciskając przycisk [Wyposażenie](Arch_Equipment/pl.md).

![](images/Arch_pipe_example_01.jpg )

-   Wyposażenie Architektury ma teraz nową właściwość **Punkty przyciągania**, która jest listą wektorów 3D. Pozwala to na dodanie niestandardowych punktów przyciągania, do których można przyciągać, gdy nowy przycisk przyciągania [specjalnego](Draft_Snap_Special/pl.md) jest włączony. Obecnie ta właściwość jest dostępna tylko w środowisku Python. W powyższym przypadku dodałem nowy punkt przyciągania przy wyjściu z urządzenia WC. Wektory wewnątrz Punktów Przyciągania pojawiają się na modelu jako białe kropki:

FreeCAD.ActiveDocument.Equipment.SnapPoints=[FreeCAD.Vector(0,0,100)]

![](images/Arch_pipe_example_02.jpg )

-   Dzięki nowemu [specjalnemu](Draft_Snap_Special/pl.md) przyciąganiu, możesz teraz przyciągać do tych punktów niestandardowych:

![](images/Arch_pipe_example_03.jpg )

-   Teraz możemy narysować orurowanie przy użyciu linii, polilinii środowiska Rysunek Roboczy lub szkiców. Najlepszym sposobem jest jednak użycie tylko linii rysunku roboczego:

![](images/Arch_pipe_example_04.jpg )

-   Pojawiło się nowe narzędzie [Ustaw nachylenie](Draft_Slope/pl.md), które pozwala na zmianę nachylenia linii Draft, na przykład do 5% (0.05). Dzięki temu możemy szybko nadać naszym liniom odpadów prawidłowe nachylenie. Narzędzie to zmienia tylko współrzędne z, więc musimy tylko przyciągnąć je do siebie, rzut z góry pozostanie niezmieniony.

![](images/Arch_pipe_example_05.jpg )

-   Teraz wystarczy zaznaczyć wszystkie linie i nacisnąć przycisk [Rura](Arch_Pipe/pl.md). Narzędzie Rura działa z każdym obiektem opartym na Części, który zawiera jedną i tylko jedną otwartą polilinię.

![](images/Arch_pipe_example_06.jpg )

-   Możemy teraz tworzyć połączenia, wybierając 2 lub 3 zbiegające się rury i naciskając przycisk [Kształtka](Arch_PipeConnector/pl.md). Jeśli wybrano 3 rury, dwie z nich muszą być wyrównane, aby utworzyć trójnik:

![](images/Arch_pipe_example_07.jpg )

-   Zmiana promienia łączników nie zmienia długości linii bazowej, a jedynie wynikową rurę *(poprzez zmianę ich właściwości StartOdsunięcia lub ZakończenieOdsunięcia)*. W ten sposób można nadal rysować układ linii tylko z liniami prostymi, bez konieczności dbania o krzywe i promienie.

Możliwe jest również tworzenie rur bez linii bazowej, w tym przypadku należy użyć właściwości \"Długość\" do zdefiniowania długości.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Rura** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
pipe = makePipe(baseobj=None, diameter=0, length=0, placement=None, name="Pipe")
```

-   Tworzy obiekt `pipe` z danego `baseobj` i `diameter`.
    -   
        `baseobj`
        
        to [Rysunek Roboczy: Linia](Draft_Line/pl.md) lub [Rysunek Roboczy: Polilinia](Draft_Wire/pl.md).

    -   Jeśli `baseobj` jest pominięty, można utworzyć prostą rurę podając tylko `diameter` (średnicę) i `length` (długość w kierunku Z).
-   Jeśli `placement` jest podane, będzie użyte.


```python
import Draft, Arch

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2500, 200, 0)
p3 = FreeCAD.Vector(3100, 1000, 0)
p4 = FreeCAD.Vector(3500, 500, 0)
line = Draft.make_wire([p1, p2, p3, p4])

pipe = Arch.makePipe(line, 200)
FreeCAD.ActiveDocument.recompute()

pipe2 = Arch.makePipe(diameter=120, length=3000)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > Arch Pipe/pl
