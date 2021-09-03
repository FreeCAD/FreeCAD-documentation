 {{TOCright}}


{{Fake heading|sub=4|< Back to [[FreeCAD Howto Import Export]]}}


<div class="mw-translate-fuzzy">

## 왜 DWG 파일을 FreeCAD 안으로 import 할 수 없나요? {#왜_dwg_파일을_freecad_안으로_import_할_수_없나요}

DWG 형식은 닫힌 소스 이진 파일 형식이며 FreeCAD에서 직접 지원하지 않습니다. It requires an external 3rd party file converter to first convert then import the conversion into FreeCAD for use.


</div>

The **DWG format is a closed source binary file format** that is not directly supported by FreeCAD. It requires an external 3rd party file converter to first convert then import the conversion into FreeCAD for use.

Note that at this time, it is not possible to import 3D DWG in FreeCAD. 3D data is embedded as binary .SAT (ACIS) data, a proprietary and undocumented format.


<div class="mw-translate-fuzzy">

## DWG 파일을 import 하려면 필요한 것은? {#dwg_파일을_import_하려면_필요한_것은}


</div>


<div class="mw-translate-fuzzy">

### ODA Converter (formerly Teigha Converter) {#oda_converter_formerly_teigha_converter}

-   홈페이지: <https://www.opendesign.com/guestfiles/oda_file_converter>
-   라이선스: freeware
-   optional, used to enable import and export of DWG files


</div>

-   homepage: <https://www.opendesign.com/guestfiles/oda_file_converter>
-   license: freeware
-   optional, used to enable import and export of DWG files

The ODA Converter is a small freely available utility that allows to convert between several versions of DWG and DXF files. FreeCAD can use it to offer DWG import and export, by converting DWG files to the DXF format under the hood,then using its standard DXF importer to import the file contents. The restrictions of the [DXF importer](Draft_DXF.md) apply.


<div class="mw-translate-fuzzy">

#### 설치

On all platforms, only by installing the appropriate package from <https://www.opendesign.com/guestfiles/oda_file_converter>. After installation, if the utility is not found automatically by FreeCAD, you might need to set the path to the converter executable manually. open Edit → Preferences → Import-Export → DWG and fill \"Path to Teigha File Converter\" appropriately.


</div>

On all platforms, only by installing the appropriate package from <https://www.opendesign.com/guestfiles/oda_file_converter>. After installation, if the utility is not found automatically by FreeCAD, you might need to set the path to the converter executable manually. open Edit → Preferences → Import-Export → DWG and fill \"Path to Teigha File Converter\" appropriately.


<div class="mw-translate-fuzzy">

더 자세한 설명을 보려면 \[<http://www.freecadweb.org/wiki/index.php?title=Dxf_Importer_Install#Third_step>: this tutorial\].


</div>


<div class="mw-translate-fuzzy">

#### 사용법

The program may be used with the command line interface or the graphical interface. Be sure to convert the DWG files to an ASCII-Format.


</div>

The program may be used with the command line interface or the graphical interface. Be sure to convert the DWG files to an ASCII-Format.

명령 라인 형식:

1.  Quoted Input Folder
2.  Quoted Output Folder
3.  Output\_version {\"ACAD9\",\"ACAD10\",\"ACAD12\", \"ACAD13\",\"ACAD14\", \"ACAD2000\",\"ACAD2004\", \"ACAD2007\",\"ACAD2010\"}
4.  Output File type {\"DWG\",\"DXF\",\"DXB\"}
5.  Recurse Input Folder {\"0\",\"1\"}
6.  Audit each file {\"0\",\"1\"}
7.  \[optional\] Input file filter (default:\"\*.DWG;\*.DXF\")

**리눅스용 예**
ODAFileConverter \"/home/dwg-data\" \"/home/dxf-data\" \"ACAD2010\" \"DXF\" \"0\" \"1\" \"test.dwg\" The second number (audit) needs to be 1 otherwise it fails

**Example for Windows**
\"C:\\Program Files\\ODA\\Teigha File Converter 3.08.2\\TeighaFileConverter.exe\" \"Path-To-Input-Directory\" \"Path-To-Output-Directory\" \"ACAD2010\" \"DXF\" \"0\" \"1\" \"Name-Of-A-Test-File.dwg\"

### CADExchanger Workbench {#cadexchanger_workbench}

Installing the CADExchanger Workbench allows for working with DWG files through integration with the paid commercial file converter product [CADExchanger](https://cadexchanger.com/). Just follow the instructions in the [GitHub repository](https://github.com/yorikvanhavre/CADExchanger). You can discuss this workbench on [its forum thread](https://forum.freecadweb.org/viewtopic.php?f=9&t=22227&p=462421).

At the moment, the CADExchanger way is the only one that allows to work with 3D DWG files, by converting them to other 3D formats.

## FreeCAD v0.19 and LibreDWG {#freecad_v0.19_and_libredwg}

As from 0.19, FreeCAD doesn\'t need the ODA converter anymore and can use libreDWG directly. Be aware that, since libreDWG is a work-in-progress, depending on your file, the results might not be the same.

-   homepage: <https://www.gnu.org/software/libredwg/>
-   license: GPLv2-or-later
-   optional, used to enable import and export of DWG files

GNU LibreDWG is a free C library to handle DWG files. It aims to be a free replacement for the Open Design Alliance Drawings SDK libraries.

## Installation

### AppImage releases {#appimage_releases}

LibreDWG is included in v 0.19\_pre appimages[1](https://forum.freecadweb.org/viewtopic.php?f=8&t=39827&start=20#p372933)

### Windows

LibreDWG can be configured to work on Windows by downloading and unzipping the appropriate [pre-compiled windows binary](https://github.com/LibreDWG/libredwg/releases) and [adding the folder to your Windows versions system path](https://duckduckgo.com/?t=ffab&q=how+to+add+a+folder+to+your+windows+system+path).

### Linux/Unix systems {#linuxunix_systems}

git clone [https://git.savannah.gnu.org/git/libredwg.git](https://git.savannah.gnu.org/git/libredwg.git)
cd libredwg
mkdir build
cd build
cmake ..
make
make install (or use checkinstall, or simply locate & copy the dwg2dxf utility to your executables path, it will be then autodetected by FreeCAD)

### openSUSE

To prevent from program execution problems you must use LibreDWG package compiled for the installed openSUSE OS distribution. LibreDWG is typically installed with **YAST** (abbr. Yet another Setup Tool), the Linux operating system\'s setup and configuration tool.

The more experienced user first gets an overview of possible packages provided. **Note:** openSUSE has several options to choose from when downloading LibreDWG. To view these options, visit [Survey of provided LibreDWG packages on openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=libredwg).

For e. g. Intel or AMD 64-bit desktops, laptops, and servers the (x86\_64) release is the one to select. So, **libredwg0** and **libredwg-tools** are of the right choice to install.

It is recommended to grab the binary packages directly. Then select the correct distribution for your installed openSUSE OS.

In any terminal/console (root rights required) the installation will be carried out with:

:   
    
```python
    zypper install libredwg0 libredwg-tools
    
```
    

Afterwards every \*.dwg file import should work properly.


<div class="mw-translate-fuzzy">

## 대안은 무엇인가요? {#대안은_무엇인가요}


</div>

### DoubleCAD XT {#doublecad_xt}

There is also DoubleCAD XT (https://www.turbocad.com/content/doublecad-xt-v5). The program is free for personal and commercial use. It requires a free sign-up to receive an activation code via E-Mail. This Program is windows-only. Note: it does not seem to have been updated for years.

### NanoCAD 5.0 {#nanocad_5.0}

There is also nanoCAD 5.0 (https://nanocad.com/products/nanoCAD/download/). The program is free for personal and commercial use. It requires a free sign-up to receive an activation code via E-Mail. This Program is windows-only.


<div class="mw-translate-fuzzy">

### AutoCAD 파일을 친근한 형식으로 내보내기 {#autocad_파일을_친근한_형식으로_내보내기}

Exporting your AutoCAD files in a more FreeCAD friendly format, like DXF R12 or R14, SVG, and if version supports it, IGES. All are better alternatives to the DWG format when using FreeCAD.


</div>

Exporting your AutoCAD files in a more FreeCAD friendly format, like DXF R12 or R14, SVG, and if version supports it, IGES. All are better alternatives to the DWG format when using FreeCAD.

It is important to know that, contrarily to popular belief, there is no difference between the contents of a file saved in DWG or DXF formats, provided it is the same version (ex. DWG 2014 vs. DXF 2014). Both formats are maintained by Autodesk, and they both support exactly the same features. The difference is that DWG is closed (machine-encoded) while DXF is open.

## 도우려면 무엇을 할 수 있나요? {#도우려면_무엇을_할_수_있나요}


<div class="mw-translate-fuzzy">

### Promote the use of alternative formats {#promote_the_use_of_alternative_formats}

간단히 말해, DWG 형식의 작업을 수락하는 것을 중지합니다. 실제로, 이것은 종종 말하기보다 쉽습니다. 그러나 가능하면 언제든지 FreeCAD 사용자와 지지자들이 DWG 형식을 피하고 거부하는 것은 나쁜 관행은 아닙니다.


</div>

Simply put, stop accepting work done in DWG format. In practice, this is often easier said than done. Still, it would not be bad practice for users and supporters of FreeCAD to avoid and reject the DWG format whenever possible.

### Use the LibreDWG library and file bug reports {#use_the_libredwg_library_and_file_bug_reports}

In development version as mentioned above you can switch from the proprietary ODA Converter to the free software LibreDWG library for DWG (and DXF) files. Please do this and report any problems you encounter.


 

[Category:File\_Formats{{\#translation:}}](Category:File_Formats.md) [Category:Common Questions{{\#translation:}}](Category:Common_Questions.md)
