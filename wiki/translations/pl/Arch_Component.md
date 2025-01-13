---
 GuiCommand:
   Name: Arch Component
   Name/pl: Architektura: Komponent‎‏‎
   MenuLocation: 3D/BIM , Narzędzia ogólne 3D , Komponent‎‏‎
   Workbenches: BIM_Workbench/pl
   Shortcut: **C** **M**
---

# Arch Component/pl



## Opis

Tworzy nieparametryczny komponent [BIM](BIM_Workbench/pl.md) z dowolnego obiektu opartego na [Części](Part_Workbench/pl.md). Daje to obiektowi opartemu na części te same atrybuty i właściwości co innym obiektom Architektury i pozwala określić, w jaki sposób powinien być eksportowany do IFC poprzez ustawienie jego właściwości **Typ IFC**.



## Użycie

1.  Wybierz obiekt oparty na [Części](Part_Workbench/pl.md).
2.  Istnieje kilka sposobów wywołania polecenia:
    -   Naciśnij przycisk **<img src="images/Arch_Component.svg" width=16px> Komponent**.
    -   Wybierz z menu opcję **3D/BIM → Narzędzia ogólne 3D → <img src="images/Arch_Component.svg" width=16px> Komponent**.
    -   Użyj skrótu klawiaturowego: **C**, a następnie **M**.



## Właściwości

Obiekt komponent Architektury jest również bazą współdzieloną przez wszystkie inne obiekty Architektury *([ścina](Arch_Wall/pl.md), [konstrukcja](Arch_Structure/pl.md) itd.)* Dlatego niektóre z jego właściwości i zachowań są wspólne dla wszystkich obiektów Architektury *(z wyjątkiem narzędzi, które nie tworzą obiektów bryłowych, takich jak [Płaszczyzna przekroju](Arch_SectionPlane/pl.md) lub [Osie](Arch_Axis/pl.md))*.



### Dane


{{TitleProperty|Komponent}}

-    **Dodatki|LinkList**: Komponenty architektury mają właściwość obiektu dodanego, która może zawierać odniesienie do dowolnej liczby innych obiektów opartych na [kształcie](Part_Workbench/pl.md). Kształt tych dodatków zostanie połączony z podstawowym kształtem komponentu, aby uzyskać ostateczny kształt. Zobacz akapit [Uwagi](#Uwagi.md)

-    **Oś|Link**: An optional axis or axis system on which this object should be duplicated.

-    **Kształt bazowy|Link**: Komponenty architektury są zawsze oparte na obiekcie bazowym [kształtu](Part_Workbench/pl.md). Niektóre typy obiektów będą po prostu używać kształtu bazowego, inne *(na przykład <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [ściana](Arch_Wall/pl.md))* wykonają na nim dodatkowe operacje, takie jak wyciągnięcie. W przypadku niektórych typów, posiadanie obiektu bazowego nie jest obowiązkowe *(<img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [konstrukcja](Arch_Structure/pl.md))*.

-    **Klon z|Link**: Każdy komponent Architektury może być klonem innego komponentu Architektury tego samego typu *(Ściana może być tylko klonem innej Ściany, itd.)*. Jedynym wyjątkiem jest generyczny komponent architektury *(generowany przez to polecenie)*, który może być klonem dowolnego innego typu *(ściana, struktura, okno itp.)*. Pozwala to na użycie generycznego komponentu Architektury do nadpisania typu innego komponentu.

-    **Wysoka rozdzielczość|Link**: Komponenty Architektury mogą używać kształtu innego obiektu jako wersji o wyższej rozdzielczości. W tym celu należy ustawić zarówno właściwość Wysoka rozdzielczość, jak i tryb wyświetlania Wysokiej rozdzielczości. Pozwala to na przykład na stworzenie prostej ściany, a następnie wymodelowanie każdej cegły, która ją tworzy, na przykład za pomocą [Sześcian](Part_Box/pl.md). Następnie użyj złożenia tych cegieł jako wersji ściany w wysokiej rozdzielczości. Kształt ściany nie jest modyfikowany przez dodanie obiektu wysokiej rozdzielczości. Zmieni się tylko jego reprezentacja w oknie [widoku 3D](3D_view/pl.md), przyjmując reprezentację wersji wysokiej rozdzielczości zamiast własnej.

-    **Obszar poziomy|Area**: Obszar rzutu tego obiektu na płaszczyznę XY *(tylko do odczytu)*.

-    **Materiał|Link**: Wszystkie komponenty Architektury posiadają miejsce na materiał, który może zawierać [Material](Arch_SetMaterial/pl.md) lub [Materiał wielowarstwowy](Arch_MultiMaterial/pl.md) *(nie wszystkie typy obiektów Architektury wspierają użycie [Materiału wielowarstwowego](Arch_MultiMaterial/pl.md))*. Właściwości Rozproszony kolor i Przezroczystość dołączonego materiału zdefiniują kolor kształtu i przezroczystość komponentu Architektury. Materiał będzie importowany i eksportowany do [IFC](Arch_IFC/pl.md), [OBJ](Arch_OBJ/pl.md) i [DAE](Arch_DAE/pl.md).

-    **Przesuń bazę|Bool**: Określa, czy przeniesienie tego obiektu spowoduje przeniesienie jego podstawy.

-    **Przesuń z obiektem nadrzędnym|Bool**: Gdy komponent jest osadzony wewnątrz innego *(na przykład okno wewnątrz ściany)*, ustawienie tej właściwości na {{True/pl}} sprawi, że obiekt przesunie się i obróci razem, gdy jego obiekt nadrzędny zostanie przesunięty lub obrócony za pomocą narzędzi [Przesuń](Draft_Move/pl.md) lub [Obróć](Draft_Rotate/pl.md).

-    **Długość obwodu|Length**: Długość obwodu obszaru poziomego *(tylko do odczytu)*.

-    **Kod standardowy|String**: Opcjonalny kod standardowy *(OmniClass itp.)* dla tego komponentu.

-    **Odjęcia|LinkList**: Komponenty architektury mają właściwość obiektu odjęcia, która może zawierać odniesienie do dowolnej liczby innych obiektów opartych na [kształcie](Part_Workbench/pl.md). Kształt tych obiektów zostanie odjęty od bazowego kształtu komponentu, aby uzyskać ostateczny kształt. Zobacz akapit [Uwagi](#Uwagi.md).

-    **Obszar pionowy|Area**: Obszar wszystkich pionowych powierzchni tego obiektu *(tylko do odczytu)*.


{{TitleProperty|IFC}}

-    **Dane IFC|Map|Hidden**:

-    **Właściwości IFC|Map|Hidden**:

-    **Typ IFC|Enumeration**: Każdy komponent architektury, oprócz funkcji zdefiniowanej przez jego typ *(ściana, okno itp.)*, posiada również właściwość Rola, która może dodatkowo definiować rodzaj pełnionej przez niego funkcji. Na przykład [konstrukcja](Arch_Structure/pl.md) może pełnić rolę belki lub słupa. Generyczne komponenty Architektury *(generowane przez to polecenie)* mogą mieć dowolną rolę dostępną w całym środowisku roboczym Architektury. Rola jest używana do definiowania typu obiektu IFC, który ma zostać wyeksportowany podczas [eksport do IFC](Arch_IFC/pl.md).


{{TitleProperty|Atrybuty IFC}}

-    **Opis|String**: Wszystkie komponenty Architektury mają pole Opis, które może zawierać dowolny tekst. Jest ono używane podczas [eksportu do IFC](Arch_IFC/pl.md).

-    **Id Globalny|String**:

-    **Typ Obiektu|String**:

-    **Typ predefiniowany|Enumeration**:

-    **Tag|Enumeration**: Właściwość Tag jest kolejnym polem tekstowym, które może być użyte do nadania dodatkowej niestandardowej tożsamości obiektom.



## Uwagi

-   Umieszczenie komponentu archiektury jest stosowane po wykonaniu dodawania i odejmowania, więc są one wykonywane względem obiektu bazowego w jego lokalizacji bazowej. Następnie wynik jest przenoszony do lokalizacji Umiejscowienia.

-   Obiekty mogą być dodawane lub usuwane z list dodawania i odejmowania komponentów poprzez zaznaczenie zarówno obiektu, jak i komponentu, a następnie użycie przycisku [Połącz obiekty](Arch_Add/pl.md) lub [Usuń komponent](Arch_Remove/pl.md) lub z panelu zadań poprzez dwukrotne kliknięcie komponentu w [Widoku drzewa](Tree_view/pl.md). Panel zadań pozwala również sprawdzić, który obiekt jest aktualnie częścią tych list.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Component/pl
