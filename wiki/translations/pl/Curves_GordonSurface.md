---
 GuiCommand:
   Name: Curves GordonSurface
   Name/pl: Krzywe: Powierzchnia Gordona
   MenuLocation: Surfaces , Gordon surface
   Workbenches: Curves_Workbench/pl
---

# Curves GordonSurface/pl



## Opis

Polecenie <img alt="" src=images/Curves_GordonSurface.svg  style="width:24px;"> **Powierzchnia Gordona** tworzy powierzchnię, która pokrywa się siecią krzywych. Narzędzie to jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) o nazwie [Krzywe](Curves_Workbench/pl.md).

<img alt="" src=images/GordonSurf-1.png  style="width:800px;">



## Użycie

1.  Powierzchnia Gordon wymaga sieci linii lub krzywych, które tworzą sieć wsparcia dla powierzchni.
    -   Powierzchnia będzie \"napięta\" pomiędzy i nad tymi liniami.
2.  W powyższym przykładzie niebieskie linie (lub żebra) reprezentują kształt powierzchni w różnych punktach wzdłuż powierzchni.
    -   Można je traktować jako przekroje wzdłuż powierzchni. Lub, jak podpory, nad którymi powierzchnia będzie \"rozciągać się\".
3.  Żółte linie reprezentują zakres i kształt powierzchni pomiędzy przekrojami (\"żebrami\") zdefiniowanymi przez niebieskie linie.
4.  Te linie (niebieskie i żółte) mogą być tworzone na szkicach.
    -   Szkice zawierające niebieskie żebra zazwyczaj mają przesunięcie położenia.
        -   Każde \"żebro\" znajduje się w osobnym szkicu.
    -   Szkice zawierające linie zasięgu/kształtu (żółte) będą zazwyczaj odnosić się do geometrii zewnętrznej ze szkiców \"żeber\" w celu dokładnego pozycjonowania.
5.  Należy je utworzyć przed następnym krokiem.
6.  Przełącz się do środowiska pracy <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Krzywe](Curves_Workbench/pl.md) *(instalacja za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) jest konieczna, jeśli nie zainstalowano go wcześniej)*.
7.  Teraz wybierz wszystkie linie, które będą definiować powierzchnię.
8.  Kolejność wyboru definiuje kolejność zszywania lub rozciągania powierzchni.
9.  Użyj wielokrotnego wyboru, aby zaznaczyć wszystkie linie definiujące powierzchnię. *(Kliknij lewym przyciskiem myszy, przytrzymując klawisz Ctrl)*.
10. Wybierz żebra jako pierwsze, w kolejności. *(W powyższym przykładzie zaznacz niebieskie linie od lewej do prawej lub od prawej do lewej)*.
11. Kontynuuj przytrzymywanie klawisza Ctrl i zaznaczaj linie zasięgu. *(Żółte linie w powyższym przykładzie)*.
12. Aby wywołać polecenie, wykonaj jedną z następujących czynności:
    -   Naciśnij przycisk <img alt="" src=images/Curves_GordonSurface.svg  style="width:24px;">
    -   Użyj **Surfaces → Gordon surface**.



## Właściwości

-    **Umiejscowienie**: Może być używane do dostosowania położenia wynikowej powierzchni Gordon. Zobacz informacje na stronie: [Umiejscowienie](Placement/pl.md).

    -   Uwaga: Właściwości Umiejscowienie nie dostosowują położenia krzywych / linii użytych do utworzenia powierzchni, a jedynie samą powierzchnię.

-    **Etykieta**: Określona przez użytkownika etykieta (nazwa) powierzchni. *(Domyślnie: Gordon)*

-    **Wyjście**: Określa typ wyjścia. *(Domyślnie: Powierzchnia, opcje: Powierzchnia, Szkielet)*

-    **Gordon>Max Ctrl Pts**: *(Domyślnie: 80)*

-    **Gordon>Sources**: Wybrane przez użytkownika linie, które są używane do tworzenia powierzchni Gordona.

-    **Gordon>Tol3D**: Tolerancja 3D *(Domyślnie: 0.01)*

-    **Wireframe>Samples U**: Liczba próbek w kierunku U. *(Domyślnie: 16)*

    -   Ta wartość jest używana do określenia gęstości siatki, gdy właściwość Wyjście jest ustawiona na Szkielet.

-    **Wireframe>Samples V**: Liczba próbek w kierunku V. *(Domyślnie: 16)*

    -   Ta wartość jest używana do określenia gęstości siatki, gdy właściwość Wyjście jest ustawiona na Szkielet.
    -   Powierzchnia Gordona w trybie szkielet, U=16, V=16

[600px](Plik:GordonSurf-wireframe.png.md)



## Uwagi

-   krzywe każdej grupy *(żebra i szyny)* powinny stykać się ze wszystkimi krzywymi drugiej grupy.
    -   Innymi słowy, muszą one tworzyć siatkę lub wzór siatki, jak pokazano tutaj:

<img alt="" src=images/grid.png  style="width:200px;">

-   Ogólnie rzecz biorąc, normalna powierzchni wynikowej powierzchni Gordona będzie określona przez kierunek żeber.

W tym przykładzie, powierzchnia po lewej stronie, szyny zostały narysowane od +Y do -Y, a wynikowa normalna powierzchni wynosi +Z
Po prawej stronie żebra zostały narysowane od -Y do +Y, w wyniku czego normalna powierzchni wynosi -Z.

<img alt="" src=images/Normals_shown.png  style="width:600px;">

-   [Wyciągnięcie](Part_Extrude/pl.md) środowiska Część może być użyte do stworzenia bryły z powierzchni.

-   [Wyciągnięcie](PartDesign_Pad/pl.md) środowiska Projekt Części może również utworzyć bryłę z powierzchni. Przeciągnięcie powierzchni do bryły tworzy [cechę bazową](PartDesign_Body/pl#Cecha_podstawowa.md), która może być następnie wypełniona.

## Ograniczenia



## Tworzenie skryptów 





{{Curves Tools navi

}}



---
⏵ [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves GordonSurface/pl
