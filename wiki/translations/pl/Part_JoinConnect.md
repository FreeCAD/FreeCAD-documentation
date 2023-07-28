---
- GuiCommand:/pl
   Name:Part JoinConnect
   Name/pl:Część: Połącz obiekty
   MenuLocation:Część → Połącz → Połącz obiekty
   Workbenches:[Część](Part_Workbench/pl.md)
   Version:0.16
   SeeAlso:[Osadź obiekty](Part_JoinEmbed/pl.md), [Wycięcie dla obiektu](Part_JoinCutout/pl.md), [Operacja logiczna](Part_Boolean/pl.md), [Grubość](Part_Thickness/pl.md)
---

# Part JoinConnect/pl



## Opis

Narzędzie Połącz łączy wnętrza obiektów posiadających dwie ścianki *(np. rur)*. Może również łączyć powłoki i linie.

![600px](images/JoinFeatures_Connect.png)



## Użycie

1.  Wybierz obiekty do połączenia.

Kolejność wyboru nie ma znaczenia, ponieważ działanie narzędzia jest symetryczne. Wystarczy wybrać jeden z kształtów podrzędnych każdego obiektu *(np. ściany)*. Można również wybrać złożenie zawierające wszystkie kształty do połączenia, np. [Szyk ortogonalny](Draft_OrthoArray/pl.md).

1.  Polecenie **Połącz obiekty** można wywołać na kilka sposobów:
    -   Naciśnij przycisk <img alt="" src=images/Part_JoinConnect.svg  style="width:24px;"> **Połącz obiekty** na pasku narzędzi.
    -   Użyj polecenia **Część → Połącz → Połącz obiekty** w menu głównym.

Tworzony jest obiekt parametryczny Połączenie. Oryginalne obiekty są ukrywane, a wynik połączenia jest wyświetlany w oknie [widoku 3D](3D_view/pl.md).



## Właściwości


{{TitleProperty|Połączenie}}

-    **Obiekty**: Lista obiektów do połączenia. Ogólnie rzecz biorąc, potrzebne są co najmniej dwa obiekty, ale wystarczy również pojedyncze złożenie zawierające kształty do połączenia. *(od wersji FreeCAD v0.17.8053 właściwość ta nie jest wyświetlana w [Edytorze właściwości](Property_editor/pl.md) i można uzyskać do niej dostęp tylko za pośrednictwem skryptów [Python](#Tworzenie_skryptów.md))*.

-    **Ulepsz**: Określa, czy zastosować operację [ulepszania](Part_RefineShape/pl.md) wobec ostatecznego kształtu. Wartość domyślna jest określona przez pole wyboru \"Automatycznie udoskonal model po wykonaniu operacji logicznej\" w [Preferencjach środowiska Projekt Części](PartDesign_Preferences/pl.md).

-    **Tolerancja**: wartość \"rozmycia\". Jest to dodatkowa tolerancja stosowana podczas wyszukiwania przecięć, oprócz tolerancji przechowywanych w przetwarzanych kształtach wejściowych.



## Przykład

1.  Utwórz rurę, stosując narzędzie [grubość](Part_Thickness/pl.md) do bryły [cylindra](Part_Cylinder/pl.md):

![320px](images/JoinFeatures_Example_step1.png)

1.  Utwórz kolejną rurę o mniejszej średnicy i [umieść](Placement/pl.md) ją tak, aby przebiła ścianę pierwszej rury:

![320px](images/JoinFeatures_Example_step2.png)

1.  Zaznacz pierwszą i drugą rurę, a następnie kliknij polecenie **Połącz obiekty** na rozwijanym pasku narzędzi Połącz.

![320px](images/JoinFeatures_Example_step3_Connect.png)

1.  Zastosuj narzędzie przekroju *([Przełącz płaszczyznę tnącą](Std_ToggleClipPlane/pl.md), [Płaszczyzna przekroju](Arch_SectionPlane/pl.md) środowiska Architektura, [Płaszczyzna cięcia](Arch_CutPlane/pl.md) środowiska Architektura)*, aby odsłonić elementy wewnętrzne. Na poniższym obrazku użyto narzędzia Płaszczyzna przekroju środowiska Architektura.

![320px](images/JoinFeatures_Example_step4_Connect.png)



## Sposób działania 

Algorytmy stojące za narzędziami Połącz są dość proste, a ich zrozumienie jest ważne dla prawidłowego korzystania z narzędzi. Zauważmy, że algorytm narzędzia Połącz jest nieco bardziej złożony od innych, ale wystarczy myśleć o nim jako o symetrycznym wariancie algorytmu [osadzania](Part_JoinEmbed/pl#Sposób_działania.md).

1\. Każdy obiekt jest dzielony na części przez skrzyżowania z innymi obiektami. *(patrz [Fragmentacja funkcją logiczną](Part_BooleanFragments/pl.md))*.

2\. Z kawałków danego obiektu zachowuje się tylko największy, wszystkie pozostałe są usuwane.

3\. Elementy przecięcia, które dotykają co najmniej dwóch obiektów, są dodawane do wyniku. Następnie elementy są łączone, aby utworzyć wynik operacji połączenia.



### Uwagi

-   Jeśli w kroku 1 każdy obiekt pozostaje w jednym kawałku, wynik połączenia będzie równoważny działaniu funkcji [połączenia logicznego](Part_Fuse/pl.md) obiektów.
-   Teraz wszystkie dostarczone złożenia są rozbijane przed połączeniem. Oznacza to, że samoprzecinające się złożenia, które są nieprawidłowe dla wszystkich innych operacji logicznych, są prawidłowe dla funkcji Połącz *(Może to zostać zmienione w przyszłości)*.
-   \"Największy\" element to ten, który ma największą masę. Oznacza to, że dla brył porównywane są objętości; dla powłok i ścian porównywane są powierzchnie i tak dalej.
-   Od wersji FreeCAD v0.17.8053 i wersji OCC 6.9.0 lub wyższej, funkcja Połącz jest prawie tak szybka, jak wszystkie inne operacje logiczne. W starszych wersjach funkcja Połącz jest około 5 razy wolniejsza niż zwykła operacja logiczna i działa tylko na bryłach.



## Tworzenie skryptów 

Narzędzie **Połącz obiekty** może być używane w [makrodefinicjach](macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:

**BOPTools.JoinFeatures.makeConnect(name)**

-   Tworzy pustą funkcję Połącz. Właściwość \"Obiekty\" musi zostać przypisana jawnie, a następnie.
-   Zwraca nowo utworzony obiekt.

Funkcja Połącz może być również stosowana do zwykłych kształtów, bez konieczności posiadania obiektu dokumentu:

**Part.BOPTools.JoinAPI.connect(list_of_shapes, tolerance = 0.0)**

Może to być przydatne do tworzenia niestandardowych funkcji skryptowych Python.

Przykład:


{{code|code=
import Part
j = Part.BOPTools.JoinFeatures.makeConnect(name= 'Connect')
j.Objects = FreeCADGui.Selection.getSelection()
}}

Samo narzędzie jest zaimplementowane w środowisku Python, patrz **/Mod/Part/BOPTools/JoinFeatures.py** ([Link do Github](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/BOPTools/JoinFeatures.py)) w miejscu, w którym zainstalowany jest FreeCAD.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinConnect/pl
