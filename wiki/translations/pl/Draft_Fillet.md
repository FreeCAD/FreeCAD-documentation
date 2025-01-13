---
 GuiCommand:
   Name: Draft Fillet
   Name/pl: Rysunek Roboczy: Zaokrąglenie
   MenuLocation: Kreślenie , Zaokrąglenie<br>Kreślenie 2D , Zaokrąglenie
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   Shortcut: **F** **I**
   Version: 0.19
   SeeAlso: Draft_Line/pl, Draft_Wire/pl
---

# Draft Fillet/pl



## Opis

Polecenie <img alt="" src=images/Draft_Fillet.svg  style="width:24px;"> **Zaokrąglenie** tworzy zaokrąglenie, zaokrąglony narożnik lub sfazowanie, prostą krawędź między dwiema wskazanymi krawędziami.

W {{VersionMinus/pl|0.21}} to polecenie działa poprawnie tylko jeśli obie wskazane krawędzie są proste.

W {{VersionMinus/pl|1.0}} jeśli wskazane obiekty mają wiele krawędzi, użyta zostanie ich pierwsza krawędź. Może to nie być krawędź, która została wskazana w [widoku 3D](3D_view/po.md).

<img alt="" src=images/Draft_Fillet_example.png  style="width:400px;"> 
*Kilka zaokrągleń i sfazowań utworzonych między dwiema liniami*



## Użycie

1.  Wybierz dwie krawędzie, które spotykają się w jednym punkcie.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_Fillet.svg" width=16px> '''Zaokrąglenie'''**.
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Wybierz z menu opcję **Kreślenie → <img src="images/Draft_Fillet.svg" width=16px> Zaokrąglenie**.
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Kreślenie 2D → <img src="images/Draft_Fillet.svg" width=16px> Zaokrąglenie** z menu.
    -   Użyj skrótu klawiaturowego: **F**, a następnie **I**.
3.  Wpisz **Promień zaokrąglenia**. Należy pamiętać, że polecenie nie powiedzie się, jeśli promień jest zbyt duży dla wybranych krawędzi.
4.  Opcjonalnie zaznacz opcję **Usuń oryginalne obiekty**.
5.  Opcjonalnie zaznacz opcję **Utwórz sfazowanie**.
6.  Jeśli wybrano jedną z dwóch poprzednich opcji: Kliknij w polu wprowadzania **Promień zaokrąglenia**.
7.  Naciśnij **Enter**.



## Opcje

-   Naciśnij przycisk **Esc** lub przycisk **Zamknij** aby przerwać wykonywanie polecenia.



## Uwagi

-   Zaokrąglenie nie może być edytowane, ani nie jest powiązane z krawędziami, które zostały użyte do jego utworzenia.
-   [Polilinia](Draft_Wire/pl.md), która ma co najmniej trzy punkty, może zostać zaokrąglona lub sfazowana poprzez zmianę odpowiednio właściwości **Promień** lub **Rozmiar sfazowania**. Ponieważ [linia](Draft_Line/pl.md) i [polilinia](Draft_Wire/pl.md) mogą być łączone za pomocą komendy [polilinia](Draft_Wire/pl.md), komendy [Połącz](Draft_Join/pl.md) lub komendy [Ulepsz kształt](Draft_Upgrade/pl.md), zapewnia to alternatywną metodę tworzenia zaokrągleń i sfazowań.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Zaokrąglenie wywodzi się z obiektu [Część: Part2DObject](Part_Part2DObject/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Rysunek Roboczy}}

-    **Koniec|VectorDistance**: *(tylko do odczytu)* określa punkt końcowy zaokrąglenia.

-    **Promień zaokrąglenia|Length**: *(tylko do odczytu)* promień, do utworzenia zaokrąglenie.

-    **Długość|Length**: *(tylko do odczytu)* określa całkowitą długość zaokrąglenia.

-    **Start|VectorDistance**: *(tylko do odczytu)* określa punkt początkowy zaokrąglenia.



### Widok


{{TitleProperty|Rysunek Roboczy}}

-    **Rozmiar strzałki|Length**: określa rozmiar symbolu wyświetlanego na końcu zaokrąglenia.

-    **Styl strzałki|Enumeration**: określa typ symbolu wyświetlanego na końcu zaokrąglenia, którym może być {{value|Kropka}}, {{value|Okrąg}}, {{value|Strzałka}}, {{value|Grot}} lub {{value|Grot-2}}.

-    **Zakończenie strzałki|Bool**: określa, czy na końcu zaokrąglenia ma być wyświetlany symbol, aby można go było użyć jako linii adnotacji.

-    **Wzór|Enumeration**: nie używane.

-    **Wzór Size|Float**: nie używane.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć zaokrąglenie, użyj metody `make_fillet` modułu Rysunek Roboczy.


```python
fillet = make_fillet([edge1, edge2], radius=100, chamfer=False, delete=False)
```

-   Tworzy obiekt `Fillet` pomiędzy krawędziami `edge1` i `edge2`, używając `radius` dla krzywizny.
-   Jeśli `chamfer` ma wartość `True`, utworzy prostą krawędź zamiast zaokrąglonej.
-   Jeśli `delete` jest `True`, usunie podane `edge1` i `edge2` i pozostawi tylko nowy obiekt.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

edge1 = Draft.make_line(p1, p2)
edge2 = Draft.make_line(p2, p3)

doc.recompute()

fillet = Draft.make_fillet([edge1, edge2], radius=500)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Fillet/pl
