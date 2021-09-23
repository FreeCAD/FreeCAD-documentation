# Macro CloneConvert/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Macro CloneConvert
|Icon=Macro_CloneConvert.png
|Description={{ColoredText|#ff0000|#ffffff|New version GUI modifyed for the HD dpi (QGridLayout) run only FC version 0.18 and more (PySide2 Qt5)}}<br/><br/> 
For the precedent version see [https://gist.githubusercontent.com/mario52a/9f2f2f6144e1307a048f1840ef99300c/raw/0a141260ad8d5f67f0fc18b9b40ef37757c06c65/Macro_CloneConvert.FCMacro Macro_CloneConvert] and install it manually.<br/><br/> Creates a clone or Copy or Compound of the object(s) and the converted in the chosen position and size (inch, mm, m, µm...) or free. The base object is recognized in mm (FreeCAd base).
|Author=mario52
|Version=0.15
|Date=2020-06-06
|FCVersion= 0.18 è piu
|Download=[https://www.freecadweb.org/wiki/images/0/0a/Macro_CloneConvert.png ToolBar Icon]
}}


</div>


<div class="mw-translate-fuzzy">

## Descrizione

Crea un clone o una copia dell\'oggetto, lo colloca nella posizione indicata e con le dimensioni desiderate (cm, mm, m, um \...) a piacere. L\'originale, cioè l\'oggetto selezionato, è riconosciuto in mm (secondo il sistema base di FreeCAD)


</div>


{{Codeextralink|https://gist.githubusercontent.com/mario52a/9f2f2f6144e1307a048f1840ef99300c/raw/39bc54e90b80053a5af76b0b17694cb53697aebd/Macro_CloneConvert.FCMacro}}


<div class="mw-translate-fuzzy">

## Utilizzo

Avviare la macro, definire le impostazioni XYZ se è necessario, scegliere \"Clone\" oppure \"Copia\", scegliere una unità di conversione, selezionare l\'oggetto e poi fare clic su il pulsante {{KEY/it|OK}} per avviare l\'operazione.


</div>


<div class="mw-translate-fuzzy">

Se non viene inserito alcun valore viene creata una copia o un clone senza modifiche. Se non è selezionato alcun oggetto il pulsante **Ok** è colorato in rosso.


</div>


<div class="mw-translate-fuzzy">

Il valore di **BoundingBox**, **Volume** e **Surface** sono indicate nella vista Report, nel caso di oggetti **Copy** multiple, il display visualizza BoundingBox 0.0.


</div>


<div class="mw-translate-fuzzy">

L\'unità di base e il mm. L\'originale viene quindi considerato come un oggetto in cui l\'unità di misura è il mm.

Esempio di conversione di uno cubo avente il lato di **1 mm** in un cubo avente lato **25,4 mm**:


</div>

Selezionare nel comboBox l\'unità **inch**, **1 inch = 25.4 mm** , notare che il valore nei campi **\"Scale free\"** si adeguano automaticamente a 25.4 che corrisponde appunto a 1 pollice (per impostare scalature differenti secondo gli assi, i valori ​​in **\"Scale-free\"** possono essere modificati individualmente). Cliccare sul pulsante **OK**. Il cubo clone creato in questo modo ha le dimensioni di **25,4 mm**

Operazione inversa :

Per convertire un oggetto, ad esempio un cubo di 25,4 mm (1 inch) in un cubo di 1mm x 1mm x 1mm, utilizzare la formula **1 / 25,4 = 0,0393700** e inserire il valore **0,0393700** (con la virgola) nel campo Scale X, Y e Z.

Per un cubo di 5mm, fare **5 / 25,4 = 0,1968503**e inserire il valore **0,1968503** (con la virgola) nel campo Scale X, Y e Z.

**150%** = **1,50** nel campo **\"Scale free\"**
**104%** = **1,04** nel campo **\"Scale free\"**

Operazione inversa:

Per convertire un oggetto, ad esempio un cubo di 25,4 mm (1 inch) in un cubo di 1mm x 1mm x 1mm, utilizzare la formula **1 / 25,4 = 0,0393700** e inserire il valore **0,0393700** (con la virgola) nel campo Scale X, Y e Z.

Per un cubo di 5mm, fare **5 / 25,4 = 0,1968503**e inserire il valore **0,1968503** (con la virgola) nel campo Scale X, Y e Z.

**50%** = **0,50** nel campo **\"Scale free\"**
*\' 4%*\' = **0,04** nel campo **\"Scale free\"**


<div class="mw-translate-fuzzy">

Le unita predefinite sono: km, hm, dam, m, dm, cm, **mm**, µm, nm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.


</div>

<img alt="CloneConvert" src=images/Macro_CloneConvert_01.png  style="width:350px;">

-   **Mode**
-   **Clone :** Crea un clone
-   **Copy :** Crea una copia
-   **Comp :** Crea un composto di oggetto
-   **Increm. :** incrementa i dati delle coordinate alle coordinate originali dell\'oggetto (Placement, Rotation \...)
    Se questo non viene attivato il posizionamento inizia alle coordinate 0,0,0 di FreeCAD
    Nel caso in cui un composto le coordinate di Placement sono \[0,0,0\], e il posizionamento inizia nella posizione dell\'oggetto
    Se il posizionamento non inizia nella posizione 0,0,0, utilizzare il pulsante **ValueAt()** per ottenere il posizionamento reale dei subObject selezionati Face, Wire, Line \....
-   **Unique :** Se viene selezionata questa casella con diversi oggetti selezionati, il clone viene creato come un oggetto unico

-   **Coordinate**
-   ****...** :** Questo pulsante forza il valore di Y e Z ai valori di X per avere gli stessi valori ​​XYZ (o manualmente). Due click ripristinano i valori delle coordinate a 0.0
-   **Coordinate X :** Sposta la copia alla coordinata X selezionata (Base 0,0,0 se Increm. non è attivo)
-   **Coordinate Y :** Sposta la copia alla coordinata Y selezionata (Base 0,0,0 se Increm. non è attivo)
-   **Coordinate Z :** Sposta la copia alla coordinata Z selezionata (Base 0,0,0 se Increm. non è attivo)

-   **Rotation**
-   ****...** :** Questo pulsante forza i valori di beccheggio e rollio sul valore di imbardata per avere lo stesso valore di Rotazione (o manualmente). Due click ripristinano i valori delle rotazioni a 0.0
-   **Yaw (Z ) :** Ruota la copia sull\'asse Z (Yaw) (Inizia da 0 se Increm. non è attivo)
-   **Pitch ( Y ) :** Ruota la copia sull\'asse Y (Pitch) (Inizia da 0 se Increm. non è attivo)
-   **Roll ( X ) :** Ruota la copia sull\'asse X (Roll) (Inizia da 0 se Increm. non è attivo)

-   **Scale predefined**
-   **Scale predefined :** le scale predefinite sono km, hm, dam, m, dm, cm, **mm**, µm, nm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique, oppure impostare l\'unità desiderata nel campo Scale free.

-   \'\'\'Number copy \'\'\'
-   **Number copy :** numero di copie

-   **Scale free**
-   ****...** :** Questo pulsante adatta i valori per Y e Z al valore di X per scalare su tutti gli assi con lo stesso valore (o impostare manualmente gli stessi valori). Due click per ripristinare i valori di scale a 1,0
-   **Scale X :** scala a scelta , se il valore è negativo **( -10)** , l\'oggetto viene ingrandito **x 10** e viene invertita la direzione sull\'asse X, per ridurre la forma inserire un valore decimale **(0,5)**
-   **Scale Y :** scala a scelta , se il valore è negativo **( -10)** , l\'oggetto viene ingrandito **x 10** e viene invertita la direzione sull\'asse Y, per ridurre la forma inserire un valore decimale **(0,5)**
-   **Scale Z :** scala a scelta , se il valore è negativo **( -10)** , l\'oggetto viene ingrandito **x 10** e viene invertita la direzione sull\'asse Z, per ridurre la forma inserire un valore decimale **(0,5)**

-   ****ValueAt()** :** Attribuisce il vettore valueAt() dei subObject selezionati Face, Wire, Line \...
    Questa opzione è utile quando i dati indicati di Placement sono \[0,0,0\] e la posizione effettiva dell\'oggetto non corrisponde alle coordinate di base 0,0,0 (non dà informazioni sulla rotazione dell\'oggetto)
-   ****OK** :** il pulsante OK convalida e lancia il comando, se non è selezionato alcun oggetto il pulsante **Ok** ha il colore rosso
-   ****Reset** :** il pulsante Reset azzera tutti i valori
-   ****Quit** :** esce dalla macro




## Script

L\'icona di Macro\_CloneConvert: ![](images/Macro_CloneConvert.png )

**Macro\_CloneConvert.FCMacro**

Scaricare la macro da Gist [Macro\_CloneConvert.FCMacro](https://gist.github.com/mario52a/9f2f2f6144e1307a048f1840ef99300c)

## Revision

14/06/2016 ver 0.9 = adding the choice of number of copies and labels optimization

06/06/2020 ver 0.15 = icon

20/05/2020 ver 0.14 = grid layout PySide2 Qt5

15/09/2019 ver 0.13 = replace the grec sign micro to \"um\", replace all \"\_translate(\"MainWindow\", \"mm\", None)\" to \"mm\" and comment line \"text.encode(\'utf-8\')\" cause not work with FC 0.19 18.213

01/06/2019 ver 0.12 = adapted for 0.19 et correction \"Copy:legacy=True\" and ShapeColor \.....

30/03/2018 ver 0.11 = odd checkBox, if multi selection the clone are object unique or object separate

07/06/2017 ver 0.10 = replace Draft\...Copy to Part..Shape cause section Copy : not draw copy scaled of object but copy not scaled ??

14/06/2016 ver 0.9 = adding the choice of number of copies and labels optimization

31/01/2016 ver 0.8 = modify the buttons reset section for two click for reset (in case modification the value)

30/01/2016 ver 0.7 = rewriting code with Placement and Increment and adding buttons Compound, Increment, ValueAt(),

26/01/2016 ver 0.6 = correction placement with many objets Copy

26/07/2015 ver 0.5 = correction rotate many objects Function Copy

25/07/2015 ver 0.4 = adding rotation

11/08/2014 replace \"AttributeError\" to \"Exception\"

02/07/2014 ver. 0.3 = modified to operate PyQt4 and PySide

09/05/2014 ver. 0.2 = adding function \"Copy\"

---
[documentation index](../README.md) > Macro CloneConvert/it
