---
- GuiCommand:
   Name:Draft Arc
   Name/pl:Rysunek Roboczy: Łuk
   MenuLocation:Kreślenie → Narzędzia łuku → Łuk
   Workbenches:[Rysunek Roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md)
   Shortcut:**A** **R**
   Version:0.7
   SeeAlso:[Okrąg](Draft_Circle/pl.md), [Łuk przez trzy punkty](Draft_Arc_3Points/pl.md)
---

# Draft Arc/pl

## Opis

Polecenie <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> **Tworzy różne rodzaje łuków** utworzy łuk kołowy w bieżącej [płaszczyźnie roboczej](Draft_SelectPlane/pl.md) ze środka, promienia, kąta początkowego i kąta wierzchołkowego. Promień i kąty mogą być zdefiniowane przez wybranie punktów.

Łuk jest w rzeczywistości obiektem typu [okrąg](Draft_Circle/pl.md) z {{PropertyData/pl|kątem pierwszym}}, który nie jest taki sam jak jego {{PropertyData/pl|kąt drugi}}.

<img alt="" src=images/Draft_Arc_example.jpg  style="width:400px;"> 
*Łuk zdefiniowany za pomocą czterech punktów, środka, promienia, punkty początku i końca łuku.*

## Użycie

Zobacz również [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Arc.svg" width=16px> [Tworzy różne rodzaje łuków ...](Draft_Arc/pl.md)**.
    -   Wybierz z menu opcję **Kreślenie → Narzędzia łuku → <img src="images/Draft_Arc.svg" width=16px> Łuk**.
    -   Użyj skrótu klawiaturowego: **A**, a następnie **R**. {{Version/pl|0.20}}
2.  Otworzy się panel zadań **Łuk**. Zobacz rozdział [Opcje](#Opcje.md), aby uzyskać więcej informacji.
3.  Wybierz pierwszy punkt - środek łuku, w oknie [widoku 3D](3D_view/pl.md), lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**.
4.  Wybierz drugi punkt w oknie [widoku 3D](3D_view/pl.md), lub wpisz wartość **Promienia**.
5.  Wybierz trzeci punkt w oknie [widoku 3D](3D_view/pl.md), lub wpisz wartość **Kąta rozpoczęcia**.
6.  Wybierz czwarty punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz wartość **Kąta otwarcia**.

## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi.

-   Aby ręcznie wprowadzić współrzędne środka, wprowadź składowe X, Y i Z, a następnie naciśnij klawisz **Enter** po każdej z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy masz już wybrane wartości. Wskazane jest, aby przed wprowadzeniem współrzędnych wysunąć kursor poza okno [widoku 3D](3D_view/pl.md).
-   Naciśnij przycisk **G** lub kliknij pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne są odniesione do globalnego układu współrzędnych, w przeciwnym razie są one odniesione do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md). {{Version/pl|0.20}}
-   Naciśnij klawisz **T** lub kliknij na pole wyboru **Kontynuuj**, aby przełączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie uruchomi się ponownie po zakończeniu pracy, pozwalając na dalsze tworzenie łuków.
-   Wciśnij klawisz **S** by włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).
-   Naciśnij klawisz **Esc** lub przycisk **Zamknij**, aby zakończyć działanie polecenia.

## Uwagi

-   Szkic łuku można edytować za pomocą polecenia [Edycja](Draft_Edit/pl.md).

## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Preferencje](Draft_Preferences/pl.md).

-   Aby zmienić ilość miejsc po przecinku używanych przy wprowadzaniu współrzędnych, promieni i kątów: **Edycja → Preferencje → Ogólne → Jednostki → Ustawienia jednostek → Liczba cyfr po przecinku**.
-   Jeśli w oknie ustawień opcja **Edycja → Preferencje → Rysunek Roboczy → Ustawienia ogólne → Opcje narzędzi do kreślenia → Używaj elementów pierwotnych, gdy jest to możliwe** jest zaznaczona, polecenie utworzy [okrąg](Part_Circle/pl.md) środowiska Część, zamiast okręgu Rysunku Roboczego.

## Właściwości

Zobacz stronę [Rysunek Roboczy: Okrąg](Draft_Circle/pl#W.C5.82a.C5.9Bciwo.C5.9Bci.md).

## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć łuk użyj metody `make_circle` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `makeCircle`.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

arc1 = Draft.make_circle(200, startangle=0, endangle=90)
arc2 = Draft.make_circle(500, startangle=20, endangle=160)
arc3 = Draft.make_circle(750, startangle=-30, endangle=-150)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Arc/pl
