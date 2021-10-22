---
- GuiCommand:/pl
   Name:Part ProjectionOnSurface
   Name/pl:Część: Rzutowanie na powierzchnię
   MenuLocation:Część → Utwórz rzut na powierzchnię ...
   Workbenches:[Część](Part_Workbench/pl.md)
   Version:0.19
---

# Part ProjectionOnSurface/pl

## Opis


**<img src=images/Part_ProjectionOnSurface.svg style="width:16px"> [Rzutowanie na powierzchnię](Part_ProjectionOnSurface/pl.md)**

służy do rzutowania <img src=images/Draft_ShapeString.svg style="width:kształtu](Shape/pl.md) na powierzchnię innego obiektu. Można użyć tej funkcji do rzutowania logo lub obiektu tekstowego *(patrz **[16px"> [Kształt z tekstu](Draft_ShapeString/pl.md)**)* na różne powierzchnie, aby stworzyć interesujące efekty.

Biorąc pod uwagę _ do uzyskiwania efektów takich jak grawerowanie czy stemplowanie.

<img alt="" src=images/Part_ProjectionOnSurface1.png  style="width:300px;"> <img alt="" src=images/Part_ProjectionOnSurface2.png  style="width:300px;">



*Rzutowanie logo na zakrzywionej powierzchni.*

## Użycie

1.  Upewnij się, że masz co najmniej dwa obiekty w swoim dokumencie; obiekt \"źródłowy\", który chcesz rzutować, oraz obiekt \"docelowy\", na który rzut zostanie wykonany.
2.  Kliknij na przycisk **<img src=images/Part_ProjectionOnSurface.svg style="width:16px"> [Rzutowanie na powierzchnię](Part_ProjectionOnSurface/pl.md)**, aby uruchomić [panel zadań](Task_panel/pl.md) z różnymi opcjami.
3.  Kliknij na przycisk **Wybierz powierzchnie rzutowania**, a następnie kliknij na \"docelową\" powierzchnię, na której zostanie utworzony rzut.
4.  Następnie kliknij na określony przycisk, aby wybrać typ elementu podrzędnego, który chcesz dodać do obiektu rzutu.
    -   
        **Dodaj powierzchnię**
        
        : wybierz powierzchnię źródłową.

    -   
        **Dodaj zamknięte krawędzie**
        
        : wybierz krawędź źródłową. Narzędzie wyodrębni całą zamkniętą krawędź, do której należy dana krawędź. Na przykład wybranie pojedynczej krawędzi wielokąta spowoduje rzutowanie całego wielokąta.

    -   
        **Dodaj krawędź**
        
        : wybierz krawędź źródłową. Narzędzie będzie rzutować tylko wybraną krawędź.

    -   Gdy przycisk jest wciśnięty, wybierz element podrzędny w oknie [widoku 3D](3D_view/pl.md). Jeśli chcesz go odznaczyć, wybierz ponownie ten sam element.

    -   Po dokonaniu wyboru naciśnij ten sam przycisk **Dodaj ...**, aby wyjść z trybu wyboru.
5.  Następnie kliknij odpowiednie pole wyboru, aby wybrać typ kształtu rzutu, który chcesz utworzyć.
    -   
        {{RadioButton|TRUE|Wyświetl wszystko}}
        
        : pokaże wszystkie typy zamkniętych linii i krawędzi na powierzchni docelowej. Jeśli w poprzednim kroku został wybrany element podrzędny \"powierzchnia czołowa\", to w zależności od wartości parametru **Wysokość wyciągnięcia** zostanie pokazany podgląd bryły wyciągniętej z rzutu.

    -   
        {{RadioButton|TRUE|Pokaż powierzchnie}}
        
        : wyświetli podgląd wypełnionej powierzchni docelowej. Będzie to działać tylko jeśli w poprzednim kroku wybrałeś element podrzędny \"powierzchnia\". Jeśli wybrałeś \"zamknięty krawędzie\", tylko krawędzie *(bez powierzchni)* zostaną utworzone jako rzut. Jeśli wybrałeś \"krawędź\", tylko krawędzie zostaną utworzone jako rzut.

    -   
        {{RadioButton|TRUE|Pokaż krawędzie}}
        
        : pokaże podgląd krawędzi na powierzchni docelowej. Opcja działa niezależnie od tego, czy w poprzednim kroku dodałeś element podrzędny \"powierzchnie\", \"krawędzie zamknięte\", czy \"krawędzie\". Nawet jeśli dodałeś wypełnioną \"powierzchnię\", tylko krawędzie zostaną utworzone jako rzut.
6.  Naciśnij przycisk **OK**, aby zakończyć operację i utworzyć nowy obiekt rzutowania.

Uwagi:

-   Kierunek rzutowania jest automatycznie pobierany z kierunku ujęcia widoku w oknie [ widoku 3D](3D_view/pl.md) w momencie uruchomienia narzędzia.
-   Aby zmienić kierunek, przesuń ujęcie widoku i naciśnij **Pobierz aktualne ujęcie widoku**.
-   Możesz też nacisnąć przyciski **X:**, **Y:** lub **Z:**, aby ustawić kierunek rzutowania na główne osie globalne, +X, -X, +Y, -Y, +Z lub -Z.
-   Aby to zrobić, musisz ponownie wybrać geometrię, naciskając przyciski **Dodaj ...** i wybierając ponownie elementy podrzędne.

## Opcje

-    **Wysokość wyciągnięcia**: jest to wysokość bryły, która zostanie utworzona przez wyciągnięcie rzutowanej powierzchni, od powierzchni docelowej i wzdłuż ujemnej wartości kierunku rzutowania. Na przykład, jeśli kierunek rzutowania jest wzdłuż osi +Y {{Value|(0, 1, 0)}}, to bryła zostanie utworzona w kierunku -Y {{Value|(0, -1, 0)}}. To wyciągnięcie bryły zostanie utworzone tylko wtedy, gdy wybrany element podrzędny był zamkniętą ścianą, po naciśnięciu przycisku **Dodaj powierzchnię** i wybraniu opcji {{RadioButton|TRUE|Wyświetl wszystko}}.

-    **Głębokość bryły**: jest to odległość, o jaką obiekt rzutowania jest przesuwany wzdłuż kierunku rzutowania. Wartości ujemne spowodują przesunięcie obiektu w przeciwnym kierunku; pozwala to na tworzenie rzutów, które są przesunięte względem powierzchni docelowej.

## Ograniczenia

Algorytm rzutowania czasami nie jest w stanie utworzyć poprawnej powierzchni rzutowania. Jeśli tak się stanie, nie będzie można utworzyć również wyciągnięcia bryły.

Jeśli tak się stanie:

-   Sprawdź, czy twoja powierzchnia źródłowa jest poprawna; spróbuj uruchomić narzędzie **<img src=images/Part_CheckGeometry.svg style="width:16px"> [Sprawdź geometrię](Part_CheckGeometry/pl.md)** w poszukiwaniu wskazówek.
-   Sprawdź, czy kierunek rzutowania jest poprawny. Czy powierzchnia źródłowa może być realistycznie rzutowana na powierzchnię docelową? Czy rzut prosty trafiłby w powierzchnię? Ustaw ujęcie widoku tak, aby powierzchnia źródłowa znajdowała się przed powierzchnią docelową, a następnie spróbuj ponownie.
-   Spróbuj użyć opcji {{RadioButton|TRUE|Wyświetl krawędzie}}. Czy krawędzie są wyświetlane poprawnie? Spróbuj ręcznie odtworzyć krawędzie na powierzchni.

## Odnośniki internetowe 

-   Wątek na forum: [Rzutowanie powierzchni czołowych na zagiętą powierzchnię](https://forum.freecadweb.org/viewtopic.php?f=9&t=33700)

## Przykłady

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part ProjectionOnSurface/pl
