# Branding/zh-cn
## 概述

本文介绍FreeCAD的"品牌化"。品牌化意味着基于FreeCAD构建你自己的应用程序。可以仅仅是你自己的可执行文件或[启动页面](Splash_screen.md)，也可以是完全重新改造的程序。在FreeCAD的灵活架构的基础上，很容易构建你自己的特殊用途的应用程序。

## 警告

尽管你可以自由修改FreeCAD，社区也乐于看到其他基于FreeCAD的应用出现，但另一方面，我们也看到很多人对这个页面上的信息进行了不公平的使用，他们只是简单地将FreeCAD重新命名为一个闭源应用程序来从中获利。

虽然[LGPL许可证](License.md)允许在闭源应用程序中使用FreeCAD源代码，但它也给出了严格的规则，即不允许将FreeCAD改个名字它并去掉它的许可证

如果您对在闭源应用程序中使用FreeCAD感兴趣，请确保彻底核对LGPL许可的含义，最好在这样做之前联系任何FreeCAD开发人员、管理员或仲裁员。

## 通用

大部分的品牌化都是在**MainCmd.cpp**或**MainGui.cpp**中完成的。这些项目生成FreeCAD的可执行文件。要制作自己的品牌，只需复制Main或MainGui项目，并给可执行文件自己的名称，例如**FooApp.exe**。 对于新外观最重要的设置在main()函数的一个地方。下面是控制品牌化的代码部分:

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


第一个Config项定义程序名称。这不是可执行文件名称（可以通过重命名或编译器设置来更改），而是显示在windows上的任务栏或Unix系统上的程序列表中的名称。

接下来的几行定义FooApp应用程序的Config项。Config及其条目的描述，您可以在[启动和配置](启动和配置.md)中找到。

## 图像

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



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Branding/zh-cn
