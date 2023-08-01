# Macro FCSpring Helix Variable/it
{{Macro/it
|Name=Macro FCSpring Helix Variable
|Translate=Molla a spirale variabile
|Icon=FCSpring Helix Variable.png
|Description=Questa macro crea una molla personalizzabile, la configurazione della molla può essere salvata in un file con estensione '''.FCSpring''' o coordinate '''.FCSpringCoor'''.<br/>Vengono rilevati: Superficie (Direzione della faccia), Cilindro (raggio), Ellisse (raggio minore), Sfera (raggio), Toroide (raggio1), Piano (direzione), Linea (seguire la direzione), Punto (posizione vertice XYZ) <br / > Se non viene rilevato alcun oggetto (non selezione) la molla viene creata nel punto XYZ 0., 0., 0. <br / >Vedi [https://www.freecadweb.org/wiki/Macro_FCSpring_Helix_Variable/it#Esempi esempi]
|Author=Mario52
|Version=01.18
|Date=2022/03/16
|Download=Download the [https://forum.freecadweb.org/download/file.php?id=80844 the Icons] in .zip file 
|FCVersion=0.19
}}

## Descrizione

Questa macro crea una molla con una configurazione altamente personalizzabile. Qualsiasi modifica che cambi la configurazione della molla può essere salvata in un file con estensione .FCSpring o coordinate .FCSpringCoor
Vengono rilevati: superficie (direzione faccia), cilindro (raggio), ellisse (raggio minore), sfera (raggio), toroide (raggio1), piano (direzione), linea (seguire la direzione), punto (posizione vertice XYZ)
Se non viene rilevato alcun oggetto (non selezione) la molla viene creata nel punto XYZ 0., 0., 0.
Si possono creare diverse configurazioni di molle, secondo le proprie esigenze, e poi salvarle in un file con estensione **.FCSpring**


{{Codeextralink|https://gist.githubusercontent.com/mario52a/68c81c32a0727a693d3a/raw/8b0b60336a62f22c0730e6fb88687ffd1b1dd502/Macro_FCSpring_Helix_Variable.FCMacro}}

<img alt="" src=images/TruncateSpring00.png  style="width:400px;"> 
*FCSpring Helix Variable*

## Uso

Configurazione della molla

Schema di configurazione della molla

![](images/Macro_TruncateSpring_01.png ) 

#### **Gui**

![](images/Macro_FCSpring_Helix_Variable_01.png ) 

#### Configurazione

-    {{SpinBox|10 coils}}**Number of coil** : Numero di spire. Default = 10

-    {{SpinBox|20,000 mm}}**Radius of spring** : Raggio della molla. Default = 20.0

-    {{SpinBox|15,000 mm}}**Pitch of spring** : Passo principale. Default = 15.0

-    {{SpinBox|5 ( 72 points )}}**Precision of turn** : Precisione della curvatura, la precisione corrisponde al numero di punti per spira ed è calcolata \* {{SpinBox|5 ( 72 points )}} : precision (numero di punti) = (passo / (360/precisione)). Default = 5 (72 punti)

-    {{SpinBox|20,000 mm}}**Spring conical** : Diametro maggiore del cono, questa dimensione deve essere maggiore o uguale al raggio

-    {{CheckBox|Spring conical}}: Dai al diametro grande del cono che la dimensione sarà sempre maggiore del raggio

-    {{CheckBox|Angles}}: Casella di scelta per attivare la funzione angolo iniziale e angolo finale della molla, deselezionata per impostazione predefinita.
    Se questa funzione è selezionata, la precisione viene impostata automaticamente a 1 (360 punti per spira, 1 punto = 1 grado)

-    {{SpinBox|0 deg}}**Begin** : Angolo iniziale della prima spira della molla.

-    {{SpinBox|360 deg}}**End** : Angolo finale dell\'ultima spira della molla.

![](images/Macro_FCSpring_Helix_Variable_02.png ) 

#### Tipo di linea 

-    {{RadioButton|TRUE|<img src="images/Draft_BSpline.svg" width=24px> Bspline}}**BSpline** : Linea di tipo BSpline.

-    {{RadioButton|<img src="images/Draft_Wire.svg" width=24px> Wire}}**Wire** : Linea di tipo Wire.

-    {{CheckBox|<img src="images/Draft_Point.svg" width=24px> Points}}**Points** : Casella di controllo dei punti, se è attivata viene creato un punto in ogni punto.

-    {{CheckBox|Reverse}}**Reverse** : Casella di controllo per invertire la direzione della molla

![](images/Macro_FCSpring_Helix_Variable_03.png ) 

#### Opzione

Questa sezione viene visualizzata se è selezionato l\'oggetto. Il tipo di oggetto viene visualizzato in Text Editor

L\'oggetto può essere una linea, 2 punti, un cerchio, un contorno \... un asse, la lunghezza della molla viene creata automaticamente

Detection : Cylinder (radius), Sphere (radius), Toroid (radius) , Cone (little radius), Circle (radius), Arc (radius), Ellipse (little radius)

-    **Normal.**: Se uno circo e seletto **Norm** il raggio non e modificato (Difetto)

    -   
        **Adapt Rad.**
        
        : Se il pulsante **Normal** e attivato, il raggio della molla e datato al raggio della selezione se uno raggio e detetto

-    **Point Mouse**: Se date uno clic mouse sopra una faccia l\'asso della molla sarà il punto di coordinate della molla

    -   
        **Center Face**
        
        : Si il pulsante **Point Mouse** è attivato, il pulsante cambia a **Center Face** è la molla sarà creata in centro della facia

-    {{CheckBox|Position}}**Position** : Se due obbietti sonno selezionate (primo asso secondo molla) potete modificare il posizionamento della molla allungo l\'asso creato

-    **Circle**: Se tre punti sonno selezionati potete creare un cerchio che servirà di punto di partenza della molla

![](images/Macro_FCSpring_Helix_Variable_02_1.png ) 

#### Position (0)(xx) 

(0)(xx) : Number selection(s), length in mm of axis created x 10, Dati e numeri punti per la posizione della molla sopra l\'asso

-    **Begin/End**: Posizione della base della molla su l\'asso, inizia, meta, fine del asso

-    **Reverse Spr.**: Riversa la molla sopra l\'asso

-    {{SpinBox|0,1 mm}}: posizione della molla con una precinzione di spostamento di (0.1 mm) a longo l\'asso

-    **Reverse Count.**: Riversa il contatore ex: Begin 0 to 10.. or End 0 to 10..

-   **Slider** : Posizione rapida della molla a longo l\'asso

![](images/Macro_FCSpring_Helix_Variable_02_2.png ) 

#### Spire di lunghezza speciale 

-    {{SpinBox|Num: 2}}**Numbering of coil** : Numero di spire da modificare. (Defaut : nessuna)

-    {{CheckBox|Smoothing}}**Smoothing** Questa casella apre una casella numerica per determinare il grado di lisciatura. Il valore massimo è il valore di precisione -1 (questa opzione è ancora allo stadio di prototipo e il risultato può essere soddisfacente o completamente sbagliato)

-    {{SpinBox|0,000 mm}}**Pitch of coil** : Passo delle spire da modificare. (Defaut : nessuna)

-    **15.0 mm**: Se viene premuto questo pulsante il valore di \"Pitch of string\" influenza \"Pitch of coil\" (Questo valore viene allineato automaticamente al valore di Pitch of string)

-    {{SpinBox|0,000 mm}}**Radius of coil** : Raggio della spira da modificare. (Defaut : nessuno)

-    **20.0 mm**: Se viene premuto questo pulsante il valore di \"Radius of string\" influenza \"Radius of coil\" (Questo valore viene allineato automaticamente al valore di Radius of string)

-    **<img src="images/FCSpring_Helix_Variable_Icon_01.png" width=16px> Accept the value modified**: Pulsante da premere per confermare le modifiche definite prima.

-   **Text edit** : Questa finestra mostra tutte le spire modificate.

-    **Clear**: Ripulisce l\'editor

-    **Zoom**: Pulsante \"Zoom\" ingrandisce la finestra di modifica del testo

![](images/Macro_FCSpring_Helix_Variable_04.png ) 

## Comandi

-    **<img src="images/FCSpring_Helix_Variable_Icon_02.png" width=16px> Load**: Apre una finestra di dialogo per leggere un file **.FCSpring**.

-    **<img src="images/FCSpring_Helix_Variable_Icon_03.png" width=16px> Save**: Apre una finestra di dialogo per salvare un file **.FCSpring** .

-    **<img src="images/FCSpring_Helix_Variable_Icon_02b.png" width=16px> Load Coordinates**: Apre una finestra di dialogo per leggere un file **.FCSpringCoor** (tutte le coordinate dei punti di una molla).

-    **<img src="images/FCSpring_Helix_Variable_Icon_03b.png" width=16px> Save Coordinates**: Apre una finestra di dialogo per salvare un file **.FCSpringCoor** (tutte le coordinate dei punti di una molla).

-    **<img src="images/FCSpring_Helix_Variable_Icon_04.png" width=16px> Quit**: Esce dalla macro.

-    **<img src="images/FCSpring_Helix_Variable_Icon_05.png" width=16px> Reset**: Ripristina la configurazione iniziale della macro.

-    **<img src="images/FCSpring_Helix_Variable_Icon_06.png" width=16px> Launch**: Avvia la macro per creare una molla configurata.

-    **Help**: Questo pulsante visualizza la pagina wiki nel browser FreeCAD.

![](images/Macro_FCSpring_Helix_Variable_05.png ) 

## Registro degli eventi 

La finestra Report visualizzata tutti i valori modificati.

![](images/Macro_FCSpring_Helix_Variable_06.png ) 

## Esempio di molla 

Esempio di molla modificata

![](images/Macro_FCSpring_Helix_Variable_07.png ) 

## Esempio di rapporto nel Registro degli eventi 

All\'avvio della macro viene visualizzato l\'elenco completo dei giri sotto forma di tabella.

Questi sono i dati della molla precedente visualizzati nella finestra Report ![](images/Macro_FCSpring_Helix_Variable_08.png ) 

## Icone

Scaricare le immagini e copiarle nel repertorio delle macro.

Cliccare sull\'immagine con il tasto destro del mouse e salvarla nella nuova posizione selezionando \"Salva oggetto con nome \...\"

Pulsanti della barra degli strumenti ![Button](images/FCSpring_Helix_Variable.png )  Icone della macro

![](images/FCSpring_Helix_Variable_Icon_01.png ) ![](images/FCSpring_Helix_Variable_Icon_02.png ) ![](images/FCSpring_Helix_Variable_Icon_02b.png ) ![](images/FCSpring_Helix_Variable_Icon_03.png ) ![](images/FCSpring_Helix_Variable_Icon_03b.png ) ![](images/FCSpring_Helix_Variable_Icon_04.png ) ![](images/FCSpring_Helix_Variable_Icon_05.png ) ![](images/FCSpring_Helix_Variable_Icon_06.png ) 

## Script

**Macro_FCSpring_Helix_Variable.FCMacro**

Download the macro to Gist [Macro_FCSpring_Helix_Variable](https://gist.github.com/mario52a/68c81c32a0727a693d3a)

## Installazione

Il file sopra è una macro sotto forma di codice GitHub. Scaricare il file Zip da GitHub, quindi seguire le istruzioni di installazione delle macro mostrate in [installing FreeCAD macros in Ubuntu](https://wiki.opensourceecology.org/wiki/Installing_Macros_in_FreeCAD).

## Esempi


<center>

<File:Valves> Assembly IN EX.png\| Valves Assembly IN EX with permit and created by r.tec see [Inlet & Exhaust Valves Assembly](http://forum.freecadweb.org/viewtopic.php?f=24&t=14183) and [Spiralfeder](http://forum.freecadweb.org/viewtopic.php?f=13&t=14143) thanks r.tec


</center>



<center>

<File:Macro> FCSpring Helix Variable 12.png\| <File:Macro> FCSpring Helix Variable 13.png\|


</center>



<center>

<File:Macro> FCSpring Helix Variable 14.png\| <File:Macro> FCSpring Helix Variable 15.png\|


</center>



<center>

<File:Macro> FCSpring Helix Variable 16.png\| <File:Macro> FCSpring Helix Variable 17.png\|


</center>



<center>

<File:Macro> FCSpring Helix Variable 18.png\|


</center>



<center>

<File:Macro> FCSpring Helix Variable 19.png\|Difference between Smooth (here 71 with precision 5 (72 points)) and normal


</center>



<center>

<File:Macro> FCSpring Helix Variable.gif\|Example


</center>



<center>

<File:Macro> FCSpringHelixVariable Example 02.gif\|Example create conical spring


</center>



<center>

<File:Macro_FCSpringHelixVariable_Spring_On_Circle.gif%7CEsempio> creare la molla sul cerchio <File:Macro_FCSpringHelixVarable_Spring_Along_Axis.gif%7CMuovimenti> lungo l\'asse


</center>


## Link

La discussione nel forum: [Try to do a Spring](http://forum.freecadweb.org/viewtopic.php?f=3&t=8313&p=68161#p68161)

## In progetto 

molla troncata

ammorbidire i raccordi: fatto

modificare il diametro di qualsiasi spira: fatto

## Versione

2022/03/16 Version 0.18 : adding scrollBar, possibility docking Left or Right, restore the chrono *(time.time())*, memorise the last FilePath


```python
####chrono################
import time
global depart ; depart  = 0.0
global arrivee; arrivee = 0.0
def chrono(switch):    # 0=depart autre=stop
#time.strftime('%X %x %Z')#'15:44:07 12/14/19 Paris, Madrid'
    global depart
    global arrivee
    try:
        if switch == 0:
            depart = time.time()#time.clock()
            App.Console.PrintMessage("Chrono begin   : "+str(time.strftime('%X'))+"\n")
        else:
            arrivee = time.time()#time.clock()
            App.Console.PrintMessage("Chrono end     : "+str(time.strftime('%X'))+"\n")
            parcouru = ((arrivee - depart)/60.0)
            App.Console.PrintError("Time execution : "+str("%.3f" % parcouru)+" min"+"\n\n")
        return parcouru
        FreeCADGui.updateGui()    
    except Exception: None
####chrono################
```

2020/11/12 Version=01.17 : suppress the timer chrono !!

2020/10/18 Ver 00.16b : i suppress the test on FC 18 line 56, i suppress the timer chrono and i wait one little

2020/05/01 Ver 00.16: correction error file (save and load) cause \"label_11_Name\" suppressed\...

2020/04/11 Ver 01.15: layout and little presentation

2019/05/03 Ver 01.14: compatibile FreeCAD 0.19.16523 (Git)

2019/04/08 Ver 01.13: compatible FreeCAD 0.18.16093 (Git) /Python version: 3.6.6 /Qt version: 5.6.2

03/04/2017: ver 01.12: correction bug line 2314 add \"global ui\"

11/12/2016: ver 01.11: Aggiunto Posizione della molla sopra l\'oggetto selezionato

10/09/2016: ver 01.10: Adding Button \"Zoom\" enlarge the textedit window

04/09/2016: ver 01.09: add smoothing

16/03/2016: ver 01.08 : correct and add \"int()\" to debutAngle and finAngle (read file)

02/03/2016: ver 01.07 : add option reverse spring

08/02/2016: ver 01.06 : correct bug angle cause \"modifyAngle = int(file.readline().rstrip(\'\\n\\r\')) \# 9\" modifyAngle is int() not char

07/01/2015: ver 01.05 : adding \"Try \...Except\" (data cone) for compatibility with old version

07/01/2015: ver 01.04 : adding spring conical and modify the path to \"UserAppData\" and adding the icone.

07/12/2014: ver 01.03 : new version with radius coil adjustable

17/11/2014 ver 1.02 : nuova versione con interfaccia grafica e con la possibilità di modificare qualsiasi spira e salvare o caricare i dati su disco.

10/11/2014: (23h20) correction of the modification 
```python
ligne.Placement = App.Placement(App.Vector(0.0,0.0,0.0), App.Rotation(App.Vector(0,0,1),angleTr), App.Vector(0,0,0))
``` 10/11/2014: modify line 44 : 
```python
        a = FreeCAD.ActiveDocument.Line.Placement=App.Placement(App.Vector(0.0,0.0,0.0), App.Rotation(App.Vector(0,0,1),angleTr), App.Vector(0,0,0))
``` con 
```python
        ligne = FreeCAD.ActiveDocument.Line.Placement=App.Placement(App.Vector(0.0,0.0,0.0), App.Rotation(App.Vector(0,0,1),angleTr), App.Vector(0,0,0))
``` 6/11/2014 : aggiunto \"makeBSpline\" e configurazione

## Limitationi

Durante i test di sweep ho ottenuto questi errori!


<center>

<File:Macro> FCSpring Helix Variable 20.png\|For the moment the macro is not adapted for the square, rectangle\...
Only circle work well


</center>



<center>

<File:Macro> FCSpring Helix Variable 09.png\|ACCESS VIOLATION <File:Macro> FCSpring Helix Variable 10.png\|TCollection_IndexedDataMap


</center>



<center>

<File:Macro> FCSpring Helix Variable 11.png\|Wrong usage of punctual sections


</center>



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro FCSpring Helix Variable/it
