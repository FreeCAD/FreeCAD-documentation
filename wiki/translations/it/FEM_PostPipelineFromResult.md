# FEM PostPipelineFromResult/it
---
- GuiCommand:/it   Name:FEM PostPipelineFromResult   Name/it:Post Pipeline da risultato   MenuLocation: Risultati → Post Pipeline da risultato   |Workbenches:[Version:0.17   Shortcut:   SeeAlso:[[FEM_tutorial/it|Tutorial FEM](FEM_Workbench/it___FEM]].md)---


</div>

**\* You need a valid result object in the **<img src="images/FEM_Analysis.svg" width=24px> [Analysis container](FEM_Analysis.md)
**, such as **CalculiX static results**.**

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Pipeline è un oggetto risultato, che crea una nuova rappresentazione grafica dei risultati dell\'analisi FEM sulla parte analizzata. Aggiunge scala di colori e più opzioni di visualizzazione.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Utilizzo

-   Serve un oggetto risultato valido nel **<img src="images/_FEM_Analysis.png_" width= 24px> [contenitore Analisi](FEM_Analysis/it.md)**, come **CalculiX_static_results**.
-   Selezionare l\'oggetto risultato
-   Fare clic sul pulsante <img alt="" src=images/_FEM_PostPipelineFromResult.png  style="width:24px;">, oppure fare clic sul menu **Risultati** e sull\'elemento **Post Pipeline from results**. Al documento viene aggiunto un nuovo oggetto chiamato \"Pipeline\" ; notare che appare al di fuori del contenitore delle analisi.
-   Fare doppio clic sul nuovo oggetto Pipeline nell\'albero del modello e selezionare il tipo di proprietà da visualizzare. Le impostazioni tipiche sono: Mode: selezionare **Superficie**, Field: I.e. **Von Mises stress** ![](images/Pipeline.PNG )
    -   Mode: come disegnare i risultati
    -   Field: quale proprietà risultato disegnare
    -   Vector: se una proprietà è un vettore, è possibile limitare i dati a un asse (X, Y, Z) o selezionare Magnitudine per utilizzare il valore vettoriale.
-   Se non si vede alcun modello nell\'area grafica, andare a **Modifica** → **Preferenze**, selezionare **Visualizazione** e attivare la casella **Abilita il colore di retroilluminazione**
-   Facendo doppio clic sulla scala, è possibile modificare le proprietà di visualizzazione.

![](images/_SIMTUT_05.PNG )

-   -   Gradiente: si può selezionare l\'ordine inverso del gradiente di colore predefinito o Nero-Bianco o Bianco-Nero.
    -   Intervallo parametri: i valori minimo e massimo vengono inseriti automaticamente quando si seleziona una proprietà da valutare sull\'oggetto **Pipeline**; è possibile modificarli, accertarsi però di sapere cosa si sta facendo. È inoltre possibile modificare il numero di etichette visualizzate e il numero di posizioni decimali da visualizzare.


</div>

## Limitazioni

Ancora una volta, si noti, che la rappresentazione Pipeline dei risultati (denominata VTK) sulla parte visualizzata è diversa dai risultati del gradiente di colore che sono visibili al termine della soluzione. I valori nella scala sfumatura non possono essere applicati all\'oggetto risultato della soluzione.





{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM PostPipelineFromResult/it
