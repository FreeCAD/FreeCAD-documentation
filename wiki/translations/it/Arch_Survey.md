---
- GuiCommand:/it
   Name:Arch Survey
   Name/it:Ispeziona
   MenuLocation:Arch → Ispeziona
   Workbenches:[Arch](Arch_Workbench/it.md)
   SeeAlso:[FCInfo|<img src=images/FCInfo.png style="width:24px"> [FCInfo (macro)](Macro_FCInfo/it.md)<br />[Macro SimpleProperties (macro)](Macro_SimpleProperties.md)
---

# Arch Survey/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Arch_Survey.svg  style="width:16px;"> Ispeziona entra in una speciale modalità di rilevamento, che consente di acquisire rapidamente misure e informazioni provenienti da un modello, e di trasferirle ad altre applicazioni. Quando si è in modalità Ispeziona, cliccando sui diversi sotto-elementi degli oggetti 3D si acquisiscono le seguenti informazioni, secondo su cosa si clicca:


</div>

-   Se si fa clic su uno spigolo, si ottiene la sua lunghezza
-   Se si fa clic su un vertice, si ottiene la sua altezza (coordinata sull\'asse Z)
-   Se si fa clic su una faccia, si ottiene la sua area
-   Se si fa doppio clic su una qualsiasi cosa, quindi si seleziona l\'intero oggetto, si ottiene il suo volume

Quando vengono acquisite delle informazioni, succedono tre cose:

-   Sulla parte superiore dell\'elemento selezionato viene posta una etichetta che visualizza il valore (con la \"a\" per l\'area, \"l\" per la lunghezza, \"z\" per l\'altezza, o \"v\" per il volume)
-   Il valore numerico viene copiato negli appunti, in modo da poterlo incollare in un\'altra applicazione
-   Nella finestra di output di FreeCAD viene stampata una riga. Quando si esce dalla modalità di indagine, tali righe possono essere copiate e incollate in un\'altra applicazione (i valori sono separati da virgole, rendendo più facile convertirli in dati per i fogli di calcolo)

<img alt="" src=images/Arch_Survey_example.jpg  style="width:640px;">

*L\'immagine sopra mostra cosa succede quando si esegue la modalità di indagine.*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Arch_Survey.svg" width=16px> Ispeziona
**
2.  Cliccare su vertici, spigoli, facce o fare doppio clic per selezionare gli oggetti interi
3.  Fare clic all\'esterno di qualsiasi geometria (sullo sfondo della vista 3D) per rimuovere le etichette esistenti, stampare una riga del totale nella finestra di dialogo Azioni e riavviare da zero il conteggio delle lunghezze e delle aree.
4.  Premere **ESC** o il pulsante **'''Close'''** per uscire dalla modalità di indagine e rimuovere tutte le etichette.


</div>

## Opzioni

-   È possibile aggiungere un\'etichetta personalizzata a qualsiasi riga nella finestra di dialogo Attività facendo clic su quella linea, quindi aggiungendo un testo nel campo della descrizione, quindi premere il pulsante **imposta descrizione**.
-   Alla fine, prima di chiudere, si può esportare il contenuto della finestra di dialogo Attività premendo il pulsante \"export CSV\". Il file CSV risultante può quindi essere aperto in qualsiasi applicazione di foglio di calcolo come Excel o LibreOffice Calc. Nel file CSV risultante i valori e le unità sono separati e i totali sono scritti come funzioni SUM().

<img alt="" src=images/Arch_Survey_spreadsheet.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

La modalità di indagine non ha un\'interfaccia di programmazione, ma da qualsiasi oggetto selezionato basato su [Part](Part_Workbench/it.md) è facile raccogliere le stesse informazioni e riprodurle utilizzando il seguente script:


</div>


```python
import FreeCADGui

selection = FreeCADGui.Selection.getSelectionEx()

for obj in selection:
    for element in obj.SubObjects:
        print("Area: %f", element.Area)
        print("Length: %f", element.Length)
        print("Volume: %f", element.Volume)
        print("Center of Mass: %f", element.CenterOfMass)
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Survey/it
