# <img alt="L\'icona dell\'ambiente esterno FCGear." src=images/FCGear_workbench_icon.svg  style="width:64px;"> FCGear Workbench/it

## Introduzione


{{TOCright}}

**FCGear** è un [ambiente esterno](external_workbenches/it.md) per la produzione di diversi tipi di ingranaggi e viti senza fine in FreeCAD. La modellazione parametrica consente di modificare in qualsiasi momento le geometrie richieste. Ad esempio, modificando alcuni parametri, l\'ingranaggio evolvente diventa un ingranaggio cilindrico, un ingranaggio elicoidale o un ingranaggio a doppia elica.

Affinché i risultati di FC Gear siano utilizzabili, è necessaria una certa conoscenza di base sui diversi tipi di ingranaggi. Modulo, diametro primitivo e diametro di piede sono termini comuni e dovrebbero quindi essere noti.

In associazione con la stampa 3D, gli utenti domestici hanno ora la possibilità di progettare e produrre ingranaggi e viti senza fine secondo le proprie idee personali e, se necessario, adattarli alle condizioni costruttive.

Prima di poter avviare FCGear, è necessario installarlo (vedere come fare nel paragrafo **Installazione**) sottostante. Dopo l\'installazione, gli strumenti sono disponibili nella barra degli strumenti.

:   ![](images/FCGear_Drop-down-menu_example-en.png )
:   
    
*Il menu a discesa di FCGear*
    

## Tipi di ingranaggi 

### Ingranaggio a spirale 

:   ![](images/Involute-Gear_example.png )
:   
    
*Da sinistra a destra: ingranaggi cilindrici, ingranaggi elicoidali, ingranaggi a doppia elica (vedere [Ingranaggio a spirale](FCGear_InvoluteGear/it.md))*
    

### Cremagliera

:   ![](images/Involute-Rack_example.png )
:   
    
*Da sinistra a destra: ingranaggi cilindrici, ingranaggi elicoidali, ingranaggi a doppia elica (vedere [Cremagliera](FCGear_InvoluteRack/it.md))*
    

### Ingranaggio cicloidale 

:   ![](images/Cycloid-Gear_example_1.png )
:   
    
*Da sinistra a destra: ingranaggi cilindrici, ingranaggi elicoidali, ingranaggi a doppia elica (vedere [Ingranaggio cicloidale](FCGear_CycloideGear/it.md))*
    

### Ingranaggio conico 


<div class="mw-translate-fuzzy">


:   ![](images/Bevel-Gear_example.png )
:   
    
*Da sinistra a destra: ingranaggi cilindrici, denti a spirale (vedere [Ingranaggio conico](FCGear_BevelGear/it.md))*
    


</div>

### Vite senza fine 

:   ![](images/Worm-Gear_example.png )
:   
    
*Sopra: vite senza fine (vedere [Vite senza fine](FCGear_WormGear/it.md))*
    

### Corona dentata 

:   ![](images/Crown-Gear_example.png )
:   
    
*Sopra: corona dentata (vedere [Corona dentata](FCGear_CrownGear/it.md))*
    

### Ingranaggio di distribuzione e Ingranaggio a lanterna 

:   ![](images/Timing+Latern-gear_example.png )
:   
    
*Da sinistra a destra: ingranaggio di distribuzione e ingranaggio a lanterna (vedere [Ingranaggio di distribuzione](FCGear_TimingGear/it.md) o [Ingranaggio a lanterna](FCGear_LanternGear/it.md))*
    

## Riferimenti

-   Autore: looooo
-   Home page: <https://github.com/looooo/FCGear>
-   Codice sorgente su github: <https://github.com/looooo/FCGear>

## Strumenti

### Barra degli strumenti 

-   <img alt="" src=images/FCGear_InvoluteGear.svg  style="width:32px;"> [Ingranaggio a spirale](FCGear_InvoluteGear/it.md) crea un ingranaggio a spirale
-   <img alt="" src=images/FCGear_InvoluteRack.svg  style="width:32px;"> [Cremagliera](FCGear_InvoluteRack/it.md) crea una cremagliera
-   <img alt="" src=images/FCGear_CycloideGear.svg  style="width:32px;"> [Ingranaggio cicloidale](FCGear_CycloideGear/it.md) crea un ingranaggio cicloidale
-   <img alt="" src=images/FCGear_BevelGear.svg  style="width:32px;"> [Ingranaggio conico](FCGear_BevelGear/it.md) crea un ingranaggio conico
-   <img alt="" src=images/FCGear_WormGear.svg  style="width:32px;"> [Vite senza fine](FCGear_WormGear/it.md) crea una vite senza fine
-   <img alt="" src=images/FCGear_CrownGear.svg  style="width:32px;"> [Corona dentata](FCGear_CrownGear/it.md) crea una corona dentata
-   <img alt="" src=images/FCGear_TimingGear.svg  style="width:32px;"> [Ingranaggio di distribuzione](FCGear_TimingGear/it.md) crea un ingranaggio di temporizzazione
-   <img alt="" src=images/FCGear_LanternGear.svg  style="width:32px;"> [Ingranaggio a lanterna](FCGear_LanternGear/it.md) crea un ingranaggio a lanterna

## Installazione

### Installazione automatica 


<div class="mw-translate-fuzzy">

Il metodo di installazione consigliato a partire dalla v0.17 è tramite il <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md). Si trova in 
**Strumenti → Addon manager**


</div>


<div class="mw-collapsible mw-collapsed toccolours" style="width:700px">

### Installazione manuale 

Se è necessario installare manualmente questo ambiente, vengono fornite le seguenti istruzioni per farlo:


<div class="mw-collapsible-content">

#### Linux

-    `git clone https://github.com/looooo/FCGear.git`
    

-   link o copiare la cartella in {{FileName|/freecad/Mod}}

:   

    :   
        `sudo ln -s (path_to_FCGear) (path_to_freecad)/Mod`
        

#### Windows

Testato su (7/8/8.1/10) (From GitHub)

-   scaricare l\'archivio ZIP facendo clic sul pulsante nell\'angolo in alto a destra
-   andare nella cartella Macro di FreeCAD (in FreeCAD, usare \"Modifica \> Preferenze \> Generale \> Macro per visualizzare il percorso di Macro)
-   se le impostazioni standard non sono state modificate, dovrebbe essere \"C:\\Users\\Your\_Windows\_User\_Name\\AppData\\Roaming\\FreeCAD\"
-   \\appdata è una cartella NASCOSTA, quindi potrebbe essere necessario modificare le impostazioni di Esplora file per vederla
-   creare una sottocartella chiamata \"FCGear\"
-   assicursi di copiare file e cartelle ESATTAMENTE come mostrato sopra nella sottocartella appena creata
-   riavviare FreeCAD e il workbench dovrebbe apparire nel menu a discesa
-   all\'interno di FreeCAD si può scegliere \"Strumenti\> Personalizza\> Ambienti\" per abilitare o disabilitare gli ambienti di lavoro

#### MacOSX

Vedere sopra le istruzioni per Linux


</div>


</div>

## Link all\'ambiente Gear 

-   Workbench Wiki: <https://github.com/looooo/FCGear/wiki>
-   FreeCAD Wiki: [Macro\_FCGear](http://www.freecadweb.org/wiki/index.php?title=Macro_FCGear) and [Bevel gear](http://forum.freecadweb.org/viewtopic.php?f=3&t=12878)
-   FreeCAD Forum: <http://forum.freecadweb.org/viewtopic.php?f=21&t=12968>
-   Tutorials:
-   Videos:
-   Files:
-   Report bugs: Please report bugs at <https://github.com/looooo/FCGear/issues>

## Altri link utili 


<div class="mw-translate-fuzzy">

-   <img alt="PartDesign\_InvoluteGear" src=images/PartDesign_InvoluteGear.svg  style="width:24px;"> [PartDesign InvoluteGear](PartDesign_InvoluteGear/it.md): questo strumento consente di creare un profilo 2D di un ingranaggio a spirale. Questo profilo 2D è completamente parametrico e può essere estruso con la funzione [PartDesign Pad](PartDesign_Pad/it.md).
-   [Ambienti esterni](External_workbenches/it.md): Un elenco di tutti gli ambienti di lavoro esterni correnti di FreeCAD
-   [Raccolta di macro](Macros_recipes/it.md)


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > FCGear Workbench/it
