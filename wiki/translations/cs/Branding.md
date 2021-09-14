# Branding/cs







{{TOCright}}

## Overview

This article describes the **Branding** of FreeCAD. Branding means to create your own application based on FreeCAD. That can be only your own executable or [splash screen](Splash_screen.md) till a complete reworked program. On base of the flexible architecture of FreeCAD it\'s easy to use it as base for your own special purpose program.

### General

Most of the branding is done in the {{FileName|MainCmd.cpp}} or {{FileName|MainGui.cpp}}. These Projects generate the executable files of FreeCAD. To make your own Brand just copy the Main or MainGui projects and give the executable its own name, e.g. {{FileName|FooApp.exe}}. The most important settings for a new look are made in one place in the main() function. Here is the code section that controls the branding:

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


The first Config entry defines the program name. This is not the executable name, which can be changed by renaming or by compiler settings, but the name that is displayed in the task bar on windows or in the program list on Unix systems.

The next lines define the Config entries of your FooApp Application. A description of the Config and its entries you find in [Start up and Configuration](Start_up_and_Configuration.md).

### Images

Image resources are compiled into FreeCAD using [Qt\'s resource system](http://qt-project.org/doc/qt-4.8/resources.html). Therefore you have to write a {{FileName|.qrc}} file, an XML-based file format that lists image files on the disk but also any other kind of resource files. To load the compiled resources inside the application you have to add a line


```python
Q_INIT_RESOURCE(FooApp); 
```

into the main() function. Alternatively, if you have an image in XPM format you can directly include it into your {{FileName|main.cpp}} and add the following line to register it:


```python
Gui::BitmapFactory().addXPM("FooAppSplasher", ( const char** ) splash_screen);
```

### Branding XML 

In FreeCAD there is also a method supported without writing a customized main() function. For this method you must write a file name called {{FileName|branding.xml}} and put it into the installation directory of FreeCAD. Here is an example with all supported tags:

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


All listed tags are optional.







[Category:Developer Documentation](Category:Developer_Documentation.md)
