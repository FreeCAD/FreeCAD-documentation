# Preference Packs/pl
{{TOCright}}

## Wprowadzenie

**Pakiet Preferencji** jest dystrybuowalnym zbiorem preferencji użytkownika ({{Version/pl|0.20}}), który może być zainstalowany jako dodatek i zastosowany jako pojedynczy zestaw. Każdy parametr użytkownika, który może być ustawiony w pliku user.cfg może być zawarty w pakiecie preferencji. Zastosowanie pakietu preferencji ustawia wszystkie zmienne w dostarczonym pliku CFG, nie modyfikując żadnych innych ustawień użytkownika. Na przykład, te pakiety mogą być użyte do stworzenia \"Motywów\" poprzez połączenie niestandardowego arkusza stylów wraz z zestawem preferencji użytkownika, które ustawiają różne kolory i style elementów w programie FreeCAD, które nie są kontrolowane przez arkusz stylów.

## Pakiet Preferencji głównego interfejsu użytkownika 

Większość interakcji użytkownika z zainstalowanymi Pakietami Preferencji odbywa się poprzez zakładkę **Ogólne** w sekcji **Ustawienia ogólne** [Edytora Preferencji](Preferences_Editor/pl.md).

<img alt="" src=images/PreferencePacks_MainInterface.png  style="width:400px;">

## Użycie zainstalowanego pakietu 

Aby zastosować pakiet preferencji, kliknij przycisk **Zastosuj** obok jego nazwy w zakładce **Ogólne** w edytorze [Edytor Preferencji](Preferences_Editor/pl.md). Głównym elementem pakietu preferencji jest zestaw preferencji użytkownika. Podczas stosowania pakietu każda z tych preferencji jest zmieniana na wartość zdefiniowaną w pakiecie. Opcjonalnie, autor pakietu może dołączyć makro przed i/lub po zastosowaniu, które również może zostać uruchomione. Ponieważ pakiety mogą potencjalnie dokonać dużych (i potencjalnie niepożądanych) zmian w preferencjach użytkownika, wykonywana jest kopia zapasowa oryginalnych preferencji ze znacznikiem czasu i przechowywana w folderze {{FileName|FREECAD_USER_DATA/SavedPreferencePacks/Backups}}. Te kopie zapasowe są przechowywane przez jeden tydzień.

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

-   Preferences/MainWindow/DockWindows/Std\_SelectionView
-   Preferences/MainWindow/DockWindows/Std\_ComboView
-   Preferences/MainWindow/DockWindows/Std\_ReportView
-   Preferences/MainWindow/DockWindows/Std\_PythonView
-   Preferences/MainWindow/DockWindows/Std\_TreeView
-   Preferences/MainWindow/DockWindows/Std\_PropertyView
-   Preferences/MainWindow/DockWindows/Std\_DAGView
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

The [Package Metadata](Package_Metadata.md) file, package.xml, defines the name of the Preference Pack, and allows you to assign other metadata items such as a version number, author information, and tags (which are displayed in the main UI as a comma-separated list). For a Preference Pack saved using the GUI as explained above, a single package.xml file is created in the {{FileName|FREECAD_USER_DATA/SavedPreferencePacks/}} directory. This file is used to describe the details such as the name and tags of all user-saved preference packs. To change a pack\'s name or tags, that file must be manually edited with a text editor. It can also provide a template for distributed preference packs: the author of a distributed pack may choose to start by saving a pack locally, then copying the pack\'s subdirectory and this global package.xml file as a starting point, modifying the copied package.xml file to only reference the pack being packaged for distribution.

Other files may also be included in a distribution, depending on what\'s required for the pack. A well-produced preference pack designed for distributing a visual theme called \"DarkSide\" for FreeCAD might look like:

-   package.xml
-   resources/
    -   icons/
        -   DarkSide.svg
-   DarkSide/
    -   DarkSide.cfg
    -   DarkSide.qss

Note the omission of the *pre.FCMacro* and *post.FCMacro* files, which are often unnecessary, as well as the inclusion of an icon (for display by the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md)), and the inclusion of a qss file (which will then be referenced in the *DarkSide.cfg* configuration data file).

The pre- and post- macro files are standard FreeCAD Python macros, and may contain any commands valid in such a macro. If the pre.FCMacro raises an exception (of any type), the application of the preference pack is cancelled. If the post.FCMacro raises an exception (of any type), the application of the pack is rolled back using the backup taken prior to its application. For example, these macros may be used to query the user for license acceptance, or to verify they are happy with the final state of their system after application.

The package.xml file for this example pack might be:

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

### Including templates in your add-on 

Many add-ons have user-specifiable preference information that is added to the user.cfg file. An add-on author may also choose to provide a Preference Pack Template file that lists the user configuration variables that can be automatically saved using the \"Save new pack\" method described above. To include these template files, add-on authors should create a subdirectory in their package called either \"PreferencePackTemplates\" or \"preference\_pack\_templates\". Within that folder should be one or more \*.cfg files: each must be a valid, well-formed user.cfg XML file containing one or more configuration variables set to their default values. The name of the file should reflect its purpose, e.g. \"colors.cfg\", \"active\_tabs.cfg\", etc. This set of files will be presented to the user when they save a new preference pack, with each file receiving a checkable entry in the list of items to save. The filename is used to generate the UI entry, with underscores replaced by spaces (and the extension omitted).

## Distributing a pack 

Preference Packs are distributed identically to [External Workbenches](External_workbenches.md) through the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md). To install a pack manually, use git to clone the package repository into your FreeCAD data directory (the directory where your user.cfg file is located), in a subdirectory called \"Preference Packs\".



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Developer Documentation](Category_Developer Documentation.md) > Preference Packs/pl
