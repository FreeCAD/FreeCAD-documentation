# <img alt="Ikonka FreeCAD dla środowiska pracy Fcmcua" src=images/Fcmcua_wb.svg  style="width:64" height="64px;"> Fcmcua Workbench/pl






## Wprowadzenie

Fcmcua jest [zewnętrznym środowiskiem pracy](External_workbenches/pl.md), które jest używane do kontrolowania zespołu utworzonego w środowisku [Złożenie 4](Assembly4_Workbench/pl.md) z serwera [OPC UA](wikipedia_OPC_Unified_Architecture.md). Zapewnia to funkcjonalność symulacji maszyn sterowanych przez cyfrowe sterowniki takie jak [PLC](wikipedia_Programmable_logic_controller.md), o ile sterownik obsługuje OPC UA. Środowisko używa wartości dostarczonych przez serwer OPC UA do manipulowania Attachment Offset lokalnego układu współrzędnych *(LCS)* każdej części.



## Instalacja

Środowisko pracy **Fcmcua** można zainstalować za pomocą [Menadżera dodatków](Std_AddonMgr/pl.md).



## Użycie

Fcmcua udostępnia dwa typy mechanizmów do symulacji ruchu w modelu: **Oś** i **Siłownik**.

**Oś** jest kontrolowana przez wartości [zmiennoprzecinkowe](https://pl.wikipedia.org/wiki/Liczba_zmiennoprzecinkowa), które reprezentują pozycję osi lub prędkość silnika napędzającego oś.

**Siłownik** to dowolny ruch wyzwalany sygnałem binarnym. W takim przypadku Fcmcua sama symuluje ruch, obliczając wartości pozycji potrzebne do symulacji.

Dalsze instrukcje użytkowania można znaleźć na stronie [repozytorium Fcmcua](https://github.com/heissgetraenk/fcmcua).



### Połaczenia

<img alt="" src=images/Fcmcua_wb.svg  style="width:64px;">

Adres URL do serwera OPC UA musi być określony w postaci {{Incode|opc.tcp://127.0.0.1:4840}}.

Ustawienie częstotliwości odpytywania może być wykorzystane do ograniczenia czasu między aktualizacjami zespołu FreeCAD.

Stan połączenia jest wyświetlany na panelu połączenia.



### Ustawienia dla osi 

<img alt="" src=images/Fcmcua_axes.svg  style="width:64px;">

Węzeł osi na serwerze OPC UA reprezentuje jednowymiarową zmianę przesunięcia mocowania części w zespole. Aby skonfigurować to przypisanie, należy określić następujące informacje:

-   **Node Id:** Adres węzła serwera.
-   **Document Name:** Nazwa dokumentu części.
-   **LCS:** Etykieta lokalnego układu współrzędnych części.
-   **Offset:** Komponent wektorowy przesunięcia dołączenia, który zaktualizuje wartość węzła.
-   **Type:** Oś prędkości lub oś pozycyjna.

Wartość z serwera może być również odwrócona lub skalowana poprzez podanie znaku matematycznego i / lub współczynnika.



### Ustawienia dla siłownika 

<img alt="" src=images/Fcmcua_actuator.svg  style="width:64px;">

Węzeł siłownika na serwerze OPC UA działa jako wyzwalacz \"otwarcia\" lub \"zamknięcia\" siłownika. Aby skonfigurować siłownik, należy podać następujące informacje:

-   **Type :** Opisuje, ile sygnałów jest używanych do otwierania lub zamykania siłownika.
-   **Conditional Block:** Siłownik może mieć ogranicznik ruchu, aktywowany przez inny sygnał binarny. Ta funkcja jest opcjonalna.
-   **Node Ids:** W zależności od konfiguracji: adresy węzłów, które wyzwalają otwarcie / zamknięcie lub blok siłownika.
-   **Positions:** W zależności od konfiguracji: wartości odsunięcia dołączenia w modelu, które reprezentują pozycję otwarcia, zamknięcia lub zablokowania siłownika.
-   **Durations:** Czas, w którym siłownik otwiera się lub zamyka.



## Odnośniki internetowe 

-   [repozytorium Fcmcua](https://github.com/heissgetraenk/fcmcua)
-   [Zewnętrzne środowiska pracy](External_workbenches/pl.md)



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External%20Workbenches.md) > Fcmcua Workbench/pl
