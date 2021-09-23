# Dxf Importer Install/ro



<div class="mw-translate-fuzzy">


{{TutorialInfo/ro|Topic=SampleClass|Level=Medium user|Time=15 minutes|Author=[Mario52](User:Mario52.md)|FCVersion=All}}


</div>

### Descriere

Această pagină explică pas cu pas pas cu pas calea de urmat pentru a instala ansamblul de fișiere Draft-dxf-import yorikhavre pentru a începe uploadul de fișiere cu formatul DXF în FreeCAD și să importați cu ajutorul utilitarului teighafileconverter. Această instalare a fost făcută sub Windows Vista, dar în principiu sistemul poate funcționa și sub Linux

### Primul pas: 

identificați folderul FreeCAD al macrocomenzii

**1 :** deschideți FreeCAD


<div class="mw-collapsible mw-collapsed toccolours">

Dacă aveți o versiune începând cu pachetul 0.15, puteți utiliza actualizarea automată a pachetului DXF (pentru a vedea expandați conținutul)


<div class="mw-collapsible-content">

<img alt="Automatic DXF install" src=images/Dxf_Importer_Install_01b.png  style="width:640px;"> 


</div>


</div>

**2 :** click pe **Menu \> Macro \> Macros** sau click în partea de jos <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> \"Open a dialog to let you execute a macro Recorded\"

![open FreeCAD](images/Dxf_Importer_Install_01.png ) 

**3 :** deschide o casetă de dialog

**4 :** copiază adresa \"Macro destination\" (here **C:\\Users\\d\\AppData\\Roaming\\FreeCAD\\**) In Ubuntu, este normal aceasta **/home/your\_user\_name/.FreeCAD**

![Open a dialog to let you execute a macro Recorded](images/Dxf_Importer_Install_02.png ) 

**5 :** lipește (din copy&paste) adresa în browserul dvs. și confirmați

![paste the address into your browser](images/Dxf_Importer_Install_03.png ) 

**6 :** lăsați deschis explorer

![](images/Dxf_Importer_Install_04.png ) 

**7 :** Închideți FreeCAD

### Al doilea pas: 

Descărcați fișierele

**8 :** descărcați fișierele din pagina <https://github.com/yorikvanhavre/Draft-dxf-importer>

**9 :** și click pe iconița butonului **Download ZIP** pentru versiunea implicită.


<div class="mw-collapsible mw-collapsed toccolours">

(sau alegeți pentru versiunea dvs. de dezvoltare, consultați pagina următoare )(extindeți pentru a vedea)


<div class="mw-collapsible-content">

<img alt="Automatic DXF install" src=images/Dxf_Importer_Install_05b.png  style="width:640px;"> 


</div>


</div>

![download files](images/Dxf_Importer_Install_05.png ) 

**10 :** trebuie să extrageți fișierul într-un director temporar (aici **c:\\tmp**)

![extract the file](images/Dxf_Importer_Install_06.png ) 

**11 :** dezarhivarea creează un nou folder numit \"**Draft-dxf-import-master**\"

![decompresser creates a new folder](images/Dxf_Importer_Install_07.png ) 

**12 :** Fișierele sunt în acest folder, selectați pe toate și \"Cut\"

![select all the files and Cut](images/Dxf_Importer_Install_08.png ) 

**13 :** lipește fișierele în folderul FreeCAD cu macrocomenzi în deschiderea explorer (step 6) (**C:\\Users\\d\\AppData\\Roaming\\FreeCAD\\**)

In Ubuntu, este normal aceasta **/home/your\_user\_name/.FreeCAD**

![paste the files in the folder](images/Dxf_Importer_Install_09.png ) 

**14 :** Deschide FreeCAD click butonul <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> , fișierele necesare în format DXF sunt prezente, închideți fereastra \"Execute macro

![open FreeCAD](images/Dxf_Importer_Install_15.png ) 

**15 :** încarcă fișierul DXF

![load your DXF file](images/Dxf_Importer_Install_10.png ) 

**16 :** fișierul DXF file poate fi utilizat

![DXF file can be used](images/Dxf_Importer_Install_11.png ) 

**VERSIUNI**

Acest depozit conține mai multe versiuni ale importatorului DXF. Versiunea implicită, pe care o descărcați când apăsați butonul \"download ZIP\" de mai sus, este totuși versiunea cerută de versiunea freeware actuală stabilă a FreeCAD.

Dacă utilizați o altă versiune a FreeCAD, de exemplu o versiune de dezvoltare sau o versiune mai veche, este posibil să aveți nevoie și de o altă versiune a acestei biblioteci DXF. Puteți afla care versiune a bibliotecii DXF este necesară de versiunea dvs. de FreeCAD, introducând următorul cod în consolă Python FreeCAD: 
```python
import importDXF
print importDXF.CURRENTDXFLIB
```

### Al treilea pas 

Descărcați convertorul Teigha converter pentru a utiliza fișiere DWG

**17 :** descărcați teighafileconverter la [teighafileconverter page](http://www.opendesign.com/guestfiles/teighafileconverter)

![download Teigha](images/Dxf_Importer_Install_12.png ) 

**18 :** alegeți versiunea care se potrivește cu Qt și OS dvs

![choose the version](images/Dxf_Importer_Install_13.png ) 

**19 :** și instalați ăn sistemul dvs ![install it on your system](images/Dxf_Importer_Install_14.png ) 

**20 :** deschideți FreeCAD și click pe butonul <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> \"Open a dialog to let you execute a macro Recorded\"

**21 :** închideți fereastra de macrocomenzi

**22 :** și activați Atelierul Draft workbench

![activate the Draft workbebch](images/Dxf_Importer_Install_16.png ) 

**23 :** acum putem să intrăm pagina de opțiuni DXF / DWG click \"Menu \> Edit \> Preferences\"

![Menu \> Preferences](images/Dxf_Importer_Install_17.png ) 

**24 :** selectați \"Draft \> DXF / DWG options\" tab

**25 :** In secțiunea opțiunii formatului DWG, click cele 3 puncte **\...** ![Draft \> DXF / DWG options](images/Dxf_Importer_Install_18.png ) 

**26 :** pentru a da drumul convertorului Teigha pe care FreeCAD îl va folosi pentru a converti DWG în DXF

**27 :** introduceți în directorul de aici în windows la \"**C:/Program Files/ODA/Teigha File Converter 4.00.1/**\" and select TeighaFileConverter.exe și confirmați

![DWG format option](images/Dxf_Importer_Install_19.png ) 

**28 :** operația este completă click pe **OK** puteți testa un fișier DWG

![directory Teigha File Converter 4.00.1](images/Dxf_Importer_Install_20.png ) 

### Al patrulea pas: 

Utilizare Teigha. Teigha este un program complet și poate fi folosit fără FreeCAD

![directory Teigha File Converter 4.00.1](images/Dxf_Importer_Install_21.png ) 

**1 :** Imput folder: calea folderului este DXF sau DWG fișierele pentru conversie

**2 :** folder de Outputr: calea pentru folderul destinație pentru fișierele convertite

**3 :** Folder Recursiv(autoreferențiere):

**4 :** Audit:

**5 :** filtru pentrut files filter: filtrează numai pentru DXF, DWG or DXF and DWG

**6 :** Ieșire de ieșire: fișierul va fi convertit în format și în versiunea selectată

**7 :** Start: lansează procesul

### Links

Video tutorial [FreeCAD Tutorial 24 - DXF/DWG Import](https://www.youtube.com/watch?v=wHxTWuDhc3M)
