---
 GuiCommand:
   Name: Part Compound‏‎
   Name/pl: Część: Utwórz kształt złożony
   MenuLocation: Część , Złożenie , Utwórz kształt złożony
   Workbenches: Part_Workbench/pl
   Version: 0.14
   SeeAlso: Part_Fuse/pl, Part_CompoundFilter/pl, Part_ExplodeCompound/pl
---

# Part Compound/pl



## Opis

To polecenie tworzy złożenie obiektów o topologicznym kształcie, takich jak obiekty bryłowe oraz inne obiekty z powierzchniami i / lub krawędziami. Nie obsługuje siatek, ponieważ nie mają one kształtu topologicznego.



## Użycie

1.  Zaznacz w [widoku drzewa](Tree_view/pl.md) drzewa kształty topologiczne, które mają zostać dodane do złożenia,
2.  Wybierz z menu **Część → Złożenie → Utwórz kształt złożony** lub kliknij na przycisk <img alt="" src=images/Part_Compound.svg  style="width:24px;">



## Uwagi

Złożenie zawierające elementy, które przecinają się lub dotykają, jest **nieprawidłowy** dla operacji logicznych. Ze względu na problemy z wydajnością, sprawdzanie czy elementy się przecinają nie jest wykonywane domyślnie. Automatyczne sprawdzanie geometrii *(dostępne dla operacji logicznych)* jest również wyłączone dla operacji złożenia części.

Aby uaktywnić tę kontrolę, przejdź do **Narzędzia → Edycja Parametrów → Preferences... → Mod → Part → CheckGeometry → RunBOPCheck** i ustaw parametr na `true`.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Compound/pl
