---
 GuiCommand:
   Name: Draft Rotate
   Name/pl: Rysunek Roboczy: Obróć
   MenuLocation: Modyfikacja , Obróć
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Shortcut: **R** **O**
   SeeAlso: Draft_SubelementHighlight/pl
   Version: 0.7
---

# Draft Rotate/pl



## Opis

Polecenie <img alt="" src=images/Draft_Rotate.svg  style="width:24px;"> **Obróć** - obraca lub kopiuje wybrane obiekty wokół punktu środkowego o zadany kąt. W trybie elementu podrzędnego polecenie obraca wybrane punkty i krawędzie lub kopiuje wybrane krawędzie [linii](Draft_Line/pl.md) i [polilinii](Draft_Wire/pl.md).

Narzędzie Przesuń może być używane na obiektach 2D utworzonych za pomocą środowisk pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), ale może być również używane dla wielu typów obiektów 3D, takich jak te utworzone za pomocą środowisk pracy [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md).

<img alt="" src=images/Draft_Rotate_example.jpg  style="width:400px;"> 
*Obracanie obiektu przy użyciu punktu środkowego.*



## Użycie

Zobacz także strony: [Rysunek Roboczy: Przyciąganie](Draft_Snap/pl.md) i [Rysunek Roboczy: Wiązania](Draft_Constrain/pl.md).

1.  Opcjonalnie wybierz jeden lub więcej obiektów, albo jeden lub więcej elementów podrzędnych [linii](Draft_Line/pl.md) lub [polilinii](Draft_Wire/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Rotate.svg" width=16px> '''Obróć'''**.
    -   Wybierz z menu **Modyfikacja → <img src="images/Draft_Rotate.svg" width=16px> Obróć**.
    -   Użyj skrótu klawiaturowego: **R**, a następnie **O**.
3.  Jeśli nie zaznaczyłeś jeszcze obiektu: wybierz obiekt w oknie [widoku 3D](3D_view/pl.md).
4.  Otworzy się panel zadań **Obróć**. Zobacz [Opcje](#Opcje.md), aby uzyskać więcej informacji.
5.  Jeśli zostały wybrane elementy podrzędne: zaznacz pole wyboru **Modyfikuj elementy podrzędne**, aby włączyć tryb pracy z elementami podrzędnymi.
6.  Wybierz pierwszy punkt, środek obrotu, w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px>. Wprowadź punkt**.
7.  Wybierz drugi punkt w [widoku 3D](3D_view/pl.md), lub wprowadź **Kąt bazowy**.
8.  Wybierz trzeci punkt w oknie [widoku 3D](3D_view/pl.md), lub wprowadź **Obrót**.



## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi *(w wersji 0.22)*.

-   Aby ręcznie wprowadzić współrzędne środka obrotu, wprowadź składowe X, Y i Z, a następnie naciśnij klawisz **Enter** po każdej z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy masz już żądane wartości. Wskazane jest, aby przed wprowadzeniem współrzędnych wysunąć kursor poza okno[widoku 3D](3D_view/pl.md).
-   Naciśnij klawisz **G** lub kliknij pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne są odniesione do globalnego układu współrzędnych, w przeciwnym razie są one odniesione do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md). {{Version/pl|0.20}}
-   Naciśnij klawisz **N** lub kliknij w polu wyboru **Kontynuuj**, aby przełączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie zostanie uruchomione ponownie po zakończeniu. Ten tryb naprawdę ma sens tylko wtedy, gdy włączony jest tryb kopiowania. W zależności od preferencji **Wybierz obiekty bazowe po skopiowaniu**, albo oryginalne obiekty są wybierane do następnego wywołania polecenia, albo kopie, które zostały utworzone jako ostatnie. Zobacz [Ustawienia](#Ustawienia.md).
-   Naciśnij klawisz **C** lub kliknij pole wyboru **Kopiuj**, aby przełączyć tryb kopiowania. Jeśli tryb kopiowania jest włączony, polecenie utworzy obrócone kopie zamiast obracania oryginalnych obiektów.
-   Naciśnij klawisz **B** lub kliknij pole wyboru **Modifikuj elementy podrzędne**, aby przełączyć tryb elementów podrzędnych. Jeśli tryb elementów podrzędnych jest włączony, polecenie będzie używać wybranych elementów podrzędnych zamiast całych obiektów. Elementy podrzędne muszą należeć do [linii](Draft_Line/pl.md) lub [polilinii](Draft_Wire/pl.md).
-   Jeśli tryb kopiowania i tryb elementów podrzędnych są włączone, a krawędzie [polilinii](Draft_Wire/pl.md) są zaznaczone, nowe linie zostaną utworzone z tych krawędzi.
-   Przytrzymanie klawisza **Alt** po wprowadzeniu polecenia **Kąt bazowy** również przełączy tryb kopiowania. Gdy klawisz **Alt** jest przytrzymany, można wybrać wiele punktów dla polecenia **Obróć**. Zwolnij klawisz **Alt**, aby zakończyć polecenie i zobaczyć utworzone kopie.
-   Naciśnij **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).
-   Naciśnij klawisz **Esc** lub przycisk **Zamknij**, aby przerwać polecenie.



## Uwagi

-   Obiekt, który jest [mocowany](Part_EditAttachment/pl.md) nie może być obracany za pomocą polecenia Obróć. Aby go obrócić, należy obrócić jego obiekt {{PropertyData/pl|podparcia}} lub zmienić jego właściwość {{PropertyData/pl|przesunięcie umocowania}}.



## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Ustawienia](Draft_Preferences/pl.md).

-   Aby ponownie wybrać obiekty bazowe po skopiowaniu obiektów: **Edycja → Preferencje → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Zaznacz obiekty bazowe po skopiowaniu**.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz

[Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Do obracania obiektów służy metoda `rotate` środowiska Rysunek Roboczy.


```python
rotated_list = rotate(objectslist, angle, center=Vector(0,0,0), axis=Vector(0,0,1), copy=False)
```

-    `objectslist`zawiera obiekty, które mają zostać obrócone. Może to być pojedynczy obiekt lub lista obiektów.

-    `kąt`określa kąt obrotu w stopniach.

-    `środek`określa punkt środkowy obrotu.

-    `oś`wskazuje kierunek osi obrotu.

-   Jeśli parametr `kopia` posiada wartość {{True/pl}}, to zamiast obracania oryginalnych obiektów tworzone są ich kopie.

-   Zwracana jest lista `rotated_list` z oryginalnymi obróconymi obiektami lub z nowymi kopiami. Jest to albo pojedynczy obiekt, albo lista obiektów, w zależności od `objectlist`.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=300)
Draft.move(polygon1, App.Vector(1000, 0, 0))

# Rotation around the origin
angle1 = 45
rot2 = Draft.rotate(polygon1, angle1, copy=True)
rot3 = Draft.rotate(polygon1, 2*angle1, copy=True)
rot4 = Draft.rotate(polygon1, 4*angle1, copy=True)

polygon2 = Draft.make_polygon(3, radius=1000)
polygon3 = Draft.make_polygon(5, radius=500)
Draft.move(polygon2, App.Vector(2000, 0, 0))
Draft.move(polygon3, App.Vector(2000, 0, 0))

# Rotation around another point
angle2 = 60
cen = App.Vector(3100, 0, 0)
list2 = [polygon2, polygon3]
rot_list2 = Draft.rotate(list2, angle2, center=cen, copy=True)
rot_list3 = Draft.rotate(list2, 2*angle2, center=cen, copy=True)
rot_list4 = Draft.rotate(list2, 4*angle2, center=cen, copy=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rotate/pl
