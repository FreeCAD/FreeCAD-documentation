---
- GuiCommand:/pl
   Name:Part Cut
   Name/pl:Częśc: Wytnij
   MenuLocation:Część → Logiczne → Wytnij
   Workbenches:[Part](Part_Workbench/pl.md)
   SeeAlso:_, [Part: Common](Part_Common/pl.md)
---

# Part Cut/pl

## Opis

Tnie *(odejmuje)* wybrane obiekty typu Część, przy czym ostatni jest odejmowany od pierwszego. Operacja ta jest w pełni parametryczna, a komponenty mogą być modyfikowane, a wynik przeliczany.

**Uwaga:** To polecenie jest zautomatyzowaną formą <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Operacji na bryłach](Part_Boolean/pl.md).

_

## Użycie

1.  Wybierz dwa kształty,
2.  Wywołaj polecenie **Wytnij** na kilka sposobów:
    -   Naciśnij przycisk **![](images/) '''Wytnij'''** na pasku narzędziowym Funkcje logiczne,
    -   Użyj pozycji z menu **Część → Funkcje logiczne → Wytnij**.

### Obsługiwane dane wejściowe 

Obiekty wejściowe muszą być kształtami [OpenCascade](OpenCASCADE/pl.md). Przykłady: obiekty wykonane z użyciem Środowisk pracy Część, Projekt części, Szkicownik. Nie mogą to być siatki *(chyba że zostały zamienione na kształty)* - dla siatek, w środowisku pracy Siatka istnieją specyficzne narzędzia do przeprowadzania operacji logicznych.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/pl
