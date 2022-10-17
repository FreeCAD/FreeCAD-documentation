# Macro FCCircularText/it
{{Macro/it
|Name=Macro FCCircularText
|Translate=Testo Circolare
|Icon=FCCircularTextButtom.png
|Description={{ColoredText|#ff0000|#ffffff|La nuova GUI della versione modificata per l'HD dpi (QGridLayout) esegue solo la versione FC 0.18 e successive (PySide2 Qt5)}} <br/><br/>Per la versione precedente vedere [https   *//gist.githubusercontent.com/mario52a/a25e802498bae6959335/raw/db47f78f2b20a35137ac213b8d1a62d30f525dcb/Macro_FCCircularText.FCMacro FCCircularText] and install it manually. <br/><br/>Questa macro crea un testo intorno ad un cilindro.<br />Ultima Versione=0.14 Date=2019/04/27<br />Download the [https   *//www.freecadweb.org/wiki/images/c/c1/FCCircularTextButtom.png toolBar icon]<br />
|Version=0.22
|Date=2022/06/06
|FCVersion=0.19 è più
|Download=[https   *//www.freecadweb.org/wiki/images/c/c1/FCCircularTextButtom.png ToolBar Icon]
}}

## Descrizione

Questa macro usa <img alt="" src=images/Draft_ShapeString.svg  style="width   *24px;"> [Draft ShapeString](Draft_ShapeString/it.md) è scrive un testo, in piedi o coricato, circonferenziale o elicoidale nel modo di [Trajan Column](http   *//en.wikipedia.org/wiki/Trajan%27s_Column) e crea un orologio con numeri arabi **1 2 3 \...** o Romani **I II III \...** (ispirata a [Macro to Create Clock Face](http   *//forum.freecadweb.org/viewtopic.php?f=22&t=5013&hilit=Clock)) FC community member, cblt2l.


{{Codeextralink|https   *//gist.githubusercontent.com/mario52a/a25e802498bae6959335/raw/cffba4018708a61e43c7f19627993c3e80182312/Macro_FCCircularText.FCMacro}}

<img alt="texte 360 degrees" src=images/FCCircularText_01.png  style="width   *400px;"> 
*Esempio di macro che mostra il testo con un orientamento a 360 gradi*

## Utilizzo

Usare la macro **FcString** per creare dei caratteri e il file **FcClock** per creare degli orologi.

Tutti i caratteri sono e rimangono indipendenti. Quando si creano le estrusioni non viene eliminato nulla. Se viene creato un Compound (oggetto Composto) con **Run Comp** esso viene copiato in una nuova cartella.

Di default le opzioni sono disattivate e si attivano quando si seleziona {{CheckBox|TRUE|}} una delle funzioni   *

-    {{CheckBox|Extrude Char.}}
    

-    {{CheckBox|Placement.}}
    

-    {{CheckBox|SP. inclination.}}
    

Fatta eccezione per la casella **Z** di Placement per Clock che è attiva e che sposta il testo lungo l\'asse Z per consentire posizionare il testo sulla superficie di appoggio.

## Nota

Le opzioni che sono facoltative per la funzione selezionata sono inattive e quindi non utilizzabili.

## L\'interfaccia grafica di Circular Text 

Panoramica

![GUI](images/FCCircularText_06.png ) 

### Prima sezione 

![](images/FCCircularText_07.png ) 

-   La finestra di editazione del testo che consente di inserire il testo da visualizzare (cliccando su **Reset**, nella finestra del titolo si può vedere quanti caratteri contiene la stringa di input)

-   Il pulsante **Reverse** serve per invertire il testo

-    {{CheckBox|Word}}selezionata, questa opzione considera il testo come parola, il testo viene tagliato nello spazio e scrive il testo parola per parola (invece carattere per carattere nell\'uso normale)

-   Il **Help** visualizza la pagina wiki nel browser FreeCAD

-   LineEdit    * visualizza il percorso e il nome del font del file

-    **Other**per cercare altre font in altri directory

-   ComboView per il font scelto

-    **Origin**ritorna al l\'origine sistema font ex   * \"C   */Windows/Fonts/\"

    -   ARIAL.TTF è il font di default

#### Opzioni disponibili 

Dopo il primo utilizzo, è possibile modificare i parametri vedere   *

**User parameter   *BaseApp/Preferences/Macros/FCMmacros/FCCircularText**

**switchModeTextList**

-   0 = modalità testo normale (e nero) chiude switchFontComBox
-   1 = consente switchFontComBox 1

**switchFontComBox**

-   0 = (e switchModeTextList = 1) modalità testo (a colori) nell\'elenco ComboBox, più veloce
-   1 = (e switchModeTextList = 1) font ComboBoxst più lento ma più bello!

**setSystemFonts**

-   0 = matplotlib.font_manager.findSystemFonts (\"C   */\", \"ttf\")
-   fare tutti i caratteri (in tutte le cartelle e sottocartelle del DD) tempo !!
-   1 = fontman.findSystemFonts (self.pathFont)
-   esegue tutti i caratteri nella directory (e in tutte le sottocartelle)

**seTtextAlignement**

-   0 = AlignLeft (default)
-   1 = AlignCenter
-   2 = AlignRight

setFontByDefault

-   Font impostazione predefinita (ultimo utilizzato)

**switchResetFALSE**

-   0 = reset (predefinito)
-   1 = nessun reset (sconsigliato) alcuni switch possono rimanere aperti o chiusi inaspettatamente!

**Esempio**

![](images/FCCirculatText_Config_0000A0.png )

1.  switchModeTextList= `False`
2.  switchFontComBox = `False`
3.  setSystemFonts = `False`
4.  seTtextAlignement = 0




![](images/FCCirculatText_Config_1000A0.png )

1.  switchModeTextList= `True`
2.  switchFontComBox = `False`
3.  setSystemFonts = `False`
4.  seTtextAlignement = 0




![](images/FCCirculatText_Config_1001A0.png )

1.  switchModeTextList= `True`
2.  switchFontComBox = `False`
3.  setSystemFonts = `False`
4.  seTtextAlignement = 1 *(0=Left, 1=Centered, 2=Right)*




![](images/FCCirculatText_Config_1101A0.png )

1.  switchModeTextList= `True`
2.  switchFontComBox = `True`
3.  setSystemFonts = `False`
4.  seTtextAlignement = 1




## Seconda sezione 

Configurare i caratteri in FCCircularText

![](images/FCCircularText_08.png ) 

#### Prima zona 

Scegliere   *

![](images/FCCircularText_09.png )


<center>

Image   *FCCircularText 20.png\|**Outdoor** esterno Image   *FCCircularText 21.png\|**Indoor** interno Image   *FCCircularText 22.png\|**Helix** elicoidale Image   *FCCircularText 23.png\|**Clock** orologio


</center>




![](images/FCCircularText_24.png )

-    **Mode Stand**o **Mode Flat**    * Il testo può essere messo in piedi o coricato e le opzioni **Outdoor** e **Indoor** indicano se è rivolto verso l\'esterno o verso l\'interno .





<center>

Image   *FCCircularText 01.png\|**Mode Stand** **Outdoor** Il testo è disposto verticale, leggibile dall\'esterno. Image   *FCCircularText_40.png\|**Mode Flat** **Outdoor** Il testo è posizionato orizzontale, leggibile dall\'esterno.


</center>


<center>

Image   *FCCircularText 39.png\|**Mode Flat** **Indoor** Il testo è orizzontale, leggibile dall\'interno. Image   *FCCircularText_03.png\|**Mode Stand** **Indoor** Il testo è verticale, leggibile dall\'interno.


</center>

#### Seconda zona 

Questa sezione permette di configurare il comportamento complessivo dei caratteri in tutte le scelte disponibili, ma con qualche variazione. I comandi non utilizzabili con l\'opzione scelta sono visualizzati in grigio.

![ left](images/FCCircularText_10.png )

-    {{SpinBox|10.0 mm}}**Radius of circle**    * Raggio del cerchio. (Default 10)

-    {{SpinBox|2.0 mm}}**Size character**    * Altezza del carattere. (Default 2)

-    {{SpinBox|0 deg}}**Begin angle**    * Angolo a cui posizionare il primo carattere. (Default 0 °)

-    {{SpinBox|360 deg}}**End angle**    * Angolo a cui posizionare l\'ultimo carattere. (Default 360)

-    {{SpinBox|10.0 deg}}**Correction angle**    * Angolo di correzione per rendere il carattere tangente al cerchio. (Default 10 °)

-    {{SpinBox|0.15 mm}}**Correction radius**   * Corregge il raggio del cerchio dei caratteri (optional). (Default 0.15)

-
-    {{CheckBox|'''Extrude Char'''}}   * Estrusione dei caratteri. (di default è disattivato)

-    {{CheckBox|'''Placement'''}}   * Posizione del testo nella vista 3D. (di default è disattivato)

-    {{CheckBox|'''Sp. inclination'''}}   * Inclinazione del testo rispetto agli assi X, Y e Z (ad esempio per scrivere su un cono). (di default è disattivato)




##### Outdoor

Modo di default. Il testo viene scritto all\'esterno della circonferenza del cerchio.


<center>

Image   *FCCircularText 20.png\|**Outdoor** Image   *FCCircularText 25.png\| Image   *FCCircularText 30.png\|


</center>

##### Indoor

Il testo viene scritto all\'interno della circonferenza del cerchio


<center>

<File   *FCCircularText> 21.png\|**Indoor** Image   *FCCircularText 03.png\| Image   *FCCircularText 27.png\|


</center>

##### Helix

Il testo viene inserito all\'esterno di un\'elica.


<center>

Image   *FCCircularText 22.png\| **Helix** Image   *FCCircularText 33.png\| Image   *FCCircularText 34.png\|


</center>

![](images/FCCircularText_11.png )

-   L\'area dell\'elica è nascosto e solo visibile se il {{RadioButton|Helix}} e verificato.




![](images/FCCircularText_14.png )

-   Tutte le opzioni di configurazione dei caratteri sono disponibili.
-   **Step of helix** passo dell\'elica
-   **Char. per turn** numero di caratteri per ogni spira dell\'elica.




![](images/FCCircularText_15.png )

-   Se **Step of helix** (passo dell\'elica) è zero, i campi **Base Helix** e **End Helix** sono attivi.
-   **Base Helix** fornisce la base per iniziare l\'elica (anche Placement Z). Se *\'Placement Z\'* è diverso da zero, il punto di partenza viene aggiunto a Placement Z.
-   **End Helix** Fine di passo dell\'elica che è calcolato rispetto all\'altezza e al numero di caratteri per spira.

##### Orologio

Le figure sono parte di un cerchio con numeri arabi o romani.


<center>

Image   *FCCircularText 23.png\|**Clock** Image   *FCCircularText 35.png\|**Axial** Image   *FCCircularText 36.png\|**Redress**


</center>

-   Di default, è nascosto e solo visibile se il {{RadioButton|Clock}} e verificato.




![](images/FCCircularText_16.png )

-   Quando si seleziona l\'orologio, diventano utilizzabili le seguenti funzioni   *
    1.  Angolo iniziale.
    2.  Angolo finale.
    3.  Angolo di correzione.
    4.  Correzione del raggio.
    5.  I pulsanti **Mode Stand** o **Mode Flat**.
-   L\'area **Clock** è attiva.




![](images/FCCircularText_19.png )

-   **Radius of support**    * Se viene dato un valore, viene creato un supporto (default 0).
-   Se **Support number face** è diverso da zero viene creato un supporto. Se **Extrude support**= zero viene creata una faccia.
    -   1 = Viene creato un cerchio. Appare un cerchio.
    -   2 = Viene creato un rettangolo. Lunghezza = (Radius of media \* 1.5) width = Radius of support. Appare un rettangolo.
    -   3 = Viene creato un triangolo circoscritto. Appare un triangolo.
    -   4 = Viene creato un quadrato, raggio del supporto. Appare un quadrato.
    -   5 = Viene creato un poligono circoscritto con il numero di facce indicate. Appare un poligono.
-   **Extrude support** viene attivato e si può fornire una dimensione di estrusione.




<img alt="" src=images/FCCircularText_18.png )![](images/FCCircularText_38.png  style="width   *200px;">  <img alt="" src=images/FCCircularText_17.png )![](images/FCCircularText_37.png  style="width   *200px;"> 

-   Se **Support number face** è uguale a zero non c\'è il supporto.

-    **Mode Roman**   * La scrittura è in cifre romane **I II III IIII V VI VII VIII IX X XI XII**

-    **Axial**   * I dati sono scritti assialmente.

### Path section 

![](images/FCCircularText_06_Path.png ) 

La sezione del titolo cambia e visualizza la lunghezza del filo selezionato.

Se selezioni un filo, un arco, un cerchio, una linea e un bordo, il percorso della sezione è colorato in {{ColoredText|#E0F8E0|green}} e il comando inutilizzato è colorato in {{ColoredText|#F8E0E0|red}}

1.  
    {{RadioButton|Orthogonal}}il carattere è ortogonale alla vista

2.  
    {{RadioButton|Tangent}}il carattere è tangente al percorso del punto sul filo




1.  
    {{RadioButton|BB Base}}il punto base del carattere deve puntare il percorso sul filo

2.  
    {{RadioButton|BB Center}}il centro del bounBox del personaggio deve indicare il percorso sul filo

3.  
    {{RadioButton|BB Top}}il boundBox superiore del carattere deve indicare il percorso sul filo

l\'ultimo pulsante di opzione utilizzato viene salvato nel parametro di FreeCAD

### Sezione comandi 

![](images/FCCircularText_13.png ) 

-    **Exit**   * Esce dalla macro macro.

-    **Reset**   * Ripristina tutti i valori e visualizza il numero di caratteri visualizzati nella finestra.

-    **Run Comp**   * Lancia la macro e crea un oggetto Composto da tutti i caratteri.

-    **Run**   * Lancia la macro

### Parametri disponibili 

Alcuni parametri sono disponibili nei parametri di FreeCAD vedere   ***Menu → Tools → Edit parameters...**

-   User parameter   * BaseApp/Preferences/Macros/FCMmacros/FCCircularText

-   -   
        `switchModeTextList`
        
           *

        -   
            `False`
            
            normale modalità di testo (e nero) si trasforma off switchFontComBox

        -   
            `True`
            
            permettere switchFontComBox 1 (default)

    -   
        `switchFontComBox`
        
           *

        -   
            `False`
            
            (é switchModeTextList = 1) modalità testo (a colori) nell\'elenco ComboBox più veloce (predefinito)

        -   
            `True`
            
            (and switchModeTextList = 1) Famiglia di caratteri nell\'elenco ComboBox più lento ma più bello!

    -   
        `setSystemFonts`
        
           *

        -   
            `False`
            
            matplotlib.font_manager.findSystemFonts (\"C   * /\", \"ttf\") fare tutti i caratteri (in tutte le cartelle e sottocartelle dell\'HD) tempo !!

        -   
            `True`
            
            fontman.findSystemFonts (self.pathFont)crea tutti i caratteri nella directory (e in tutte le sottocartelle) (predefinito)

    -   
        `seTtextAlignement`
        
           * 0 = AlignLeft (default) 1 = AlignCenter 2 = AlignRight

    -   
        `setFontByDefault`
        
           * Carattere predefinito (l\'ultimo utilizzato)

    -   
        `switchResetFALSE`
        
           * `False` reset (default), `True` no reset (non consigliato) alcuni interruttori possono rimanere aperti o chiudersi inaspettatamente!

    -   
        `setPathOrthogonal`
        
           * `True` `False`

    -   
        `setPathTangent`
        
           * `True` `False`

    -   
        `setPositionBase`
        
           * `True` `False`

    -   
        `setPositionCenter`
        
           * `True` `False`

    -   
        `setPositionTop`
        
           * `True` `False`

    -   
        `switchVersionSearch`
        
           * `True` `False`

    -   
        `Version`
        
           * FCCircularText versione

Usare la macro **FcString** per creare dei caratteri e il file **FcClock** per creare degli orologi.

## Script

Scaricare lo script da   *

L\'icona per ill pulsante   *

\- in .PNG ![](images/FCCircularTextButtom.png )

\- in .SVG <File   *FCCircularTextButtom.svg>

Per maggiori informazioni vedere [Personalizzare la barra degli strumenti](Customize_Toolbars/it.md)

### Vedi il Codice 

**Macro_Circular_Text.FCMacro**

o tele carica lo script    *

\- on github [Macro_FCCircularText.FCMacro](https   *//gist.github.com/mario52a/a25e802498bae6959335) ver 0.21 2022/05/31

\- o dal forum [Extrude from curved surface of cylinder](http   *//forum.freecadweb.org/viewtopic.php?f=3&t=7384&p=87642#p87642)

## Esempi


<center>

Image   *FCCircularText 02.png\|Testo verticale (in piedi), compreso tra 180 gradi (**Begin angle**) e 360 gradi (**End angle**), esterno alla curva. Image   *FCCircularText 03.png\|Testo interno alla curva.


</center>



<center>

Image   *FCCircularText 04.png\|Testo interno e esterno alla curva. Image   *FCCircularText 05.png\|Testo circolare orizzontale (coricato) su un oggetto piano.


</center>



<center>

Image   *FCCircularText IndoorFlat 01.png\|Configuration Superior.(click to elarge) Image   *FCCircularText IndoorFlat 02.png\|Configuration Inferior.(click to elarge)


</center>



<center>

Image   *FCCircularText 26.png\|Testo estruso, esterno alla curva. Image   *FCCircularText 28.png\|Testo estruso, interno alla curva.


</center>



<center>

Image   *FCCircularText 29.png\|Interno e sottratto. Image   *FCCircularText 31.png\|esterno alla curva.


</center>



<center>

Image   *FCCircularText 32.png\|interno e sottratto. Image   *FCCircularText 41.png\|Estrusione su un cono con **Sp. Inclination** di 45° sull\'asse Z.


</center>



<center>

Image   *FCCircularText 42.png\|Anello, interno alla curva con sottrazione. Image   *FCCircularText 61.png\|Caratteri ruotati di 0°, 90°, \....


</center>



<center>

Image   *FCCircularText_Path_00_002_000.png\| {{CheckBox|TRUE|Word}} Il testo sta tagliando sul carattere dello spazio


</center>

==Esempi su ellisse==


<center>

Image   *FCCircularText 43.png\|Crea l\'ellisse di 100x50. Image   *FCCircularText 44.png\|Estruderla di 50 mm.


</center>



<center>

Image   *FCCircularText 45.png\|Discretizzare il perimetro e creare punti con la macro [Work Features](Macro_WorkFeatures/it.md).
Tab Point \> Point 2/3 \> Points=Cut (Wire) Image   *FCCircularText 46.png\|Creare il cerchio da 3 punti con la macro [Work Features](Macro_WorkFeatures/it.md).
Tab Circle Circle=(3 Points)


</center>



<center>

Image   *FCCircularText 47.png\|Creare centro del cerchio con la macro [Work Features](Macro_WorkFeatures/it.md).
Tab Point \> Point 1/3 \> Circle(s) center. Image   *FCCircularText 48.png\|Creare le linee di riferimento e configurare FCCircularText.


</center>



<center>

Image   *FCCircularText 49.png\|Crea il testo con **Run Comp**. Image   *FCCircularText 50.png\|Selezionare Ellipse Extrude e Shape poi premere il pulsante **<img src="images/Part_Cut.png" width=16px> '''Part Cut'''**.


</center>



<center>

Image   *FCCircularText 51.png\|Eliminare il cerchio, i punti e le linee. Image   *FCCircularText 52.png\|Ellisse.


</center>

Modalità rilievo   *


<center>

Image   *FCCircularText 53.png\|Creare un ellisse. ![](images/Draft_Ellipse.png ) Image   *FCCircularText 54.png\|Creare un rettangolo che includa tutti gli oggetti. ![](images/Draft_Rectangle.png )


</center>



<center>

Image   *FCCircularText 55.png\|Selezionare il rettangolo e l\'ellisse poi creare un composto
Attivare il modulo Part, poi il menu Part \> Crea composto. Image   *FCCircularText 56.png\|Estrudere il composto in Solido.


</center>



<center>

Image   *FCCircularText 57.png\|Selezionare Shape (il testo) e il Composto poi eseguire Cut. Image   *FCCircularText 58.png\|Il testo viene intagliato nella forma dell\'ellisse.


</center>



<center>

Image   *FCCircularText 59.png\|Selezionare Ellisse estruso e il Cut (testo) e poi fonderli.


</center>


## Example section path 


<center>

Image   *FCCircularText_Path_00_Orth_Base_000.png\|Testo su BoundBox Base (normale) Image   *FCCircularText_Path_00_Orth_Center_000.png\|Testo sul carattere BoundBox Center


</center>



<center>

Image   *FCCircularText_Path_00_Orth_Top_000.png\|Testo su BoundBox Carattere superiore Image   *FCCircularText_Path_00_001_000_000.png\|Testo sulla riga selezionata   *
1   * Orthogonal
2   * Tangent


</center>

## Limitativo


**Note**

(PS   * è possibile che si verifichi un errore tra le versioni. Pubblica il problema sul forum e attendi la correzione aggiornata o il rollback a una versione precedente della macro. Grazie)

È possibile che due caratteri si sovrappongano, qui un piccolo rimedio con [Macro_Rotate_To_Point](https   *//www.freecadweb.org/wiki/Macro_Rotate_To_Point)


<center>

Image   *FCCircularText Correction.gif\|Character overlap issue and the workaround


</center>

(non totalmente sviluppato)

In projetto    *

Scrivere un testo circolare posizionato su un oggetto selezionato

## Registro delle modifiche   * 

-   ver 0.22 2022/06/06    * adding QScrollArea cause    * [Unable to run FCCircularText \[Problem with screen size\]](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=69206)

-   ver 0.21 2022/05/31    * adding button search other path fontmanuelly, and button return font origin of system

-   ver 0.20 2021/04/05    * adding icone in macro, Tab for diminish the heigth of the macro, remove all dimensions of widgets now fully compatible with the stylesheet, revisite the search version for compatibility and other little change.

-   ver 1.19 2021/03/15    * adding button **Delette** the last object created and the code `FreeCAD.ActiveDocument.openTransaction("FCCTc")` for Undo/Redo system

-   -   Adding CheckBox {{CheckBox|FALSE|Reset}} for switched/activated (*requested by users*) the natural reset after all push button **Run**and **Run comp**. This use checkBox is {{ColoredText|not advised}}, is you constade one malfunction pusch the **Reset** button or quit FCCircularText and restart.

-   ver 0.18 2021/01/19    * correction bug see [FCCircularText Macro issues](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=54524&p=468687#p468687)

-   ver 0.17b 2020/09/28    * correction little bug (pl instead plm in path section) and arrange the window (dimension) Clock, Helix, Path

-   ver 0.17 2020/09/26    * adding create circular text on wire (curve, arc, spline, line \...) selected, mode word

ver 16d 2020/09/15    * vedi [MasterCATZ commented Sep 14, 2020 message](https   *//gist.github.com/mario52a/a25e802498bae6959335)

Elimina il FC 0.18 test sezione   *


```python
#### Test FreeCAD.Version simple ############################################################################################################
if int(FreeCAD.Version()[1]) < 18   *      # Version de FreeCAD
    FreeCAD.Console.PrintMessage("This version " + __Title__ + " rmu  work with the FreeCAD 0.18 or higher." + "\n\n")
    FreeCAD.Console.PrintMessage("For the precedent version see the page " + "\n\n")
    FreeCAD.Console.PrintMessage("https   *//gist.githubusercontent.com/mario52a/a25e802498bae6959335/raw/db47f78f2b20a35137ac213b8d1a62d30f525dcb/Macro_FCCircularText.FCMacro" + "\n\n")
#### Test FreeCAD.Version simple ############################################################################################################
```

-   ver 0.16c 2020/07/24    * modify text proposed by Kunda1 [Please review FCVerticalText Macro](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=48902#p418776)

-   ver 0.16b 2020/07/24    * correct **\_\_title\_\_** to **\_\_Title\_\_** in 0.18 FC test (see [Please review FCVerticalText Macro](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=48902))

-   ver 0.16 2020/06/07    * little bug in Linux with the path, impost **PolicePath = \"/usr/share/fonts/\"** (stay on path /xx/xx/xx/xx/xx/xx/ on entry)

-   ver 0.15 2020/06/01    * For PySide2 Qt5 adding matplotlib fonts in comboView, config on parameter

-   ver 0.14-4 2020/04/25    * corretto con \"**DisplayMode = u\"Flat Lines**\"    *

-   ver 0.14-3 2020/04/25    * adatto per    *


```python
OS   * Windows 10 (10.0)
Word size of OS   * 64-bit
Word size of FreeCAD   * 64-bit
Version   * 0.19.20655 (Git)
Build type   * Release
Branch   * master
Hash   * e8e67e8c5ebbc9f9ed9ea67aba5b891969595ece
Python version   * 3.6.8
Qt version   * 5.12.1
Coin version   * 4.0.0a
OCC version   * 7.3.0
```

-   ver 0.14-2 2019/07/22 replace chr(176) (give error \<FC 0.18) and replace with the wmayer code, see [Fehler in Version 0.19 pre ??](https   *//forum.freecadweb.org/viewtopic.php?f=13&t=36380&p=308476#p308357)

       carDegrees = b' \xc2\xb0'.decode("utf-8")    #thanks wmayer [https   *//forum.freecadweb.org/viewtopic.php?f=13&t=36380&p=308476#p308357](https   *//forum.freecadweb.org/viewtopic.php?f=13&t=36380&p=308476#p308357)
       self.DS_InclinaisonX.setSuffix(carDegrees)
       self.DS_InclinaisonY.setSuffix(carDegrees)
       self.DS_InclinaisonZ.setSuffix(carDegrees)

-   ver 0.14-1 2019/06/11 replace \"°\" to chr(176)

-   ver 0.14 2019/04/27 compatibile con Python 3.6.6 and Qt 5.6.2 (cause   * unicode() )


```python
latest testing   *

#OS   * Windows 10
#Word size of OS   * 64-bit
#Word size of FreeCAD   * 64-bit
#Version   * 0.19.16523 (Git)
#Build type   * Release
#Branch   * master
#Hash   * 9b3ec233c8b21e0df66fada487cd10f471d60cac
#Python version   * 3.6.6
#Qt version   * 5.6.2
#Coin version   * 4.0.0a
#OCC version   * 7.3.0
```

-   ver 0.13 30/01/2018 add feature Pivot for rotate the character on himself

-   ~~ver 0.13 09/08/2016 replace the button \"New font\" to \"fontComboBox\" cause , with Windows 10 the window Font stay empty the files are hidden~~

-   ver 0.12 03/07/2016 optimize the code for accept the decimal number in determination angle

replace the line 
```python
            for angleTr in range(debut,rotation,((rotation-debut)/nombre))   * 
``` to 
```python
            for angleTrFloat in range((debut*10000),(rotation*10000),int((round(((float(rotation)-float(debut))/float(nombre)),4)*10000)) )   *    # pour 4 decimales
                angleTr = (float(angleTrFloat)/10000)
```

-   ver 0.10 17/05/2015 adding lines 1365, 1366 only created more clock face ?? ()


```python
            supp.MakeFace = True
            App.activeDocument().recompute()
```

-   ver 0.9 11/05/2015 thank you NormandC for testing

replace 
```python
        self.DS_InclinaisonX.setSuffix(" X°")
        self.DS_InclinaisonY.setSuffix(" Y°")
        self.DS_InclinaisonZ.setSuffix(" Z°")
``` to 
```python
        self.DS_InclinaisonX.setSuffix(unicode(" X°"))
        self.DS_InclinaisonY.setSuffix(unicode(" Y°"))
        self.DS_InclinaisonZ.setSuffix(unicode(" Z°"))
```

-   ver 0.8 10/05/2015 replace \"**String=texte\[ii2\]**\" to \"**String=unicode(texte\[ii2\])**\" line 1290. cause \"**TypeError   * Property \'FontFile\'   * type must be str or unicode, not QString**\"\<span \\\>


```python

# ver 0.8 10/05/2015 /_ # testing with OS    *
##################################################################################################
# OS   * Ubuntu 14.04.1 LTS                          # OS   * Ubuntu 14.04.2 LTS
# Platform   * 32-bit                                # Word size of OS   * 32-bit
# Version   * 0.14.2935 (Git)                        # Word size of FreeCAD   * 32-bit
# Branch   * master                                  # Version   * 0.16.4928 (Git)
# Hash   * eab159b6ee675012bf79de838c206a311e911d85  # Branch   * master
# Python version   * 2.7.6                           # Hash   * d8f63bcfd10301f3d1e141cced4370f0782238d0
# Qt version   * 4.8.6                               # Python version   * 2.7.6
# Coin version   * 4.0.0a                            # Qt version   * 4.8.6
# SoQt version   * 1.6.0a                            # Coin version   * 4.0.0a
# OCC version   * 6.7.0                              # OCC version   * 6.8.0.oce-0.17
##################################################################################################
# OS   * Windows Vista                               # OS   * Windows Vista
# Word size of OS   * 32-bit                         # Word size of OS   * 32-bit
# Word size of FreeCAD   * 32-bit                    # Word size of FreeCAD   * 32-bit
# Version   * 0.15.4527 (Git)                        # Version   * 0.15.4671 (Git)
# Branch   * master                                  # Branch   * releases/FreeCAD-0-15
# Hash   * 0da2e4c45a9a259c26abd54c2a35393e1c15696f  # Hash   * 244b3aef360841646cbfe80a1b225c8b39c8380c
# Python version   * 2.7.8                           # Python version   * 2.7.8
# Qt version   * 4.8.6                               # Qt version   * 4.8.6
# Coin version   * 4.0.0a                            # Coin version   * 4.0.0a
# OCC version   * 6.7.1                              # OCC version   * 6.8.0.oce-0.17
##################################################################################################
```

-   ver 0.7 02/02/2015 suppression 2 str **App.Console.PrintMessage(str(PolicePath)+\"\\n\")** to **App.Console.PrintMessage((PolicePath)+\"\\n\")** that caused an error with the characters above 128 in the police path.
-   ver 0.6 23/11/2014 corrected \"texte = unicode(self.textEdit.toPlainText())\" now accept \"\'éèà@\...\"
-   ver 0.5 19/11/2014 Gui
-   ver 0.4 10/10/2014 add variable \"rotation\" in the loop (**for i in range(0,rotation,(rotation/nombre))   * \# 360 a parametrer**)
-   ver 0.4 27/08/2014 correction error of de radius (exterieur=0, debout=1)
-   ver 0.3 26/08/2014 add creation text of flat curve
-   ver 0.2 26/08/2014 add creation text of internal curve
-   ver 0.1

\(2537\)

### Link

I commenti nella pagina del forum   * [Extrude from curved surface of cylinder](http   *//forum.freecadweb.org/viewtopic.php?f=3&t=7384)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Category_Draft.md) > Macro FCCircularText/it
