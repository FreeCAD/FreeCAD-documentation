# Branding/ro
{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

Acest articol descrie **Branding** al FreeCAD. Branding înseamnă să începeți propria aplicație pe baza FreeCAD. Acesta poate fi doar propriul dvs. executabil sau [ splash screen](Splash_screen.md) până la un program complet reconfigurat. Pe baza arhitecturii flexibile a FreeCAD, este ușor de utilizat ca bază pentru propriul program special.


</div>

### General


<div class="mw-translate-fuzzy">

### General 

Majoritatea branding-ului se face în *\' MainCmd.cpp*\' sau \'\'\' MainGui.cpp \'\'\'. Aceste proiecte generează fișierele executabile ale FreeCAD. Pentru a crea propriul dvs. brand doar copiați proiectele Main sau MainGui și dați executabilului un nume propriu, de ex. FooApp.exe. Cele mai importante setări pentru un aspect nou pot fi făcute într-un singur loc în funcția principal (). Iată secțiunea de cod care controlează branding-ul:


</div>

 {.C}
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


Prima intrare Config defineste numele programului. Acesta nu este numele executabilului, care poate fi modificat prin redenumire sau prin setările compilatorului, dar numele care este afișat în bara de activități din ferestrele sau în lista de programe din sistemele Unix.

Următoarele linii definesc intrările Config ale aplicației dvs. FooApp. O descriere a Config și a intrărilor pe care le găsiți în [Start up and Configuration](Start_up_and_Configuration.md).

### Images


<div class="mw-translate-fuzzy">

### Imagini

Resursele de imagine sunt compilate în FreeCAD folosind [Qt\'s resource system](http://qt-project.org/doc/qt-4.8/resources.html). Prin urmare, trebuie să scrieți un fișier .qrc, un format de fișier bazat pe XML care afișează fișierele imagine pe disc, dar și orice alt tip de fișiere de resurse. Pentru a încărca resursele compilate din cadrul aplicației, trebuie să adăugați o linie


</div>


```python
Q_INIT_RESOURCE(FooApp); 
```


<div class="mw-translate-fuzzy">

în funcția principal (). Alternativ, dacă aveți o imagine în format XPM, puteți să o includeți direct în main.cpp și să adăugați următoarea linie pentru a o înregistra:


</div>


```python
Gui::BitmapFactory().addXPM("FooAppSplasher", ( const char** ) splash_screen);
```

### Branding XML 


<div class="mw-translate-fuzzy">

### Branding XML 

În FreeCAD există și o metodă acceptată fără scrierea unei funcții principale personalizate (). Pentru această metodă trebuie să scrieți un nume de fișier numit branding.xml și să-l puneți în directorul de instalare al FreeCAD. Iată un exemplu cu toate etichetele acceptate:


</div>

 {.XML}
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



<div class="mw-translate-fuzzy">

Toate etichetele enumerate sunt opționale.


</div>


<div class="mw-translate-fuzzy">


{{docnav|Continuous Integration|Localisation}}


</div>




[Category:Developer Documentation](Category:Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Branding/ro
