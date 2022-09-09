---
- GuiCommand   */pl
   Name   *Std AddonMgr
   Name/pl   *Std   * Menadżer dodatków
   MenuLocation   *Przybory → Menadżer dodatków
   Workbenches   *Wszystkie
   Version   *0.17
   SeeAlso   *[Zewnętrzne środowiska pracy](External_workbenches/pl.md), [Makrodefinicje](Macros/pl.md)
---

# Std AddonMgr/pl

## Opis


<div class="mw-translate-fuzzy">

Polecenie **Std   * Menadżer dodatków** otwiera Menadżer dodatków. Za jego pomocą możesz zainstalować i zarządzać [Zewnętrznymi środowiskami pracy](External_workbenches/pl.md) oraz [makropoleceniami](Macros/pl.md) dostarczonymi przez społeczność FreeCAD. Dostępne Środowiska pracy i makra są pobierane z dwóch repozytoriów, [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) i [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/), oraz ze strony [Przepisy na makropolecenia](Macros_recipes/pl.md).


</div>


<div class="mw-translate-fuzzy">

Z powodu zmian na platformie GitHub w roku 2020 menedżer dodatków nie działa już, jeśli używasz FreeCAD w wersji 0.17 lub starszej. Musisz zaktualizować program do wersji [0.18.5](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) lub nowszej [0.19](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.19_pre). Alternatywnie możesz zainstalować dodatki ręcznie, zobacz [uwagi](#Uwagi.md) poniżej.


</div>

## Użycie


<div class="mw-translate-fuzzy">

1.  Wybierz opcję z menu **Przybory → <img src="images/Std_AddonMgr.svg" width=16px> Menedżer dodatków**.
2.  Jeśli używasz menedżera dodatków po raz pierwszy, zostanie otwarte okienko informacyjne z ostrzeżeniem, że rozszerzenia w menedżerze dodatków nie są oficjalnie częścią programu FreeCAD. Naciśnij przycisk **OK**, aby potwierdzić zapoznanie się z tą informacją i kontynuować.
3.  Otworzy się okno dialogowe Menadżer Dodatków. Więcej informacji znajdziesz w rozdziale [Opcje](#Opcje.md).
4.  Przycisk **<img src="images/Button_valid.svg" width=16px>Aktualizuj wszystko** nie działa w tym momencie.
5.  Naciśnij przycisk **<img src="images/Process-stop.svg" width=16px>Zamknij** , aby zamknąć okienko dialogowe.
6.  Jeżeli zainstalowałeś lub zaktualizowałeś Środowisko pracy, otworzy się nowe okno dialogowe informujące o konieczności ponownego uruchomienia programu FreeCAD, aby wprowadzone zmiany zaczęły funkcjonować.


</div>

## Opcje

<img alt="" src=images/AddonManager_Main.png  style="width   *600px;">

1.  The Addon manager provides two view layouts   * \"Condensed\" and \"Expanded\". In \"Condensed\" view, each addon takes a single line, and its description is truncated to fit the available space. \"Expanded\" shows additional details, including more of the description text as well as maintainer information, more installation details, etc.
2.  Three different types of addons are supported   * [workbenches](external_workbenches.md), [macros](macros.md), and [preference packs](Preference_Packs.md). You can choose to show just one type, or all of them in a single list.
3.  The list can be limited to show just installed packages, just packages with available updates, or just packages that are not yet installed.
4.  The list can be filtered, searching for a keyword in the title, description, and tags (description and tags must be specified by the addon developer in their addon\'s metadata). The filter can even be a regular expression, for fine-grained control of the exact search term.
5.  The expanded view shows available version information, description, maintainer information, and installation version information, for packages that provide a [package metadata](Package_Metadata.md) file (or for macros with embedded metadata).
6.  Addon data is cached locally, with a variable cache update frequency set in the user preferences.
7.  At any time you can choose to manually update your local cache to see the latest updates available for each addon.
8.  Update checks may be set up to be automatic, or done manually via a button click (configured in user preferences). If GitPython and git are installed on your system then update information is fetched using git. If not, then update information is obtained from any present metadata file.

Clicking on an addon in this view brings up the addon\'s Details page   *

<img alt="" src=images/AddonManager_Details.png  style="width   *600px;">

The details page shows buttons allowing installing, uninstalling, updating, and temporarily disabling an addon. For installed addons it lists the currently installed version and the installation date, and whether that is the most recent version available. Below is an embedded web browser window showing the addon\'s README page (for workbenches and preference packs), or Wiki page (for macros).

## Preferences

The preferences for the Addon manager can be found in the [Preferences Editor](Preferences_Editor#Addon_Manager.md). <small>(v0.20)</small> 

## Uwagi


<div class="mw-translate-fuzzy">

-   Korzystanie z dodatków nie jest ograniczone do wersji FreeCAD, w której zostały zainstalowane. Będziesz mógł również używać ich w każdej innej wersji programu, obsługiwanej przez dodatek, która może być zainstalowana w Twoim systemie.
-   Dodatki dostępne w menedżerze dodatków nie są częścią oficjalnego programu FreeCAD i nie są wspierane przez główny zespół programistów FreeCAD. Powinieneś uważnie przeczytać zamieszczone informacje, aby upewnić się, że wiesz, co instalujesz.
-   Zgłoszenia błędów i prośby o funkcje powinny być kierowane bezpośrednio do twórcy dodatku poprzez odwiedzenie wskazanej strony internetowej. Wielu twórców dodatków jest stałymi użytkownikami [forum FreeCAD](https   *//forum.freecadweb.org) i można się z nimi również tam kontaktować.
-   Jeśli pakiet [GitPython](https   *//github.com/gitpython-developers/GitPython) jest zainstalowany na Twoim komputerze, menedżer dodatków będzie z niego korzystał, dzięki czemu pobieranie będzie szybsze.
-   Możesz również zainstalować dodatki ręcznie. Zobacz artykuł [Jak zainstalować dodatkowe Środowiska pracy](How_to_install_additional_workbenches/pl.md) oraz [Jak zainstalować makrodefinicje](How_to_install_macros/pl.md).


</div>

## Informacja dla programistów 

See [Addon](Addon#Information_for_developers.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std AddonMgr/pl
