---
 GuiCommand:
   Name: BIM ProjectManager
   Name/pl: BIM: Zarządzaj projektem
   MenuLocation: Zarządzanie , Zarządzaj projektem
   Workbenches: BIM_Workbench/pl
---

# BIM ProjectManager/pl



## Opis

Okno dialogowe **Konfiguracji projektu** to okno kreatora, które umożliwia utworzenie podstawowego zestawu obiektów przewodnika w bieżącym dokumencie lub w nowym dokumencie, który pomoże rozpocząć modelowanie projektu BIM.

<img alt="" src=images/BIM_project_screenshot.png  style="width:600px;"> 
*Zarządzaj projektem BIM.*



## Użycie

Można utworzyć okno dialogowe konfiguracji projektu:

-   Nowa [struktura dokumentu](Document_structure/pl.md). Alternatywnie, inne obiekty zostaną utworzone w aktualnie otwartym dokumencie.
-   [teren](Arch_Site/pl.md). Obiekt Teren reprezentuje kawałek terenu, na którym będzie zlokalizowany projekt. Możesz nadać mu wiele przydatnych właściwości, takich jak adres ulicy i współrzędne globalne. Po utworzeniu, plac budowy jest tylko pustym pojemnikiem dla innych obiektów BIM, ale obiekt 3D reprezentujący rzeczywisty teren może być dołączony do niego później.
-   [Budowla](Arch_Building/pl.md). Obiekt Budowli jest kontenerem dla wszystkich obiektów BIM, które będą należeć do tego samego budynku. Możesz zdefiniować typ budynku i nadać mu prostokątne wymiary brutto, które będą reprezentowane jako prostokąt narysowany na płaszczyźnie gruntu *(X,Y)*.
-   Zestaw [Osie](Arch_Axis/pl.md), definiując ich liczbę i odstępy. Osie są używane jako wytyczne do wyrównywania obiektów 2D i 3D. Osie te można później modyfikować lub wprowadzać nowe.
-   Zestaw [Część budowli](Arch_BuildingPart/pl.md) do reprezentowania poziomów. Część budowli to ogólne obiekty kontenerowe BIM, które mogą być używane do grupowania innych obiektów BIM na wiele znaczących sposobów, takich jak powtarzalne komponenty lub poziomy budynku.
-   Zestaw domyślnych [grup](Std_Group/pl.md) wewnątrz każdego poziomu. Grupy mogą być używane do organizowania obiektów BIM w bardziej przejrzyste kategorie, takie jak \"Ściany\" lub \"Kolumny\". Nie mają one wpływu na sam model, ale często pomagają uczynić strukturę modelu bardziej przejrzystą, gdy zawiera on wiele obiektów.



## Szablony

Narzędzie Projekt obsługuje dwa rodzaje szablonów:

-   Po wypełnieniu różnych opcji zawartość kreatora konfiguracji projektu BIM można *zapisać* jako szablon. Szablony te można *przywrócić* i dostosować w późniejszym czasie. Szablony projektów są przechowywane jako zwykłe pliki tekstowe w folderze użytkownika FreeCAD.
-   Alternatywnie, możesz też zapisać zawartość bieżącego dokumentu jako szablon. To zapisze aktualnie otwarty dokument jako standardowy plik **.FCStd** file, ale również uwzględni dodatkowe ustawienia BIM, takie jak bieżąca płaszczyzna robocza lub bieżące jednostki. Po użyciu opcji **przywróć** w dowolnej chwili, zawartość tego pliku szablonu zostanie połączona z aktywnym dokumentem a wszystkie ustawienia w nim znalezione będą zastosowane.



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM ProjectManager/pl
