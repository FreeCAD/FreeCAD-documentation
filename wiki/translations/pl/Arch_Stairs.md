---
 GuiCommand:
   Name: Arch Stairs
   Name/pl: BIM: Schody
   MenuLocation: 3D / BIM , Schody
   Workbenches: BIM_Workbench/pl
   Shortcut: **S** **R**
   Version: 0.14
   SeeAlso: 
---

# Arch Stairs/pl



## Opis

Narzędzie **Schody** umożliwia automatyczne tworzenie kilku rodzajów schodów. Proste schody *(z centralnym podestem lub bez)* mogą być tworzone od podstaw. Bardziej złożone schody wymagają obiektów bazowych.

Zobacz wpis [Schody w Wikipedii](https://pl.wikipedia.org/wiki/Schody), aby zapoznać się z definicją różnych terminów używanych do opisania części schodów.

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:600px;"> 
*Dwa modele schodów, jeden z masywną konstrukcją i podestem, drugi z pojedynczą podłużnicą.*



## Opcje

-   Schody dzielą wspólne właściwości i zachowania wszystkich [komponentów](Arch_Component/pl.md).



## Użycie

1.  Opcjonalnie wybierz jeden lub więcej obiektów bazowych, na przykład [linie](Draft_Line/pl.md), [polilinie](Draft_Wire/pl.md) i [szkice](Sketch/pl.md):
    -   Polilinie lub szkice z dwoma lub więcej segmentami będą używane do tworzenia spoczników. Muszą one znajdować się na płaszczyźnie równoległej do globalnej płaszczyzny XY. Na przykład, wybierz linię w kształcie litery U na spocznik z półobrotem i linię w kształcie litery L na spocznik narożny.
    -   Linie i szkice z jedną krawędzią będą używane do tworzenia biegów.
    -   Jeśli wierzchołki wszystkich linii i polilinii mają prawidłowe współrzędne Z, utworzone schody wykorzystają te informacje. Szkic (na płaszczyźnie równoległej do XY) z pojedynczą krawędzią lub linia bez delta Z również zadziała do biegu, wtedy Wysokość jest używana do skonstruowania biegu.
    -   Obiekty bazowe muszą być wybrane w odpowiedniej kolejności, zaczynając od najniższego obiektu.
2.  Naciśnij przycisk **<img src="images/Arch_Stairs.svg" width=16px> '''Schody'''** lub naciśnij klawisze **S**, **R**.
3.  Dostosuj żądane właściwości. Niektóre części schodów, takie jak konstrukcja, mogą nie pojawić się od razu, jeśli któraś z właściwości to uniemożliwia, np. grubość konstrukcji równa {{Value|0}}.

<img alt="" src=images/Stairs_and_Landing_02.png  style="width:600px;">

<img alt="" src=images/Stairs_and_Landing_01.png  style="width:600px;">

<img alt="" src=images/Arch_Stairs_Complex_Example.png  style="width:600px;">



*Złożone schody oparte na wybranych liniach i poliliniach, jak pokazano po lewej stronie.<br>
Na czerwono zaznaczono polilinie używane na spoczniki w Z&equals;1500mm, Z&equals;3000mm oraz Z&equals;4500mm.<br>
Na czarno linie łączące je używane do utworzenia biegów.
*



## Właściwości



### Dane


{{TitleProperty|Segment i części}}

-    **Abs Top|Vector**: *(tylko do odczytu)* Absolutnie najwyższy poziom, na który prowadzą schody.

-    **Last segment|Link**: Ostatni segment *(bieg lub spocznik)* schodów łączących się z tym segmentem. Poziom początkowy schodów będzie poziomem końcowym tego ostatniego segmentu.

-    **Outline Left|VectorList**: Lewy kontur schodów (tylko do odczytu).

-    **Outline Left All|VectorList**: Lewy kontur wszystkich segmentów schodów (tylko do odczytu).

-    **Outline Right|VectorList**: Prawy kontur schodów (tylko do odczytu).

-    **Outline Right All|VectorList**: Prawy kontur wszystkich segmentów schodów (tylko do odczytu).

-    **Railing Height Left|Length**: Wysokość lewej poręczy schodów lub spocznika.

-    **Railing Height Right|Length**: Wysokość prawej poręczy schodów lub spocznika.

-    **Railing Left|LinkHidden**: Obiekt lewej poręczy. {{Version/pl|0.20}}: Zaktualizowano typ właściwości z {{Incode|String}} do {{Incode|LinkHidden}}.

-    **Railing Offset Left|Length**: Odsunięcie lewej poręczy od krawędzi schodów lub podestu.

-    **Railing Offset Right|Length**: Odsunięcie prawej poręczy od krawędzi schodów lub spocznika.

-    **Railing Right|LinkHidden**: Prawy obiekt poręczy. {{Version/pl|0.20}}: Zaktualizowano typ właściwości z {{Incode|String}} do {{Incode|LinkHidden}}.


{{TitleProperty|Schody}}

-    **Wyrównanie|Enumeration**: Wyrównanie schodów na linii bazowej. Używane tylko jeśli zdefiniowano linię bazową. Może być {{value|Lewa}}, {{value|Prawa}} lub {{value|Środek}}.

-    **Wysokość|Length**: Całkowita wysokość schodów. Używane tylko jeśli nie zdefiniowano linii bazowej lub jeśli linia bazowa jest pozioma. Ignorowane, jeśli wartość właściwości **Riser Height Enforce** jest niezerowa.

-    **Długość|Długość**: Całkowita długość schodów, jeśli nie zdefiniowano linii bazowej. Ignorowane, jeśli wartość właściwości **Tread Depth Enforce** jest niezerowa.

-    **Szerokość|Length**: Szerokość schodów.

-    **Szerokość spocznika|FloatList**: Jeśli **Liczba stopni** wynosi {{Value|1}}, obiekt schodów działa jak spocznik. W takim przypadku, gdy linia bazowa jest wielosegmentowa, szerokość pierwszego segmentu spocznika jest zgodna z właściwościa **Szerokość**, a szerokości kolejnych segmentów są zgodne z ustawioną tutaj listą.


{{TitleProperty|Stopnie}}

-    **współczynnik Blondel|Float**: *(tylko do odczytu)* Obliczony współczynnik Blondela. Współczynnik ten wskazuje wygodne schody i powinien wynosić od 62 do 64 cm lub od 24,5 do 25,5 cala.

-    **Głębokość spocznika|Length**: Głębokość spocznika, jeśli jest włączona w właściwości **Spoczniki**. Domyślnie równa właściwości **Szerokość** jeśli wartość wynosi {{Value|0}}.

-    **Noski|Length**: Rozmiar noska.

-    **Liczba stopni|Integer**: Liczba stopni (pionów). Musi wynosić co najmniej 2 dla pojedynczego biegu i co najmniej 4 dla schodów z centralnym spocznikiem.

-    **Wysokość stopnia|Length**: *(tylko do odczytu)* Wysokość stopni. Jeśli wartość właściwości **Wymuszona wysokość pionu** wynosi {{Value|0}}, jest ona obliczana *(**Wysokość** / **Ilość stopni**)*. W przeciwnym razie jest taka sama jak wartość właściwości **Wymuszona wysokość pionu**.

-    **Wymuszona wysokość pionu|Length**: Wymuszona wysokość pionów.

-    **Grubość pionu|Długość**: Grubość pionów.

-    **Głębokość stopnic|Length**: *(tylko do odczytu)* Głębokość stopnic. Jeśli wartość właściwości **Wymuszona głębokość stopnic** wynosi 0, jest ona obliczana (**Długość** / **Ilość stopni**). W przeciwnym razie jest taka sama jak **Wymuszona głębokość stopnicy**.

-    **Wymuszona głębokość stopnicy|Length**: Wymuszona głębokość stopnicy.

-    **Grubość stopnicy|Length**: Grubość stopnicy.


{{TitleProperty|Konstrukcja}}

-    **Dolne połączenie początku schodów|Enumeration**: Typ połączenia między dolną płytą podłogi a początkiem schodów. Może mieć wartość {{value|HorizontalCut}}, {{value|VerticalCut}} lub {{value|HorizontalVerticalCut}}.

-    **Górne połączenie końca schodów|Enumeration**: Typ połączenia między końcem schodów a górną płytą podłogową. Może być {{value|toFlightThickness}} lub {{value|toSlabThickness}}.

-    **Grubość płyty dolnej|Length**: Grubość dolnej płyty podłogowej.

-    **Bieg|Enumeration**: Kierunek biegu po spoczniku. Może być {{value|Straight}}, {{value|HalfTurnLeft}} lub {{value|HalfTurnRight}}.

-    **Spoczniki|Enumeration**: Rodzaj spocznika. Może być {{value|Brak}} lub {{value|Na środku}} *({{value|Na każdym narożniku}} jeszcze nie zaimplementowane)*.

-    **Zakładka podłużnic|Length**: Zakładka podłużnic nad dolną częścią stopni.

-    **Szerokość podłużnicy.|Length**: Szerokość podłużnicy.

-    **Konstrukcja|Enumeration**: Typ konstrukcji schodów. Może być {{value|Brak}}, {{value|Masywne}}, {{value|Jedna podłużnica}} lub {{value|Dwie podłużnice}}.

-    **Odsunięcie konstrukcji|Length**: Przesunięcie między krawędzią schodów a konstrukcją.

-    **Grubość konstrukcji|Length**: Grubość konstrukcji.

-    **Grubość płyty w górę|Length**: Grubość górnej płyty podłogowej.

-    **Uzwojenie|Enumeration**: Typ uzwojenia. Nie zaimplementowano.



## Ograniczenia

-   Obecnie dostępne są schody proste, z połową skrętu w lewo lub w prawo i półpiętra.
-   Zobacz [wpis na forum](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534) dla schodów okrągłych.
-   Zobacz ogłoszenie na forum [1](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564).



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Schody** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji: 
```python
Stairs = makeStairs(baseobj=None, length=None, width=None, height=None, steps=None, name="Stairs")
```

-   Tworzy obiekt `Stairs` z podanego `baseobj`.
-   Jeśli `baseobj` nie zostanie podany, użyje `length`, `width`, `height` i `steps`, aby zbudować solidny obiekt.

Przykład: 
```python
import Arch

Stairs = Arch.makeStairs(length=5000, width=1200, height=3000, steps=14)
```



---
⏵ [documentation index](../README.md) > Arch Stairs/pl
