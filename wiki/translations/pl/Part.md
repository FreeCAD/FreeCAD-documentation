# Part/pl
## Wprowadzenie


{{TOCright}}

W programie FreeCAD słowo \"[Część](Part/pl.md)\" jest zwykle używane w odniesieniu do typu obiektu <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Std: Część](Std_Part/pl.md) *(klasa `App::Part`)*, kontenera, który jest zdefiniowany przez system bazowy. Ta część jest używana do zarządzania pozycją kształtów 3D w celu tworzenia złożeń mechanicznych.

Zobacz stronę <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Std: Część](Std_Part/pl.md), aby uzyskać więcej informacji na temat tego typu obiektów.

## Użycie

Narzędzie Std: Część nie jest definiowane przez konkretne środowisko pracy, ale przez system bazowy, dlatego znajduje się w **pasku narzędzi struktury**, który jest dostępny we wszystkich [środowiskach pracy](Workbenches/pl.md).

1.  Naciśnij przycisk **[<img src=images/Std_Part.svg style="width:16px"> [Stwórz nową część](Std_Part/pl.md)**. Pusta część jest tworzona i automatycznie staje się ona *[aktywna](Std_Part/pl#Status_aktywno.C5.9Bci.md)*.

## Uwagi

W nieformalnym użyciu, \"Część\" może być dowolną figurą geometryczną, która jest widoczna w oknie [widoku 3D](3D_view/pl.md), a zatem jej pojęcie może być mylone z pojęciem \"[Zawartości](Body/pl.md)\" lub \"[Złożenia](Assembly/pl.md)\".

Jednakże, gdy wymagana jest większa precyzja, należy dokonać rozróżnienia.

-   \"[Zawartość](Body/pl.md)\" jest używana dla pojedynczych, ciągłych elementów, zazwyczaj tworzonych za pomocą środowisk [Część](Part_Workbench/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md).
    -   \"Bryła\" ma \"[Kształt](Shape/pl.md)\".
-   \"Część\" jest używana do grupowania pojedynczych \"Zawartości\" lub kilku z nich w celu utworzenia \"Złożenia\".
    -   \"Część\" posiada pewną strukturę \"[Kształtów](Shape/pl.md)\", ale nie posiada własnego \"Kształtu\".
-   \"Złożenie\" jest zbiorem \"Części\" ułożonych w jakiś sposób, ręcznie lub przy użyciu środowiska pracy.


{{Std Base navi

}} {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > Part/pl
