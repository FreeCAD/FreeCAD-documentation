# Macro CirclePlus/it
{{Macro/it
|Name=Macro CirclePlus
|Translate=Cerchio con opzione
|Icon=Macro_CirclePlus.png
|Description=Crea un cerchio o un arco dando raggio, diametro, circonferenza, area, inizio, fine, arco, anglecenter, corda, freccia, centro (punto), placemObject a scelta (con interfaccia grafica).
|Download=[https://www.freecadweb.org/wiki/images/4/4c/Macro_CirclePlus.png Macro_CirclePlus].
|Author=mario52
|FCVersion=All
|Version=0.4
|Date=2019/04/07
}}

## Descrizione

Questa macro crea un cerchio o un arco e consente all\'utente, utilizzando la seguente opzione (tramite una finestra di dialogo), di personalizzare: \'\'raggio, diametro, circonferenza, area, angolo iniziale, angolo finale, arco, angolo al centro, corda, freccia, centro (punto), \'\' e \'\' placemObject \'\'.

Il cerchio, per impostazione predefinita, è rivolto verso lo schermo (si riferisce alla funzione getCameraOrientation per ottenere il suo orientamento). È possibile modificare manualmente questa funzione per personalizzare il posizionamento della forma.

### Legenda

Nella finestra di dialogo CirclePlus alcuni spinbox cambiano colore. Il verde indica che una casella di selezione è stata modificata ed è pronta per essere eseguita. Arancione indica una casella di selezione opzionale che l\'utente può utilizzare se lo ritiene necessario. Il rosso indica un valore mancante o inadeguato. Anche **Ok** diventa rosso e non funziona fino a quando non verranno utilizzati i valori corretti.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/0ed8129bacbe9124a41e3ae1d378d5b7/raw/3f810ac142dd0d9245c5ccc964b8b2d7d750b276/Macro%2520CirclePlus.FCMacro}}


<div class="mw-translate-fuzzy">

## Uso


</div>

Copiare il codice e incollarlo nella directory delle macro

![](images/Macro_CirclePlus_00.png )

-   **X Y Z** : coordinate del cerchio, se non vengono fornite le coordinate il cerchio è creato sul punto 0,0,0
-   **radius** : raggio del cerchio
-   **diameter** : diametro del cerchio
-   ****Reset**** : resetta il valore delle coordinate
-   ****Equal**** : copia il valore di X nelle caselle Y e Z.
-   **CheckBox :**
-   **Options** : altre opzioni per creare il cerchio
-   **Point** : se selezionato, viene creato il punto centrale
-   **Info** : se selezionato, mostra le informazioni fornite nella macro
-   **Face** : se selezionato, nel cerchio viene creata una faccia
-   **Sector** : se selezionato, viene creato un settore
-   **Segment** : se selezionato, viene creato un segmento
-   *SpinBox 1.0*\' : incremento di passo per raggio e diametro (Default: 1.0 (per modificare il valore cambiare il valore riga 87 **\"incrementDS = xx.xx\"**))
-   **SpinBox 8** : assegna l\'altezza del testo nella macro

-   ****Quit**** : esce dalla macro (questo pulsante è colorato in rosso in caso di errore)
-   ****Ok**** : crea il cerchio




![](images/Macro_CirclePlus_01.png )

-   **Opzioni disponibili**
-   **circumference** : circonferenza del cerchio
-   **area** : area del cerchio
-   **startangle** : angolo iniziale per un arco
-   **endangle** : angolo finale per un arco
-   **arc** e **anglecenter** : arco in combinazione con anglecenter
    -   **arc** = lunghezza dell\'arco
    -   **anglecenter** = angolo al centro del cerchio, alle estremità dell\'arco
-   **cord** e **arrow** : corda in combinazione con la freccia del cerchio
    -   **cord** : lunghezza della corda del cerchio
    -   **arrow** : lunghezza della freccia del cerchio




## Script

Scaricare l\'icona <img alt="" src=images/Macro_CirclePlus.png  style="width:64px;"> e inserirla nella stessa directory della macro (non cambiare il suo nome)
{{CodeDownload|https://gist.github.com/mario52a/0ed8129bacbe9124a41e3ae1d378d5b7|Ultima versione di Macro_CirclePlus e le icone alla fine della pagina}}

## Promemoria sulle circonferenze 

**Esempi di codice**

<img alt="examples 1, 2, 3" src=images/Macro_Circle_01.png  style="width:640px;">  <img alt="examples" src=images/Macro_Circle_02.png  style="width:640px;"> 

## Versione

ver 04 , 07-04-2019 : replace setStyleSheet DoubleSpinBox by setStyleSheet Label cause: the increment in the Dspinbox does not work ??!

ver 03 , 06-04-2019 : supp all \"(QtGui.QApplication.translate(\"MainWindow\", \"Diameter\", None, QtGui.QApplication.UnicodeUTF8))\" give error in 0.18.16093 (Git) Hash: 690774c0effe4fd7b8d2b5e2fb2b8c8d145e21ce Python version: 3.6.6 Qt version: 5.6.2

ver 0.2 , 05-04-2019 : add increment the step from 1.0 to 0.1 (DoubleSpinbox)

ver 0.1 , 2018-07-14 : add create segment

ver 0.0 , 2018-07-10 :



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro CirclePlus/it
