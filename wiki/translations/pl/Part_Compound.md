---
- GuiCommand:/pl
   Name:Part Compound‏‎
   Name/pl:Część: Złożenie
   MenuLocation:Część → Złożenie
   Workbenches:[Część](Part_Workbench/pl.md)
   Version:0.14
   SeeAlso:[Suma](Part_Fuse/pl.md), [Filtr złożeń](Part_CompoundFilter/pl.md), [Rozbij złożenie](Part_ExplodeCompound/pl.md)
---

# Part Compound/pl

## Wprowadzenie

To polecenie tworzy połączenie dowolnego rodzaju kształtów topologicznych. Mogą to być bryły, siatki lub każdy inny rodzaj kształtów powierzchni.

Złożenie jest zbiorem kształtów zgrupowanych w jednym obiekcie.

## Użycie

1.  Zaznacz w [widoku drzewa](Tree_view/pl.md) drzewa kształty topologiczne, które mają zostać dodane do złożenia,
2.  Wybierz z menu **Część → Złożenie → Utwórz kształt złożony** lub kliknij na przycisk <img alt="" src=images/Part_Compound.svg  style="width:24px;">

## Uwagi

Złożenie zawierające elementy, które przecinają się lub dotykają, jest **nieprawidłowy** dla operacji logicznych. Ze względu na problemy z wydajnością, sprawdzanie czy elementy się przecinają nie jest wykonywane domyślnie. Automatyczne sprawdzanie geometrii *(dostępne dla operacji logicznych)* jest również wyłączone dla operacji złożenia części.

Aby uaktywnić tę kontrolę, przejdź do **Narzędzia → Edycja Parametrów → Preferences... → Mod → Part → CheckGeometry → RunBOPCheck** i ustaw parametr na `true`.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Compound/pl
