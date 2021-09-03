





{{TOCright}}

## Übersicht

Dieser Artikel beschreibt die **Markenbildung** von FreeCAD. Markenbildung bedeutet, deine eigene Anwendung basierend auf FreeCAD zu erstellen. Das kann nur eine eigene ausführbare Datei oder [Eingangsbildschirm](Splash_screen/de.md) sein, bis hin zu einem komplett überarbeiteten Programm. Aufgrund der flexiblen Architektur von FreeCAD ist es einfach, es als Basis für die Erstellung deines eigenen speziellen Programms zu verwenden.

### Allgemeines

Die Markenbildung geschieht hauptsächlich in den Dateien {{FileName|MainCmd.cpp}} oder {{FileName|MainGui.cpp}}. Diese Projekte generieren die ausführbaren Dateien von FreeCAD. Um deine eigene Marke zu erstellen, kopiere einfach die Main- oder MainGui Projekte und gib der ausführbaren Datei ihren eigenen Namen, z. B. {{FileName|FooApp.exe}}. Die wichtigsten Einstellungen für ein neues Aussehen werden an einer Stelle in der main() Funktion vorgenommen. Hier ist der Code-Abschnitt, der die Markenbildung steuert:

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


Der erste Config Eintrag definiert den Namen des Programms. Dies ist nicht der Name der ausführbaren Datei, die durch Umbenennen oder Kompilierer Einstellungen geändert werden kann, sondern der Name, der in der Aufgabenleiste bei Windows oder in der Programmliste auf Unix Systemen angezeigt wird.

Die nächsten Zeilen definieren die Config Einträge Ihrer FooApp Anwendung. Eine Beschreibung der Config und ihrer Einträge findest du unter [Inbetriebnahme und Konfiguration](Start_up_and_Configuration/de.md).

### Bilder

Bildquellen werden über das [Qt-System](http://qt-project.org/doc/qt-4.8/resources.html) in FreeCAD kompiliert. Deshalb muss eine {{FileName|.qrc}} Datei geschrieben werden; ein XML-basiertes Dateiformat, das die Bilddateien auf der Festplatte auflistet. Um die kompilierten Ressourcen innerhalb der Anwendung zu laden, muss folgende Zeile hinzugefügt werden:


```python
Q_INIT_RESOURCE(FooApp); 
```

innerhalb der main()-Funktion. Liegt ein Bild in XPM-Format vor, kann es mit Hilfe folgender Zeile direkt in der Datei {{FileName|main.cpp}} registriert werden:


```python
Gui::BitmapFactory().addXPM("FooAppSplasher", ( const char** ) splash_screen);
```

### Branding XML {#branding_xml}

In FreeCAD wird auch eine Branding-Methode unterstützt, ohne eine angepasste main() Function zu schreiben. Für diese Methode müssen Sie eine Datei namens {{FileName|branding.xml}} schreiben und diese im Installationsverzeichnis von FreeCAD ablegen. Hier ein Beispiel mit allen unterstützten Tags:

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


Alle aufgeführten Tags sind optional.


{{docnav/de
|[Kontinuierliche Integration](Continuous_Integration/de.md)
|[Lokalisierung](Localisation/de.md)
}}




[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
