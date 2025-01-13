# FreeCAD and DWG Import/ko
{{Fake heading|sub=4|< Back to [[FreeCAD Howto Import Export]]}}



## FreeCAD 에서 DWG 파일 작업이 어려운 이유 ? 

DWG 파일은 내용을 이진 숫자로 기록하고 밀봉한 형식으로 되어 있어서 FreeCAD 에서 직접적으로 처리되지 않습니다. 3rd 단체가 제작한 \'파일변환\' 기능을 이용하여, DWG 파일을 DXF 파일로, 또는 그 반대로 변환 하는 것을 거쳐야 합니다.



## DWG 파일을 불러오기 위해 필요한 것 ? 

### LibreDWG

-   홈 페이지 : <https://www.gnu.org/software/libredwg/>
-   검증 : [GPLv3-or-later](https://savannah.gnu.org/projects/libredwg/)
-   DWG 파일을 위해 \'내보내기\'(dfx2dwg.exe 이용)나 \'불러오기\'(dwg2dxf.exe 이용) 등의 별도의 변환을 해주어야 함

GNU LibreDWG 는 DWG 파일을 다루는 기능들을 모아 놓은 c 언어로 된 개방형 라이브러리입니다. 이것은 개방형 설계 단체의 설계도 개발 도구의 라이브러리에 대해 자유를 갖는 대체물이 되는 것을 목표로 하고 있습니다. 염두에 두어야 할 것은, libreDWG 는 작성중인 상태의 제품이므로 DWG 의 어떤 내용물은 처리가 충분하지 않을 수 있다는 겁니다.



#### 윈도우에서 설치 

여러분의 윈도우 버젼을 확인하고 2진수 코드로 컴파일 해놓은 파일을 [pre-compiled Windows binary](https://github.com/LibreDWG/libredwg/releases) ☜ 여기에서 내려받고 적절한 폴더에 압축 해제 합니다. 윈도우가 검색 (<small>(v0.21)</small> ) 할 때 자동적으로 조사하는 폴더 목록에 실행 파일이 있는 폴더를 등록 합니다 파이선 명령어 {{Incode|os.getenv("PATH")}} 또는, 수동으로 설정 합니다.

[윈도우즈의 검색창에, "환경 변수 편집" 입력하고, "환경 변수(N)..." "시스템 변수(S)" 변수 "Path" 선택 "편집(I)..." "새로 만들기(N)" "찾아보기(B)" 등등의 선택을 하게 됩니다. 역자 주]. 

[Import Export Preferences](Import_Export_Preferences#DWG.md) ☜ 를 눌러 보세요.



#### Linux / Unix 시스템에 설치 


<div class="mw-translate-fuzzy">


{{Code|lang=shell|code=
git clone --recurse-submodules https://git.savannah.gnu.org/git/libredwg.git
cd libredwg
mkdir build
cd build
cmake ..
make
make install # 또는 checkinstall , 또는 dwg2dxf 를 위치 복사 등을 사용 합니다
             # 여러분의 실행 파일 폴더를 설치 하기, 이 후로는 프리캐드에 의해 자동적으로 될 겁니다
}}


</div>

이 운영체제가 검색 (<small>(v0.21)</small> ) 할 때 자동적으로 조사하는 폴더 목록에 실행 파일이 있는 폴더를 등록 합니다 {{Incode|os.getenv("PATH")}} 또는, 수동으로 설정 합니다.



#### openSUSE 에 설치하기 

설치시 사고를 피하기 위해서 \'openSUSE 운영체제가 설치된 상태에서 LibreDWG를 설치하는 것\'을 위해 컴파일된 패키지를 사용해야 합니다. LibreDWG 는 보통 **YAST** 라고 하는 리눅스 시스템의 설치 및 환경설정 도구를 통해 설치합니다(다른 시스템에서의 설치 도구).

경험 많은 사용자는 패키지에 관한 요약문을 먼저 확인 합니다. **주의사항 :** openSUSE 는 내려받기 할 LibreDWG 에 관해 몇 가지 선택사항이 있습니다. 그 내용들은, [Survey of provided LibreDWG packages on openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=libredwg) ☜ 를 눌러 보세요.

예를 들면 인텔 또는 AMD 의 64 비트 시스템 이고, 데스트 탑, 노트북, 서버(x86_64) 등의 장치에 대한 것은 따로 있습니다. 그러므로 설치를 하려면 **libredwg0** 와 **libredwg-tools** 들을 선택하는 것이 맞습니다.

It is recommended to grab the binary packages directly. Then select the correct distribution for your installed openSUSE OS.

In any terminal/console (root rights required) the installation will be carried out with:


```python
zypper install libredwg0 libredwg-tools
```

Place the executable in the OS search path, {{Incode|os.getenv("PATH")}}, for automatic detection (<small>(v0.21)</small> ), or set the path manually. See [Import Export Preferences](Import_Export_Preferences#DWG.md).




<div class="mw-translate-fuzzy">

### ODA Converter (formerly Teigha Converter) 

-   홈페이지: <https://www.opendesign.com/guestfiles/oda_file_converter>
-   라이선스: freeware
-   optional, used to enable import and export of DWG files


</div>

-   homepage: <https://www.opendesign.com/guestfiles/oda_file_converter>
-   license: freeware
-   optional, used to enable import and export of DWG files

The ODA File Converter is a small freely available utility that allows to convert between several versions of DWG and DXF files. FreeCAD can use it to offer DWG import and export, by converting DWG files to the DXF format under the hood, then using its standard DXF importer to import the file contents. The restrictions of the [DXF importer](Draft_DXF.md) apply.




<div class="mw-translate-fuzzy">

#### 설치

On all platforms, only by installing the appropriate package from <https://www.opendesign.com/guestfiles/oda_file_converter>. After installation, if the utility is not found automatically by FreeCAD, you might need to set the path to the converter executable manually. open Edit → Preferences → Import-Export → DWG and fill \"Path to Teigha File Converter\" appropriately.


</div>

If the utility is not found automatically by FreeCAD after installation, you need to set the path to the executable manually. See [Import Export Preferences](Import_Export_Preferences#DWG.md).

### QCAD pro 


<small>(v0.20)</small> 

-   homepage: <https://qcad.org/en/qcad-command-line-tools#dwg2dwg>
-   license: commercial
-   optional, used to enable import and export of DWG files

QCAD is a well-known open-source DXF-based 2D CAD platform. It also offers a paid pro version, which is basically the open-source version plus support for the DWG format. When buying the pro version, QCAD also includes a DWG to DXF conversion utility that can be used by FreeCAD.

#### Installation

If the utility is not found automatically by FreeCAD after installation (<small>(v0.21)</small> ), you need to set the path to the bash file (Linux and macOS) or batch file (Windows) manually. See [Import Export Preferences](Import_Export_Preferences#DWG.md).

### CADExchanger Workbench 

Installing the CADExchanger Workbench allows for working with DWG files through integration with the paid commercial file converter product [CADExchanger](https://cadexchanger.com/). Just follow the instructions in the [GitHub repository](https://github.com/yorikvanhavre/CADExchanger). You can discuss this workbench on [its forum thread](https://forum.freecadweb.org/viewtopic.php?f=9&t=22227&p=462421).

At the moment, the CADExchanger way is the only one that allows to work with 3D DWG files, by converting them to other 3D formats.




<div class="mw-translate-fuzzy">

## 대안은 무엇인가요? 


</div>

### DoubleCAD XT 

There is also DoubleCAD XT (https://www.turbocad.com/content/doublecad-xt-v5). The program is free for personal and commercial use. It requires a free sign-up to receive an activation code via E-Mail. This Program is windows-only. Note: it does not seem to have been updated for years.

### NanoCAD 5.0 

There is also nanoCAD 5.0 (https://nanocad.com/products/nanoCAD/download/). The program is free for personal and commercial use. It requires a free sign-up to receive an activation code via E-Mail. This Program is windows-only.




<div class="mw-translate-fuzzy">

### AutoCAD 파일을 친근한 형식으로 내보내기 

Exporting your AutoCAD files in a more FreeCAD friendly format, like DXF R12 or R14, SVG, and if version supports it, IGES. All are better alternatives to the DWG format when using FreeCAD.


</div>

Exporting your AutoCAD files in a more FreeCAD friendly format, like DXF R12 or R14, SVG, and if version supports it, IGES. All are better alternatives to the DWG format when using FreeCAD.

It is important to note that there is no difference between the contents of a file saved in DWG or DXF formats, provided it is the same version (ex. DWG 2014 vs. DXF 2014). Both formats are maintained by Autodesk, and they both support exactly the same features. The difference is that DWG is closed (machine-encoded) while DXF is open.




<div class="mw-translate-fuzzy">

## 도우려면 무엇을 할 수 있나요? 


</div>




<div class="mw-translate-fuzzy">

### Promote the use of alternative formats 

간단히 말해, DWG 형식의 작업을 수락하는 것을 중지합니다. 실제로, 이것은 종종 말하기보다 쉽습니다. 그러나 가능하면 언제든지 FreeCAD 사용자와 지지자들이 DWG 형식을 피하고 거부하는 것은 나쁜 관행은 아닙니다.


</div>

Simply put, stop accepting work done in DWG format. In practice, this is often easier said than done. Still, it would not be bad practice for users and supporters of FreeCAD to avoid and reject the DWG format whenever possible.

### Use the LibreDWG library and file bug reports 

In development version as mentioned above you can switch from the proprietary ODA Converter to the free software LibreDWG library for DWG (and DXF) files. Please do this and report any problems you encounter.



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Common Questions](Category_Common Questions.md) > [Draft](Category_Draft.md) > FreeCAD and DWG Import/ko
