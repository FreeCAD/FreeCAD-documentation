# Macro WorkFeatures/it
{{Macro/it
|Name=Macro WorkFeatures
|Icon=WF_wf.png
|Translate=WorkFeatures
|Description=Utility Tool per creare Punti, Assi, Piani e diverse altre funzioni.
|Author=rentlau_64
|Version=2019-05
|Date=2019-05-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/9/9d/WF_wf.png ToolBar Icon]
}}

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Strumenti utili per creare Punti (punti centrali, centri di cerchi, centri di oggetti \...) Assi (da due punti, normale a un piano \...) Piani (da tre punti, da un asse e un punto\...) e molte altre funzioni che facilitano la creazione del progetto. Questi strumenti sono ospitati nella scheda \"Work Features\" della vista combinata.


</div>

<img alt="" src=images/WF.png  style="width:640px;"> 
*WorkFeatures*

## Uses


<div class="mw-translate-fuzzy">

## Uso

**Work Features**


</div>


<center>

Image:Macro WorkFeatures 01.png\|Dopo l\'attivazione di WorkFeatures i suoi strumenti sono visibili nella corrispondente scheda della Vista combinata. Image:Macro WorkFeatures 07.png\|Ogni funzione e ogni voce che corrisponde a un gruppo di funzioni è inserita in un sottogruppo creato con il nome della scheda utilizzata. Gli Assi, i Punti e i Piani in origine sono impostati Nascosti. Image:Macro WorkFeatures 08.png\|Si può entrare nel gruppo e usare i normali comandi per rendere visibili le funzioni create.
Ad es. con il comando ****Spazio**** oppure selezionare l\'oggetto, fare clic destro del mouse e poi fare clic su \"**Nascondi selezione**\" o \"**Mostra selezione**\".


</center>

**Scheda Origin**

+++
| <img alt="" src=images/Macro_WorkFeatures_02.png  style="width:200px;"> | -   **Scheda Origin**                                                                                                               |
|                                                                         |                                                                                                                                     |
|                                                                         | -                                                                                                                    |
|                                                                         |     **Origin**                                                                                                                  |
|                                                                         |                                                                                                                                  |
|                                                                         |     : Crea una origine: un punto con gli assi X,Y,Z e i piani XZ,XY,YZ. Tutti gli elementi sono automaticamente impostati nascosti. |
+++

**Scheda Points**

+++
| <img alt="" src=images/Macro_WorkFeatures_03.png  style="width:200px;"> | -   **Scheda Points**                                                                 |
|                                                                         |                                                                                       |
|                                                                         | -                                                                      |
|                                                                         |     **Object(s) Center**                                                          |
|                                                                         |                                                                                    |
|                                                                         |     : Crea un punto nel centro di tutti gli oggetti selezionati.                      |
|                                                                         |                                                                                       |
|                                                                         | -                                                                      |
|                                                                         |     **Lines(s) Center**                                                           |
|                                                                         |                                                                                    |
|                                                                         |     : Crea un punto nel centro di ciascuna linea selezionata.                         |
|                                                                         |                                                                                       |
|                                                                         | -                                                                      |
|                                                                         |     **Line(s) Extrema**                                                           |
|                                                                         |                                                                                    |
|                                                                         |     : Crea punti all\'inizio e alla fine di ogni linea selezionata.                   |
|                                                                         |                                                                                       |
|                                                                         | -                                                                      |
|                                                                         |     **Circle(s) Center**                                                          |
|                                                                         |                                                                                    |
|                                                                         |     : Crea un punto nel centro di ogni cerchio o arco selezionato.                    |
|                                                                         |                                                                                       |
|                                                                         | -                                                                      |
|                                                                         |     **Point along Line**                                                          |
|                                                                         |                                                                                    |
|                                                                         |     : Crea un punto su una linea ad una certa distanza dal punto estremo selezionato. |
|                                                                         |                                                                                       |
|                                                                         | -   **SpinBox** : immettere il valore di scostamento                                  |
|                                                                         |                                                                                       |
|                                                                         | -                                                                      |
|                                                                         |     **Face(s) Center**                                                            |
|                                                                         |                                                                                    |
|                                                                         |     : Crea un punto nel centro di ogni faccia selezionata.                            |
|                                                                         |                                                                                       |
|                                                                         | -                                                                      |
|                                                                         |     **Point (Line,Face)**                                                         |
|                                                                         |                                                                                    |
|                                                                         |     : Crea un punto nell\'intersezione tra la linea e il piano selezionato.           |
|                                                                         |                                                                                       |
|                                                                         | -                                                                      |
|                                                                         |     **Point (Line,Point)**                                                        |
|                                                                         |                                                                                    |
|                                                                         |     : Crea un punto di proiezione di un punto su una linea e un punto simmetrico.     |
|                                                                         |                                                                                       |
|                                                                         | -                                                                      |
|                                                                         |     **Point (Point,Face)**                                                        |
|                                                                         |                                                                                    |
|                                                                         |     : Crea un punto di proiezione di un punto su una faccia.                          |
|                                                                         |                                                                                       |
|                                                                         | -                                                                      |
|                                                                         |     **Object(s) Base Point**                                                      |
|                                                                         |                                                                                    |
|                                                                         |     : Crea un punto base di tutti gli oggetti selezionati.                            |
+++

**Scheda Axis**

+++
| <img alt="" src=images/Macro_WorkFeatures_04.png  style="width:200px;"> | -   **Scheda Axis**                                                         |
|                                                                         |                                                                             |
|                                                                         | -                                                            |
|                                                                         |     **Object(s) X, Y, Z Axes**                                          |
|                                                                         |                                                                          |
|                                                                         |     : Crea 3 assi nel centro di tutti gli oggetti selezionati.              |
|                                                                         |                                                                             |
|                                                                         | -                                                            |
|                                                                         |     **Two Points Axis**                                                 |
|                                                                         |                                                                          |
|                                                                         |     : Crea un asse passante per due punti                                   |
|                                                                         |                                                                             |
|                                                                         | -   **SpinBox** : immettere il valore di scostamento                        |
|                                                                         |                                                                             |
|                                                                         | -                                                            |
|                                                                         |     **Cylinder(s) Axis**                                                |
|                                                                         |                                                                          |
|                                                                         |     : Crea l\'asse del cilindro.                                            |
|                                                                         |                                                                             |
|                                                                         | -                                                            |
|                                                                         |     **Axis (Line,Line)**                                                |
|                                                                         |                                                                          |
|                                                                         |     : Creare un asse tra due assi.                                          |
|                                                                         |                                                                             |
|                                                                         | -                                                            |
|                                                                         |     **Plane(s) Axes**                                                   |
|                                                                         |                                                                          |
|                                                                         |     : Crea 2 assi perpendicolari nel centro di un piano.                    |
|                                                                         |                                                                             |
|                                                                         | -                                                            |
|                                                                         |     **Axis (Point,Axis)**                                               |
|                                                                         |                                                                          |
|                                                                         |     : Crea un asse parallelo ad un altro asse e passante per un punto.      |
|                                                                         |                                                                             |
|                                                                         | -                                                            |
|                                                                         |     **Axis (Axis,Point)**                                               |
|                                                                         |                                                                          |
|                                                                         |     : Crea un asse perpendicolare ad un altro asse e passante per un punto. |
|                                                                         |                                                                             |
|                                                                         | -   **SpinBox** : immettere il valore di scostamento                        |
|                                                                         |                                                                             |
|                                                                         | -                                                            |
|                                                                         |     **Axis (Plane,Axis)**                                               |
|                                                                         |                                                                          |
|                                                                         |     : Crea un asse su un piano dalla proiezione di un altro asse.           |
|                                                                         |                                                                             |
|                                                                         | -                                                            |
|                                                                         |     **Axis (Plane,Plane)**                                              |
|                                                                         |                                                                          |
|                                                                         |     : Crea un asse dalla intersezione di 2 piani.                           |
|                                                                         |                                                                             |
|                                                                         | -                                                            |
|                                                                         |     **Object(s) Base Axis**                                             |
|                                                                         |                                                                          |
|                                                                         |     : Crea 3 assi nella posizione di base di tutti gli oggetti selezionati. |
+++

**Scheda Plane**

+++
| <img alt="" src=images/Macro_WorkFeatures_05.png  style="width:200px;"> | -   **Scheda Plane**                                                                            |
|                                                                         |                                                                                                 |
|                                                                         | -                                                                                |
|                                                                         |     **Three Points Plane**                                                                  |
|                                                                         |                                                                                              |
|                                                                         |     : Crea un piano passante per 3 Punti.                                                       |
|                                                                         |                                                                                                 |
|                                                                         | -                                                                                |
|                                                                         |     **Plane (Point, Axis)**                                                                 |
|                                                                         |                                                                                              |
|                                                                         |     : Crea un piano passante per una linea e un punto. Il punto non deve appartiene alla linea! |
|                                                                         |                                                                                                 |
|                                                                         | -                                                                                |
|                                                                         |     **Plane (Point, _Axis)**                                                                |
|                                                                         |                                                                                              |
|                                                                         |     : Crea un piano perpendicolare ad una linea e passante per un punto.                        |
|                                                                         |                                                                                                 |
|                                                                         | -                                                                                |
|                                                                         |     **Plane (Point, Plane)**                                                                |
|                                                                         |                                                                                              |
|                                                                         |     : Crea un piano passante per un punto e parallelo ad un piano.                              |
|                                                                         |                                                                                                 |
|                                                                         | -   **SpinBox** : immettere il valore di scostamento                                            |
|                                                                         |                                                                                                 |
|                                                                         | -                                                                                |
|                                                                         |     **Plane (Plane, Axis)**                                                                 |
|                                                                         |                                                                                              |
|                                                                         |     : Crea un piano passante per una linea e perpendicolare ad un piano.                        |
|                                                                         |                                                                                                 |
|                                                                         | -   **SpinBox** : immettere il valore di scostamento                                            |
|                                                                         |                                                                                                 |
|                                                                         | -                                                                                |
|                                                                         |     **Object(s) Center Planes**                                                             |
|                                                                         |                                                                                              |
|                                                                         |     : Crea 3 piani (XY, XZ e YZ) nel centro di tutti gli oggetti selezionati.                   |
+++

**Scheda Objects**

+++
| <img alt="" src=images/Macro_WorkFeatures_06.png  style="width:200px;"> | -   **Scheda Objects**                                                                                                                                                                                                     |
|                                                                         |                                                                                                                                                                                                                            |
|                                                                         | -                                                                                                                                                                                                           |
|                                                                         |     **Bounding Box(es)**                                                                                                                                                                                               |
|                                                                         |                                                                                                                                                                                                                         |
|                                                                         |     : Crea un solido di contenimento intorno a ogni oggetto selezionato.                                                                                                                                                   |
|                                                                         |                                                                                                                                                                                                                            |
|                                                                         | -                                                                                                                                                                                                           |
|                                                                         |     **Bounding Box**                                                                                                                                                                                                   |
|                                                                         |                                                                                                                                                                                                                         |
|                                                                         |     : Crea un solido di contenimento intorno a tutti gli oggetti selezionati.                                                                                                                                              |
|                                                                         |                                                                                                                                                                                                                            |
|                                                                         | -                                                                                                                                                                                                           |
|                                                                         |     **Cylinder**                                                                                                                                                                                                       |
|                                                                         |                                                                                                                                                                                                                         |
|                                                                         |     : Prima selezionare un asse e un punto. Definire diametro e lunghezza, se necessario. Quindi fare clic sul pulsante \... Si crea un cilindro allineato sull\'asse selezionato con una estremità nel punto selezionato. |
|                                                                         |                                                                                                                                                                                                                            |
|                                                                         | -                                                                                                                                                                                                           |
|                                                                         |     **Cube**                                                                                                                                                                                                           |
|                                                                         |                                                                                                                                                                                                                         |
|                                                                         |     : Prima selezionare un asse e un punto. Definire le dimensioni se necessario. Quindi fare clic sul pulsante \... Si crea un cubo allineato sull\'asse selezionato con una estremità nel punto selezionato.             |
+++

**Scheda Views**

+++
| <img alt="" src=images/Macro_WorkFeatures_09.png  style="width:200px;"> | -   **Scheda Views**                                                                                                                                                                                    |
|                                                                         |                                                                                                                                                                                                         |
|                                                                         | -                                                                                                                                                                                        |
|                                                                         |     **Align to ...**                                                                                                                                                                                |
|                                                                         |                                                                                                                                                                                                      |
|                                                                         |     : Imposta la vista corrente perpendicolare alla faccia selezionata, o allineata lungo l\'asse selezionato, o allineata lungo 2 punti. Ricliccando sulla stessa selezione si invertire la direzione. |
+++

**Scheda Modif.**

+++
| <img alt="" src=images/Macro_WorkFeatures_10.png  style="width:200px;"> | -   **Scheda Modif. Cutting**                                                                    |
|                                                                         |                                                                                                  |
|                                                                         | -                                                                                 |
|                                                                         |     **Select Object**                                                                        |
|                                                                         |                                                                                               |
|                                                                         |     : Prima, selezionare l\'oggetto da tagliare poi fare clic sul pulsante \'Select Object\',    |
|                                                                         |                                                                                                  |
|                                                                         |     -   Viene visualizzato il nome dell\'oggetto selezionato                                     |
|                                                                         |                                                                                                  |
|                                                                         | -                                                                                 |
|                                                                         |     **Select Cut Line**                                                                      |
|                                                                         |                                                                                               |
|                                                                         |     : Secondo, selezionare una linea di taglio, cliccare sul pulsante \'Select Cut Line\',       |
|                                                                         |                                                                                                  |
|                                                                         |     -   Viene visualizzato il nome della linea selezionata                                       |
|                                                                         |                                                                                                  |
|                                                                         | -                                                                                 |
|                                                                         |     **Select Ref. Plane**                                                                    |
|                                                                         |                                                                                               |
|                                                                         |     : Ultimo, selezionare un piano di riferimento e cliccare sul pulsante \'Select Ref. Plane\'! |
|                                                                         |                                                                                                  |
|                                                                         |     -   Viene visualizzato il nome del piano selezionato                                         |
|                                                                         |                                                                                                  |
|                                                                         | -   **Angle** : Angolo di taglio (Defaut : 0.0)                                                  |
|                                                                         |                                                                                                  |
|                                                                         | -   **Thichness** : Spessore di taglio (Defaut : 0.0)                                            |
|                                                                         |                                                                                                  |
|                                                                         | -                                                                                 |
|                                                                         |     **Reset**                                                                                |
|                                                                         |                                                                                               |
|                                                                         |     : Ripristina i valori                                                                        |
|                                                                         |                                                                                                  |
|                                                                         | -                                                                                 |
|                                                                         |     **Apply**                                                                                |
|                                                                         |                                                                                               |
|                                                                         |     : Applica i valori                                                                           |
+++

**Check. Tab**

+++
| <img alt="" src=images/Macro_WorkFeatures_11.png  style="width:200px;"> | -   **Check. Tab**                                                                                                                                   |
|                                                                         |                                                                                                                                                      |
|                                                                         | -                                                                                                                                     |
|                                                                         |     **are Parallel ?**                                                                                                                           |
|                                                                         |                                                                                                                                                   |
|                                                                         |     : Controlla se due facce o due bordi sono paralleli                                                                                              |
|                                                                         |                                                                                                                                                      |
|                                                                         |     -   Selezionare 2 facce/piani o 2 bordi/linee, poi cliccare questo pulsante                                                                      |
|                                                                         |                                                                                                                                                      |
|                                                                         | -                                                                                                                                     |
|                                                                         |     **are Perpendicular ?**                                                                                                                      |
|                                                                         |                                                                                                                                                   |
|                                                                         |     : Controlla se due facce o due bordi sono perpendicolari                                                                                         |
|                                                                         |                                                                                                                                                      |
|                                                                         |     -   Selezionare 2 facce/piani o 2 bordi/linee, poi cliccare questo pulsante                                                                      |
|                                                                         |                                                                                                                                                      |
|                                                                         | -                                                                                                                                     |
|                                                                         |     **are Coplanar ?**                                                                                                                           |
|                                                                         |                                                                                                                                                   |
|                                                                         |     : Controlla se due facce o due bordi sono complanari                                                                                             |
|                                                                         |                                                                                                                                                      |
|                                                                         |     -   Selezionare 2 facce/piani o 2 bordi/linee, poi cliccare questo pulsante                                                                      |
|                                                                         |                                                                                                                                                      |
|                                                                         | -                                                                                                                                     |
|                                                                         |     **Distance Clearance ?**                                                                                                                     |
|                                                                         |                                                                                                                                                   |
|                                                                         |     : Controlla la distanza di sicurezza tra due oggetti                                                                                             |
|                                                                         |                                                                                                                                                      |
|                                                                         |     -   Misura rapidamente la distanza tra le facce parallele e oggetti posizionati in modo simile. Selezionare i 2 oggetti e fare clic sul pulsante |
|                                                                         |                                                                                                                                                      |
|                                                                         | -                                                                                                                                     |
|                                                                         |     **Angle ?**                                                                                                                                  |
|                                                                         |                                                                                                                                                   |
|                                                                         |     : Calcola l\'angolo tra 2 oggetti, due bordi, due piani o tra un bordo e un piano                                                                |
|                                                                         |                                                                                                                                                      |
|                                                                         |     -   Selezionare 2 elementi poi cliccare sul pulsante                                                                                             |
|                                                                         |                                                                                                                                                      |
|                                                                         | -                                                                                                                                     |
|                                                                         |     **Distance ?**                                                                                                                               |
|                                                                         |                                                                                                                                                   |
|                                                                         |     : Controlla la distanza e i valori delta (sugli assi principali) tra due punti                                                                   |
|                                                                         |                                                                                                                                                      |
|                                                                         |     -   Selezionare 2 punti poi cliccare sul pulsante                                                                                                |
|                                                                         |                                                                                                                                                      |
|                                                                         | -                                                                                                                                     |
|                                                                         |     **Length ?**                                                                                                                                 |
|                                                                         |                                                                                                                                                   |
|                                                                         |     : Misura la lunghezza e i valori delta (sugli assi principali) di una linea                                                                      |
|                                                                         |                                                                                                                                                      |
|                                                                         |     -   Selezionare una linea poi cliccare sul pulsante                                                                                              |
|                                                                         |                                                                                                                                                      |
|                                                                         | -                                                                                                                                     |
|                                                                         |     **Area ?**                                                                                                                                   |
|                                                                         |                                                                                                                                                   |
|                                                                         |     : Misura l\'area di una superficie, o di un gruppo di superfici                                                                                  |
|                                                                         |                                                                                                                                                      |
|                                                                         |     -   Selezionare uno o più piani poi cliccare sul pulsante                                                                                        |
|                                                                         |                                                                                                                                                      |
|                                                                         | -                                                                                                                                     |
|                                                                         |     **View**                                                                                                                                     |
|                                                                         |                                                                                                                                                   |
|                                                                         |     : Rileva la posizione della fotocamera. Il valore restituito è il valore fornito dalla funzione getCameraOrientation().                          |
+++

## Script


<div class="mw-translate-fuzzy">

## Script 

Dopo aver scaricato il file compresso


</div>

Icona barra strumenti ![](images/WF_wf.png )

**[Download the latest version on GitHub](https://github.com/Rentlau/WorkFeature)** , è necessario decomprimerlo e copiare tutti i file nella directory delle macro di FreeCAD.


<div class="mw-translate-fuzzy">

**Nota:Questa macro è ancora in fase di sviluppo si prega di visitare questa pagina per essere sicuri di avere l\'ultima versione.**


</div>

<img alt="Download in GitHub click the Download ZIP button" src=images/Macro_Work_Features_GitHub_00.png  style="width:640px;"> 


<div class="mw-translate-fuzzy">

Per installare facilmente la macro WorkFeatures e altre interessanti macro vedere: [addons_installer](https://github.com/FreeCAD/FreeCAD-addons/blob/master/addons_installer.FCMacro)


</div>


<div class="mw-translate-fuzzy">

Per informazioni dettagliate vedere la pagina [Come installare le Macro](How_to_install_macros/it.md)


</div>

## Esempi

### Strumenti di taglio 

**Impostazione dello strumento Taglio:** Selezionare un oggetto da tagliare, una linea di taglio e un piano di riferimento. Angle è un angolo tra il piano di taglio e il piano di riferimento. Spessore è la larghezza del piano di taglio.


<center>

Image:CuttingSettings.jpg\|Qui è selezionato un cilindro. Image:CuttingResult.jpg\|Il risultato: il cilindro tagliato in due parti!


</center>





<center>

**Esempio pratico**

Image:Macro Work Features Cutting 01.png\|Selezionare la **Scheda **Plane**** Image:Macro Work Features Cutting 02.png\|e cliccare il pulsante **Plane**
(è possibile modificare le dimensioni del piano (**Default: 10 x 10**)).


</center>





<center>

Image:Macro Work Features Cutting 03.png\|scegliere l\'oggetto da lavorare. Il piano viene creato tangente all\'oggetto (qui un cilindro) Image:Macro Work Features Cutting 04.png\|cliccare la scheda **Modif**, e
**1 :** cliccare l\'oggetto da tagliare
**2 :** cliccare il pulsante **Select object** (qui il cilindro e quindi ne viene visualizzato il nome)


</center>





<center>

Image:Macro Work Features Cutting 05.png\|**3 :** fare clic sulla linea di taglio
**4 :** cliccare su **Select Cut Line** (quindi ne viene visualizzato il nome) Image:Macro Work Features Cutting 06.png\|**5 :** cliccare il piano di lavoro
**6 :** cliccare su **Select Ref. Plane** (quindi ne viene visualizzato il nome)


</center>





<center>

Image:Macro Work Features Cutting 07.png\| cliccare su **Apply** Image:Macro Work Features Cutting 08.png\| L\'operazione è completata e tutte le operazioni sono salvaguardate.


</center>





<center>

Image:Macro Work Features Cutting 09.png\| per il vostro taglio si può anche assegnare un Angolo e uno Spessore.


</center>




### Vincolo concentrico tra due parti non cilindriche 


<div class="mw-translate-fuzzy">


<center>

Image:Concentric Constraint Between two non cylindrical parts.gif\|Come vincolare concentriche due parti non cilindriche.
**1 :** L\'oggetto originale da modificare.
**2 :** Obiettivo centrare due tubi quadrati.
**3 :** Selezionare il primo oggetto e nel menu **Axis 1/2** cliccare \"Object(s)\" X, Y, Z Axes.
**4 :** Stessa procedura per il secondo oggetto.
**5 :** Cliccare sul pulsante **Draw style** a e su \"Wireframe\",
**6 :** per migliorare la vista.
**7 :** Selezionare il centro dell\'oggetto e dei sui assi.
**8 :** Cliccare sul pulsante **Draft Move**
**9 :** e selezionare il primo asse da spostare sul secondo asse.
**10 :** Ripristinare la visualizzazione normale con i tasti **Draw style** e **As is**.
**11 :** Fare clic sul primo oggetto spostato e correggere la posizione con \"Combo view \> Data \> Placement\".
**12 :** Selezionare l\'oggetto creato da WorkFeature (contener axis) ed eliminarlo.
**13 :** L\'oggetto ripulito.
**14 :** Il risultato.


</center>





</div>


</center>




### Rotazione oggetti 


<center>

Image:WorkFeature_Rotation_Object.gif\|Click the image for see the animation.


</center>





<center>

Image:Macro_Work_Features_PlaneFaceTangent.gif\|Click the image for see the animation.
Click the object, click the **Face tangent** button, click the point on face for create the plane.


</center>




## Link

La discussione nel forum [MACRO:Work Feature 2014_12](http://forum.freecadweb.org/viewtopic.php?f=22&t=9056)

## Ambienti aggiuntivi 

Gli ambienti di FreeCAD sono facili da programmare in [Python](Python/it.md), quindi ci sono molte persone che sviluppano ambienti aggiuntivi al di fuori degli sviluppatori principali di FreeCAD.


<div class="mw-translate-fuzzy">

La pagina [Ambienti complementari](external_workbenches/it.md) contiene alcune informazioni e tutorial su alcuni di loro, e il progetto [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) mira a raccoglierli e renderli facilmente installabili dall\'interno di FreeCAD.


</div>

Sono in fase di sviluppo ulteriori nuovi ambienti.

## Ultima versione 

**Icone:**

![](images/WF_wf.png )

![](images/WF_centerObjectsPlanes.png )

**Sorgenti:**

Su github : [/github.com/Rentlau/WorkFeature-WB.git](https://github.com/Rentlau/WorkFeature-WB.git)

Data 2019-05-01 (YYYY-MM-DD)

20/01/2019

08/03/2015: [WF_2015_03_08](http://github.com/Rentlau/WorkFeature.git) - Circle cut added - Are Parallel, Are Perpendicular, Are Coplanar added

17/02/2015 : [WF_2015_02_17](https://github.com/Rentlau/WorkFeature.git) - Circle and Ellipse Tab added - Cutting tab added

25/01/2015 : [WF_2015_01_25.zip](http://forum.freecadweb.org/download/file.php?id=10937&sid=b770dec5362ae499adb4173547ef445f) add Object Cylinder Cube

18/01/2015 : [WF_2015_01_18.tar.gz](http://forum.freecadweb.org/download/file.php?id=10799) add plane and face to view

28/12/2014 : [WorkFeatures_2014_12_28.zip](http://forum.freecadweb.org/download/file.php?id=10347)

27/12/2014 : [WF_2014_12_27.zip](http://forum.freecadweb.org/download/file.php?id=10325)



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [User Documentation](Category_User Documentation.md) > Macro WorkFeatures/it
