---
- GuiCommand:/it
   Name:Sketcher CreatePeriodicBSpline
   Name/it:Sketcher BSpline periodica
   Icon:Sketcher Create Periodic BSpline.svg
   MenuLocation: Schizzo → Geometrie → Crea B-spline periodica
   Workbenches: [Sketcher](Sketcher_Workbench/it.md)
   Version:0.17
   SeeAlso:[B-spline](Sketcher_CreateBSpline/it.md)
---

# Sketcher CreatePeriodicBSpline/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento traccia una curva B-spline periodica (chiusa) dai suoi punti di controllo.


</div>

![](images/Sketcher_Periodic_B-spline_example01.png )


<div class="mw-translate-fuzzy">

*Una curva B-spline periodica (in bianco) composta da 5 punti. Nell\'immagine ci sono il poligono di controllo in verde (le linee rette che collegano i punti rossi), i cerchi di peso in blu e il pettine di curvatura in verde. La cifra (3) al centro si riferisce al grado della B-spline, e le cifre (1) e (2) sui nodi che si trovano sulla curva si riferiscono alla loro molteplicità.*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **[<img src=images/Sketcher_Create_Periodic_BSpline.svg style="width:24px"> '''Crea B-spline periodica'''**.
2.  Creare una serie di punti facendo clic nella vista 3D. Mentre il comando è attivo, i punti creati sono collegati con linee rette e viene creato un cerchio di costruzione centrato su ciascun punto.
3.  Selezionare il primo punto della curva o fare clic con il pulsante destro per terminare l\'input e generare la curva.
4.  A seconda delle preferenze, lo strumento può rimanere attivo per tracciare una nuova curva. Fare nuovamente clic con il pulsante destro per uscire dal comando.

-   È possibile definire il peso dei punti di controllo modificando i raggi dei cerchi del peso. I vincoli di uguaglianza sui cerchi devono essere cancellati per primi. Il vincolo del raggio è arbitrario, il peso dei punti di controllo è definito dai raggi dei relativi cerchi. Funziona in modo simile alla gravità: più un cerchio è grande rispetto agli altri, più la curva è attratta dal punto di controllo.
-   La visibilità del poligono di controllo, del pettine di curvatura, del grado e della molteplicità dei nodi può essere attivata o disattivata dalla barra degli strumenti [Strumenti B-spline](Sketcher_Workbench/it#Sketcher_B-spline_tools.md).
-   Vedere gli altri strumenti nella barra degli [Strumenti B-spline](Sketcher_Workbench/it#Sketcher_B-spline_tools.md) per ulteriori strumenti di modifica delle B-spline.


</div>

## Limitazioni


<div class="mw-translate-fuzzy">

-   In questo momento molti tipi di vincoli non sono ancora supportati. Possono essere vincolati solo il punto di controllo e i punti finali della B-spline.
-   Gli strumenti [Rifila](Sketcher_Trimming/it.md) e [Estendi](Sketcher_Extend/it.md) non sono supportati.
-   La forma di una curva B-spline può essere modificata solo trascinando uno dei punti di controllo. I nodi che si trovano sulla curva non possono essere selezionati.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePeriodicBSpline/it
