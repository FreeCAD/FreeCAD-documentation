# DXF/pl
## Tło historyczne 

Drawing Exchange Format *(DXF)* to zastrzeżony format danych CAD opracowany przez Autodesk w celu umożliwienia wymiany plików między ich flagowym produktem AutoCAD a innym oprogramowaniem. Istnieje wiele dobrych bibliotek oprogramowania do odczytu/zapisu formatu DXF.

Istnieje wiele wersji formatu DXF. Można usłyszeć o niektórych kluczowych wersjach, takich jak R12 *(z 1992 r.)* lub R14 *(z 1997 r., która miała splajny)*. Późniejsze wersje DXF mają elementy 3D, ale są one rzadko używane lub wdrażane. Sposób wykorzystania DXF do udostępniania danych CAD między programami zależy głównie od ograniczeń i błędów w odpowiednich czytnikach / importerach i programach zapisujących / eksporterach. Rzadko są one w pełni udokumentowane i mogą być źródłem frustracji.

Jeśli edytujesz pliki DXF i chcesz, aby pozostały prawie takie same po ich zapisaniu, zalecamy użycie [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD) lub [QCad](https://en.wikipedia.org/wiki/QCad), ponieważ wewnętrzne struktury danych tych programów są kompatybilne z obiektami w pliku DXF.

W programie FreeCAD czytniki DXF muszą przetłumaczyć geometrię *(np. kształty splajnu)* z pliku DXF na określone wewnętrzne reprezentacje środowiska pracy.



## Metody importowania DXF 

Jeśli zamierzasz często sprawdzać ustawienia, zalecamy przejście do menu **Edycja → Preferencje ...→ Import-Eksport → DXF** i zaznaczenie pola {{CheckBox|TRUE|}} Pokaż okno dialogowe podczas importowania i eksportowania.

Więcej informacji znajduje się na stronach [Rysunek Roboczy: DXF](Draft_DXF/pl.md) i [FreeCAD i import DXF](FreeCAD_and_DXF_Import/pl.md).

Jeśli zaimportowana geometria jest używana do tworzenia kształtów 3D w środowisku pracy Projekt Części, po zaimportowaniu pliku DXF do szkicu należy użyć opcji [Sprawdź poprawność szkicu](Sketcher_ValidateSketch/pl.md).



### Importer C++ DXF 

Ta implementacja jest szybka, ale pomija funkcje, których nie rozpoznaje, takie jak splajny DXF. Może również importować geometrię do środowiska pracy Rysunek Roboczy tylko jako pojedyncze wpisy w drzewie modelu. Kolory mogą być odczytywane z pliku po zaznaczeniu tej opcji. Aby uzyskać więcej informacji, zobacz [ten post na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=32493).



### Importer DXF w Pythonie 

Ten importer musi zostać pobrany i zainstalowany, zanim będzie można z niego korzystać. Użyj opcji {{CheckBox|TRUE|}} Pozwól programowi FreeCAD na automatyczne pobieranie i aktualizację bibliotek DXF.

Ten importer ma więcej funkcji *(takich jak implementacja splajnów)* i ma opcję ładowania kształtów DXF do środowiska pracy Szkicownik. Należy jednak pamiętać, że wszystkie elementy szkicu pojawią się pojedynczo po raz drugi w drzewie modelu, co może być mylące. Możesz usunąć wszystkie te pojedyncze obiekty i zachować pojedynczy szkic *(który pojawi się jako drugi wpis na liście nowych elementów)*.

Niestety, Szkicownik nie implementuje kolorów, więc cała geometria pojawi się na tym samym poziomie, co stanowi problem, jeśli plik zawiera wiele linii konstrukcyjnych. Jednym z obejść jest otwarcie rysunku w LibreCAD i usunięcie całej geometrii, której nie chcesz wyświetlać, przed zapisaniem pliku zawierającego dokładnie tę geometrię, którą chcesz załadować.



### Makrodefinicje

Miej oko na forum FreeCAD lub [Przepisy na makropolecenia](Macros_recipes/pl.md) na alternatywne implementacje importowania i czyszczenia DXF w miarę ich rozwoju.



## Zapis DXF 

Oprócz opcji w menu **Edycja → Preferencje ...**, środowisko pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) może również eksportować strony rysunku do DXF za pomocą funkcji [Eksport strony do DXF](TechDraw_ExportPageDXF/pl.md).



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Draft](Category_Draft.md) > [TechDraw](Category_TechDraw.md) > [File_Formats](Category_File_Formats.md) > DXF/pl
