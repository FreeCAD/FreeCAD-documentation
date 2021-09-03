 {{TOCright}}


{{Fake heading|sub=4|< Back to [[FreeCAD Howto Import Export]]}}


<div class="mw-translate-fuzzy">

## Perché non è possibile importare i file DWG in FreeCAD? 


</div>

Il formato DWG è un formato di file binario closed source che non è supportato direttamente da FreeCAD. Prima deve essere convertito usando un\'applicazione esterna e dopo si può importare la conversione in FreeCAD e utilizzarla.

Notare che al momento non è possibile importare DWG 3D in FreeCAD. I dati 3D sono incorporati come dati binari .SAT (ACIS), un formato proprietario e non documentato.


<div class="mw-translate-fuzzy">

## Cosa serve per poter importare i file DWG? 


</div>


<div class="mw-translate-fuzzy">

### ODA Converter (anteriormente Teigha Converter) 

-   homepage: <https://www.opendesign.com/guestfiles/oda_file_converter>
-   licenza: freeware
-   optional, usato per abilitare l\'importazione e l\'esportazione dei file DWG


</div>

-   homepage: <https://www.opendesign.com/guestfiles/oda_file_converter>
-   license: freeware
-   optional, used to enable import and export of DWG files

Il convertitore ODA è una piccola utility liberamente disponibile che consente di convertire tra diverse versioni i file DWG e DXF. FreeCAD può usarlo per offrire l\'importazione e l\'esportazione dei file DWG, convertendo prima i formati DWG in DXF al suo interno, e poi importando il contenuto dei file tramite il suo importatore DXF standard. Si applicano le restrizioni di [importazione di DXF](Draft_DXF/it.md).


<div class="mw-translate-fuzzy">

### Installazione

Su tutte le piattaforme, basta installare il pacchetto appropriato da <https://www.opendesign.com/guestfiles/oda_file_converter>. Se, dopo l\'installazione, l\'utility non viene trovata automaticamente da FreeCAD, può essere necessario impostare manualmente il percorso del file eseguibile del converter. Attivare l\'ambiente Draft, poi nelle opzioni del menu Modifica → Preferenze → Draft → Importa/Esporta → DWG inserire il percorso per l\'eseguibile Teigha File Converter.


</div>

On all platforms, only by installing the appropriate package from <https://www.opendesign.com/guestfiles/oda_file_converter>. After installation, if the utility is not found automatically by FreeCAD, you might need to set the path to the converter executable manually. open Edit → Preferences → Import-Export → DWG and fill \"Path to Teigha File Converter\" appropriately.


<div class="mw-translate-fuzzy">

Per maggiori dettagli sull\'installazione vedere [ questo tutorial](Dxf_Importer_Install/it.md).


</div>


<div class="mw-translate-fuzzy">

#### Uso

Il programma può essere utilizzato da riga di comando o dall\'interfaccia grafica. Accertarsi di convertire i file dwg in un formato ASCII.


</div>

The program may be used with the command line interface or the graphical interface. Be sure to convert the DWG files to an ASCII-Format.

Il formato da riga di comando è:

1.  Quoted Input Folder
2.  Quoted Output Folder
3.  Output\_version {\"ACAD9\",\"ACAD10\",\"ACAD12\", \"ACAD13\",\"ACAD14\", \"ACAD2000\",\"ACAD2004\", \"ACAD2007\",\"ACAD2010\"}
4.  Output File type {\"DWG\",\"DXF\",\"DXB\"}
5.  Recurse Input Folder {\"0\",\"1\"}
6.  Audit each file {\"0\",\"1\"}
7.  \[optional\] Input file filter (default:\"\*.DWG;\*.DXF\")

**Esempio per Linux**
TeighaFileConverter \"/home/dwg-data\" \"/home/dxf-data\" \"ACAD2010\" \"DXF\" \"0\" \"1\" \"test.dwg\" Il secondo numero (audit) deve essere 1 altrimenti l\'operazione fallisce

**Esempio per Windows**
\"C:\\Program Files\\ODA\\Teigha File Converter 3.08.2\\TeighaFileConverter.exe\" \"Path-To-Input-Directory\" \"Path-To-Output-Directory\" \"ACAD2010\" \"DXF\" \"0\" \"1\" \"Name-Of-A-Test-File.dwg\"

### CADExchanger Workbench 

Installing the CADExchanger Workbench allows for working with DWG files through integration with the paid commercial file converter product [CADExchanger](https://cadexchanger.com/). Just follow the instructions in the [GitHub repository](https://github.com/yorikvanhavre/CADExchanger). You can discuss this workbench on [its forum thread](https://forum.freecadweb.org/viewtopic.php?f=9&t=22227&p=462421).

At the moment, the CADExchanger way is the only one that allows to work with 3D DWG files, by converting them to other 3D formats.

## FreeCAD v0.19 and LibreDWG 

As from 0.19, FreeCAD doesn\'t need the ODA converter anymore and can use libreDWG directly. Be aware that, since libreDWG is a work-in-progress, depending on your file, the results might not be the same.

-   homepage: <https://www.gnu.org/software/libredwg/>
-   license: GPLv2-or-later
-   optional, used to enable import and export of DWG files

GNU LibreDWG is a free C library to handle DWG files. It aims to be a free replacement for the Open Design Alliance Drawings SDK libraries.

## Installation

### AppImage releases 

LibreDWG is included in v 0.19\_pre appimages[1](https://forum.freecadweb.org/viewtopic.php?f=8&t=39827&start=20#p372933)

### Windows

LibreDWG can be configured to work on Windows by downloading and unzipping the appropriate [pre-compiled windows binary](https://github.com/LibreDWG/libredwg/releases) and [adding the folder to your Windows versions system path](https://duckduckgo.com/?t=ffab&q=how+to+add+a+folder+to+your+windows+system+path).

### Linux/Unix systems 

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

## Quali sono le alternative? 


</div>


<div class="mw-translate-fuzzy">

### DoubleCAD XT 

C\'è anche DoubleCAD XT (https://www.turbocad.com/content/doublecad-xt-v5). Il programma è gratuito per uso personale e commerciale. Si richiede una iscrizione gratuita per ricevere il codice di attivazione via e-mail. Questo programma è solo per Windows. Nota: non sembra essere stato aggiornato per anni.


</div>

There is also DoubleCAD XT (https://www.turbocad.com/content/doublecad-xt-v5). The program is free for personal and commercial use. It requires a free sign-up to receive an activation code via E-Mail. This Program is windows-only. Note: it does not seem to have been updated for years.

### NanoCAD 5.0 

There is also nanoCAD 5.0 (https://nanocad.com/products/nanoCAD/download/). The program is free for personal and commercial use. It requires a free sign-up to receive an activation code via E-Mail. This Program is windows-only.


<div class="mw-translate-fuzzy">

### Esportare i file di AutoCAD in Formati Amichevoli 

Esportare i file di AutoCAD in un formato più *amichevole* a FreeCAD, come DXF R12 o R14, SVG, e se la versione lo supporta, IGES. Tutti questi formati sono delle alternative migliori al formato DWG quando si utilizza FreeCAD.


</div>

Exporting your AutoCAD files in a more FreeCAD friendly format, like DXF R12 or R14, SVG, and if version supports it, IGES. All are better alternatives to the DWG format when using FreeCAD.

È importante sapere che, contrariamente alla credenza popolare, non vi è alcuna differenza tra il contenuto di un file salvato in formato DWG o DXF, a condizione che sia la stessa versione (es. DWG 2014 o DXF 2014). Entrambi i formati sono mantenuti da Autodesk, ed entrambi supportano esattamente le stesse caratteristiche. La differenza è che DWG è chiuso (codice-macchina), mentre DXF è aperto.

## Cosa posso fare per dare un aiuto? 


<div class="mw-translate-fuzzy">

### Promuovere l\'uso dei formati alternativi 

In poche parole, smettere di accettare il lavoro svolto in formato DWG. Nella pratica, spesso questo è più facile a dirsi che a farsi. Tuttavia, per gli utenti e i sostenitori di FreeCAD non sarebbe una cattiva pratica quella di evitare e respingere il formato DWG, quando possibile.


</div>

Simply put, stop accepting work done in DWG format. In practice, this is often easier said than done. Still, it would not be bad practice for users and supporters of FreeCAD to avoid and reject the DWG format whenever possible.

### Use the LibreDWG library and file bug reports 

In development version as mentioned above you can switch from the proprietary ODA Converter to the free software LibreDWG library for DWG (and DXF) files. Please do this and report any problems you encounter.


 

[Category:File\_Formats{{\#translation:}}](Category:File_Formats.md) [Category:Common Questions{{\#translation:}}](Category:Common_Questions.md)
