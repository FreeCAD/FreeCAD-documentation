---
- GuiCommand:/it   Name:Part Torus   Name/it:Toro   MenuLocation:Parte → Primitive → Toro   Workbenches:[SeeAlso: [[Part_CreatePrimitives/it|Crea primitive](Part_Workbench/it___Parte]].md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Crea un semplice toro parametrico, con i parametri position, angle1, angle2, angle3, radius1 e radius2.


</div>

<img alt="" src=images/SimpleTorus.jpg  style="width:400px;">

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Attivare l\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/it.md).
2.  Richiamare il comando Toro in uno di questi modi:
    -   Premere il pulsante <img alt="" src=images/Part_Torus.svg  style="width:24px;">.
    -   Usare **Part → Toro** dal menu principale.


</div>


<div class="mw-translate-fuzzy">

**Risultato:** Il toro verrà posizionato nell\'origine (punto 0,0,0) al momento della creazione.
I parametri angolo (angolo1, angolo2, angolo3), nonché i parametri raggio (raggio1, raggio2) consentono di parametrizzare il toro. Vedere la sezione successiva.


</div>

## Opzioni

![](images/TorusExampleOverviewParameters.jpg )

**Parametri**

Un toro può essere assimilato ad un disco che compie un\'orbita circolare attorno un\'asse immaginario. Quindi il toro parametrico è definito dai seguenti parametri:

-    {{Parameter|Raggio1:}}Raggio del cerchio attorno al quale circola il disco. Distanza tra l\'asse di rotazione, centro del toro, e il centro del disco.

-    {{Parameter|Raggio2:}}Raggio del disco che definisce la forma del toro

-    {{Parameter|Angolo1:}}1° Angolo di taglio per definire il disco del toro

-    {{Parameter|Angolo2:}}2° Angolo di taglio per definire il disco del toro

-    {{Parameter|Angolo3:}}3° Angolo per definire la circonferenza del toro. Ampiezza della rotazione

nonché la serie standard di parametri di posizionamento. Le immagini sottostanti danno una rappresentazione grafica dei parametri citati:

![](images/TorusExampleRadius1.jpg ) Il parametro Raggio1 ha il valore di 20 mm.

![](images/TorusExampleRadius2.jpg ) Il parametro Raggio2 ha il valore di 2 mm.

![](images/TorusExampleAngle1.jpg ) Il parametro Angolo1 ha il valore di -90°. Notare che, lo strumento \"di misura dell\'angolo\" non in grado di visualizzare l\'angolo negativo. Considerare il valore visualizzato nell\'immagine come \"-90°\".

![](images/TorusExampleAngle2.jpg ) Il parametro Angolo2 ha il valore di 90°.

![](images/TorusExampleAngle3.jpg ) Il parametro Angolo3 ha il valore di 90°. 


<div class="mw-translate-fuzzy">





</div>


 
