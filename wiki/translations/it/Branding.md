# Branding/it
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Presentazione


<div class="mw-translate-fuzzy">

Questo articolo descrive la personalizzazione o **Marchiatura** di FreeCAD.

Marchiare (Branding) significa avviare la realizzazione di una propria applicazione basata su FreeCAD. La personalizzazione può riguardare solo il proprio eseguibile oppure andare dalla [schermata iniziale](Splash_screen/it.md) fino alla rielaborazione completa del programma. Sulla base dell\'architettura flessibile di FreeCAD è facile utilizzarlo come base per il proprio programma per scopi speciali.


</div>

## Warning

Although FreeCAD is offered to you free of charge, and the FreeCAD community is happy to see other applications emerging, that are based on FreeCAD, we have on the other hand seen a lot of unfair use of the information contained on this page by people who simply rebranded FreeCAD into a closed-source application to make profit from it.

Although the [LGPL license](License.md) allows to use the FreeCAD source code in closed-source applications, it also gives strict rules to do so, and does not allow simply taking FreeCAD, renaming it and stripping it of its license.

Would you be interested in using FreeCAD in a closed-source application, be sure to check thoroughly the implications of the LGPL license, and, even better, contact any FreeCAD developer, administrator or moderator before doing so.

## General


<div class="mw-translate-fuzzy">

#### Generale

La maggior parte della marchiatura avviene in **MainCmd.cpp** oppure in **MainGui.cpp**. Questi Progetti generano i file eseguibili di FreeCAD. Per costruire il proprio marchio è sufficiente copiare i progetti Main o MainGui e dare all\'eseguibile un nome diverso, ad esempio, **FooApp.exe**.

Le impostazioni più importanti per dare all\'applicazione un nuovo aspetto possono essere fatte all\'interno della funzione main().

Ecco la sezione di codice che controlla la marchiatura   *


</div>

 {.C}
int main( int argc, char ** argv )
{
    // Name and Version of the Application
    App   *   *Application   *   *Config()["ExeName"] = "FooApp";
    App   *   *Application   *   *Config()["ExeVersion"] = "0.7";

    // set the banner (for loging and console)
    App   *   *Application   *   *Config()["CopyrightInfo"] = sBanner;
    App   *   *Application   *   *Config()["AppIcon"] = "FooAppIcon";
    App   *   *Application   *   *Config()["SplashScreen"] = "FooAppSplasher";
    App   *   *Application   *   *Config()["StartWorkbench"] = "Part design";
    App   *   *Application   *   *Config()["HiddenDockWindow"] = "Property editor";
    App   *   *Application   *   *Config()["SplashAlignment" ] = "Bottom|Left";
    App   *   *Application   *   *Config()["SplashTextColor" ] = "#000000"; // black

    // Inits the Application 
    App   *   *Application   *   *Config()["RunMode"] = "Gui";
    App   *   *Application   *   *init(argc,argv);

    Gui   *   *BitmapFactory().addXPM("FooAppSplasher", ( const char** ) splash_screen);

    Gui   *   *Application   *   *initApplication();
    Gui   *   *Application   *   *runApplication();
    App   *   *Application   *   *destruct();

    return 0;
}


La prima voce Config definisce il nome del programma. Questo nome non è il nome del file eseguibile, il quale può essere modificato rinominandolo o tramite le impostazioni del compilatore, ma è il nome che viene visualizzato nella barra delle applicazioni di Windows o nell\'elenco dei programmi sui sistemi Unix.

Le righe successive definiscono le voci di configurazione della vostra applicazione FooApp. Una descrizione di Config e delle sue voci si trova in [Avvio e Configurazione](Start_up_and_Configuration/it.md).

## Images


<div class="mw-translate-fuzzy">

#### Immagini

In FreeCAD tutte le risorse immagine vengono compilate utilizzando [Qt\'s resource system](http   *//qt-project.org/doc/qt-4.8/resources.html). Pertanto è necessario scrivere un file **.qrc**, un file basato sul formato XML, che elenca i file di immagine sul disco, ma anche qualsiasi altro tipo di file di risorse. Per caricare all\'interno dell\'applicazione le risorse compilate è necessario aggiungere una riga


</div>


```python
Q_INIT_RESOURCE(FooApp); 
```

nella funzione main(). In alternativa, se si dispone di un\'immagine in formato XPM è possibile includerla direttamente nella propria **main.cpp** e aggiungere la seguente riga per registrarla   *


```python
Gui   *   *BitmapFactory().addXPM("FooAppSplasher", ( const char** ) splash_screen);
```

## Branding XML 


<div class="mw-translate-fuzzy">

### Branding XML 

In FreeCAD c\'è anche un metodo supportato senza scrivere una funzione main() personalizzata. Per questo metodo basta scrivere un file chiamato **branding.xml** e metterlo nella directory di installazione di FreeCAD. Ecco un esempio con tutti i tag supportati   *


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

Tutti i tag elencati sono opzionali.


</div>


<div class="mw-translate-fuzzy">





</div>




[Category   *Developer Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Branding/it
