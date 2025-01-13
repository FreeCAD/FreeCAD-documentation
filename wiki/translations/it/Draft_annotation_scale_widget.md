# Draft annotation scale widget/it
## Descrizione

Il **Dispositivo (widget) Draft scala annotazione** può essere utilizzato per specificare la scala di annotazione di Draft. Questa scala determina il **Scale Multiplier** dei nuovi [Testi](Draft_Text/it.md), [Quote](Draft_Dimension/it.md) e [Etichette](Draft_Label/it.md). Il dispositivo è disponibile solo in ambiente <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/it.md). È un elemento GUI [opzionale](#Preferenze.md) che si trova nella [Barra di stato](Status_bar/it.md).

![](images/Draft_annotation_scale_widget_button.png ) 
*Il dispositivo Draft scala annotazione*



## Utilizzo

1.  Premere il pulsante **x:x** nella [Barra di stato](Status_bar/it.md). Il pulsante visualizza la scala di annotazione corrente.
2.  Si apre il menu della scala.
3.  Effettuare una delle seguenti operazioni:
    -   Selezionare una delle scale standard.
    -   Selezionare l\'opzione **Personalizza**:
        -   Nella finestra di dialogo che si apre inserire una scala personalizzata utilizzando il formato {{Value|x:x}} o {{Value|x<nowiki>=</nowiki>x}}.
        -   Premere **Enter** o il pulsante **OK**.

![](images/Draft_annotation_scale_widget_menu.png ) 
*Il menu del dispositivo*



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Il dispositivo Draft Scala annotazione è facoltativo: **Modifica → Preferenze... → Draft → Interfaccia →  Mostra il dispositivo Scala annotazione nell'Ambiente Draft**.
-   Per modificare la scala dell\'annotazione senza il dispositivo: **Strumenti → Modifica parametri... → BaseApp → Preferences → Mod → Draft → DraftAnnotationScale**. La scala è definita da un singolo numero. Per una scala di {{Value|1:50}} inserire {{Value|0.02}}.



## Note

-   Vedere anche: [Draft Imposta Stile](Draft_SetStyle/it.md) e [Draft Applica Stile](Draft_ApplyStyle/it.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft annotation scale widget/it
