# FEM PostPipelineFromResult/it
---
 GuiCommand:   Name: FEM PostPipelineFromResult   Name/it: Post Pipeline da risultato   MenuLocation:  Risultati , Post Pipeline da risultato   ---


</div>

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

If you see no model in the graphical area, go to and enable **Edit → Preferences → Display → 3D View → Rendering → Backlight color**.

If you use a [SI](https://en.wikipedia.org/wiki/International_System_of_Units)-derived FreeCAD [unit system](Preferences_Editor#Units.md), the values in the output scale are based on SI units as well. This means the displacement is in meter, the stress is in Pascal and the temperature is in Kelvin.

## Properties

### Dialog box 

This pipeline dialog box has the following settings:

-   **Mode**: How to draw the results. The possible modes are
    -   **Outline**: The outline of the result mesh. In fact, it displays no results but only the borders of the mesh.
    -   **Nodes**: The result mesh nodes.
    -   **Surface**: This is the default and displays the surface of the result mesh.
    -   **Surface with Edges**: Like **Surface** but with the mesh outline edges and the surface mesh node connection lines.
-   **Field**: Which result property to draw.
-   **Vector**: Is only active if the **Field** is a vector. You can select whether to display the vector *Magnitude* or its X, Y, Z components.

### Scale

If you double-click on the scale, you get this settings dialog box:

![](images/SIMTUT_05.PNG )

and you can modify these properties:

-   **Gradient**: You can select reversed order of the default color gradient, *Red-White-Blue*, *Black-White* or *White-Black*.
-   **Style**: The default option *Flow* uses the full color gradient range. The option *Zero* uses only the color gradient range starting form the color that would display the mean value to the maximum.
-   **Visibility**: The option *Out grayed* will color all mesh nodes whose values are outside the set minimum/maximum range in gray. The option *Out transparent* will make these mesh nodes transparent.
-   **Parameter range**: Minimum and maximum values are filled-in automatically. You can modify them, however make sure you know what you are doing. You can also change the number of displayed decimal places and the number of labels distributed over the parameter range.

### Property Editor 

In the [property editor](Property_editor.md) you can set in the *View* tab the settings from the dialog box. In the *Data* tab you can additionally set this:

-    **Mode**: How the filters used in the pipeline will be treated. These modes are possible:

    -   **Serial**: In this mode every filter takes the previous filter as input. The order is hereby the order of creation. The first created filter takes the pipeline as input. Its **Input** property is therefore empty.
    -   **Parallel**: In this mode all filters take the pipeline as input.
    -   **Custom**: <small>(v0.20)</small>  This is the default and keeps the input of the filters as they are. Therefore it allows to have e.g. two filters that take the pipeline as input, and a third filter that takes one of the two filters as input.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostPipelineFromResult/it
