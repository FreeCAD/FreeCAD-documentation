---
 GuiCommand:
   Name: Draft Split
   Name/pl: Rysunek Roboczy: Rozdziel
   MenuLocation: Modyfikacja , Rozdziel
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   Shortcut: **S** **P**
   Version: 0.18
   SeeAlso: Draft_Join/pl
---

# Draft Split/pl



## Opis

Polecenie <img alt="" src=images/Draft_Split.svg  style="width:24px;"> **Rozdziel** środowiska pracy Rysunek Roboczy dzieli [linie](Draft_Line/pl.md) lub [polilinie](Draft_Wire/pl.md) w określonym punkcie lub krawędzi. Polecenie to jest odpowiednikiem polecenia [Połącz](Draft_Join/pl.md).



## Użycie

1.  Istnieje kilka sposobów wywołania polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Split.svg" width=16px> '''Rozdziel'''**.
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Wybierz z menu opcję **Modyfikacja → <img src="images/Draft_Split.svg" width=16px> Rozdziel**.
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Modyfikacja → <img src="images/Draft_Split.svg" width=16px> Rozdziel** z menu.
    -   Użyj skrótu klawiaturowego: **S**, a następnie **P**.
2.  Przesuń kursor nad właściwą krawędź [linii](Draft_Line/pl.md) lub [polilinii](Draft_Wire/pl.md).
3.  Krawędź zostanie podświetlona.
4.  Wykonaj jedną z następujących czynności:
    -   Jeśli krzywa jest zamknięta:
        -   Wybierz dowolny punkt na krawędzi.
        -   Krawędź zostanie odłączona od linii i stanie się oddzielną linią.
    -   Jeśli krzywa jest otwarta:
        -   Wybierz odpowiedni punkt na krawędzi. Zobacz [Uwagi](#Uwagi.md).
        -   Lina zostanie podzielona w wybranym punkcie.



## Uwagi

-   Jeśli otwarta polilinia zostanie podzielona, a kliknięty punkt nie leży dokładnie na wybranej krawędzi, nowy punkt nie będzie współliniowy z poprzednią krawędzią. Użyj odpowiedniej opcji [przyciągania](Draft_Snap/pl.md), aby temu zapobiec.
-   Aby podzielić obiekty, które nie są [linią](Draft_Line/pl.md) lub [polilinią](Draft_Wire/pl.md), możesz spróbować użyć narzędzia [Ulepsz kształt](Draft_Upgrade/pl.md) i / lub [Rozbij kształt](Draft_Downgrade/pl.md) na nich jeden lub więcej razy.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby Rozdzielić polilinię, użyj metody `split` modułu Rysunek Roboczy. Metoda ta zwraca `Brak`.


```python
split(wire, newPoint, edgeIndex)
```

-    `wire`obiekt krzywej, który ma zostać podzielony.

-    `newPoint`punkt, w którym ma nastąpić podział.

-    `edgeIndex`indeks krawędzi, na której ma nastąpić podział *(z dokładnością do 1)*.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(500, 0, 0)
p3 = App.Vector(250, 0, 0)

wire = Draft.make_wire([p1, p2])

Draft.split(wire, p3, 1)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Split/pl
