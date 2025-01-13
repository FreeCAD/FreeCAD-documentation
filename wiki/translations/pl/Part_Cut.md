---
 GuiCommand:
   Name: Part Cut
   Name/pl: Część: Wytnij
   MenuLocation: Część , Operacje logiczne , Wytnij
   Workbenches: Part_Workbench/pl
   SeeAlso: Part_Boolean/pl, Part_Fuse/pl, Part_Common/pl
---

# Part Cut/pl



## Opis

Narzędzie <img alt="" src=images/Part_Cut.svg  style="width:24px;"> **Część: Wytnij** tnie *(odejmuje)* wybrane obiekty środowiska Część, przy czym ostatni jest odejmowany od pierwszego. Operacja ta jest w pełni parametryczna, a komponenty mogą być modyfikowane, a wynik przeliczany.

To narzędzie jest zautomatyzowaną formą <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Operacji na bryłach](Part_Boolean/pl.md).

<img alt="" src=images/Part_Cut_01.png  style="width:480px;">



## Użycie

1.  Wybierz dwa kształty,
2.  Istnieje kilka sposobów wywołania tego polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Cut.svg" width=16px> [Wytnij](Part_Cut/pl.md)**.
    -   Wybierz opcję **Część → Operacje logiczne → <img src="images/Part_Cut.svg" width=16px> Wytnij** z menu.



### Obsługiwane dane wejściowe 

Obiekty wejściowe muszą być kształtami [OpenCascade](OpenCASCADE/pl.md). Przykłady: obiekty wykonane z użyciem Środowisk pracy Część, Projekt części, Szkicownik. Dla siatek istnieją dedykowane narzędzia logiczne w środowisku pracy [Siatka](Mesh_Workbench/pl.md).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/pl
