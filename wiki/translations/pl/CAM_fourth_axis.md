# CAM fourth axis/pl
}









## Opis

Te eksperymentalne narzędzia pozwalają na frezowanie z użyciem czwartej osi [ścian](https://forum.freecadweb.org/viewtopic.php?f=15&t=36773) i [kieszeni](https://forum.freecadweb.org/viewtopic.php?f=15&t=35867)

Te narzędzia są we wczesnym rozwoju. Możliwe są błędy. Dziękujemy za opinie i testowanie.



## Instalacja

Najlepiej zaktualizuj FreeCAD do wersji 0.19.16502 lub wyższej.

Pobierz te skrypty:

-   PathProfileFaces.py [dostępny tutaj](https://forum.freecadweb.org/viewtopic.php?f=15&t=36773) i
-   PathAreaOp.py [tutaj](https://forum.freecadweb.org/viewtopic.php?f=15&t=35867)
-   PathPocketShape.py [tutaj](https://forum.freecadweb.org/viewtopic.php?f=15&t=35867) (do operacji kieszeni)

Umieść je w swojej ścieżce FreeCAD/Mod/CAM/PathScripts, \*po\* zmianie nazw oryginałów aby je bezpiecznie zachować. Zmień nazwy nowych skryptów na nazwy oryginalnych skryptów. Uruchom FreeCAD ponownie i baw się dobrze.

Używaj na własną odpowiedzialność.



## Ograniczenia

Obecne operacje wspierające czwartą oś nie obsługują złożonych obrotów: tych w osiach X i Y jednocześnie.

Nie ma obecnie integracji GUI ustawień obrotów dla czwartej osi w oficjalnej wersji programu FreeCAD. Wszystkie powiązane ustawienia są w zakładce Dane widoku właściwości dla każdej wspieranej operacji osobno.



## Użycie



### Profilowanie ścian 

-   Wybierz ścianę/ściany do operacji jak zazwyczaj
-   Kliknij ikonę [CAM Profilowanie ścian](CAM_Profile/pl#Profilowanie_ścian.md), aby rozpocząć operację
-   Zmień ustawienia zgodnie z potrzebami
-   Kliknij OK, aby uruchomić operację
-   W liście właściwości nowej operacji zmień ustawienie „Enable Rotation" w razie potrzeby dla powierzchni
-   Przelicz ponownie operację
-   Dostosuj głębokości początkowe/końcowe w razie potrzeby. Głębokość końcowa jest kodowana tak, aby nie przekraczała wybranej powierzchni użytej do profilu.



### Kieszeń kształtu 

-   Kliknij ikonę [CAM Kieszeń kształtu](CAM_Pocket_Shape/pl.md), aby rozpocząć operację.
-   Kliknij OK, aby utworzyć operację - bez wybranych powierzchni
-   Wybierz nową operację Pocket_Shape w oknie zadań
-   W liście właściwości operacji przewiń do sekcji CAM i zmień właściwość „Enable Rotation" na żądane ustawienie 4-osiowe.
-   Przelicz ponownie operację
-   Kliknij dwukrotnie tę samą operację, aby edytować ustawienia w oknie zadań.
-   Otwórz zakładkę \'Geometry podstawowa\'. Wybierz jedną powierzchnię (preferowaną na razie) i kliknij przycisk \'Dodaj\', aby umieścić tę powierzchnię na liście Geometry Bazowej.
-   Zmień inne ustawienia operacji zgodnie z potrzebami.
-   Kliknij OK, aby zapisać i zastosować zmiany.



## Rozwiązywanie problemów 

-   Jest właściwość „Inverse Angle". Może być konieczne jej przełączenie, aby uzyskać poprawne ścieżki dla niektórych powierzchni.
-   Ustaw „Enable Rotation" na coś innego niż \'Off\', aby profilować powierzchnie prostopadłe, które nie są normalne do osi Z.
-   Przełącz właściwość „Reverse Direction", jeśli ścieżka wydaje się być przesunięta o 180 stopni.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM fourth axis/pl
