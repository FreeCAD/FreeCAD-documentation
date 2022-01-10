---
- GuiCommand:/pl
   Name:Part Box
   Name/pl:Część: Prostopadłościan
   MenuLocation:Część → Bryła pierwotna → Sześcian
   Workbenches:[Środowisko pracy Część](Part_Workbench/pl.md)
   SeeAlso:[Bryły pierwotne](Part_Primitives/pl.md)
---

# Part Box/pl

## Opis

Polecenie **Prostopadłościan** ze środowiska prazy [Część](Part_Workbench/pl.md) wstawia parametryczny [prostokątny prostopadłościan](http://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid), jako geometryczną bryłę pierwotną do aktywnego dokumentu. Domyślnie, polecenie Prostopadłościan wstawia sześcian o wymiarach 10 x 10 x 10mm, umieszczony w punkcie początkowym, z etykietą \"sześcian\". Parametry te mogą być modyfikowane po dodaniu obiektu.

<img alt="Part\_Box" src=images/Part_Box.jpg  style="width:400px;">

## Użycie

1.  Przełącz się na środowisko pracy <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Część](Part_Workbench/pl.md)
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Box.svg" width=16px> Utwórz prostopadłościan** na pasku narzędzi.
    -   Wybierz polecenie **Część → Bryła pierwotna → <img src="images/Part_Box.svg" width=16px> Prostopadłościan** z paska menu.

**Wynik:** Domyślnym wynikiem jest sześcian o długości, szerokości i wysokości, wynoszącej 10mm. Jest on dołączony do globalnej płaszczyzny XY, a jedna jego krawędź pokrywa się z globalną osią Z.

Właściwości sześcianu mogą być później korygowane w edytorze właściwości lub przez podwójne kliknięcie na sześcian w drzewie modelu.

## Właściwości


{{Properties_Title|Prostopadłościan}}

-    {{PropertyData/pl|Długość}}: Parametr *długość* jest wymiarem bryły w kierunku X.

-    {{PropertyData/pl|Szerokość}}: Parametr *szerokość* jest wymiarem bryły w kierunku Y.

-    {{PropertyData/pl|Wysokość}}: Parametr *wysokość* jest wymiarem bryły w kierunku Z.

## Tworzenie skryptów 

Prostopadłościan można utworzyć przy pomocy następującej funkcji:


```python
box = FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```

-   Gdzie parametr {{Incode|myBox}} jest etykietą dla obiektu prostopadłościanu.
-   Zwraca nowo utworzony obiekt typu prostopadłościan.

Możesz uzyskać dostęp i modyfikować atrybuty obiektu {{Incode|Prostopadłościanu}}. Na przykład, można zmienić parametry długości, szerokości i wysokości.


```python
box.Length = 25
box.Width = 15
box.Height = 30
```

Możesz zmienić jego umiejscowienie za pomocą:


```python
box.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Box/pl
