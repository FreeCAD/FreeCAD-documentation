# Branding/fr
{{TOCright}}

## Présentation

Cet article décrit le **Branding (identification à la marque)** de FreeCAD. Branding signifie que vous pouvez lancer votre propre application sur une base de FreeCAD. Cela peut être seulement votre propre exécutable ou votre [écran de démarrage](Splash_screen/fr.md) jusqu\'à une refonte complète du programme. Grace à l\'architecture flexible de FreeCAD, il est facile de l\'utiliser comme base pour votre propre programme spécifique.

### Generalités

La plupart des marques (branding) se font dans {{FileName|MainCmd.cpp}} ou {{FileName|MainGui.cpp}}. Ces projets génèrent les fichiers exécutables de **FreeCAD**. Pour faire votre propre marque (branding), il suffit de copier **Main** (les projets principaux) ou **MainGui** (les projets graphiques GUI) et donner à l\'exécutable un nom qui vous est propre, pour notre exemple, {{FileName|FooApp.exe}}. Les réglages les plus importants pour un nouveau visuel sont effectués à un seul endroit, dans la fonction main(). Voici la section de code qui contrôle l\'image de marque (branding) :

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


La première entrée, **::Config** définit le nom du programme ici, **\"FooApp.exe\"**. Ce n\'est pas le nom de l\'exécutable qui peut être modifié en le renommant, ou par les paramètres du compilateur, mais le nom qui est affiché dans la barre des tâches sur les fenêtres, ou dans la liste des programmes sur les systèmes Unix.

Les lignes suivantes définissent les entrées de configuration de votre application **\"FooApp\"**, une description de la configuration et de ses entrées que vous trouverez dans [Démarrage et configuration](Start_up_and_Configuration/fr.md).

### Images

Les ressources contenant les images sont compilées dans FreeCAD à l\'aide de [Qt\'s resource system](http://qt-project.org/doc/qt-4.8/resources.html). Par conséquent, vous devez écrire un fichier {{FileName|.qrc}}, un format de fichier basé sur XML qui répertorie les fichiers image sur le disque, mais également tout autre type de fichier de ressources. Pour charger les ressources compilées dans l\'application, vous devez ajouter une ligne


```python
Q_INIT_RESOURCE(FooApp); 
```

dans la fonction main(). Sinon, si vous avez une image au format XPM, vous pouvez directement l\'inclure dans votre {{FileName|main.cpp}} puis ajoutez la ligne suivante pour l\'enregistrer:


```python
Gui::BitmapFactory().addXPM("FooAppSplasher", ( const char** ) splash_screen);
```

### Branding XML 

Dans FreeCAD, une méthode est également prise en charge sans écrire de fonction main() personnalisée. Pour cette méthode, vous devez écrire un nom de fichier appelé {{FileName|branding.xml}} et le placer dans le répertoire d\'installation de FreeCAD. Voici un exemple avec toutes les balises prises en charge:

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


Toutes les balises répertoriées sont facultatives.







_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Branding/fr
