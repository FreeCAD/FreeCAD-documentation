# <img alt="Ikonka FreeCAD dla środowiska pracy Upraszczanie" src=images/Defeaturing_workbench_icon.svg  style="width:64px;"> Defeaturing Workbench/pl



## Wprowadzenie


{{TOCright}}

<img alt="" src=images/Defeaturing_workbench_icon.svg  style="width:24px;"> Środowisko pracy **Upraszczanie** jest dodatkowym środowiskiem pracy przeznaczonym do edycji modeli STEP, usuwając wybrane cechy z modelu. Jest to [zewnętrzne środowiskiem pracy](External_workbenches/pl.md) i dlatego nie jest częścią standardowej instalacji FreeCAD.



## Funkcjonalność

-   Zawiera zestaw narzędzi do edycji kształtu lub modelu STEP, usuwania otworów, ścian, upraszczania modelu, zmiany tolerancji, stosowania rozmytych operacji logicznych itp.
-   Istnieją również narzędzia do utworzenia brył z krawędzi, ścian lub powłok.
-   Możliwe jest również użycie bezpośredniego modelowania modelu, gdy historia operacji jest niedostępna *(Dotyczy to modeli 3D STEP)*.
-   Przydatne w sytuacjach wymagających szybkiego usunięcia zastrzeżonych szczegółów modelu przed jego udostępnieniem. Zobacz również stronę [Usuwanie cech](Defeaturing/pl.md).

Uwaga: Bardziej zaawansowane narzędzia do upraszczania mogą być użyte, jeśli [OCC7.3](OpenCASCADE/pl.md) jest dostępne.



## Instalacja



### Automatyczna *(zalecane)* 

Używając <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Menedżera dodatków](Std_AddonMgr/pl.md) FreeCAD, dostępnego w {{VersionPlus/pl|0.17}} poprzez menu **Przybory → Menedżer dodatków**. Wyszukaj <img alt="" src=images/Defeaturing_workbench_icon.svg  style="width:24px;"> ikonkę środowiska pracy Upraszczanie. Menedżer dodatków powiadamia również użytkownika, gdy dostępna jest nowa wersja tego dodatku.



### Samodzielna

Zobacz również stronę [Jak zainstalować dodatkowe środowiska pracy](How_to_install_additional_workbenches/pl.md)



### Zgodność

-   FreeCAD v0.15 4671
-   FreeCAD v0.16 \>= 6712
-   FreeCAD v0.17 \>= 13522
-   FreeCAD v0.18+



## Bibliografia

-   Autor: GitHub: [\@easyw](https://github.com/easyw) \| FreeCAD forum: [1](https://forum.freecadweb.org/viewtopic.php?f=9&t=29506)
-   Kod źródłowy na GitHub: <https://github.com/easyw/Defeaturing_WB>
-   Wątek na forum FreeCAD: <https://forum.freecadweb.org/viewtopic.php?t=29506>



## Narzędzia

![Okno dialogowe Upraszczanie](images/Defeaturing_WB.png )

<img alt="" src=images/Defeaturing_Tools.svg  style="width:32px;"> Narzędzia do rozbrajania znajdują się na osobnym panelu.

-   <img alt="" src=images/DefeatWB_Tools_rmv_hole.png  style="width:32px;"> [Usuń otwory](DefeatWB_Tools_rmv_hole.md): usuń dziurę ze ściany.
-   <img alt="" src=images/DefeatWB_Tools_rmv_listed_Faces.png  style="width:32px;"> [Usuń ściany na liście](DefeatWB_Tools_rmv_listed_Faces.md): usuń ściany z listy elementów.
-   <img alt="" src=images/DefeatWB_Tools_add_Faces_listed_Edges.png  style="width:32px;"> [Dodaj ściany wymienione na liście krawędzi](DefeatWB_Tools_add_Faces_listed_Edges.md): dodawanie ścian z \"listy\" krawędzi.
-   <img alt="" src=images/DefeatWB_Tools_select_Faces_Param_Defeat.png  style="width:32px;"> [Wybierz ściany, które zostaną parametrycznie uproszczone](DefeatWB_Tools_select_Faces_Param_Defeat.md): wybierz ściany do parametrycznego usunięcia.
-   <img alt="" src=images/DefeatWB_Tools_create_copy_listed_edges.png  style="width:32px;"> [Utwórz kopę krawędzi z listy](DefeatWB_Tools_create_copy_listed_edges.md): utwórz kopię krawędzi wymienionej na liście elementów.

-   <img alt="" src=images/DefeatWB_Tools_copy_Faces_listed_faces.png  style="width:32px;"> [Kopiuj ścianę z listy ścian](DefeatWB_Tools_copy_Faces_listed_faces.md): kopiowanie ścian wymienionych na liście ścian.
-   <img alt="" src=images/DefeatWB_Tools_offset_ściana.png  style="width:32px;"> [Odsunięcie ściany](DefeatWB_Tools_offset_face.md): przesunięcie ściany.
-   <img alt="" src=images/DefeatWB_Tools_offset_edge.png  style="width:32px;"> [Odsunięcie krawędzi](DefeatWB_Tools_offset_edge.md): przesunięcie krawędzi.

-   <img alt="" src=images/DefeatWB_Tools_make_solid_listed_faces.png  style="width:32px;"> [Utwórz bryłę z listy ścian](DefeatWB_Tools_make_solid_listed_faces.md): tworzy bryłę z listy ścian.
-   <img alt="" src=images/DefeatWB_Tools_make_solid_faces_selected_objects.png  style="width:32px;"> [utwórz bryłę z ścian wybranych obiektów](DefeatWB_Tools_make_solid_faces_selected_objects.md): tworzy bryłę z ścian wybranych obiektów.
-   <img alt="" src=images/DefeatWB_Tools_select_one_object_2_make_solid_step_proc.png  style="width:32px;"> [Utwórz bryłę z listy ścian](DefeatWB_Tools_select_one_object_2_make_solid_step_proc.md): wybierz JEDEN obiekt, aby spróbować utworzyć bryłę poprzez proces importu / eksportu STEP.
-   <img alt="" src=images/DefeatWB_Tools_Connect.png  style="width:32px;"> [Połącz](DefeatWB_Tools_Connect.md): łączy obiekty
-   <img alt="" src=images/DefeatWB_Tools_clean_face_rmv_holes.png  style="width:32px;"> [wyczyść ściany usuwając dziury i łącząc ze sobą linie zewnętrzne](DefeatWB_Tools_clean_face_rmv_holes.md): czyści ściany usuwając dziury i łącząc ze sobą linie zewnętrzne.

-   <img alt="" src=images/DefeatWB_Tools_show_listed_edges.png  style="width:32px;"> [Pokaż krawędzie z listy](DefeatWB_Tools_show_listed_edges.md): zaznacza krawędzie z listy.
-   <img alt="" src=images/DefeatWB_Tools_show_listed_faces.png  style="width:32px;"> [Pokaż ściany z listy](DefeatWB_Tools_show_listed_faces.md): zaznacza ściany z listy.
-   <img alt="" src=images/DefeatWB_Tools_refine.png  style="width:32px;"> [Ulepsz](DefeatWB_Tools_refine.md): dopracuj obiekt.
-   <img alt="" src=images/DefeatWB_Tools_simple_copy.png  style="width:32px;"> [Prosta kopia](DefeatWB_Tools_simple_copy.md): tworzy prostą kopię obiektu.
-   <img alt="" src=images/DefeatWB_Tools_parametric_refine.png  style="width:32px;"> [Ulepszenie parametryczne](DefeatWB_Tools_parametric_refine.md): udoskonala obiekt w oparciu o podane parametry.

-   <img alt="" src=images/DefeatWB_Tools_geometry_check.png  style="width:32px;"> [Sprawdź geometrię](DefeatWB_Tools_geometry_check.md): przeprowadza sprawdzenie geometrii.
-   <img alt="" src=images/DefeatWB_Tools_get_Tolerance_value.png  style="width:32px;">. [pobierz wartość tolerancji](DefeatWB_Tools_get_Tolerance_value.md): Pobiera wartość tolerancji.
-   <img alt="" src=images/DefeatWB_Tools_set_Tolerance_value.png  style="width:32px;">. [Ustaw wartość tolerancji](DefeatWB_Tools_set_Tolerance_value.md): ustawia wartość tolerancji

-   <img alt="" src=images/DefeatWB_Tools_make_edges_selected_vertexes.png  style="width:32px;"> [Utwórz krawędź z wybranych wierzchołków](DefeatWB_Tools_make_edges_selected_vertexes.md): tworzy krawędź pa podstawie zaznaczonych wierzchołków.
-   <img alt="" src=images/DefeatWB_Tools_reset_placement.png  style="width:32px;"> [Zresetuj umiejscowienie](DefeatWB_Tools_reset_placement.md): resetuje współrzędne umiejscowienia.
-   <img alt="" src=images/DefeatWB_Tools_show_hide_typeId_shape.png  style="width:32px;"> [Pokaż / ukryj identyfikator typu kształtu](DefeatWB_Tools_show_hide_typeId_shape.md): Wyświetla lub ukrywa identyfikator typu kształtu.
-   <img alt="" src=images/DefeatWB_Tools_help.png  style="width:32px;"> [Pomoc](DefeatWB_Tools_help.md): wyświetla pomoc.

-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Cut.png  style="width:32px;"> [Fuzzy Cut](DefeatWB_Tools_Fuzzy_Cut.md): Rozmyte cięcie.
-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Union.png  style="width:32px;"> [Fuzzy Union](DefeatWB_Tools_Fuzzy_Union.md): Rozmyte połączenie.
-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Common.png  style="width:32px;"> [Fuzzy Common](DefeatWB_Tools_Fuzzy_Common.md): Rozmyta część wspólna.



## Poradniki Wideo 

### Upraszczanie

Usuwanie funkcji przy użyciu nowych narzędzi OCC7.3

[480px\|left\|thumb \|link=[https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/removing-holes.mp4\|Usunięcie](https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/removing-holes.mp4%7CUsunięcie) cech - otworów](Image:Defeaturing-WB-@Work_v3.png.md)

[480px\|left\|thumb \|link=<https://youtu.be/yrTtWFakAyE> \|alt=Defeaturing-WB-@Work\|Uproszczenie modelu](Image:Defeaturing-WB-@Work_v1.png.md)

[480px\|left\|thumb \|link=<https://youtu.be/vgQwGI6Fk6Q%7CWielokrotny> wybór ścian do operacji upraszczania](Image:Defeaturing-WB-@Work_v2.png.md)

[480px\|left\|thumb \|link=[https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/removing-fillet-chamfer.mp4\|Usunięcie](https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/removing-fillet-chamfer.mp4%7CUsunięcie) zaokrągleń i sfazowań](Image:Defeaturing-WB-@Work_v4.png.md)

[480px\|left\|thumb \|link=[https://peertube.mastodon.host/videos/watch/c6bc5abd-2eb7-48c7-af67-c4d8e6783872\|przegląd](https://peertube.mastodon.host/videos/watch/c6bc5abd-2eb7-48c7-af67-c4d8e6783872%7Cprzegląd) funkcji *(w języku niemieckim)*](Image:Defeaturing-WB-@Work_v5.png.md)

[480px\|left\|thumb \|link=<https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/parametric-defeaturing.mp4%7CUpraszczanie> parametryczne](Image:Defeaturing-WB-@Work_v6.png.md) 

### Naprawa

-   Szycie kształtu.
-   Usuwanie lub upraszczanie ścian.
-   Usuwanie otworów lub kieszeni.
-   Odczyt lub zmiana tolerancji.
-   Wykonywanie rozmytych operacji logicznych.



## Zewnętrzne środowiska pracy 

Środowiska pracy FreeCAD są łatwe do zaprogramowania w środowisku [Python](Python/pl.md). Dlatego też, wiele osób opracowuje dodatkowe \"przestrzenie robocze\" wykraczające poza główny obszar rozwoju programu FreeCAD.

Strona [Zewnętrzne środowiska pracy](External_workbenches/pl.md) zawiera informacje i poradniki na temat niektórych z nich, a projekt [Dodatki FreeCAD](https://github.com/FreeCAD/FreeCAD-addons) ma na celu zebranie ich i uczynienie łatwymi do zainstalowania z poziomu programu FreeCAD.

Nowe środowiska pracy są w czasie tworzenia, bądź cierpliwy!



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Defeaturing Workbench/pl
