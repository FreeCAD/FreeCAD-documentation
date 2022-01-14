---
- GuiCommand:
   Name:Sketcher ConstrainRadius
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   MenuLocation:Sketch → Sketcher constraints → Constrain radius
   SeeAlso:[Constrain distance](Sketcher_ConstrainDistance.md), [Constrain horizontal distance](Sketcher_ConstrainDistanceX.md), [Constrain vertical distance](Sketcher_ConstrainDistanceY.md)
---

# Sketcher ConstrainRadius/ro


</div>


<div class="mw-translate-fuzzy">

## Descriere

Această constrângere obligă valoarea razei unui cerc sau a unui arc de cerc să aibă o valoare specifică. Dacă este selectat mai mult de un cerc sau un arc de cerc înainte de lansarea comenzii, un dialog contextual vă va întreba dacă toate elementele selectate ar trebui să partajeze aceeași rază. În cazul unui răspuns afirmativ, se va adăuga o constrângere de rază și o [equal length](Sketcher_ConstrainEqual.md) va fi adăugată la toate elementele. În negativ, vor fi create constrângeri separate de rază pentru fiecare cerc / arc, dar cu valori egale care vor fi editate separat după crearea.


</div>

This constraint constrains the value of the radius of a circle or arc to have a specific value. If more than one circle or arc is selected before launching the command :

-   If the constrain is applied in \'Reference\' mode, a new reference constrain is added to each object separately according above rules
-   If the constrain is applied in \'Normal\' (driving) mode, following rules are applied
    -   A reference constrain is applied separately on each object which is an external geometry

    -   
        **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Equal constrains](Sketcher_ConstrainEqual.md)**
        
        are applied sequentially between all real/construction geometry objects and a dimensional constrain is applied to the first selected object according above rules

NB : B-spline poles can\'t be mixed with other object type in the selection

![](images/Sketcher_ConstrainRadius_example.png )


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Selectați una sau mai multe cercuri sau arce e cerc.
2.  Apăsați butonul **[<img src=images/Sketcher_ConstrainRadius.png style="width:24px"> '''Constrain radius'''** .
3.  Un dialog contextual se deschide pentru a edita sau a confirma vloarea. Apăsați **OK** pentru a valida.În cazul în care au fost selectate mai multe cercuri/arce, toate constrângerile vor adopta această valoare. Editați valorile lor separat făcând dublu clic pe cota/eticheta de dimensiuni din vizualizarea 3D; sau în lista Constrângeri, faceți dublu clic pe constrângere sau faceți clic dreapta și selectați**Change value**.
4.  Opțional, eticheta/cota și linia de cotă pot fi mutate și rotite în vizualizarea 3D făcând clic pe valoare și tragând în timp ce mențineți apăsat butonul stânga al mouse-ului.


</div>


<div class="mw-translate-fuzzy">

**Notă:** instrumentul de constrângere poate fi pornit și fără o selecție prealabilă. Implicit, comanda va fi în modul continuu pentru a crea noi constrângeri; apăsați o dată butonul drept al mouse-ului sau**ESC** pentrru a părăsi comanda.


</div>

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `ArcOrCircle`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/ro
