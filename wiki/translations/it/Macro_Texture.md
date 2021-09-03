


<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Macro_Texture
|Translate=Texture
|Icon=FCTexture.png
|Description=Crea una immagine 3D partendo da una immagine BMP.
|Author=Mario52
|Version=0.14c
|Date=2021/01/16
|FCVersion=0.18 e superiore
|Download=[https://www.freecadweb.org/wiki/images/9/90/FCTexture.png ToolBar Icon], [https://www.freecadweb.org/wiki/Macro_Loft Macro Loft] [16px|FCCreaLoft](File:FCCreaLoft.png.md)
|SeeAlso=[32px|FCCreaLoft](File:FCCreaLoft.png.md) [Macro Loft](Macro_Loft/it.md)
}}


</div>


<div class="mw-translate-fuzzy">

## Descrizione

Questa macro permette di creare facilmente un modello 3D partendo da una immagine bitmap con 256 livelli di grigio.


</div>


<div class="mw-translate-fuzzy">

Siccome con questa macro si può convertire qualsiasi immagine in oggetti 3D senza alcun intervento, spero che questo cambi il modo di concepire il CAD e il CNC.


</div>


<div class="mw-translate-fuzzy">

Tutto diventa possibile indipendentemente dalla complessità dell\'immagine!


</div>


<div class="mw-translate-fuzzy">

La macro <img alt="FCCreaLoft" src=images/FCCreaLoft.png  style="width:32px;"> [Macro Loft](Macro_Loft/it.md) permette di automatizzare il \"multi loft\"


</div>


{{Codeextralink|https://gist.githubusercontent.com/mario52a/262317bc7d8555885b0e/raw/3ec2ab127d8ad01a6b657aa5df9a6127ff07c7c0/Macro%2520FCTexture.FCMacro}}

<img alt="" src=images/Texture_004_Honda.png  style="width:480px;"> 
*Texture 004 Honda*


<div class="mw-translate-fuzzy">

## Uso

Questo macro ha bisogno di una immagine con 256 livelli di grigio (0-255) (8 bit) pertanto prima di utilizzare la macro è necessario convertire l\'immagine in scala di grigi. Il numero di colori viene rilevato automaticamente. Ogni colore viene trattato come un livello di grigio, il bianco (255) è il livello più alto e il nero (0) è il livello più basso. Se l\'immagine ha più di 256 colori (32 bit) viene attivato il modo Plan. (Il tempo di esecuzione delle funzioni di visualizzazione dei punti può essere molto lungo)


</div>

La configurazione si esegue prima di aprire il file, i valori predefiniti producono un disegno con le seguenti dimensioni:

-   la coordinata **X** è la larghezza dell\'immagine in punti,
-   la coordinata **Y** è l\'altezza dell\'immagine in punti,
-   la coordinata **Z** è la profondità o spessore del disegno adattato a 10 mm (256 mm in modo raw).

In FreeCAD il file dell\'immagine si sviluppa come in una scansione x1 x2 x3 \... con incrementi del valore y di 1 mm per volta. Il valore di z è determinato dal valore del colore. Questi valori sono configurabili nell\'interfaccia della macro.


<div class="mw-translate-fuzzy">

Attenzione: secondo le dimensioni dell\'immagine, il file del disegno può diventare molto grande! Tenere presente che un\'immagine di 100 px di larghezza e 100 px di altezza produce **100 x 100 = 10000 punti** e quindi, siccome a ogni punto corrisponde una coordinata, ci sono **10000 coordinate XYZ** o vettori.


</div>


<div class="mw-translate-fuzzy">

### L\'interfaccia


</div>

<img alt="Texture 002" src=images/Texture_002.png  style="width:300px;">





<div class="mw-translate-fuzzy">

#### Coordinate

-   Coordinate X: <img alt="" src=images/Std_CoordinateSystem.svg  style="width:24px;"> {{SpinBox|0,00 mm}} : Coordinata X della posizione dell\'oggetto, di default : 0.
-   Coordinate Y: <img alt="" src=images/Std_CoordinateSystem.svg  style="width:24px;"> {{SpinBox|0,00 mm}} : Coordinata Y della posizione dell\'oggetto, di default : 0.
-   Coordinate Z: <img alt="" src=images/Std_CoordinateSystem.svg  style="width:24px;"> {{SpinBox|0,00 mm}} : Coordinata Z della posizione dell\'oggetto, di default : 0.


</div>


<div class="mw-translate-fuzzy">

#### Stetching

-   Stetching X {{SpinBox|0,00 mm}} : diminuisce o aumenta la lunghezza dell\'oggetto, di default : 0.
-   Stetching Y {{SpinBox|0,00 mm}} : aumenta l\'altezza dell\'oggetto, di default : 0.
-   Stetching Z {{SpinBox|0,00 mm}} : diminuisce o aumenta la profondità dell\'oggetto, di default : 0.


</div>


<div class="mw-translate-fuzzy">

#### Inversion

-    {{CheckBox|Axis X}}: Inverte le coordinate **X** dell\'immagine.

-    {{CheckBox|Axis Y}}: Inverte le coordinate **Y** dell\'immagine.

-    {{CheckBox|Axis Z}}: Inverte le coordinate **Z** dell\'immagine.


</div>


<div class="mw-translate-fuzzy">

#### Mode 8 Bits {#mode_8_bits}

Il valore iniziale dell\'operazione si adegua automaticamente alla funzione selezionata: 0 se l\'impostazione è su Nero (Black), oppure 255 o 20 se l\'impostazione è Bianco (White)


</div>


<div class="mw-translate-fuzzy">

-    {{RadioButton|TRUE|<img src="images/Draft_Wire.svg" width=24px> Wire}}: Costruisce la linea (i vettori) in forma di Wire.

-    {{RadioButton|<img src="images/Draft_BSpline.svg" width=24px> Bspline}}: Costruisce la linea (i vettori) in forma di Bspline.

-    {{RadioButton|<img src="images/Workbench_Points.svg" width=24px> Cloud}}: Crea i vettori dei punti nella nuvola di punti.

-    {{RadioButton|<img src="images/Draft_Point.svg" width=24px> Point}}: Crea un punto per ogni pixel (vettoriale). (La procedura può essere lunga)

-    {{CheckBox|Nuance}}: Se Nuance è attivato i colori dei punti sono restituiti come se fosse una foto.


</div>


<div class="mw-translate-fuzzy">

#### Mode 32 Bits {#mode_32_bits}

-    {{RadioButton|TRUE|Photo}}: Il modo Photo è attivato automaticamente quando viene rilevata una immagine di **32 bit**. (La procedura può essere lunga)

-    {{RadioButton|Plan}}: Il modo Plan consente di importare una immagine di **32 bit** e ignorare lo sfondo del piano. Il colore predefinito dello sfondo del piano è il nero, per ignorare più colori regolare il **Capping**. Se è selezionato il bianco, ignora il bianco e lascia passare tutti gli altri colori. (La procedura può essere lunga)


</div>


<div class="mw-translate-fuzzy">

#### Files

-    {{CheckBox|.pcd}}: Se è selezionato viene salvato un file originalName.bmp.pcd nella stessa directory del file (pcd v0.7).

-    {{CheckBox|.asc}}: Se è selezionato viene salvato un file originalName.bmp.asc nella stessa directory del file. Questo file può essere usato come una nuvola di punti (formato: X Y Z).


</div>


<div class="mw-translate-fuzzy">

#### Capping (10mm) {#capping_10mm}

-   Slider : Definisce l\'altezza della forma, l\'altezza viene visualizzata nel riquadro del titolo.

-    {{SpinBox|0 height}}: Definisce l\'altezza della forma, l\'altezza viene visualizzata nel riquadro del titolo.

-   Raw mode {{CheckBox|20}} : Serve a regolare il numero di colori (livelli). La modalità predefinita è 0-19 (che costituisce un filtro e permette di ottenere maggiori dettagli, secondo la complessità dell\'immagine). Quando viene selezionata questa opzione la modalità passa a 0-255 (tutta la scala di colori).

-    {{CheckBox}}: Questo checkBox abilita lo spinbox.

-    {{SpinBox|0/2 Contour}}: Questa casella numerica determina il colore che deve essere rimosso per ottenere il contorno dell\'oggetto (ad esempio 0 per rimuovere lo sfondo).

-   Capping {{CheckBox|White}} : L\'operazione di tappatura può essere eseguita su colori a scelta, bianco (impostazione predefinita) o nero. Il grado di tappatura si regola da 19 a 0 (o da 255 a 0) se la casella di controllo è impostata su **White** , oppure da 0 a 19 (o da 0 a 255) se la casella di controllo è impostata su **Black**.

-    {{SpinBox|20 Capping}}: Questa casella numerica determina il grado di Capping


</div>


<div class="mw-translate-fuzzy">

#### Command

-    **File and launch**: Apre il file immagine e avvia la conversione.

-    **Help**: Apre la pagina del wiki dentro il FreeCAD webBrowser

    -   Visualizza la pagina Wiki nel browser di FreeCAD
    -   Per modificare il parametro disponibile: vai su \'\' \'Strumenti → Modifica parametro \...\' \'\'
    -   \_\_ Il passaggio globale su spinBox: \_\_
    -   User parameter:**BaseApp/Preferences/Macros/FCMmacros/FCTexture → SingleStep**
    -   Regola il valore desiderato (1.0 per impostazione predefinita)
    -   \_\_ Per la ricerca se la macro è aggiornata: \_\_
    -   User parameter:**BaseApp/Preferences/Macros/FCMmacros/FCTexture → switchVesionMacroSearch**
    -   Regola switchVesionMacroSearch su `True` (`False` per impostazione predefinita)


</div>


<div class="mw-translate-fuzzy">

-    **Quit**: Esce dalla funzione.


</div>

## Script

Le icone in formato .png <img alt="" src=images/FCTexture.png  style="width:64px;"> e .svg<img alt="" src=images/FCTexture.svg  style="width:64px;">

**Macro\_Texture.FCMacro**

Scaricare la macro da Gist [Macro FCTexture.FCMacro](https://gist.github.com/mario52a/262317bc7d8555885b0e)

## Esempio

Le immagini sono state inclinate per esaltare l\'effetto 3D.


<center>

<File:FCTexture_008.png%7CHonda>


</center>



<center>

<File:Macro_FCTexture_008b.png%7CHere> with option contour


</center>


<center>

<File:Texture> Nano Photo.png\|Ecco un esempio di immagine bmp convertita in punti e ripristinata in foto larga 6.5 nm
[Grazie a Yorik per l\'autorizzazione](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893#p47075) Image:Texture NanoDesign.png\|Questo è un esempio di immagine bmp convertita in oggetto 3D largo 6.7 nm.
[Grazie a Yorik per l\'autorizzazione](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893#p47075)


</center>



<center>

Image:Texture 001 Logo.png\|Il logo di FreeCAD. Image:Texture 002 Fe FC.png\|Una parte dello sfondo di FreeCAD. Il [file](http://forum.freecadweb.org/viewtopic.php?f=3&t=4708&start=10#p46353).


</center>



<center>

Image:Texture\_003\_napperon.png\|Una porzione di una tovaglia. Image:Texture\_005\_larme.png\|Una lastra zigrinata.


</center>



<center>

<File:FCTexture> 006.png\|Modo Plan: nell\'immagine a sinistra è stato ignorato lo sfondo bianco, nell\'immagine a destra è stato ignorato il colore nero (uno [esempio](http://forum.freecadweb.org/viewtopic.php?f=3&t=6123&hilit=teobo&start=10#p49024) su il foro)


</center>



<center>

<File:Texture> Topographie.png\|Esempio con un\'immagine topografica di un Terrill dove ogni gradino corrisponde ad un diverso livello di colore.


</center>



<center>

<File:FCTexture_007_FreeCAD_ASCII_00.png%7CImmagine> convertita in carattere ASCII (non ancora in funzione).


</center>



<center>

<File:FCTexture_Example.gif%7CProcedura> per creare il solido:
**1:** Creare un loft con lo strumento <img alt="" src=images/Part_RuledSurface.svg  style="width:24px;"> o con la <img alt="FCCreaLoft" src=images/FCCreaLoft.png  style="width:32px;"> [Macro Loft](Macro_Loft/it.md)
**2:** Selezionare tutto e estrudere con lo strumento <img alt="" src=images/Part_Extrude.svg  style="width:24px;">
**3A:** Per Linux Download [GMSHMesh](https://github.com/psicofil/Macros_FreeCAD) (autore psicofil) [Pagina del wiki Macro GMSH](Macro_GMSH/it.md)
**3B:** Per Windows Download [GmshMesh2.zip](http://forum.freecadweb.org/download/file.php?id=15220) decomprimere il file e installarlo nella propria directory Mod (autore ulrich1a)
**4:** Creare il proprio file Mesh e utilizzarlo


</center>



<center>

<File:FCTexture> Example Mesh.png\|Converte solidi in mesh con [GmshMesh.](Macro_GMSH/it.md)


</center>


## Link

La discussione sul [forum](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893) per esprimere le proprie impressioni e contattare l\'autore.

La <img alt="FCCreaLoft" src=images/FCCreaLoft.png  style="width:32px;"> [Macro Loft](Macro_Loft/it.md) che permette di automatizzare il \"multi loft\"

[apply hair cell texture](http://forum.freecadweb.org/viewtopic.php?f=3&t=4708&start=10#p46353)

[How to handle pdf import properly and feasibly?](http://forum.freecadweb.org/viewtopic.php?f=3&t=6123&hilit=teobo&start=10#p49024)

## Revisioni

-   Ver 0.14c : 15-01-2021 include **Gui.SendMsgToActiveView(\"ViewFit\")**

-   Ver 0.14b : 15-01-2021 Create Tab Coordinate and Tab Stretching for diminish the height of the macro and accepted in 15\" screen

-   ver 0.14 : 06/01/2021 change the search path procedure and adding preference option: search the new macro upgraded


```python
                ####new2
                pathFile      = os.path.dirname(SaveName) + "/"  #= C:/Provisoire400/
                formatFichier = os.path.splitext(SaveName)[1]    #= .png
                SaveName      = os.path.splitext(SaveName)[0]    #= /home/kubuntu/.FreeCAD/Macro/Texture_007_H #= C:/Provisoire400/image3D
                SaveNameformatFichier = SaveName + formatFichier #= C:/Provisoire400/image3D.png
                ####new2
                FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/FCTexture").SetString("Path",pathFile)
                ####new
```

-   ver 0.13b: 30/12/2020 add try for **time.clock()** and **time.process\_time()** for Python 3xyz\...
-   ver 0.13 : 17/04/2020 Layout and PySide2 Qt5
-   ver 0.12 : 04/08/2019 add spinbox button for height
-   ver 0.11 :03/07/2019 adapt to Python 3
-   ver 0.10 : 28/12/2016 add save point in .pcd, .asc display a points cloud, height form, contour
-   ver 0.9 : 12/12/2016 adding save file .asc for cloud point
-   ver 0.8 : 16/03/2016 adding progressBar
-   ver 0.7 : 03/09/2014 Delete \"**translate**\" forgotten and bug fix discovered by the passage of PyQt to Pyside !
-   ver 0.6 : 26/08/2014 Delete all \"**\_translate**\"
-   ver 0.5 : 25/08/2014 Delete \"**\_translate (\" MainWindow \",**\" Stretching X \"**, None)**\" that prevented the display of tooltip with PySide (Windows Vista)

ver 0.4 : 08/08/2014 PyQt4 PySide

ver 0.3 : 28/03/2014 :commentata la riga \"**\# self.checkBox\_5.setAccessibleName(\_fromUtf8(\"\"))**\" che causa un errore con la seguente versione di FreeCAD : 0.14.3343 (Git), Python version: 2.7.6, Qt version: 4.8.5




