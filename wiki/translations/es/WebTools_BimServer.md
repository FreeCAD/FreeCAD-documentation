---
- GuiCommand:/es
   Name/es:Arch BimServer‏‎‏‎
   Workbenches:[Arch](Arch_Workbench/es.md)
   MenuLocation:Arch → Utilities → BIM server
   Shortcut:‏‎
   SeeAlso:
---


</div>


<div class="mw-translate-fuzzy">

**Nota:** A partir de FreeCAD v0.17, esta herramienta se eliminó de Arch Workbench y ahora forma parte del [WebTools Workbench](WebTools_Workbench.md) externo que puede instalar a través del menú Herramientas → Administrador de complementos.


</div>

## Descripción

Este comando le permite interactuar con una instancia de [BIMServer](http://www.bimserver.org), abrir archivos almacenados en el servidor de Bim y guardar nuevas revisiones de esos archivos. BIMServer es un sistema de servidor de código abierto y gratuito creado para trabajar con archivos IFC. En su estado actual, permite administrar proyectos con múltiples archivos IFC y administrar revisiones. Su sistema de base de datos altamente extensible y su arquitectura de complementos también permiten diseñar herramientas avanzadas de consulta / validación y flujos de trabajo de fusión inteligente.

Para utilizar este comando, se deben cumplir las siguientes condiciones:


<div class="mw-translate-fuzzy">

-   Los módulos **json** y **requests** deben estar instalados en su sistema.
-   Debe tener acceso a una instancia de BimServer (lea la [documentación de BIMServer](https://github.com/opensourceBIM/BIMserver/wiki) para instalar un BIMServer localmente) y tener credenciales (nombre de usuario y contraseña) para ese servidor. Al momento de escribir, la versión estable de BIMServer es 1.4, pero le recomendamos que instale una de las versiones beta 1.5.X disponibles, que instala muchos complementos automáticamente (en la versión 1.4 tiene que instalar los complementos manualmente).
-   Todas las transferencias de archivos con BIMServer se realizan con archivos IFC. Por lo tanto, necesita saber cómo trabajar con [ IFC files](Arch_IFC.md).


</div>

## Usage

1.  Make sure the above requirements are met, and you have access to a running BIMServer instance.
2.  Select menu **Web Tools → <img src="images/WebTools_BimServer.svg" width=16px> [BIM Server](WebTools_BimServer.md)
**
3.  Press the **Connect** button and fill in your credential details
4.  Once the connection to the BIMServer has been made, choose a project to work with from the **Project** drop-down box

## Options

![](images/Arch_Bimserver_panel.jpg )

-   If this is the first time you are connecting to a BIMServer from FreeCAD, press the **Connect** button, and fill in the server URL, your login (which is always an email address) and your password in the dialog box that will pop up. If you wish to log in automatically the next time you will use the BimServer command, check the **save credentials** option (your login and password are not saved by FreeCAD, only a session cookie).
-   Once FreeCAD has successfully connected to a BIMServer instance, the **Connect** button will turn to **Connected**. Click the button again to disconnect. This will also erase the stored session cookie, so you will need to enter your credentials again next time.
-   In order to delete the session cookie manually and reset everything, you can simply delete the BIMServer URL stored in **Edit → Preferences → Arch → BimServer**.
-   The **Open in browser** button will open the web interface of the BIMServer either in FreeCAD\'s internal web browser, or, if you marked that option in **Edit → Preferences → Arch → BimServer**, in an external web browser. This allows for example to create new projects, or analyze the contents stored on the BIMServer.

### Downloading revisions 

-   The **Project** drop-down box will show the available projects stored on the BIMServer. Choose one to see the available revisions for that project.
-   Select one revision and click **Open** to download and open the IFC file corresponding to that revision in FreeCAD.
-   When pressing the **Open** button, a dialog box will open to allow you to save the downloaded IFC file at a location of your choice before opening it. If you press **Cancel**, the file will be saved under a temporary name in the system\'s temporary directory instead.

### Uploading revisions 

-   If you wish to upload a new revision, make sure the right project has been selected in the **Project** drop-down box
-   Choose the **Root object** you wish to upload. It must be either an [Arch Site](Arch_Site.md) or an [Arch Building](Arch_Building.md). Only objects belonging to that root object will be uploaded.
-   Write a **Comment**, that will be the description (name) of the revision.
-   Press the **Upload** button. A dialog box will open to allow you to save the produced IFC file at a location of your choice before uploading it. If you press **Cancel**, the file will be saved under a temporary name in the system\'s temporary directory instead.
