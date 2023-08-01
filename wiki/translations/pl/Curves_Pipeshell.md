---
- GuiCommand:/pl
   Name:Curves Pipeshell
   Name/pl:Krzywe: Powłoka rury
   MenuLocation:Powierzchnia → Powłoka rury
   Workbenches:[Krzywe](Curves_Workbench/pl.md)
---

# Curves Pipeshell/pl

## Opis

Narzędzie <img alt="" src=images/Curves_Pipeshell.svg  style="width:24px;"> [Powłoka rury](Curves_Pipeshell/pl.md) tworzy obiekt wyciągnięcia po ścieżce powłoki rury. To narzędzie jest częścią [środowisk zewnętrznych](External_workbenches/pl.md) o nazwie [Krzywe](Curves_Workbench/pl.md).

## Użycie

1.  Przełącz się na środowisko <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Krzywe](Curves_Workbench/pl.md) *(instalacja z <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) jest konieczna, jeśli nie zostało to zrobione wcześniej)*.
2.  Wybierz krawędź, która buduje ścieżkę wyciągania w oknie [widoku 3D](3D_view/pl.md).
3.  Wybierz jeden lub więcej wymaganych profili w [Widoku drzewa](Tree_view/pl.md).
4.  Aby wywołać polecenie, wykonaj jedną z poniższych czynności:
    -   Naciśnij przycisk <img alt="" src=images/Curves_Pipeshell.svg  style="width:24px;"> [Utwórz powłokę rury](Curves_Pipeshell/pl.md) na pasku narzędziowym
    -   Użyj polecenia **Powierzchnie → Powłoka rury**
5.  Zmień parametr `Powłoka rury` na odpowiednie wymagania.

## Właściwości

### Dane


{{Properties_Title|Podstawowe}}

-    **Umiejscowienie**: [Umiejscowienie](Placement/pl.md) to położenie i orientacja obiektu w przestrzeni.

-    **Etykieta**: Nazwa użytkownika obiektu w [Widoku drzewa](Tree_view/pl.md).


{{Properties_Title|Główne}}

-    **Tryb**: Domyślnie jest to **Frenet**. Tryb służy do wyboru algorytmu wyciągnięcia. Do wyboru: Frenet, DiscreteTrihedron, FixedTrihetron, Binormal, ShapeSupport, AuxiliarySpine.

-    **Wyjście**: Domyślnie jest to wartość **Powierzchnia**. Wyjście określa kształt obiektu. Do wyboru: Powierzchnia, Sekcje, Wyciągnięte sekcje.

-    **Profil**: Lista użytych profili.

-    **Spine**:


{{Properties_Title|Tryb}}

-    **Auxiliary**:

-    **Contact**:

-    **Corrected**:

-    **Direction**:

-    **Equi Curvi**:

-    **Location**:

-    **Support**:


{{Properties_Title|Ustawienia}}

-    **Max Degree**:

-    **Max Segments**:

-    **Samples**:

-    **Solid**: Wartość domyślna to **False**

-    **Tol3d**: Wartość domyślna to **0.00**.

-    **Tol Ang**: Wartość domyślna to **0.00**.

-    **Tol Bound**: Wartość domyślna to **0.00**.

## Uwagi

-    **Powłoka rury**wymaga obiektu polilinii *(jako ścieżki wyciągnięcia)* i przynajmniej jednego **profilu**.

-   Dwa narzędzia **Powłoka rury** i **Profil** działają razem jako \"Zaawansowane\" narzędzie Wyciągania.

## Ograniczenia

## Tworzenie skryptów 





{{Curves Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves Pipeshell/pl
