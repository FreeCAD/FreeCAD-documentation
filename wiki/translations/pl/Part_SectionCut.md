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


<div class="mw-translate-fuzzy">

Funkcja **Wycinek przekroju** jest dostępna dla wszystkich środowisk pracy, choć działa tylko dla obiektów Część i Projekt Części oraz ich złożeń. Tworzy ona trwałe przecięcie obiektów i złożeń. Ponieważ wynik cięcia jest normalnym obiektem [wycięcia](Part_Cut/pl.md) środowiska Część, może być dalej modyfikowany lub np. drukowany na drukarce 3D. Zobacz poniżej możliwe zastosowania.


</div>

<img alt="" src=images/Part_SectionCut_example.png  style="width:300px;"> 
*Przekrój złożenia. Niektóre przecięte powierzchnie zostały ręcznie pokolorowane. Żółta część nie jest cięta, ponieważ została celowo przesunięta o jeden mikron w głąb innej części.*



## Użycie

![Okno dialogowe Wycinek z przekroju.](images/Part_SectionCut_Dialog.png )


<div class="mw-translate-fuzzy">

Okno dialogowe **Wycinek przekroju** jest otwierane za pomocą menu **Widok → <img src="images/Part_SectionCut.svg" width=16px> Trwałe przycięcie przekroju**. Jest ono niezależne od bieżącego obszaru roboczego i aktualnie otwartego dokumentu. Można je odłączyć od pozycji wyjściowej, naciskając przycisk w prawym górnym rogu okna dialogowego.


</div>

Funkcja **Wycinek przekroju** uwzględnia wszystkie aktualnie widoczne obiekty części w aktywnym dokumencie. Dzięki temu można kontrolować, co zostanie wycięte, poprzez uwidocznienie lub nie danej części. Zaznaczenie jednej z opcji **Cięcie** w oknie dialogowym powoduje uaktywnienie funkcji. Następnie można wprowadzić pozycję *(we współrzędnych dokumentu)* lub ustawić pozycję cięcia za pomocą suwaków. Możliwe jest także łączenie cięć, np. cięcie w kierunku X i Z. Przyciski **Odwróć** odwracają stronę, która ma zostać przecięta.

Gdy tylko w oknie dialogowym zostanie zaznaczona opcja **Cięcie**\', w oknie [widok drzewa](Tree_view/pl.md) pojawi się obiekt cięcia. Jego nazwa to np. *SekcjaCięcieY*, gdy jest to cięcie w kierunku Y.

Opcja okna dialogowego **Cięcia będą widoczne tylko przy zamykaniu** ukrywa wszystko w widoku drzewa z wyjątkiem obiektu cięcia, gdy zostanie kliknięty przycisk **Zamknij** w celu zamknięcia okna dialogowego.

Aby usunąć wycięty obiekt, należy odznaczyć wszystkie opcje **Wycinania**.

Po usunięciu zaznaczenia wszystkich opcji **Wycinania** uaktywnia się przycisk **Odśwież widok**. Jego naciśnięcie powoduje wykonanie zrzutu ekranu z aktualnie widocznymi obiektami części. Zostanie on wykorzystany podczas kolejnego sprawdzania opcji **Wycinania**. Odświeżenie jest konieczne po przełączeniu dokumentu. Jest ono ponadto przydatne w przypadku złożeń, w których można ukryć niektóre części, a później dodać je do rozkroju. W takim przypadku odświeżanie przelicza wartości min/max suwaków i pozycji cięcia zgodnie z aktualnie widocznymi wymiarami obiektu.

Jeśli zaznaczona jest opcja **Auto** w sekcji powierzchni cięcia, dla powierzchni cięcia zostanie przyjęty kolor i przezroczystość wyciętych obiektów. Działa to tylko wtedy, gdy wszystkie wycięte obiekty mają taką samą wartość parametru barwy lub przezroczystości.

The option **Cut intersecting objects** allows to cut also objects that intersects each other. I assemblies intersections happen sometimes for object that are designed to only touch each other due to numerical precision issues. The drawback of the option is that all visible objects will get the same color. This color can be specified like in the cut face section of the dialog. If you need the cut for e.g. a nice picture with several face colors, you can change the face colors using the tool <img alt="" src=images/Part_FaceColors.svg  style="width:24px;"> [Set face colors](Part_FaceColors.md).

**Uwaga:** W przypadku złożeń suwaki w oknie dialogowym są wyłączone *(z wyjątkiem suwaka przezroczystości)*. Powodem tego jest fakt, że przesunięcie suwaka powoduje wykonanie wielu operacji cięcia w krótkim czasie. W przypadku złożeń szybko zużywa to całą moc procesora, a ciągłe przesuwanie suwaka nie jest użyteczne.

Po wybraniu obiektu przekroju w widoku drzewa, a następnie otwarciu okna dialogowego Wycinek przekroju, pozycje przekroju zostaną wczytane do okna dialogowego.



## Zastosowanie


<div class="mw-translate-fuzzy">

-   Ważnym przypadkiem zastosowania jest to, że funkcja Wycinek przekroju tworzy rzeczywiste przekroje, a nie puste w środku, jak funkcja **[Przełącz płaszczyznę tnącą](Std_ToggleClipPlane/pl.md)**.
-   Funkcja Wycinek przekroju jest przydatna dla złożeń w celu wizualizacji, na przykład, zasady działania urządzenia. Można też pokolorować niektóre wycięte powierzchnie, używając narzędzia **[Kolor powierzchni](Part_FaceColors/pl.md)**. Aby użyć tego narzędzia, należy przejść do środowiska pracy Część lub Projekt Części, kliknąć prawym przyciskiem myszy na wycięty obiekt w widoku drzewa i wybrać z menu kontekstowego **Ustaw kolory**.
-   Ograniczenie polegające na tym, że można wycinać tylko te części, które nie przecinają się wzajemnie (patrz poniżej), można użyć jako testu kolizji.
-   Funkcja Wycinek przekroju może być używana w rysunkach technicznych w celu wyróżnienia pewnych obszarów lub umożliwienia narysowania wymiarów. Poniższy obrazek pokazuje przykład, w którym użyto funkcji środowiska pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) takich jak [Aktywny widok](TechDraw_ActiveView/pl.md) i [Widok](TechDraw_View/pl.md).


</div>

<img alt="" src=images/Part_SectionCut_TD-example.png  style="width:400px;"> 
*Rysunek techniczny, na którym zaprezentowano wynik działania funkcji. ''(Kliknij obrazek, aby uzyskać pełny rozmiar)''.*



## Specjalne pozycje cięcia 

<img alt="Ukośne przecięcie złożenia." src=images/Part_SectionCut_slant-cut.png  style="width:200px;">

-   Na przykład na pierwszym rysunku na tej stronie wycięto tylko jedną czwartą złożenia. Zostało to wykonane przez utworzenie cięcia w kierunku X. Następnie w wynikowym obiekcie cięcia **SectionCutX** zmieniono [umiejscowienie](Placement/pl.md) obiektu podrzędnego **SectionCutBoxX**\'.
-   Aby uzyskać cięcie w dowolnym kierunku, możesz zrobić tak:

1.  Utwórz nową zawartość [części](Std_Part/pl.md).
2.  W widoku drzewa zaznacz wszystkie obiekty, które chcesz przeciąć i przenieś je do zawartości.
3.  Teraz ustaw położenie kontenera na wybrany przez siebie obrót. Na obrazku po lewej stronie kontener został obrócony o 45° wokół osi X i Z, a cięcie zostało wykonane w kierunku X.






## Ograniczenia

<img alt="Złożenie, w którym dwie części krzyżują się ze sobą i dlatego nie są przecięte. Zwróć uwagę na artefakty kolorystyczne na powierzchni przecięcia." src=images/Part_SectionCut_Color-artifact.png  style="width:200px;">


<div class="mw-translate-fuzzy">

-   **Ważne:** Funkcja wycinania przekroju źle działa z [OpenCASCADE](OpenCASCADE/pl.md) 7.4 i starszym z powodu błędów. Dlatego zalecane jest używanie OpenCASCADE 7.5 lub nowszego *(wszystkie wersje FreeCAD {{VersionPlus/pl|0.20}} to zapewniają)*.
-   Na złożeniach części, **które wzajemnie na siebie nachodzą**, nie są możliwe przecięcia. Zazwyczaj elementy wzajemnie na siebie nachodzące nie są cięte, podczas gdy pozostałe są cięte. Jednakże, czasami cięcie może dać dziwne rezultaty, co jest błędem w bibliotekach OpenCASCADE. Aby uzyskać widok przekroju również dla przecinających się obiektów, można użyć makrodefinicji [Przekrój](Macro_cross_section/pl.md).
-   Szczególnie w przypadku korzystania ze środowiska pracy [A2plus](A2plus_Workbench/pl.md) niektóre złożenia mogą nachodzić na siebie zaledwie o mikron z powodu wewnętrznych błędów zaokrąglania. Aby to naprawić, dodaj mikron jako odstęp w ustawieniach wiązań.
-   W wyniku cięcia mogą pojawić się artefakty kolorystyczne. Czy i w jaki sposób zależą one od biblioteki OpenCASCADE, a także od położenia widoku. W wielu przypadkach artefakty kolorystyczne znikają po lekkim obróceniu widoku 3D.
-   Jeśli przecięte obiekty mają różne kolory, nie jest możliwe automatyczne zastosowanie ich koloru do odpowiednich powierzchni cięcia. Wszystkie wycięte powierzchnie otrzymają ten sam kolor, który został wybrany w oknie dialogowym.
-   W przypadku korzystania ze środowiska pracy [A2plus](A2plus_Workbench/pl.md) nie można automatycznie zastosować koloru złożenia do odpowiadających im powierzchni przyciętych. Wszystkie przecięte powierzchnie otrzymają ten sam kolor, który został wybrany w oknie dialogowym. Powodem tego jest fakt, że A2plus nie wprowadza części [jako link](App_Link/pl.md), lecz ładuje je jako plik.





</div>



## Informacje ogólne 

Funkcja **Wycinek z przekroju** została zainspirowana makrodefinicją [Przekrój](Macro_cross_section/pl.md) i działa technicznie w ten sposób:


<div class="mw-translate-fuzzy">

Wszystkie widoczne obiekty umieszcza się w kontenerze [złożenia](Part_Compound/pl.md), a następnie rozcina się go za pomocą obiektu [prostopadłościanu](Part_Box/pl.md). Prostopadłościan musi być tak duży, aby objął całą objętość wszystkich widocznych obiektów. Aby to osiągnąć, pobierane jest ramka otaczającej obiektów. Podczas zmiany widoku przez dodanie / usunięcie obiektów lub zmianę dokumentu należy zaktualizować ramkę. Odbywa się to po kliknięciu przycisku **Odśwież widok**.


</div>





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part SectionCut/pl
