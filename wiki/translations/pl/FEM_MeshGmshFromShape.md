---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM MeshGmshFromShape
   Name/pl: Siatka MES z kształtu przy pomocy generatora Gmsh
   MenuLocation: Siatka , Siatka MES z kształtu przy pomocy generatora Gmsh
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: Wszystkie
}}
---

# FEM MeshGmshFromShape/pl



## Opis

Geometria do analizy metodą elementów skończonych musi być poddana dyskretyzacji do [siatki MES](FEM_Mesh/pl.md). To narzędzie korzysta z programu [Gmsh](https://en.wikipedia.org/wiki/Gmsh) (który musi być zainstalowany w systemie) do generowania siatki.

W zależności od Twojego systemu operacyjnego i pakietu instalacyjnego, Gmsh może być dołączony do programu FreeCAD lub nie. Więcej informacji można znaleźć na stronie [Instalacja środowiska MES](FEM_Install/pl.md).



## Użycie

1.  Wybierz kształt, który chcesz analizować. Dla objętości musi to być bryła pojedyncza lub złożona. Bryła złożona jest konieczna jeśli część jest wykonana z wielu materiałów *(bryłę złożoną można utworzyć przy pomocy narzędzia [Fragmentacja funkcją logiczną](Part_BooleanFragments/pl.md))*.
2.  Aktywuj narzędzie na jeden z następujących sposobów:
    -   Press the **<img src="images/FEM_MeshGmshFromShape.svg" width=16px> '''FEM mesh from shape by Gmsh'''** button.
    -   Wybierz opcję **Siatka → <img src="images/FEM_MeshGmshFromShape.svg" width=16px> Siatka MES z kształtu przy pomocy generatora Gmsh** z menu.
3.  Opcjonalnie, edytuj minimalny i maksymalny rozmiar elementu *(domyślne ustawienie często tworzy zbyt rzadkie siatki)*. Możesz też zmienić przestrzeń elementów (ale domyślne ustawienie *From shape* zwykle wystarczy) i ich rząd.
4.  Wciśnij przycisk **Zastosuj** i poczekaj aż zakończy się generowanie siatki. {{Version/pl|1.0}}: Opcjonalnie, wciśnij przycisk **Anuluj** aby zatrzymać generowanie siatki.
5.  Wciśnij przycisk **OK** aby zamknąć okno dialogowe. Powinieneś widzieć nowy obiekt FEMMeshGmsh dodany do aktywnego kontenera analizy. Możesz też kliknąć **Anuluj** aby anulować zmiany bądź tworzenie obiektu siatki.

Po utworzeniu siatki można zmienić jej właściwości używając [edytora właściwości](Property_editor/pl.md). Po zmianie właściwości należy ponownie otworzyć okno dialogowe narzędzia i wcisnąć przycisk **Zastosuj** *(można zostawić okno dialogowe otwarte podczas zmieniania właściwości)*.

Przycisk **Wersja Gmsh** pozwala sprawdzić szczegóły dotyczące aktualnie używanego pliku wykonywalnego Gmsh.



## Właściwości

-    **Algorithm2D**: Algorytm do tworzenia siatek 2D. Dostępne algorytmy są opisane [na stronie projektu GMSH](https://gmsh.info/doc/texinfo/gmsh.html#Choosing-the-right-unstructured-algorithm). Dla Delaunay zobacz stronę [triangulacja Delone](https://pl.wikipedia.org/wiki/Triangulacja_Delone).

-    **Algorithm3D**: Algorytm do tworzenia siatek 3D. Dostępne algorytmy są opisane [na stronie projektu GMSH](https://gmsh.info/doc/texinfo/gmsh.html#Choosing-the-right-unstructured-algorithm).

-    **Characteristic Length Max**: Maksymalny rozmiar elementów. Jeśli ustawione jest *0.0* to rozmiar zostanie dobrany automatycznie. Ta właściwość może być również zmieniona w oknie dialogowym narzędzia w polu **Maksymalny rozmiar elementu**.

-    **Characteristic Length Min**: Minimalny rozmiar elementów. Jeśli ustawione jest {{Value|0.0}} to rozmiar zostanie dobrany automatycznie. Ta właściwość może być również zmieniona w oknie dialogowym narzędzia w polu **Minimalny rozmiar elementu**.

-    **Coherence Mesh**:

    -   
        {{true/pl}}
        
        *(domyślne)* zduplikowane węzły siatki zostaną usunięte

    -   
        {{false/pl}}
        

-    **Element Dimension**: Przestrzeń elementów siatki. Ta właściwość może być również zmieniona w oknie dialogowym narzędzia w polu **Wymiar elementu**.

    -   From Shape *(domyślne)* przestrzeń zostanie określona na podstawie przestrzeni obiektu, dla którego siatka jest generowana
    -   1D
    -   2D
    -   3D

-    **Element Order**: [Rząd elementów](https://www.comsol.de/support/knowledgebase/1270). Ta właściwość może być również zmieniona w oknie dialogowym narzędzia w polu **Kolejność elementów**. {{Version/pl|0.20}}

    -   1st
    -   2nd *(domyślne)***Uwaga:** Jeśli korzystasz z solvera [Elmer](FEM_SolverElmer/pl.md), możesz trafić na ten błąd: *ERROR:: GetEdgeBasis: Can\'t handle but linear elements, sorry.* To oznacza, że dane równanie *(typ analizy)* nie wspiera siatek drugiego rzędu. W takim wypadku użyj siatki pierwszego rzędu lub sprawdź stronę wiki danego równania żeby znaleźć ewentualne możliwości używania siatek drugiego rzędu.

-    **Geometrical Tolerance**: Tolerancja geometryczna dla dopasowania siatki do krawędzi obiektu. Domyślne ustawienie *0.0* oznacza, że Gmsh skorzysta z wartości 1e-8.

-    **Groups Of Nodes**: Wszystkie węzły a nie tylko elementy zostaną zapisane dla każdej fizycznej grupy siatki. Fizyczne grupy siatki to zbiory obiektów siatki *(punktów, krawędzi, powierzchni i objętości)*. Są one identyfikowane za pomocą przestrzeni i indywidualnego oznaczenia. Przykładowo, siatka tego samego obszaru obiektu jest wewnętrznie oznaczana tak samo. Więc wszystkie powierzchnie tego obszaru będą tworzyły jedną grupę fizyczną.

-    **High Order Optimize**: Czy i jak siatki z właściwością {{Version/pl|0.20}} Gmsh wspiera różne algorytmy optymalizacji. **Elastic** to algorytm, w którym elementy siatki są traktowane jako kolekcja deformowalnych ciał lepkosprężystych. Siatki pierwszego rzędu nie mogą być optymalizowane, ponieważ ich krawędzie są liniowe i nie można ich deformować.

-    **Mesh Size From Curvature**{{Version/pl|0.20}}: Liczba elementów siatki na $2\pi$ razy promień krzywizny. Aby uzyskać gęstszą siatkę dla małych wierzchołków lub otworów, należ zwiększyć tą wartość dla lepszych wyników.

<img alt="" src=images/FEM_Gmsh-MeshSizeFromCurvature.png  style="width:450px;"> 
*Efekt właściwości  ''Mesh Size From Curvature'''. Po lewej: ustawionej na 12. Po prawej: dezaktywowanej.
*

-    **Optimize Netgen**: Czy siatka będzie optymalizowana przy pomocy generatora siatki 3D [Netgen](https://github.com/NGSolve/netgen) aby poprawić jakość elementów czworościennych. **Uwaga:** ponieważ Netgen może tworzyć tylko elementy czworościenne, ta opcja jest ignorowana dla siatek, których właściwość **Element Dimension** nie jest ustawiona na *3D*.

-    **Recombination Algorithm**{{Version/pl|0.20}}: Algorytm używany przez **Recombine 3D All** i przez **Recombine All**. Więcej informacji można znaleźć w sekcji [Rekombinacja elementów](#Rekombinacja_elementów.md) a szczegóły technicznej znajdują się w [dokumentacji Gmsh](https://www.gmsh.info/doc/texinfo/gmsh.html#t11).

-    **Recombine 3D All**{{Version/pl|0.20}}: Stosuje algorytm rekombinacji 3D dla wszystkich objętości. Czworościany będą przekształcone w pięciościany, prostopadłościany lub piramidki gdzie będzie to możliwe.

-    **Recombine All**: Stosuje algorytm rekombinacji dla wszystkich powierzchni. Trójkąty będą przekształcone w czworokąty gdzie będzie to możliwe a recombination algorithm to all surfaces.

-    **Optimize Std**Optymalizuje siatkę aby zwiększyć jakość elementów czworościennych.

-    **Second Order Linear**: Czy węzły elementów drugiego rzędu *(jeśli wlaściwość **Element Order** jest ustawiona **2nd**)* i / lub punkty zagęszczania siatki są tworzone przez interpolację liniową.

    -   
        {{true/pl}}
        
        używana jest interpolacja liniowa.

    -   
        {{false/pl}}
        
        *(domyślne)* używana jest interpolacja krzywoliniowa.

-    **Algorytm podziału**. {{Version/pl|1.0}}: umożliwia tworzenie elementów czworościennych i sześciościennych przez podział.

    -   Brak: nie używa żadnego algorytmu podziału.
    -   Wszystkie czworokąty: tworzy elementy czworokątne poprzez podział.
    -   Wszystkie heksaedry: tworzy elementy heksaedralne poprzez podział.
    -   Barocentryczny: tworzy elementy trójkątne poprzez podział barycentryczny.



## Uwagi



### Ujemne jakobiany 

Jeśli pojawia się błąd o ujemnych jakobianach, można wypróbować następujące podejściaː

-   Ustawić właściwość **Second Order Linear** na {{true/pl}}, ale zostawić **Element Order** na *2nd*.
-   Ustawić **Element Order** na *1st*.
-   Zmniejszyć rozmiar elementów siatki poprzez redukcję **Characteristic Length Max**.
-   Jeśli używany jest solver ccxtools i przycisk uruchamiania *(nie panel zadań)* to węzły elementów z ujemnymi jakobianami będą zaznaczone na zielono.



### Wzrost siatki 

Na krawędziach i małych obiektach geometrycznych siatka musi być mniejsza niż w obszarach z dala od krawędzi. Więc rozmiar elementu rośnie w oddaleniu od krawędzi. Strategia wzrostu siatki w Gmsh to wzrost między krawędziami o różnych rozmiarach. Więc wzrost zawodzi jeśli obszar ma krawędzie o tych samych rozmiarach jak w poniższym przykładzieː

<img alt="" src=images/FEM_Gmsh-MeshGrowth-failing.png  style="width:400px;"> 
*Wzrost siatki zawodzi, ponieważ obszar cylindryczny jest otoczony takimi samymi krawędziami.*

Aby umożliwić rozsądny wzrost siatki, należy w takim przypadku dodać krawędź do tego obszaru. W tym przykładzie byłby to okrąg w środku walca. Okrąg jest dodany jako część bryły złożonej z [fragmentacji funkcją logiczną](Part_BooleanFragments/pl.md), zobacz [plik projektu](https://forum.freecadweb.org/download/file.php?id=146255) tego przykładu.

<img alt="" src=images/FEM_Gmsh-MeshGrowth-success.png  style="width:400px;"> 
*Rozsądny wzrost siatki dzięki dodatkowej krawędzi w środku cylindrycznego obszaru.*



### Rekombinacja elementów 

Elementy mogą być rekombinowane na dwa sposoby, na powierzchni obiektów tak, że trójkąty są przekształcane w czworoboki jeśli to możliwe i w objętości obiektów tak, że czworościany są przekształcane w pięciościany, prostopadłościany lub piramidki jeśli to możliwe. Oczywiste jest, iż wynik rekombinacji silnie zależy od geometrii obiektu i że rekombinacja obiektu 3D tylko na powierzchni zwykle prowadzi do niepożądanych rezultatów.

Zostało to przedstawione na rysunku poniżej. Siatka dla prostopadłościanu jest tworzona ze standardowymi ustawieniami *(czworościany drugiego rzędu)* To rysunek w lewym górnym rogu. Rysunek w prawym górnym rogu pokazuje wynik gdy dodatkowo elementy są rekombinowane tylko na powierzchni obiektu. Wynik jest zły, ponieważ zmienione elementy na powierzchni nie pasują do niezmienionych elementów w objętości. Więc sama właściwość Jeśli używana jest dodatkowo właściwość **Recombine 3D All**, wynik jest lepszy *(lewy dolny rysunek)*. Jednak wynik nie odbiega znacząco od siatki bez rekombinacji. Ponieważ obiekt jest prostopadłościanem, rozsądne jest użycie algorytmu rekombinacji, który próbuje też utworzyć prostopadłościany. Taki wynik jest pokazany na prawym dolnym rysunku.

Algorytm rekombinacji *Simple* zostawi pewną liczbę trójkątów w siatce jeśli rekombinacja prowadzi do złej jakości czworoboków. W takich przypadkach należy użyć algorytmu *full-quad*, który automatycznie tworzy rzadszą siatkę a następnie dokonuje rekombinacji, wygłaszania i podziału. Więcej informacji można znaleźć [w tym wątku na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=20351#p520392).

<img alt="" src=images/FEM_Gmsh-Recombination.png  style="width:600px;"> 
*Efekt rekombinacji elementów siatki.<br>
Górny lewy róg: standardowa siatka.<br>
Górny prawy róg: rekombinacja tylko na powierzchni przy pomocy algorytmu '''Simple'''.<br>
Dolny lewy róg: rekombinacja na powierzchni i w objętości przy pomocy algorytmu '''Simple'''.<br>
Dolny prawy róg: rekombinacja na powierzchni i w objętości przy pomocy algorytmu '''Simple full-quad'''*





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshGmshFromShape/pl
