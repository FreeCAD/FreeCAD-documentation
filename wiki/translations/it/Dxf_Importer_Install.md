# Dxf Importer Install/it




{{TutorialInfo/it|Topic=SampleClass|Level=Utente medio|Time=15 minuti|Author=[Mario52](User:Mario52.md)|FCVersion=Tutte}}

### Descrizione

Questa pagina spiega passo a passo come installare il pacchetto Draft-dxf-import di Yorikvanhavre per caricare i file in formato DXF in FreeCAD e importare i file DWG utilizzando l\'utility Teighafileconverter. Questa installazione è stata fatta in ambiente Windows Vista, ma il metodo funziona anche per Linux

### Prima parte: 

Individuare la cartella delle macro in FreeCAD

**1 :** aprire FreeCAD


<div class="mw-collapsible mw-collapsed toccolours">

Dalla versione 0.15 è possibile utilizzare l\'aggiornamento automatico (espandere per vedere come fare)


<div class="mw-collapsible-content">

<img alt="Automatic DXF install" src=images/Dxf_Importer_Install_01b.png  style="width:640px;"> 


</div>


</div>

**2 :** cliccare **Menu \> Macro \> Macros** oppure usare il pulsante <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> \"Apri una finestra di dialogo che consente di eseguire una macro registrata\"

![open FreeCAD](images/Dxf_Importer_Install_01.png ) 

**3 :** si apre la finestra di dialogo

**4 :** copiare l\'indirizzo di \"Percorso Macro\" (qui **C:\\Users\\d\\AppData\\Roaming\\FreeCAD\\**) In Ubuntu di solito è **/home/your\_user\_name/.FreeCAD**

![Open a dialog to let you execute a macro Recorded](images/Dxf_Importer_Install_02.png ) 

**5 :** incollare l\'indirizzo nel proprio browser e confermare

![paste the address into your browser](images/Dxf_Importer_Install_03.png ) 

**6 :** lasciare aperto l\'esploratore

![](images/Dxf_Importer_Install_04.png ) 

**7 :** Chiudere FreeCAD

### Seconda parte: 

Scaricare i file

**8 :** scaricare i file dalla pagina <https://github.com/yorikvanhavre/Draft-dxf-importer>

**9 :** e cliccare sul pulsante **Download ZIP** per la versione di default, .


<div class="mw-collapsible mw-collapsed toccolours">

(o scegliere a fondo pagina la versione desiderata) (espandere per vedere come fare)


<div class="mw-collapsible-content">

<img alt="Automatic DXF install" src=images/Dxf_Importer_Install_05b.png  style="width:640px;"> 


</div>


</div>

![download files](images/Dxf_Importer_Install_05.png ) 

**10 :** è necessario estrarre il file in una directory temporanea (in questo caso **c:\\tmp**)

![extract the file](images/Dxf_Importer_Install_06.png ) 

**11 :** il file decompresso crea una nuova cartella denominata \"**Draft-dxf-import-master**\"

![decompresser creates a new folder](images/Dxf_Importer_Install_07.png ) 

**12 :** selezionare tutti i file estratti di questa cartella e poi selezionare \"Taglia\"

![select all the files and Cut](images/Dxf_Importer_Install_08.png ) 

**13 :** incollare i file nella cartella delle macro di FreeCAD aperta nel browser (punto 6 **C:\\Users\\d\\AppData\\Roaming\\FreeCAD\\**)

In Ubuntu, di solito è **/home/your\_user\_name/.FreeCAD**

![paste the files in the folder](images/Dxf_Importer_Install_09.png ) 

**14 :** Aprire FreeCAD e cliccare sul pulsante <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> , verificare che i file necessari per il formato DXF siano, chiudere la finestra \"Esegui la macro\".

![open FreeCAD](images/Dxf_Importer_Install_15.png ) 

**15 :** in FreeCAD \"Aprire\" un proprio file DXF

![load your DXF file](images/Dxf_Importer_Install_10.png ) 

**16 :** a questo punto, il file DXF è utilizzabile.

![DXF file can be used](images/Dxf_Importer_Install_11.png ) 

**VERSIONI**

Questo repository contiene diverse versioni dell\'importatore DXF. La versione di default, che si scarica quando si preme il pulsante \"download ZIP\" di cui sopra, è sempre la versione necessaria per la corrente versione stabile di FreeCAD.

Se si utilizza un\'altra versione di FreeCAD, per esempio, una versione di sviluppo o una versione precedente, allora potrebbe essere anche necessaria un\'altra versione di questa libreria DXF. Per scoprire quale versione della libreria DXF è necessaria per la vostra versione di FreeCAD, inserire il seguente codice nella console Python: 
```python
import importDXF
print importDXF.CURRENTDXFLIB
```

### Terza parte: 

Scaricare e installare Teigha converter per usare i file DWG

**17 :** teighafileconverter si scarica dalla pagina [teighafileconverter](http://www.opendesign.com/guestfiles/teighafileconverter)

![download Teigha](images/Dxf_Importer_Install_12.png ) 

**18 :** Scegliere la versione adatta al proprio Qt e OS

![choose the version](images/Dxf_Importer_Install_13.png ) 

**19 :** e poi installarla ![install it on your system](images/Dxf_Importer_Install_14.png ) 

**20 :** aprire FreeCAD e cliccare sul pulsante <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> \"Apri una finestra di dialogo che consente di eseguire una macro registrata\"

**21 :** chiudere la finestra delle macro

**22 :** e attivare l\'ambiente Draft

![activate the Draft workbebch](images/Dxf_Importer_Install_16.png ) 

**23 :** Secondo la versione di FreeCAD in uso:

-   aprire il menu \"Modifica \> Preferenze \> Draft \> Opzioni DXF/DWG\" oppure
-   aprire il menu \"Modifica \> Preferenze \> Import-Export \> DXF/DWG\"

![Menu \> Preferences](images/Dxf_Importer_Install_17.png ) 

**24 :** selezionare la scheda \"Draft \> DXF / DWG options\"

**25 :** nella sezione \"Opzioni formato DWG\", cliccare sui tre puntini **\...** ![Draft \> DXF / DWG options](images/Dxf_Importer_Install_18.png ) 

**26 :** per indicare il percorso di Teigha converter che FreeCAD deve usare per convertire i DWG in DXF

**27 :** entrare nella directory, che in questo caso in Window è \"**C:/Program Files/ODA/Teigha File Converter 4.00.1/**\", selezionare TeighaFileConverter.exe e confermare

![DWG format option](images/Dxf_Importer_Install_19.png ) 

**28 :** l\'operazione è completata, cliccare **OK** poi testare un file DWG

![directory Teigha File Converter 4.00.1](images/Dxf_Importer_Install_20.png ) 

### Parte quarta: 

Usare Teigha. Teigha è un programma completo utilizzabile senza FreeCAD

![directory Teigha File Converter 4.00.1](images/Dxf_Importer_Install_21.png ) 

**1 :** Imput folder: percorso della cartella dove ci sono i file DXF o DWG da convertire

**2 :** Output folder: percorso della cartella dove si vuole collocare i file DXF o DWG convertiti

**3 :** Recurse folder:

**4 :** Audit:

**5 :** Input files filter: filtrare solo i file DXF o solo i file DXF oppure entrambi

**6 :** Output release: il formato in cui si vuole ottenere i file convertiti

**7 :** Start: avvia il processo

### Link

Video tutorial [FreeCAD Tutorial 24 - DXF/DWG Import](https://www.youtube.com/watch?v=wHxTWuDhc3M)
