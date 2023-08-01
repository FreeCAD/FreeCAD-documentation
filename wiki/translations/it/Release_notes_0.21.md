# Release notes 0.21/it
**FreeCAD 0.21 è in fase di sviluppo, non è ancora prevista una data di rilascio.**


{{Message|
Mancano funzionalità? Menzionale nel thread del forum [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;69438 Release notes for v0.21].

Vedere [Help FreeCAD](Help_FreeCAD.md) per le modalità con cui contribuire a FreeCAD.
}}


{{Message|Tutte le immagini in questa pagina devono utilizzare il suffisso **_relnotes_0.21**}}


{{TOCright}}

**FreeCAD 0.21** è stato rilasciato il **DD MM 2023**, scaricalo dalla pagina [Download](Download/it.md). Questa pagina elenca tutte le nuove funzionalità e modifiche.

Le note di rilascio delle versioni precedenti di FreeCAD sono disponibili alla pagina [Funzionalità](Feature_list/it#Note_di_rilascio.md).

Segnaposto per un\'immagine accattivante selezionata dagli amministratori dal [forum delle vetrine degli utenti](https://forum.freecadweb.org/viewforum.php?f=24).



## Aspetti generali 



## Interfaccia utente 

   
  ![](images/Navi_Cube_relnotes_0.21.png )   Il [Cubo di navigazione](Navigation_Cube.md) è stato aggiornato. Il cubo non viene più mostrato in prospettiva se la [Vista 3D](3D_view/it.md) è in modalità di visualizzazione ortogonale. Le facce degli angoli sono state rese esagonali e più grandi in modo che siano più facili da cliccare. I bordi sono stati aggiunti intorno ai pulsanti. La selezione e il dimensionamento predefiniti dei caratteri sono stati migliorati. Il menu Mini-cubo ora include una casella di controllo per attivare o disattivare la mobilità del cubo. Sono stati aggiunti diversi nuovi parametri, vedere la pagina [Cubo di navigazione](Navigation_Cube/it.md) per ulteriori informazioni.[Pull request #7876](https://github.com/FreeCAD/FreeCAD/pull/7876), \[https ://github.com/FreeCAD/FreeCAD/pull/8266 Pull request n. 8266\], [Pull request n. 8646](https://github.com/FreeCAD/FreeCAD/pull/8646) e [/FreeCAD/FreeCAD/pull/9356 Pull request #9356](https://github.com).
   

+++
| <img alt="" src=images/Part_SectionCut_example_relnotes_0.21.gif  style="width:384px;">Sezione persistente di oggetti che si intersecano.Fare clic sull\'immagine per visualizzare l\'animazione. | Lo strumento [Taglio sezione persistente](Part_SectionCut/it.md) consente ora di tagliare oggetti che si intersecano. Ciò è utile per gli assiemi in cui a volte non è possibile evitare le intersezioni di oggetti a contatto a causa di problemi numerici. |
|                                                                                                                                                                                                                                               | [Pull request #8252](https://github.com/FreeCAD/FreeCAD/pull/8252).                                                                                                                                                                                                  |
+++

   
  <img alt="" src=images/Measurement-Part_relnotes_0.21.png  style="width:384px;">   Lo stile di visualizzazione dei risultati [misura](Part_Workbench#Measure.md) creati utilizzando l\'ambiente [Part](Part_Workbench/it.md) o [PartDesign](PartDesign_Workbench/it.md) può ora essere modificato nelle [preferenze](PartDesign_Preferences#Measure.md). [Richiesta pull n. 7148](https://github.com/FreeCAD/FreeCAD/pull/7148)
   

   
  <img alt="" src=images/WbSelector_relnotes_0.21.png  style="width:384px;">   Il selettore dell\'ambiente di lavoro può ora essere inserito facoltativamente nella barra dei menu anziché nell\'area della barra degli strumenti. [Pull request n. 7679](https://github.com/FreeCAD/FreeCAD/pull/7679)
   



### Ulteriori miglioramenti dell\'interfaccia utente 

-   I pulsanti per <img alt="" src=images/Std_Print.svg  style="width:24px;"> [Stampa](Std_Print/it.md) e <img alt="" src=images/Std_UserEditModeDefault.svg  style="width:24px;"> [Modalità modifica](Std_UserEditMode/it.md) sono stati rimossi dalla barra degli strumenti File. Possono essere aggiunti di nuovo [personalizzando](Std_DlgCustomize/it.md) la barra degli strumenti. [Pull request n. 7570](https://github.com/FreeCAD/FreeCAD/pull/7570) e [commit ea9a04e](https://github.com/FreeCAD/FreeCAD/commit/ea9a04e)
-   La barra degli strumenti File è stata divisa. I pulsanti per <img alt="" src=images/Std_Undo.svg  style="width:24px;"> [Annulla](Std_Undo/it.md), <img alt="" src=images/Std_Redo.svg  style="width:24px;"> [Ripristina](Std_Redo/it.md) e [24px ](Image:Std_Refresh.svg.md) [Aggiorna](Std_Refresh/it.md) sono stati spostati nella nuova barra degli strumenti Modifica. I pulsanti per <img alt="" src=images/Std_Cut.svg  style="width:24px;"> [Taglia](Std_Cut/it.md), <img alt="" src=images/Std_Copy.svg  style="width:24px;"> [Copia](Std_Copy/it.md) e [24px ](Image:Std_Paste.svg.md) [Incolla](Std_Paste/it.md) sono stati spostati nella nuova barra degli strumenti degli Appunti. Il pulsante per <img alt="" src=images/Std_WhatsThis.svg  style="width:24px;"> [Cos\'è?](Std_WhatsThis/it.md) è stato spostato nella nuova barra degli strumenti della Guida. [Pull request n. 7620](https://github.com/FreeCAD/FreeCAD/pull/7620)
-   Sono stati aggiunti comandi a [Memorizza](Std_StoreWorkingView/it.md) e [Richiama](Std_RecallWorkingView/it.md) una vista di lavoro temporanea. [Pull request n. 7525](https://github.com/FreeCAD/FreeCAD/pull/7525)
-   Le modifiche ai valori con la rotellina del mouse nei \"campi di input\" (un tipo di widget utilizzato per inserire valori nei pannelli delle attività, ad esempio da [Draft Linea](Draft_Line/it.md)) sono disabilitate se il widget non ha il focus e il parametro [ComboBoxWheelEventFilter](Fine-tuning#Mouse_related.md) è abilitato. Ciò impedisce modifiche di valore indesiderate durante lo scorrimento, come già accadeva per le caselle rotanti e combinate. [Pull request n. 7561](https://github.com/FreeCAD/FreeCAD/pull/7561)
-   Ora è possibile impostare una trasparenza predefinita per i nuovi oggetti [Part](Part_Module/it.md) o [PartDesign](PartDesign_Workbench/it.md) nelle [Preferenze](PartDesign_Preferences/it.md). [Pull request n. 7103](https://github.com/FreeCAD/FreeCAD/pull/7103)
-   C\'è il nuovo stile orbita **Piatto libero**. Può essere abilitato nelle [Preferenze](Preferences_Editor#Navigation.md) o premendo il pulsante **[<img src=images/NavigationCAD_dark.svg style="width:16px">** nella [Barra di stato](Status_bar/it.md) e poi utilizzando il menu **Impostazioni → Orbita**). [Pull request n. 8048](https://github.com/FreeCAD/FreeCAD/pull/8048)
-   Il pannello attività [Impostare l\'aspetto degli oggetti](Std_SetAppearance/it.md) ora ha anche un pulsante per impostare la proprietà Point Color. [Pull request n. 7708](https://github.com/FreeCAD/FreeCAD/pull/7708)
-   È stato aggiunto un pulsante per cambiare i colori del gradiente di sfondo [Vista 3D](3D_view/it.md) nelle [Preferences](Preferences_Editor#Colors.md). [Pull request n. 7155](https://github.com/FreeCAD/FreeCAD/pull/7155)
-   Tutte le impostazioni di trasparenza utilizzano ora il pulsante di rotazione uniforme del 5%: un clic sul pulsante in una finestra di dialogo o l\'[editor di proprietà](Property_editor/it.md) cambia la trasparenza del 5%. Tenere premuto il pulsante per modificare più passi del 5% contemporaneamente. [Pull request n. 7723](https://github.com/FreeCAD/FreeCAD/pull/7723)
-   La finestra Output è stata rinominata in Report per uniformità con l\'interfaccia utente. [Pull request n. 7739](https://github.com/FreeCAD/FreeCAD/pull/7739)
-   Image Workbench è stato rimosso. Per inserire un piano immagine è ora possibile utilizzare il comando [Importa](Std_Import/it.md). Fare doppio clic su un piano dell\'immagine per modificarne l\'orientamento e la scala. Il nuovo comando [Carica immagine](Std_ViewLoadImage/it.md) sostituisce il comando Apri immagine. [Pull request n. 8955](https://github.com/FreeCAD/FreeCAD/pull/8955)
-   Il deprecato ambiente di lavoro Raytracing è stato rimosso. Al suo posto dovrebbe essere usato [Render Workbench](https://github.com/FreeCAD/FreeCAD-render) esterno. [Pull request n. 9420](https://github.com/FreeCAD/FreeCAD/pull/9420)



## Sistema principale e API 



### Sistema principale 

-   La funzione **cbrt(x)** per le radici cubiche è stata aggiunta per l\'uso in [Espressioni](Expressions/it#Funzioni_esponenziali_e_logaritmiche.md). [Pull request n. 8629](https://github.com/FreeCAD/FreeCAD/pull/8629)
-   Molte nuove [Proprietà](Property/it#Tutti_i_tipi_di_proprietà.md) sono disponibili per lo scripting. [Pull request n. 6717](https://github.com/FreeCAD/FreeCAD/pull/6717)
-   Aggiunte funzioni di creazione oggetto {{Incode|vector}}, {{Incode|matrix}}, {{Incode|rotation}}, {{Incode|placement}} così come le funzioni di matrice {{Incode|mrotate}}, { {Incode\|mrotatex}}, {{Incode|mrotatey}}, {{Incode|mrotatez}}, {{Incode|mtranslate}} per l\'uso in [Espressioni](Expressions/it.md). [Pull request n. 8603](https://github.com/FreeCAD/FreeCAD/pull/8603).

### API


<div class="mw-collapsible mw-collapsed toccolours">



#### Nuove API Python 


<div class="mw-collapsible-content">

-   *BSplineSurfacePy::scaleKnotsToBounds*: Ridimensiona gli elenchi di nodi U e V per adattarli ai limiti specificati. [Pull request n. 7258](https://github.com/FreeCAD/FreeCAD/pull/7258) e [Richiesta pull n. 7385](https://github.com/FreeCAD/FreeCAD/pull/7385)
-   *BSplineCurvePy::scaleKnotsToBounds*: Ridimensiona l\'elenco dei nodi per adattarlo ai limiti specificati. [Pull request n. 7385](https://github.com/FreeCAD/FreeCAD/pull/7385)

-   *ShapeFix_EdgeConnectPy*: classe radice per le operazioni di correzione. [commit 4d4adb93](https://github.com/FreeCAD/FreeCAD/commit/4d4adb93)
-   *ShapeFix_EdgePy*: correzione del bordo non valido. [commit 4089cbfb](https://github.com/FreeCAD/FreeCAD/commit/4089cbfb)
-   *ShapeFix_FaceConnectPy*: Ricostruisce la connettività tra le facce nella shell. [commit a0eb2e9d](https://github.com/FreeCAD/FreeCAD/commit/a0eb2e9d)
-   *ShapeFix_FacePy*: Classe per correggere le operazioni sulle facce. [commit b6cd635c](https://github.com/FreeCAD/FreeCAD/commit/b6cd635c)
-   *ShapeFix_FixSmallFacePy*: Classe per operazioni di correzione sulle facce. [commit 4c2946c8](https://github.com/FreeCAD/FreeCAD/commit/4c2946c8)
-   *ShapeFix_FixSmallSolidPy*: correzione di solidi di piccole dimensioni. [commit b70d8d37](https://github.com/FreeCAD/FreeCAD/commit/b70d8d37)
-   *ShapeFix_FreeBoundsPy*: Destinato a produrre limiti liberi della forma. [commit 1ee1aee1](https://github.com/FreeCAD/FreeCAD/commit/1ee1aee1)
-   *ShapeFix_RootPy*: classe root per le operazioni di correzione. [commit f3e941a3](https://github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_ShapePy*: Classe per correggere operazioni sulle forme. [commit 87db9dcc](https://github.com/FreeCAD/FreeCAD/commit/87db9dcc)
-   *ShapeFix_ShapeTolerancePy*: Modifica le tolleranze delle sotto-forme (vertici, spigoli, facce). [commit 125d5b63](https://github.com/FreeCAD/FreeCAD/commit/125d5b63)
-   *ShapeFix_ShellPy*: classe radice per le operazioni di correzione. [commit f3e941a3](https://github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_SolidPy*: Classe principale per le operazioni di correzione. [commit 8d568793](https://github.com/FreeCAD/FreeCAD/commit/8d568793)
-   *ShapeFix_SplitCommonVertexPy*: Classe per correggere operazioni sulle forme. [commit 4b44c54c](https://github.com/FreeCAD/FreeCAD/commit/4b44c54c)
-   *ShapeFix_SplitToolPy*: Strumento per dividere e tagliare i bordi. [commit bbecc3f2](https://github.com/FreeCAD/FreeCAD/commit/bbecc3f2)
-   *ShapeFix_WireframePy*: Fornisce metodi per correggere il wireframe della forma. [commit 6843a461](https://github.com/FreeCAD/FreeCAD/commit/6843a461)
-   *ShapeFix_WirePy*: Classe per operazioni di correzione sulle polilinee. [commit 94f6279a](https://github.com/FreeCAD/FreeCAD/commit/94f6279a)
-   *ShapeFix_WireVertexPy*: Correzione dei bordi disconnessi nelle polilinee. [commit 8c6ffc99](https://github.com/FreeCAD/FreeCAD/commit/8c6ffc99)


</div>



#### Python API rimosse 

-   *FreeCAD.EndingAdd*: sostituito da *FreeCAD.addImportType*. [Pull request n. 7167](https://github.com/FreeCAD/FreeCAD/pull/7167)
-   *FreeCAD.EndingGet*: sostituito da *FreeCAD.getImportType*. [Pull request n. 7167](https://github.com/FreeCAD/FreeCAD/pull/7167)


</div>

## Addon Manager 



## Ambiente Arch 

-   Sono state aggiunte diverse categorie [Arch Profilo](Arch_Profile/it.md): IS RHS, IS SHS, IS Angle e IS Tee. [Pull request n. 7181](https://github.com/FreeCAD/FreeCAD/pull/7181) e [Pull request n. 7217](https://github.com/FreeCAD/FreeCAD/pull/7217)
-   Gli oggetti [Arch Profilo](Arch_Profile/it.md) ora supportano la modifica del tipo di profilo dopo la creazione. [Pull request n. 7217](https://github.com/FreeCAD/FreeCAD/pull/7217)
-   Diversi problemi relativi alla modalità di modifica sono stati risolti e i menu contestuali [Vista ad albero](Tree_view/it.md) per gli oggetti Arch sono stati migliorati. Gli oggetti che possono essere modificati ora hanno un\'opzione **Modifica** in quel menu. L\'opzione **Imposta colori** è stata rimossa per gli oggetti senza faccia o che possono avere solo una faccia. [Pull request n. 8122](https://github.com/FreeCAD/FreeCAD/pull/8122)
-   Gli oggetti [Arch Piano di sezione](Arch_SectionPlane/it.md) ora gestiscono gli oggetti non solidi allo stesso modo degli oggetti solidi. [Pull request n. 8688](https://github.com/FreeCAD/FreeCAD/pull/8688)



### Ulteriori miglioramenti Arch 

-   Lo strumento **Inverti posizione cerniera** è stato migliorato. Per tutte le polilinee rettangolari ora viene rilevato correttamente il bordo opposto. [Pull request n. 8199](https://github.com/FreeCAD/FreeCAD/pull/8199)
-   Il Terreno di un [Arch Sito](Arch_Site/it.md) ora può anche essere un solido. [Pull request n. 8409](https://github.com/FreeCAD/FreeCAD/pull/8409)
-   Un [Arch Sito](Arch_Site/it.md) non mostra più una rappresentazione fantasma degli oggetti nel suo Gruppo. [Pull request n. 8409](https://github.com/FreeCAD/FreeCAD/pull/8409)



## Ambiente Draft 

-   L\'imprecisione di [Draft Aggancia Vicino](Draft_Snap_Near/it.md) durante l\'aggancio (snap) alle curve è stata corretta. Inoltre, [Draft Aggancia Perpendicolare](Draft_Snap_Perpendicular/it.md) ora può anche eseguire l\'aggancio alle facce e trovare più punti. Per eseguire lo snap a un vertice (ad es. un [Draft Punto](Draft_Point/it.md)) [Draft Aggancia Punto finale](Draft_Snap_Endpoint/it.md) deve ora essere utilizzato invece di [Draft Aggancia Vicino](Draft_Snap_Near/it.md). [Pull request n. 7132](https://github.com/FreeCAD/FreeCAD/pull/7132)
-   Per facilitare il lavoro con i [layers](Draft_Layer/it.md), il loro comportamento di trascinamento è stato modificato. Se si rilascia un oggetto da un [Gruppo](Std_Group/it.md), o un oggetto simile a un gruppo come un [Arch Parte di edificio](Arch_BuildingPart/it.md), su un layer, non viene più rimosso dal gruppo e viceversa . Funziona senza tenere premuto il tasto **Ctrl**. [Pull request pull n. 7462](https://github.com/FreeCAD/FreeCAD/pull/7462)
-   Il comando [Draft Serie su punti](Draft_PointArray/it.md) ora supporta più tipi di oggetti punto. È possibile utilizzare qualsiasi oggetto con una forma e vertici, nonché una [mesh](Mesh_Workbench/it.md) e una [nuvola di punti](Points_Workbench/it.md). [Pull request n. 7597](https://github.com/FreeCAD/FreeCAD/pull/7597)
-   I menu contestuali [Vista ad albero](Tree_view/it.md) per gli oggetti Draft sono stati migliorati. Gli oggetti che possono essere modificati con il comando [Draft Modifica](Draft_Edit/it.md), o che hanno una soluzione di modifica dedicata, ora hanno un\'opzione **Modifica** in quel menu. L\'opzione **Imposta colori** è stata rimossa per gli oggetti senza faccia o che possono avere solo una faccia. [Pull request n. 7970](https://github.com/FreeCAD/FreeCAD/pull/7970)
-   Le proprietà degli oggetti di annotazione di Draft sono state unificate. Gli oggetti [Draft Testo](Draft_Text/it.md), [Draft Quota](Draft_Dimension/it.md) e [Draft Etichetta](Draft_Label/it.md) ora hanno tutti una proprietà Nome carattere, Dimensione carattere e Colore testo. Anche le opzioni della modalità di visualizzazione sono state rese coerenti e ora sono: Schermo e Mondo. [Issue #7861](https://github.com/FreeCAD/FreeCAD/issues/7861) e [Pull request #8081](https://github.com/FreeCAD/FreeCAD/pull/8081)
-   Nel pannello delle attività del comando [Draft Imposta stile](Draft_SetStyle/it.md) il pulsante **Texts/dims** è stato sostituito dal pulsante **Annotations**. La pressione di questo pulsante elaborerà tutte le annotazioni, incluse [Draft Etichette](Draft_Label/it.md). Sono stati aggiunti i parametri **Dim overshoot**, **Ext lines** e **Ext overshoot**. Sono stati risolti anche diversi problemi aggiuntivi minori. [Pull request n. 8190](https://github.com/FreeCAD/FreeCAD/pull/8190), [Pull request n. 8195](https://github.com/FreeCAD/FreeCAD/pull/8195), [.com/FreeCAD/FreeCAD/pull/8196 Pull request #8196](https://github)_e_[Pull_request_#9514](https://github.com/FreeCAD/FreeCAD/pull/9514).
-   Annulla/Ripristina non funzionava correttamente per i comandi di modifica di Draft su Windows. [Pull request n. 8267](https://github.com/FreeCAD/FreeCAD/pull/8267)
-   Il comando [LayerManager](Draft_LayerManager/it.md) è stato migrato dall\'ambiente BIM all\'ambiente Draft. [Pull request n. 8795](https://github.com/FreeCAD/FreeCAD/pull/8795)



### Ulteriori miglioramenti di Draft 

-   Quando si allineava il piano di lavoro con una faccia, veniva ruotato solo per corrispondere agli assi globali se la faccia era un quad. [Pull request n. 7249](https://github.com/FreeCAD/FreeCAD/pull/7249)
-   Diversi problemi relativi a [Draft Serie su tracciato](Draft_PathArray/it.md) sono stati risolti. [Pull request n. 7506](https://github.com/FreeCAD/FreeCAD/pull/7506) e [Pull request n. 7662](https://github.com/FreeCAD/FreeCAD/pull/7662)
-   Il comando [Draft Modifica](Draft_Edit/it.md) ha ricevuto diversi miglioramenti. Per [Polilinee](Draft_Wire/it.md), [B-spline](Draft_BSpline/it.md) e [Curve di Bézier](Draft_BezCurve/it.md) è stata aggiunta un\'opzione Chiudi/Apri al menu contestuale del bordo. Per le B-spline e le curve di Bézier è stata aggiunta allo stesso menu anche l\'opzione Inverti. I pannelli delle attività sono stati ripuliti. [Pull request n. 7527](https://github.com/FreeCAD/FreeCAD/pull/7527) e [Pull request n. 7541](https://github.com/FreeCAD/FreeCAD/pull/7541)
-   L\'uso di Esc per uscire da un comando non disattiva più la modalità continua. [Pull request n. 7611](https://github.com/FreeCAD/FreeCAD/pull/7611)
-   La barra degli strumenti [Draft Aggancia](Draft_Snap/it.md) è stata modificata in una barra degli strumenti standard. Le scorciatoie da tastiera ora possono essere assegnate agli agganci. Ma usarli durante un comando funziona solo se nessuna delle caselle di input nel pannello delle attività ha il focus mentre \"catturano\" le cosiddette scorciatoie in comando. [Pull request n. 7656](https://github.com/FreeCAD/FreeCAD/pull/7656)
-   Diversi bug di [Draft Stile delle annotazioni](Draft_AnnotationStyleEditor/it.md) sono stati corretti. Sono stati aggiunti i parametri **Colore testo** e **Spaziatura testo**. [Pull request n. 8207](https://github.com/FreeCAD/FreeCAD/pull/8207) e [Pull request n. 9702](https://github.com/FreeCAD/FreeCAD/pull/9702)
-   Le proprietà Start e End Offset sono state aggiunte agli oggetti [Draft Serie su tracciato](Draft_PathArray/it.md). [Pull request n. 8295](https://github.com/FreeCAD/FreeCAD/pull/8295)
-   Una proprietà Count è stata aggiunta alle serie prive di questa proprietà: le versioni non-Link di [Draft Serie ortogonale](Draft_OrthoArray/it.md), [Draft Serie polare](Draft_PolarArray/it.md) e [Draft Serie circolare](Draft_CircularArray/it.md). [Pull request n. 8433](https://github.com/FreeCAD/FreeCAD/pull/8433)
-   Il comportamento on/off della [griglia](Draft_Snap_Grid/it.md) è stato corretto. [Pull request n. 8818](https://github.com/FreeCAD/FreeCAD/pull/8818)
-   La gestione dei convertitori DWG è stata migliorata. [Pull request n. 9444](https://github.com/FreeCAD/FreeCAD/pull/9444) e [Pull request #9830](https://github.com/FreeCAD/FreeCAD/pull/9830)



## Ambiente FEM 

   
  <img alt="" src=images/FEM_PostFilterContours_relnotes_0.21.png  style="width:384px;">Iso-contorni, raffiguranti la componente y della densità del flusso magnetico assoluto all\'interno e intorno a un filo di rame attraversato \>corrente elettrica a una frequenza di 100 kHz.Per maggiori informazioni su questo modello, vedere la sezione 14 del [Elmer Tutorials](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   C\'è il nuovo filtro <img alt="" src=images/FEM_PostFilterContours.svg  style="width:24px;"> [Contours filter](FEM_PostFilterContours.md) che permette di disegnare isolinee o isocontorni. Gli iso-contorni sono nodi mesh collegati che hanno lo stesso valore del campo risultato. Un tipico esempio sono le linee di campo elettrico. [Pull request n. 8462](https://github.com/FreeCAD/FreeCAD/pull/8462)
   

   
  <img alt="" src=images/FEM_Elmer-Multithread_relnotes_0.21.png  style="width:384px;">Risultato della simulazione (dell\'acqua corrente che viene riscaldata) in cui sono visibili 8 regioni mesh (una per ogni core della CPU utilizzato).   Ora è possibile eseguire il risolutore [Elmer](FEM_SolverElmer/it.md) utilizzando più core della CPU. Per maggiori informazioni sugli avvertimenti, vedere [questo post del forum](https://forum.freecadweb.org/viewtopic.php?p=610617#p610617) [Pull request pull n. 7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
   

   
  <img alt="" src=images/FEM_EquationMagnetodynamic2D_relnotes_0.21.png  style="width:300px;">Risultato della simulazione della parte immaginaria della densità di corrente inun crogiolo riscaldato elettricamente da una bobina circostante.Questo modello è disponibile tramite [Esempi FEM](FEM_Examples/it.md).Per maggiori informazioni su questo modello, vedere la sezione 16 di [Tutorial Elmer](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   La <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:24px;"> [Equazione magnetodinamica 2D](FEM_EquationMagnetodynamic2D/it.md) è stata aggiunta. Con questo è possibile eseguire simulazioni elettromagnetiche in 2D. [Pull request n. 8355](https://github.com/FreeCAD/FreeCAD/pull/8355)
   

   
  <img alt="" src=images/FEM_EquationMagnetodynamic_relnotes_0.21.png  style="width:384px;">Risultato della simulazione della parte immaginaria della densità del flusso magnetico dentroe attorno a un filo di rame attraversato da corrente elettrica a una frequenza di 100 kHz.Questo modello è disponibile tramite [Esempi FEM](FEM_Examples/it.md).Per maggiori informazioni su questo modello, vedere la sezione 14 di \[<https://www.nic>. funet.fi/index/elmer/doc/ElmerTutorials.pdf Elmer Tutorials\].   La <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:24px;"> [Equazione magnetodinamica](FEM_EquationMagnetodynamic/it.md) è stata aggiunta. Con questo è possibile eseguire simulazioni elettromagnetiche. [Pull request n. 8380](https://github.com/FreeCAD/FreeCAD/pull/8380)
   

   
  <img alt="" src=images/FEM_EquationDeformation_relnotes_0.21.png  style="width:384px;">Risultato della simulazione di un filo a U di ferro che viene deformatopremendo insieme le estremità della U.Per ulteriori informazioni a riguardo modello, vedere la sezione 8 dei [Elmer Tutorials](https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf).   La <img alt="" src=images/FEM_EquationDeformation.svg  style="width:24px;"> [Equazione di deformazione](FEM_EquationDeformation/it.md) è stata aggiunta. Con questo è possibile eseguire analisi di elasticità non lineare (deformazione). [Pull request n. 8981](https://github.com/FreeCAD/FreeCAD/pull/8981)
   



### Ulteriori miglioramenti di FEM 

-   Quando si eseguono analisi utilizzando il <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> [risolutore CalculiX](FEM_SolverCalculixCxxtools/it.md), ora c\'è anche una [results pipeline](FEM_PostPipelineFromResult/it.md) creata per visualizzare i risultati. [Pull request n. 8525](https://github.com/FreeCAD/FreeCAD/pull/8525) e [Pull request n. 8903](https://github.com/FreeCAD/FreeCAD/pull/8903)
-   Ora è possibile eseguire [analisi transitorie](FEM_SolverElmer_SolverSettings/it#Timestepping_(transient_analyses).md) quando si utilizza il <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [risolutore Elmer](FEM_SolverElmer/it.md). [Pull request n. 9056](https://github.com/FreeCAD/FreeCAD/pull/9056)
-   Il <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [vincolo di pressione iniziale](FEM_ConstraintInitialPressure/it.md) è stato aggiunto per impostare la pressione interna iniziale dei fluidi. [Pull request n. 7364](https://github.com/FreeCAD/FreeCAD/pull/7364)
-   Il <img alt="" src=images/FEM_ConstraintCurrentDensity.svg  style="width:24px;"> [vincolo di densità corrente](FEM_ConstraintCurrentDensity/it.md) è stato aggiunto per impostare le densità correnti per corpi e facce. [Pull request n. 8348](https://github.com/FreeCAD/FreeCAD/pull/8348)
-   Il <img alt="" src=images/FEM_ConstraintMagnetization.svg  style="width:24px;"> [vincolo di magnetizzazione](FEM_ConstraintMagnetization/it.md) è stato aggiunto per impostare le magnetizzazioni per corpi e facce. [Pull request n. 8393](https://github.com/FreeCAD/FreeCAD/pull/8393)
-   Il <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:24px;"> [vincolo di velocità del flusso](FEM_ConstraintFlowVelocity/it.md) e <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:24px;"> [vincolo di velocità del flusso iniziale](FEM_ConstraintInitialFlowVelocity/it.md) sono stati completamente riscritti. Ora è anche possibile specificare una velocità tramite una formula matematica (per definire un profilo di velocità). [Pull request n. 8963](https://github.com/FreeCAD/FreeCAD/pull/8963) e [Pull request n. 8964](https://github.com/FreeCAD/FreeCAD/pull/8964)**Nota:** Questa è una modifica importante. Le analisi con la velocità del flusso esistente e i vincoli di velocità del flusso iniziale non funzioneranno più. È necessario creare nuovi vincoli di velocità del flusso nell\'analisi per far funzionare le analisi esistenti.**Nota inoltre:** fino a FreeCAD 0.21 i risultati del risolutore di flusso erano errati (densità e viscosità del fluido erano un fattore 1000 troppo alto). Pertanto la necessaria ricreazione del vincolo di velocità assicura anche che i risultati saranno corretti.
-   È ora possibile definire nei <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:24px;"> [vincoli di spostamento](FEM_ConstraintDisplacement/it.md) gli spostamenti come equazioni (spostamento in base al tempo corrente del risolutore).
-   Il <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:24px;"> [vincolo della fonte di calore corporeo](FEM_ConstraintBodyHeatSource/it.md) ha ora un pannello delle attività ed è possibile impostare il calore per diversi corpi o utilizzare diversi vincoli per diversi corpi in un\'unica analisi . [Pull request n. 7367](https://github.com/FreeCAD/FreeCAD/pull/7367)
-   Il <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:24px;"> [vincolo a molla](FEM_ConstraintSpring/it.md) non è stato utilizzato da nessun risolutore. Ora può essere utilizzato dal risolutore [Elmer](FEM_SolverElmer/it.md) tramite le equazioni [Deformazione](FEM_EquationDeformation/it.md) e [Elasticity](FEM_EquationElasticity/it.md). [Pull request n. 9005](https://github.com/FreeCAD/FreeCAD/pull/9005)
-   È stata aggiunta la funzione di taglio mesh risultante <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> [Filter function cylinder](FEM_PostCreateFunctionCylinder/it.md). [Pull request n. 8735](https://github.com/FreeCAD/FreeCAD/pull/8735)
-   È stata aggiunta la funzione di taglio mesh dei risultati <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:24px;"> [Filter function box](FEM_PostCreateFunctionBox/it.md). [Pull request n. 8825](https://github.com/FreeCAD/FreeCAD/pull/8825)
-   Ora è possibile aprire (e quindi visualizzare) file \*.pvtu (dati di griglia non strutturati VTK partizionati). Un file \*.pvtu è anche il risultato di una simulazione [Elmer](FEM_SolverElmer/it.md), quando per i calcoli viene utilizzato più di un core della CPU. [Pull request n. 7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
-   Il rapporto di deformazione critica è stato aggiunto alla pipeline dei risultati VTK. Fornisce un\'indicazione della rottura duttile per i materiali con un oggetto \"MaterialMechanicalNonlinear\". [Pull request n. 7467](https://github.com/FreeCAD/FreeCAD/pull/7467)
-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:24px;"> [FEM mesh to mesh](FEM_FemMesh2Mesh/it.md) ha il nuovo parametro *scale* per definire la scala della mesh deformata usando Python. [Discussione del forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=71936) e [Pull request n. 7715](https://github.com/FreeCAD/FreeCAD/pull/7715)
-   Le [preferences](FEM_Preferences/it.md) hanno una nuova opzione per definire quale solutore deve essere aggiunto automaticamente quando si crea una nuova analisi.
-   Miglioramenti dell\'usabilità:
    -   Se ci si trova nell\'ambiente FEM durante il caricamento di un file di FreeCAD contenente un\'analisi, l\'analisi viene attivata automaticamente (si ha accesso immediato a tutti i pulsanti della barra degli strumenti FEM).
    -   La barra degli strumenti ha solo pulsanti per i risolutori installati sul tuo sistema. I risolutori non disponibili non vengono più visualizzati.
-   Nuovi file di esempio per le seguenti equazioni sono disponibili tramite [FEM Examples](FEM_Examples/it.md): [Deformation](FEM_EquationDeformation/it.md), [Flow](FEM_EquationFlow/it.md), [Flux](FEM_EquationFlux/it.md), [Heat](FEM_EquationHeat/it.md), [Magnetodynamic](FEM_EquationMagnetodynamic/it.md) e [Magnetodynamic 2D](FEM_EquationMagnetodynamic2D/it.md). Pull request [#8550](https://github.com/FreeCAD/FreeCAD/pull/8550), [#8569](https://github.com/FreeCAD/FreeCAD/pull/8569), [/FreeCAD/FreeCAD/pull/8579 #8579](https://github.com), [#8597](https://github.com/FreeCAD/FreeCAD/pull/8597), [#8630](https://github.com/FreeCAD/FreeCAD/pull/8630) e [#9004](https://github.com/FreeCAD/FreeCAD/pull/9004).
-   Nuova scheda materiale per l\'anidride carbonica e una lega di titanio. [Pull request n. 8332](https://github.com/FreeCAD/FreeCAD/pull/8332) e [Pull request n. 8636](https://github.com/FreeCAD/FreeCAD/pull/8636)



## Esportazione

## Mesh



### Ulteriori miglioramenti di Mesh 

-   Supporto per aggiungere trasparenze a una mesh. [Thread del forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=72531) e [Commit f88305e](https://github.com/FreeCAD/FreeCAD/commit/f88305e)



## Ambiente OpenSCAD 



## Ambiente Part 



### Ulteriori miglioramenti di Part 

-   Il comando [Part Crea punti da mesh](Part_PointsFromMesh/it.md) è stato esteso per accettare qualsiasi oggetto geometrico come input. [Pull request n. 8730](https://github.com/FreeCAD/FreeCAD/pull/8730)



## Ambiente PartDesign 

   
  <img alt="" src=images/PD_Counterdrill_relnotes_0.21.png  style="width:384px;">Un controforo.   La finestra di dialogo [Foro](PartDesign_Hole/it.md) supporta il tipo di testa della vite *Contropunta*. [Pull request n. 7562](https://github.com/FreeCAD/FreeCAD/pull/7562)
                                                                                                                        
   

   
  <img alt="" src=images/PartDesign_task_dialog_relnotes_0.21.png  style="width:384px;">   L\'esperienza utente su più finestre di dialogo delle attività di PartDesign per la selezione delle geometrie è stata migliorata, ora non richiede più l\'uso di pulsanti separati per aggiungere o rimuovere geometrie alla selezione. [Pull request n. 8990](https://github.com/FreeCAD/FreeCAD/pull/8990)
                                                                                                          
   



### Ulteriori miglioramenti di PartDesign 

-   Nella finestra di dialogo [Foro](PartDesign_Hole/it.md), i tipi di testa della vite obsoleti (testa di formaggio, vite a testa cilindrica ecc.) sono stati rimossi. Sono stati deprecati da FreeCAD 0.19. I fori che utilizzano questi tipi vengono trasformati in svasature/fori svasati personalizzati con il diametro e la profondità utilizzati dai tipi. [Pull request n. 7654](https://github.com/FreeCAD/FreeCAD/pull/7654)
-   Nelle finestre di dialogo [Loft additivo](PartDesign_AdditiveLoft/it.md) e [Loft sottrattivo](PartDesign_SubtractiveLoft/it.md), l\'opzione precedentemente non funzionante **Chiuso** ora crea un loft chiuso (come un anello). [Pull request n. 8748](https://github.com/FreeCAD/FreeCAD/pull/8748)
-   Il comando [Convalida schizzo](Sketcher_ValidateSketch/it.md) è stato aggiunto alla barra degli strumenti Helper. [Pull request n. 7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   I comandi inutilizzabili [Lascia schizzo](Sketcher_LeaveSketch/it.md) e [Visualizza schizzo](Sketcher_ViewSketch/it.md) sono stati rimossi dal menu. I comandi [Modifica schizzo](Sketcher_EditSketch/it.md), [Unisci schizzi](Sketcher_MergeSketches/it.md) e [Specchia schizzo](Sketcher_MirrorSketch/it.md) sono stati aggiunti al menu. [Pull request n. 7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   Il [profilo ingranaggio evolvente](PartDesign_InvoluteGear/it.md) ha nuove proprietà per modificare la lunghezza del dente. Ciò ora consente di apportare modifiche a determinati tipi di interferenze e di utilizzare il profilo anche per creare [involute splines](https://en.wikipedia.org/wiki/Spline_(mechanical)). [Pull request n. 8184](https://github.com/FreeCAD/FreeCAD/pull/8184)
-   Il [profilo dell\'ingranaggio ad evolvente](PartDesign_InvoluteGear/it.md) ora offre la possibilità di spostamento del profilo. [Issue #5618](https://github.com/FreeCAD/FreeCAD/issues/5618) e [Pull request #8934](https://github.com/FreeCAD/FreeCAD/pull/8934)
-   Quando si crea un [Clone](PartDesign_Clone/it.md) ora erediterà i colori dell\'oggetto clonato. [Pull request n. 9547](https://github.com/FreeCAD/FreeCAD/pull/9547)



## Ambiente Path 

-   Integrazione Camotics. Se è installato camotics (versione 1.2.2 o successiva), verrà aggiunta una nuova icona alla barra degli strumenti Percorso. Selezionare un percorso di lavoro e premere il pulsante per aprire la finestra di dialogo Camotics. Quindi trascinare il cursore per generare un solido simulato in qualsiasi punto del lavoro. Si può anche avviare l\'applicazione Camotics completa per eseguire la simulazione animata. Ciò si traduce in una post-elaborazione silenziosa del lavoro e nella creazione di un file di progetto camotics. [Pull request n. 6637](https://github.com/FreeCAD/FreeCAD/pull/6637)

-   Stringhe di sostituzione aggiuntive per la denominazione automatica dell\'output. Se l\'output viene suddiviso in più file, i nomi file possono sostituire automaticamente l\'etichetta toolcontroller, Work Coordinate Systems (WCS) o l\'etichetta operazione. Questo è in aggiunta alle altre stringhe di sostituzione esistenti come data, nome del lavoro, ecc.

-   Opzione rompitruciolo implementata per i cicli di foratura peck. La rottura del truciolo emette un ciclo G73 che fa sì che il controllo esegua un movimento di retrazione molto piccolo per rompere il truciolo senza ritrarre completamente la punta dal foro. G73 è supportato nativamente da LinuxCNC. Alcuni altri postprocessori dovranno interpretare il G73 ed emettere codici di controllo appropriati o scomporre la retrazione in mosse G1/G0. Il supporto del postprocessore per la scomposizione G73 è stato aggiunto ai postprocessori \"refactored\".[Pull request #7469](https://github.com/FreeCAD/FreeCAD/pull/7469)



## Modulo Plot 



## Ambiente Sketcher 

   
  <img alt="" src=images/Constrain_B-spline_knots_relnotes_0.21.gif  style="width:384px;">Trascinamento dei nodi B-spline.Fare clic sull\'immagine per vedere l\'animazione.   I nodi B-spline ora possono essere trascinati e vincolati come qualsiasi altro punto dello schizzo. [Pull request n. 7484](https://github.com/FreeCAD/FreeCAD/pull/7484)
                                                                                                                                                                                                                            
   

   
  <img alt="" src=images/sketcher-move-piece_relnotes_0.21.gif  style="width:384px;">Trascinamento di una B-spline.Fare clic sull\'immagine se l\'animazione non si avvia.   Il trascinamento di una B-spline ora sposta solo la parte tra i nodi. [Pull request n. 7110](https://github.com/FreeCAD/FreeCAD/pull/7110)
                                                                                                                                                                                                                     
   

   
  <img alt="" src=images/Sketcher_Join_Curves_relnotes_0.21.gif  style="width:384px;">Fare clic sull\'immagine per vedere l\'animazione.   È stato aggiunto lo strumento [Unisci curve](Sketcher_JoinCurves/it.md). Può combinare due curve in un\'unica B-spline. [Pull request n. 6507](https://github.com/FreeCAD/FreeCAD/pull/6507)
                                                                                                                                                                      
   

   
  <img alt="" src=images/Sketcher_BackEdit_relnotes_0.21.gif  style="width:384px;">Fare clic sull\'immagine per vedere l\'animazione.   Ora gli schizzi possono essere modificati senza problemi dalla parte anteriore o posteriore. Quando si lavora dal retro, i vertici (e tutte le geometrie e i vincoli) sono ugualmente selezionabili e la vista in sezione viene cambiata automaticamente. [Pull request n. 7417](https://github.com/FreeCAD/FreeCAD/pull/7417)
                                                                                                                                                                
   

   
  <img alt="" src=images/Sketcher_Grid_Rework_relnotes_0.21.png  style="width:384px;">   La griglia di Sketcher è stata rielaborata. Lo strumento [Griglia](Sketcher_Grid/it.md) è stato aggiunto. È stata aggiunta l\'opzione di ridimensionamento automatico della griglia. [Pull request n. 8473](https://github.com/FreeCAD/FreeCAD/pull/8473)
                                                                                                      
   

   
  <img alt="" src=images/Sketcher_Constraint_Widget_relnotes_0.21.png  style="width:384px;">   Il widget Sketcher Constraint è stato rielaborato per semplificare l\'interfaccia utente. [Pull request n. 7566](https://github.com/FreeCAD/FreeCAD/pull/7566)
                                                                                                                  
   

   
  <img alt="" src=images/Sketcher_Element_Widget_relnotes_0.21.gif  style="width:384px;">Fare clic sull\'immagine per vedere l\'animazione.   Il widget Elemento è stato rielaborato per semplificare l\'interfaccia utente e consentire una selezione più semplice delle diverse parti di ciascuna geometria: bordo, punto iniziale, punto finale e punto medio. [Pull request n. 7567](https://github.com/FreeCAD/FreeCAD/pull/7567)
                                                                                                                                                                            
   

   
  <img alt="" src=images/Sketcher_Grid_relnotes_0.21.gif  style="width:384px;">   Sono state introdotte una funzionalità per ridimensionare automaticamente la griglia in base al livello di zoom e altri miglioramenti. [Pull request n. 8473](https://github.com/FreeCAD/FreeCAD/pull/8473)
                                                                                        
   

   
  <img alt="" src=images/Sketcher_layers_relnotes_0.21.gif  style="width:384px;">   È stata introdotta la funzionalità dei livelli visivi di base, per ora sono supportati solo 3 livelli codificati. Aspettatevi ulteriori miglioramenti lungo la strada. Questa PR rimuove anche il widget \"Modifica controlli\" dal pannello delle attività poiché tutto il suo contenuto è stato spostato in altre posizioni o rimosso. Le opzioni dell\'ordine di rendering sono state spostate nella barra degli strumenti di modifica di Sketcher. [Pull request n. 8716](https://github.com/FreeCAD/FreeCAD/pull/8716) e [Pull request n. 9590](https://github.com/FreeCAD/FreeCAD/pull/9590)
                                                                                            
   

   
  <img alt="" src=images/Sketcher_Circle2CircleConstraint_relnotes_0.21.png  style="width:384px;">   È stato introdotto [vincolo di distanza](Sketcher_ConstrainDistance/it.md) da cerchio a cerchio. [Pull request n. 8896](https://github.com/FreeCAD/FreeCAD/pull/8896)
                                                                                                                              
   

   
  <img alt="" src=images/Sketcher_Circle2LineConstraint_relnotes_0.21.png  style="width:384px;">   È stato introdotto [vincolo di distanza](Sketcher_ConstrainDistance/it.md) da cerchio a linea. [Pull request n. 9044](https://github.com/FreeCAD/FreeCAD/pull/9044)
                                                                                                                          
   

   
  <img alt="" src=images/Sketcher-snap2_relnotes_0.21.gif  style="width:384px;">Fare clic sull\'immagine per vedere l\'animazione.   Sono stati aggiunti Snap Manager, snap ad angolo e snap al punto medio. [Pull request n. 8387](https://github.com/FreeCAD/FreeCAD/pull/8387)
                                                                                                                                                          
   

   
  <img alt="" src=images/Sketcher-concentric_relnotes_0.21.gif  style="width:384px;">   [Vincolo coincidente](Sketcher_ConstrainCoincident/it.md) ora può fungere da vincolo concentrico quando si selezionano 2 o più cerchi, archi, ellissi o archi di ellissi. [Pull request n. 7703](https://github.com/FreeCAD/FreeCAD/pull/7703)
                                                                                                    
   

   
  <img alt="" src=images/Sketcher-B-spline_by_knots_v2_relnotes_0.21.gif  style="width:384px;">   Lo strumento [B-spline per nodi](Sketcher_CreateBSplineByInterpolation/it.md) è stato aggiunto. [Pull request n. 8530](https://github.com/FreeCAD/FreeCAD/pull/8530)
                                                                                                                        
   

   
  <img alt="" src=images/Sketcher-periodic_B-spline_by_knots_v2_relnotes_0.21.gif  style="width:384px;">   Lo strumento [B-spline periodico per nodi](Sketcher_CreatePeriodicBSplineByInterpolation/it.md) è stato aggiunto. [Pull request n. 8530](https://github.com/FreeCAD/FreeCAD/pull/8530)
                                                                                                                                          
   



### Ulteriori miglioramenti di Sketcher 

-   Il pulsante della barra degli strumenti per [Vincola rifrazione (legge di Snell)](Sketcher_ConstrainSnellsLaw/it.md) è stato rimosso. [Commit ef62fc3](https://github.com/FreeCAD/FreeCAD/commit/ef62fc3)
-   [Split](Sketcher_Split/it.md) ora supporta più curve (ellissi, parabole, iperboli e B-spline). [Pull request n. 6971](https://github.com/FreeCAD/FreeCAD/pull/6971)
-   Le [Vincoli dimensionali](Sketcher_Workbench/it#Vincoli_dimensionali.md) e le Spin Box di quantità ora supportano la stessa matematica delle [Espressioni](Expressions/it.md) (Valutate sul posto). [Pull request n. 7124](https://github.com/FreeCAD/FreeCAD/pull/7124)
-   I pulsanti della barra degli strumenti per [Seleziona vincoli ridondanti](Sketcher_SelectRedundantConstraints/it.md) e [Seleziona vincoli in conflitto](Sketcher_SelectConflictingConstraints/it.md) sono stati rimossi. [Pull request n. 7568](https://github.com/FreeCAD/FreeCAD/pull/7568)
-   Il pulsante della barra degli strumenti per [Interrompi operazione](Sketcher_StopOperation/it.md) è stato rimosso. [Pull request n. 7569](https://github.com/FreeCAD/FreeCAD/pull/7569)
-   Il pulsante della barra degli strumenti per [Select unconstrained DoF](Sketcher_SelectElementsWithDoFs/it.md) è stato rimosso. [Pull request n. 7603](https://github.com/FreeCAD/FreeCAD/pull/7603)
-   La barra degli strumenti di Sketcher è stata divisa in due: \'Sketcher-edit-mode\' e \'Sketcher\' (ovvero \'modalità non modifica\'). Le barre degli strumenti di Sketcher che sono solo per la modalità di modifica sono nascoste in modalità non di modifica e quelle solo per la modalità non di modifica sono nascoste in modalità di modifica. Anche la barra degli strumenti Struttura è nascosta in Sketcher. [Pull request n. 7655](https://github.com/FreeCAD/FreeCAD/pull/7655)
-   [Copia carbone](Sketcher_CarbonCopy/it.md), se possibile, ora utilizza i nomi dei vincoli nelle espressioni che crea invece di un riferimento basato sull\'indice, rendendolo più affidabile. [Pull request n. 7688](https://github.com/FreeCAD/FreeCAD/pull/7688)
-   Lo strumento Vincola allineamento interno è stato rimosso. Era obsoleto dall\'introduzione dello strumento [Mostra/nascondi geometria interna](Sketcher_RestoreInternalAlignmentGeometry/it.md). [Pull request n. 8863](https://github.com/FreeCAD/FreeCAD/pull/8863)
-   La casella delle attività \"Messaggio risolutore\" di Sketcher è stata semplificata. La casella di controllo auto-rimozione-ridondante è stata spostata nel menu del pulsante di impostazione della casella delle attività Vincolo. La casella di controllo dell\'aggiornamento automatico è stata spostata nel menu del pulsante di aggiornamento. [Pull request n. 8864](https://github.com/FreeCAD/FreeCAD/pull/8864)



## Ambiente Spreadsheet 



### Ulteriori miglioramenti di Spreadsheet 



## Ambiente Surface 

   
  <img alt="" src=images/Surface_BlendCurve_relnotes_0.21.png  style="width:250px;">   È stato aggiunto lo strumento [Blend Curve](Surface_BlendCurve/it.md). [Pull request n. 7339](https://github.com/FreeCAD/FreeCAD/pull/7339)
                                                                                                  
   



## Ambiente TechDraw 

   
  <img alt="" src=images/TechDraw_SurfaceFinishExample_relnotes_0.21.png  style="width:250px;">             Lo strumento [SurfaceFinishSymbol](TechDraw_SurfaceFinishSymbol/it.md) è stato aggiunto per consentire la creazione di simboli di finitura superficiale che descrivono rugosità, deposizione e ondulazione, ma denotano anche il tipo di trattamento superficiale. Supporta entrambi gli stili ISO e ASME. Come mostrato nell\'immagine, lo strumento [Linea guida](TechDraw_LeaderLine/it.md) esistente può essere utilizzato per riferire correttamente i simboli orientati ai bordi di un oggetto. [Pull request n. 7227](https://github.com/FreeCAD/FreeCAD/pull/7227)
  <img alt="" src=images/TechDraw_ComplexSection_relnotes_0.21.png  style="width:250px;">                         Lo strumento [ComplexSection](TechDraw_ComplexSection/it.md) è stato aggiunto per consentire la creazione di metà sezioni, sfalsate e allineate. [Pull request n. 7658](https://github.com/FreeCAD/FreeCAD/pull/7658)
  <img alt="" src=images/TechDraw_HoleShaftFitExample_relnotes_0.21.png  style="width:250px;">               Lo strumento [HoleShaftFit](TechDraw_HoleShaftFit/it.md) è stato aggiunto. [Pull request n. 8455](https://github.com/FreeCAD/FreeCAD/pull/8455)
  <img alt="" src=images/TechDraw_AxoLengthDimensionExample_relnotes_0.21.png  style="width:250px;">   Lo strumento [AxoLengthDimension](TechDraw_AxoLengthDimension/it.md) è stato aggiunto. [Pull request n. 8359](https://github.com/FreeCAD/FreeCAD/pull/8359)
                                                                                                                                  
   



### Ulteriori miglioramenti di TechDraw 

-   Le modalità di navigazione sono state aggiornate per corrispondere a quelle utilizzate nella vista 3D. [Pull request n. 7081](https://github.com/FreeCAD/FreeCAD/pull/7081) e [Pull request n. 7107](https://github.com/FreeCAD/FreeCAD/pull/7107)
-   Il tratteggio bitmap è stato risolto. [Issue #6582](https://github.com/FreeCAD/FreeCAD/issues/6582) e [Pull request #7121](https://github.com/FreeCAD/FreeCAD/pull/7121)
-   È stato aggiunto il supporto per gli spazi regolabili per le linee di estensione di [quote](TechDraw_Preferences/it#Quote.md). [Pull request n. 7133](https://github.com/FreeCAD/FreeCAD/pull/7133)
-   È stato introdotto il multithreading per la rimozione delle linee nascoste e la ricerca delle facce. [Pull request n. 7377](https://github.com/FreeCAD/FreeCAD/pull/7377)
-   L\'algoritmo di rilevamento delle facce è stato migliorato. [Pull request n. 7448](https://github.com/FreeCAD/FreeCAD/pull/7448)
-   È stato aggiunto lo strumento [PrintAll](TechDraw_PrintAll/it.md). [Pull request n. 7460](https://github.com/FreeCAD/FreeCAD/pull/7460)
-   Sono stati aggiunti [Quattro strumenti](TechDraw_StackGroup/it.md) per controllare l\'ordine di sovrapposizione delle viste. [Issue #6012](https://github.com/FreeCAD/FreeCAD/issues/6012) e [Pull request #7460](https://github.com/FreeCAD/FreeCAD/pull/7460)
-   [ActiveView](TechDraw_ActiveView/it.md) ora crea un\'acquisizione dello schermo anziché un\'immagine SVG. [Pull request n. 7471](https://github.com/FreeCAD/FreeCAD/pull/7471)
-   Tutti i modelli di caratteri latini sono stati convertiti in \"plain svg\". [Pull request n. 7472](https://github.com/FreeCAD/FreeCAD/pull/7472)
-   È stata aggiunta un\'anteprima al pannello delle attività dello strumento [SectionView](TechDraw_SectionView/it.md). [Pull request n. 7658](https://github.com/FreeCAD/FreeCAD/pull/7658)
-   Le funzioni DrawViewPart obsolete sono state rimosse: replaceCenterLine, replaceCosmeticEdge, replaceCosmeticVertex e replaceGeomFormat.
-   Le quote 3D ora possono essere create allo stesso modo delle quote 2D (a parte il fatto che la geometria deve essere selezionata in una vista 3D). Ciò elimina la necessità di collegarli manualmente alla geometria 3D. [Pull request n. 8141](https://github.com/FreeCAD/FreeCAD/pull/8141)
-   È stato aggiunto lo strumento [DimensionRepair](TechDraw_DimensionRepair/it.md). [Pull request n. 8141](https://github.com/FreeCAD/FreeCAD/pull/8141)
-   È stata aggiunta una funzione per rimuovere i bordi sovrapposti restituiti dall\'algoritmo di rimozione delle linee nascoste, inclusa una nuova impostazione (nelle preferenze avanzate) per il numero di passaggi di questa funzione. [Pull request n. 9280](https://github.com/FreeCAD/FreeCAD/pull/9280)

## Web



## Ambienti esterni 

### A2plus

### Assembly3

### Assembly4

### FCGear

### Ship



## Compilazione

Da questa versione FreeCAD può essere compilato solo utilizzando Qt 5.xe Python 3.x. La versione Qt più bassa supportata è 5.12, la versione Python supportata più bassa è 3.8.

Per compilare FreeCAD vedere le istruzioni per [Windows](Compile_on_Windows/it.md), [Linux](Compile_on_Linux/it.md) e [macOS](Compile_on_MacOS/it.md).

I sistemi operativi supportati sono:

-   Windows 7, 8, 10 e 11
-   Linux Ubuntu Focal Fossa (20.04) e successivi
-   macOS: 10.12 Sierra o successivo



## Limitazioni note 

### 32bit Windows 

Da FreeCAD 0.19 non supportiamo più ufficialmente Windows a 32 bit. FreeCAD potrebbe funzionare su questi sistemi, ma non viene fornito alcun supporto.



### Desktop remoto su Windows 

A seconda delle capacità grafiche OpenGL di un computer, potrebbe verificarsi un arresto anomalo durante l\'esecuzione di FreeCAD tramite desktop remoto. Per risolvere questo problema, aggiornare il proprio driver OpenGL. Solo se questo non aiuta:

-   Scaricare [this](https://downloads.fdossena.com/geth.php?r=mesa64-latest) libreria OpenGL per Windows a 64 bit ed estrarla.
-   Rinominare il file DLL in *opengl32sw.dll* e copiarlo nella sottocartella *bin* della cartella di installazione di FreeCAD (sovrascrivere lì la DLL esistente).



### macOS: Start Workbench mostra una pagina vuota 

Se [Start Workbench](Start_Workbench/it.md) mostra solo una pagina vuota, si deve abilitare l\'opzione **Usa software OpenGL** nel menu **FreeCAD-0.21 → Preferenze → Visualizza**.



---
![](images/Button_right.svg) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.21/it
