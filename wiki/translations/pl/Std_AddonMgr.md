---
- GuiCommand:/pl
   Name:Std AddonMgr
   Name/pl:Std: AddonMgr
   MenuLocation:Narzędzia → Menadźer dodatków
   Workbenches:Wszystkie
   Version:0.17
   SeeAlso:[Zewnętrzne Środowiska pracy](External_workbenches/pl.md), [Makrodefinicje](Macros/pl.md)
---

# Std AddonMgr/pl

## Opis

Polecenie **Std: AddonMgr** otwiera Menadżer dodatków. Za jego pomocą możesz zainstalować i zarządzać [Zewnętrznymi Środowiskami pracy](external_workbenches/pl.md) oraz [makropoleceniami](macros/pl.md) dostarczonymi przez społeczność FreeCAD. Dostępne Środowiska pracy i makra są pobierane z dwóch repozytoriów, [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) i [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/), oraz ze strony [Przepisy na makropolecenia](Macros_recipes.md).

Dodatki oznaczone {{emphasis|Tylko Python 2}} nie będą działać we FreeCAD w wersji 0.19 lub nowszej.

Z powodu zmian na platformie GitHub w roku 2020 menedżer dodatków nie działa już, jeśli używasz FreeCAD w wersji 0.17 lub starszej. Musisz zaktualizować program do wersji [0.18.5](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) lub nowszej [0.19](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19_pre). Alternatywnie możesz zainstalować dodatki ręcznie, zobacz [uwagi](#Uwagi.md) poniżej.

![](images/Std_AddonMgr_dialog.png ) *Okienko dialogowe Menedżera dodatków*

## Użycie

1.  Wybierz opcję z menu **Narzędzia → <img src="images/Std_AddonMgr.svg" width=16px> Menedżer dodatków**.
2.  Jeśli używasz menedżera dodatków po raz pierwszy, zostanie otwarte okienko informacyjne z ostrzeżeniem, że rozszerzenia w menedżerze dodatków nie są oficjalnie częścią programu FreeCAD. Naciśnij przycisk **OK**, aby potwierdzić zapoznanie się z tą informacją i kontynuować.
3.  Otworzy się okno dialogowe Menadżer Dodatków. Więcej informacji znajdziesz w rozdziale [Opcje](#Opcje.md).
4.  Przycisk **<img src="images/Button_valid.svg" width=16px>Aktualizuj wszystko** nie działa w tym momencie.
5.  Naciśnij przycisk **<img src="images/Process-stop.svg" width=16px>Zamknij** , aby zamknąć okienko dialogowe.
6.  Jeżeli zainstalowałeś lub zaktualizowałeś Środowisko pracy, otworzy się nowe okno dialogowe informujące o konieczności ponownego uruchomienia programu FreeCAD, aby wprowadzone zmiany zaczęły funkcjonować.

## Opcje

Okno dialogowe Menadżer dodatków ma dwie zakładki po lewej stronie, jedna z nich zawiera listę dostępnych Środowisk pracy, a druga listę dostępnych makr. W panelu informacyjnym po prawej stronie zostanie wyświetlona strona główna wybranego dodatku.

### Odinstalowanie

1.  Wybierz zainstalowany dodatek w zakładce <img alt="" src=images/Folder.svg  style="width:16px;"> **Środowiska pracy** lub <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Makrodefinicje**.
2.  Naciśnij przycisk **<img src="images/Delete.svg" width=16px> Odinstaluj wybrane**.

### Instalacja / aktualizacja 

1.  Wybierz dodatek w zakładce <img alt="" src=images/Folder.svg  style="width:16px;"> **Środowiska pracy** lub <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Makrodefinicje**.
2.  Wciśnij przycisk **<img src="images/Edit_OK.svg" width=16px> Zainstaluj/zaktualizuj wybrane**.
3.  Jeśli chcesz dodać makropolecenie do niestandardowego paska narzędzi, nie zapomnij samodzielnie pobrać pliku z obrazem ikony, jeśli jest dostępny, klikając odnośnik na stronie głównej w panelu informacyjnym. Patrz [Dostosowanie interfejsu](Interface_Customization/pl#Paski_narzędzi.md).
4.  Aby zmienić położenie dodatkowego Środowiska pracy na liście [Wybór środowiska pracy](Interface_Customization/pl#Środowiska_pracy.md) można zapoznać się z informacjami w dokumencie [Dostosowanie interfejsu](Interface_Customization/pl#Środowiska_pracy.md).

### Konfiguracja

1.  Wciśnij przycisk **<img src="images/Preferences-general.svg" width=16px> Konfiguruj...
**
2.  Zostanie otworzone okienko dialogowe Menadżera dodatków.
3.  Opcjonalnie zaznacz pole wyboru {{CheckBox|TRUE|Automatyczne sprawdzaj aktualizacje podczas uruchomienia ''(wymaga GitPython)''}}.
4.  Opcjonalnie dodaj repozytoria do listy **Repozytoria użytkownika**. Dodatki z tych repozytoriów zostaną dodane na liście w zakładce <img alt="" src=images/Folder.svg  style="width:16px;"> **Środowiska pracy** lub <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Makrodefinicje**.
5.  Opcjonalnie wybierz ustawienia proxy.
6.  Wciśnij przycisk **OK** lub **Anuluj** aby zamknąć okno dialogowe.

## Uwagi

-   Korzystanie z dodatków nie jest ograniczone do wersji FreeCAD, w której zostały zainstalowane. Będziesz mógł również używać ich w każdej innej wersji programu, obsługiwanej przez dodatek, która może być zainstalowana w Twoim systemie.
-   Dodatki dostępne w menedżerze dodatków nie są częścią oficjalnego programu FreeCAD i nie są wspierane przez główny zespół programistów FreeCAD. Powinieneś uważnie przeczytać zamieszczone informacje, aby upewnić się, że wiesz, co instalujesz.
-   Zgłoszenia błędów i prośby o funkcje powinny być kierowane bezpośrednio do twórcy dodatku poprzez odwiedzenie wskazanej strony internetowej. Wielu twórców dodatków jest stałymi użytkownikami [forum FreeCAD](https://forum.freecadweb.org) i można się z nimi również tam kontaktować.
-   Jeśli pakiet [GitPython](https://github.com/gitpython-developers/GitPython) jest zainstalowany na Twoim komputerze, menedżer dodatków będzie z niego korzystał, dzięki czemu pobieranie będzie szybsze.
-   Możesz również zainstalować dodatki ręcznie. Zobacz artykuł [Jak zainstalować dodatkowe Środowiska pracy](How_to_install_additional_workbenches/pl.md) oraz [Jak zainstalować makrodefinicje](How_to_install_macros/pl.md).

## Informacja dla programistów 

Jeśli opracowałeś Środowisko pracy lub makrodefinicję i chcesz zobaczyć je w Menedżerze dodatków, przeczytaj jak to zrobić na stronach repozytorium: ([FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) i [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/)). Jeśli dodasz swoje makro do strony [Przepisy na makropolecenia](Macros_recipes/pl.md), nie będziesz miał już nic innego do zrobienia, zostanie ono automatycznie przechwycone przez Menadżer dodatków.

### Python i środowiska pracy 

Aby dodać swoje Środowisko pracy do menedżera dodatków, nie potrzebujesz żadnej konkretnej zgody, a będąc poza kodem źródłowym FreeCAD, możesz wybrać licencję, którą chcesz. Jeśli poprosisz o dodanie swojego Środowiska pracy do listy *(nie dodamy żadnego nowego stanowiska pracy bez prośby jego autorów)*, albo prosząc o to na forum, albo otwierając sprawę w repozytorium [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/), Twój kod pozostanie w Twoim własnym repozytorium git, po prostu dodamy go jako dodatkowy moduł do repozytorium [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/). Oczywiście, przed dodaniem twojego Środowiska pracy, przyjrzymy się mu i upewnimy się, że nie ma z nim nic potencjalnie problematycznego.

### C++ i środowiska pracy 

Jeśli tworzysz własne środowisko pracy w C++, nie może ono być uruchamiane bezpośrednio przez użytkowników i musi być najpierw skompilowane. Masz wtedy dwie opcje, albo sam dostarczysz prekompilowane wersje swojego Środowiska pracy, dla różnych systemów operacyjnych, albo powinieneś poprosić o połączenie swojego kodu z kodem źródłowym FreeCAD. W tym celu należy skorzystać z licencji LGPL *(lub w pełni kompatybilnej licencji jak MIT lub BSD)*, a nowe narzędzia należy przedstawić społeczności na forum [FreeCAD](https://forum.freecadweb.org) do wglądu. Po przetestowaniu i zatwierdzeniu kodu, powinieneś rozwidlić repozytorium FreeCAD, jeśli jeszcze tego nie zrobiłeś, stworzyć nową gałąź, wcisnąć do niej swój kod i otworzyć polecenie \"pull\", aby Twoja gałąź została połączona z głównym repozytorium.





{{Std Base navi

}}

---
[documentation index](../README.md) > Std AddonMgr/pl
