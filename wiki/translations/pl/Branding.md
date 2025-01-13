# Branding/pl
## Informacje ogólne 

Ten artykuł opisuje \"Branding\" FreeCAD. Branding oznacza utworzenie własnej aplikacji w oparciu o FreeCAD. Może to być tylko twój własny program wykonywalny lub [ekran powitalny](Splash_screen/pl.md) do czasu opracowania pełnej modyfikacji. W oparciu o elastyczną architekturę FreeCAD można go łatwo wykorzystać jako bazę do stworzenia własnego programu specjalnego przeznaczenia.



## Ostrzeżenie

Chociaż FreeCAD jest oferowany za darmo, a społeczność FreeCAD jest szczęśliwa widząc pojawiające się inne aplikacje oparte na FreeCAD, z drugiej strony widzieliśmy wiele przypadków nieuczciwego wykorzystania informacji zawartych na tej stronie przez ludzi, którzy po prostu przekształcili FreeCAD w aplikację o zamkniętym kodzie źródłowym, aby czerpać z tego zyski.

Chociaż licencja [LGPL](License/pl.md) pozwala na używanie kodu źródłowego FreeCAD w aplikacjach o zamkniętym kodzie źródłowym, to jednocześnie podaje ścisłe zasady takiego postępowania i nie pozwala po prostu wziąć programu FreeCAD, zmienić jego nazwy i pozbawić go licencji.

Jeśli jesteś zainteresowany użyciem FreeCAD w aplikacji o zamkniętym kodzie źródłowym, upewnij się, że dokładnie sprawdziłeś implikacje licencji LGPL, a nawet lepiej, skontaktuj się z każdym deweloperem, administratorem lub moderatorem FreeCAD zanim to zrobisz.



## Informacje ogólne 

Przeważającą część pracy przeprowadza się w **MainCmd.cpp** lub **MainGui.cpp**. Projekty te generują pliki wykonywalne FreeCAD. Aby stworzyć własną markę, wystarczy skopiować projekty **Main** lub **MainGui** i nadać plikom wykonywalnym własną nazwę, np. **FooApp.exe**. Najważniejszych ustawienia dla nowego wyglądu można dokonać w jednym miejscu w funkcji **main()**. Oto fragment kodu sterujący brandingiem:

 C
int main( int argc, char ** argv )
{
    // Name and Version of the Application
    App::Application::Config()["ExeName"] = "FooApp";
    App::Application::Config()["ExeVersion"] = "0.7";

    // set the banner (for loging and console)
    App::Application::Config()["CopyrightInfo"] = sBanner;
    App::Application::Config()["AppIcon"] = "FooAppIcon";
    App::Application::Config()["SplashScreen"] = "FooAppSplasher";
    App::Application::Config()["StartWorkbench"] = "Part design";
    App::Application::Config()["HiddenDockWindow"] = "Property editor";
    App::Application::Config()["SplashAlignment" ] = "Bottom|Left";
    App::Application::Config()["SplashTextColor" ] = "#000000"; // black

    // Inits the Application 
    App::Application::Config()["RunMode"] = "Gui";
    App::Application::init(argc,argv);

    Gui::BitmapFactory().addXPM("FooAppSplasher", ( const char** ) splash_screen);

    Gui::Application::initApplication();
    Gui::Application::runApplication();
    App::Application::destruct();

    return 0;
}


Pierwsza pozycja Config pozwala określić nazwę programu. Nie jest to nazwa pliku wykonywalnego, którą można zmienić poprzez zmianę nazwy lub ustawień kompilatora. Jest to nazwa, która jest wyświetlana na pasku zadań w systemie Windows lub na liście programów w systemie Unix.

Kolejne linie określają konkretne pozycje konfiguracji aplikacji FooApp. Opis konfiguracji i jej wpisów znajduje się w [Uruchomienie i konfiguracja](Start_up_and_Configuration.md).



## Pliki obrazów 

Wszystkie zasoby są zestawiane w FreeCAD przy użyciu [System zasobów Qt](http://qt-project.org/doc/qt-4.8/resources.html). Dlatego musisz zapisać plik **.qrc**, plik oparty na formacie XML, który wyświetla pliki obrazów na dysku, ale także każdy inny rodzaj plików zasobów. Aby załadować skompilowane zasoby wewnątrz aplikacji należy dodać linię:


```python
Q_INIT_RESOURCE(FooApp); 
```

do funkcji **main()**. Ewentualnie, jeśli posiadasz obraz w pliku XPM, możesz go bezpośrednio włączyć do **main.cpp** i dodać następującą linię, aby go zarejestrować:


```python
Gui::BitmapFactory().addXPM("FooAppSplasher", ( const char** ) splash_screen);
```



## Marka z XML 

W FreeCAD istnieje również metoda obsługiwana bez pisania niestandardowych funkcji main(). Dla tej metody musisz napisać nazwę pliku o nazwie **branding.xml** i umieścić go w katalogu instalacyjnym programu FreeCAD. Oto przykład z wszystkimi obsługiwanymi znacznikami:

 XML
<?xml version="1.0" encoding="utf-8"?>
<Branding>
    <Application>FooApp</Application>
    <WindowTitle>Foo App in title bar</WindowTitle>
    <BuildVersionMajor>1</BuildVersionMajor>
    <BuildVersionMinor>0</BuildVersionMinor>
    <BuildRevision>1234</BuildRevision>
    <BuildRevisionDate>2014/1/1</BuildRevisionDate>
    <CopyrightInfo>(c) My copyright</CopyrightInfo>
    <MaintainerUrl>Foo App URL</MaintainerUrl>
    <ProgramLogo>Path to logo (appears in bottom right corner)</ProgramLogo>
    <WindowIcon>Path to icon file</WindowIcon>
    <ProgramIcons>Path to program icons</ProgramIcons>
    <SplashScreen>splashscreen.png</SplashScreen>
    <SplashAlignment>Bottom|Left</SplashAlignment>
    <SplashTextColor>#ffffff</SplashTextColor>
    <SplashInfoColor>#c8c8c8</SplashInfoColor>
    <StartWorkbench>PartDesignWorkbench</StartWorkbench>
</Branding>


Wszystkie wymienione znaczniki są opcjonalne.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Branding/pl
