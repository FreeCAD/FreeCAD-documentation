---
- GuiCommand:
   Name:PartDesign Migrate
   Name/pl:Projekt Części: Przenieś ze starszej wersji
   MenuLocation:Projekt Części → Przenieś ze starszej wersji ...
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
---

# PartDesign Migrate/pl



## Opis

Środowisko pracy Projekt Części w FreeCAD v0.17 wprowadza nowe narzędzia i elementy, które nie są rozpoznawane przez starsze wersje FreeCAD {{VersionMinus/pl|0.16}}. Dokumenty FreeCAD utworzone w starszych wersjach mogą być nadal otwierane i edytowane. Aby skorzystać z nowych funkcji, należy je zmigrować za pomocą funkcji z menu **Projekt Części → Przenieś ze starszej wersji**.


{{Version/pl|0.17}}



## Użycie

1.  Otwórz dokument FreeCAD, który został utworzony za pomocą FreeCAD {{VersionMinus/pl|0.16}}.
2.  Przełącz się na środowisko pracy **<img src="images/Workbench_PartDesign.svg" width=16px> [Projekt Części](PartDesign_Workbench/pl.md)**.
3.  Przejdź do menu **Projekt Części → Przenieś ze starszej wersji**.
4.  Jeśli migracja się powiedzie, zostanie utworzony obiekt <img alt="" src=images/Std_Part.svg  style="width:24px;"> [kontener](Std_Part/pl.md), który będzie zawierał jedną lub więcej <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Zawartości](PartDesign_Body/pl.md), z których każda będzie zawierała łańcuch cech.



## Ograniczenia

-   Przed rozpoczęciem procesu migracji sprawdź, czy model został zbudowany z włączonymi opcjami automatycznego udoskonalania *(w menu **Edycja → Preferencje → Projekt Części → Ogólne**)* i odpowiednio ustaw swoje preferencje. Można to łatwo ustalić, sukcesywnie przełączając widoczność cech w drzewie modelu. Jeśli między elementami takimi jak Pads i Pockets nie pozostały żadne krawędzie, opcje automatycznego udoskonalania były wyłączone.
-   Jeśli migrowany dokument zawiera tylko szkice i elementy środowiska pracy Projekt Części, proces migracji może zakończyć się powodzeniem. Niektóre funkcje, takie jak fazki i zaokrąglenia, mogą wymagać przebudowy.
-   Jeśli migrowany dokument zawiera mieszany przepływ pracy w środowisku Część / Projekt Części, konwersja najprawdopodobniej zakończy się niepowodzeniem lub w najlepszym przypadku przyniesie nieoczekiwane rezultaty i będzie wymagać ręcznej migracji.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Migrate/pl
