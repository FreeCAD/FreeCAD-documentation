---
- GuiCommand:/it
   Name:PartDesign_WizardShaft
   Name/it:PartDesign Procedura guidata per alberi
   MenuLocation:PartDesign → Assistente Formazione Albero...
   Workbenches:[DisegnoPezzo](PartDesign_Workbench/it.md)
---

# PartDesign WizardShaft/it

## Descrizione

Questo strumento permette di creare un albero da una tabella di valori, e di analizzare forze e momenti. Si può avviare la procedura guidata dal menu Part Design **Part Design → [<img src=images/PartDesign_WizardShaft.svg style="width:20px"> Procedura guidata per alberi...**.

L\'assistente si avvierà e mostrerà una tabella predefinita, la parte d\'albero corrispondente e i grafici forza/momento.

<img alt="" src=images/WizardShaft_Part.jpg  style="width:780px;"> 

La parte superiore della finestra è occupata dalla tabella. È organizzata in colonne numerate che corrispondono ai segmenti dell\'albero. Un segmento d\'albero è caratterizzato da una certa lunghezza e diametro. La finestra principale mostra due schede. Una è la parte dell\'albero stesso (una caratteristica di rivoluzione), mostrata nell\'immagine sopra. La seconda scheda mostra i grafici delle forze di taglio e dei momenti creati dai carichi definiti nella tabella.

<img alt="" src=images/shaftwizard1.jpg  style="width:1024px;"> 

## Prerequisiti

L\'assistente di creazione dell\'albero dipende dalla [matplotlib](http://matplotlib.org/) libreria per creare e visualizzare i grafici della forza di taglio e del momento di flessione. Per i sistemi basati su Debian/Ubuntu, è disponibile tramite il pacchetto python-matplotlib.

## Parametri

Per ogni segmento dell\'albero, possono essere definiti i seguenti parametri:

-   La lunghezza del segmento.
-   Il diametro del segmento.
-   Il tipo di carico. (Notare che dopo il suo scorrimento, è necessario fare clic nel menu sulla voce desiderata, altrimenti non viene selezionata).
    -   None : Nessun carico.
    -   Fixed : L\'albero è fissato ad una estremità (ad esempio saldato a un\'altra parte). Questo tipo di carico può essere definito per il primo o l\'ultimo segmento.
    -   Static : C\'è un carico statico sul segmento dell\'albero.
-   Il carico sul segmento dell\'albero.
-   La posizione in cui è applicato il carico al segmento. La posizione viene calcolata dal bordo sinistro del segmento.

(La funzionalità per altre linee e tipi di carico non è stata ancora implementata)

## Menu

Per aggiungere un nuovo segmento all\'albero, fare clic con il tasto destro nello spazio vuoto a destra della tabella, quindi fare clic su **Aggiungi colonna**.

## Limitazioni

-   Non è possibile avere segmenti d\'albero adiacenti con lo stesso diametro.

## Funzionalità pianificate 

-   Tabella guidati smussi e arrotondamenti sui le bordi dell\'albero
-   Riconoscono una parte creato prima con assistente albero e inizializzare dei valori della tabella da essa
-   Calcolazione sollecitazioni sull\'albero
-   Visualizzazione dei carichi sull\'albero (può usare la stessa funzionalità del modulo FEM)
-   Definizione dei carichi come un oggetto documento (può usare la stessa funzionalità del modulo FEM)
-   Database dei materiali
-   Permettere carichi in direzione Z e in direzione Y (richiede la definizione dei carichi come un oggetto documento, altrimenti la tabella diventerà molto lunga)





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign WizardShaft/it
