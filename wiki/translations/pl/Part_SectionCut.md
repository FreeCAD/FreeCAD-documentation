---
- GuiCommand:
   Name:Part SectionCut
   Name/pl:Część: Wycinek przekroju
   MenuLocation:Widok → Wycinek z przekroju
   Workbenches:All
   Version:0.20
   SeeAlso:[[Std_ToggleClipPlane/pl]]
---

# Part SectionCut/pl

## Opis

Funkcja **Wycinek przekroju** jest dostępna dla wszystkich środowisk pracy, choć działa tylko dla obiektów Część i Projekt Części oraz ich złożeń. Tworzy ona trwałe przecięcie obiektów i złożeń. Ponieważ wynik cięcia jest normalnym obiektem [wycięcia](Part_Cut/pl.md) środowiska Część, może być dalej modyfikowany lub np. drukowany na drukarce 3D. Zobacz poniżej możliwe zastosowania.

<img alt="" src=images/Part_SectionCut_example.png  style="width:300px;"> 
*Przekrój złożenia. Niektóre przecięte powierzchnie zostały ręcznie pokolorowane. Żółta część nie jest cięta, ponieważ została celowo przesunięta o jeden mikron w głąb innej części.*

## Użycie

![Okno dialogowe Wycinek z przekroju.](images/Part_SectionCut_Dialog.png )

Okno dialogowe **Wycinek przekroju** jest otwierane za pomocą menu **Widok → <img src="images/Part_SectionCut.svg" width=16px> Trwałe przycięcie przekroju**. Jest ono niezależne od bieżącego obszaru roboczego i aktualnie otwartego dokumentu. Można je odłączyć od pozycji wyjściowej, naciskając przycisk w prawym górnym rogu okna dialogowego.

The **Section Cut** feature takes all currently visible Part objects in the active document into account. Therefore you can control what will be cut, by making a part visible or not. By checking one of the **Cutting** options in the dialog the feature is activated. You can then either enter a position (in coordinates of the document) or use the sliders to set the cut position. It is also possible to combine cuts, for example to cut in X and Z direction. The buttons **Flip** flip the side that is cut.

As soon as a **Cutting** option is checked in the dialog, you get a cut object in the [tree view](Tree_view.md). Its name is e.g. *SectionCutY* when it is a cut in Y direction.

The dialog option **Keep only cuts visible when closing** hides everything in the tree view except of the cut object when the button **Close** is clicked to close the dialog.

To remove the cut object, uncheck all **Cutting** options.

By unchecking all **Cutting** options, the button **Refresh view** becomes active. When pressed, it takes a kind of a screenshot of the currently visible Part objects. This will be used when you check the next time a **Cutting** option. The refreshing is necessary when you switched the document. It is furthermore useful for assemblies, where you might want to hide some parts or later want to add them to the cut. In this case the refreshing recalculates the min/max values of the sliders and cut positions according to the currently visible object dimensions.

If the option **Auto** in the cut face section is checked, the color and transparency of the cut objects will be taken for the cut face. This only works if all cut objects have the same color or transparency.

**Note:** For assemblies the sliders in the dialog are disabled (except the one for the transparency). The reason is that a slider movement results in many cut operations is a short time. For assemblies this quickly consumes all CPU power and a sticky slider movement is not helpful.

When you select a cut object in the tree view and then open the Section Cut dialog, the cut positions will be read into the dialog.

## Applications

-   An important use case is that Section Cut creates real cuts, not hollow ones like the **[Clip Plane](Std_ToggleClipPlane.md)** feature.
-   Section Cut is useful for assemblies to visualize for example the working principle of a device. You thereby might want to color certain cut faces using the **[Face Colors](Part_FaceColors.md)** tool. To use the tool, switch to the Part or PartDesign workbench, right-click on the cut object in the tree view and select in the context menu **Set colors**.
-   The limitation that only parts can be cut that don\'t intersect each other, see below, can be used as collision test.
-   The Section Cut feature can be used for technical drawings to highlight certain areas or to be able to draw in dimensions. The image below shows an example where the [TechDraw](TechDraw_Workbench.md) features [ActiveView](TechDraw_ActiveView.md) and [View](TechDraw_View.md) are used.

<img alt="" src=images/Part_SectionCut_TD-example.png  style="width:400px;"> 
*A technical drawing where a Section Cut result is used. (Click on the image for full size.)*

## Specjalne pozycje cięcia 

<img alt="Ukośne przecięcie złożenia." src=images/Part_SectionCut_slant-cut.png  style="width:200px;">

-   Na przykład na pierwszym rysunku na tej stronie wycięto tylko jedną czwartą złożenia. Zostało to wykonane przez utworzenie cięcia w kierunku X. Następnie w wynikowym obiekcie cięcia **SectionCutX** zmieniono [umiejscowienie](Placement/pl.md) obiektu podrzędnego **SectionCutBoxX**\'.
-   Aby uzyskać cięcie w dowolnym kierunku, możesz zrobić tak:

1.  Utwórz nową zawartość [części](Std_Part/pl.md).
2.  W widoku drzewa zaznacz wszystkie obiekty, które chcesz przeciąć i przenieś je do zawartości.
3.  Teraz ustaw położenie kontenera na wybrany przez siebie obrót. Na obrazku po lewej stronie kontener został obrócony o 45° wokół osi X i Z, a cięcie zostało wykonane w kierunku X.




## Ograniczenia

<img alt="Złożenie, w którym dwie części krzyżują się ze sobą i dlatego nie są przecięte. Zwróć uwagę na artefakty kolorystyczne na powierzchni przecięcia." src=images/Part_SectionCut_Color-artifact.png  style="width:200px;">

-   **Ważne:** Funkcja wycinania przekroju źle działa z [OpenCASCADE](OpenCASCADE/pl.md) 7.4 i starszym z powodu błędów. Dlatego zalecane jest używanie OpenCASCADE 7.5 lub nowszego *(wszystkie wersje FreeCAD 0.20 to zapewniają)*.
-   Na złożeniach części, które wzajemnie na siebie nachodzą, nie są możliwe przecięcia. Zazwyczaj elementy wzajemnie na siebie nachodzące nie są cięte, podczas gdy pozostałe są cięte. Jednakże, czasami cięcie może dać dziwne rezultaty, co jest błędem w bibliotekach OpenCASCADE. Aby uzyskać widok przekroju również dla przecinających się obiektów, można użyć makrodefinicji [Przekrój](Macro_cross_section/pl.md).
-   Szczególnie w przypadku korzystania ze środowiska pracy [A2plus](A2plus_Workbench/pl.md) niektóre złożenia mogą nachodzić na siebie zaledwie o mikron z powodu wewnętrznych błędów zaokrąglania. Aby to naprawić, dodaj mikron jako odstęp w ustawieniach wiązań.
-   W wyniku cięcia mogą pojawić się artefakty kolorystyczne. Czy i w jaki sposób zależą one od biblioteki OpenCASCADE, a także od położenia widoku. W wielu przypadkach artefakty kolorystyczne znikają po lekkim obróceniu widoku 3D.
-   Jeśli przecięte obiekty mają różne kolory, nie jest możliwe automatyczne zastosowanie ich koloru do odpowiednich powierzchni cięcia. Wszystkie wycięte powierzchnie otrzymają ten sam kolor, który został wybrany w oknie dialogowym.
-   W przypadku korzystania ze środowiska pracy [A2plus](A2plus_Workbench/pl.md) nie można automatycznie zastosować koloru złożenia do odpowiadających im powierzchni przyciętych. Wszystkie przecięte powierzchnie otrzymają ten sam kolor, który został wybrany w oknie dialogowym. Powodem tego jest fakt, że A2plus nie wprowadza części [jako link](App_Link/pl.md), lecz ładuje je jako plik.




## Informacje ogólne 

Funkcja **Wycinek z przekroju** została zainspirowana makrodefinicją [Przekrój](Macro_cross_section/pl.md) i działa technicznie w ten sposób:

Wszystkie widoczne obiekty umieszcza się w kontenerze [złożenia](Part_Compound/pl.md), a następnie rozcina się go za pomocą obiektu [prostopadłościanu](Part_Box/pl.md). Prostopadłościan musi być tak duży, aby objął całą objętość wszystkich widocznych obiektów. Aby to osiągnąć, pobierane jest ramka otaczającej obiektów. Podczas zmiany widoku przez dodanie / usunięcie obiektów lub zmianę dokumentu należy zaktualizować ramkę. Odbywa się to po kliknięciu przycisku **Odśwież widok**.

Aby umożliwić przecinanie obiektów wzajemnie na siebie nachodzących, zamiast kontenera złożenia potrzebny jest kontener [funkcji logicznej rozdzielającej](Part_BooleanFragments/pl.md). Dodanie tej funkcji jest planowane w następnej wersji programu FreeCAD.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part SectionCut/pl
