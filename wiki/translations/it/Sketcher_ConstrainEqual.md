# Sketcher ConstrainEqual/it
---
- GuiCommand:/it   Name:Sketcher ConstrainEqual   Name/it:Uguale   Workbenches:[MenuLocation:PartDesign → Schizzo → Uguale   Shortcut:E   SeeAlso:[[Sketcher_ConstrainRadius/it|Raggio](Sketcher_Workbench/it___Schizzo]].md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Il vincolo Uguale forza due o più segmenti di linea in una linea, in una polilinea o in un rettangolo ad avere uguale lunghezza. Se applicato a archi o cerchi, vincola uguali i raggi. Non può essere applicato a geometrie primitive che non sono dello stesso tipo, ad esempio segmenti con archi.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

Lo schizzo dell\'esempio seguente contiene una serie di primitive di disegno (linea, polilinea, rettangolo, arco e cerchio).


</div>

![](images/EqualConstraint1.png )

Selezionare due o più segmenti di linea (ad esempio una linea e un lato del rettangolo).

![](images/EqualConstraint2.png )


<div class="mw-translate-fuzzy">

Fare clic sull\'icona **[<img src=images/Constraint_EqualLength.png style="width:16px"> [Uguale](Sketcher_ConstrainEqual/it.md)** nella barra degli strumenti di vincolo o selezionare il vincolo Uguale dal sottomenu dell\'ambiente Schizzo (o quello dell\'ambiente PartDesign).


</div>

![](images/EqualConstraint3.png )

Ora selezionare l\'arco e il cerchio nel disegno.

![](images/EqualConstraint4.png )


<div class="mw-translate-fuzzy">

e applicare il vincolo <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> come in precedenza.


</div>

![](images/EqualConstraint5.png )

Ora selezionare il segmento di linea, tutti i segmenti della poli-linea e uno dei lati non ancora vincolati del rettangolo

![](images/EqualConstraint6.png )


<div class="mw-translate-fuzzy">

e applicare vincolo <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> come in precedenza.


</div>

![](images/EqualConstraint7.png )

Selezionare il segmento di retta e l\'arco

![](images/EqualConstraint8.png )


<div class="mw-translate-fuzzy">

e applicare il vincolo <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> come in precedenza. Una finestra di messaggio ricorda che gli elementi da vincolare devono essere dello stesso tipo geometrico (linee di curvatura pari a zero o linee con curvatura diversa da zero).


</div>

![](images/EqualConstraint9.png )

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1` and `Edge2` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/it
