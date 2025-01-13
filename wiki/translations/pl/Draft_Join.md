---
 GuiCommand:
   Name: Draft Join
   Name/pl: Rysunek Roboczy: Połącz
   MenuLocation: Modyfikacja , Połącz
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   Shortcut: **J** **O**
   Version: 0.18
   SeeAlso: Draft_Split/pl
---

# Draft Join/pl



## Opis

Polecenie <img alt="" src=images/Draft_Join.svg  style="width:24px;"> **Połącz** środowiska pracy Rysunek Roboczy łączy [linie](Draft_Line/pl.md) i [polilinie](Draft_Wire/pl.md) w jedną linię. Polecenie to jest odpowiednikiem polecenia [Rozdziel](Draft_Split/pl.md).



## Użycie

1.  Punkty końcowe [linii](Draft_Line/pl.md) i / lub [polilinii](Draft_Wire/pl.md), które mają zostać połączone, muszą się dokładnie pokrywać. W razie potrzeby najpierw dostosuj położenie punktów, aby upewnić się, że tak jest.
2.  Wybierz dwie lub więcej [linii](Draft_Line/pl.md) i / lub [polilinii](Draft_Wire/pl.md).
3.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Join.svg" width=16px> '''Połącz'''**.
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Wybierz z menu opcję **Modyfikacja → <img src="images/Draft_Join.svg" width=16px> Połącz**.
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Modyfikacja → <img src="images/Draft_Join.svg" width=16px> Połącz** z menu.
    -   Użyj skrótu klawiaturowego: **J**, a następnie **O**.



## Uwagi

-   [Liniie](Draft_Line/pl.md) i [polilinie](Draft_Wire/pl.md) mogą być również łączone za pomocą narzędzia [polilinia](Draft_Wire/pl.md) lub [Ulepsz kształt](Draft_Upgrade/pl.md).
-   Aby połączyć obiekty, które nie są [liniami](Draft_Line/pl.md) lub [poliliniami](Draft_Wire/pl.md), możesz spróbować użyć [Ulepsz kształt](Draft_Upgrade/pl.md) i/lub [Rozbij kształt](Draft_Downgrade/pl.md) na nich jeden lub więcej razy.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Do Połączenia linii należy użyć metody `join_wires` *({{Version/pl|0.19}})* modułu Rysunek Roboczy. Metoda ta zastępuje przestarzałą metodę `joinWires`. Metoda ta zwraca `Brak`.


```python
join_wires(wires)
```

-    `wires`jest listą obiektów linii, które mają zostać połączone.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(500, 0, 0)
p3 = App.Vector(500, 500, 0)
p4 = App.Vector(0, 500, 0)

wire1 = Draft.make_wire([p1, p2])
wire2 = Draft.make_wire([p2, p3])
wire3 = Draft.make_wire([p3, p4])
wire4 = Draft.make_wire([p4, p1])

Draft.join_wires([wire1, wire3, wire2, wire4])
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Join/pl
