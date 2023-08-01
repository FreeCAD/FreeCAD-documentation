# Addon/pl
## Wprowadzenie

W programie FreeCAD i w tej dokumentacji **Dodatek** to dowolny komponent, który nie jest częścią podstawowej instalacji, ale który można dodać do systemu za pomocą określonych metod.



## Różne rodzaje 

Istnieją trzy rodzaje dodatków:

-   [Makrodefinicje](Macros/pl.md): krótki wycinek kodu środowiska [Python](Python/pl.md), który dostarcza nowe narzędzie lub funkcjonalność w pojedynczym pliku o rozszerzeniu `.FCMacro`.
-   [Środowiska pracy](External_workbenches/pl.md): zbiory plików środowiska Python, które zapewniają powiązane [polecenia GUI](Gui_Command/pl.md) *(narzędzia)* skupione wokół konkretnego tematu, na przykład narzędzia do projektowania szafek, lub narzędzia do pracy z architekturą, lub narzędzia do projektowania łodzi, itp. Te środowiska zazwyczaj definiują nowe paski narzędzi, w których [polecenia](Gui_Command/pl.md) są umieszczone jako przyciski.
-   [Pakiety preferencji](Preference_Packs/pl.md): dystrybuowane zbiory preferencji użytkownika. {{Version/pl|0.20}}



## Instalacja

Zalecanym sposobem na instalację dodatków jest <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menedżer dodatków](Std_AddonMgr/pl.md).

Ale w przypadku makrodefinicji i środowisk pracy możliwa jest również instalacja ręczna:

-   [Jak zainstalować makrodefinicje](How_to_install_macros/pl.md)
-   [Instalacja większej ilości środowisk pracy](Installing_more_workbenches/pl.md)



## Informacja dla programistów 

Jeśli opracowałeś Środowisko pracy lub makrodefinicję i chcesz zobaczyć je w Menedżerze dodatków, przeczytaj jak to zrobić na stronach repozytorium: *([FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) i [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/))*. Jeśli dodasz swoje makro do strony [Przepisy na makropolecenia](Macros_recipes/pl.md), nie będziesz miał już nic innego do zrobienia, zostanie ono automatycznie przechwycone przez Menadżer dodatków.

Zobacz również:

-   [Dystrybucja środowiska pracy stworzonego w Python](Workbench_creation/pl#Dystrybucja.md).
-   [Dystrybucja środowiska pracy stworzonego w C++](Workbench_creation/pl#Dystrybucja_2.md).



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/pl
