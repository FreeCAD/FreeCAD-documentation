

## Funkcje

-   Tłumacz
    -   Możliwość proponowania i głosowania na tłumaczenie w danym języku.
    -   Poproś o więcej kontekstu, poproś o wyjaśnienie, zgłoś błędy w tłumaczonym tekście, zakwestionuj bieżący wpis w tłumaczeniu itd.

-   Korektor
    -   Zarządza tłumaczeniami, które tłumacze proponują i/lub nad którymi głosują. Korektor następnie akceptuje/odrzuca tłumaczenie.
    -   Dodatkowy krok jest potrzebny, aby ostatecznie zatwierdzić tłumaczenie. Ponieważ \"zatwierdzenie\" tłumaczenia wymaga ponownego przeczytania go i zaznaczenia, stanowi to rodzaj warstwy \"zapewnienia jakości\". Zatwierdzenie tłumaczenia powoduje zaznaczenie ciągu znaków na zielono i zwiększenie postępu na zielonym pasku stanu języka, który jest tłumaczony. Zielony pasek postępu może wskazywać na \"zdrowie\" tłumaczonego języka. Pozwala on również programistom na dodatkową elastyczność w łączeniu tłumaczeń, które zostały tylko zatwierdzone.
    -   Odpowiadaj na pytania tłumaczy w platformie Crowdin. Na przykład, jeśli potrzeba więcej kontekstu; lub jest błąd w łańcuchu, który ma być przetłumaczony, lub tłumaczenie, które zostało zaakceptowane lub zatwierdzone jest kwestionowane itp.
    -   Zgłaszanie deweloperom wszelkich istotnych problemów, które wymagają zmian w kodzie źródłowym itp.

### Filtrowanie ciągów znaków {#filtrowanie_ciągów_znaków}

<img alt="" src=images/Crowdin_Filter_Strings.png  style="width:300px;"> Filtrowanie ciągów znaków jest przydatną funkcją dla korektorów i menedżerów. Daje ona możliwość efektywnego sortowania wielu ciągów tłumaczeń, aby na przykład pokazać tylko te ciągi, które zostały oznaczone jako \"brak dodatkowych informacji kontekstowych\" lub \"nieprawidłowy ciąg źródłowy\". Ta usługa, którą tłumacze wykonują dla FreeCAD zapewnia dodatkową warstwę testowania jakości. Wiele literówek, problemów gramatycznych, a nawet błędów może zostać ujawnionych poprzez sprawdzanie tłumaczeń. I tak użytkownicy zaznaczają te problematyczne ciągi, abyśmy mogli na nie odpowiedzieć i ostatecznie je rozwiązać.

------------------------------------------------------------------------

### Skróty klawiaturowe {#skróty_klawiaturowe}

![](images/Crowdin_keyboard_shortcuts.png ) Korzystanie ze skrótów klawiaturowych to ważna wskazówka dotycząca oszczędności czasu i wydajności. Warto się jej nauczyć, jeśli jesteś tłumaczem, korektorem lub menedżerem. Listę skrótów klawiaturowych można wyświetlić, naciskając ikonę klawiatury w prawej górnej części interfejsu użytkownika programu Crowdin.

**Ważna uwaga:** Należy pamiętać, aby nie wprowadzać błędów do ciągów tłumaczeń, które powstały przez przypadkowe naciśnięcia klawiszy, które miały być skrótami klawiaturowymi.

#### Często używane skróty {#często_używane_skróty}

-   Kopiowanie tłumaczenia źródłowego: **Alt** + **C**
-   Zapisanie tłumaczenia: **Ctrl** + **Enter**
-   Zatwierdzenie tłumaczenia: **Alt** + **L** *(istotne dla korektorów tekstów)*

### Powiązane strony {#powiązane_strony}

-   [Lokalizacja - tłumaczenie interfejsu i dokumentacji](Localisation/pl.md)
-   [Skrypty środowiska Crowdin](Crowdin_Scripts.md)
-   [Proces wydania](Release_process.md)




[Category:Administration{{\#translation:}}](Category:Administration.md)
