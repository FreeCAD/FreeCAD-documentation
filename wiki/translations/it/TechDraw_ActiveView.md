---
 GuiCommand:
   Name: TechDraw ActiveView
   Name/it: TechDraw Vista attiva
   MenuLocation: TechDraw , Viste Da Altri Ambienti , Inserisci Vista attiva 
   Workbenches: TechDraw_Workbench/it
   Version: 0.19
   SeeAlso: TechDraw_Image/it
---

# TechDraw ActiveView/it



## Descrizione

Lo strumento **TechDraw Vista attiva** inserisce un\'immagine bitmap della finestra 3D attiva in una pagina di disegno.

![](images/TechDraw_ActiveView_example.png ) 
*Una vista semplice dal modello 3D.*



## Utilizzo

1.  Passare alla [Vista 3D](3D_view/it.md) corretta.
2.  Se nel documento sono presenti più pagine di disegno: facoltativamente selezionare la pagina desiderata nella [Vista ad albero](Tree_view/it.md).
3.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_ActiveView.svg" width=16px> [Inserisci Vista attiva (Vista 3D)](TechDraw_ActiveView/it.md)**.
    -   Seleziona l\'opzione **TechDraw → Viste Da Altri Ambienti → <img src="images/TechDraw_ActiveView.svg" width=16px> Inserisci Vista attiva (Vista 3D)** dal menu.
4.  Se nel documento sono presenti più pagine di disegno e non si ha ancora selezionato una pagina, si apre la finestra di dialogo **Scelta pagina**:
    1.  Selezionare la pagina desiderata.
    2.  Premere il pulsante **OK**.
5.  Si apre il pannello delle attività da **ActiveView a TD View**. Vedere [Opzioni](#Opzioni.md) per ulteriori informazioni.
6.  Premere il pulsante **OK**.



## Opzioni

È possibile specificare quanto segue:

-    **Ritaglia**: Ritaglia la bitmap generata.

-    **Larghezza**: La larghezza (in mm) per ritagliare la vista generata.

-    **Altezza**: L\'altezza (in mm) per ritagliare la vista generata.

-    **Nessuno sfondo**: Se selezionato, la bitmap generata avrà uno sfondo trasparente.

-    **Sfondo uniforme**: Se selezionato, il generato avrà uno sfondo del colore selezionato.

-    **Usa sfondo 3D**: Se selezionato, la bitmap generata utilizzerà lo sfondo della finestra 3D.



## Note

-   Le Viste attive sono statiche una volta generate e non vengono mai aggiornate con le modifiche al modello 3D.
-   Una Vista Attive dietro le quinte è una [Immagine](TechDraw_Image/it.md). Il suo **Scale Type** è quindi sempre inizializzato come {{Value|Custom}}.
-   In {{VersionMinus/it|0.20}} le Viste Attive erano un [Simbolo](TechDraw_Symbol/it.md).



## Proprietà

Vedere [TechDraw Immagine](TechDraw_Image/it#Properietà.md).





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ActiveView/it
