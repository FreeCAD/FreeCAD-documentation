# <img alt="L\'icona dell\'ambiente Defeaturing" src=images/Defeaturing_workbench_icon.svg  style="width:64px;"> Defeaturing Workbench/it

## Introduzione




L\'ambiente <img alt="" src=images/Defeaturing_workbench_icon.svg  style="width:24px;"> **Defeaturing** è un ambiente aggiuntivo destinato alla modifica dei modelli STEP, per rimuovere dal modello le funzioni selezionate. È un [ambiente esterno](External_Workbenches/it.md) e quindi non fa parte dell\'installazione standard di FreeCAD.

## Funzioni

-   Dispone di una serie di strumenti per modificare una forma o un modello STEP, rimuovere fori, facce, semplificare il modello, modificare la tolleranza, applicare operazioni booleane fuzzy ecc \...
-   Ci sono anche strumenti per creare forme solide, da bordi, facce o gusci.
-   È anche possibile utilizzare la modellazione diretta del modello, quando la cronologia delle operazioni non è disponibile. (Questo è il caso dei modelli 3D STEP).
-   Utile in situazioni per rimuovere rapidamente i dettagli proprietari del modello prima di condividerlo. Vedere [Defeaturing](Defeaturing/it.md)

Nota: è possibile utilizzare gli strumenti di Defeaturing più avanzati se è disponibile [OCC7.3](OpenCASCADE/it.md).

## Installazione

### Automatica (consigliata) 

Utilizzando FreeCAD <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md) disponibile in v0.17+ tramite **Strumenti → Addon Manager**. Cerca l\'icona <img alt="" src=images/Defeaturing_workbench_icon.svg  style="width:24px;"> Defeaturing_workbench. Addon Manager avvisa anche l\'utente quando è disponibile una nuova versione di questo Addon.

### Manuale

Vedere [Come installare ambienti di lavoro aggiuntivi](How_to_install_additional_workbenches/it.md)

### Supporti

-   FreeCAD v0.15 4671
-   FreeCAD v0.16 \>= 6712
-   FreeCAD v0.17 \>= 13522
-   FreeCAD v0.18+

## Riferimenti

-   Autore: Github: [\@easyw](https://github.com/easyw) \| FreeCAD Forums: [1](https://forum.freecadweb.org/viewtopic.php?f=9&t=29506)
-   Codice sorgente in github: <https://github.com/easyw/Defeaturing_WB>
-   Discussione nel forum di FreeCAD <https://forum.freecadweb.org/viewtopic.php?t=29506>

## Strumenti

![Finestra di dialogo degli strumenti di Defeaturing](images/Defeaturing_WB.png )

<img alt="" src=images/Defeaturing_Tools.svg  style="width:32px;"> Gli strumenti di defeaturing si trovano in una maschera separata.

-   <img alt="" src=images/DefeatWB_Tools_rmv_hole.png  style="width:32px;"> [Remove Holes](DefeatWB_Tools_rmv_hole.md): rimuove il foro dalla faccia
-   <img alt="" src=images/DefeatWB_Tools_rmv_listed_Faces.png  style="width:32px;"> [Remove listed Faces](DefeatWB_Tools_rmv_listed_Faces.md): rimuove le facce \"in elenco\"
-   <img alt="" src=images/DefeatWB_Tools_add_Faces_listed_Edges.png  style="width:32px;"> [Add Faces from \'in List\' Edges](DefeatWB_Tools_add_Faces_listed_Edges.md): aggiunge facce dai bordi \"in elenco\"
-   <img alt="" src=images/DefeatWB_Tools_select_Faces_Param_Defeat.png  style="width:32px;"> [Select Faces to be Parametric defeatured](DefeatWB_Tools_select_Faces_Param_Defeat.md): seleziona le facce a cui applicare il defeaturing parametrico
-   <img alt="" src=images/DefeatWB_Tools_create_copy_listed_edges.png  style="width:32px;"> [Create a copy of the \'in List\' Edges ](DefeatWB_Tools_create_copy_listed_edges.md): crea una copia dei bordi \"in elenco\"

-   <img alt="" src=images/DefeatWB_Tools_copy_Faces_listed_faces.png  style="width:32px;"> [copy Faces from \'in List\' Faces ](DefeatWB_Tools_copy_Faces_listed_faces.md): copia le facce \"in elenco\"
-   <img alt="" src=images/DefeatWB_Tools_offset_face.png  style="width:32px;"> [ offset face](DefeatWB_Tools_offset_face.md): sposta una faccia
-   <img alt="" src=images/DefeatWB_Tools_offset_edge.png  style="width:32px;"> [offset edge](DefeatWB_Tools_offset_edge.md): sposta un bordo

-   <img alt="" src=images/DefeatWB_Tools_make_solid_listed_faces.png  style="width:32px;"> [Make Solid from in List Faces](DefeatWB_Tools_make_solid_listed_faces.md): crea un solido da un elenco di facce
-   <img alt="" src=images/DefeatWB_Tools_make_solid_faces_selected_objects.png  style="width:32px;"> [Make Solid from the Faces of the selected Objects](DefeatWB_Tools_make_solid_faces_selected_objects.md): crea un solido dalle facce degli oggetti selezionati
-   <img alt="" src=images/DefeatWB_Tools_select_one_object_2_make_solid_step_proc.png  style="width:32px;"> [Make Solid from in List Faces](DefeatWB_Tools_select_one_object_2_make_solid_step_proc.md): seleziona un oggetto per provare a creare un solido attraverso il processo di importazione/esportazione di STEP
-   <img alt="" src=images/DefeatWB_Tools_Connect.png  style="width:32px;"> [Connect](DefeatWB_Tools_Connect.md): collegamento
-   <img alt="" src=images/DefeatWB_Tools_clean_face_rmv_holes.png  style="width:32px;"> [clean Face(s) removing holes and merging Outwire](DefeatWB_Tools_clean_face_rmv_holes.md): pulisce le facce rimuovendo i fori e unendo i contorni

-   <img alt="" src=images/DefeatWB_Tools_show_listed_edges.png  style="width:32px;"> [show \'in List' Edge(s)](DefeatWB_Tools_show_listed_edges.md): mostra i bordi \"in elenco\"
-   <img alt="" src=images/DefeatWB_Tools_show_listed_faces.png  style="width:32px;"> [show \'in List' Face(s)](DefeatWB_Tools_show_listed_faces.md): mostra le facce \"in elenco\"
-   <img alt="" src=images/DefeatWB_Tools_refine.png  style="width:32px;"> [refine](DefeatWB_Tools_refine.md): affina
-   <img alt="" src=images/DefeatWB_Tools_simple_copy.png  style="width:32px;"> [simple copy](DefeatWB_Tools_simple_copy.md): copia semplice
-   <img alt="" src=images/DefeatWB_Tools_parametric_refine.png  style="width:32px;"> [parametric Refine](DefeatWB_Tools_parametric_refine.md): affina parametricamente

-   <img alt="" src=images/DefeatWB_Tools_geometry_check.png  style="width:32px;"> [geometry check](DefeatWB_Tools_geometry_check.md): controlla la geometria
-   <img alt="" src=images/DefeatWB_Tools_get_Tolerance_value.png  style="width:32px;"> [get Tolerance value](DefeatWB_Tools_get_Tolerance_value.md): cerca il valore di tolleranza
-   <img alt="" src=images/DefeatWB_Tools_set_Tolerance_value.png  style="width:32px;"> [set Tolerance value](DefeatWB_Tools_set_Tolerance_value.md): imposta il valore di tolleranza

-   <img alt="" src=images/DefeatWB_Tools_make_edges_selected_vertexes.png  style="width:32px;"> [make Edge from selected Vertexes](DefeatWB_Tools_make_edges_selected_vertexes.md): crea bordi dai vertici selezionati
-   <img alt="" src=images/DefeatWB_Tools_reset_placement.png  style="width:32px;"> [reset Placement](DefeatWB_Tools_reset_placement.md): resetta il posizionamento
-   <img alt="" src=images/DefeatWB_Tools_show_hide_typeId_shape.png  style="width:32px;"> [show/hide TypeId of the Shape](DefeatWB_Tools_show_hide_typeId_shape.md): mostra o nasconde il tipo ID della forma
-   <img alt="" src=images/DefeatWB_Tools_help.png  style="width:32px;"> [help](DefeatWB_Tools_help.md): aiuto

-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Cut.png  style="width:32px;"> [Fuzzy Cut](DefeatWB_Tools_Fuzzy_Cut.md): taglio approssimativo
-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Union.png  style="width:32px;"> [Fuzzy Union](DefeatWB_Tools_Fuzzy_Union.md): unione approssimativa
-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Common.png  style="width:32px;"> [Fuzzy Common](DefeatWB_Tools_Fuzzy_Common.md): intersezione approssimativa

## Tutorial video 

### Defeaturing

Rimozione delle funzioni mediante i nuovi strumenti OCC7.3

[480px\|left\|thumb \|link=<https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/removing-holes.mp4%7CDefeaturing-WB>: removing-features (holes)](Image:Defeaturing-WB-@Work_v3.png.md)

[480px\|left\|thumb \|link=<https://youtu.be/yrTtWFakAyE> \|alt=Defeaturing-WB-@Work\|YouTube: Defeaturing tools - Simplifying the model](Image:Defeaturing-WB-@Work_v1.png.md)

[480px\|left\|thumb \|link=<https://youtu.be/vgQwGI6Fk6Q%7CYouTube>: Defeaturing tools - Multi-select faces for defeaturing](Image:Defeaturing-WB-@Work_v2.png.md)

[480px\|left\|thumb \|link=<https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/removing-fillet-chamfer.mp4%7CDefeaturing-WB> - removing-fillet-chamfer](Image:Defeaturing-WB-@Work_v4.png.md)

[480px\|left\|thumb \|link=<https://peertube.mastodon.host/videos/watch/c6bc5abd-2eb7-48c7-af67-c4d8e6783872%7CDefeaturing-WB> - overview-features (in german language)](Image:Defeaturing-WB-@Work_v5.png.md)

[480px\|left\|thumb \|link=<https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/parametric-defeaturing.mp4%7CDefeaturing-WB> - parametric-defeaturing](Image:Defeaturing-WB-@Work_v6.png.md) 

### Riparazioni

-   Cucire una forma
-   Rimuovere o semplificare delle facce
-   Rimuovere i fori o le tasche
-   Leggere o modificare la tolleranza
-   effettuare operazioni booleane

## Ambienti esterni 

Gli ambienti di lavoro per FreeCAD sono facilmente programmabili in [Python](Python/it.md), quindi ci sono molte persone che stanno sviluppando degli ambienti aggiuntivi al di fuori del codice di base di FreeCAD.

La pagina [Ambienti complementari](external_workbenches/it.md) contiene alcune informazioni e tutorial su alcuni di loro, e il progetto [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) mira a raccoglierli e renderli facilmente installabili dall\'interno di FreeCAD.

Sono in fase di sviluppo ulteriori nuovi ambienti.



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Defeaturing Workbench/it
