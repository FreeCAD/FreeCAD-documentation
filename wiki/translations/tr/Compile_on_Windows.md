# Compile on Windows/tr
{{TOCright}}

This page explains step by step **how to compile FreeCAD 0.19 or newer on Windows** using Microsoft\'s MSVC compiler. For information on using MSYS2/MinGW see [Compile on MinGW](Compile_on_MinGW.md). For other platforms see [Compiling](Compiling.md).

## Prerequisites

Compiling FreeCAD on Windows requires several tools and libraries.

### Required

-   A compiler. FreeCAD is tested with Visual Studio (MSVC)---other compilers may work, but instructions for use are not included here. More details in [\#Compiler](#Compiler.md), below.

-   [Git](http   *//git-scm.com/) (There are also GUI frontends available for Git, see the next section.)

-   [CMake](https   *//cmake.org/download/) version 3.11.x or newer.  *Hint   ** Choosing the option *Add CMake to the system PATH for all users* when installing CMake will make CMake accessible from the Windows command prompt, which can be useful.

-   LibPack (also called FreeCADLibs). This is a single package containing all of the libraries necessary to compile FreeCAD on Windows. Download the version of the LibPack that corresponds to the version of FreeCAD you want to compile. To compile FreeCAD 0.19 or the latest development version 0.20, download the [LibPack for 0.19/0.20](https   *//github.com/apeltauer/FreeCAD/releases/tag/LibPack_12.5.4) (64-bit only). Extract the LibPack to a convenient location. (If your computer does not recognize the .7z extension, you should install the program [7-zip](https   *//www.7-zip.org).)  **Note**   * It is highly recommended to compile FreeCAD with the compiler version the LibPack is designed for. For example, you might run into problems compiling FreeCAD 0.19 using MSVC 15 because the LibPack for 0.19 is designed to be built with MSVC 17.

### Optional programs 

-   A GUI frontend for Git. There are several frontends available, see [this list](https   *//en.wikipedia.org/wiki/Comparison_of_Git_GUIs). The main benefit of a frontend is that you don\'t have to learn the Git commands to get the source code of FreeCAD or to send patches to the GitHub repository of FreeCAD.

In the following we describe source code handling using the [TortoiseGit](https   *//tortoisegit.org/) frontend. This frontend integrates directly into Windows file explorer and has a large user community to get help in case you have problems.

-   [NSIS](http   *//sourceforge.net/projects/nsis/) is used to generate the FreeCAD Windows installer.

### Source code 

Now you can get the source code of FreeCAD   *

#### Using a frontend 

When using the [Git frontend](https   *//en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit   *

1.  Create a new folder where the source code will be downloaded.
2.  Right-click on this folder in the Windows file explorer and select **Git Clone** in the context menu.
3.  A dialog will appear. In it, enter the URL for the FreeCAD Git repository

*<https   *//github.com/FreeCAD/FreeCAD.git>*

and click **OK**.

The latest source code will be downloaded from the FreeCAD Git repository and the folder will be tracked by Git.

#### Using the command line 

To create a local tracking branch and download the source code, open a terminal (command prompt) and switch there to the directory you want the source, then type   *


```python
git clone https   *//github.com/FreeCAD/FreeCAD.git
```

### Compiler

The default (recommended) compiler is MS Visual Studio (MSVC). Though it may be possible to use other compilers, for example gcc via Cygwin or MinGW, it is not tested or covered here.

You can get a free version of MSVC (for individual usage) by downloading the [*Community* edition of MS Visual Studio](https   *//visualstudio.microsoft.com/vs/community/).

For those who want to avoid installing the huge MSVC for the mere purpose of having a compiler, see [CompileOnWindows - Reducing Disk Footprint](CompileOnWindows_-_Reducing_Disk_Footprint.md).

**Note   *** Although the *Community* edition of MSVC is free, to use the IDE for more than a 30-day trial period you must create a Microsoft account. If you will only compile using the command line, you don\'t need the IDE and thus no Microsoft account.

As a free and OpenSource alternative IDE you can use [KDevelop](https   *//www.kdevelop.org/download). You can use KDevelop to modify and write C++ code but must use the command line to compile.

### Optional system path configuration 

Optionally you can include the paths to some folders to the system PATH variable. This is helpful if you want to access programs in these folders from the command line/powershell or if you want special programs to be found by the compiler or CMake. Besides this, adding folders to the PATH might be necessary if you did not use the corresponding options when installing the program.

-   You can include the folder of your LibPack in your system PATH variable. This is useful if you plan to build multiple configurations/versions of FreeCAD.
-   If you did not use the option to add CMake to the PATH while installing it, add its installation folder

*C   *Program Files\\CMake\\bin* to the PATH.

-   If you did not use the option to add TortoiseGit to the PATH while installing it, add its installation folder

*C   *Program Files\\TortoiseGit\\bin* to the PATH.

To add folder paths to the PATH variable   *

1.  In the Windows Start menu Right click on *Computer* and choose *Properties*.
2.  In the appearing dialog click on *Advanced system settings*.
3.  Another dialog will open. Click there in the tab *Advanced* on **Environment Variables**.
4.  Again another dialog will open. Select then the variable *Path* and click on **Edit**.
5.  And again another dialog will open. Click there on **New** and add to path to the folder of Git or the LibPack.
6.  Finally press **OK** and close all dialogs by pressing **OK** as well.

## Configuration

Once you have all of the necessary tools, libraries, and FreeCAD source code, you are ready to begin the configuration and compilation process. This process will proceed in five steps   *

1.  Run CMake once to examine your system and begin the configuration progress (this will report that it failed).
2.  Adjust necessary CMake settings to set the locations of the LibPack and enable Qt5.
3.  Re-run CMake to finalize the configuration (this time it should succeed).
4.  Use CMake to generate the Visual Studio build system.
5.  Use Visual Studio to build FreeCAD.

### CMake

First, configure the build environment using CMake   *

1.  Open the CMake GUI
2.  Specify the source folder of FreeCAD.
3.  Specify a build folder (do not use the source folder \-- CMake will create this folder if it does not exist).
4.  Click **Configure**.
5.  In the dialog that appears specify the generator you want to use   * in most cases you will use the defaults in this dialog. For the standard MS Visual Studio use *Visual Studio xx 2yyy* where xx is the compiler version and 2yyy the year of its release. It is recommended to use the default option *Use default native compilers*.

**Note   *** It is important to specify the correct bit variant. If you have the 64-bit variant of the LibPack you must also use the x64 compiler.

This will begin the configuration and *will fail* because of missing settings. This is normal, you have not yet specified the location of the LibPack. However, there are other failures that might occur that require some further action on your part.

If it fails with the message that Visual Studio could not be found, the CMake support in MSVC is not yet installed. To do this   *

1.  Open the MSVC IDE
2.  Use the menu Tools → Get Tools and Features
3.  In the *Workloads* tab enable *Desktop development with C++*
4.  On the right side you should now see that the component *Visual C++ tools for CMake* will be installed.
5.  Install it.

If it fails with a message about the wrong Python version or missing Python, then   *

1.  Use the \"Search   *" box in CMake to search for the string \"Python\"
2.  If you see there a path like *C   */Program Files/Python38/python.exe*, CMake recognized the Python that is already installed on your PC, but that version is not compatible with the LibPack. Since the LibPack includes a compatible version of Python, modify the following Python settings in CMake to its paths (assuming the LibPack is in the folder *D   *FreeCAD-build\\FreeCADLibs\_12.5.2\_x64\_VC17*)   *

![](images/CMake_Python_settings.png )

If there is no error about Visual Studio or Python, everything is fine, but CMake does not yet know all necessary settings. Therefore now   *

1.  Search in CMake for the variable **FREECAD\_LIBPACK\_DIR** and specify the location of the LibPack folder you downloaded earlier.
2.  Only if building FreeCAD 0.19, search for the variable **BUILD\_QT5** and enable this option.
3.  Click **Configure** again.

There should now be no errors. If you continue to encounter errors that you cannot diagnose, visit the [Install/Compile forum](https   *//forum.freecadweb.org/viewforum.php?f=4) on the FreeCAD forum website. If CMake proceeded correctly, click on **Generate**. After this is done you can close CMake and start the compilation of FreeCAD using Visual Studio. However, for the first compilation keep it open in case you want or need to change some options for the build process.

**Note   *** When compiling FreeCAD 0.19, the CMake variable **BUILD\_ENABLE\_CXX\_STD** will be set to **C++14** while for FreeCAD 0.20 it will be set to **C++17**. This is because FreeCAD 0.20 requires at least the C++ language standard version 17. So when you compiled the last time FreeCAD 0.19 it is necessary to re-run CMake for FreeCAD 0.20 to change the C++ language standard.

### Options for the build process 

The CMake build system gives you control over some aspects of the build process. In particular, you can switch on and off some features or modules using CMake variables.

Here is a description of some of these variables   *

  Variable name                            Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Default
    
  BUILD\_XXX                               Build FreeCAD with the component XXX. If you don\'t want/need to compile e.g. the workbench *OpenSCAD*, disable the variable *BUILD\_OPENSCAD*. FreeCAD will then not have this workbench. **Note   *** Some components are required for other components. If you for example uncheck *BUILD\_ROBOT* CMake will inform you that then the component *Path* cannot be compiled correctly. Therefore check the CMake output after you changed a BUILD\_XXX option!                                                                                                       depends
  BUILD\_ENABLE\_CXX\_STD                  The version of the C++ language standard. **C++14** is the highest possible for FreeCAD 0.19 while at least **C++17** is required for FreeCAC 0.20. See also the note in section [Building with Visual Studio 15 (2017) and 16 (2019)](#Release_Build.md)                                                                                                                                                                                                                                                                                                  depends
  BUILD\_FLAT\_MESH                        Necessary to have a build that includes the [CreateFlatMesh feature](MeshPart_CreateFlatMesh.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                           OFF
  CMAKE\_INSTALL\_PREFIX                   The output folder when building the target *INSTALL*, see also section [Running and installing FreeCAD](#Running_and_installing_FreeCAD.md)                                                                                                                                                                                                                                                                                                                                                                                                                Windows default program installation folder
  FREECAD\_COPY\_DEPEND\_DIRS\_TO\_BUILD   Copies depending libraries needed to execute the FreeCAD.exe to the build folder. See also section [Running and installing FreeCAD](#Running_and_installing_FreeCAD.md). **Note   *** the options FREECAD\_COPY\_XXX only appear if the libraries were not already copied. So when you change to another LibPack version, it is important to delete all folders in your build folder, except of the LibPack folder. In CMake delete the cache and start as if you compile for the first time and you will get the FREECAD\_COPY\_XXX options.   OFF
  FREECAD\_COPY\_LIBPACK\_BIN\_TO\_BUILD   Copies the LibPack binaries needed to execute the FreeCAD.exe to the build folder. See also section [Running and installing FreeCAD](#Running_and_installing_FreeCAD.md).                                                                                                                                                                                                                                                                                                                                                                                  OFF
  FREECAD\_COPY\_PLUGINS\_BIN\_TO\_BUILD   Copies Qt\'s plugin files needed to execute the FreeCAD.exe to the build folder. See also section [Running and installing FreeCAD](#Running_and_installing_FreeCAD.md).                                                                                                                                                                                                                                                                                                                                                                                    OFF
  FREECAD\_LIBPACK\_USE                    Switch the usage of the FreeCAD LibPack on or off                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ON
  FREECAD\_LIBPACK\_DIR                    Directory where the LibPack is                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     FreeCAD\'s source code folder
  FREECAD\_RELEASE\_PDB                    Create debug libraries also for release builds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ON
  FREECAD\_USE\_MP\_COMPILE\_FLAG          Adds the /MP (multiprocessor) option to the Visual Studio projects, enabling speedups on multi-core CPUs. This can greatly accelerate builds on modern processors.**Note   *** If you turn off **FREECAD\_USE\_PCH**, the compilation can quickly overload your heap space, even if you have 16 GB RAM.                                                                                                                                                                                                                                                 ON
  FREECAD\_USE\_PCH                        [Precompiles the headers](https   *//en.wikipedia.org/wiki/Precompiled_header) in order to save compilation time.                                                                                                                                                                                                                                                                                                                                                                                                                                                     ON
  FREECAD\_USE\_PYBIND11                   Includes the [PyBind11](https   *//github.com/pybind/pybind11) library. Necessary to have a build that includes the [CreateFlatMesh feature](MeshPart_CreateFlatMesh.md).                                                                                                                                                                                                                                                                                                                                                                                     OFF

## Building FreeCAD 

Depending on your compiler, the process for building FreeCAD will be slightly different. In the following sections you known workflows are described. If you are building with Qt Creator, jump to [Building with Qt Creator](#Building_with_Qt_Creator.md), otherwise proceed directly   *


<div class="mw-collapsible mw-collapsed toccolours">

### Building with Visual Studio 15 (2017), 16 (2019), and 17 (2022) 


<div class="mw-collapsible-content">

#### Release Build 

1.  Start the Visual Studio IDE. This can either be done by pressing the button *Open Project* in the CMake GUI or by double-clicking on the file *FreeCAD.sln* that you find in your build folder.
2.  In the toolbar of the MSVC IDE assure that you use for the first compilation *Release*.
3.  There is a window called *Solution Explorer*. It lists all possible compilation targets. To start a full compilation, right-click on the target **ALL\_BUILD** and then choose **Build**.

This will now take quite a long time.

To compile a ready-to use FreeCAD, compile the target *INSTALL*, see section [Running and installing FreeCAD](#Running_and_installing_FreeCAD.md).

If you don\'t get any errors you are done. **Congratulations!** You can exit MSVC or keep it open.

**Note   *** FreeCAD 0.20 requires at least the C++ language standard version 17 but the 3rd-party component *flann* from the LibPack is not yet ready for this. Therefore you will get compilation errors for the target *ReverseEngineering*. To fix this, right-click on this target in the MSVC solution explorer and select in the context menu the last entry *Properties*. In the appearing dialog change the **C++ Language Standard** to **ISO C++14**. Finally build the target **ALL\_BUILD** again.

#### Debug Build 

For a debug build it is necessary that the Python is used that is included in the LibPack. To assure this   *

1.  Search in the CMake GUI for \"Python\"
2.  If you see there a path like *C   */Program Files/Python38/python.exe*, CMake recognized the Python that is installed on your PC and not the one of the LibPack. In this case adapt these different Python settings in CMake to this (assuming the LibPack is in the folder *D   *FreeCAD-build\\FreeCADLibs\_12.5.2\_x64\_VC17*)   *

![](images/CMake_Python_settings.png )

Now

1.  Start the Visual Studio IDE. This can either be done by pressing the button *Open Project* in the CMake GUI or by double-clicking on the file *FreeCAD.sln* that you find in your build folder.
2.  In the toolbar of the MSVC IDE assure that you use for the first compilation *Debug*.
3.  There is a window called *Solution Explorer*. It lists all possible compilation targets. To start a full compilation, right-click on the target **ALL\_BUILD** and then choose **Build** in the context menu.

This will now take quite a long time. If there were no compilation errors, you can start the debug build   *

1.  Right-click on the target **FreeCADMain** and then choose **Set as Startup Project** in the context menu.
2.  Finally click in the toolbar on the button with the green triangle named **Local Windows Debugger**.

This will start the debug build of FreeCAD and you can use the MSVC IDE to debug it.

#### Video Resource 

An English language tutorial that begins with configuration in CMake Gui and continues to the \Build\ command in Visual Studio 16 2019 is available unlisted on YouTube at [Tutorial   * Build FreeCAD from source on Windows 10](https   *//youtu.be/s4pHvlDOSZQ).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Building with Qt Creator (outdated) 


<div class="mw-collapsible-content">

#### Installation and configuration of Qt Creator 

-   Download and install [Qt Creator](https   *//www.qt.io/offline-installers)
-   Tools → Options → Text Editor → Behavior tab   *
    -   File Encodings → Default Encodings   *
    -   Set to   * **ISO-8859-1 /\...csISOLatin1** (Certain characters create errors/warnings with Qt Creator if left set to UTF-8. This seems to fix it.)
-   Tools → Options → Build & Run   *
    -   CMake tab
        -   Fill Executable box with path to cmake.exe
    -   Kits tab
        -   Name   * MSVC 2008
        -   Compiler   * Microsoft Visual C++ Compiler 9.0 (x86)
        -   Debugger   * Auto detected\...
        -   Qt version   * None
    -   General tab
        -   Uncheck   * Always build project before deploying it
        -   Uncheck   * Always deploy project before running it

#### Import project and building 

-   File → Open File or Project
-   Open **CMakeLists.txt** which is in the top level of the source
-   This will start CMake
-   Choose build directory and click next
-   Set generator to **NMake Generator (MSVC 2008)**
-   Click Run CMake. Follow the instructions depicted above to configure CMake to your liking.

Now FreeCAD can be built

-   Build → Build All
-   This will take a long time\...

Once complete, it can be run   * There are 2 green triangles at the bottom left. One is debug. The other is run. Pick whichever you want.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Command line build 


<div class="mw-collapsible-content">

The steps how to compile from the command line depends on the compiler. For MSVC 2017 the steps are   *

1.  In Windows start menu go to **Visual Studio 2017 → Visual Studio Tools** and choose **Developer Command Prompt for VS 2017**
2.  Change to your build folder.
3.  Execute the command


```pythonmsbuild ALL_BUILD.vcxproj /p   *Configuration=Release```

or


```pythonmsbuild INSTALL.vcxproj /p   *Configuration=Release```

These steps can also be automaized. Here is for example a solution for MSVC 2017   *

1.  Download the script [compile-FC.txt](https   *//forum.freecadweb.org/download/file.php?id=92135).
2.  Rename it to *compile-FC.bat*
3.  In Windows file explorer Shift+Right-click on your build folder and use from the context menu *Command prompt here*.
4.  Execute the command


```pythoncompile-FC install```

Instead of calling **compile-FC** with the option *install* you can also use *debug* or *release*   *

*debug*   - compile FreeCAD in debug configuration

*release* - compile FreeCAD in release configuration

*install*    - compile FreeCAD in release configuration and create an install setup


</div>


</div>

## Running and installing FreeCAD 

There are 2 methods to run the compiled FreeCAD   *

*Method 1*   * You execute the FreeCAD.exe that you find in your build folder in the subfolder *bin*

*Method 2*   * You build the target *INSTALL*

Method 2 is the simpler one because it automatically assures that all libraries needed to run the FreeCAD.exe are in the correct folder. The FreeCAD.exe and the libraries will be output in the folder you specified in the CMake variable *CMAKE\_INSTALL\_PREFIX*.

For Method 1 you need to put the libraries into the *bin* folder of your build folder (where the FreeCAD.exe is). This can easily be done   *

1.  Open the CMake GUI.
2.  Search there for the variable option *FREECAD\_COPY\_DEPEND\_DIRS\_TO\_BUILD* and check it. If there is no such option, the libraries were already copied, see the [description of the options](#Options_for_the_build_process.md).
3.  Search there for the variable option *FREECAD\_COPY\_LIBPACK\_BIN\_TO\_BUILD* and check it.
4.  Search there for the variable option *FREECAD\_COPY\_PLUGINS\_BIN\_TO\_BUILD* and check it.
5.  Click on **Configure**. At the end of the configuration CMake will automatically copy the necessary libraries from the LibPack folder.

## Updating the build 

FreeCAD is very actively developed. Therefore its source code changes almost daily. New features are added and bugs are fixed. To benefit from these source code changes, you must rebuild your FreeCAD. This is done in two steps   *

1.  Updating the source code
2.  Recompilation

### Updating the source code 

#### Using a frontend 

When using the [Git frontend](https   *//en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit   *

1.  Right-click on your FreeCAD source code folder in the Windows file explorer and select in the context menu **Pull**.
2.  A dialog will appear. Select there what development branch you want to get. **master** is the main branch. Therefore use this unless you want to compile a special new feature from a branch that has not yet been merged to *master*. (For more about Git branches, see [Git development process](Source_code_management#Git_development_process.md).)

Finally click **OK**.

#### Using the command line 

Open a terminal (command prompt) and switch there to your source directory. Then type   *


```python
git pull https   *//github.com/FreeCAD/FreeCAD.git master
```

where *master* the the name of the main development branch. If you want to get code from another branch, use its name instead of *master*.

### Recompilation

1.  Open the MSVC IDE by double-clicking either on the file *FreeCAD.sln* or on the file *ALL\_BUILD.vcxproj* in your build folder.
2.  Continue with step 2 from section [Building with Visual Studio 15 2017](#Building_with_Visual_Studio_15_2017.md).

## Tools

In order to join the FreeCAD development you should compile and install the following tools   *

### Qt Designer plugin 

FreeCAD uses [Qt](https   *//en.wikipedia.org/wiki/Qt_(software)) as toolkit for its user interface. All dialogs are setup in UI-files that can be edited using the program [Qt Designer](https   *//doc.qt.io/qt-5/qtdesigner-manual.html) that is part of any Qt installation and also included in the LibPack. FreeCAD has its own set of Qt widgets to provide special features like adding a unit to input fields and to set preferences properties.

#### Installation

To make Qt Designer aware of the FreeCAD widgets, you must

1.  Download the [ZIP file](https   *//github.com/donovaly/FreeCAD-Qt-Designer-plugin/releases/tag/Qt-5.15.x-1). (Compiled using Qt 5.15, see [below](#Compilation.md).)
2.  Extract the DLL file from the ZIP.

-   If you use the LibPack   * to the folder*\~\\FreeCADLibs\_12.5.4\_x64\_VC17\\bin\\designer*Since there will only be a *bin* folder and you must first create the *designer* subfolder.
-   If you have a full Qt installation   * you can choose between the folder*C   *Qt\\5.15.2\\msvc2019\_64\\plugins\\designer*or*C   *Qt\\5.15.2\\msvc2019\_64\\bin\\designer* (you must first create the *designer* subfolder.)(adapt the paths to your installation!).

(Re)Start Qt Designer and check its menu **Help → Plugins**. If the plugin **FreeCAD\_widgets.dll** is listed as being loaded, you can now design and change FreeCAD\'s .ui files. If not, you must [compile](#Compilation.md) the DLL by yourself.

If you prefer using [Qt Creator](https   *//en.wikipedia.org/wiki/Qt_Creator) instead of Qt Designer, the DLL must be placed in this folder   **C   *Qt\\Qt5.15.2\\Tools\\QtCreator\\bin\\plugins\\designer*(Re)Start Qt Creator, switch to the mode **Design** and then check the menu **Tools → Form Editor → About Qt Designer Plugins**. If the plugin **FreeCAD\_widgets.dll** is listed as being loaded, you can now design and change FreeCAD\'s .ui files. If not, you must [compile](#Compilation.md) the DLL by yourself.

#### Compilation

The DLL cannot be loaded as plugin if it was compiled using another Qt version than the one your Qt Designer/Qt Creator is based on. In this case you must compile the DLL by yourself. This is done the following way   *

1.  Change to the FreeCAD source folder*\~\\src\\Tools\\plugins\\widget*
2.  Open a *x64 Native Tool Command Prompt* using the Windows Start menu and change within it to the above folder. It is important that it is the x64 version of the command prompt!
3.  Execute this command *D   *FreeCAD-build\\FreeCADLibs\_12.5.4\_x64\_VC17\\bin\\qmake -t vclib plugin.pro*for a full Qt installation it is*C   *Qt\\5.15.2\\msvc2019\_64\\bin\\qmake -t vclib plugin.pro* (adapt the paths to your installation!)
4.  The call of *qmake* created the file **FreeCAD\_widgets.vcxproj** in the folder *\~\\src\\Tools\\plugins\\widget*. Double-click on it and the MSVC IDE will open.
5.  In the toolbar of the MSVC IDE assure that you use the compilation target *Release*.
6.  There is a window called *Solution Explorer*. Right-click there on **FreeCAD\_widgets** and then choose **Build**.
7.  As result you should now have a **FreeCAD\_widgets.dll** in the folder *\~\\src\\Tools\\plugins\\widget\\release* that you can install as plugin as described above.

### Thumbnail Provider 

FreeCAD has the feature to provide preview thumbnails for \*.FCStd files. That means that in the Windows file explorer \*.FCStd files are shown with a screenshot of the model it contains. To provide this feature, FreeCAD needs to have the file **FCStdThumbnail.dll** installed to Windows.

#### Installation 

The DLL is installed this way   *

1.  Download [this ZIP file](https   *//forum.freecadweb.org/download/file.php?id=13404) and extract it.
2.  Open a Windows command prompt with administrator privileges (these privileges are a requirement).
3.  Change to the folder where the DLL is.
4.  Execute this command 
```pythonregsvr32 FCStdThumbnail.dll```

So check if it works, assure that in FreeCAD the preferences option **[Save thumbnail into project file when saving document](Preferences_Editor#Document.md)** is enabled and save a model. Then view in Windows Explorer the folder of the saved model using a symbol view. You should now see a screenshot of the model in the folder view.

#### Compilation 

To compile the FCStdThumbnail.dll

1.  Change to the FreeCAD source folder*\~\\src\\Tools\\thumbs\\ThumbnailProvider*
2.  Open the CMake GUI
3.  Specify there as source folder the one you are currently in.
4.  Use the same folder as build folder.
5.  Click **Configure**
6.  In the appearing dialog, specify the generator according to the one you want to use. For the standard MS Visual Studio use *Visual Studio xx 2yyy* where xx is the compiler version and 2yyy the year of its release. It is recommended to use the default option *Use default native compilers*.**Note   *** It is important to specify the correct bit variant. If you have the 64bit variant of LibPack you must also use the x64 compiler.
7.  Click on **Generate**.
8.  You should now have the file **ALL\_BUILD.vcxproj** in the folder *\~\\src\\Tools\\thumbs\\ThumbnailProvider*. Double-click on it and the MSVC IDE will open.
9.  In the toolbar of the MSVC IDE assure that you use the compilation target *Release*.
10. There is a window called *Solution Explorer*. Right-click there on **ALL\_BUILD** and then choose **Build**.
11. As result you should now have a **FCStdThumbnail.dll** in the folder *\~\\src\\Tools\\thumbs\\ThumbnailProvider\\release* that you can install as described above.

## Compiling OpenCASCADE 

The standard Libpack comes with a version of OpenCASCADE that is suitable for general use. However, under some circumstances you may wish to compile against an alternate version of OpenCASCADE, such as one of their official releases, or a patched fork. Note that there is no guarantee that FreeCAD will work with all versions of OpenCASCADE, and using a non-Libpack version is for advanced users only. Note also that if you are using the Netgen library, it uses OpenCASCADE for some of its functionality and must be compiled against the same version of OpenCASCADE that you use when compiling FreeCAD.

The process for building a custom version of OpenCASCADE is similar to that for FreeCAD, and can make use of the FreeCAD Libpack that you have already downloaded to provide the third-party dependencies it needs (Freetype and Tcl/Tk).

First obtain the OpenCASCADE source code, either directly from the release page at [OpenCASCADE.org](https   *//old.opencascade.com/content/latest-release), via [git](https   *//git.dev.opencascade.org/repos/occt.git), or by cloning someone else\'s fork, such as [the \"blobfish\" fork](https   *//gitlab.com/blobfish/occt) maintained by FreeCAD forum member [tanderson69](https   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=208).

Next, use CMake to configure the build system in a similar manner to building FreeCAD. Notable CMake options for OpenCASCADE are   *

-   **3RDPARTY\_DIR** - The location of your thrid-party libraries, typically set to your FreeCAD Libpack directory
-   **INSTALL\_DIR** - Where to install the finished libraries. A good practice is to use an isolated directory on your system, rather than installing globally, or overwriting the Libpack\'s version.

Finally, open the project in Visual Studio and build the ALL\_BUILD and then INSTALL targets.

Once you have generated the appropriate DLLs for OpenCASCADE (there are many of them), you will need to rebuild FreeCAD. Open CMake and set up the source and build directories of a FreeCAD build as directed above. It is generally a good idea to use a new build directory for this alternate version of OpenCASCADE so that it is easy to switch back to your old version of FreeCAD if something goes wrong, and to set up an install directory so you can ensure the correct libraries are in place. In addition to the CMake variables discussed above, set the OpenCASCADE\_DIR variable to the location of the cmake folder containing your OpenCASCADE build information. For example   *

CMAKE_INSTALL_PREFIX    C   */Users/JaneDoe/Work/FreeCAD_occt751-install/
OpenCASCADE_DIR         C   */Users/JaneDoe/Work/opencascade-7.5.1-install/cmake/

Once you have used CMake to generate the build files for FreeCAD, open it in Visual Studio, build it, and then run build on the INSTALL target.

## References

See also

-   [Compiling - Speeding up](Compiling_(Speeding_up).md)







[Category   *Developer\_Documentation](Category_Developer_Documentation.md) [Category   *Developer](Category_Developer.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Windows/tr
