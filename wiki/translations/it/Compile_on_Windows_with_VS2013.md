# Compile on Windows with VS2013/it
 {{Note|Important Note:|This page is a child of the [Complile of Windows](CompileOnWindows.md) page.}} The following procedure will work for compiling on Windows Vista/7/8, for XP an alternate VS tool set is required for VS 2012 and 2013, which has not been tested successfully with the current Libpacks. To target XP(both x32 and x64) it is recommended to use VS2008 and Libpack FreeCADLibs\_11.0\_x86\_VC9.7z

## **Prerequisites**

### Windows Libpack 

FreeCAD is built upon a number of third party libraries. For the users convenience FreeCAD supplies Libpacks that contain all the necessary dependencies so you don\'t have to compile them yourself.

First you\'ll need to download a Windows Libpack. FreeCAD Windows Libpacks are available on the FreeCAD GitHub release page: <https://github.com/FreeCAD/FreeCAD-ports-cache/releases/tag/v0.18>

Libpacks are available for x32 and x64 for VC12(Visual Studio 2013) The Libpacks will work with both the Professional and Express/Community Editions of Visual Studio. Choose the Libpack relevant to your system architecture and Compiler.

Assuming that your Win 7 or later, x64, and planning to use VS2013 Community Edition choose:

FreeCADLibs\_11.11\_x64\_VC12.7z

Extract the Libpack to a directory on your hard drive.

You can download 7-zip if you need it here: <http://www.7-zip.org/>

### Source Code 

#### Using Git(Preferred) 

Next you will need to install git to be able to download the source code. You can get Git here: <http://git-scm.com/downloads>

Some information how to set-up a local tracking branch and a working branch can be found here:

[Source code management](Source_code_management.md)

To create a local tracking branch and download the source code you need to open a terminal(command prompt) and cd to the directory you want the source, then type:

git clone <git://git.code.sf.net/p/free-cad/code> free-cad-code

Now you have the source code and the tools you\'ll need to compile FreeCAD on Windows.

#### Download Snapshot .zip(Alternate) 


{{Note|Note:|This is Source Cade Snapshot not Development Snapshot pre-compiled binaries.
}}

<http://sourceforge.net/p/free-cad/code/ci/master/tarball>

You will need to extract this to a directory using 7zip or Window\'s default .zip extractor.

**NOTE: In order for Cmake to properly update your \"About FreeCAD\" information git must be installed and be present in your PATH environment variable, Therefore downloading with git is preferred.**

### Cmake

Next you will need Cmake, you can get it here: <http://www.cmake.org/download/>

FreeCAD 0.15.xxxx master will configure and generate with Cmake 2.x.x or 3.x.x, you can download the latest version. Older versions of FreeCAD require Cmake 2.x.x You should choose the non-default option to add Cmake to your system PATH environment variable.

### Visual Studio 

Lastly you will need the C-compiler. MS VS 12 2013 Community Edition Update 4 is Free for personal and Open Source Projects. It can be downloaded here:

<http://www.visualstudio.com/en-us/news/vs2013-community-vs.aspx>

## **Configuring and Generating with Cmake** 

### First Pass 

Start the CMake GUI by double-clicking on the desktop icon created during installation.

Specify source folder (This is where you cloned or extracted the source code)

Specify build folder (This is where you want to build the source, if it doesn\'t exist Cmake will prompt you to create it)

Click Configure

Specify the generator as Visual Studio 12 x64(or the alternate C-Compiler you are using)

This will begin configuration and should fail because the location of FREECAD\_LIBPACK\_DIR is unset.

Expand the FREECAD category and set: 
```python
FREECAD_LIBPACK_DIR          "...\Path\to\Libpack" (Ex: C:\user\USERNAME\FreeCADLibs_11.0_x64_VC12)
FREECAD_USE_EXTERNAL_PIVY    (Check)
FREECAD_USE_FREETYPE         (Check)
``` FREETYPE is optional. It is necessary to take advantage of the DRAFT Work Bench\'s Shape String functionality. Under normal situations it is a desirable option.

### Configure and Generate 

Click Configure again (There should be no errors)

Click Generate (missing doxgen is OK, unless you are a developer and need the source documentation)

Close Cmake

## **Dependencies**

**Copy The Libpack\\bin folder into the new build folder CMake created.**

You could put the Libpack in your system PATH environment variable. but you still are required to copy some files?

## **Building with Visual Studio** 

Start Visual Studio 12 2013 by clicking on the desktop icon created at installation.

Open the project by: File -\> Open -\> Project/Solution

Open FreeCAD\_Trunk.sln from the build folder CMake created

Switch the Solutions Configuration drop down at the top to **Release** **X64**

Build -\> Build Solution

This will take a long time\...

If you don\'t get any errors your done. Exit Visual Studio and start FreeCAD by double clicking the FreeCAD icon in the bin folder of the build directory.




[Category:Developer\_Documentation](Category:Developer_Documentation.md) [Category:Developer](Category:Developer.md)
