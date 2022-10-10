# Interface/it
{{TOCright}}

## Introduzione

L\'interfaccia di FreeCAD si basa su Qt, un noto toolkit di interfaccia utente grafica (GUI), particolarmente utilizzato in Linux, ma disponibile anche in Windows e MacOS.

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width   *1024px;">



*Interfaccia standard di FreeCAD 0.19.*

La finestra principale dell\'applicazione può essere suddivisa approssimativamente in 11 sezioni   *

1.  L\'[area della vista principale](main_view_area/it.md), che può contenere diverse finestre a schede
2.  La [vista 3D](3D_view/it.md), normalmente incorporata nell\'area della vista principale
3.  La parte superiore della [vista combinata](combo_view/it.md), che include la [vista ad albero](tree_view/it.md) e il [pannello delle azioni](task_panel/it.md)
4.  La parte inferiore della [vista combinata](combo_view/it.md), che include l\'[editor delle proprietà](property_editor/it.md)
5.  La [vista della selezione](selection_view/it.md)
6.  La [vista dei report](report_view/it.md)
7.  La [console Python](Python_console/it.md)
8.  La [barra di stato](status_bar/it.md)
9.  L\'area della barra degli strumenti, vedere le informazioni seguenti sulla barra degli strumenti
10. Il [selettore degli ambienti](Std_Workbench/it.md), che a sua volta è una barra degli strumenti
11. Il [menu standard](Standard_Menu/it.md)

## Componenti dell\'interfaccia 

Come molti software, FreeCAD include una barra dei menu standard, quindi una serie di barre degli strumenti e pannelli in cui si trovano gli strumenti per l\'utente.

### Menu

I [menu standard](Standard_Menu/it.md) sono   * [**File**](Std_File_Menu/it.md), [**Modifica**](Std_Edit_Menu/it.md), [**Visualizza**](Std_View_Menu/it.md), [**Strumenti**](Std_Tools_Menu/it.md), [**Macro**](Std_Macro_Menu/it.md), [**Finestre**](Std_Windows_Menu/it.md), [**Aiuto**](Std_Help_Menu/it.md).

### Barre degli strumenti 

Le barre degli strumenti standard che appaiono nell\'interfaccia sono   *

-   Barra degli strumenti File   * strumenti per lavorare con i file, aprire documenti, copiare, incollare, annullare e ripetere azioni.
-   [Selettore degli ambienti](Std_Workbench/it.md)   * contiene un singolo widget per selezionare l\'[ambiente](workbenches/it.md) attivo.
-   Barra degli strumenti Macro   * strumenti per registrare, modificare ed eseguire le [macro](macros/it.md).
-   Barra degli strumenti Visualizza   * strumenti per controllare la modalità di visualizzazione degli oggetti nella [Vista 3D](3D_view/it.md).
-   Barra degli strumenti Struttura   * strumenti per organizzare gli oggetti nel documento e creare collegamenti a documenti aggiuntivi.

Questi possono essere attivati e disattivati facendo clic con il pulsante destro del mouse su uno spazio vuoto su una delle barre degli strumenti e scegliendo l\'elemento desiderato, oppure dal menu **Visualizza → Barre degli strumenti**.

### Pannelli

I pannelli principali che consentono di lavorare con gli oggetti sono   *

-   [Vista 3D](3D_view/it.md)   * l\'area in cui viene disegnata la geometria 2D e 3D.
-   [Vista combinata](Combo_view/it.md)   * il pannello che contiene la [vista ad albero](tree_view/it.md), il [pannello azioni](task_panel/it.md), e l\'[editor delle proprietà](property_editor/it.md).
-   [Vista ad albero](Tree_view/it.md)   * l\'elemento che mostra tutti gli oggetti nel documento e la loro cronologia parametrica.
-   [Pannello Azioni](Task_panel/it.md)   * il pannello che mostra diverse azioni e opzioni a seconda dello strumento selezionato.
-   [Editor delle proprietà](Property_editor/it.md)   * il luogo in cui si possono modificare le proprietà dell\'oggetto.
-   [Vista selezione](Selection_view/it.md)   * il pannello che mostra gli elementi attualmente selezionati.
-   [Vista report](Report_view/it.md)   * il campo di testo che mostra i messaggi dell\'applicazione e dei suoi strumenti.
-   [Console Python](Python_console/it.md)   * l\'editor che consente di eseguire il codice [Python](Python/it.md) in modo interattivo per vedere i risultati nella [vista 3D](3D_view/it.md).
-   [Barra di stato](Status_bar/it.md)   * la barra che mostra determinati messaggi dell\'applicazione e che ha il selettore per impostare il [tipo di mouse](Mouse_navigation/it.md).
-   [Vista DAG](DAG_view/it.md)   * un\'alternativa alla [vista ad albero](tree_view/it.md), che mostra le relazioni tra oggetti diversi attraverso un grafico.

Ad eccezione della vista 3D, tutto può essere attivato e disattivato facendo clic con il pulsante destro del mouse su uno spazio vuoto su una delle barre degli strumenti in alto e scegliendo l\'elemento desiderato, oppure dal menu **Visualizza → Pannelli**.

Per attivare e disattivare la barra di stato utilizzare il menu **Visualizza → Barra di stato**.

### Altro

Altre interfacce e finestre utili includono   *

-   [Ispettore di scena](Std_SceneInspector/it.md)   * un pannello che mostra i nodi Coin3D che compongono la [scena grafica](Scenegraph/it.md). Per utenti esperti e sviluppatori, può essere utile per risolvere le operazioni che manipolano direttamente la scena e gli oggetti creati nella [Vista 3D](3D_view/it.md).
-   [Grafico delle dipendenze](Std_DependencyGraph/it.md)   * una finestra che mostra il grafico delle dipendenze di tutti gli oggetti nel documento, creato con il programma ausiliario [Graphviz](https   *//graphviz.org/). È utile per riconoscere i problemi nella creazione di oggetti, come le dipendenze circolari, che potrebbero non essere del tutto evidenti dalla [vista ad albero](Tree_view/it.md) o dalla [vista DAG](DAG_view/it.md).

### Personalizzazione

Le barre degli strumenti possono avere più o meno pulsanti e le barre degli strumenti personalizzate possono essere create con un mix di strumenti diversi e per ospitare le macro sviluppate.

Queste opzioni sono nel menu **Strumenti → Personalizza**. Vedere [Personalizzare l\'interfaccia](Interface_Customization/it.md).


{{Interface navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Interface/it
