# Preference Packs/pl
## Wprowadzenie

**Pakiet Preferencji** jest dystrybuowalnym zbiorem preferencji użytkownika ({{Version/pl|0.20}}), który może być zainstalowany jako dodatek i zastosowany jako pojedynczy zestaw. Każdy parametr użytkownika, który może być ustawiony w pliku user.cfg może być zawarty w pakiecie preferencji. Zastosowanie pakietu preferencji ustawia wszystkie zmienne w dostarczonym pliku CFG, nie modyfikując żadnych innych ustawień użytkownika. Na przykład, te pakiety mogą być użyte do stworzenia \"Motywów\" poprzez połączenie niestandardowego arkusza stylów wraz z zestawem preferencji użytkownika, które ustawiają różne kolory i style elementów w programie FreeCAD, które nie są kontrolowane przez arkusz stylów.

## Pakiet Preferencji głównego interfejsu użytkownika 

Większość interakcji użytkownika z zainstalowanymi Pakietami Preferencji odbywa się poprzez zakładkę **Ogólne** w sekcji **Ustawienia ogólne** [Edytora Preferencji](Preferences_Editor/pl.md).

<img alt="" src=images/PreferencePacks_MainInterface.png  style="width:400px;">

## Użycie zainstalowanego pakietu 

Aby zastosować pakiet preferencji, kliknij przycisk **Zastosuj** obok jego nazwy w zakładce **Ogólne** w edytorze [Edytor Preferencji](Preferences_Editor/pl.md). Głównym elementem pakietu preferencji jest zestaw preferencji użytkownika. Podczas stosowania pakietu każda z tych preferencji jest zmieniana na wartość zdefiniowaną w pakiecie. Opcjonalnie, autor pakietu może dołączyć makro przed i/lub po zastosowaniu, które również może zostać uruchomione. Ponieważ pakiety mogą potencjalnie dokonać dużych (i potencjalnie niepożądanych) zmian w preferencjach użytkownika, wykonywana jest kopia zapasowa oryginalnych preferencji ze znacznikiem czasu i przechowywana w folderze **FREECAD_USER_DATA/SavedPreferencePacks/Backups**. Te kopie zapasowe są przechowywane przez jeden tydzień.

## Tworzenie nowego pakietu 

Pakiety mogą być tworzone ręcznie lub inicjowane za pomocą przycisku **Zapisz nowy...** w zakładce **Ogólne** w [Edytorze Preferencji](Preferences_Editor/pl.md). Kliknięcie tego przycisku powoduje wyświetlenie okna dialogowego z prośbą o podanie nazwy nowego pakietu i wyświetla zestaw pól wyboru pozwalających na zapisanie tylko podzbioru preferencji.

<img alt="" src=images/PreferencePacks_SaveNewPack.png  style="width:400px;">

Ze względu na sposób, w jaki FreeCAD wewnętrznie używa preferencji, tylko elementy zawarte w tych plikach szablonów mogą być zapisane automatycznie przy użyciu tej procedury. Elementy nie zawarte w plikach szablonów muszą być ręcznie dołączone do pliku \*.cfg pakietu. Nie ma wbudowanego ograniczenia co do tego, jakie elementy preferencji mogą być zawarte w pakiecie preferencji, ale autorom zdecydowanie odradza się zmienianie ustawionego języka użytkownika, modyfikowanie listy ostatnich plików lub zmienianie czegokolwiek związanego z tymczasowym stanem UI *(np. zapisany rozmiar okna z możliwością zmiany rozmiaru itp.)*.

### Szczegóły szablonu 

Te sekcje zawierają listę wszystkich preferencji zawartych we wbudowanych szablonach. W tej chwili skupiają się one na elementach związanych z wyglądem, ale mile widziane są prośby i sugestie z forum dotyczące dodatkowych elementów. Zainstalowane dodatki mogą również dostarczać własne szablony *(nie są one tutaj udokumentowane)*. Kliknij \"Rozwiń\" po prawej stronie każdego wpisu, aby zobaczyć listę.


<div class="mw-collapsible mw-collapsed toccolours">

**Kolory dla środowiska Architektura**


<div class="mw-collapsible-content">

-   Preferences/Mod/Arch/WallColor
-   Preferences/Mod/Arch/StructureColor
-   Preferences/Mod/Arch/RebarColor
-   Preferences/Mod/Arch/WindowColor
-   Preferences/Mod/Arch/WindowGlassColor
-   Preferences/Mod/Arch/PanelColor
-   Preferences/Mod/Arch/ColorHelpers
-   Preferences/Mod/Arch/defaultSpaceColor


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Kolory dla Konsoli**


<div class="mw-collapsible-content">

-   Preferences/OutputWindow/colorText
-   Preferences/OutputWindow/colorLogging
-   Preferences/OutputWindow/colorWarning
-   Preferences/OutputWindow/colorError


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Kolory dla środowiska Rysunek Roboczy**


<div class="mw-collapsible-content">

-   Preferences/Mod/Draft/constructioncolor
-   Preferences/Mod/Draft/gridTransparency
-   Preferences/Mod/Draft/gridColor
-   Preferences/Mod/Draft/snapcolor


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Kolory dla Edytora**


<div class="mw-collapsible-content">

-   Preferences/Editor/Text
-   Preferences/Editor/Bookmark
-   Preferences/Editor/Breakpoint
-   Preferences/Editor/Keyword
-   Preferences/Editor/Comment
-   Preferences/Editor/Block comment
-   Preferences/Editor/Number
-   Preferences/Editor/String
-   Preferences/Editor/Character
-   Preferences/Editor/Class name
-   Preferences/Editor/Define name
-   Preferences/Editor/Operator
-   Preferences/Editor/Python output
-   Preferences/Editor/Python error
-   Preferences/Editor/Current line highlight


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Kolory dla czcionki edytora**


<div class="mw-collapsible-content">

-   Preferences/Editor/FontSize
-   Preferences/Editor/Font


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Kolory dla okna głównego**


<div class="mw-collapsible-content">

-   Preferences/MainWindow/DockWindows/Std_SelectionView
-   Preferences/MainWindow/DockWindows/Std_ComboView
-   Preferences/MainWindow/DockWindows/Std_ReportView
-   Preferences/MainWindow/DockWindows/Std_PythonView
-   Preferences/MainWindow/DockWindows/Std_TreeView
-   Preferences/MainWindow/DockWindows/Std_PropertyView
-   Preferences/MainWindow/DockWindows/Std_DAGView
-   Preferences/MainWindow/Toolbars/File
-   Preferences/MainWindow/Toolbars/Workbench
-   Preferences/MainWindow/Toolbars/Macro
-   Preferences/MainWindow/Toolbars/View
-   Preferences/MainWindow/Toolbars/Structure
-   Preferences/MainWindow/Toolbars/Navigation


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Kolory dla środowiska Path**


<div class="mw-collapsible-content">

-   Preferences/Mod/Path/DefaultNormalPathColor
-   Preferences/Mod/Path/DefaultRapidPathColor
-   Preferences/Mod/Path/DefaultPathMarkerColor
-   Preferences/Mod/Path/DefaultExtentsColor
-   Preferences/Mod/Path/DefaultProbePathColor
-   Preferences/Mod/Path/DefaultHighlightPathColor
-   Preferences/Mod/Path/DefaultBBoxSelectionColor
-   Preferences/Mod/Path/DefaultBBoxNormalColor


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Kolory dla środowiska Szkicownik**


<div class="mw-collapsible-content">

-   Preferences/View/SketchEdgeColor
-   Preferences/View/SketchVertexColor
-   Preferences/View/EditedEdgeColor
-   Preferences/View/EditedVertexColor
-   Preferences/View/ConstructionColor
-   Preferences/View/ExternalColor
-   Preferences/View/InvalidSketchColor
-   Preferences/View/FullyConstrainedColor
-   Preferences/View/InternalAlignedGeoColor
-   Preferences/View/FullyConstraintElementColor
-   Preferences/View/FullyConstraintConstructionElementColor
-   Preferences/View/FullyConstraintInternalAlignmentColor
-   Preferences/View/FullyConstraintConstructionPointColor
-   Preferences/View/ConstrainedIcoColor
-   Preferences/View/NonDrivingConstrDimColor
-   Preferences/View/ConstrainedDimColor
-   Preferences/View/ExprBasedConstrDimColor
-   Preferences/View/DeactivatedConstrDimColor
-   Preferences/View/CursorTextColor
-   Preferences/View/CursorCrosshairColor
-   Preferences/View/CreateLineColor


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Kolory dla środowiska Start**


<div class="mw-collapsible-content">

-   Preferences/Mod/Start/BackgroundColor1
-   Preferences/Mod/Start/BackgroundTextColor
-   Preferences/Mod/Start/PageColor
-   Preferences/Mod/Start/PageTextColor
-   Preferences/Mod/Start/BoxColor
-   Preferences/Mod/Start/LinkColor
-   Preferences/Mod/Start/BackgroundColor2


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Kolory dla środowiska Rysunek Techniczny**


<div class="mw-collapsible-content">

-   Preferences/Mod/TechDraw/Decorations/SectionColor
-   Preferences/Mod/TechDraw/Decorations/CenterColor
-   Preferences/Mod/TechDraw/Decorations/VertexColor
-   Preferences/Mod/TechDraw/Decorations/HighlightColor
-   Preferences/Mod/TechDraw/Colors/Hatch
-   Preferences/Mod/TechDraw/Colors/Background
-   Preferences/Mod/TechDraw/Colors/PreSelectColor
-   Preferences/Mod/TechDraw/Colors/HiddenColor
-   Preferences/Mod/TechDraw/Colors/SelectColor
-   Preferences/Mod/TechDraw/Colors/NormalColor
-   Preferences/Mod/TechDraw/Colors/CutSurfaceColor
-   Preferences/Mod/TechDraw/Colors/GeomHatch
-   Preferences/Mod/TechDraw/Colors/FaceColor
-   Preferences/Mod/TechDraw/Colors/ClearFace


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Kolory dla okien**


<div class="mw-collapsible-content">

-   Preferences/View/BacklightColor
-   Preferences/View/BackgroundColor
-   Preferences/View/BackgroundColor2
-   Preferences/View/BackgroundColor3
-   Preferences/View/BackgroundColor4
-   Preferences/View/Simple
-   Preferences/View/Gradient
-   Preferences/View/UseBackgroundColorMid
-   Preferences/View/HighlightColor
-   Preferences/View/SelectionColor
-   Preferences/View/DefaultShapeColor
-   Preferences/View/RandomColor
-   Preferences/TreeView/TreeEditColor
-   Preferences/TreeView/TreeActiveColor
-   Preferences/MainWindow/TiledBackground
-   Preferences/MainWindow/StyleSheet


</div>


</div>

### Struktura pakietu preferencji 

Podczas gdy rdzeniem większości Pakietów Preferencji jest pojedynczy plik konfiguracyjny, z powodu ich przeznaczenia do dystrybucji, wymagana jest również pewna pomocnicza struktura. Cztery podstawowe pliki definiują pakiet, ułożone w następującej strukturze katalogów *(dla pakietu preferencji o nazwie \"SamplePreferencePack\")*:

-   package.xml
-   SamplePreferencePack/
    -   SamplePreferencePack.cfg
    -   pre.FCMacro
    -   post.FCMacro

Plik [Metadane pakietu](Package_Metadata/pl.md), package.xml, definiuje nazwę pakietu preferencji i umożliwia przypisanie innych elementów metadanych, takich jak numer wersji, informacje o autorze i znaczniki *(które są wyświetlane w głównym interfejsie użytkownika jako lista oddzielona przecinkami)*. W przypadku pakietu preferencji zapisanego za pomocą interfejsu graficznego w sposób opisany powyżej tworzony jest jeden plik package.xml w katalogu **FREECAD_USER_DATA/SavedPreferencePacks/**. Plik ten jest używany do opisywania szczegółów, takich jak nazwa i znaczniki wszystkich zapisanych przez użytkownika pakietów preferencji. Aby zmienić nazwę lub znaczniki pakietu, należy ręcznie edytować ten plik za pomocą edytora tekstu. Może on także stanowić szablon dla pakietów dystrybuowanych: autor pakietu dystrybuowanego może zacząć od zapisania pakietu lokalnie, a następnie skopiowania podkatalogu pakietu i globalnego pliku package.xml jako punktu wyjścia, modyfikując skopiowany plik package.xml tak, aby zawierał tylko odniesienie do pakietu pakowanego do dystrybucji.

Do dystrybucji mogą być dołączone także inne pliki, w zależności od tego, co jest wymagane w danym pakiecie. Dobrze wyprodukowany pakiet preferencji przeznaczony do dystrybucji motywu wizualnego o nazwie \"DarkSide\" dla programu FreeCAD może wyglądać następująco:

-   package.xml
-   resources/
    -   icons/
        -   DarkSide.svg
-   DarkSide/
    -   DarkSide.cfg
    -   DarkSide.qss

Zwróć uwagę na pominięcie plików *pre.FCMacro* i *post.FCMacro*, które często są niepotrzebne, a także na dołączenie ikony *(do wyświetlania przez <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżer dodatków](Std_AddonMgr/pl.md))*, i dołączenie pliku qss *(do którego następnie będzie się odwoływał plik danych konfiguracyjnych **DarkSide.cfg**)*.

Pliki pre- i post- makra są standardowymi makrodefinicjami FreeCAD Python i mogą zawierać dowolne polecenia obowiązujące w tego typu makrodefinicjach. Jeśli podczas wykonywania pre.FCMacro zostanie zgłoszony wyjątek *(dowolnego typu)*, stosowanie pakietu preferencji zostanie anulowane. Jeśli natomiast post.FCMacro zgłosi wyjątek *(dowolnego typu)*, zastosowanie pakietu jest cofane przy użyciu kopii zapasowej wykonanej przed jego zastosowaniem. Makrodefinicji tego typu można na przykład użyć do zapytania użytkownika o akceptację licencji lub do sprawdzenia, czy użytkownik jest zadowolony z ostatecznego stanu systemu po zastosowaniu pakietu.

Plik package.xml dla tego przykładowego pakietu może mieć następującą postać:

    <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <package format="1" xmlns="https://wiki.freecad.org/Package_Metadata">
      <name>DarkSide Theme Package</name>
      <description>A preference pack including a stylesheet and other GUI color information for a Dark mode.</description>
      <version>1.0.0</version>
      <maintainer email="chennes@pioneerlibrarysystem.org">Chris Hennes</maintainer>
      <license file="LICENSE">GPLv3</license>
      <url type="repository" branch="main">https://github.com/chennes/DarkSideThemePackage</url>
      <icon>resources/icons/DarkSide.svg</icon>

      <content>
        <preferencepack>
          <name>DarkSide</name>
          <description>Dark mode color scheme</description>
          <tag>color</tag>
          <tag>stylesheet</tag>
          <tag>dark</tag>
          <file>DarkSide.qss</file>
        </preferencepack>
      </content>

    </package>

### Włączanie szablonów do dodatku 

Wiele dodatków zawiera informacje o preferencjach użytkownika, które są dodawane do pliku user.cfg. Autor dodatku może również dostarczyć plik szablonu pakietu preferencji, zawierający listę zmiennych konfiguracyjnych użytkownika, które mogą być automatycznie zapisane za pomocą opisanej powyżej metody \"Zapisz nowy pakiet\". Aby dołączyć te pliki szablonów, autorzy dodatków powinni utworzyć w swoim pakiecie podkatalog o nazwie \"PreferencePackTemplates\" lub \"preference_pack_templates\". W tym katalogu powinien znajdować się jeden lub więcej plików \*.cfg: każdy z nich musi być poprawnym, dobrze sformatowanym plikiem XML user.cfg, zawierającym jedną lub więcej zmiennych konfiguracyjnych ustawionych na wartości domyślne. Nazwa pliku powinna odzwierciedlać jego przeznaczenie, np. \"colors.cfg\", \"active_tabs.cfg\" itd. Ten zestaw plików zostanie przedstawiony użytkownikowi podczas zapisywania nowego pakietu preferencji, a każdy z nich będzie miał zaznaczoną pozycję na liście elementów do zapisania. Do wygenerowania wpisu w interfejsie użytkownika używana jest nazwa pliku, przy czym podkreślenia są zastępowane spacjami (a rozszerzenie pomijane).

## Dystrybucja pakietu 

Pakiety Preferencji są dystrybuowane tak samo jak [Zewnętrzne środowiska pracy](External_workbenches/pl.md) poprzez <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżer dodatków](Std_AddonMgr/pl.md). Aby zainstalować pakiet ręcznie, użyj git, aby sklonować repozytorium pakietów do katalogu danych FreeCAD *((wpisz `App.getUserAppDataDir()` w [Konsoli Python](Python_console/pl.md), aby poznać tę ścieżkę))*, w podkatalogu o nazwie \"Pakiety preferencji\".

Zobacz również stronę [Osobiste pakiety preferencji](Private_Preference_Packs/pl.md).



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Developer Documentation](Category_Developer Documentation.md) > Preference Packs/pl
