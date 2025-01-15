---
 GuiCommand:
   Name: Arch BuildingPart
   MenuLocation: Architektura , Część budynku, 3D/BIM , Poziom
   Workbenches: Arch_Workbench/pl
   Version: 0.18
   SeeAlso: Arch_Building/pl, Arch_Site/pl
---

# Arch BuildingPart/pl



## Opis

Narzędzie Część budynku zastępuje stare narzędzia [Podłoga](Arch_Floor/pl.md) i [Budynek](Arch_Building/pl.md) nową, bardziej wszechstronną wersją, która może być używana nie tylko do tworzenia Pięter / Poziomów, ale także wszelkiego rodzaju sytuacji, w których różne obiekty Arch / BIM muszą być pogrupowane, a ta grupa może wymagać traktowania jako jednego obiektu lub replikacji.



## Użycie

1.  Opcjonalnie, wybierz jeden lub więcej obiektów, które mają być zawarte w nowej części budynku.
2.  Naciśnij przycisk **<img src="images/Arch_BuildingPart.svg" width=16px> '''Część budowli'''**.



### Uwagi

Obiekty \\Część budynku\\ posiadają wbudowaną, domyślną [płaszczyznę przekroju](Arch_SectionPlane/pl.md).

Płaszczyzna ta jest zawsze równoległa do płaszczyzny bazowej obiektu Część budynku, ale można określić przesunięcie między nimi. Tak więc wszystkie narzędzia, które działają z płaszczyzną przekroju, takie jak [Widok 2D kształtu](Draft_Shape2DView/pl.md) i [Wstaw obiekt środowiska Architektura](TechDraw_ArchView/pl.md) również działają z obiektem Część budynku.



## Opcje

-   Po utworzeniu obiektu Część budynku można dodać do niego więcej obiektów, przeciągając je i upuszczając w widoku drzewa lub korzystając z narzędzia **<img src="images/Arch_Add.svg" width=16px> [Połącz obiekty](Arch_Add/pl.md)**.
-   Można usuwać obiekty z Części budynku, przeciągając je i upuszczając poza obiekt Widoku drzewa lub korzystając z narzędzia **<img src="images/Arch_Remove.svg" width=16px> [Usuń komponent](Arch_Remove/pl.md)**.
-   Podwójne kliknięcie na obiekcie Część budynku w widoku drzewa ustawia płaszczyznę roboczą w jego lokalizacji, a obiekt Część budynku staje się aktywny, co oznacza, że nowe obiekty zostaną do niego automatycznie dodane. Kolejne podwójne kliknięcie na Części budynku ponownie go dezaktywuje i przywróci płaszczyznę roboczą do poprzedniej pozycji *(aby ta opcja była dostępna, należy ją ustawić w panelu Właściwości Widoku - Interakcja - Podwójne Kliknięcie Aktywuje)*.
-   Część budynku może wyświetlać znacznik w widoku 3D z etykietą i wskazaniem poziomu.
-   Gdy Część budynku jest przesuwana / obracana, wszystkie jej obiekty podrzędne, które nie mają właściwości **Ruch z obiektem nadrzędnym** lub mają ją włączoną, zostaną przesunięte / obrócone razem.
-   Części Budynku mogą być [Klonowane](Draft_Clone/pl.md).
-   Części Budynku mogą przyjmować dowolny typ IFC. Jego właściwość **Typ IFC** określa jego zastosowanie. Jeśli ustawisz go na **Poziom Budynku**, będzie działać jak poziom. Jeśli ustawisz go na **Budynek**, zachowuje się jak budynek, a jeśli ustawisz go na **Element złożenia**, zachowuje się jak zmontowane elementy. Jego ikona zmieni się, aby odzwierciedlić to ustawienie, ale poza tym nie ma to żadnego innego wpływu w programie FreeCAD. Jednak eksport do IFC jako jeden z tych typów może mieć wpływ na inne aplikacje BIM.
-   Części budynku pozwalają zdefiniować **Automatyczną grupę przechwytywania**. Następne obiekty Rysunku Roboczego i Architektury, lub cokolwiek innego, co korzysta z Draft.autogroup(), zostaną automatycznie dodane do tej Części budynku, jeśli znajdują się w całości w polu przechwytywania. {{Version/pl|0.20}}



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Część budowli** wywodzi się z obiektu [App: Cechy geometrii](App_GeoFeature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Podstawa}}

-    **Grupa|LinkList**: Lista obiektów, do których istnieją odniesienia.

-    **_ Group Touched|Bool|Ukryte**.


{{TitleProperty|Część Budynku}}

-    **Powierzchnia|Area**: Obliczona powierzchnia podłogi tej kondygnacji.

-    **Wysokość|Length**: Wysokość tego obiektu i jego obiektów podrzędnych. Obiekty podrzędne mogą być na przykład [ścianami](Arch_Wall/pl.md). Wysokość każdej ściany musi być ustawiona na `0`, aby właściwość wysokości Części Budynku przenosiła się do obiektów wewnątrz niej.

-    **Przesunięcie Poziomu|Length**: Punkt (0,0,0) tego poziomu. Wartość ta jest dodawana do atrybutu `Placement.Base.z` obiektu Część budynku, aby wskazać pionowe przesunięcie bez faktycznego przesuwania obiektu. Wynikowe przesunięcie jest wyświetlane, jeśli **Show Level** ma wartość {{TRUE/pl}}.

-    **Tabela Materiałów|Map|Ukryte**: Mapa MaterialName:SolidIndexesList, która określa powiązanie nazw materiałów z indeksami brył do użycia podczas odwoływania się do tego obiektu z innych plików.

-    **Tylko Bryły|Bool**: Jeśli ustawiono {{TRUE/pl}}, tylko bryły będą pobierane przez ten obiekt, gdy będą przywoływane z innych plików.

-    **Zapisany twórca|FileIncluded|Hidden**: Ten atrybut przechowuje reprezentację twórcy dla tego obiektu.

-    **Kształt|PartShape|Hidden**: Kształt tego obiektu.


{{TitleProperty|Obiekt podrzędny}}

-    **Propagacja wysokości|Bool**: Jeśli wartość ta przyjmie {{true/pl}}, wartość wysokości będzie przekazywana do zawartych obiektów. Zobacz właściwość **Height** dla dodatkowych warunków, które mają zastosowanie.


{{TitleProperty|IFC}}

-    **Dane IFC|Map|Hidden**: dane zgodne ze standardem IFC.

-    **Własciwości IFC|Map|Hidden**: Właściwości IFC tego obiektu.

-    **Typ IFC|Enumeration**: Typ IFC dla tego obiektu.


{{TitleProperty|Atrybuty IFC}}

-    **Opis|String**: Opcjonalny opis dla tego komponentu

-    **Globalny Id|String**.

-    **Typ obiektu|String**.

-    **Wysokość całkowita|Length**
    

-    **Szerokość całkowita|Length**
    

-    **Typ podziału|Enumeration**
    

-    **Zdefiniowany typ|Enumeration**
    

-    **Tag|String**: Opcjonalny znacznik dla tego komponentu.

-    **Typ podziału użytkownika|String**.



### Widok


{{TitleProperty|Grupa automatycznie}}

-    **Autogroup Autosize|Bool**: Automatycznie ustawia rozmiar pola przechwytywania na podstawie zawartości części budynku. {{Version/pl|0.20}}.

-    **Autogroup Box|Bool**: Włącza/wyłącza automatyczne grupowanie (i wyświetlanie pola przechwytywania). <small>(v0.20)</small> 

-    **Autogroup Margin|Length**: Margines używany, gdy włączony jest automatyczny rozmiar. <small>(v0.20)</small> 

-    **Autogroup Size|IntegerList**: Pole przechwytywania dla nowo utworzonych obiektów wyrażone jako \[XMin,YMin,ZMin,XMax,YMax,ZMax\]. {{Version/pl|0.20}}.


{{TitleProperty|Część Budynku}}

-    **Nazwa Czcionki|Font**: Czcionka do użytku w tekstach.

-    **Rozmiar Czcionki|Font Size|Length**: Rozmiar czcionki dla tekstów.

-    **Grubość Linii|Line Width|Float**: Grubość linii dla tego obiektu.

-    **Przesunięcie Początku|Origin Offset|Bool**: Jeśli wartość to {{true/pl}}, aktywując, przesunięcie wyświetlania będzie również miało wpływ na znacznik początku.

-    **Nadpisz Jednostkę|String**: Opcjonalna jednostka do wyrażenia poziomów.

-    **Pokaż Etykietę|Bool**: Jeśli wartość to {{true/pl}}, po aktywowaniu wyświetlana jest etykieta obiektu.

-    **Pokaż Poziom|Bool**: Jeśli wartość to {{true/pl}}, pokazuj poziom.

-    **Pokaż Jednostkę|Bool**: Jeśli wartość to {{true/pl}}, pokazuj jednostkę na znaczniku poziomu.


{{TitleProperty|Obiekt podrzędny}}

-    **Kolor Linii obiektów podrzędnych|Kolor**: Kolor linii do zastosowania dla obiektów podrzędnych tego elementu budynku.

-    **Grubość Linii obiektów podrzędnych|Float**: Grubość linii do zastosowania dla obiektów podrzędnych tego elementu budynku.

-    **Nadpisanie obiektów podrzędnych|Bool**: Jeśli watrość to {{True/pl}}, obiekty zawarte w tym elemencie budynku będą stosować te ustawienia linii, koloru i przezroczystości.

-    **Kolor Kształtu obiektów podrzędnych|Kolor**: Kolor kształtu do zastosowania dla obiektów podrzędnych tego elementu budynku.

-    **Przezroczystość obiektów podrzędnych|Procent**: Przezroczystość do zastosowania dla obiektów podrzędnych tego elementu budynku.


{{TitleProperty|Wycinek}}

-    **Automatyczne Wycinanie Widoku|Bool**: Włącz wycinanie widoku podczas aktywacji tego poziomu.

-    **Margines Wycinania|Długość**: Odległość między płaszczyzną poziomu a linią wycinania.

-    **Wycinanie Widoku|Bool**: Wytnij widok powyżej tego poziomu.


{{TitleProperty|Interakcje}}

-    **Automatyczna Płaszczyzna Robocza|Bool**: Jeśli ustawiono wartość {{True/pl}}, płaszczyzna robocza będzie utrzymana w trybie Automatycznym.

-    **Aktywacja Podwójnego Kliknięcia|Bool**: Jeśli ustawiono wartość {{True/pl}}, podwójne kliknięcie tego obiektu w drzewie aktywuje go.

-    **Przywróć Widok|Bool**: Jeśli ustawiono wartość {{True/pl}}, widok przechowywany w tym obiekcie zostanie przywrócony po podwójnym kliknięciu.

-    **Zapisz Inventor|Bool**: Jeśli opcja jest włączona, reprezentacja inventor tego obiektu zostanie zapisana w pliku FreeCAD, co pozwoli na odwołanie się do niej w innych plikach w trybie lekkim.

-    **Zapisany Inventor|FileIncluded|Ukryte**: Slot do zapisywania reprezentacji inventor tego obiektu, jeśli jest włączony.

-    **Ustaw Płaszczyznę Roboczą|Bool**: Jeśli ustawiono wartość {{True/pl}}, po aktywowaniu płaszczyzna robocza automatycznie dostosuje się do tej Części budynku.

-    **Dane Widoku|FloatList|Ukryte**: Dane pozycji kamery skojarzone z tym obiektem.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Część budynku** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
BuildingPart = makeBuildingPart(objectslist=None)
```

-   Tworzy obiekt `BuildingPart` z `objectslist`, który jest listą obiektów.

Przykład: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch BuildingPart/pl
