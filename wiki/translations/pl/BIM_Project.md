---
 GuiCommand:Addon/pl
   Name: BIM Project
   Name/pl: BIM: Projekt
   Workbenches: BIM_Workbench/pl
   Addon: BIM
   MenuLocation: Manage , Manage project...
---

# BIM Project/pl



## Opis

<img alt="" src=images/BIM_project_screenshot.png  style="width:1024px;">

Okno dialogowe konfiguracji projektu to okno kreatora, które umożliwia utworzenie podstawowego zestawu obiektów przewodnika w bieżącym dokumencie lub w nowym dokumencie, który pomoże rozpocząć modelowanie projektu BIM.

Można utworzyć okno dialogowe konfiguracji projektu:

-   Nowa [struktura dokumentu](Document_structure/pl.md). Alternatywnie, inne obiekty zostaną utworzone w aktualnie otwartym dokumencie.
-   [teren](Arch_Site/pl.md). Obiekt Teren reprezentuje kawałek terenu, na którym będzie zlokalizowany projekt. Możesz nadać mu wiele przydatnych właściwości, takich jak adres ulicy i współrzędne globalne. Po utworzeniu, plac budowy jest tylko pustym pojemnikiem dla innych obiektów BIM, ale obiekt 3D reprezentujący rzeczywisty teren może być dołączony do niego później.
-   [Budowla](Arch_Building/pl.md). Obiekt Budowli jest kontenerem dla wszystkich obiektów BIM, które będą należeć do tego samego budynku. Możesz zdefiniować typ budynku i nadać mu prostokątne wymiary brutto, które będą reprezentowane jako prostokąt narysowany na płaszczyźnie gruntu *(X,Y)*.
-   Zestaw [Osie](Arch_Axis/pl.md), definiując ich liczbę i odstępy. Osie są używane jako wytyczne do wyrównywania obiektów 2D i 3D. Osie te można później modyfikować lub wprowadzać nowe.
-   Zestaw [Część budowli](Arch_BuildingPart/pl.md) do reprezentowania poziomów. Część budowli to ogólne obiekty kontenerowe BIM, które mogą być używane do grupowania innych obiektów BIM na wiele znaczących sposobów, takich jak powtarzalne komponenty lub poziomy budynku.
-   Zestaw domyślnych [grup](Std_Group/pl.md) wewnątrz każdego poziomu. Grupy mogą być używane do organizowania obiektów BIM w bardziej przejrzyste kategorie, takie jak \"Ściany\" lub \"Kolumny\". Nie mają one wpływu na sam model, ale często pomagają uczynić strukturę modelu bardziej przejrzystą, gdy zawiera on wiele obiektów.



### Szablony

Narzędzie Projekt obsługuje dwa rodzaje szablonów: Po wypełnieniu różnych opcji zawartość kreatora konfiguracji projektu BIM można *zapisać* jako szablon. Szablony te można *przywrócić* i dostosować w późniejszym czasie. Szablony projektów są przechowywane jako zwykłe pliki tekstowe w folderze użytkownika FreeCAD.

Alternatywnie można również zapisać zawartość bieżącego dokumentu jako szablon. Spowoduje to zapisanie aktualnie otwartego dokumentu jako standardowego pliku *.FCStd*, ale także uwzględni dodatkowe ustawienia BIM, takie jak bieżąca płaszczyzna robocza lub bieżące jednostki. Używając opcji *przywróć* w dowolnym momencie, zawartość tego pliku szablonu zostanie scalona z aktywnym dokumentem i zastosowane zostaną wszystkie znalezione w nim ustawienia.



---
⏵ [documentation index](../README.md) > BIM Project/pl
