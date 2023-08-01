---
- GuiCommand:
   Name:Part Cut
   Name/pl:Część: Wytnij
   MenuLocation:Część → Operacje logiczne → Wytnij
   Workbenches:[Part](Part_Workbench/pl.md)
   SeeAlso:[Operacja logiczna](Part_Boolean/pl.md), [Połączenie](Part_Fuse/pl.md), [Część wspólna](Part_Common/pl.md)
---

# Part Cut/pl



## Opis

Tnie *(odejmuje)* wybrane obiekty środowiska Część, przy czym ostatni jest odejmowany od pierwszego. Operacja ta jest w pełni parametryczna, a komponenty mogą być modyfikowane, a wynik przeliczany.

**Uwaga:** To polecenie jest zautomatyzowaną formą <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Operacji na bryłach](Part_Boolean/pl.md).

[480px\|left\|Cut](IMAGE:Part_Cut_01.png.md)



## Użycie

1.  Wybierz dwa kształty,
2.  Wywołaj polecenie **Wytnij** na kilka sposobów:
    -   Naciśnij przycisk **![](images/) '''Wytnij'''** na pasku narzędziowym Funkcje logiczne,
    -   Użyj pozycji z menu **Część → Funkcje logiczne → Wytnij**.



### Obsługiwane dane wejściowe 

Obiekty wejściowe muszą być kształtami [OpenCascade](OpenCASCADE/pl.md). Przykłady: obiekty wykonane z użyciem Środowisk pracy Część, Projekt części, Szkicownik. Dla siatek istnieją dedykowane narzędzia logiczne w środowisku pracy [Siatka](Mesh_Workbench/pl.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/pl
