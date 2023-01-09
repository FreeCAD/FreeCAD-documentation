---
- TutorialInfo:/pl
   Topic:Modelowanie
   Level:Początkujący
   Author:Carlo Dormeletti ([onekk](User_onekk.md))<br>Ed Williams ([edwilliams16](User_edwilliams16.md))<br>Roy 043 ([Roy 043](User_Roy_043.md))
   Time:1 godzina
   FCVersion:0.19 lub nowszy
   SeeAlso:[Poradnik: Podstawy dla środowiska pracy Projekt Części](Basic_Part_Design_Tutorial/pl.md)
---

# Basic Part Design Tutorial 019/pl







## Wprowadzenie

*Poradnik ten to jest uaktualniona wersja poradnika [Podstawy dla środowiska pracy Projekt Części](Basic_Part_Design_Tutorial/pl.md)*.

![](images/Pd_tut_final_solid.png )

Ten poradnik wprowadza użytkowników do środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md). W tym poradniku stworzymy model przestrzennej bryły części pokazanej na powyższym obrazku. W [rysunku](TechDraw_Workbench/pl.md) na końcu tego akapitu podane są wszystkie niezbędne wymiary do wykonania zadania.

Rozpoczniemy od utworzenia podstawowego kształtu bryły ze szkicu bazowego, a następnie będziemy rozbudowywać ten kształt, dodając tzw. cechy. Cechy te będą dodawać materiał do bryły lub usuwać go z niej za pomocą dodatkowych szkiców i towarzyszących im operacji.

Zastosujemy niektóre z technik opisanych w artykule [Porady dotyczące tworzenia stabilnych modeli](Feature_editing/pl#Porady_dotycz.C4.85ce_tworzenia_stabilnych_modeli.md)

-   Użyjemy **szkicu głównego**
-   **Nazwane wiązania** posłużą do przechowywania wymiarów, do których będzie można się odwołać w dalszej części budowy modelu.
    Na przykład, aby zmienić szerokość modelu z 53 mm, jak na rysunku technicznym, na 55mm wystarczy zmodyfikować wartość **Długość**\' odpowiedniego **nazwanego wiązania** w **szkicu głównym**, a cały model odpowiednio się zmodyfikuje. Jest to projektowanie \"parametryczne\" w działaniu.
-   **Geometrie zewnętrzne** są potencjalnie objęte [Problemom nazewnictwa topologicznego](Topological_naming_problem/pl.md). Będziemy ich używać tylko wtedy, gdy będzie to absolutnie konieczne i będziemy starali się odwoływać do najbardziej **stabilnych** dostępnych elementów. Odwoływanie się do krawędzi i wierzchołków szkiców jest zwykle bardziej stabilne niż odwoływanie się do krawędzi i wierzchołków wygenerowanej geometrii bryłowej.

Ten poradnik nie będzie wykorzystywał wszystkich funkcji i narzędzi dostępnych w środowisku pracy Projekt Części, ale zapewni podstawy, na których użytkownicy mogą budować swoją wiedzę i umiejętności.

Zapraszamy do sygnalizowania wszelkich błędów i problemów w tym wątku na forum: [Nowy poradnik środowiska Projekt Części dla FC 019 i 020](https://forum.freecad.org/viewtopic.php?f=36&t=73235).

<img alt="" src=images/Tutorial_Drawing_Sheet.png  style="width:900px;">



## Uwagi wstępne 

-   Ten poradnik zawiera szczegółowe instrukcje, gdy opisuje daną operację po raz pierwszy. Kolejne operacje będą miały bardziej zwięzły opis. W razie wątpliwości należy znaleźć operację, która zawiera bardziej szczegółowy opis. Na przykład podczas tworzenia szkicu po raz pierwszy proces wyboru płaszczyzny szkicu będzie szczegółowo wyjaśniony, dla kolejnych szkiców nie będzie.
-   Wszystkie wymienione narzędzia są dostępne z pasków narzędziowych oraz z menu.
-   Ten poradnik zakłada, że opcja {{CheckBox|TRUE|Wiązania automatyczne}} w oknie **Edycja kontrolek** Szkicownika jest zaznaczona. Dzięki temu niektóre wiązania zostaną zastosowane automatycznie. W przeciwnym razie trzeba będzie zastosować je samodzielnie.
-   Jeśli solver szkicownika wykryje zbędne wiązanie, zmieni kolor szkicu na pomarańczowy. Przed dodaniem kolejnych wiązań należy usunąć nadmiarowe wiązania. Nadmiarowe wiązania są widoczne w panelu zadań, kliknij niebieskie odniesienie i naciśnij **Usuń**.
-   Kolor wymieniony powyżej jest kolorem domyślnym, można go zmienić w preferencjach. To samo dotyczy innych kolorów wymienionych w tym poradniku.
-   Z narzędzia do rysowania Szkicownik wychodzimy naciskając klawisz **Esc** lub klikając prawym przyciskiem myszy pusty obszar okna [widoku 3D](3D_view/pl.md). Kursor myszki zmieni swój wygląd na standardowy kursor ze strzałką. Jeśli naciśniesz **Esc** jeszcze raz, wyjdziesz z trybu edycji szkicu. Aby powrócić do edytora, kliknij zakładkę Model, a następnie kliknij dwukrotnie element Szkic w [Widoku drzewa](Tree_view/pl.md) lub kliknij go prawym przyciskiem myszki i wybierz **Edycja szkicu** z menu kontekstowego. Aby uniknąć opuszczania trybu edycji po zbyt częstym naciskaniu klawisza **Esc**, zmień preferencje **Klawisz Esc umożliwia wyjście z trybu edycji szkicu**, zobacz stronę [Ustawienia szkicownika](Sketcher_Preferences/pl#Og.C3.B3lne.md).
-   Możliwe jest, że niektóre elementy w panelu zadań, na przykład przycisk **OK**, nie są widoczne, jeśli panel nie jest wystarczająco szeroki. Możesz go poszerzyć, przeciągając jego prawy brzeg. Umieść kursor myszki nad krawędzią, gdy kursor zmieni wygląd na dwukierunkową strzałkę, przytrzymaj lewy przycisk myszki i przeciągnij.
-   W trakcie cyklu rozwoju v0.21/v1.0 wprowadzono nową ikonę dla narzędzia [Utwórz polilinię](Sketcher_CreatePolyline/pl.md): <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:24px;">. Stara ikona wygląda tak: <img alt="" src=images/Sketcher_CreatePolyline_rel_0.20.svg  style="width:24px;">. W tym poradniku będziemy używać nowej ikony.
-   Zapoznaj się z informacjami na stronie [Koncepcje środowiska Projekt Części](Part_and_PartDesign/pl#Koncepcje_.C5.9Brodowiska_Projekt_Cz.C4.99.C5.9Bci.md), aby zapoznać się z pewnymi podstawami koncepcyjnymi.
-   Zapoznaj się z informacjami na stronie [środowisko pracy Szkicownik](Sketcher_Workbench/pl.md), aby uzyskać bardziej szczegółowe wyjaśnienie niektórych terminów używanych tutaj.



## Rozpoczynamy

Najpierw upewnij się, że właśnie jesteś w środowisku pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md). W razie potrzeby wybierz go z listy rozwijanej [Środowisk pracy](Std_Workbench/pl.md). Po uruchomieniu go należy utworzyć nowy dokument, jeśli jeszcze tego nie zrobiłeś. Dobrym nawykiem jest częste zapisywanie swojej pracy, dlatego najpierw zapisz nowy dokument, nadając mu dowolną nazwę.

Cała praca w ramach środowiska pracy Projekt Części zaczyna się od [Zawartości](Glossary#Body.md). Kliknij <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Utwórz zawartość](PartDesign_Body/pl.md), aby ją utworzyć i aktywować. Zauważ, że możliwe jest również pominięcie tego kroku: podczas tworzenia szkicu za pomocą narzędzia środowiska Projekt Części <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Utwórz szkic](PartDesign_NewSketch/pl.md), jeśli nie zostanie znaleziona żadna istniejąca zawartość, nowa zostanie automatycznie utworzona i aktywowana.



## Szkic główny 

Szkic główny zawiera prostokątny kształt podstawy modelu oraz dwa *nazwane wiązania*, które dostarczą prawidłowe wymiary do innych części modelu: **długość**, która będzie zawierać 53 mm *(wynik dodania wymiaru 39 mm do dwóch boków 7 mm)*, oraz **szerokość**, która będzie zawierać 26 mm. Aby móc wykorzystać symetrię modelu w dalszych krokach, górna krawędź prostokąta zostanie wyśrodkowana względem punktu odniesienie położenia za pomocą wiązania symetrycznego.

**Sketch**

<img alt="Fig: MS1" src=images/Pd_start_00.png  style="width:300px;"> <img alt="Fig: MS2" src=images/Pd_tut_sketch_start.png  style="width:300px;"> <img alt="Fig: MS3" src=images/Pd_tut_sel_points_h.png  style="width:300px;"> <img alt="Fig: MS4" src=images/Pd_tut_rect_h_dim_end.png  style="width:300px;"> <img alt="Fig: MS5" src=images/Pd_tut_rect04.png  style="width:300px;"> <img alt="Fig: MS6" src=images/Pd_tut_rect_v3.png  style="width:300px;">

**Krok A: Utwórz szkic**

1.  Kliknij <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Utwórz szkic](PartDesign_NewSketch/pl.md). Spowoduje to utworzenie szkicu w obrębie właśnie utworzonej bryły. Będzie on nosił nazwę **Szkic**.
2.  Otworzy się panel zadań podobny do tego z **Rys. MS1**, w którym należy wybrać, do której płaszczyzny zostanie dołączony szkic.
    1.  Wybierz **XY_Plane** z listy lub wybierz tę płaszczyznę w oknie [widoku 3D](3D_view/pl.md).
    2.  Kliknij **OK**.
3.  FreeCAD automatycznie przełączy się na środowisko pracy <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Szkicownik](Sketcher_Workbench/pl.md)
4.  Szkic jest otwierany w trybie edycji: zobaczysz coś w rodzaju **Rys: MS2**. Wskazane są osie X i Y szkicu oraz jego punkt odniesienia położenia *(czerwony punkt)*.

**Krok B: Dodaj geometrię**

1.  Kliknij <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> [Utwórz prostokąt](Sketcher_CreateRectangle/pl.md).
2.  Podczas gdy narzędzie jest aktywne kursor ma następujący wygląd:
    ![](images/Pd_tut_rec_cursor.png )
3.  Wybierz dwa punkty, aby utworzyć prostokąt z grubsza wyśrodkowany wokół **osi Y** podobnie jak na **Rys: MS3**. Uwaga:
    -   Nie umieszczaj punktów na osi, ponieważ Solver automatycznie zastosuje wiązania, które później stworzą problemy.
    -   Wymiary prostokąta są w tym momencie nieistotne. Zostaną one przypisane za pomocą więzów w późniejszym kroku.
4.  Po zakończeniu naciśnij **Esc** lub kliknij prawym przyciskiem myszy, aby zakończyć pracę z narzędziem.

**Krok C: Przypisz wiązanie poziome**

1.  Wybierz linię zdefiniowaną przez **P2** i **P3** w **Rys: MS3**.
2.  Kliknij <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Zwiąż odległość poziomą](Sketcher_ConstrainDistanceX/pl.md):
    1.  Pomiędzy punktami końcowymi wybranej linii pojawi się wymiar. Ten wymiar to aktualna wartość długości.
    2.  Dodatkowo pojawi się okno dialogowe:

![](images/Pd_tut_rect03.png )

1.  1.  Przypisz **Długość = 53 mm**
    2.  Aby można było później odwołać się do tego wymiaru potrzebna jest jego nazwa. Możesz użyć dowolnej nazwy, musi być ona tylko unikalna w obrębie szkicu. Przypisz **Nazwę = długość**.
    3.  Kliknij **OK**.

2.  Wynik powinien być podobny do **Rys. MS4**

**Krok D: Przypisz wiązanie symetrii**

1.  Wybierz punkty **P2** i **P3** prostokąta.
2.  Wybierz **punkt odniesienia położenia** szkicu. Uwaga: kolejność wyboru punktów jest ważna.
3.  Kliknij <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [Wiązanie symetrii](Sketcher_ConstrainSymmetric/pl.md).
4.  W końcu otrzymasz coś, co wygląda jak **rysunek: MS5**.

*\'Krok E: Przypisz wiązanie pionowe*

:   Przypisz pionowe wiązanie odległości, stosując tę samą procedurę, która została użyta dla poprzednio zastosowanego poziomego wiązania odległości:

1.  Wybierz linię zdefiniowaną przez **P3** i **P4** w **Rys: MS3**.
2.  Kliknij <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Zwiąż odległość pionową](Sketcher_ConstrainDistanceY/pl.md):
    1.  Przypisz **Długość = 26 mm**
    2.  Przypisz **Nazwę = szerokość**.
    3.  Kliknij **OK**.
3.  Wynik powinien odpowiadać **rysunkowi: MS6**.
4.  Szkic jest teraz w pełni związany:
    -   Linie w szkicu są jasnozielone.
    -   W sekcji **Komunikaty Solvera** w panelu zadań wyświetlany jest komunikat **W pełni związany**.
    -   Jeśli wybierzesz dowolną linię lub wierzchołek szkicu i spróbujesz go przeciągnąć, pozostanie on nieruchomy.

**Krok F: Zamknij szkic**

:   Kliknij **Zamknij** u góry panelu [Zadań](Task_panel/pl.md), aby wyjść z trybu edycji szkicu.







## Profil główny 

Profil główny jest tworzony przez [wyciągnięcie](PartDesign_Pad/pl.md) nowego szkicu.

**Sketch001**

<img alt="Fig. MP1" src=images/OffsetSketch001.png  style="width:240px;"> <img alt="Fig: MP2" src=images/Pd_tut_side_fc.png  style="width:240px;">

**Krok A: Utwórz szkic**

:   Click <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Create sketch](PartDesign_NewSketch.md) and create a sketch attached to the **YZ_Plane**. FreeCAD will assign the name **Sketch001**.

**Krok B: Dodaj geometrię**

1.  Click <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:24px;"> [Create polyline](Sketcher_CreatePolyline.md) and make a shape like in **Fig: MP1**.
2.  The labels P1, P2 etc. will not appear in the sketch. They were added for reference.
3.  For the last point of the final segment make sure to pick the first point of the shape. The point will change color and you will see the symbol for a <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident constraint](Sketcher_ConstrainCoincident.md) appear near the cursor. Coincident constraints have to be explicit. Just having two points visually coincident is not sufficient.
4.  Press **Esc** or right-click to exit the tool.

**Step C: Assign constraints**

1.  The three vertical and horizontal constraints you see in the image should have been added automatically provided you drew those lines that way. If you didn\'t you need to add them.
2.  Select the point **P2** and the **Y axis** and apply a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Point onto object constraint](Sketcher_ConstrainPointOnObject.md).
3.  Select the **origin** and the point **P1** and apply a <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> [Horizontal constraint](Sketcher_ConstrainHorizontal.md). Why not a <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident constraint](Sketcher_ConstrainCoincident.md)? you might ask. Try it (and undo). The sketch will turn orange and a solver message **Redundant constraints** will appear. Because the line P1 to P2 has already been constrained to be vertical, the only remaining degree of freedom is P1\'s Y coordinate. The coincidence constraint sets both the X and Y coordinates to zero, but the X coordinate is already determined. The horizontal constraint, on the other hand, only sets the Y coordinate to zero, which is sufficient.
4.  Select the line defined by the points **P2** and **P3**, apply a <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontal distance constraint](Sketcher_ConstrainDistanceX.md), and assign **Length = 5 mm**.
5.  Select the line defined by the points **P1** and **P2**, apply a <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertical distance constraint](Sketcher_ConstrainDistanceY.md), and assign **Length = 26 mm**.
6.  Select the line defined by the points **P1** and **P4** and apply a <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontal distance constraint](Sketcher_ConstrainDistanceX.md):
    1.  For this value you will use a **named constraint** using [Expressions](Expressions.md). To do so you have to click the little button in the **Length** input field: <img alt="" src=images/Bound-expression.svg  style="width:24px;">.
    2.  You will be presented with a new dialog named **Formula editor** that contains an input field and a **Result:** label, similar to the image below:
        ![](images/Pd_tut_expressions.png )
        When you start typing in the input field, you will be presented with some autocompletions.
    3.  Select the label of the sketch. In our case we want **>.**. Note the period after the label.
    4.  To select the **named constraint** \"width\", you first have to enter **Constraints.** with the period. Here autocomplete works.
    5.  To add \"width\", as yet autocompletion is not available, so complete the cell to read **>.Constraints.width**. If all went well the red error message after **Result:** has been replaced by the correct value as in the image below:
        ![](images/Pd_tut_expression_end.png )
    6.  Click **OK** to close the **Formula editor** dialog.
    7.  Click **OK** to close the **Insert length** dialog.
7.  You should have a fully constrained sketch similar to **Fig: MP2**.
8.  Note the different colors used for distance constraints assigned using expressions, and those assigned specifying a length.

**Step D: Close the sketch**

:   Click **Close** at the top of the [tasks panel](Task_panel.md) to leave sketch edit mode.

**Pad**

<img alt="Fig: MP3" src=images/Pd_tut_pad1.png  style="width:240px;">

1.  Make sure **Sketch001** is selected.
2.  Click <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [Pad](PartDesign_Pad.md):
    1.  The **Pad parameters** task panel opens.
    2.  For **Type** select {{ComboBox|Dimension}}.
    3.  For **Length** again use an expression, but this time enter **>.Constraints.length**. This should evaluate to 53 mm.
    4.  Select {{CheckBox|TRUE|Symmetric to plane}}.
    5.  Click **OK** to close the task panel.
3.  You should now have a solid as shown in **Fig: MP3**.





## Corner cutouts 

For the corner cutouts two features are added to the model. A [pocket](PartDesign_Pocket.md), based on another sketch, is used to create the first cutout, and this feature is then [mirrored](PartDesign_Mirrored.md).

**Sketch002**

<img alt="Fig: CC1" src=images/Pd_tut_sk2_start.png  style="width:300px;"> <img alt="Fig: CC2" src=images/Pd_tut_sk2_eg01.png  style="width:300px;"> <img alt="Fig: CC3" src=images/Pd_tut_sk2_end.png  style="width:300px;">

**Step A: Hide the solid**

:   Hide the just created solid: Select **Pad** and click the **Spacebar**.

**Step B: Create the sketch**

:   Click <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Create sketch](PartDesign_NewSketch.md) and create a sketch attached to the **XZ_Plane**. The sketch will be named **Sketch002**.

**Step C: Add geometry**

1.  Select <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> [Create rectangle](Sketcher_CreateRectangle.md), and create a rectangle. Do not create it too near an axis, to avoid any automatic constraints that would make it difficult to move it into the correct position later.
2.  Exit the tool.

**Step D: Assign dimensional constraints**

1.  Select one of the horizontal lines, apply a <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontal distance constraint](Sketcher_ConstrainDistanceX.md), and assign a value of **11 mm**.
2.  Select one of the vertical lines, apply a <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertical distance constraint](Sketcher_ConstrainDistanceY.md), and assign a value of **5 mm**.
3.  You should obtain something similar to **Fig: CC1**.

**Step E: Close the sketch**

:   Click **Close**. **Sketch002** is not fully constrained at this stage.

**Step F: Make previous sketches visible**

:   To use [external geometry](Sketcher_External.md), the sketches whose elements we want to reference must be visible. Make sure **Sketch** and **Sketch001** are both visible. Use the **Spacebar** to toggle visibility if needed. Expand the **Pad** node in the [Tree view](Tree_view.md) to access **Sketch001**.

**Step G: Add external geometry and fully constrain the sketch**

1.  Double click **Sketch002** to enter edit mode.
2.  Rotate the view so you can clearly see the points as shown in **Fig: CC2**. This will ease subsequent steps. Note that the rectangle\'s initial position may be different in your sketch.
3.  Click <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [External geometry](Sketcher_External.md).
4.  While the tool is active the cursor has this appearance:
    ![](images/Pd_tut_eg_cursor.png )
5.  Select point **P1** in **Fig: CC2**. The selected point is added to the sketch as external geometry. In the **Elements** section of the task panel it will appear with a purple X icon or, <small>(v1.0)</small> , a purple dot icon.
6.  With the tool still active select point **P2** in **Fig: CC2**. This external geometry should also appear in the **Elements** section.
7.  Exit the tool.
8.  Select point **P1** and point **P3** and apply a <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;"> [Vertical constraint](Sketcher_ConstrainVertical.md). The rectangle will be aligned with the X position of **P1**.
9.  Select point **P2** and point **P3** and apply a <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> [Horizontal constraint](Sketcher_ConstrainHorizontal.md). The rectangle will be aligned with the Y position of **P2**.
10. You should have a fully constrained sketch similar to **Fig: CC3**.

**Krok H: Zamknij szkic**

:   Kliknij **Zamknij**.

**Kieszeń**

<img alt="Fig: CC4" src=images/Pd_tut_pck01.png  style="width:300px;"> <img alt="Fig: CC5" src=images/Pd_tut_pck02-mir.png  style="width:300px;">

To create the cutouts we will use the <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Pocket](PartDesign_Pocket.md) tool. This tool is the opposite of the Pad tool. Whereas the Pad tool adds material, the Pocket tool removes material.

1.  Select **Sketch002**.
2.  Click <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Pocket](PartDesign_Pocket.md):
    1.  The **Pocket parameters** task panel opens.
    2.  Select **Type** {{ComboBox|Through all}}.
    3.  Check {{CheckBox|TRUE|Reversed}}
    4.  Click **OK**.
3.  You should have something that resembles **Fig: CC4**

**Odbicie lustrzane**

Instead of creating another sketch and pocketing it, we take advantage of the model\'s symmetry about the YZ plane and use <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [Mirrored](PartDesign_Mirrored.md) to create the second cutout.

1.  Select **Pocket**.
2.  Click <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [Mirrored](PartDesign_Mirrored.md):
    1.  The **Mirrored parameters** task panel opens.
    2.  Select **Plane** {{ComboBox|Vertical sketch axis}} from the pulldown menu. The plane will be defined by this axis (the Y axis) and also by the Z axis of the sketch. Note that selecting **Base YZ Plane** would have the same result.
    3.  Click **OK**.
3.  You should now have a part that looks like **Fig: CC5**.







## Boki

The sides are created in a similar manner, but instead of removing material we will add material with a [pad](PartDesign_Pad.md) feature.

**Sketch003**

<img alt="Fig: SD1" src=images/Pd_tut_sk3_1.png  style="width:300px;"> <img alt="Fig: SD2" src=images/Pd_tut_pad001.png  style="width:300px;"> <img alt="Fig: SD3" src=images/Pd_tut_pad02-mir.png  style="width:300px;">

1.  Make sure **Sketch** is visible, and **Mirrored** is hidden.
2.  Click <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Create sketch](PartDesign_NewSketch.md) and create a new sketch attached to the **XY_Plane**. The sketch will be named **Sketch003**.
3.  Click <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> [Create rectangle](Sketcher_CreateRectangle.md) and create a rectangle similar to the smaller rectangle in **Fig: SD1**. Because the rectangle is offset from the X axis this should not trigger an automatic <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Point onto object constraint](Sketcher_ConstrainPointOnObject.md).
4.  Exit the tool.
5.  Click <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [External geometry](Sketcher_External.md).
6.  Select the point **P1** as shown in **Fig: CC2**.
7.  Exit the tool.
8.  Apply these constraints:
    1.  Select one of the horizontal lines, apply a <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontal distance constraint](Sketcher_ConstrainDistanceX.md), and assign a value of **7 mm**.
    2.  Select one of the vertical lines, apply a <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertical distance constraint](Sketcher_ConstrainDistanceY.md), and assign this expression: **>.Constraints.width**.
    3.  Select the **top-left** point of the created rectangle (marked **TL** in **Fig: SD1**) and the newly added **external geometry point** and apply a <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident constraint](Sketcher_ConstrainCoincident.md).
9.  The sketch should be fully constrained now.
10. Click **Close**.

**Pad001**

1.  Select **Sketch003**.
2.  Click <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [Pad](PartDesign_Pad.md):
    1.  Assign **Type =** {{ComboBox|Dimension}}.
    2.  Assign **Length = 16.7 mm**
    3.  Click **OK**.
3.  You should have a result as shown in **Fig: SD2**

**Mirrored001**

1.  Select **Pad001**.
2.  Click <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [Mirrored](PartDesign_Mirrored.md):
    1.  Make sure **Plane** {{ComboBox|Vertical sketch axis}} is selected.
    2.  Click **OK**.
3.  You should now have a part that looks like **Fig: SD3**.

**Uwaga**

Our two mirror operations have a common symmetry plane, so we could have made our model a little simpler by combining them. We would:

1.  Omit the first **Mirror** operation.
2.  Select both **Pad001** and **Pocket** in step 1 of the above **Mirrored001** operation.

This emphasizes the important concept that we are mirroring the selected features (the operations we performed on the body, in the selected order), not the body itself.







## Środkowy otwór 

Now it is time for the most challenging part of our modeling, a challenge that arises because some of the dimensions of the center hole are defined along the slanted face. If you use this face, created by padding **Sketch001**, as a reference for the next sketch, you expose yourself to the [Topological Naming Problem](Topological_naming_problem.md). A better solution is to reference **Sketch001** itself.

**Sketch004**

<img alt="Fig: CH1" src=images/Pd_tut_cen01.png  style="width:240px;"> <img alt="Fig: CH2" src=images/Pd_tut_cen02.png  style="width:240px;">

1.  Make **Sketch001** visible, and hide **Sketch** and **Mirrored001**.
2.  Click <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Create sketch](PartDesign_NewSketch.md) and create a new sketch attached to the **YZ_Plane**. The sketch will be named **Sketch004**.
3.  Click <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:24px;"> [Create polyline](Sketcher_CreatePolyline.md) and trace a polyline like that indicated by the points **P1**, **P2**, **P3** and **P4** in **Fig: CH1**.
4.  Remember to close the polyline by picking the first point. This will create the required <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincident constraint](Sketcher_ConstrainCoincident.md).
5.  Exit the tool.
6.  Check the applied constraints:
    -   Delete the redundant <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;"> [Vertical constraint](Sketcher_ConstrainVertical.md) applied to the line defined by **P1** and **P2**.
    -   Make sure a <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> [Horizontal constraint](Sketcher_ConstrainHorizontal.md) has been applied to the lines defined by **P1** and **P4**, and **P2** and **P3**.
    -   Make sure a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Point onto object constraint](Sketcher_ConstrainPointOnObject.md) has been applied to **P1** and the **Y axis**, and to **P2** and the **Y axis**.
7.  Click <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [External geometry](Sketcher_External.md)
8.  Select the line defined by **EGP1** and **EGP2** in **Sketch001**, indicated by the purple color in **Fig: CH2**.
9.  Exit the tool.
10. Apply a <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Point onto object constraint](Sketcher_ConstrainPointOnObject.md) to **P3** and the **external geometry**, and repeat this for **P4**. This will make the line defined by **P3** and **P4** coincident with the line defined by **EGP1** and **EGP2**.
11. Select the line **P3** to **P4**, apply a <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> [Distance constraint](Sketcher_ConstrainDistance.md), and assign 
**Length = 17 mm**
12. Select the points **EGP2** and **P4**, apply a <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> [Distance constraint](Sketcher_ConstrainDistance.md), and assign **Length = 7 mm**.
13. This will result in a fully constrained sketch like **Fig: CH2**.
14. Click **Close**.
15. Hide **Sketch001**.

**Pocket001**

1.  Select **Sketch004**.
2.  Click <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Pocket](PartDesign_Pocket.md):
    1.  Select **Type** {{ComboBox|Two Dimensions}}.
    2.  Assign **8.5 mm** to **Length** and **2nd length**.
    3.  Click **OK**.
3.  Select the newly created **Pocket001**.
4.  Change its **Refine** property to **True**.

**Uwagi**

1.  For **Pocket001** we could have alternatively used **Type** {{ComboBox|Dimension}}, checked **Symmetric to Plane**, and entered **17 mm** for the **Length** value.
2.  **Refine** will try to remove seams left by previous operations. It is advisable to only refine the final solid, as some operations can fail if a previous feature has been refined. However, there are also cases where refine can make an operation succeed. So in case of problems check this property and test. Unfortunately there is not yet a general rule to follow.







## Wynik

Model jest kompletny. Powinien wyglądać jak na poniższym obrazku.

Na koniec wybieramy **Szkic** w [Widoku Drzewa](Tree_view/pl.md) i na zakładce Dane w [Edytorze właściwości](Property_editor/pl.md) szukamy **Szkic → Wiązania**. Rozwiń ten węzeł i zmień wiązania **długość** i **szerokość**. Model powinien ulec zmianie parametrycznej.

![](images/Pd_tut_final_solid.png )


{{PartDesign Tools navi

}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Basic Part Design Tutorial 019/pl
