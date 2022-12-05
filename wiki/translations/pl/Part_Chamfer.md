---
- GuiCommand:/pl
   Name:Part Chamfer
   Name/pl:Część: Fazka
   MenuLocation:Część → Fazka
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Zaokrąglenie](Part_Fillet/pl.md)
---

# Part Chamfer/pl

## Opis

Fazuje wybraną krawędź obiektu. Okno dialogowe pozwala wybrać krawędź do pracy, jak również modyfikować różne parametry fazowania.

![Przykład utworzenia fazki](images/Chamfer-example.png )

## Użycie

1.  Istnieje kilka sposobów aby wywołać polecenie **Fazuj wybrane krawędzie**:
    -   Naciśnij przycisk **<img src="images/Part_Chamfer.svg" width=24px>**.
    -   Użyj pozycji w menu **Część → Fazka**.
2.  Wybierz kształt do wykonania fazek z menu okna dialogowego.
3.  Wybierz krawędzie do fazowania, zaznaczając odpowiednie pole w oknie dialogowym fazy lub wybierając je bezpośrednio na modelu.
4.  Edycja parametrów fazy.
5.  Naciśnij przycisk **OK**, aby zamknąć okno dialogowe fazy i nanieść fazki.

## Opcje

![Okienko dialogowe funkcji fazowania](images/Dialog-chamfer.png )

-   Podczas wybierania krawędzi w modelu, masz możliwość wyboru według krawędzi lub według ściany. Wybranie według ściany spowoduje wybranie wszystkich krawędzi granicznych.
-   Fazowanie o stałej długości lub fazowanie o zmiennej długości.
    -   Faza o stałej długości utworzy fazę o krawędziach równych odległości od oryginalnej krawędzi w podanej odległości.
    -   Faza o zmiennej długości będzie miała krawędzie, które mogą być ustawione w różnych odległościach od oryginalnej krawędzi, co pozwala na utworzenie fazy pod zmiennym kątem.

## Właściwości

![Właściwości funkcji Fazka w środowisku pracy Część](images/Part_Chamfer-Properties.png ) 


{{Properties_Title|Podstawowe}}

-    **Podstawowe**: Kształt, na którym ma być zastosowana fazka.

-    **Umiejscowienie**: Określa orientację i położenie kształtu w przestrzeni 3D.

-    **Etykieta**: Etykieta nadana obiektowi. Zmień ją według własnych potrzeb.




## Ograniczenia

Fazowanie może się nie powieść, jeśli wynik dotknie lub przekroczy następną sąsiednią krawędź. Więc jeśli nie otrzymasz oczekiwanego rezultatu, spróbuj z mniejszą wartością. To samo dotyczy funkcji <img alt="" src=images/Part_Fillet.svg  style="width:24px;"> [Zaokrąglij wybrane krawędzie \...](Part_Fillet/pl.md) środowiska Część.

Zwróć również uwagę, że na funkcję fazowania części wpływa na [Topologiczny problem nazewnictwa](Topological_naming_problem/pl.md), gdy jakakolwiek zmiana jest dokonywana na wcześniejszym etapie modelowania w łańcuchu, który wpływa na liczbę powierzchni lub wierzchołków. Może to spowodować nieprzewidywalny rezultat. Do czasu rozwiązania tego problemu *(prawdopodobnie z v0.20)* zaleca się stosowanie operacji Fazowania i [Zaokrąglania](Part_Fillet/pl.md) na ostatnich etapach łańcucha.

## Tworzenie skryptów 

Narzędzie fazowania może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli środowiska [Python](Python/pl.md) poprzez dodanie obiektu fazowania do dokumentu.

**Przykład skryptu:**


```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part::Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
chmfr = FreeCAD.ActiveDocument.addObject("Part::Chamfer", "myChamfer")
chmfr.Base = FreeCAD.ActiveDocument.myCube
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
chmfr.Edges = myEdges
FreeCADGui.ActiveDocument.myCube.Visibility = False
FreeCAD.ActiveDocument.recompute()
```

**Przykładowe objaśnienie skryptu:**


```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part::Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
```

-   Tworzy sześcian o boku 5 mm, na który będziemy nakładać sfazowane krawędzie. Zobacz stronę [Part_API](Part_API/pl.md) aby uzyskać wyjaśnienie metody **makeBox**.


```python
chmfr = FreeCAD.ActiveDocument.addObject("Part::Chamfer", "myChamfer")
```

-   Dodaje do dokumentu nowy obiekt typu Fazka *(pochodzący z modułu Część)* z etykietą \"myChamfer\".


```python
chmfr.Base = FreeCAD.ActiveDocument.myCube
```

-   Określa, że podstawowym kształtem obiektu fazki powinien być \"myCube\".


```python
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
```

-   Tworzy pustą tablicę \"myEdges\", a następnie dodaje do niej parametry fazy każdej krawędzi.
-   Składnia dla każdego elementu powinna być następująca *(krawędź#, długość początkowa fazy, długość końcowa fazy)*.


```python
chmfr.Edges = myEdges
```

-   Ustawia atrybut Krawędzie naszego obiektu Fazka odpowiadający tablicy, którą właśnie utworzyliśmy.


```python
FreeCADGui.ActiveDocument.myCube.Visibility = False
```

-   Ta linia po prostu ukrywa \"myCube\" tak, aby nasz nowo utworzony obiekt \"myChamfer\" był jedynym widocznym.


```python
FreeCAD.ActiveDocument.recompute()
```

-   Ponownie oblicza wszystkie zmienione elementy na ekranie i odświeża widok.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Chamfer/pl
