# Macro CloneConvert/it
{{Macro/it
|Name=Macro CloneConvert
|Icon=Macro_CloneConvert.png
|Description=Crea un Clone/Copia/Composto dell'oggetto/degli oggetti e poi converte in una posizione e dimensione scelta (''pollici, mm, m, µm''...) o libera. L'oggetto base è riconosciuto in ''mm'' (base FreeCAD).
|Author=mario52
|Version=0.16
|Date=2025-01-06
|FCVersion= ≥0.18
|Download=[https://www.freecadweb.org/wiki/images/0/0a/Macro_CloneConvert.png ToolBar Icon]
}}

## Descrizione

Crea un clone o una copia dell\'oggetto e poi lo colloca nella posizione scelta e con le dimensioni desiderate (*pollici, mm, m, µm*\...) o a piacere. L\'oggetto base è misurato in *mm* (secondo il sistema base di FreeCAD)


{{Codeextralink|https://gist.githubusercontent.com/mario52a/9f2f2f6144e1307a048f1840ef99300c/raw/fb76b3c728c1c7cd085e87f5d6d223d9f79bb574/Macro_CloneConvert.FCMacro}}

## Utilizzo

1.  Avviare la macro
2.  Definire le impostazioni di XYZ
3.  Scegliere \"Clone\" o \"Copy\"
4.  Scegliere un\'unità di misura
5.  Selezionare l\'oggetto
6.  Fare click su **Ok**

## Note

-   Se non viene inserito alcun valore viene creata una copia o un clone senza modifiche.
-   Se non è selezionato alcun oggetto il pulsante **Ok** è colorato in rosso.

I valori di **BoundingBox**, **Volume** e **Surface** sono indicati nella [vista Report](Report_view/it.md), nel caso di **Copy** per oggetti multipli, il display visualizza BoundingBox 0.0.

L\'unità di base è il mm, esempio con il lato del cubo di **1 mm**:

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
**4%** = **0,04** nel campo **\"Scale free\"**
Le unita predefinite sono: km, hm, dam, m, dm, cm, **mm**, µm, nm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.
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

-   **Number copy**
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

L\'icona di Macro_CloneConvert: ![](images/Macro_CloneConvert.png )

**Macro_CloneConvert.FCMacro**

Scaricare la macro da Gist [Macro_CloneConvert.FCMacro](https://gist.github.com/mario52a/9f2f2f6144e1307a048f1840ef99300c)



## Revisioni

01/06/2025 ver 00.16 sostituisce PySide2 con PySide aumenta mini e maxi cancella tutti i riferimenti a PySide, PySide2 e QtWidgets e corregge il clone, composto

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
⏵ [documentation index](../README.md) > Macro CloneConvert/it
