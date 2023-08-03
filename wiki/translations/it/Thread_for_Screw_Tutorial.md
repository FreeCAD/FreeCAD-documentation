---
 TutorialInfo:t
   Topic:  Modellazione
   Level:  Avanzato
   Time:  
   Author: User:DeepSOIC, User:Murdic
   FCVersion: 0.14 o superiore 
   Files: 
---

# Thread for Screw Tutorial/it




<div class="mw-translate-fuzzy">




</div>




<div class="mw-translate-fuzzy">

### Introduzione

Questo tutorial è un insieme di tecniche per modellare le filettature in FreeCAD.


</div>

This tutorial is a collection of techniques to model screw threads in FreeCAD. It was updated for v0.19, although the overall process has been essentially the same since v0.14, when the tutorial was originally written. The updated content focuses on the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md) to create the thread, but does not use the <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:24px;"> [PartDesign AdditiveHelix](PartDesign_AdditiveHelix.md) tool as this was introduced later.


<div class="mw-translate-fuzzy">

La modellazione delle filettature è sconsigliata, perché carica notevolmente il kernel di modellazione, e anche il rendering. Le forme filettate occupano molta memoria e anche una sola filettatura in un progetto FreeCAD può facilmente far balzare le dimensioni del file nella gamma dei megabyte. Tuttavia, ci sono alcune situazioni, in cui è indispensabile modellare la filettatura con tutti i suoi dettagli, e questo è il motivo per cui viene prodotto questo tutorial.


</div>

Many of the techniques presented here have been collected from different forum threads:

-   [Gathering thread modeling techniques](https://forum.freecad.org/viewtopic.php?f=3&t=12593)
-   [Creating a thread: Unexpected results](https://forum.freecad.org/viewtopic.php?f=3&t=6506)

See also helpful videos:

-   [Introducing a strategy for designing a bolt without the commonly found problems.](https://forum.freecad.org/viewtopic.php?f=8&t=44259)

Remember that thread shapes take a lot of memory, and having just one thread in a document can increase the file size significantly, so the user is advised to create threads only when absolutely necessary.




<div class="mw-translate-fuzzy">

### Metodo 0. Procurarsi una filettatura dalla libreria delle parti 

Utilizzare i modelli prodotti da altri utenti è semplice e fa risparmiare tempo. Consultare la [Macro BOLTS](Macro_BOLTS/it.md), che è un\'interfaccia per l\'inserimento di parti standard dalla libreria BOLTS.


</div>

Using utilities and parts that other people have created is easy and saves time. See the [external workbenches](External_workbenches.md) page for information on external tools.

In particular, three resources are recommended that can be installed from the [Addon Manager](Std_AddonMgr.md):

-   [Fasteners Workbench](Fasteners_Workbench.md), to add/attach various fasteners to parts. The screws and nuts don\'t show a thread by default, but this can be controlled with an option.
-   [BOLTSFC Workbench](BOLTSFC_Workbench.md), to place fasteners from the BOLTS library.
-   [ThreadProfile Workbench](ThreadProfile_Workbench.md), to create common threads.

<img alt="" src=images/T13_00_Threads_fasteners.png  style="width:" height="300px;"> 
*Various standard screws inserted with the Fasteners Workbench. An option controls whether an object shows the real thread or just a plain cylinder.*




<div class="mw-translate-fuzzy">

### Metodo 1. Usare le macro 

C\'è la famosa [macro Screw Maker](Macro_screw_maker1_2/it.md), creata da ulrich1a, e un intero [Fasteners Workbench](http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/) creato da shaise ([link to GitHub](https://github.com/shaise/FreeCAD_FastenersWB)). Queste macro hanno la possibilità di generare un filetto. Esse creano dei profili di filettatura standard (triangolare-ish).


</div>

-   In the past, the [Macro BOLTS](Macro_BOLTS.md) was used to insert the parts from the BOLTS library. This is now deprecated. Use the [BOLTSFC Workbench](BOLTSFC_Workbench.md) instead.

-   In the past the stand-alone [Screw Maker macro](Macro_screw_maker1_2.md), by ulrich1a, was used to create individual bolts, screws, and washers. This is now deprecated. The [Fasteners workbench](Fasteners_Workbench.md), by shaise, includes the complete screw maker macro, together with a GUI to select the right component.




<div class="mw-translate-fuzzy">

### Metodo 2. Simulare accatastando dei dischi 

Questo è un ottimo modo per visualizzare le filettature, pur mantenendo semplice la geometria.


</div>

In many cases we don\'t need real threads, we just need a visual indication that the threads will be there.


<div class="mw-translate-fuzzy">

L\'idea è quella di creare una filettatura non elicoidale (cioè che sia solo la rivoluzione di un profilo a dente di sega, o una pila di dischi con i bordi rastremati). Solo a vista, è difficile distinguere tale falsa filettatura da quella reale elicoidale. Questo può funzionare anche per FEM. Purtroppo, se si desidera stamparla in 3D, questo metodo non funziona.


</div>

<img alt="" src=images/T13_01_Threads_comparison_fake_real.png  style="width:" height="300px;"> 
*Left: simple bolt with a fake, non-helical thread. Right: simple bolt with a real helical thread. When 3D printing is not needed, a simulated thread is often sufficient for visualization.*

### Revolving sawtooth profile 

1.  Click on **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**.
2.  Click on **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign New sketch](PartDesign_NewSketch.md)**. Select {{Value|XZ_Plane}}.
3.  Draw a closed sketch with the required inner diameter {{Value|10 mm}}, outer diameter around {{Value|12.6 mm}}, pitch {{Value|3 mm}}, number of teeth {{Value|8}}, and total height {{Value|30 mm}}.
4.  Select the sketch, then click on **[<img src=images/PartDesign_Revolution.svg style="width:16px"> [PartDesign Revolution](PartDesign_Revolution.md)**. Select {{Value|Vertical sketch axis}}, and press **OK**.

<img alt="" src=images/T13_02_Threads_Sawtooth_sketch_profile.png  style="width:" height="300px;"> 
*Profile used to create the revolution that will simulate a thread.*

<img alt="" src=images/T13_03_Threads_Sawtooth_revolution_1.png  style="width:" height="300px;"> <img alt="" src=images/T13_04_Threads_Sawtooth_revolution_2.png  style="width:" height="300px;"> 
*Sectional view of the resulting non-helical thread produced by revolving the sawtooth profile around the vertical axis.*

### Stacking discs 

1.  Repeat the first two steps from the previous section.
2.  Draw a closed sketch with the required inner diameter {{Value|10 mm}}, outer diameter around {{Value|12.6 mm}}, and pitch {{Value|3 mm}}, but draw only a single tooth of the sawtooth.
3.  Select the sketch, then click on **[<img src=images/PartDesign_Revolution.svg style="width:16px"> [PartDesign Revolution](PartDesign_Revolution.md)**. Select {{Value|Vertical sketch axis}}, and press **OK**.
4.  Select the {{Value|Revolution}}, then click on **[<img src=images/PartDesign_LinearPattern.svg style="width:16px"> [PartDesign Linear pattern](PartDesign_LinearPattern.md)**. Select {{Value|Vertical sketch axis}}. For a fake thread with a pitch of {{Value|3 mm}}, set the **Length** to {{Value|3}}, and **Occurrences** to {{Value|2}}, then press **OK**. This will create two discs, one on top of the other.
5.  You can add more discs by increasing the value of **Occurrences** in the linear pattern, and by raising the **Length**, which is the total length of the fake thread.

The **Length** and **Occurrences** are related. If the length is too large, but the number of occurrences is not high enough, you will have disconnected discs, and the Body computation will fail, as the resulting object must always be a [single contiguous solid](PartDesign_Body.md). For example, to get a total height of {{Value|30 mm}}, set **Length** to {{Value|27 mm}} and **Occurrences** to {{Value|10}}.

If you wish, you may add a **[<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [PartDesign Additive cylinder](PartDesign_AdditiveCylinder.md)** with a diameter equal to the inner diameter of the discs, and as high as the total thread height. This will join all discs into a single solid, thus guaranteeing that there will not be disconnected discs.

<img alt="" src=images/T13_05_Threads_Stacked_discs_sketch.png  style="width:" height="300px;"> 
*Profile used to create a revolved disc that will be used to simulate a thread.*

<img alt="" src=images/T13_06_Threads_Stacked_discs_1.png  style="width:" height="300px;"> <img alt="" src=images/T13_07_Threads_Stacked_discs_2.png  style="width:" height="282px;"> 
*Left: single disc created by revolution. Right: multiple discs placed in a linear pattern in the Z direction simulating a helical thread.*




<div class="mw-translate-fuzzy">

### Metodo 3. Sweep di un profilo verticale. 

#### Idea

L\'idea è piuttosto semplice: disegnare il profilo del filetto, e quindi eseguirne lo [sweep](Part_Sweep/it.md) lungo una [elica](Part_Helix/it.md). Quando si esegue lo sweep, accertarsi di spuntare le caselle di controllo Solido e Frenet. Solido è la chiave per poter eseguire delle operazioni di [unione](Part_Union/it.md) o di [taglio](Part_Cut/it.md) su di esso. Frenet evita la torsione del profilo (ulteriori informazioni sono disponibili nella documentazione di [Sweep](Part_Sweep/it.md)).


</div>

### PartDesign Workbench 

A true thread consists of a closed profile sweeping a solid along a helical path.

1.  In the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md), click on **[<img src=images/Part_Primitives.svg style="width:16px"> [Part Primitives](Part_Primitives.md)** to create a **[<img src=images/Part_Helix.svg style="width:16px"> [Part Helix](Part_Helix.md)**. Give it the appropriate values for **Pitch** {{Value|3 mm}}, **Height** {{Value|23 mm}}, and **Radius** {{Value|10 mm}}.
2.  Move to the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md), and click on **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**.
3.  Click on **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign New sketch](PartDesign_NewSketch.md)**. Select {{Value|XZ_Plane}}.
4.  Draw a closed sketch with the required profile for the thread teeth, normally a triangular shape. In this case we will use a height of {{Value|2.9 mm}}, which is slightly smaller than the {{Value|3.0 mm}} pitch used for the helix path. The profile must not create any self intersections when moved along the helix, neither between the turns nor in the middle, thus the sketch as shown for stacking disks cannot be used.
5.  Select the sketch, then click on **[<img src=images/PartDesign_AdditivePipe.svg style="width:16px"> [PartDesign Additive pipe](PartDesign_AdditivePipe.md)**. In **Path to sweep along**, click on **Object**, and choose the helix object previously created. Then change **Orientation mode** to {{Value|Frenet}} so that the profile sweeps the path without twisting; then press **OK**.
6.  When the dialog asks for a reference, choose {{Value|Create cross-reference}}.
7.  The helical coil is created, but there is no central body or shaft.
8.  Click on **[<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [PartDesign Additive cylinder](PartDesign_AdditiveCylinder.md)** with the appropriate **Radius** {{Value|10 mm}} and **Height** {{Value|29.9 mm}} to touch the rest of the helical thread and automatically fuse to it.
9.  Additional boolean operations are needed to shape up the abrupt ends of the coil. For example, you can use additive features to provide a head to the screw, and a tip.

<img alt="" src=images/T13_08_Threads_Helical_thread_profile.png  style="width:" height="300px;"> <img alt="" src=images/T13_09_Threads_Helical_thread_path.png  style="width:" height="300px;"> 
*Left: profile for a helical thread. Right: helical path that will be used to create a sweep.*

<img alt="" src=images/T13_10_Threads_Helical_thread_coil.png  style="width:" height="300px;"> <img alt="" src=images/T13_11_Threads_Helical_thread_coil_sliced.png  style="width:" height="300px;"> 
*Left: helical coil resulting from the sweep operation of the closed profile along the helical path. Right: sectional view of the coil produced from the sweep.*

<img alt="" src=images/T13_12_Threads_Helical_thread_cylinder.png  style="width:" height="300px;"> <img alt="" src=images/T13_13_Threads_Helical_thread_finished.png  style="width:" height="300px;"> 
*Left: helical coil fused to a central cylinder to form the body of the screw. Right: more features, a head and a tip, added to improve the shape of the screw.*

### Part Workbench 

This process can also be done with the tools of the [Part Workbench](Part_Workbench.md).

1.  In the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md), click on **[<img src=images/Part_Primitives.svg style="width:16px"> [Part Primitives](Part_Primitives.md)** to create a **[<img src=images/Part_Helix.svg style="width:16px"> [Part Helix](Part_Helix.md)**. Give it the appropriate values for **Pitch** {{Value|3 mm}}, **Height** {{Value|23 mm}}, and **Radius** {{Value|10 mm}}.
2.  In this case, you don\'t need a **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**. Switch to the <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md), then click **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher New sketch](Sketcher_NewSketch.md)**, and choose the global XZ plane.
3.  Then return to the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md), and use **[<img src=images/Part_Sweep.svg style="width:16px"> [Part sweep](Part_Sweep.md)**.
4.  Select the appropriate sketch from **Available profile** and click the arrow to pass it to **Selected profiles**.
5.  Click **Sweep path**, and choose all edges of the existing helix in the [3D view](3D_view.md). Click **Done**.
6.  Make sure to tick {{CheckBox|TRUE|Create solid}} and {{CheckBox|TRUE|Frenet}}. Obtaining a solid is the key to be able to perform [Part Boolean](Part_Boolean.md) operations with the resulting coil, otherwise only a surface will be produced.
7.  Click **OK** to exit the dialog and create the coil.


<div class="mw-translate-fuzzy">

Questo genera la spira del filetto, senza il supporto o il foro. Per effettuare una filettatura su un supporto o in un foro, si deve [unire](Part_Union/it.md) o [tagliare](Part_Cut/it.md) questa spira con un cilindro. Ulteriori operazioni booleane sono necessarie per smussare le brutte estremità della spira che termina bruscamente .


</div>

<img alt="" src=images/T13_14_Threads_components.png  style="width:" height="300px;">


<div class="mw-translate-fuzzy">

<img alt="Creare un filetto con lo sweep di un profilo verticale. 1 - il profilo (uno [schizzo" src=images/Sketcher_Workbench/it.md)). 2 - il percorso sweep ([Elica](Part_Helix/it.md)). 3 - il risultato dello sweep ([Sweep](Part_Sweep/it.md))](thread-by-vertical-profile.png  style="width:500px;">


</div>




<div class="mw-translate-fuzzy">

#### Trucchi per avere successo 


</div>

-    **Rule 1.**When the profile sweeps the helix, the resulting solid coil must not touch or self-intersect as it will be an invalid solid. This holds for the profile moving along the helix, as well as intersections in the center of the helix. Attempts to do boolean operations with it (fuse or cut) are very likely to fail. Check the quality of the coil with **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part CheckGeometry](Part_CheckGeometry.md)**; if self-intersections are reported, you must increase the pitch of the helix.

<img alt="" src=images/T13_15_Threads_self_intersection.png  style="width:" height="300px;"> <img alt="" src=images/T13_16_Threads_no_self_intersections_OK.png  style="width:" height="300px;">


<div class="mw-translate-fuzzy">

Regola 1. Lo sweep non deve auto-intersecarsi o toccarsi. Uno sweep auto-intersecante è un solido non valido. Molto probabilmente i tentativi di fonderlo o di tagliarlo sono destinati a fallire. Tuttavia, lasciando il filetto ed il cilindro non fusi, ma intersecati, questo può essere utile per la stampa 3d e la visualizzazione.


</div>

-    **Rule 2.**When a cylinder is added to a coil to form the main shaft of a screw, the cylinder must not be tangent to the coil profile. That is, the cylinder must not have the same radius as the inner radius of the thread, as this is very likely to fail a fuse operation. In general, avoid geometry coincident to elements of the sweep, such as tangent faces, or edges tangent to faces they are not connected to. In order to produce a good boolean union, the swept coil and the cylinder must intersect. Check the quality of the fusion with **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part CheckGeometry](Part_CheckGeometry.md)**; if coplanar faces are reported increase the cylinder\'s radius by a small amount.

-   If the coil and the cylinder are tangent, even if the first fusion succeeds, it may fail in subsequent boolean operations with a third solid.

-   This is a limitation of the OpenCASCADE Technology (OCCT) kernel; in general, it doesn\'t handle well operations between coplanar surfaces.

<img alt="" src=images/T13_17_Threads_tangent_faces.png  style="width:" height="300px;"> <img alt="" src=images/T13_18_Threads_no_tangent_faces_OK.png  style="width:" height="300px;">


<div class="mw-translate-fuzzy">

Regola 2. Ricordare che in FreeCAD un\'elica è una cosa imprecisa. Di conseguenza, è molto probabile che la fusione del cilindro che deve accoppiarsi con la filettatura non vada a buon fine. In generale, evitare di far coincidere delle geometrie con gli elementi dello sweep, come facce tangenti, bordi tangenti alle facce a cui non sono connessi, bordi coincidenti e tangenti, etc.


</div>

-    **Rule 3.**The inner cylinder has a seamline. You should avoid placing the start of the helix along that seam. Either turn the helix or the cylinder by some degrees.


<div class="mw-translate-fuzzy">

Suggerimento 1. Il raggio dell\'elica non è importante (a meno che l\'elica sia conica). Tutto ciò che conta è il passo e l\'altezza della traiettoria elicoidale. Questo significa che è possibile utilizzare un elica generica per generare numerosi filetti con lo stesso passo.


</div>


<div class="mw-translate-fuzzy">

Suggerimento 2. Mantenere il filetto corto (pochi giri). I filetti lunghi tendono a fallire nelle operazioni booleane. Se un filetto lungo si rivela problematico, considerare l\'impilamento di filetti corti usando [Draft Array](Draft_Array/it.md).


</div>

-    **Tip 3.**For 3D visualization and 3D printing it may be okay to leave the cylinder and the thread unfused, that is, with intersections between the two solids. Reducing the amount the boolean operations results in less memory consumption and smaller files.




<div class="mw-translate-fuzzy">

#### Pro e contro 

\+ Modo molto naturale di definire il profilo di una filettatura


</div>


<div class="mw-translate-fuzzy">

\+ facile da capire


</div>


<div class="mw-translate-fuzzy">

\- per l\'invalidità degli sweep auto-intersecanti, è quasi impossibile generare un filetto senza lacune (cioè, senza facce cilindriche sui lati esterni o interni del filetto)


</div>




<div class="mw-translate-fuzzy">

### Metodo 4. Sweep di un profilo orizzontale 

#### Idea 


</div>

### General


<div class="mw-translate-fuzzy">

L\'idea è quella di creare lo sweep di una sezione orizzontale del filetto lungo l\'elica. Il problema principale è capire quale profilo si deve usare per ottenere un determinato filetto.


</div>

<img alt="" src=images/thread-by-horz-profile.png  style="width:600px;">


<div class="mw-translate-fuzzy">

Se si usa un cerchio come profilo orizzontale (il cerchio deve essere posizionato scostato dall\'origine, e questa distanza definisce la profondità del filetto), il profilo del filetto risulta sinusoidale.


</div>


<div class="mw-translate-fuzzy">

Per ottenere un profilo standard a dente di sega, si devono fondere in un wire una coppia di spirali di Archimede riflesse. La figura risultante è una forma di cuore, che diventa a malapena distinguibile da un cerchio quando la profondità del filetto è piccola rispetto al suo diametro (è per questo motivo che nell\'immagine sopra viene mostrato con una linea \"spessa\").


</div>




<div class="mw-translate-fuzzy">

#### Generare il profilo 

Non è facile capire qual è il profilo orizzontale necessario per ottenere un determinato profilo verticale. Per i casi semplici, come quello triangolare o trapezoidale, può essere costruito manualmente. In alternativa, può essere costruito creando un filetto corto con il metodo 3, e poi ricavando una sua sezione con una operazione [Parte comune](Part_Common/it.md) tra una faccia piana orizzontale e il filetto.


</div>

Figuring out the horizontal profile to obtain a certain vertical profile is not easy. For simple cases like triangular or trapezoidal it can be constructed manually. Alternatively, it can be constructed by creating a short thread with method 4, and getting a slice of it by doing a [Part Common](Part_Common.md) between a horizontal plane face and the thread.




<div class="mw-translate-fuzzy">

##### Profilo per filetti triangolari 

1.  Creare una spirale di Archimede nel piano XY.
    1.  Impostare il numero di giri a 0.5,
    2.  impostare il raggio interno del filetto (il raggio esterno è questo raggio + la profondità di taglio)
    3.  e aggiungere il doppio della profondità di taglio del filetto.
2.  [Riflettere](Part_Mirror/it.md) la spirale sul piano XY
3.  [Unire](Part_Union/it.md) la spirale con la sua riflessione in modo da ottenere un contorno chiuso, a forma di cuore. Fatto!


</div>

1.  First create an Archimedian spiral in the XY plane.
    1.  Set the number of turns to 0.5.
    2.  Set the radius to the inner radius of the thread, the outer radius will be this plus the depth of the cut.
    3.  Set the growth to double the depth of cut of the thread.
2.  [Part Mirror](Part_Mirror.md) the spiral against the XY plane
3.  [Part Fuse](Part_Fuse.md) the spiral and the mirror to obtain a closed wire, shaped like a heart.




<div class="mw-translate-fuzzy">

##### Profilo per una sezione arbitraria 

<img alt="" src=images/thread-by-horz-profile-profileMake.png  style="width:1000px;">


</div>

<img alt="" src=images/thread-by-horz-profile-profileMake.png  style="width:1000px;">


<div class="mw-translate-fuzzy">

1.  Disegnare una sezione verticale del profilo. Assicurarsi che l\'altezza del disegno corrisponda al passo della filettatura.
2.  Creare una elica1 con altezza identica al passo e il passo identico al passo della filettatura ed un raggio dell\'elica di 0,42\*diametro nominale della filettatura.
3.  Eseguire lo sweep del profilo della sezione lungo elica1. Impostare Solido e Frenet su true.
4.  Creare un cerchio con il raggio nominale della filettatura nel piano xy.
5.  Creare una faccia dal cerchio. (Ambiente Part: utilità avanzate per creare forme, oppure con [Promuovi](Draft_Upgrade/it.md) rendere MakeFace = true)
6.  Tagliare la faccia con il profilo dello sweep
7.  Fare un clone dal taglio (Ambiente Draft)
8.  Retrocedere il clone in modo da ottenere un wire (Ambiente Draft). Questo wire è il profilo orizzontale necessario per questo metodo.
9.  Creare una spirale con il raggio nominale, il passo e l\'altezza della filettatura desiderata.
10. Eseguire lo sweep del wire lungo l\'elica. Impostare Solido e Frenet su true.

Fatto.


</div>


<div class="mw-translate-fuzzy">

Credito: guida passo-passo dal [forum post by Ulrich1a](http://forum.freecadweb.org/viewtopic.php?f=3&t=6506#p52558), leggermente modificata.


</div>


<div class="mw-translate-fuzzy">

I passaggi sono anche mostrati in azione in questo video di Gaurav Prabhudesai: <http://www.youtube.com/watch?v=fxKxSOGbDYs>


</div>




<div class="mw-translate-fuzzy">

#### Pro e contro 

\+ Lo sweep crea la filettatura pronta per l\'uso direttamente su una forma solida.


</div>

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> a ready-to-use thread-on-a-rod solid shape is created by the sweep directly.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> fewer or even no boolean operations are required, so generation speed is very high compared to Method 4.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> thread ends are nicely cut straight away
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> long threads are not a problem, unless a boolean operation is needed. Otherwise, it is not going to be much better than Method 4.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> threads without a gap are not a problem.


<div class="mw-translate-fuzzy">

\- È complicato definire il profilo del filetto.


</div>




<div class="mw-translate-fuzzy">

### Metodo 5. Loft tra facce elicoidali estruse 


</div>




<div class="mw-translate-fuzzy">

#### Idea 


</div>

Le Spline elicoidali estrudono delle facce coassiali che possono essere usate per un loft, mentre l\'elica parametrica di FreeCAD no. Per definire una filettatura servono due spline elicoidali. Esse possono essere prelevate da una libreria di spline, poi posizionate ed estruse in modo appropriato per ottenere la giusta forma.

Le eliche parametriche di FreeCAD non sono veramente elicoidali, ma non è difficile tracciare delle b-spline elicoidali. Un metodo manuale consiste nel creare delle matrici dodecagonali (poligono di 12 lati) con 5mm di raggio, o 10mm di diametro, a intervalli z di 1/12mm (0.08333.mm) e tracciare una spline da vertice a vertice in ordine ascendente e rotazionale. Considerare di costruirle, ad esempio, per 10 giri, e poi archiviarle come file di una libreria in modo da poterle importare e riutilizzare. Per comodità di ridimensionamento, conviene usare un diametro di 10mm e un passo di 1mm. Fatto manualmente, è più facile disegnare una Dwire e poi convertirla in un b-spline che disegnare direttamente una spline. Nelle linee Dwire non viene calcolata la curvatura mentre vengono disegnate, quindi seguono meglio il cursore e obbediscono di più all\'aggancio.

Once the splines are scaled to the right size and located so that the loft will have the right included angle between the thread flanks, they\'re extruded along their axis, a pitch length\'s worth for the inner spline, the outer pitch/8.

<img alt="" src=images/splineextrudeloft.png  style="width:912px;">

ISO e altri thread hanno alleviato, cioè bordi piatti, interni ed esterni piuttosto che affilati, il che si adatta agli utenti di FreeCAD con questo metodo, perché possiamo loft alla faccia elicoidale alla dimensione nominale del fissaggio, mentre una faccia interna non può essere loftata una spline del bordo esterno perché una faccia è un profilo chiuso, una spline è aperta. Lo standard ISO afferma che le dimensioni nominali dei filetti esterni hanno un passo della larghezza della faccia/8. L\'immagine mostra come è organizzata la geometria e le facce elicoidali che ne risultano. Quindi, ai fili viene aggiunto un loft tra le facce e quindi un cilindro che dà la faccia elicoidale interna, che ISO mette a passo/4 di larghezza.

![761PX](images/Threadform.PNG )

Questo metodo produce solidi affidabili che booleano correttamente. Sebbene non produca filettature \"parametriche\" in dimensioni standard nel senso di avere un accesso semplice alla forma in base alle dimensioni del dispositivo di fissaggio, è un modo semplice di produrre una libreria accurata per il riutilizzo e modelli di forme specializzate come ACME o viti Archimedian , sono anche semplici come one-offs.


 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Thread for Screw Tutorial/it
