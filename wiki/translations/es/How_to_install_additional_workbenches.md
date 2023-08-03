---
 TutorialInfo:s
   Topic: Programación
   Level: Programador mediano
   Time: 15 minutos
   FCVersion: Todos
   Author: User:R-Frank
   Files: ninguno
---

# How to install additional workbenches/es







## Descripción

Usuarios avanzados han extendido FreeCAD con varios [Ambiente de trabajo externos](external_workbenches/es.md), que no están integrados en el código fuente principal de FreeCAD, pero son fáciles de instalar en una instalación de FreeCAD existente. Aquí cubriremos los métodos de instalación para los distintos sistemas operativos.


**Note:**

a partir de la versión 0.17, FreeCAD presenta un <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Administrador de complementos](Std_AddonMgr/es.md) en el menú **Herramientas → Administrador de complementos**, que permite instalar tanto macros como bancos de trabajo. Las instrucciones que siguen sólo son necesarias si se desea instalar manualmente un banco de trabajo. Esto puede ser necesario si por alguna razón el Administrador de complementos no funciona pero tienes acceso al banco de trabajo descargado como un paquete **.zip**.


<div class="mw-collapsible mw-collapsed toccolours">



## Instalación en Windows 

Como instalar Ambiente de trabajo adicionales y complementos en Windows


<div class="mw-collapsible-content">



### Obsoleto


**Nota:**

usar el \"addons-installer\" ya no es recomendado. Usar el [Administrador de complementos](Std_AddonMgr/es.md) es el método recomendado en todos los sistemas.

Use el [addons-installer de Github](https://github.com/FreeCAD/FreeCAD-addons)

Durante el verano del código 2016 de Google, el estudiante Mandeep Singh comenzó a trabajar en una versión mejorada ([disponible aquí](https://github.com/mandeeps708/PluginManager)), pero esa versión necesita más trabajo antes de que pueda ser totalmente integrada en FreeCAD.

### Manual Install 


<div class="mw-translate-fuzzy">

### Instalación manual 


**Nota:**

Este método es posible pero no necesario con la introducción del [Administrador de complementos](Std_AddonMgr/es.md). Sin embargo, la información aquí puede ser útil para algunos.


</div>

-   Download the workbench from github by clicking on the button **Clone** or **Download** on the github page (upper right corner) and choosing \"Download ZIP\"
-   Unpack the downloaded archive on your local hard disk
-   Within FreeCAD, locate the macro path by choosing **Edit → Preferences → General → Macro** and look for the "Macro path"
-   Supposed your Windows-Login is "*username*" the default macro path is **%APPDATA%\FreeCAD\** which is usually **C:\Users\''username''\Appdata\Roaming\FreeCAD**
-   Within the macro-directory create (if not already present) a folder called "**Mod**"
-   Within the Mod folder, create a folder with the name of the workbench, for example "Curves"
-   Now move the unpacked files and sub-folders of the workbench to the just created workbench-folder
-   After restart of FreeCAD you should now have an entry in the [workbench selector](Std_Workbench.md)

**Recomendación adicional para la actualización de l\'Ambiente de trabajo**

En Windows, cuando se actualiza un Ambiente de trabajo ya instalado, Windows mantiene los viejos archivos .py como .pyc. Dado que esto puede dar lugar a problemas, se recomienda desinstalar el Ambiente de trabajo, reiniciar FreeCAD e instalar la nueva versión del Ambiente de trabajo.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Instalación en Linux 

Cómo instalar bancos de trabajo adicionales y complementos en Linux


<div class="mw-collapsible-content">

### Using git 

Adding the [community-ppa](https://launchpad.net/~freecad-community/+archive/ubuntu/ppa) within the ppa-manager.
Installing the workbenches via Synaptic Packet Manager.


```python
$ sudo apt-get install git python-numpy python-pyside
$ mkdir ~/.FreeCAD/Mod
$ cd ~/.FreeCAD/Mod
$ git clone  https://github.com/tomate44/CurvesWB.git
```

In FreeCAD you will now have a new workbench-entry called \"CurvesWB\". Once installed, use git to upgrade to the latest version:


```python
$ cd ~/.FreeCAD/Mod/CurvesWB
$ git pull
$ rm *.pyc
```

### Manual Installation 


**Note:**

This method is possible but not necessary with the introduction of the [Addon Manager](Std_AddonMgr.md). Nevertheless, the information here may still be useful to some.

-   Download the workbench from github by clicking on the button **Clone** or **Download** on the github page (upper right corner) and choosing \"Download ZIP\"
-   Unpack the downloaded archive on your local hard disk
-   Within FreeCAD, locate the macro path by choosing **Edit → Preferences → General → Macro** and look for the "Macro path"
-   By default, the macro directory is the (hidden) **./.FreeCAD/** directory in your home-directory
-   Within the macro-directory create (if not already present) a folder called "**Mod**"
-   Within the Mod/ folder, create a folder with the name of the workbench, for example "Curves"
-   Now move the unpacked files and sub-folders of the workbench to the just created workbench-folder
-   After restart of FreeCAD you should now have an entry in the [workbench selector](Std_Workbench.md)


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Installing on Mac 

How to install additional workbenches and addons on macOS


<div class="mw-collapsible-content">

### Manual Installation 


**Note:**

This method is possible but not necessary with the introduction of the [Addon Manager](Std_AddonMgr.md). Nevertheless, the information here may still be useful to some.

For the sake of this example, say you\'ve chosen the [Curves Workbench](Curves_Workbench.md) as the external workbench you want to install:

-   Choose and download the git repository of your chosen external workbench as a ZIP file
-   There are two possible locations for your Addon workbench \'Mods\':

1.  All Users: **/Applications/FreeCAD.app/Contents/Resources/Mod**
2.  Current user only: **/Users/myusername/Library/Application Support/FreeCAD/Mod**

-   If you use Finder to navigate manually to the All Users location in Applications you will need to
    -   go to **/Applications**\" and select FreeCAD.app
    -   right-mouse-click and select \"Show Package Contents\", a new window will appear with a folder named \"Contents\"
    -   single-click on the folder \"Contents\" then on \"Resources\" and double-click to open the folder \"Mod\"
-   Once you are in whichever \"Mod\" folder you want to use, create a New Folder named \"Curves\"
-   Unzip downloaded repository in the folder \"Mod/Curves\"


</div>


</div>



## Solución de problemas generales 

-   Don\'t use special characters (for example German umlauts) in your windows user name, otherwise FreeCAD will not recognize files and folders in the macro path.
-   If you have already set up a user name with special characters either create a new user name or point the macro path to a directory not using special characters.
-   Go to **Tools → Customize → Workbenches** and make sure the workbench is not set to invisible.
-   With 32-bit systems and FreeCAD 0.16.6706, after attempts to install, the additional Workbenches may not be available. In this case
    -   keep the [report view](report_view.md) open while starting FreeCAD, and read the error,
    -   see this forum thread [Assembly2 in Version: 0.16.5602 (Git)](http://forum.freecadweb.org/viewtopic.php?t=12839#p102933)



---
⏵ [documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > [Addons](Category_Addons.md) > How to install additional workbenches/es
