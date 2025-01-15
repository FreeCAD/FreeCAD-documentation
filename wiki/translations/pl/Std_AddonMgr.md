---
 GuiCommand:
   Name: Std AddonMgr
   Name/pl: Std: Menadżer dodatków
   MenuLocation: Przybory , Menadżer dodatków
   Workbenches: Wszystkie
   Version: 0.17
   SeeAlso: External_workbenches/pl, Macros/pl
---

# Std AddonMgr/pl



## Opis

Polecenie **Std: Menadżer dodatków** otwiera Menadżer dodatków. Za jego pomocą możesz zainstalować i zarządzać [Zewnętrznymi środowiskami pracy](External_workbenches/pl.md) oraz [makropoleceniami](Macros/pl.md) i [paczkami ustawień](Preference_Packs/pl.md) dostarczonymi przez społeczność FreeCAD. Domyślnie dostępne dodatki pobierane są z dwóch repozytoriów [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) oraz [Przepisy na makrodefinicje](Macros_recipes/pl.md). Jeśli w systemie zainstalowane są GitPython i Git, dodatkowe makra zostaną załadowane z [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/). Własne repozytoria można dodać w ustawieniach [Menadżera dodatków](Preferences_Editor/pl#Menad.C5.BCer_dodatk.C3.B3w.md).

Z powodu zmian na platformie GitHub w roku 2020 menedżer dodatków nie działa już, jeśli używasz FreeCAD w wersji 0.17 lub starszej. Musisz zaktualizować program do wersji [0.18.5](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) lub nowszej. Alternatywnie możesz zainstalować dodatki ręcznie, zobacz [uwagi](#Uwagi.md) poniżej.



## Użycie

1.  Wybierz opcję z menu **Przybory → <img src="images/Std_AddonMgr.svg" width=16px> Menedżer dodatków**.
2.  Jeśli używasz menedżera dodatków po raz pierwszy, zostanie otwarte okienko informacyjne z ostrzeżeniem, że rozszerzenia w menedżerze dodatków nie są oficjalnie częścią programu FreeCAD. Przedstawia on również kilka opcji związanych z wykorzystaniem danych przez menedżera dodatków. Dostosuj te opcje do swoich potrzeb i naciśnij przycisk **OK**, aby potwierdzić zapoznanie się z tą informacją i kontynuować.
3.  Otworzy się okno dialogowe Menadżer Dodatków. Więcej informacji znajdziesz w rozdziale [Opcje](#Opcje.md).
4.  Jeżeli zainstalowałeś lub zaktualizowałeś Środowisko pracy, otworzy się nowe okno dialogowe informujące o konieczności ponownego uruchomienia programu FreeCAD, aby wprowadzone zmiany zaczęły funkcjonować.



## Opcje

<img alt="" src=images/AddonManager_Main.png  style="width:600px;">

1.  Menedżer dodatków udostępnia dwa układy widoków: \"Zwięzły\" i \"Rozszerzony\". W widoku \"Zwięzłym\" każdy dodatek zajmuje jedną linię, a jego opis jest obcięty, aby zmieścić się w dostępnym miejscu. Z kolei \"Rozszerzony\" pokazuje dodatkowe szczegóły, w tym więcej tekstu opisu, a także informacje o opiekunie, więcej szczegółów instalacji itp.
2.  Obsługiwane są trzy różne typy dodatków: [środowiska pracy](External_workbenches/pl.md), [makrodefinicje](Macros/pl.md), oraz [pakiety preferencji](Preference_Packs/pl.md). Możesz zdecydować, czy chcesz wyświetlić tylko jeden typ, czy wszystkie na jednej liście.
3.  Lista może być zawężona do pokazania tylko zainstalowanych pakietów, tylko pakietów z dostępnymi aktualizacjami, lub tylko pakietów, które nie są jeszcze zainstalowane.
4.  Listę można filtrować, szukając słowa kluczowego w tytule, opisie i tagach *(opis i tagi muszą być określone przez twórcę dodatku w jego metadanych)*. Filtr może być nawet wyrażeniem regularnym, co pozwala na precyzyjną kontrolę dokładnego wyszukiwania.
5.  Rozszerzony widok pokazuje dostępne informacje o wersji, opisie, opiekunie i wersji instalacji dla pakietów, które dostarczają pliki [metadanych pakietu](Package_Metadata/pl.md) *(lub dla makrodefinicji z wbudowanymi metadanymi)*.
6.  Dane dodatków są buforowane lokalnie, ze zmienną częstotliwością aktualizacji pamięci podręcznej ustawioną w preferencjach użytkownika.
7.  W każdej chwili możesz wybrać ręczne aktualizowanie lokalnej pamięci podręcznej, aby zobaczyć najnowsze aktualizacje dostępne dla każdego dodatku.
8.  Sprawdzanie aktualizacji może być ustawione jako automatyczne lub wykonywane ręcznie poprzez kliknięcie przycisku *(skonfigurowane w preferencjach użytkownika)*. Jeśli środowiska GitPython i Git są zainstalowane w systemie, to informacje o aktualizacjach są pobierane przy użyciu Git. Jeśli nie, to informacje o aktualizacjach są uzyskiwane z dowolnego obecnego pliku metadanych.

Kliknięcie dodatku w tym widoku powoduje wyświetlenie strony szczegółów:

<img alt="" src=images/AddonManager_Details.png  style="width:600px;">

Na stronie szczegółów znajdują się przyciski umożliwiające instalację, odinstalowanie, aktualizację i tymczasowe wyłączenie dodatku. Dla zainstalowanych dodatków wyświetlana jest aktualnie zainstalowana wersja i data instalacji oraz informacja, czy jest to najnowsza dostępna wersja. Poniżej znajduje się osadzone okno przeglądarki internetowej pokazujące stronę README dodatku *(dla środowisk pracy i pakietów preferencji)* lub stronę Wiki *(dla makrodefinicji)*.



## Ustawienia

Preferencje dla menedżera dodatków można znaleźć w [Edytorze ustawień](Preferences_Editor/pl#Menad.C5.BCer_dodatk.C3.B3w.md). {{Version/pl|0.20}}



## Sortowanie według punktacji 


{{Version/pl|1.0}}

Menedżer dodatków obsługuje sortowanie według wielu różnych kryteriów. Większość z nich jest pobierana bezpośrednio z serwerów FreeCAD *(który buforuje je z GitHub i FreeCAD Wiki)*, ale jeden, \"Wynik\", nie jest w ogóle dostarczany przez FreeCAD i pojawia się jako opcja tylko wtedy, gdy ustawienie URL źródła wyniku jest podane w Preferencjach.

Źródło URL wyniku jest ścieżką do zdalnego dokumentu sformatowanego jako JSON, który zawiera listę dodatków oraz jakiegoś rodzaju \"wynik\". Wynik może być obliczany w dowolny sposób, według upodobania dostawcy danych, ale powinien być wartością całkowitą, gdzie wyższe wyniki są w pewnym sensie \"lepsze\". Każdy dodatek, który nie jest wymieniony, jest wewnętrznie przypisywany wynik zero. Format pliku to pojedynczy słownik JSON, gdzie klucz to URL dodatku *(dla warsztatów roboczych i pakietów preferencji)* lub nazwa makrodefinicji *(dla makr)*. Zobacz [to źródło danych](https://gist.githubusercontent.com/chennes/e8f60e80f16e6ffbd057dd47ca36ad2a/raw/7b118cca8e84444c3379919bbd744b99e6ef6711/addon_score_for_testing.json) dla przykładu *(zauważ, że wynik tam jest po prostu długością opisu dodatku i jest przeznaczony tylko do testów i celów demonstracyjnych)*.



## Uwagi

-   Korzystanie z dodatków nie jest ograniczone do wersji FreeCAD, w której zostały zainstalowane. Będziesz mógł również używać ich w każdej innej wersji programu, obsługiwanej przez dodatek, która może być zainstalowana w Twoim systemie.
-   Dodatki dostępne w menedżerze dodatków nie są częścią oficjalnego programu FreeCAD i nie są wspierane przez główny zespół programistów FreeCAD. Powinieneś uważnie przeczytać zamieszczone informacje, aby upewnić się, że wiesz, co instalujesz.
-   Zgłoszenia błędów i prośby o funkcje powinny być kierowane bezpośrednio do twórcy dodatku poprzez odwiedzenie wskazanej strony internetowej. Wielu twórców dodatków jest stałymi użytkownikami [forum FreeCAD](https://forum.freecadweb.org) i można się z nimi również tam kontaktować.
-   Jeśli pakiet [GitPython](https://github.com/gitpython-developers/GitPython) jest zainstalowany na Twoim komputerze, menedżer dodatków będzie z niego korzystał, dzięki czemu pobieranie będzie szybsze.
-   Możesz również zainstalować dodatki ręcznie. Zobacz artykuł [Jak zainstalować dodatkowe Środowiska pracy](How_to_install_additional_workbenches/pl.md) oraz [Jak zainstalować makrodefinicje](How_to_install_macros/pl.md).



## Informacje dla twórców dodatków 

Zobacz również informacje o [dodatkach](Addon/pl#Informacja_dla_programist.C3.B3w.md).



## Tworzenie skryptów 


{{Version/pl|0.21}}

Niektóre funkcje menedżera dodatków są zaprojektowane tak, aby dostęp do nich był możliwy poprzez API Python programu FreeCAD. W szczególności dodatek może być instalowany, aktualizowany i usuwany za pomocą interfejsu środowiska Python. Większość zastosowań tego API wymaga utworzenia obiektu z co najmniej trzema atrybutami: {{Incode|name}}, {{Incode|branch}} i {{Incode|url}}. Na przykład:


```python
class MyAddonClass:
    def __init__(self):
        self.name = "TestAddon"
        self.url = "https://github.com/Me/MyTestAddon"
        self.branch = "main"
my_addon = MyAddonClass()
```

nasz obiekt {{Incode|my_addon}} jest teraz gotowy do użycia z API Menedżera addonów.



### Użycie z wiersza poleceń (nie-GUI) 

Jeśli twój kod musi zainstalować lub zaktualizować dodatek synchronicznie *(np. bez GUI)*, kod może być bardzo prosty:


```python
from addonmanager_installer import AddonInstaller
installer = AddonInstaller(my_addon)
installer.run()
```

Zauważ, że ten kod blokuje się do momentu zakończenia, więc nie powinieneś go uruchamiać na głównym wątku GUI. Dla menedżera dodatków, \"install\" i \"update\" są tym samym wywołaniem: jeśli ten dodatek jest już zainstalowany, a Git jest dostępny, zostanie zaktualizowany poprzez \"Git pull\". Jeśli nie jest zainstalowany lub został zainstalowany za pomocą metody instalacji innej niż Git, zostanie pobrany od zera *(przy użyciu Git, jeśli jest dostępny)*.

Aby odinstalować, należy użyć:


```python
from addonmanager_uninstaller import AddonUninstaller
uninstaller = AddonUninstaller(my_addon)
uninstaller.run()
```



### Użycie z GUI 

Jeśli planujesz uruchomić swój kod w GUI, lub wspierać go w pełnej wersji FreeCAD, najlepiej jest uruchomić swoją instalację w oddzielnym wątku bez GUI, aby GUI pozostał responsywny. Aby to zrobić, najpierw sprawdź, czy GUI jest uruchomione, a jeśli tak, utwórz {{Incode|QThread}} *(nie próbuj tworzyć {{Incode|QThread}}, jeśli GUI nie jest uruchomione: wymagają one aktywnej pętli zdarzeń, aby działać)*.


```python
from PySide import QtCore
from addonmanager_installer import AddonInstaller

worker_thread = QtCore.QThread()
installer = AddonInstaller(my_addon)
installer.moveToThread(worker_thread)
installer.success.connect(installation_succeeded)
installer.failure.connect(installation_failed)
installer.finished.connect(worker_thread.quit)
worker_thread.started.connect(installer.run)
worker_thread.start() # Returns immediately
```

Następnie zdefiniuj funkcje {{Incode|installation_succeeded}} i {{Incode|installation_failed}}, które mają być uruchamiane w każdym przypadku. Do deinstalacji możesz użyć tej samej techniki, choć zwykle jest ona znacznie szybsza i nie zablokuje GUI na bardzo długo, więc generalnie bezpiecznie jest użyć deinstalatora bezpośrednio, jak pokazano powyżej.



---
⏵ [documentation index](../README.md) > Std AddonMgr/pl
