---
 GuiCommand:
   Name: Draft Fillet
   Name/pl: Rysunek Roboczy: Zaokrąglenie
   MenuLocation: Kreślenie , Zaokrąglenie
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Shortcut: **F** **I**
   Version: 0.19
   SeeAlso: Draft_Line/pl, Draft_Wire/pl
---

# Draft Fillet/pl



## Opis

Polecenie <img alt="" src=images/Draft_Fillet.svg  style="width:24px;"> **Zaokrąglenie** tworzy zaokrąglenie, zaokrąglony narożnik lub sfazowanie, prostą krawędź między dwiema [Liniami](Draft_Line/pl.md).

<img alt="" src=images/Draft_Fillet_example.png  style="width:400px;"> 
*Kilka zaokrągleń i fazowań utworzonych między dwiema liniami.*



## Użycie

1.  Wybierz dwie [Linie](Draft_Line/pl.md), które spotykają się w jednym punkcie.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_Fillet.svg" width=16px> '''Zaokrąglenie'''**.
    -   Wybierz z menu opcję **Kreślenie → <img src="images/Draft_Fillet.svg" width=16px> Zaokrąglenie**.
    -   Użyj skrótu klawiaturowego: **F**, a następnie **I**.
3.  Wpisz **Promień zaokrąglenia**. Jeśli wybrano opcję **Utwórz sfazowanie**, będzie to rozmiar fazy *(długość prostej krawędzi)*. Należy pamiętać, że polecenie nie powiedzie się, jeśli promień lub rozmiar fazy jest zbyt duży dla wybranych linii.
4.  Opcjonalnie zaznacz opcję **Usuń oryginalne obiekty:**.
5.  Opcjonalnie zaznacz opcję **Utwórz sfazowanie**.
6.  Jeśli wybrano jedną z dwóch poprzednich opcji: Kliknij w polu wprowadzania **Promień zaokrąglenia**.
7.  Naciśnij **Enter**.



## Opcje

-   Naciśnij przycisk **Esc** lub przycisk **Zamknij** aby przerwać wykonywanie polecenia.



## Uwagi

-   Zaokrąglenie nie może być edytowane, ani nie jest powiązane z liniami, które zostały użyte do jego utworzenia.
-   W tej chwili obsługiwane są tylko linie, czyli [polilinie](Draft_Wire/pl.md) z tylko dwoma punktami.
-   [Polilinia](Draft_Wire/pl.md), która ma co najmniej trzy punkty, może zostać zaokrąglona lub sfazowana poprzez zmianę odpowiednio właściwości **Promień** lub **Rozmiar sfazowania**. Ponieważ [linia](Draft_Line/pl.md) i [polilinia](Draft_Wire/pl.md) mogą być łączone za pomocą komendy [polilinia](Draft_Wire/pl.md), komendy [Połącz](Draft_Join/pl.md) lub komendy [Ulepsz kształt](Draft_Upgrade/pl.md), zapewnia to alternatywną metodę tworzenia zaokrągleń i fazowań.



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
fillet = make_fillet([line1, line2], radius=100, chamfer=False, delete=False)
```

-   Tworzy obiekt `Fillet` pomiędzy liniami `line1` i `line2`, używając `radius` dla krzywizny.
-   Jeśli `chamfer` ma wartość `True`, utworzy prostą krawędź o długości `radius`, zamiast zaokrąglonej krawędzi.
-   Jeśli `delete` jest `True`, usunie podane `line1` i `line2` i pozostawi tylko nowy obiekt.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

line1 = Draft.make_line(p1, p2)
line2 = Draft.make_line(p2, p3)

doc.recompute()

fillet = Draft.make_fillet([line1, line2], radius=500)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Fillet/pl
