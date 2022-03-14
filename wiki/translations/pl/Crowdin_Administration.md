# Crowdin Administration/pl
{{TOCright}}

## Funkcje

-   Tłumacz
    -   Możliwość proponowania i głosowania na tłumaczenie w danym języku.
    -   Poproś o więcej kontekstu, poproś o wyjaśnienie, zgłoś błędy w tłumaczonym tekście, zakwestionuj bieżący wpis w tłumaczeniu itd.

-   Korektor
    -   Zarządza tłumaczeniami, które tłumacze proponują i/lub nad którymi głosują. Korektor następnie akceptuje/odrzuca tłumaczenie.
    -   Dodatkowy krok jest potrzebny, aby ostatecznie zatwierdzić tłumaczenie. Ponieważ \"zatwierdzenie\" tłumaczenia wymaga ponownego przeczytania go i zaznaczenia, stanowi to rodzaj warstwy \"zapewnienia jakości\". Zatwierdzenie tłumaczenia powoduje zaznaczenie ciągu znaków na zielono i zwiększenie postępu na zielonym pasku stanu języka, który jest tłumaczony. Zielony pasek postępu może wskazywać na \"zdrowie\" tłumaczonego języka. Pozwala on również programistom na dodatkową elastyczność w łączeniu tłumaczeń, które zostały tylko zatwierdzone.
    -   Odpowiadaj na pytania tłumaczy w platformie Crowdin. Na przykład, jeśli potrzeba więcej kontekstu; lub jest błąd w łańcuchu, który ma być przetłumaczony, lub tłumaczenie, które zostało zaakceptowane lub zatwierdzone jest kwestionowane itp.
    -   Zgłaszanie deweloperom wszelkich istotnych problemów, które wymagają zmian w kodzie źródłowym itp.

## Filtrowanie ciągów znaków 

<img alt="" src=images/Crowdin_Filter_Strings.png  style="width:500px;">

Filtrowanie ciągów znaków jest przydatną funkcją dla korektorów i menedżerów. Daje ona możliwość efektywnego sortowania wielu ciągów tłumaczeń, aby na przykład pokazać tylko te ciągi, które zostały oznaczone jako \"brak dodatkowych informacji kontekstowych\" lub \"nieprawidłowy ciąg źródłowy\". Ta usługa, którą tłumacze wykonują dla FreeCAD zapewnia dodatkową warstwę testowania jakości. Wiele literówek, problemów gramatycznych, a nawet błędów może zostać ujawnionych poprzez sprawdzanie tłumaczeń. I tak użytkownicy zaznaczają te problematyczne ciągi, abyśmy mogli na nie odpowiedzieć i ostatecznie je rozwiązać.

## Skróty klawiaturowe 

<img alt="" src=images/Crowdin_keyboard_shortcuts.png  style="width:300px;">

Korzystanie ze skrótów klawiaturowych to ważna wskazówka dotycząca oszczędności czasu i wydajności. Warto się jej nauczyć, jeśli jesteś tłumaczem, korektorem lub menedżerem. Listę skrótów klawiaturowych można wyświetlić, naciskając ikonę klawiatury w prawej górnej części interfejsu użytkownika programu Crowdin.

**Ważna uwaga:** Należy pamiętać, aby nie wprowadzać błędów do ciągów tłumaczeń, które powstały przez przypadkowe naciśnięcia klawiszy, które miały być skrótami klawiaturowymi.

**Często używane skróty:**

-   Kopiowanie tłumaczenia źródłowego: **Alt** + **C**
-   Zapisanie tłumaczenia: **Ctrl** + **Enter**
-   Zatwierdzenie tłumaczenia: **Alt** + **L** *(istotne dla korektorów tekstów)*

## Naprawa problemów z tłumaczeniem 


<div class="mw-translate-fuzzy">

Jeśli zauważysz ciąg znaków w interfejsie użytkownika FreeCAD, który nie jest przetłumaczony, wykonaj następujące czynności:

1.  Jeśli nie jesteś pewien, do którego środowiska pracy należy ciąg znaków, najpierw zlokalizuj go w kodzie źródłowym programu FreeCAD. W systemie Linux możesz użyć {{Incode|grep -r "English text" *}}.
2.  Na przykład, jeśli ciąg znaków to {{Incode|"Solver Calculix Standard"}}, znajdziesz ten plik: {{FileName|src/Mod/Fem/femcommands/commands.py}}, i będziesz wiedział, że ten ciąg należy do środowiska pracy MES.
3.  Teraz poszukaj tego łańcucha na platformie Crowdin. Jeśli twoim językiem jest polski, odwiedź stronę <https://crowdin.com/project/freecad/pl>, przejdź do warsztatu MES i sprawdź, czy jest tam przetłumaczony.
4.  Istnieją dwie możliwości:
    1.  Łańcucha nie ma w Crowdin, ponieważ nie został on odebrany przez skrypt, który zbiera łańcuchy z kodu źródłowego FreeCAD i pakuje je do plików {{FileName|.ts}}. Mogą być tego dwie przyczyny:
        -   Łańcuch nie jest prawidłowo obsługiwany przez kod {{Incode|translate()}} *(lub {{Incode|QT_TRANSLATE_NOOP()}} kod dla specjalnych przypadków, takich jak nazwy poleceń)*, to znaczy, że istnieje problem, który musi być rozwiązany w kodzie źródłowym.
        -   Wszystko wydaje się normalne, ale skrypt zbierający ma problem z tym konkretnym ciągiem znaków, co może się zdarzyć, ponieważ ma wiele błędów.
    2.  Ciąg znajduje się na Crowdin. Istnieje więc kilka możliwości:
        -   Może być tak, że najnowsze ciągi Crowdin nie zostały jeszcze scalone. Możesz sprawdzić, czy tak jest, wyszukując ten ciąg *(patrz wyżej)* i sprawdzając, czy pojawia się on w przetłumaczonych plikach {{FileName|.ts}}. W naszym przykładzie {{Incode|"Solver Calculix Standard"}} znalazłby się w {{FileName|src/Mod/Fem/Gui/Resources/translations/Fem_pl.ts}}. Oznacza to, że przetłumaczony ciąg znaków znajduje się w źródle programu FreeCAD i wszystko powinno być w porządku w następnej kompilacji.
        -   Jeśli w następnej kompilacji nadal brakuje łańcucha, problem jest bardziej złożony i będziemy musieli trochę po debugować:
            1.  Sprawdź w pliku źródłowym, czy oryginalny ciąg znaków jest obsługiwany przez {{Incode|translate()}} lub {{Incode|QT_TRANSLATE_NOOP()}}.
            2.  Sprawdź, czy kontekst pasuje do tego, co jest na Crowdinie.
            3.  W przypadku {{Incode|QT_TRANSLATE_NOOP()}} istnieje kilka szczególnych przypadków. Dla poleceń, kontekstem musi być dokładna nazwa polecenia, taka sama jak użyta w {{Incode|FreeCADGui.runCommand()}}. Dla właściwości musi to być {{Incode|"App::Property"}}. Dla nazw menu i pasków narzędzi musi to być {{Incode|"Workbench"}}.


</div>

## Odnośniki internetowe 

-   [Lokalizacja - tłumaczenie interfejsu i dokumentacji](Localisation/pl.md)
-   [Skrypty środowiska Crowdin](Crowdin_Scripts/pl.md)
-   [Proces wydania](Release_process.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Administration](Category_Administration.md) > Crowdin Administration/pl
