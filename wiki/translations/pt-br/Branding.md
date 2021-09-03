





{{TOCright}}

## Visão geral {#visão_geral}


<div class="mw-translate-fuzzy">

Este artigo descreve a **Branding** do FreeCAD. Branding significa iniciar sua própria aplicação em uma base de FreeCAD. Isso pode ser apenas seu próprio executável ou [tela de splash](Splash_screen/pt-br.md) até um programa completo retrabalhado. Com base na arquitetura flexível do FreeCAD é fácil usá-lo como base para seu próprio programa de propósito especial.


</div>

### General


<div class="mw-translate-fuzzy">

### Geral

A maioria das \'branding\' é feita no {{{FileName|MainCmd.cpp}} ou {{FileName|MainGui.cpp}}}. Estes projetos geram os arquivos executáveis do FreeCAD. Para fazer sua própria \'Brand\' basta copiar os projetos Main ou MainGui e dar ao executável seu próprio nome, por exemplo, {{{FileName|FooApp.exe}}}. As configurações mais importantes para um novo visual são feitas em um só lugar na função Main(). Aqui está a seção de código que controla a \'branding\':


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


A primeira entrada Config define o nome do programa. Este não é o nome do executável, que pode ser alterado por renomeamento ou por configurações do compilador, mas o nome que é exibido na barra de tarefas no Windows ou na lista de programas em sistemas Unix.

As próximas linhas definem as entradas de configuração de sua aplicação FooApp. Uma descrição do Config e suas entradas que você encontra em [Inicialização e configuração](Start_up_e_Configuração/pt-br.md).

### Images


<div class="mw-translate-fuzzy">

### Imagens

Os recursos de imagem são compilados no FreeCAD usando [Qt\'s resource system](http://qt-project.org/doc/qt-4.8/resources.html). Portanto, é necessário escrever um arquivo {{FileName|.qrc}}, um formato de arquivo baseado em XML que lista arquivos de imagem no disco, mas também qualquer outro tipo de arquivo de recurso. Para carregar os recursos compilados dentro do aplicativo, você tem que adicionar uma linha


</div>


```python
Q_INIT_RESOURCE(FooApp); 
```

na função main(). Alternativamente, se você tiver uma imagem no formato XPM você pode incluí-la diretamente em seu {{{FileName|main.cpp}}} e adicionar a seguinte linha para registrá-la:


```python
Gui::BitmapFactory().addXPM("FooAppSplasher", ( const char** ) splash_screen);
```

### Branding XML {#branding_xml}


<div class="mw-translate-fuzzy">

### Branding XML {#branding_xml_1}

No FreeCAD há também outro método suportado que não utiliza uma função main() personalizada. Para este método você deve escrever um nome de arquivo chamado {{FileName|branding.xml}} e colocá-lo no diretório de instalação do FreeCAD. Aqui está um exemplo com todas as tags suportadas:


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


Todas as etiquetas listadas são opcionais.







[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
