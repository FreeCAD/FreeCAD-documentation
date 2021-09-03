---
- GuiCommand:Addon/it
   Name:BIM Classification
   Name/it:Classificazione BIM
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench/it.md)
   Addon:BIM
   MenuLocation:Gestione → Classificazione
---

## Descrizione

<img alt="" src=images/BIM_classification_screenshot.png  style="width:1024px;">

Il gestore delle classificazioni consente di attribuire una classe standard a un oggetto o materiale BIM. Diversi sistemi di classificazione sono disponibili in formato XML o IFC (entrambi supportati da questo strumento) da <https://github.com/Moult/IfcClassification> o direttamente dai loro editori o da <https://www.graphisoft.com/downloads/archicad/BIM_Data.html>. Per rendere noti questi file XML o IFC a FreeCAD, essi devono essere collocati in una sottocartella BIM della cartella utente di FreeCAD. Per fornire la posizione esatta al sistema usare la finestra di dialogo di classificazione BIM. Se sono disponibili sia un file IFC che un file XML, lo strumento di classificazione BIM preferisce quello IFC.

## Utilizzo

-   Installare uno o più file XML o IFC standard di classificazione come spiegato sopra
-   Se si desidera aggiungere o modificare una classe per un oggetto, selezionare tale oggetto e premere il pulsante Classificazione BIM
-   Se si desidera aggiungere o modificare una classe per un materiale, non selezionare nulla e premere il pulsante Classificazione BIM. Si potrà sfogliare i materiali direttamente dalla finestra del manager di classificazione
