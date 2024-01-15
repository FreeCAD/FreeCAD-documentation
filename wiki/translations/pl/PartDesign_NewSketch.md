---
 GuiCommand:
   Name: PartDesign NewSketch
   Name/pl: Projekt Części: Utwór szkic
   MenuLocation: Szkic , Utwór szkic
   Workbenches: PartDesign_Workbench/pl
   Version: 0.17
   SeeAlso: Sketcher_NewSketch/pl
---

# PartDesign NewSketch/pl



## Opis

Narzędzie to tworzy nowy szkic, tworzy nową [Zawartość](PartDesign_Body/pl.md) ze szkicem, jeśli taka nie istnieje i następnie automatycznie otwiera środowisko pracy [Szkicownik](Sketcher_Workbench/pl.md).

Podczas tworzenia modeli przy użyciu środowiska [Projekt Części](PartDesign_Workbench/pl.md), narzędzie to powinno być preferowane w odniesieniu do narzędzia **[<img src=images/Sketcher_NewSketch.svg style="width:16px">  [Utwórz szkic](Sketcher_NewSketch/pl.md)** znajdującego się w środowisku [Szkicownik](Sketcher_Workbench/pl.md).



## Użycie

1.  Naciśnij przycisk **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Utwórz szkic](PartDesign_NewSketch/pl.md)** z paska narzędzi Projekt Części.
2.  W panelu Zadania zostanie wyświetlone okno dialogowe **Wybierz cechę**. Wybierz jedną z płaszczyzn na liście lub w oknie Widoku 3D, którą można zmienić dla lepszego zobrazowania.
3.  Naciśnij **OK**.
4.  Interfejs automatycznie przełączy się na środowisko pracy Szkicownik i szkic będzie można edytować. Po wyjściu ze szkicu interfejs jest przywracany do środowiska pracy Projekt Części, a widok 3D jest przywracany do ujęcia przed utworzeniem szkicu.
5.  Alternatywnie, przed utworzeniem szkicu można wybrać płaszczyznę lub ścianę na istniejącej aktywnej bryle, w którym to przypadku szkic jest tworzony natychmiast.



## Opcje

-   Aby zmienić dołączenie istniejącego szkicu, zmień jego właściwość **Tryb mapowania** *(zobacz akapit [Właściwości](#Właściwości.md))*.

-   Okno dialogowe *Wybierz cechę* definiuje cechy nowego szkicu.

:   

    :   <img alt="" src=images/PartDesign.CreateSketch.SelectFeatureDialog.jpeg  style="width:300px;">

    :   Okno dialogowe *Wybierz cechę*. Te ustawienia tworzą szkic na płaszczyźnie XY i umożliwiają odniesienia z innych elementów tej samej bryły.

Ustawienia okna dialogowego

-   Pole układu współrzędnych: określa orientację płaszczyzny szkicu.
-   Zezwalaj na używane cechy:

:   Zezwalaj na cechy zewnętrzne

-   Z innych zawartości tej samej bryły: można odwoływać się do dowolnych elementów używanych w obrębie tej samej bryły.
-   Z różnych części lub swobodnych cech:
-   Utwórz niezależną kopię: wszystkie inne elementy będą oddzielnymi kopiami, tj. nie zmienią się, gdy zmieni się oryginał.
-   Utwórz zależną kopię: elementy będą kopiami, ale zachowana zostanie zależność od oryginalnych elementów. Jest to w zasadzie użycie funkcji [Łącznik kształtu](PartDesign_ShapeBinder/pl.md).
-   Utwórz dowiązanie: połączone elementy nie będą kopiami, ale będą wskazywać na oryginalne elementy, np. szkic główny. Wszelkie zmiany są odzwierciedlane w tym szkicu

Aby odwołać się do dowolnych elementów w w obrębie środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md), użyj przycisków **<img src="images/Sketcher_External.svg" width=16px> [Utwórz zewnętrzną geometrię](Sketcher_External/pl.md)** i **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [Utwórz kalkę techniczną](Sketcher_CarbonCopy/pl.md)**. Generalnie zaleca się używanie innych szkiców jako źródła odniesień, a nie ścian lub krawędzi, ponieważ są one w mniejszym stopniu dotknięte problemem nazewnictwa topologicznego.



## Właściwości

-    **Tryb mapowania**: Tryb dołączenia szkicu do innego obiektu, zazwyczaj płaszczyzny lub ściany, ale mogą to być także inne typy obiektów. Kliknij raz w pole, aby wyświetlić przycisk **...** i naciśnij go, aby otworzyć okno dialogowe [Dołączenie](Part_EditAttachment/pl.md). Jeśli wartość jest ustawiona na *Wyłączone*, właściwość *Umiejscowienie* jest włączona.

-    **Umiejscowienie**: kontroluje orientację szkicu w przestrzeni 3D. Zobacz [Umiejscowienie](Std_Placement/pl.md). Opcja zostaje wyłączona, jeśli szkic jest dołączony poprzez właściwość **Tryb mapowania**.








{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign NewSketch/pl
