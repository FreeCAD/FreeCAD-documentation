# Part Boolean/pl
---
- GuiCommand:
   Name:Part Boolean
   Name/pl:Część: Operacja logiczna
   MenuLocation:Część - Operacje logiczne - Operacja logiczna ...
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Suma](Part_Fuse/pl.md), [Część wspólna](Part_Common/pl.md), [Wytnij](Part_Cut/pl.md), [Przecięcie](Part_Section/pl.md)---



## Opis

Narzędzie **[<img src=images/Part_Boolean.svg style="width:16px"> '''Operacja logiczna'''** jest ogólnym narzędziem logicznym wszystko w jednym. Pozwala ono na określenie obiektów i operacji do wykonania za pomocą jednego okna dialogowego.

Aby uzyskać szybszy dostęp do tych operacji, użyj **[<img src=images/Part_Fuse.svg style="width:16px"> [Połączenie](Part_Fuse/pl.md)**, **[<img src=images/Part_Common.svg style="width:16px"> [Część wspólna](Part_Common/pl.md)**, **[<img src=images/Part_Cut.svg style="width:16px"> [Wytnij](Part_Cut/pl.md)**, oraz **[<img src=images/Part_Section.svg style="width:16px"> [Przecięcie](Part_Section/pl.md)**.

![](images/PartBooleansDialog.png )



*Okno dialogowe do wyboru obiektów i wykonywania na nich operacji logicznych.*



## Jak używać 

Patrz poszczególne polecenia:

-    **<img src="images/Part_Cut.svg" width=16px> [Wytnij](Part_Cut/pl.md)
**
    

-    **<img src="images/Part_Fuse.svg" width=16px> [Połączenie](Part_Union/pl.md)
**
    

-    **<img src="images/Part_Common.svg" width=16px> [Część wspólna](Part_Common/pl.md)
**
    

-    **<img src="images/Part_Section.svg" width=16px> [Przecięcie](Part_Section/pl.md)
**
    

Patrz również menu **Część → Utwórz kopię → [Udoskonal kształt](Part_RefineShape/pl.md)**.



## Problemy współpłaszczyznowe 

Operacje typu logicznego są wykonywane przez wewnętrzne jądro geometrii, [technologię OpenCASCADE](OpenCASCADE.md) *(OCCT)*. Biblioteka ta czasami ma problemy z generowaniem wyników operacji logicznych, gdy obiekty wejściowe mają wspólne krawędzie lub powierzchnie. Aby być pewnym, że operacja logiczna zakończy się sukcesem, zaleca się, aby kształty przecinały się wyraźnie; oznacza to, że w większości przypadków jeden kształt powinien wystawać lub być większy od drugiego.

W przypadku współbieżności, nawet jeśli pierwsza operacja logiczna zakończy się sukcesem, kolejne operacje logiczne mogą zawieść. W tym przypadku, problem może nie występować w ostatniej wykonanej operacji, ale w poprzednich, czyli w zagnieżdżonych operacjach, jak wskazano w [widoku drzewa](tree_view/pl.md). Aby rozwiązać te problemy, zaleca się użycie **[<img src=images/Part_CheckGeometry.svg style="width:16px"> narzędzia [Part: sprawdź geometrie](Part_CheckGeometry/pl.md)** do sprawdzania wszystkich obiektów pod kątem problemów.

<img alt="" src=images/Part_Boolean_cut_coplanar_1.png  style="width:500px;">

<img alt="" src=images/Part_Boolean_cut_coplanar_2.png  style="width:500px;">



*Po lewej: kształty, które mają wspólną powierzchnię czołową, cięcie logiczne może dawać nieprawidłowe wyniki. <br> Po prawej: kształty, które przecinają się wyraźnie, cięcie logiczne będzie skuteczne w większości przypadków.*

<img alt="" src=images/Part_Boolean_fusion_coplanar_1.png  style="width:500px;">

<img alt="" src=images/Part_Boolean_fusion_coplanar_2.png  style="width:500px;">



*Po lewej: kształty, które mają wspólną powierzchnię, połączenie logiczne może dać nieprawidłowe wyniki. <br>Po prawej: kształty, które przecinają się wyraźnie, połączenie logiczne będzie skuteczne w większości przypadków.*



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Boolean/pl
