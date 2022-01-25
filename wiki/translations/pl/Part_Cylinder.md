---
- GuiCommand:/pl
   Name:Part Cylinder
   Name/pl:Część: Walec
   MenuLocation:Część → Bryła pierwotna → Walec
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Bryły pierwotne](Part_CreatePrimitives/pl.md)
---

# Part Cylinder/pl

## Opis

Tworzy zwykły walec, z parametrami dotyczącymi jego położenia, kąta, promienia i wysokości.

## Użycie

1.  Otwórz środowisko pracy **<img src="images/_Workbench_Part.svg" width=16px> [Część](Part_Workbench/pl.md)**.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Cylinder.svg" width=16px> Walec** na pasku narzędzi,
    -   Użyj pozycji menu głównego **Część → Bryła pierwotna → <img src="images/Part_Cylinder.svg" width=16px> Walec**.

**Wynik:** Domyślnie jest to pełny walec o promieniu 2mm i wysokości 10mm, wyśrodkowany wzdłuż globalnej osi z i dołączony do globalnej płaszczyzny xy.

Właściwości walca mogą być później edytowane w [edytorze właściwości](Property_editor/pl.md) lub przez podwójne kliknięcie stożka w [widoku drzewa](Tree_view/pl.md).

<img alt="walec utworzony przy pomocy narzędzia Utwórz walec" src=images/cylinder.png  style="width:650px;">

## Właściwości

-    **Kąt**: Jest to kąt obrotu, który umożliwia utworzenie części walca *(domyślnie ustawiony jest na 360°)*.

-    **Wysokość**: Wysokość to odległość w kierunku osi z.

-    **Promień**: Promień definiuje płaszczyznę w płaszczyźnie x-y.

-    **Kąt pierwszy**: Kąt w pierwszym kierunku {{Version/pl|0.20}}.

-    **Kąt drugi**: Kąt w drugim kierunku {{Version/pl|0.20}}.

## Tworzenie skryptów 

Walec środowiska pracy Część można utworzyć przy pomocy następującej funkcji:


```python
cylinder = FreeCAD.ActiveDocument.addObject("Part::Cylinder", "myCylinder")
```

-   Gdzie parametr {{Incode|"myCylinder"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cylinder/pl
