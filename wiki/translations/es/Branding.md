# Branding/es
{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

Este artículo describe el **Marcado** de FreeCAD. Marcado significa comenzar tu propia aplicación basada en FreeCAD. Esto puede ser sólo tu propio ejecutable o [pantalla de bienvenida](Splash_screen/es.md) pantalla de bienvenida hasta un programa completo adaptado. En base a la arquitectura flexible de FreeCAD es sencillo de utilizar como base para tus propios programas de propósito especial.


</div>

## Warning

Although FreeCAD is offered to you free of charge, and the FreeCAD community is happy to see other applications emerging, that are based on FreeCAD, we have on the other hand seen a lot of unfair use of the information contained on this page by people who simply rebranded FreeCAD into a closed-source application to make profit from it.

Although the [LGPL license](License.md) allows to use the FreeCAD source code in closed-source applications, it also gives strict rules to do so, and does not allow simply taking FreeCAD, renaming it and stripping it of its license.

Would you be interested in using FreeCAD in a closed-source application, be sure to check thoroughly the implications of the LGPL license, and, even better, contact any FreeCAD developer, administrator or moderator before doing so.

## General


<div class="mw-translate-fuzzy">

### General 

La mayoría del marcado se realiza en **MainCmd.cpp*o*MainGui.cpp**. Estos proyectos generan los archivos ejecutables de FreeCAD. Para crear tu propia Marca simplemente copia los proyectos Main o MainGui y dale al ejecutable un nombre diferente, e.g. FooApp.exe. La configuración más importante para una nueva apariencia puede realizarse en una lugar de la función main(). Aquí está la sección de código que controla el marcado:


</div>

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


La primera entrada de Config define el nombre del programa. Este no es el nombre del ejecutable, el cual puede cambiarse renombrándolo o por la configuración del compilador, sino el nombre que es mostrado en la barra de tareas en Windows o en la lista de programas en los sistemas Unix.

Las siguientes líneas definen las entradas de Config de tu aplicación FooApp. Una descripción de Config y sus entradas se encuentra en [Inicio y Configuración](Start_up_and_Configuration/es.md).

## Images

Image resources are compiled into FreeCAD using [Qt\'s resource system](http://qt-project.org/doc/qt-4.8/resources.html). Therefore you have to write a **.qrc** file, an XML-based file format that lists image files on the disk but also any other kind of resource files. To load the compiled resources inside the application you have to add a line


```python
Q_INIT_RESOURCE(FooApp); 
```

into the main() function. Alternatively, if you have an image in XPM format you can directly include it into your **main.cpp** and add the following line to register it:


```python
Gui::BitmapFactory().addXPM("FooAppSplasher", ( const char** ) splash_screen);
```

## Branding XML 

In FreeCAD there is also a method supported without writing a customized main() function. For this method you must write a file name called **branding.xml** and put it into the installation directory of FreeCAD. Here is an example with all supported tags:

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


All listed tags are optional.


<div class="mw-translate-fuzzy">


{{docnav/es|Testing/es|Localisation/es}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Branding/es
