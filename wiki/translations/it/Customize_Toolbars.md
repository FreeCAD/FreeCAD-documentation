# Customize Toolbars/it
{{TutorialInfo/it|Topic=Configurazione|Level=Principiante|Time=5 minuti|Author=[Mario52](User_Mario52.md)|FCVersion=Tutte}}

## Introduzione


<div class="mw-translate-fuzzy">

Questo tutorial spiega come creare un pulsante nella barra degli strumenti per avviare velocemente una macro o per associare altri collegamenti a una icona personalizzata. Gli strumenti (inclusi gli strumenti Macro) possono essere usati in diversi ambienti di lavoro. In un esempio, una Macro diventa uno Strumento-macro creando un **\'Testo**\', un **\'Suggerimento**\' (Tool tip) e una **\'Icona**\'. Successivamente questo Strumento-macro diventa parte di una barra degli strumenti extra in un ambiente di lavoro.


</div>

## Utilizzo

**1.** Trovare il menu Personalizza

-   Selezionare **Menu principale → Strumenti → Personalizza**

<img alt="Customize" src=images/CustomizeToolBar_01.png  style="width:640px;"> 

-   o fare clic con il pulsante destro del mouse su qualsiasi barra degli strumenti

<img alt="Right mouse click" src=images/CustomizeToolBar_02.png  style="width:640px;"> 

-   Appare la finestra Personalizza

<img alt="The Customize window appears" src=images/CustomizeToolBar_03.png  style="width:640px;"> 

**2.** Trasformare una macro in uno Strumento-macro

Selezionare la tabella *Macro*

-   Per selezionare un\'icona della barra degli strumenti per la macro cliccare sul pulsante Pixmap **... **.

<img alt="Select a toolbar" src=images/CustomizeToolBar_04.png  style="width:640px;"> 

-   Cercare l\'icona appropriata tra quelle già presenti in FreeCAD,


<div class="mw-collapsible mw-collapsed toccolours">

      \[o aggiungere una propria icona cliccando sul pulsante **Aggiungi icone...**\].                   (Espandere per un esempio)


<div class="mw-collapsible-content">

<img alt="Add icon" src=images/CustomizeToolBar_05.png  style="width:640px;"> 

     \[Si apre una finestra di selezione dei file, selezionare un file immagine che deve essere di 64x64 pixel in formato PNG\]

<img alt="Get a file" src=images/CustomizeToolBar_06.png  style="width:640px;"> 


</div>


</div>

-   Selezionare l\'icona desiderata poi cliccare sul pulsante **OK**

<img alt="Select your icon" src=images/CustomizeToolBar_07.png  style="width:640px;"> 

-   L\'icona selezionata ora è visualizzata accanto al pulsante Pixmap **...**.

<img alt="Your icon is displayed" src=images/CustomizeToolBar_08.png  style="width:640px;"> 

-   Scegliere la macro e specificare un Testo di menu (il testo che appare come etichetta nel menu); compilare anche il campo Suggerimento (il testo che appare quando il mouse si trova sopra al pulsante sulla barra degli strumenti); per il pulsante si possono anche compilare altri campi opzionali

-   Cliccare su **Aggiungi**.

<img alt="Click the button" src=images/CustomizeToolBar_09.png  style="width:640px;"> 

-   Ora il pulsante dello Strumento-macro è creato

<img alt="Your button is created" src=images/CustomizeToolBar_10.png  style="width:640px;"> 

**3.** Creare una barra degli strumenti al di fuori dell\'ambiente **Macro** che contenga lo **Strumento-macro** creato

-   Cliccare sulla scheda **Barre degli strumenti** e, nel menu a discesa sulla destra, scegliere l\'ambiente di lavoro a cui è destinata la barra degli strumenti (**Parte** in questo esempio)

\[Dalla versione 0.15 c\'è una barra degli strumenti **[<img src=images/Freecad.svg style="width:16px"> Globale **. Se la barra degli strumenti è allegata a questa barra, essa rimane sempre visibile\]

<img alt="Toolbars tab" src=images/CustomizeToolBar_11.png  style="width:640px;"> 

-   Nel menu a discesa sulla sinistra selezionare **Macros**.

<img alt="Macros" src=images/CustomizeToolBar_12.png  style="width:640px;"> 

-   Ora lo Strumento-macro e la sua icona appaiono nell\'elenco

<img alt="Your icon is listed" src=images/CustomizeToolBar_13.png  style="width:640px;"> 

-   Cliccare su **Nuovo...**

<img alt="Click on \"New\"" src=images/CustomizeToolBar_14.png  style="width:640px;"> 

-   Nella finestra \"Nuova barra degli strumenti\" inserire il nome che si vuole dare alla nuova barra per l\'ambiente Part e poi cliccare su **OK**

<img alt="Enter the name for your toolbar" src=images/CustomizeToolBar_15.png  style="width:640px;"> 

-   Ora la barra è stata creata


<div class="mw-translate-fuzzy">

-   Per aggiungere lo Strumeto-macro a questa barra degli strumenti, selezionarla nella finestra di sinistra e quindi fare clic sul **Pulsante** freccia destra.


</div>

<img alt="Select your macro" src=images/CustomizeToolBar_16.png  style="width:640px;"> 

-   È stata creata una barra degli strumenti chiamata \"Camera\" contenente lo Strumento-macro **Camera**.

-   Cliccare sul pulsante **Chiudi**

<img alt="Close" src=images/CustomizeToolBar_17.png  style="width:640px;"> 

-   La nuova barra degli strumenti è ora contenuta nel menu di scelta rapida della barra degli strumenti. Se la barra degli strumenti viene attivata (segno di spunta blu) le sue icone sono visibili (nel nostro esempio c\'è solo la fotocamera).

<img alt="New Toolbar" src=images/CustomizeToolBar_18.png  style="width:640px;"> 

## Note

Vedere anche [Personalizzare l\'interfaccia](Interface_Customization/it.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Preferences](Category_Preferences.md) > Customize Toolbars/it
