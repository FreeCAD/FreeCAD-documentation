---
- TutorialInfo:/it
   Topic: Stampa proiezioni
   Level: Base
   Time: 15 minuti
   Author:[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
   FCVersion:0.16 o superiore
   Files:
---

# Drawing tutorial/it

 **Lo sviluppo del modulo Drawing è stato interrotto in FreeCAD 0.16 con il proposito di sostituirlo con il nuovo modulo [TechDraw](TechDraw_Workbench/it.md) che sarà introdotto nella versione 0.17. Nella versione 0.17 sono forniti entrambi i moduli, ma il modulo Drawing potrebbe essere rimosso nelle versioni future.**



### Introduzione

Questo tutorial ha lo scopo di introdurre il lettore al flusso di lavoro di base dell\'ambiente [Drawing](Drawing_Workbench/it.md), e alla maggior parte degli strumenti che sono a disposizione per creare la stampa delle viste.

<img alt="" src=images/Drawing_tutorial_result.png  style="width:480px;">

### Requisiti

-   FreeCAD versione 0.16 o superiore
-   Il lettore abbia le conoscenze di base per utilizzare gli ambienti Part e PartDesign
-   Il lettore abbia terminato la lettura del [Tutorial di Draft](Draft_tutorial/it.md)

### Procedura

#### Preparativi

Per velocizzare questo tutorial, è necessario raggruppare gli elementi simili nella **Vista a albero** in modo da poter applicare le operazioni contemporaneamente a diversi elementi.

##### Raggruppare gli elementi 

1.  Nella **Vista a albero**, cliccare con il tasto destro sul nome del documento. In questo caso **Unnamed**.
2.  Selezionare **Crea gruppo**. È possibile modificare il nome del gruppo di con un doppio clic su di esso nella **Vista a albero**.
3.  Selezionare gli elementi che si desidera aggiungere e trascinarli nel gruppo

Creare i seguenti gruppi:

-   Draft_oggetti
-   Draft_dimensioni
-   Draft_annotazioni_testi

#### Modelli di squadrature 

Le squadrature sono la base dei disegni, è possibile utilizzare uno dei modelli forniti oppure crearne una propria.

1.  Selezionare il menu a discesa accanto a <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [Nuovo disegno A3 orizzontale](Drawing_Landscape_A3/it.md)
2.  Selezionare **A4 orizzontale**

Ora nella **Vista ad albero** appare una nuova cartella chiamata **Pagina**. Questo oggetto contiene tutto ciò che riguarda il **Disegno**.

#### Proiezioni

Le proiezioni sono definite come la rappresentazione visiva di un oggetto su un piano specifico, e mostrano le proprietà dell\'oggetto che sono visibili da uno specifico orientamento.

##### Proiezioni ortografiche 

Queste proiezioni sono utilizzate in Ingegneria per specificare le proprietà di un oggetto che verrà lavorato. Ci sono due standard comuni: **Terzo angolo** e **Primo angolo**.

In questo tutorial, queste proiezioni non sono utilizzate perché i nostri oggetti hanno una rappresentazione significativa solo nel piano XY.

1.  Selezionare l\'oggetto che si desidera proiettare nel disegno.
2.  Selezionare <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Vista ortogonale](Drawing_Orthoviews/it.md)
3.  Selezionare il tipo di **proiezione** che si intende usare
4.  Selezionare la vista che si desidera aggiungere

Nelle schede **Generale** e **Assonometria** si può specificare **posizione**, **scala** e **spaziatura** di ogni vista.

##### Altre proiezioni della Parte 

E\' possibile creare visualizzazioni personalizzate dell\'oggetto.

1.  Selezionare l\'oggetto che si desidera proiettare nel disegno.
2.  Selezionare <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Inserisci una nuova vista](Drawing_View/it.md)
3.  Nella scheda **Dati** editare la **Direzione della proiezione** modificando i valori degli assi **X**, **Y**, e **Z**. Di default, i valori sono **(0, 0, 1)**

Dalla tabella dei **Dati** si può anche modificare **posizione**, **scala** e **rotazione** della **Vista**, come per la **Proiezione ortografica**.

##### Proiezioni di Draft 

Il modo migliore per aggiungere gli elementi creati nell\'ambiente **Draft** è quello di usare lo strumento di questo ambiente che è progettato specificamente per questo. Con questa procedura, è possibile importare **Dimensioni**, **Annotazioni**, **Forme-testo** e ogni altro elemento creato all\'interno di Draft.

1.  Passare all\'ambiente **Draft**
2.  Selezionare il **gruppo** o gli **elementi** da proiettare. In questo caso **Draft_dimensioni**
3.  Selezionare ![](images/Draft_PutOnSheet.png ) [Disegno](Draft_Drawing/it.md)
4.  Impostare le coordinate **X** e **Y** a **(140,100)**
5.  Impostare la scala 0.5

Ripetere l\'operazione per ogni gruppo e impostare i valori indicati sopra.

#### Esportare il lavoro 

FreeCAD supporta l\'esportazione di file SVG e PDF basati su **Drawing**

##### SVG

1.  Selezionare <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Salva disegno](Drawing_Save/it.md)
2.  Specificare il percorso e il nome del file esportato

##### PDF

1.  Nel menu **File**, selezionare **Esporta PDF \...**
2.  Specificare il percorso e il nome del file esportato

Il flusso di lavoro di base per l\'ambiente [Drawing](Drawing_Workbench/it.md) è concluso.



## Letture consigliate 

-   Per informazioni su come creare modelli personalizzati vedere [Creare modelli di squadrature](Drawing_Template_HowTo/it.md)
-   Per ulteriori informazioni sugli strumenti disponibili consultare la pagina [Ambiente Drawing](Drawing_Workbench/it.md)


{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing tutorial/it
