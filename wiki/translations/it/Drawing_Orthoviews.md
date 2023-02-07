# Drawing Orthoviews/it
---
- GuiCommand:/it   Name:Drawing Orthoviews   Name/it:Viste ortogonali   Workbenches:[MenuLocation:Drawing → Inserisci viste ortogonali   Shortcut:none   SeeAlso:[[Drawing Landscape A3/it|Nuovo disegno](Drawing_Workbench/it___Drawing]],_Complete.md)---

Lo strumento Viste ortogonali inserisce una serie di proiezioni ortografiche dell\'oggetto selezionato nel foglio di disegno attivo. Notare che non crea un singolo oggetto vista sulla pagina. Crea invece una proiezione ortografica separata per ciascuna delle viste selezionate nelle opzioni.

Lo strumento Viste ortogonali crea tutte le proiezioni ortografiche è lo strumento ideale per fornire la vista principale.



## Utilizzo

1.  Selezionare una funzione nell\'albero del modello.
2.  Se è presente più di una pagina, selezionare più volte la pagina desiderata (mantenendo la funzione selezionata).
3.  Premere il pulsante **<img src="images/Drawing_Orthoviews.png" width=16px> [Inserisci viste ortogonali](Drawing_Orthoviews/it.md)**.
4.  Definire le opzioni di creazione della vista desiderate. Vedere le [Opzioni](#Opzioni.md).
5.  Fare clic su OK per creare le viste della funzione selezionata sulla pagina selezionata.



## Opzioni

A seconda delle selezioni effettuate, alcune opzioni potrebbero non essere disponibili.

![](images/Drawing_Orthoviews_Options.png )

-   **Projection**: Selezionare se si desidera una proiezione terzo angolo (impostazione predefinita) o una proiezione primo angolo
-   **View from**: Scegliere l\'asse che deve essere rivolto verso l\'utente.
-   **Axis aligned right**: Scegli l\'asse rivolto a destra sul foglio di disegno. L\'asse rimanente sarà verticale sulla pagina.
-   **Secondary views**: Scegliere le viste che si desidera creare. La vista principale si trova al centro delle caselle di controllo ed è orientata dalle opzioni {{Variable|View from}} e {{Variable|Axis aligned right}}. Vengono create delle viste secondarie per ogni casella selezionata.



### Aspetti generali 

-   **Auto scale / position**: Se questa casella è selezionata, la scala, la posizione e la spaziatura della vista sono scelte per utilizzare al meglio lo spazio disponibile sulla pagina. Se questa casella è deselezionata, l\'utente deve specificare scala, posizione e spaziatura.
-   **Scale**: La scala per la vista, espressa come denominatore di una frazione di scala. Pertanto, {{SystemInput | 2 |}} crea un gruppo di viste ridimensionato a 1:2.
-   **Top left x / y**: La posizione del gruppo di viste rispetto alla parte superiore sinistra della pagina. Aumentando il valore x (prima colonna) si spostano le viste a destra. Aumentando il valore y (seconda colonna) si spostano le viste verso il basso sulla pagina.
-   **Spacing dx / dy**: Le distanze x (prima colonna) e y (seconda colonna) tra le viste adiacenti. Le spaziature sono la spaziatura del sistema di coordinate della parte; nella maggior parte dei casi ci sarà meno spazio tra le viste rispetto al valore di spaziatura (dato che le viste hanno dimensioni x e y).
-   **Show hidden lines**: Se selezionato, nelle viste sono visibili le linee nascoste.
-   **Show smooth lines**: Se selezionato, mostra le linee in cui la curvatura è discontinua (ad esempio, dove un raccordo si collega a una parte piatta).



## Proprietà

Non ci sono proprietà per questo comando; il comando crea le proprietà per ciascuna delle singole viste.



## Script

Viste ortogonali di Drawing non è richiamabile negli script. Negli script, con il comando Viste ortogonali si possono creare solo le singole viste.



## Limitazioni

Da fare



## Tutorial

-   [Tutorial di Drawing](Drawing_tutorial/it.md), Introduzione alla creazione di disegni tecnici con l\'ambiente Drawing
-   [Manuale: Generare disegni 2D](Manual:Generating_2D_drawings/it.md) con l\'ambiente Drawing e l\'addon Drawing Dimensioning.


{{docnav/it
|[Apri Browser](Drawing_Openbrowser/it.md)
|[Simbolo](Drawing_Symbol/it.md)
|[Drawing](Drawing_Workbench/it.md)
|IconL=Drawing_Openbrowser.png
|IconC=Workbench_Drawing.svg
|IconR=Drawing_Symbol.png
}}


{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing Orthoviews/it
