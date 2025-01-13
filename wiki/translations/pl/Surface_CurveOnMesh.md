---
 GuiCommand:
   Name: Surface CurveOnMesh
   Name/pl: Powierzchnia 3D: Krzywa na siatce
   MenuLocation: Surface , Curve on mesh
   Workbenches: Surface_Workbench/pl|
   Version: 0.17
---

# Surface CurveOnMesh/pl



## Opis

Polecenie **[<img src=images/Surface_CurveOnMesh.svg style="width:16px"> '''Krzywa na siatce'''** tworzy przybliżone segmenty linii krzywej na wybranej [siatce](Mesh_Workbench/pl.md).

Jeśli obiekt nie jest [siatką](Mesh/pl.md), ale parametrycznym [kształtem](Shape/pl.md) lub powierzchnią, musi zostać najpierw przekonwertowany na siatkę przy użyciu **[<img src=images/Mesh_FromPartShape.svg style="width:16px"> [Siatka z kształtu środowiska Część](Mesh_FromPartShape/pl.md)**.

Te krawędzie utworzone na wierzchu siatki mogą być dalej używane do ponownego tworzenia powierzchni w sposób parametryczny za pomocą narzędzi takich jak **[<img src=images/Surface_GeomFillSurface.svg style="width:16px"> [Wypełnianie krzywych granicznych](Surface_GeomFillSurface/pl.md)** oraz **[<img src=images/Surface_Sections.svg style="width:16px"> [Przekrój powierzchni](Surface_Sections/pl.md)**.

![](images/Surface_CurveOnMesh_mesh_example.png ) ![](images/Surface_CurveOnMesh_example.png )

![](images/Surface_CurveOnMesh_surface_example.png )



*Powyżej po lewej: obiekt siatki z wybranymi punktami na powierzchni. Powyżej po prawej: linie utworzone przez wybranie kilku punktów na siatce. Na dole po lewej: parametryczna powierzchnia zrekonstruowana z przybliżeń odcinków przy użyciu narzędzia [Przekrój powierzchni](Surface_Sections/pl.md).*



## Użycie

1.  Upewnij się, że masz [obiekt siatki](Mesh.md). Można go utworzyć za pomocą środowiska pracy <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Siatka](Mesh_Workbench/pl.md) lub importując plik siatki typu STL, [OBJ](Arch_OBJ/pl.md) lub [DAE](Arch_DAE/pl.md). Jeśli używany jest obiekt bryłowy lub typ pliku bryłowego *(STEP)*, można go przekonwertować na siatkę za pomocą narzędzia **[<img src=images/Mesh_FromPartShape.svg style="width:16px"> [Siatka z kształtu środowiska Część](Mesh_FromPartShape/pl.md)**.
2.  Naciśnij **[<img src=images/Surface_CurveOnMesh.svg style="width:16px"> Krzywa na siatce**.
3.  Naciśnij **Start**.
4.  Używając wskaźnika myszy, wybierz punkty na powierzchni siatki w oknie [widoku 3D](3D_view/pl.md). Wybierz tyle punktów, ile potrzeba do narysowania gładkiej linii podglądu.
5.  Po dodaniu wystarczającej liczby punktów, kliknij prawym przyciskiem myszy w oknie [widoku 3D](3D_view/pl.md), aby otworzyć menu kontekstowe i wybierz **Utwórz**. W zależności od tego, jak gładka jest oryginalna siatka, w oknie [widoku drzewa](Tree_view/pl.md) zostanie utworzony jeden lub wiele odcinków linii.
6.  Powtórz sekwencję **Start** → Wskaż → **Utwórz**, aby dodać więcej aproksymowanych odcinków krzywych.
7.  Nowy odcinek zostanie utworzony i pojawi się w [widoku drzewa](Tree_view/pl.md), natychmiast po wybraniu **Utwórz**. [Panel zadań](Task_panel/pl.md) pozostanie aktywny.
8.  Naciśnij **Zamknij**, aby zamknąć [panel zadań](Task_panel/pl.md) i całkowicie zakończyć polecenie.

Po naciśnięciu **Start**, menu kontekstowe *(prawy przycisk myszy)* w oknie [widoku 3D](3D_view/pl.md) pokazuje różne opcje obok opcji **Utwórz**.

-    **Zamknij polilinię**: jeśli wybrano co najmniej trzy punkty, opcja ta będzie dostępna, aby połączyć ostatni punkt z pierwszym za pomocą linii.

-    **Wyczyść**: usunie wstępnie wybrane punkty siatki i pozwoli na wybranie nowych.

-    **Anuluj**: usunie zaznaczone punkty i zatrzyma operację zaznaczania. Naciśnij **Start** ponownie, aby ponownie wybrać punkty.



## Opcje


**(Ta informacja musi zostać potwierdzona).**

Sekcja **Polilinia**:

-    **Tolerancja przyciągania do wierzchołków**: wartość domyślna to {{Value|10 px}}. Wskazuje minimalną odległość między jednym punktem a drugim podczas wybierania za pomocą kursora.

-    **Próg rozdzielenia**: wartość domyślna to {{Value|45°}}; wskazuje odchylenie kątowe od jednego punktu siatki do innego punktu niezbędne do utworzenia nowego odcinka krzywej zamiast przedłużania poprzedniego odcinka.


**Aproksymacja krzywych**

, jeśli opcja jest zaznaczona {{CheckBox|TRUE| }}, zostaną utworzone obiekty odcinków krzywej, w przeciwnym razie zostaną utworzone obiekty prostych linii *(polilinii)*.

-    **Tolerancja siatki**: wartość domyślna to {{Value|0.2}}. Jest to parametr, który bierze pod uwagę niedoskonałości siatki; im mniejsza liczba, tym siatka będzie uważana za bardziej precyzyjną, szczególnie jeśli jest to bardzo drobna siatka.

-    **Ciągłość**: wartość domyślna to {{Value|C2}}. Określa ciągłość splajnu. Może to być {{Value|C0}} *(dotykający)*, {{Value|C1}} *(styczna)*, {{Value|C2}} *(krzywizna)* i {{Value|C3}} *(krzywizna przyspieszenia)*.

-    **Maksymalny stopień zakrzywienia**: wartość domyślna to {{Value|5}}. Określa maksymalny stopień splajnu do aproksymacji powierzchni. Może przyjmować wartość od {{Value|1}} do {{Value|8}}.



## Właściwości

Jeśli pole {{CheckBox|FALSE|Przybliżenie splajnu}} nie jest zaznaczone, narzędzie **Krzywa na siatce** tworzy podstawową [cechę](Part_Feature/pl.md) środowiska Część.

Jeśli pole {{CheckBox|TRUE|Przybliżenie splajnu}} jest zaznaczone, narzędzie **Krzywa na siatce** tworzy **[<img src=images/Part_Spline.svg style="width:16px"> '''Part Spline'''** *(klasa`Part::Spline`)*, który jest pochodną podstawowej [cechy](Part_Feature/pl.md) środowiska Część *(klasa`Part::Feature`)*, dlatego dzieli wszystkie właściwości tej ostatniej.

Oprócz właściwości opisanych na stronie [Cecha części](Part_Feature/pl.md), krzywa pochodząca ze środowiska Projekt części posiada następujące właściwości w [edytorze właściwości](Property_editor/pl.md).



### Widok


{{TitleProperty|Podstawa}}

-    **Punkty kontrolne|Bool**: wartość domyślna to {{FALSE/pl}}, Jeśli ustawiono {{TRUE/pl}}, wyświetlona zostanie nakładka z punktami kontrolnymi krzywej.





{{Surface Tools navi

}}



---
⏵ [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface CurveOnMesh/pl
