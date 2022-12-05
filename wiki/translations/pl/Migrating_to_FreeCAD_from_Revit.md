# Migrating to FreeCAD from Revit/pl
Ta strona ma na celu umożliwienie szybkiego rozpoczęcia pracy z programem FreeCAD, jeśli wcześniej korzystałeś z programu Autodesk Revit.

### Konfiguracja

FreeCAD jest wielofunkcyjną aplikacją do modelowania 3D. Chociaż nie jest to wyłącznie aplikacja BIM, posiada dwa dedykowane jej środowiska pracy: [Architektura](Arch_Workbench/pl.md), które jest dołączone do każdej instalacji programu FreeCAD i zawiera minimalny zestaw narzędzi BIM, oraz [BIM](BIM_Workbench/pl.md), które należy zainstalować za pomocą [Mendżera dodatków](Std_AddonMgr/pl.md). Zaleca się rozpoczęcie od zainstalowania pakietu BIM, który pozwoli uzyskać środowisko bardziej zbliżone do środowiska Revit.

### Kluczowe pojęcia 

Mimo że użytkownik będzie mógł wykonywać te same zadania i uzyskiwać podobne wyniki, jak w programie Revit, oba programy różnią się od siebie i należy poznać różnice między nimi.

-   Format plików Revit *(.RVT)* jest prawnie zastrzeżony, nieudokumentowany i nie jest obsługiwany przez FreeCAD *(jego obsługa byłaby gigantycznym zadaniem, które pochłonęłoby wszystkie zasoby programu FreeCAD, dając bardzo niekompletny rezultat)*. Zamiast tego należy polegać na otwartych formatach, takich jak [IFC](Arch_IFC.md), który jest dość dobrze obsługiwany przez obie aplikacje. Ponadto możliwe jest eksportowanie do formatu ACIS/SAT, który jest obsługiwany przez dodatek InventorLoader, instalowany za pomocą [Menadżera dodatków](Std_AddonMgr/pl.md).

-   Zasoby BIM, takie jak okna, wyposażenie czy meble, można zazwyczaj łatwo znaleźć na popularnych stronach internetowych, takich jak [bimobject.com](https://bimobject.com), w formacie IFC. Jednak format ten nie zawsze gwarantuje odpowiednią jakość geometrii. Na stronie [grabcad library](https://grabcad.com/library?softwares=step-slash-iges) znajduje się spory wybór zasobów do pobrania w formacie STEP o dobrej jakości geometrii.

-   W programie FreeCAD nie istnieje pojęcie rodziny. Istnieje jednak wiele sposobów na uzyskanie tego samego rezultatu, czyli kilku obiektów, które mają te same właściwości i są ze sobą powiązane *(jeśli zmodyfikujesz jeden z nich, zmodyfikujesz wszystkie)*. Najprostszym z nich jest [klonowanie](Draft_Clone/pl.md). Klon jest jak kopia obiektu, ale jeśli zmodyfikujesz oryginalny obiekt, jego klony również zostaną zaktualizowane. Istnieją jednak inne, bardziej subtelne sposoby, aby obiekty miały wspólne właściwości. Można na przykład narysować profil 2D i z tego samego profilu 2D zbudować kilka obiektów.

-   Chociaż może to być wygodne, nie trzeba używać narzędzi BIM, aby tworzyć obiekty BIM. Każdy obiekt FreeCAD, a nawet obiekty wykonane za pomocą innego oprogramowania, mogą stać się obiektami BIM. Wystarczy tylko wybrać jeden z nich i użyć narzędzia [komponent](Arch_Component/pl.md). Pozwala to również na użycie innych narzędzi, na przykład ze środowiska [Projekt części](PartDesign_Workbench/pl.md), do tworzenia złożonych obiektów, które zwykle są trudne do uzyskania za pomocą standardowych narzędzi BIM.

-   Obiekty utworzone za pomocą jednego narzędzia BIM mogą mieć wszystkie obsługiwane typy BIM. Należy tylko zmienić ich właściwość **Typ IFC**. Na przykład można utworzyć belkę za pomocą narzędzia do tworzenia ścian, zmieniając jej typ IFC na \"Belka\".

-   Narzędzia BIM opierają się na filozofii środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md): Można je tworzyć w dowolnym miejscu i w dowolny sposób w przestrzeni 3D. Wystarczy, że poprawnie ustawisz swoją [płaszczyznę roboczą](Draft_Snap_WorkingPlane/pl.md), a kolejne obiekty BIM będą tworzone na tej płaszczyźnie.

-   W programie FreeCAD nie ma obowiązkowej struktury budynku *(pięter w Revit)*. Możesz grupować swoje obiekty za pomocą [grup](Std_Group/pl.md) lub [części budowli](Arch_BuildingPart/pl.md) *(które są powszechnie używane do tworzenia poziomów, ale w rzeczywistości mogą być używane do dowolnego grupowania)*, aby działać w taki sam sposób jak w Revit, ale to Ty wybierasz najbardziej odpowiedni sposób dla swojego projektu.

### Sugerowany przepływ pracy związany z wdrożeniem 

-   Nie należy przeprowadzać migracji od razu. Nauka nowego oprogramowania to skomplikowane zadanie. FreeCAD jest darmowy, zacznij od jego zainstalowania i poznania, a następnie, gdy tylko będziesz mógł, użyj go do modelowania niewielkiej części projektu. W miarę zdobywania wiedzy i mistrzostwa rób coraz więcej w programie FreeCAD, a coraz mniej w Revit.

-   Upewnij się, że zawsze możesz wrócić do programu Revit, jeśli coś pójdzie nie tak: wcześnie i często eksportuj do IFC, otwórz plik w programie Revit, sprawdź, czy wszystko jest na swoim miejscu.

-   Tworzenie widoków i arkuszy działa podobnie jak w Revit, jeśli używasz widoków [Rysunku Roboczego](Draft_Workbench/pl.md) *(zalecany sposób)*. Utwórz [widok 2D kształtu](Draft_Shape2DView/pl.md) swoich obiektów lub poziomów, przenieś je z modelu, dodaj adnotacje, umieść wszystko w grupie lub [części budowli](Arch_BuildingPart/pl.md), następnie utwórz strony [Rysunku Technicznego](TechDraw_Workbench/pl.md) i dodaj do nich swoje widoki Rysunku Roboczego.

## Dodatkowe informacje 

-   Środowisko pracy [BIM](BIM_Workbench/pl.md)
-   [Przewodnik przejścia na FreeCAD BIM](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Migrating to FreeCAD from Revit/pl
