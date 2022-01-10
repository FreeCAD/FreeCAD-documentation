# PartDesign LinearPattern/ro
---
- GuiCommand:   Name:PartDesign LinearPattern   Workbenches:[[PartDesign Workbench   PartDesign]], Complete|MenuLocation:PartDesign → LinearPattern---


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul **Linear pattern** creează copii uniform distanțate dintr-o funcție(onalitate) într-o direcție liniară. Începând cu v0.17, se pot modela mai multe funcții.


</div>

![](images/PartDesign_LinearPattern_example.svg )

*Deasupra: Un bosaj în formă de L (B), realizat după un bosaj de bază (A, denumit și \"suport\"), este utilizat pentru un model repetitiv liniar. Rezultatul (C) este afișat în partea dreaptă.*

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Select the feature(s) to be patterned. Alternatively, the feature can be selected from a dialogue after step 2.

    :   v0.16 and below Only a single feature can be selected, and it must be the last one at the bottom of the feature tree.
2.  Press the **<img src=images/PartDesign_LinearPattern.png style="width:24px"> '''LinearPattern'''** button.
3.  v0.17 and above Press **Add feature** to add a feature to be patterned. The feature must be visible in the 3D view:
    1.  Switch to the Model tree;
    2.  Select in the tree the feature to be added and press **spacebar** to make it visible in the 3D view;
    3.  Switch back to the Tasks panel;
    4.  Select the feature in the 3D view; it will be added to the list.
    5.  Repeat to add other features.
4.  v0.17 and above Press **Remove feature** to remove a feature from the list, or right-click on the feature in the list and select *Remove*.
5.  Define the Direction. See [Options](#Options.md).
6.  Define the Length (distance) between the last copied occurrence and the original feature.
7.  Set the number of occurrences.
8.  Press **OK** .


</div>

To add or remove features from an existing pattern:

1.  Press **Add feature** to add a feature to be patterned. The feature must be visible in the [3D view](3D_view.md):
    1.  Switch to the Model tree;
    2.  Select in the tree the feature to be added and press **Space** to make it visible in the [3D view](3D_view.md);
    3.  Switch back to the Tasks panel;
    4.  Select the feature in the 3D view; it will be added to the list.
    5.  Repeat to add other features.
2.  Press **Remove feature** to remove a feature from the list, or right-click on the feature in the list and select **Remove**

## Opţiuni

![LinearPattern parameters in v0.16 and below.](images/Linearpattern_parameters.png ) ![LinearPattern parameters in v0.17 and above.](images/Linearpattern_parameters_v017.png )

### Direcția

When creating a linear pattern feature, the **LinearPattern parameters** dialogue offers different ways of specifying the pattern direction.

Atunci când creați o funcție de model repetitiv liniar, dialogul **LinearPattern parameters** oferă diferite modalități de specificare a direcției de repetare a modelului.

#### Schița Axa Orizontală 

Utilizează axa orizontală a schiței pentru direcție.

#### Schiță Axa Verticală 

Utilizează axa vertical a schiței pentru direcție.

#### Schița Axa Normală 


<div class="mw-translate-fuzzy">

v0.17 and above Uses the normal axis of the sketch for direction.


</div>

#### Selectare referințe\... 

Vă permite să selectați fie o linie de referință, fie o margine a unui obiect, sau o linie din schiță care să fie utilizată pentru direcție.

#### Schiță Axă Personalizată 

Dacă schița care definește funcția care urmează să fie modelată conține, de asemenea, o linie de construcție (sau linii), atunci lista derulantă/contextuală va conține o axă de schiță personalizată pentru fiecare linie de construcție. Prima linie de construcție va fi etichetă \"Axă de schiță 0\".

#### Baza (X/Y/Z) axa 


<div class="mw-translate-fuzzy">

v0.17 and above Select one of the Body Origin\'s standard axis (X, Y or Z) as direction. 


</div>

## Limitations


<div class="mw-translate-fuzzy">

## Limitări

-   Formele modelelor nu se pot suprapune reciproc, cu excepția cazului special de numai două apariții (original plus un exemplar)
-   Va fi exclusă orice formă de model care nu se suprapune pe suportul originalului. Acest lucru asigură faptul că o funcție PartDesign constă întotdeauna într-un singur, solid conectat
-   Pentru alte limitări, consultați secțiunea [mirrored feature](PartDesign_Mirrored.md)





</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign LinearPattern/ro
