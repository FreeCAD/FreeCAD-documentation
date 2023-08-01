# Report view/pl
## Wprowadzenie

[Widok raportu](Report_view/pl.md) to panel, w którym wyświetlane są komunikaty tekstowe z procesów i narzędzi programu FreeCAD. Jest on dostępny w menu **{{StdMenu|[Widok](Std_View_Menu/pl.md)** → Panele → Widok raportu}}.

Niektóre właściwości tego panelu, takie jak kolor tekstu oraz to, czy ma być on automatycznie wyświetlany w przypadku ostrzeżeń lub błędów, można skonfigurować w zakładce **Ogólne → Okno raportów** [Edytora preferencji](Preferences_Editor/pl#Widok_raportu.md).

<img alt="" src=images/FreeCAD_Report_view.png  style="width:800px;">



*Okno ''Widok raportu'' pokazujące komunikaty, gdy program FreeCAD został właśnie uruchomiony.*

## Komunikaty


**Zobacz również:**

[API w konsoli](Console_API/pl.md), and [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Widok raportu wyświetla komunikaty z wewnętrznej klasy FreeCAD `Console`.

-    `FreeCAD.Console.PrintMessage("text")`, wyświetla dowolny komunikat informacyjny, który nie sugeruje błędnego działania; na przykład, wyświetla współrzędne punktów, wynik obliczenia odległości, liczbę wierzchołków w kształcie, itp. Domyślnie w kolorze czarnym.

-    `FreeCAD.Console.PrintWarning("text")`, wyświetla komunikaty, które mają na celu ostrzeżenie użytkownika o dziwnym zachowaniu aplikacji. Ostrzeżenia powinny być wyświetlane, gdy brakuje jakiejś funkcjonalności, ale program nadal działa poprawnie. Domyślnie w kolorze żółtym.

-    `FreeCAD.Console.PrintError("text")`, wyświetla komunikaty, które mają być komunikatami o błędach, tzn. gdy brakuje krytycznego komponentu, który powoduje, że dana operacja nie powiedzie się. Domyślnie w kolorze czerwonym.

-    `FreeCAD.Console.PrintLog("text")`, wyświetla komunikaty, które trafiają do dziennika. Mogą to być dowolne komunikaty, które mogą być przydatne do rozwiązywania problemów w przyszłości poprzez czytanie dzienników, na przykład uruchamianie lub zamykanie środowiska pracy. Domyślnie w kolorze niebieskim.

Z funkcji tych można korzystać bezpośrednio z [konsoli Python](Python_console/pl.md) lub z [makrodefinicji](Macros/pl.md) i niestandardowych okien roboczych.

<img alt="" src=images/FreeCAD_Report_view_example.png  style="width:800px;">



*Przykładowe komunikaty w oknie Widoku raportu: komunikat ogólny, ostrzeżenie, błąd i komunikat zarejestrowany.*

## Działania

Kliknięcie prawym przyciskiem myszki w oknie widoku raportu powoduje wyświetlenie menu podręcznego z kilkoma poleceniami:

-    **Opcje**:

    -   
        **Wyświetl typy wiadomości**
        
        : zobacz stronę [Edytormpreferencji](Preferences_Editor/pl#Widok_raportu.md) aby poznać więcej szczegółów,

    -   
        **Pokaż okno Widok raportu dla**
        
        : zobacz stronę [Edytor preferencji](Preferences_Editor/pl#Widok_raportu.md) aby poznać więcej szczegółów,

    -   
        **Przekierowanie wyjście z Pythona**
        
        : zobacz stronę [Edytor preferencji](Preferences_Editor/pl#Widok_raportu.md) aby poznać więcej szczegółów,

    -   
        **Przekieruj błędy Pythona**
        
        : zobacz stronę [Edytor preferencji](Preferences_Editor/pl#Widok_raportu.md) aby poznać więcej szczegółów,

    -   
        **Przejdź na koniec**
        
        jeżeli opcja ta jest zaznaczona, widok raportu będzie przewijany do dołu po dodaniu nowej wiadomości.

-    **Kopiuj**: zapisuje zaznaczony tekst w schowku w celu późniejszego wklejenia. Opcja ta jest nieaktywna, jeśli nic nie jest zaznaczone.

-   Polecenie **Zaznacz wszystko**: zaznacza cały tekst w widoku raportu.

-    **Wyczyść**: usuwa wszystkie wiadomości w widoku raportu. Jest to przydatne, jeśli chcesz rozwiązać problem z narzędziem, które wysyła komunikaty do widoku raportu i chcesz się upewnić, że nie ma w nim starych komunikatów z poprzednich narzędzi.

-    **Zapisz jako**: zapisuje komunikaty w widoku raportu do pliku tekstowego.


{{Interface navi

}} {{Std Base navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Report view/pl
