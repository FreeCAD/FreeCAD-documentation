# Branding/it
{{TOCright}}

## Presentazione

Questo articolo descrive la **Marchiatura** di FreeCAD. Marchiare (Branding) significa creare una propria applicazione basata su FreeCAD. La personalizzazione può riguardare solo il proprio eseguibile oppure andare dalla [schermata iniziale](Splash_screen/it.md) fino alla rielaborazione completa del programma. Sulla base dell\'architettura flessibile di FreeCAD è facile utilizzarlo come base per il proprio programma per scopi speciali.

## Avvertimento

Sebbene FreeCAD sia offerto gratuitamente e la comunità di FreeCAD sia felice di vedere emergere altre applicazioni basate su FreeCAD, abbiamo d\'altronde visto un uso ingiusto delle informazioni contenute in questa pagina da parte di persone che semplicemente hanno rimarchiato FreeCAD in un\'applicazione closed-source per trarne profitto.

Sebbene la [Licenza LGPL](Licence/it.md) consenta di utilizzare il codice sorgente di FreeCAD in applicazioni closed-source, fornisce anche regole rigide per farlo e non consente semplicemente di prendere FreeCAD, rinominarlo e togliergli la licenza.

Se sei interessato a utilizzare FreeCAD in un\'applicazione closed-source, assicurati di controllare accuratamente le implicazioni della licenza LGPL e, ancora meglio, contatta qualsiasi sviluppatore, amministratore o moderatore di FreeCAD prima di farlo.

## Generale

La maggior parte della marchiatura avviene in **MainCmd.cpp** oppure in **MainGui.cpp**. Questi Progetti generano i file eseguibili di FreeCAD. Per costruire il proprio marchio è sufficiente copiare i progetti Main o MainGui e dare all\'eseguibile il proprio nome, ad esempio, **FooApp.exe**.

Le impostazioni più importanti per dare all\'applicazione un nuovo aspetto possono essere fatte all\'interno della funzione main(). Ecco la sezione di codice che controlla la marchiatura   *

 C
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

## Immagini

In FreeCAD tutte le risorse immagine vengono compilate utilizzando [Qt\'s resource system](http   *//qt-project.org/doc/qt-4.8/resources.html). Pertanto è necessario scrivere un file **.qrc**, un file basato sul formato XML, che elenca i file di immagine sul disco, ma anche qualsiasi altro tipo di file di risorse. Per caricare all\'interno dell\'applicazione le risorse compilate è necessario aggiungere una riga


```python
Q_INIT_RESOURCE(FooApp); 
```

nella funzione main(). In alternativa, se si dispone di un\'immagine in formato XPM è possibile includerla direttamente nella propria **main.cpp** e aggiungere la seguente riga per registrarla   *


```python
Gui   *   *BitmapFactory().addXPM("FooAppSplasher", ( const char** ) splash_screen);
```

## Marchiatura XML 

In FreeCAD c\'è anche un metodo supportato senza scrivere una funzione main() personalizzata. Per questo metodo basta scrivere un file chiamato **branding.xml** e metterlo nella directory di installazione di FreeCAD. Ecco un esempio con tutti i tag supportati   *

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


Tutti i tag elencati sono opzionali.







[Category   *Developer Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Branding/it
