---
 GuiCommand:
   Name: Arch CurtainWall
   Name/pl: Architektura: Ściana kurtynowa
   MenuLocation: 3D/BIM , Ściana kurtynowa
   Workbenches: BIM_Workbench/pl
   Shortcut: **C** **W**
   Version: 0.19
   SeeAlso: 
---

# Arch CurtainWall/pl



## Opis

Narzędzie **Ściana kurtynowa** tworzy [ścianę kurtynową](https://pl.wikipedia.org/wiki/%C5%9Aciana_os%C5%82onowa), dzieląc powierzchnię bazową na czworokątne powierzchnie, a następnie tworząc pionowe słupy na pionowych krawędziach, poziome rygle na poziomych krawędziach i wypełniając przestrzenie między słupami panelami.

<img alt="" src=images/Arch_CurtainWall_example.png  style="width:780px;">

Ściany kurtynowe mogą być tworzone z dowolnego istniejącego obiektu, w takim przypadku wszystkie powierzchnie obiektu zostaną podzielone. Działa to najlepiej, gdy używany jest obiekt posiadający tylko jedną powierzchnię. Zazwyczaj najpierw należy utworzyć powierzchnię, najlepiej ograniczoną dokładnie 4 krawędziami, która reprezentuje obszar, który chcesz wypełnić ścianą kurtynową, a następnie zastosować narzędzie.

Ściany kurtynowe można również budować z obiektów liniowych, takich jak linia, łuk lub polilinia, podobnie jak w przypadku zwykłego narzędzia [ściana](Arch_Wall/pl.md).

Powierzchnie o podwójnej krzywiźnie lub powierzchnie o więcej niż 4 krawędziach również będą akceptowane, ale wynik będzie mniej przewidywalny.

Powierzchnie zostaną podzielone na czworokątne fragmenty. Jeśli 4 punkty fragmentu są współpłaszczyznowe, tworzony jest fragment w kształcie kwadratu. Jeśli nie, zostaje on podzielony na dwa trójkąty, i dodany zostanie ukośny słupek.

W przypadku, gdy potrzebny jest nieregularny podział, możliwe jest również zbudowanie własnego podzielonego obiektu, na przykład przy użyciu narzędzia [Siatka](Arch_Grid/pl.md), i ustawienie pionowych i poziomych podziałów ściany kurtynowej na 1.

Możesz także użyć narzędzia ściany kurtynowej bez zaznaczonego obiektu, w którym to przypadku będziesz mógł narysować linię bazową, która następnie zostanie wyciągnięta w pionie, aby utworzyć powierzchnię, na której zostanie zbudowana ściana kurtynowa.



## Użycie



### Kreślenie ścian kurtynowych od podstaw 

1.  Upewnij się, że nic nie jest zaznaczone
2.  Jest kilka sposobów na wywołanie tego polecenia:
    -   Wciśnij przycisk **<img src="images/Arch_CurtainWall.svg" width=16px> '''Ściana kurtynowa'''**.
    -   Wybierz opcję **3D/BIM → <img src="images/Arch_CurtainWall.svg" width=16px> Ściana kurtynowa** z menu.
    -   Użyj skrótu klawiszowego **C**, a następnie **W**.
3.  Kliknij pierwszy punkt w widoku 3D lub wpisz współrzędne.
4.  Kliknij drugi punkt w widoku 3D lub wpisz współrzędne.
5.  Dostosuj wymagane właściwości.



### Tworzenie ściany kurtynowej z wybranego obiektu 

1.  Wybierz jeden lub więcej obiektów bazowych geometrii *(obiekt rysunku roboczego, szkicu itp.)*.
2.  Wywołaj narzędzie jak opisano powyżej.
3.  Dostosuj potrzebne właściwości.



## Opcje

-   Ściany kurtynowe dzielą wspólne właściwości i zachowania wszystkich [Komponentów Architektonicznych](Arch_Component/pl.md).
-   Podpory kurtynowe mogą być wykonane z automatycznego profilu kwadratowego *(ustaw ich właściwość **Rozmiar Słupka**)* lub z profilu niestandardowego *(ustaw ich właściwość **Profil Słupka**)*. Słupki można umieścić na środku każdej krawędzi lub względem punktu (0,0,0) przez wyłączenie właściwości **Wyśrodkowany Profil**. Na przykład, jeśli chcesz, aby profil był umieszczony nieco za panelami, narysuj ten profil nieco poniżej punktu pochodzenia (0,0,0).
-   Ściany kurtynowe obsługują [materiał złożony](Arch_MultiMaterial/pl.md). Wewnątrz materiału złożonego warstwa **Rama** będzie używana do słupów, a warstwa **Panel szklany** do paneli, lub **Panel stały** jeśli nie istnieje warstwa Panel szklany w materiale złożonym.
-   Ściany kurtynowe mogą być oparte na obiekcie liniowym, takim jak linia, łuk lub polilinia. W tym przypadku wewnętrznie zostanie zbudowana powierzchnia podstawowa poprzez wytłaczanie obiektu liniowego w kierunku określonym przez właściwość **Kierunek Pionowy**, o długość określoną przez właściwość **Wysokość**.



## Właściwości

Obiekty ścian osłonowych dziedziczą właściwości obiektów [Komponent](Arch_Component/pl.md), a także posiadają następujące dodatkowe właściwości:

-    **Ilość Słupków Pionowych**: Liczba pionowych słupków.

-    **Wyrównanie Słupków Pionowych**: Czy profil słupków pionowych ma być wyrównany ze ścianą czy nie.

-    **Sekcje Pionowe**: Liczba pionowych sekcji tej ściany kurtynowej.

-    **Wysokość Słupka Pionowego**: Wysokość słupków pionowych, jeśli nie jest używany żaden profil.

-    **Szerokość Słupka Pionowego**: Szerokość słupków pionowych, jeśli nie jest używany żaden profil.

-    **Profil Słupka Pionowego**: Profil dla pionowych słupków *(wyłącza wielkość pionowego słupka)*.

-    **Ilość Słupków Poziomych**: Liczba poziomych słupków.

-    **Wyrównanie Słupków Poziomych**: Czy profil poziomych słupków ma być wyrównany ze ścianą czy nie.

-    **Sekcje Poziome**: Liczba poziomych sekcji tej ściany kurtynowej.

-    **Wysokość Słupka Poziomego**: Wysokość profilu poziomych rygli, jeśli nie jest używany żaden profil.

-    **Szerokość Słupka Poziomego**: Szerokość profilu poziomych słupków, jeśli nie jest używany żaden profil.

-    **Profil Słupka Poziomego**: Profil dla poziomych słupków *(wyłącza wielkość poziomego słupka)*.

-    **Ilość Słupków Przekątnych**: Liczba przekątnych słupków.

-    **Wielkość Słupka Przekątnego**: Wielkość przekątnych słupków, jeśli jakiekolwiek, jeśli nie jest używany żaden profil.

-    **Profil Słupka Przekątnego**: Profil dla przekątnych słupków, jeśli jakiekolwiek *(wyłącza wielkość poziomego słupka)*.

-    **Nadpisywanie krawędzi**: *({{Version/pl|1.0}})* Wprowadzane są numery indeksowe krawędzi geometrii Bazowego obiektu ArchSketch / Szkic *(w trybie Edycji)*. Wybrane krawędzie są używane do tworzenia kształtu tej ściany kurtynowej architektury (zamiast domyślnego używania wszystkich krawędzi). Ignorowane, jeśli Bazowy szkic dostarczył wybrane krawędzie. AKTUALIZACJA przez ArchSketch: Narzędzie GUI \"Edytuj ścianę kurtynową\" jest dostępne w zewnętrznym <img alt="" src=images/SketchArch_Workbench.svg  style="width:16px;"> [dodatku SketchArch](https://github.com/paullee0/FreeCAD_SketchArch), aby umożliwić użytkownikom interaktywny wybór krawędzi. \"Toponaming-Tolerant\", jeśli ArchSketch jest używany jako baza 
*(i zainstalowany jest dodatek SketchArch)*. Ostrzeżenie: Nie jest \'Toponaming-Tolerant\', jeśli używany jest tylko Szkic. *(Zobacz wątek na forum - <https://forum.freecad.org/viewtopic.php?t=73018&start=40#p756554>)*

-    **Ilość Paneli**: Liczba paneli.

-    **Grubość Paneli**: Grubość paneli.

-    **Zamień Poziome z Pionowymi**: Zamienia poziome i pionowe linie.

-    **Ulepsz**: Wykonuje odejmowanie między komponentami, aby żaden nie pokrywał się.

-    **Wyśrodkuj Profile**: Wyśrodkowuje profil na krawędziach lub nie.

-    **Kierunek Pionowy**: Odniesienie kierunku pionowego do wykorzystania przez ten obiekt do wydedukowania kierunków pionowych / poziomych. Utrzymuj go blisko rzeczywistego kierunku pionowego ściany kurtynowej.

-    **Wysokość**: Wysokość tej ściany kurtynowej, jeśli jest oparta na obiekcie liniowym.

-    **Obiekt nadrzędny**: Obiekt nadrzędny tej ściany kurtynowej. Ściana kurtynowa pojawi się osadzona w obiekcie nadrzędnym w widoku drzewa *(żadne inne działanie nie zostanie wykonane)*.



## Wykonywanie ścianek szkieletowych 

Ściany osłonowe są wygodne w wykonaniu w połączeniu z narzędziem [ściana](Arch_Wall/pl.md) w celu stworzenia ścian szkieletowych *(ścian, w których wewnętrzna warstwa konstrukcyjna wykonana jest z ram, zwykle drewnianych lub metalowych, zamiast z jednorodnego materiału, takiego jak beton lub cegła)*.

<img alt="" src=images/Frame_wall_example.png  style="width:780px;">

Opisana poniżej procedura tworzy ścianę i ścianę kurtynową w oparciu o tę samą linię bazową, a następnie nadaje ścianie multi-materiał, który pozostawia pustą przestrzeń, w której umieszczana jest ściana kurtynowa:

1.  Stwórz zwykłą [ścianę](Arch_Wall/pl.md), klikając dwa punkty lub wybierając istniejący obiekt liniowy.
2.  Wybierz obiekt bazowy nowo utworzonej ściany.
3.  Naciśnij przycisk **<img src="images/Arch_CurtainWall.svg" width=16px> '''Ściana osłonowa'''**, lub użyj klawiszy **C** i **W** aby utworzyć ścianę osłonową bazującą na tej samej linii bazowej co ściana.
4.  Upewnij się, że zarówno ściana, jak i ściana kurtynowa mają taką samą **Wysokość**.
5.  Ustaw liczbę **sekcji poziomych** ściany kurtynowej na zero, jeśli chcesz mieć tylko ramy pionowe.
6.  Ustaw pożądaną **szerokość słupka poziomego** i **wysokość słupka poziomego** *(lub użyj profilu słupka)*.
7.  Przygotuj dwa *(lub więcej)* [materiały](Arch_SetMaterial/pl.md), jeden dla paneli, drugi dla pustki, w której będzie rama.
8.  Utwórz [materiał złozony](Arch_MultiMaterial/pl.md), używając jednej warstwy materiału panelowego, jednej warstwy materiału pustki z ujemną wartością szerokości *(co spowoduje, że nie będzie ona rysowana)* odpowiadającą wysokości słupka pionowego ściany kurtynowej, oraz kolejnej warstwy materiału panelowego.
9.  Przypisz materiał złozony do ściany.
10. Ustaw właściwość **Obiekt nadrzędny** ściany kurtynowej na ścianę, którą stworzyliśmy w pierwszym punkcie.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Ściana osłonowa** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
MyCurtainWall = makeCurtainWall(baseobj)
```

Przykład:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseface = FreeCAD.ActiveDocument.addObject('Part::Extrusion','Extrusion')
baseface.Base = baseline
baseface.DirMode = "Normal"
baseface.LengthFwd = 2000
curtainwall = Arch.makeCurtainWall(baseface)
curtainWall.VerticalSections = 6
FreeCAD.ActiveDocument.recompute()
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch CurtainWall/pl
