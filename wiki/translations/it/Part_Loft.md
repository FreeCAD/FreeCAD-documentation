---
 GuiCommand:
   Name: Part Loft
   Name/it: Part Loft
   MenuLocation: Parte , Loft...
   
   Version: 0.13
   SeeAlso: Part_Sweep/it
---

# Part Loft/it



## Descrizione

Il comando <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Part Loft](Part_Loft/it.md) crea una faccia, un guscio (shell) o una forma solida da due o più profili (sezioni trasversali).

<img alt="" src=images/Part_Loft_solid_ruled_from3profiles_example_FreeCAD_0_13.jpg  style="width:400px;"> 
*Loft da tre profili che sono due [Part Cerchi](Part_Circle/it.md) e un [Part Ellisse](Part_Ellipse/it.md). I parametri sono Solido "Vero" Rigato "Vero".*



## Utilizzo

1.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Part_Loft.svg" width=16px> [Loft...](Part_Loft/it.md)**.
    -   Selezionare l\'opzione **Parte → <img src="images/Part_Loft.svg" width=16px> Loft...** dal menu.
2.  Si apre la [scheda azioni](Task_panel/it.md) Loft .
3.  Nell\'elenco *Profili disponibili* a sinistra selezionare il primo profilo e fare clic sulla freccia destra per posizionarlo nell\'elenco *Profili selezionati* a destra.
4.  Ripetere per il secondo profilo e ancora se si desiderano più di due profili.
5.  Facoltativamente, utilizzare le frecce su e giù per riordinare i profili selezionati.
6.  Definire le opzioni [Crea solido](#Dati.md), [Superficie rigata](#Dati.md) e [Chiuso](#Dati.md).
7.  Fare clic su **OK**.



### Geometria accettata 

-   **Profili:** può essere un punto (vertice), una linea (bordo), una polilinea o una faccia. I bordi e le polilinee possono essere aperti o chiusi. Esistono varie [Limitazioni](#Limitazioni.md), vedere di seguito.

-   Come profili possono essere utilizzati anche gli oggetti [App Link](App_Link/it.md) collegati ai tipi di oggetto appropriati e i contenitori [App Part](App_Part/it.md) con gli oggetti visibili appropriati all\'interno. {{Version/it|0.20}}



## Opzioni



#### Crea solido 

Se \"Solid\" è impostato su \"true\", FreeCAD crea un solido, a condizione che i profili siano chiusi; se impostato su \"false\", FreeCAD crea una faccia o un guscio (shell) per profili aperti o chiusi.



#### Superficie rigata 

Se \"Superficie rigata\" è \"true\" FreeCAD crea una faccia, un guscio (shell) o un solido dalle [superfici rigate](http://en.wikipedia.org/wiki/Ruled_surface).



#### Chiuso

Se \"Closed\" è \"true\" FreeCAD tenta di collegare l\'ultimo profilo al primo profilo per creare un anello chiuso.

Per ulteriori informazioni su come sono uniti i profili, vedere [Dettagli tecnici di Part Loft](Part_Loft_Technical_Details/it.md).



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Part Loft deriva da un oggetto [Funzione Part](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Loft}}

-    **Sections|LinkList**: Elenca le sezioni utilizzate.

-    **Solid|Bool**: Falso (predefinito). True crea un solido.

-    **Ruled|Bool**: Falso (predefinito). True crea una superficie rigata.

-    **Closed|Bool**: False (predefinito). True crea un loft chiuso collegando l\'ultimo al primo profilo.

-    **Max Degree|IntegerConstraint**: Grado massimo.



## Limitazioni

Un Part Loft ha le stesse limitazioni di un [Part Sweep](Part_Sweep/it#Limitazioni.md).



### Loft chiusi 

-   -   I risultati dei loft chiusi possono essere inaspettati - il loft può produrre torsioni o piegature. L\'operazione Loft è molto sensibile al posizionamento dei profili e per collegare i corrispondenti vertici in tutti i profili servono curve molto complesse.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/it
