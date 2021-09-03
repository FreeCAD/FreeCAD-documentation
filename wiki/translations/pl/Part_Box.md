---
- GuiCommand:/pl
   Name:Part Box
   Name/pl:Część: Prostopadłościan
   MenuLocation:Część → Bryła pierwotna → Sześcian
   Workbenches:[Środowisko pracy Część](Part_Workbench/pl.md)
   SeeAlso:[Bryły pierwotne](Part_Primitives/pl.md)
---

## Opis

Polecenie **Prostopadłościan** ze środowiska prazy [Część](Part_Part_Workbench/pl.md) wstawia parametryczny [prostokątny prostopadłościan](http://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid), jako geometryczną bryłę pierwotną do aktywnego dokumentu. Domyślnie, polecenie Prostopadłościan wstawia sześcian o wymiarach 10 x 10 x 10mm, umieszczony w punkcie początkowym, z etykietą \"sześcian\". Parametry te mogą być modyfikowane po dodaniu obiektu.

<img alt="Part\_Box/pl\|Część: Sześcian" src=images/Part_Box.jpg  style="width:400px;">

## Użycie

1.  Przełącz się na środowisko pracy <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Część](Part_Workbench/pl.md)
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Box.svg" width=16px> Utwórz prostopadłościan** na pasku narzędzi.
    -   Wybierz polecenie {{MenuCommand|Część → Bryła pierwotna → <img src="images/Part_Box.svg" width=16px> Prostopadłościan}} z paska menu.

**Wynik:** Domyślnym wynikiem jest sześcian o długości, szerokości i wysokości, wynoszącej 10mm. Jest on dołączony do globalnej płaszczyzny XY, a jedna jego krawędź pokrywa się z globalną osią Z.

Właściwości sześcianu mogą być później korygowane w edytorze właściwości lub przez podwójne kliknięcie na sześcian w drzewie modelu.

## Właściwości


{{Properties_Title/pl|Podstawowe}}

-    {{PropertyData/pl|Umiejscowienie}}: Określa orientację i położenie obiektu Prostopadłościan w przestrzeni 3D. Zobacz stronę [Umiejscowienie](Placement/pl.md). Punktem odniesienia jest lewy przedni dolny róg bryły.

-    {{PropertyData/pl|Etykieta}}: Etykieta nadana obiektowi. Zmień ją, aby dostosować nazwę do swoich potrzeb.


{{Properties_Title/pl|Prostopadłościan}}

-    {{PropertyData/pl|Długość}}: Parametr *długość* jest wymiarem bryły w kierunku X.

-    {{PropertyData/pl|Szerokość}}: Parametr *szerokość* jest wymiarem bryły w kierunku Y.

-    {{PropertyData/pl|Wysokość}}: Parametr *wysokość* jest wymiarem bryły w kierunku Z.

![Właściwości prostopadłościanu utworzonego w środowisku Część](images/Part_Box-Properties.jpg )

## Tworzenie skryptów {#tworzenie_skryptów}

Polecenie Prostopadłościan może być użyte przez [makrodefinicje](Macros/pl.md) i z konsoli środowiska Python za pomocą następującej funkcji: 
```python
FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```

-   Gdzie parametr *myBox* jest etykietą dla obiektu prostopadłościanu.
-   Zwraca nowo utworzony obiekt typu prostopadłościan.

Możesz uzyskać dostęp i modyfikować atrybuty obiektu Prostopadłościanu. Na przykład, można zmienić parametry długości, szerokości i wysokości. 
```python
FreeCAD.ActiveDocument.myBox.Length = 25
FreeCAD.ActiveDocument.myBox.Width = 15
FreeCAD.ActiveDocument.myBox.Height = 30
```

Możesz zmienić jego umiejscowienie za pomocą: 
```python
FreeCAD.ActiveDocument.myBox.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```





 
