---
- GuiCommand:/pl
   Name:Part Sphere
   Name/pl:Part: Kula
   MenuLocation:Część → Bryła pierwotna → Kula
   Workbenches:[Part](Part_Workbench/pl.md)
   SeeAlso:[Bryły pierwotne](Part_CreatePrimitives/pl.md)
---

# Part Sphere/pl

## Opis

Tworzy prostą parametryczną sferę o parametrach położenie, kąt1, kąt2, kąt3 i promień.

<img alt="" src=images/SimpleSphere.jpg  style="width:400px;">

## Użycie

1.  Przełącz się na środowisko pracy <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Część](Part_Workbench/pl.md)
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Sphere.svg" width=16px> Utwórz sferę** na pasku narzędzi.
    -   Wybierz polecenie **Część → Bryła pierwotna → <img src="images/Part_Sphere.svg" width=16px> Sfera** z paska menu.

**Wynik:** Sfera zostanie umieszczona w odniesieniu położenia (punkt 0,0,0) podczas tworzenia. Parametry kąta pozwalają na utworzenie części sfery zamiast pełnej sfery *(domyślnie są ustawione na 360°)*.

Właściwości obiektu mogą być później korygowane w [edytorze właściwości](Property_editor/pl.md) lub przez podwójne kliknięcie na obiekcie w [Widoku drzewa](Tree_view/pl.md).

## Właściwości

### Dane


{{TitleProperty|Kula}}

-    {{PropertyData/pl|Promień:}}Promień sfery

-    {{PropertyData/pl|Kąt 1:}}wartość pierwszego kąta do cięcia / definiowania sfery

-    {{PropertyData/pl|Kąt 2:}}wartość drugiego kąta do cięcia / definiowania sfery

-    {{PropertyData/pl|Kąt 3:}}wartość trzeciego kąta do cięcia / definiowania sfery

Ponieważ dość trudno jest wyjaśnić znaczenie parametrów kąt 1, kąt 2, kąt 3, poniższy rysunek obrazuje zastosowanie tych parametrów o wartościach: kąt 1 = -45°, kąt 2 = 45° i kąt 3 = 90°.

<img alt="" src=images/SphereCutThreeAngles.jpg  style="width:400px;">

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sphere/pl
