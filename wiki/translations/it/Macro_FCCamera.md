# Macro FCCamera/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Macro FCCamera
|Translate=Posizione camera
|Icon=FCCamera_00.png
|Description={{ColoredText|#ff0000|#ffffff|New version GUI modifyed for the HD dpi (QGridLayout) run only FC version 0.18 and more (PySide2 Qt5)}}<br/>For the precedent version see [https://gist.githubusercontent.com/mario52a/4aa545c23b323cf68824/raw/42dc3ef73dc8db463a03b175f5a7f1f6978e3293/Macro%2520FCCamera.FCMacro FCCamera] and install it manually.<br/><br/> Questa macro può ruotare lo schermo di un determinato angolo, lungo un asse a scelta e creare un piano frontale allo schermo.
|Author=Mario52
|Version=0.14
|Date=2020/10/20
|FCVersion=0.18 e più
|Download=[https://forum.freecadweb.org/download/file.php?id=79288 FCCamera_Icones.zip]. Unzippato il pacchetto e incollare l'icona totale nella stessa directory della macro. 
}}


</div>




<div class="mw-translate-fuzzy">

## Descrizione

Questa macro serve per ruotare lo schermo di un determinato angolo lungo l\'asse voluto e per creare un piano frontale allo schermo in cui produrre una forma in una specifica posizione del piano della faccia selezionata rivolta verso lo schermo, inoltre serve per rilevare la posizione della fotocamera, per allineare la vista alla faccia o all\'asse e per allineare l\'oggetto alla vista.


</div>

This macro can rotate the screen in a defined angle and the defined axis and creates a plan to face the screen to create a form in the specified plan positions the selected face facing the screen, to detect the position of the camera, align view to face or to axis, align the object to view.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/4aa545c23b323cf68824/raw/98d90ee303e9fa5d6aed6e9f2e36e7ca1a18ca19/Macro%2520FCCamera.FCMacro}}



## Utilizzo


<div class="mw-translate-fuzzy">

![FCCamera](images/Macro_FCCamera_00.png )


</div>

**Camera of Axis**: La finestra di dialogo per immettere il valore dell\'angolo di rotazione in gradi.


<div class="mw-translate-fuzzy">

**Angle rotation Axis in degrees**: Selezionare l\'asso di rotazione **X, Y,**, **Z** o **D**.


</div>

**Axe of rotation**: Serve per selezionare l\'asse di rotazione X, Y, Z o D.

-   <img alt="" src=images/FCCamera_01.png  style="width:24px;"> **Accept the rotation** : Serve per confermare i valori inseriti

**Virtual**


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FCCamera_02.png  style="width:24px;"> **Detect camera orientation** : Rileva l\'orientamento della fotocamera e lo stampa nella vista Report. Il valore restituito è il valore fornito dalla funzione getCameraOrientation().


</div>

**Align view to face selected**

-   <img alt="" src=images/FCCamera_03.png  style="width:24px;"> **To Face.** : Allinea la vista alla faccia selezionata. Fare clic e ripetere il clic per **NormalAt** : \"(0,0,1) (0,0,-1) (0,1,0) (0,-1,0) (1,0,0) (-1,0,0)\"

-   <img alt="" src=images/FCCamera_04.png  style="width:24px;"> **To Axis.** : Allinea la vista della faccia selezionata agli Assi. Fare clic e ripetere il clic per **Surface Axis** : \"(0,0,1) (0,0,-1) (0,1,0) (0,-1,0) (1,0,0) (-1,0,0)\"


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FCCamera_05.png  style="width:24px;"> **Align object to view.** : Allinea l\'oggetto selezionato alla vista attiva. Modifica i valori di : Rotation Axis((X, Y, Z), Angle) come angoli di Eulero : Yaw, Pitch, Roll. Translation non viene modificata.


</div>

-   <img alt="" src=images/FCCamera_06.png  style="width:24px;"> **Create plane of view.** : crea un piano circolare frontale allo schermo con le coordinate del punto cliccato con il mouse su un oggetto. Il raggio del piano è uguale alla dimensione massima di boundbox. Se non è selezionato alcun oggetto, il piano viene creato nel punto 0, 0, 0 con un raggio di 20 mm. Il raggio è modificabile nella riga 515:


```python
        rayon = 20                            # Radius of plane
```


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FCCamera_07.png  style="width:24px;"> **Reset.** : Ripristina tutti i valori.
-   <img alt="" src=images/FCCamera_08.png  style="width:24px;"> **Quit.** : Esce da FCCamera.


</div>


<div class="mw-translate-fuzzy">

## Sezione Photo 


</div>


<div class="mw-translate-fuzzy">

![FCCamera](images/Macro_FCCamera_00b.png ) 


</div>


<div class="mw-translate-fuzzy">

-    **ComboBox Actual **: scegliere la propria definizione dello schermo per il formato dell\'immagine

    -   Available (pre-definito):
        -   \"Actual\" (definizione attuale dello schermo)
        -   \"Icon 16 x 16\"
        -   \"Icon 32 x 32\"
        -   \"Icon 64 x 64\"
        -   \"Icon 128 x 128\"
        -   \"CGA 320 x 200\"
        -   \"QVGA 320 x 240\"
        -   \"VGA 640 x 480\"
        -   \"SVGA 800 x 600\"
        -   \"XGA 1024 x 768\"
        -   \"XGA+ 1152 x 864\"
        -   \"SXGA 1280 x 1024\"
        -   \"SXGA+ 1400 x 1050\"
        -   \"UXGA 1600 x 1200\"
        -   \"QXGA 2048 x 1536\"
        -   \"Free\"


</div>

-    **SpinBox X and Y **
    

-    **ComboBox  Format image**-   Available :
        -   \"BMP \*.bmp\"
        -   \"ICO \*.ico\"
        -   \"JPEG \*.jpeg\"
        -   \"JPG \*.jpg\"
        -   \"PNG \*.png\" (by default)
        -   \"PPM \*.ppm\"
        -   \"TIF \*.tif\"
        -   \"TIFF \*.tiff\"
        -   \"XBM \*.xbm\"
        -   \"XPM \*.xpm\"




-   Line 2 : La definizione di schermo utilizzata

-   Immagine di sfondo :
    -   Actual : salva l\'immagine con il colore dello schermo effettivo
    -   White : salva l\'immagine con il colore dello schermo bianco
    -   Black : salva l\'immagine con il colore dello schermo nero

-    **[<img src=images/FCCamera_00.png style="width:24px"> Launch**: Apre la finestra del file, indica il nome e il percorso

-    **[<img src=images/FCCamera_07.png style="width:24px"> Reset**: Reimposta il valore predefinito

-    **[<img src=images/FCCamera_00.png style="width:24px"> Return**: Esce dal pannello foto e torna al pannello di FCCamera







<div class="mw-translate-fuzzy">

## Link

Link delle macro collegate a FCCamera


</div>

Related Links with FCCamera


<div class="mw-translate-fuzzy">

[Macro Rotate View](Macro_Rotate_View/it.md), [Macro Align Object to View](Macro_Align_Object_to_View/it.md), [Macro Align Face Object to View](Macro_Align_Face_Object_to_View/it.md), [Macro WorkFeatures](Macro_WorkFeatures/it.md)


</div>

La discussione nel forum [MACRO:Work Feature 2014_12](http://forum.freecadweb.org/viewtopic.php?f=22&t=9056)

## Script

Scaricare gli icone [FCCamera_Icones.zip](https://forum.freecadweb.org/download/file.php?id=79288)

Scaricare la macro da Gist [**Macro FCCamera.FCMacro**](https://gist.github.com/mario52a/4aa545c23b323cf68824)



## Esempi



### Come creare un foro inclinato 


<div class="mw-translate-fuzzy">


<center>

<File:FCCamera> 09.png\|Creare un oggetto <File:FCCamera> 10.png\|Creare un cilindro e posizionarlo
Scegliere l\'asse, assegnare l\'angolo di inclinazione, ad es. 15°, e poi cliccare su <img alt="" src=images/FCCamera_01.png  style="width:24px;"> 
**Accept the rotation**


</center>


</div>


<div class="mw-translate-fuzzy">


<center>

<File:FCCamera> 11.png\|Selezionare il cilindro da usare per creare il foro <File:FCCamera> 12.png\|In FCCamera cliccare su <img alt="" src=images/FCCamera_05.png  style="width:24px;"> 
**Align Object to View**


</center>


</div>


<div class="mw-translate-fuzzy">


<center>

<File:FCCamera> 13.png\|Il cilindro si inclina di 15° (assume la posizione della camera).
Poi eseguire l\'operazione booleana. <File:FCCamera> 14.png\|Ecco il foro inclinato di 15°.


</center>


</div>


<div class="mw-translate-fuzzy">

Si può ottenere lo stesso risultato posizionando uno schizzo su un piano inclinato


</div>


<div class="mw-translate-fuzzy">


<center>

<File:Macro_FCCamera_Align_To_Face.gif%7CEsempio> di posizionamento della molla in asse con la faccia


</center>


<center>

<File:Test_FCCamera_Photo_01.gif%7CEsempio> di utilizzazione di rotazione della vista 3D e salvamento delle immagine (Potete creare uno filo animato Gif [con GIMP](https://www.gimp.org/))


</center>


</div>



## Versione

-   **ver 0.14 (20/10/2020):** corretto bug \"Grid\" non accettata

-   **ver 0.13 (28/06/2020):** adding files image in source code, create plane \"On point, Center face, BBox center, Center Mass\", gridLayout

-   **ver 00.12.1 (12/02/2020):** suppress the bad character lines 674 and 675 (accent\...) again

-   **ver 12 (01/08/2019):** compatible Python 3 ( print to print() )

-   **ver 11 (13/01/2018):** minor

-   **ver 10 (13/01/2018):** add \"def centerBoundBoxGlobal():\"

-   **ver 09 (08/01/2018):** minor

-   **ver 08 (08/01/2018):** supp \"Pyqt4\"
-   **ver 07 (03/01/2018):** aggiunto pannello foto e rotazione sull\'asse selezionato (polilinea, bordo, linea)

-   **ver 0.6 (13/12/2016):** nuovo sistema per verificare il percorso delle macro direttamente nelle preferenze

#path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
#path = "your path"
param = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro")# macro path
path = param.GetString("MacroPath","") + "/"                        # macro path
path = path.replace("\\","/")
App.Console.PrintMessage("Path locality to FCCamera.....images.png [ " + path + " ]"+"\n")

-   **ver 0.5 06/09/2016:** correct name \"FCCamera_Axis_rotation_X.png\" in reset block

-   **ver 0.4 28/02/2016 :** add display all camera detection and the [Direction](http://forum.freecadweb.org/viewtopic.php?f=13&t=14213#p114667)

-   **ver 0.3 18/03/2015 :** modify line 492 replace \"**pl.Base = App.Vector(0,0,0)**\" to \"**pl.Base = sel\[0\].Placement.Base**\" now no longer moves the form at point (0,0,0) and leaves has the coordinates

-   **ver 0.2 25/02/2015 :** correct names files in for compatibility Linux (case sensitive) thanks microelly2



---
⏵ [documentation index](../README.md) > Macro FCCamera/it
