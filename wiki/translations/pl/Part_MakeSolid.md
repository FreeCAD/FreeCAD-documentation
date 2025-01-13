---
 GuiCommand:
   Name: Part MakeSolid
   Name/pl: Część: Przekształć na bryłę
   MenuLocation: Część , Przekształć na bryłę
   Workbenches: Part_Workbench/pl
   SeeAlso: Part_ShapeFromMesh/pl
---

# Part MakeSolid/pl



## Opis

Polecenie <img alt="" src=images/Part_MakeSolid.svg  style="width:24px;"> **Przekształć na bryłę** tworzy bryły z obiektów kształtu.

To polecenie jest zwykle używane jako jeden z kroków do utworzenia bryły z siatki. Zobacz stronę [Utwórz kształt z siatki](Part_ShapeFromMesh/pl#Użycie.md) aby uzyskać więcej informacji.



## Użycie

1.  Wybierz jeden lub więcej obiektów kształtu.
2.  Wybierz z menu opcję **Część → <img src="images/Part_MakeSolid.svg" width=16px> Przekształć na bryłę**.
3.  Dla każdego wybranego obiektu, bryła zostanie utworzona jako osobny nowy obiekt.



## Uwagi

-   Nie zostanie przeprowadzona analiza ani walidacja obiektów kształtu.
-   Zaleca się użycie funkcji [Udoskonal kształt](Part_RefineShape/pl.md) przed konwersją na bryłę.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Tworzone są obiekty [Część: Cecha](Part_Feature/pl.md) bez dodatkowych właściwości.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part MakeSolid/pl
