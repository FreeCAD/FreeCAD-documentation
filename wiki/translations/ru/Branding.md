# Branding/ru
{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

## Обзор

Эта статья описывает **Брендинг** FreeCAD. Брендинг средств для начала вашего собственного приложения основанного на FreeCAD. Это может быть как ваш собственный исполняемый файл или загрузочная картинка так и полностью переработанная программа. На базе гибкой архитектуры FreeCAD, её легко использовать как основу для собственной целевой программы.


</div>

### General


<div class="mw-translate-fuzzy">

### Главное

Большая часть брендинга делается в {{FileName|MainCmd.cpp}} или {{FileName|MainGui.cpp}}. Эти Проекты генерируют исполняемые файлы FreeCAD. Чтобы сделать ваш собственный Бренд просто скопируйте Main или MainGui проекты и дайте исполняемым файлам собственное имя, например {{FileName|FooApp.exe}}. Наиболее важные настройки для нового облика можно сделать в одном месте в функции main(). Вот участок кода, который управляет брендингом:


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


Первая запись Config определяет название программы. Это не имя исполняемого файла, который может быть изменен путем переименования или настройки компилятора, а имя, которое отображается в панели задач в Windows или в списке программ в Unix системах.

Следующие строки определяют Config записи вашего FooApp Приложения. Описание Config и его элементов вы можете найти в [запуске и конфигурации](Start_up_and_Configuration/ru.md).

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


<div class="mw-translate-fuzzy">





</div>




[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Branding/ru
