# FreeCAD and DWG Import
{{Fake heading|sub=4|< Back to [[FreeCAD Howto Import Export]]}}

## Why is it hard to support DWG Files in FreeCAD? 

The **DWG format is a closed source binary file format** that is not directly supported by FreeCAD. It requires an external 3rd party file converter to first convert then import the conversion into FreeCAD for use.

## What do I need to be able to import DWG files? 

### LibreDWG

GNU LibreDWG is a free C library to handle DWG files. It aims to be a free replacement for the Open Design Alliance Drawings SDK libraries. Be aware that, since libreDWG is a work-in-progress, it lacks support for some DWG entities.

-   homepage: <https://www.gnu.org/software/libredwg/>
-   license: GPLv2-or-later
-   optional, used to enable import and export of DWG files

#### Installation Windows 

LibreDWG can be configured to work on Windows by downloading and unzipping the appropriate [pre-compiled windows binary](https://github.com/LibreDWG/libredwg/releases) and [adding the folder to your Windows versions system path](https://duckduckgo.com/?t=ffab&q=how+to+add+a+folder+to+your+windows+system+path).

#### Installation Linux/Unix systems 

git clone [https://git.savannah.gnu.org/git/libredwg.git](https://git.savannah.gnu.org/git/libredwg.git)
cd libredwg
mkdir build
cd build
cmake ..
make
make install (or use checkinstall, or simply locate & copy the dwg2dxf utility to your executables path, it will be then autodetected by FreeCAD)

#### Installation openSUSE 

To prevent problems you must use LibreDWG package compiled for the installed openSUSE OS distribution. LibreDWG is typically installed with **YAST** (abbr. Yet another Setup Tool), the Linux operating system\'s setup and configuration tool.

The more experienced user first gets an overview of possible packages provided. **Note:** openSUSE has several options to choose from when downloading LibreDWG. To view these options, visit [Survey of provided LibreDWG packages on openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=libredwg).

For e.g. Intel or AMD 64-bit desktops, laptops, and servers the (x86\_64) release is the one to select. So **libredwg0** and **libredwg-tools** are of the right choice to install.

It is recommended to grab the binary packages directly. Then select the correct distribution for your installed openSUSE OS.

In any terminal/console (root rights required) the installation will be carried out with:

 
```python
zypper install libredwg0 libredwg-tools
```

### ODA File Converter 

-   homepage: <https://www.opendesign.com/guestfiles/oda_file_converter>
-   license: freeware
-   optional, used to enable import and export of DWG files

The ODA File Converter is a small freely available utility that allows to convert between several versions of DWG and DXF files. FreeCAD can use it to offer DWG import and export, by converting DWG files to the DXF format under the hood,then using its standard DXF importer to import the file contents. The restrictions of the [DXF importer](Draft_DXF.md) apply.

#### Installation

On all platforms, only by installing the appropriate package from <https://www.opendesign.com/guestfiles/oda_file_converter>. After installation, if the utility is not found automatically by FreeCAD, you might need to set the path to the converter executable manually. open Edit → Preferences → Import-Export → DWG and fill \"Path to Teigha File Converter\" appropriately.

For more detailed instruction see \[<https://wiki.freecadweb.org/Dxf_Importer_Install#Third_step>: this tutorial\].

#### Usage

The program may be used with the command line interface or the graphical interface. Be sure to convert the DWG files to an ASCII-Format.

Command Line Format is:

1.  Quoted Input Folder
2.  Quoted Output Folder
3.  Output\_version {\"ACAD9\",\"ACAD10\",\"ACAD12\", \"ACAD13\",\"ACAD14\", \"ACAD2000\",\"ACAD2004\", \"ACAD2007\",\"ACAD2010\"}
4.  Output File type {\"DWG\",\"DXF\",\"DXB\"}
5.  Recurse Input Folder {\"0\",\"1\"}
6.  Audit each file {\"0\",\"1\"}
7.  \[optional\] Input file filter (default:\"\*.DWG;\*.DXF\")

**Example for Linux**
ODAFileConverter \"/home/dwg-data\" \"/home/dxf-data\" \"ACAD2010\" \"DXF\" \"0\" \"1\" \"test.dwg\" The second number (audit) needs to be 1 otherwise it fails

**Example for Windows**
\"C:\\Program Files\\ODA\\Teigha File Converter 3.08.2\\TeighaFileConverter.exe\" \"Path-To-Input-Directory\" \"Path-To-Output-Directory\" \"ACAD2010\" \"DXF\" \"0\" \"1\" \"Name-Of-A-Test-File.dwg\"

### QCAD pro 


<small>(v0.20)</small> 

-   homepage: <https://qcad.org/en/qcad-command-line-tools#dwg2dwg>
-   license: commercial
-   optional, used to enable import and export of DWG files

### CADExchanger Workbench 

Installing the CADExchanger Workbench allows for working with DWG files through integration with the paid commercial file converter product [CADExchanger](https://cadexchanger.com/). Just follow the instructions in the [GitHub repository](https://github.com/yorikvanhavre/CADExchanger). You can discuss this workbench on [its forum thread](https://forum.freecadweb.org/viewtopic.php?f=9&t=22227&p=462421).

At the moment, the CADExchanger way is the only one that allows to work with 3D DWG files, by converting them to other 3D formats.

## What are the alternatives? 

### DoubleCAD XT 

There is also DoubleCAD XT (https://www.turbocad.com/content/doublecad-xt-v5). The program is free for personal and commercial use. It requires a free sign-up to receive an activation code via E-Mail. This Program is windows-only. Note: it does not seem to have been updated for years.

### NanoCAD 5.0 

There is also nanoCAD 5.0 (https://nanocad.com/products/nanoCAD/download/). The program is free for personal and commercial use. It requires a free sign-up to receive an activation code via E-Mail. This Program is windows-only.

### Export your AutoCAD files in friendly format 

Exporting your AutoCAD files in a more FreeCAD friendly format, like DXF R12 or R14, SVG, and if version supports it, IGES. All are better alternatives to the DWG format when using FreeCAD.

It is important to note that there is no difference between the contents of a file saved in DWG or DXF formats, provided it is the same version (ex. DWG 2014 vs. DXF 2014). Both formats are maintained by Autodesk, and they both support exactly the same features. The difference is that DWG is closed (machine-encoded) while DXF is open.

## What can I do to help? 

### Promote the use of alternative formats 

Simply put, stop accepting work done in DWG format. In practice, this is often easier said than done. Still, it would not be bad practice for users and supporters of FreeCAD to avoid and reject the DWG format whenever possible.

### Use the LibreDWG library and file bug reports 

In development version as mentioned above you can switch from the proprietary ODA Converter to the free software LibreDWG library for DWG (and DXF) files. Please do this and report any problems you encounter.

  

_ _

---
[documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and DWG Import
