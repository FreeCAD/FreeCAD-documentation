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

Funkcja **Wycinek przekroju** jest dostępna dla wszystkich środowisk pracy, choć działa tylko dla obiektów Część i Projekt Części oraz ich złożeń. Tworzy ona trwałe przecięcie obiektów i złożeń. Ponieważ wynik cięcia jest normalnym obiektem <img alt="" src=images/Part_Cut.svg  style="width:24px;"> [wycięcia](Part_Cut/pl.md) środowiska Część, może być dalej modyfikowany lub np. drukowany na drukarce 3D. Zobacz poniżej możliwe zastosowania.

<img alt="" src=images/Part_SectionCut_example.png  style="width:300px;"> 
*Przekrój złożenia. Niektóre przecięte powierzchnie zostały ręcznie pokolorowane. Żółta część nie jest cięta, ponieważ została celowo przesunięta o jeden mikron w głąb innej części.*



## Użycie

![Okno dialogowe Wycinek z przekroju.](images/Part_SectionCut_Dialog.png )

Okno dialogowe **Wycinek przekroju** jest otwierane za pomocą menu **Widok → <img src="images/Part_SectionCut.svg" width=24px> Trwałe przycięcie przekroju**. Jest ono niezależne od bieżącego obszaru roboczego i aktualnie otwartego dokumentu. Można je odłączyć od pozycji wyjściowej, naciskając przycisk w prawym górnym rogu okna dialogowego.

Funkcja **Wycinek przekroju** uwzględnia wszystkie aktualnie widoczne obiekty części w aktywnym dokumencie. Dzięki temu można kontrolować, co zostanie wycięte, poprzez uwidocznienie lub nie danej części. Zaznaczenie jednej z opcji **Cięcie** w oknie dialogowym powoduje uaktywnienie funkcji. Następnie można wprowadzić pozycję *(we współrzędnych dokumentu)* lub ustawić pozycję cięcia za pomocą suwaków. Możliwe jest także łączenie cięć, np. cięcie w kierunku X i Z. Przyciski **Odwróć** odwracają stronę, która ma zostać przecięta.

Gdy tylko w oknie dialogowym zostanie zaznaczona opcja **Cięcie**\', w oknie [widok drzewa](Tree_view/pl.md) pojawi się obiekt cięcia. Jego nazwa to np. *SekcjaCięcieY*, gdy jest to cięcie w kierunku Y.

Opcja okna dialogowego **Cięcia będą widoczne tylko przy zamykaniu** ukrywa wszystko w widoku drzewa z wyjątkiem obiektu cięcia, gdy zostanie kliknięty przycisk **Zamknij** w celu zamknięcia okna dialogowego.

Aby usunąć wycięty obiekt, należy odznaczyć wszystkie opcje **Wycinania**.

Po usunięciu zaznaczenia wszystkich opcji **Wycinania** uaktywnia się przycisk **Odśwież widok**. Jego naciśnięcie powoduje wykonanie zrzutu ekranu z aktualnie widocznymi obiektami części. Zostanie on wykorzystany podczas kolejnego sprawdzania opcji **Wycinania**. Odświeżenie jest konieczne po przełączeniu dokumentu. Jest ono ponadto przydatne w przypadku złożeń, w których można ukryć niektóre części, a później dodać je do rozkroju. W takim przypadku odświeżanie przelicza wartości min/max suwaków i pozycji cięcia zgodnie z aktualnie widocznymi wymiarami obiektu.

Jeśli zaznaczona jest opcja **Auto** w sekcji powierzchni cięcia, dla powierzchni cięcia zostanie przyjęty kolor i przezroczystość wyciętych obiektów. Działa to tylko wtedy, gdy wszystkie wycięte obiekty mają taką samą wartość parametru barwy lub przezroczystości.

Opcja *Wytnij przecinające się obiekty* pozwala na wycięcie również obiektów, które przecinają się wzajemnie. Podczas montażu zdarza się, że obiekty, które zostały zaprojektowane tak, aby tylko się dotykały, przecinają się ze względu na problemy z precyzją numeryczną. Wadą tej opcji jest to, że wszystkie widoczne obiekty otrzymają ten sam kolor. Ten kolor może być określony podobnie jak w sekcji Ściany cięcia w oknie dialogowym. Jeżeli potrzebujesz cięcia np. dla fajnego obrazka z kilkoma kolorami ścian, możesz zmienić kolory ścian za pomocą narzędzia <img alt="" src=images/Part_FaceColors.svg  style="width:24px;"> [Kolor powierzchnii](Part_FaceColors/pl.md).

**Uwaga:** W przypadku złożeń suwaki w oknie dialogowym są wyłączone *(z wyjątkiem suwaka przezroczystości)*. Powodem tego jest fakt, że przesunięcie suwaka powoduje wykonanie wielu operacji cięcia w krótkim czasie. W przypadku złożeń szybko zużywa to całą moc procesora, a ciągłe przesuwanie suwaka nie jest użyteczne.

Po wybraniu obiektu przekroju w widoku drzewa, a następnie otwarciu okna dialogowego Wycinek przekroju, pozycje przekroju zostaną wczytane do okna dialogowego.



## Zastosowanie

-   Ważnym przypadkiem zastosowania jest to, że funkcja Wycinek przekroju tworzy rzeczywiste przekroje, a nie puste w środku, jak funkcja <img alt="" src=images/Std_ToggleClipPlane.svg  style="width:24px;"> [Przełącz płaszczyznę tnącą](Std_ToggleClipPlane/pl.md).
-   Funkcja Wycinek przekroju jest przydatna dla złożeń w celu wizualizacji, na przykład, zasady działania urządzenia. Można też pokolorować niektóre wycięte powierzchnie, używając narzędzia <img alt="" src=images/Part_FaceColors.svg  style="width:24px;"> [Kolor powierzchni](Part_FaceColors/pl.md). Aby użyć tego narzędzia, należy przejść do środowiska pracy Część lub Projekt Części, kliknąć prawym przyciskiem myszy na wycięty obiekt w widoku drzewa i wybrać z menu kontekstowego **Ustaw kolory**.
-   Bez opcji **Przetnij obiekty zachodzące na siebie** tylko części, które nie przecinają innych zostaną wycięte. Można użyć jako testu kolizji.
-   Funkcja Wycinek przekroju może być używana w rysunkach technicznych w celu wyróżnienia pewnych obszarów lub umożliwienia narysowania wymiarów. Poniższy obrazek pokazuje przykład, w którym użyto funkcji środowiska pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) takich jak <img alt="" src=images/TechDraw_ActiveView.svg  style="width:24px;"> [Aktywny widok](TechDraw_ActiveView/pl.md) i <img alt="" src=images/TechDraw_View.svg  style="width:24px;"> [Widok](TechDraw_View/pl.md).

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

-   **Ważne:** Funkcja wycinania przekroju źle działa z [OpenCASCADE](OpenCASCADE/pl.md) 7.4 i starszym z powodu błędów. Dlatego zalecane jest używanie OpenCASCADE 7.5 lub nowszego *(wszystkie wersje FreeCAD {{VersionPlus/pl|0.20}} to zapewniają)*.

-    {{VersionPlus/pl|1.0}}: Opcja **Obcinaj obiekty przecinające się** spowoduje, że wszystkie widoczne części zostaną pokolorowane tak samo. Technicznie nie da się tego uniknąć. Jeśli jednak potrzebujemy trwałego cięcia np. do prezentacji, zobacz opisaną powyżej metodę jak ustawić kolor samodzielnie.

-    {{VersionMinus/pl|0.20}}: Na złożeniach części, **które wzajemnie na siebie nachodzą**, nie są możliwe przecięcia. Zazwyczaj elementy wzajemnie na siebie nachodzące nie są cięte, podczas gdy pozostałe są cięte. Jednakże, czasami cięcie może dać dziwne rezultaty, co jest błędem w bibliotekach OpenCASCADE. Aby uzyskać widok przekroju również dla przecinających się obiektów, można użyć makrodefinicji [Przekrój](Macro_cross_section/pl.md).

-    {{VersionMinus/pl|0.20}}: Szczególnie w przypadku korzystania ze środowiska pracy [A2plus](A2plus_Workbench/pl.md) niektóre złożenia mogą nachodzić na siebie zaledwie o mikron z powodu wewnętrznych błędów zaokrąglania. Aby to naprawić, dodaj mikron jako odstęp w ustawieniach wiązań.

-   W wyniku cięcia mogą pojawić się artefakty kolorystyczne. Czy i w jaki sposób zależą one od biblioteki OpenCASCADE, a także od położenia widoku. W wielu przypadkach artefakty kolorystyczne znikają po lekkim obróceniu widoku 3D.

-   Jeśli przecięte obiekty mają różne kolory, nie jest możliwe automatyczne zastosowanie ich koloru do odpowiednich powierzchni cięcia. Wszystkie wycięte powierzchnie otrzymają ten sam kolor, który został wybrany w oknie dialogowym.

-   W przypadku korzystania ze środowiska pracy [A2plus](A2plus_Workbench/pl.md) nie można automatycznie zastosować koloru złożenia do odpowiadających im powierzchni przyciętych. Wszystkie przecięte powierzchnie otrzymają ten sam kolor, który został wybrany w oknie dialogowym. Powodem tego jest fakt, że A2plus nie wprowadza części [jako link](App_Link/pl.md), lecz ładuje je jako plik.






## Informacje ogólne 

Funkcja **Wycinek z przekroju** została zainspirowana makrodefinicją [Przekrój](Macro_cross_section/pl.md) i działa technicznie w ten sposób:

Wszystkie widoczne obiekty umieszcza się w kontenerze <img alt="" src=images/Part_Compound.svg  style="width:24px;"> [Złożenie](Part_Compound/pl.md). Dla opcji **Przetnij obiekty zachodzące na siebie** obiekty umieszczane są w <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [fragmentach funkcji logicznej](Part_BooleanFragments/pl.md). Złożenie rozcina się za pomocą obiektu <img alt="" src=images/Part_Box.svg  style="width:24px;"> [prostopadłościanu](Part_Box/pl.md). Prostopadłościan musi być tak duży, aby objął całą objętość wszystkich widocznych obiektów. Aby to osiągnąć, pobierane jest ramka otaczającej obiektów. Podczas zmiany widoku przez dodanie / usunięcie obiektów lub zmianę dokumentu należy odświeżyć ramkę otaczającą. Odbywa się to po kliknięciu przycisku **Odśwież widok**.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part SectionCut/pl
