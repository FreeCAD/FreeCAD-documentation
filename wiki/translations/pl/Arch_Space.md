---
 GuiCommand:
   Name: Arch Space
   Name/pl: Architektura: Przestrzeń
   MenuLocation: 3D / BIM , Przestrzeń
   Name/pl: Architektura: 
   Workbenches: BIM_Workbench/pl
   Shortcut: **S** **P**
   Version: 0.14
   SeeAlso: 
---

# Arch Space/pl



## Opis

Narzędzie **Przestrzeń** pozwala zdefiniować pustą objętość, opierając ją na bryle, definiując jej granice lub łącząc oba te sposoby. Jeśli jest on oparty wyłącznie na granicach, objętość jest obliczana poprzez rozpoczęcie od obwiedni wszystkich podanych granic i odjęcie przestrzeni za każdą z nich. Obiekt Przestrzeń zawsze definiuje objętość bryły. Można również wyświetlić powierzchnię podłogi obiektu przestrzeni, obliczoną przez przecięcie płaszczyzny poziomej w środku masy objętości przestrzeni.

<img alt="" src=images/Arch_Space_example.jpg  style="width:640px;">



*Obiekt przestrzenny utworzony z istniejącego obiektu bryłowego, a następnie dodane dwie ściany jako granice.*



## Użycie

1.  Wybierz istniejący obiekt bryły lub ściany obiektów granicznych.
2.  Uruchom polecenie używając jednej z kilku metod:
    -   Naciśnij przycisk **<img src="images/Arch_Space.svg" width=16px> '''Przestrzeń'''** na pasku narzędzi.
    -   Użyj klawiszy **S**, a następnie **P**.
    -   Użyj opcji menu głównego **3D / BIM → Przestrzeń**.



### Ograniczenia

-   Właściwości granic nie są obecnie edytowalne przez GUI.
-   Zobacz [ogłoszenie na forum](http://forum.freecadweb.org/viewtopic.php?f=9&t=4275).



## Właściwości

-    **Baza**: Obiekt bazowy, jeśli istnieje *(musi być bryłą)*.

-    **Granice**: Lista opcjonalnych elementów brzegowych.

-    **Obszar**: Obliczona powierzchnia tej przestrzeni.

-    **Wykończenie podłogi**: Wykończenie podłogi w tej przestrzeni.

-    **Wykończenie ścian**: Wykończenie ścian w tej przestrzeni.

-    **Wykończenie sufitu**: Wykończenie sufitu w tej przestrzeni.

-    **Grupa**: Obiekty znajdujące się w tej przestrzeni, takie jak meble.

-    **Typ przestrzeni**: Rodzaj tej przestrzeni.

-    **Grubość posadzki**: Grubość wykończenia podłogi.

-    **Ilość ludzi**: Liczba osób, które zazwyczaj zajmują tę przestrzeń.

-    **Moc oświetlenia**: Moc elektryczna potrzebna do oświetlenia tej przestrzeni w watach.

-    **Moc wyposażenia**: Moc elektryczna wymagana przez wyposażenie tej przestrzeni w watach.

-    **AutoPower**: Jeśli opcja ma wartość {{True/pl}}, właściwość Moc sprzętu zostanie automatycznie wypełniona przez sprzęt znajdujący się w tej przestrzeni.

-    **Klimatyzacja**: Typ klimatyzacji tej przestrzeni.

-    **Wnętrze**: Określa, czy ta przestrzeń jest wewnętrzna czy zewnętrzna.

-    **Tekst**: Tekst do wyświetlenia. Użyj \$area, \$label, \$tag, \$floor, \$walls, \$ceiling, aby wstawić odpowiednie dane.

-    **Nazwa czcionki**: Nazwa czcionki.

-    **Kolor tekstu**: Kolor tekstu.

-    **Rozmiar czcionki**: Rozmiar tekstu.

-    **Pierwsza linia**: Rozmiar pierwszego wiersza tekstu *(mnoży rozmiar czcionki. 1 = ten sam rozmiar, 2 = podwójny rozmiar, itd.)*

-    **Odstęp między wierszami**: Odstęp między wierszami tekstu.

-    **Pozycja tekstu**: Pozycja tekstu. Pozostaw (0,0,0) dla pozycji automatycznej.

-    **Wyrównanie tekstu**: Wyrównanie tekstu.

-    **Dziesiętne**: Liczba miejsc po przecinku do użycia w tekstach wyliczanych.

-    **Wyświetl jednostki**: Pokaż przyrostek jednostki lub nie.



## Opcje

-   Aby utworzyć strefy grupujące kilka przestrzeni, należy użyć obiektu [Część budynku](Arch_BuildingPart/pl.md) i ustawić jego typ IFC na \"Strefa przestrzeni\".
-   Obiekt Przestrzeń ma te same tryby wyświetlania, co inne obiekty środowiska Architektura i Część, z jednym dodatkowym, zwanym **Footprint**, który wyświetla tylko dolną powierzchnię przestrzeni.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Przestrzeń** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
Space = makeSpace(objects=None, baseobj=None, name="Space")
```

-   Tworzy obiekt `Space` z podanego `objects` lub `baseobj`, który może być
    -   pojedynczym obiektem dokumentu, w którym to przypadku staje się on kształtem bazowym obiektu Space, lub
    -   listą zaznaczonych obiektów zwróconych przez `FreeCADGui.Selection.getSelectionEx()`, lub
    -   listą krotek `(object, subobjectname)`.

Przykład:


```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 1000
Box.Height = 1000

Space = Arch.makeSpace(Box)
Space.ViewObject.LineWidth = 2
FreeCAD.ActiveDocument.recompute()
```

Po utworzeniu obiektu przestrzeni można dodać do niego wybrane powierzchnie za pomocą następującego kodu:


```python
import FreeCAD, FreeCADGui, Draft, Arch

points = [FreeCAD.Vector(-500, 0, 0), FreeCAD.Vector(1000, 1000, 0)]
Line = Draft.makeWire(points)
Wall = Arch.makeWall(Line, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select a face of the wall
selection = FreeCADGui.Selection.getSelectionEx()
Arch.addSpaceBoundaries(Space, selection)
```

Granice można również usunąć, ponownie wybierając wskazane ściany:


```python
selection = FreeCADGui.Selection.getSelectionEx()
Arch.removeSpaceBoundaries(Space, selection)
```



---
⏵ [documentation index](../README.md) > Arch Space/pl
