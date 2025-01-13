---
 GuiCommand:
   Name: Part ReverseShape
   Name/pl: Część: Odwróć kształty
   MenuLocation: Część , Odwróć kształty
   Workbenches: Part_Workbench/pl
---

# Part ReverseShape/pl



## Opis

Polecenie <img alt="" src=images/Part_ReverseShape.svg  style="width:24px;"> **Odwróć kształty** tworzy parametryczne kopie z odwróconymi kierunkami normalnymi z wybranych obiektów.



## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Wybierz z menu opcję **Część → <img src="images/Part_ReverseShape.svg" width=16px> Odwróć kształty** z menu.
3.  Dla każdego wybranego obiektu zostanie utworzony odwrócony kształt.



## Uwagi

-   Obiekty [odniesienia](App_Link/pl.md) powiązane z odpowiednimi typami obiektów i kontenery środowiska [Część](App_Part/pl.md) z odpowiednimi widocznymi obiektami wewnątrz mogą być również używane jako obiekty źródłowe. {{Version/pl|0.20}}
-   Aby zobaczyć efekt polecenia, zmień właściwość {{PropertyView/pl|Oświetlenie}} odwróconego kształtu na {{Value|On side}} i w razie potrzeby zmień opcję **Edycja → Preferencje ... → Wyświetlanie → Widok 3D → Renderowanie → Kolor podświetlenia**.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Część: Odwróć kształty wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Reverse}}

-    **Source|Link**: określa powiązany kształt źródłowy.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ReverseShape/pl
