---
- GuiCommand:/ro
   Name:PartDesign PolarPattern
   Name/ro:PartDesign PolarPattern
   Workbenches:[PartDesign](PartDesign_Workbench/ro.md)
   MenuLocation:PartDesign → PolarPattern
---


</div>

## Descriere

Instrumentul **PolarPattern** ia o funcție selectată ca intrare și creează plecând de la aceasta un set de copii rotite (în jurul unei axe date). Începând cu v0.17, se pot modela mai multe funcții.

![](images/PartDesign_PolarPattern_example.png )

*Above: a slot-shaped pocket (B) made on top of a base solid (A, also referred to as support) is used for a polar pattern. The result (C) is shown on the right.*


<div class="mw-translate-fuzzy">

## Cum se folosește {#cum_se_folosește}


</div>

#### To create a pattern {#to_create_a_pattern}

1.  (Optional) Select the feature (<small>(v0.19)</small>  or several features) to be patterned.
2.  Press the **<img src=images/PartDesign_PolarPattern.svg style="width:24px">** **PolarPattern** button.
    -   If you didn\'t initially select any features, you\'ll be able to select a *single* base feature
3.  Define the **Axis**. See [Options](#Options.md).
4.  Define the **Angle** between the last copied occurrence and the original feature.
5.  Set the number of **Occurrences**.
6.  If you have several features in the pattern, their order can be important, see the image below.
7.  Press **OK**.

#### Ordering features {#ordering_features}

![](images/PartDesign_feature-order.gif ) *Effect of the feature order*


<small>(v0.19)</small> 

You can change the order by dragging the feature in the list and you will see the result immediately as preview.

#### Adding features {#adding_features}

###### v0.18

1.  Press **Add feature** to add a feature to be patterned. The feature must be visible in the [3D view](3D_view.md):
2.  Switch to the Model tree;
3.  Select in the tree the feature to be added and press **Spacebar** to make it visible in the [3D view](3D_view.md);
4.  Switch back to the Tasks panel;
5.  Select the feature in the 3D view; it will be added to the list.
6.  Repeat to add other features.

###### v0.19

1.  Press **Add feature** to add a feature to be patterned.
2.  Switch to the Model tree;
3.  Select in the tree the feature to be added.
4.  Repeat to add other features.

#### Removing features {#removing_features}

-   Right-click on the feature in the list and select *Remove*.

or

###### v0.18 {#v0.18_1}

1.  Press **Remove feature** to remove a feature from the list. The feature must be visible in the [3D view](3D_view.md):
2.  Switch to the Model tree;
3.  Select in the tree the feature to be removed and press **Spacebar** to make it visible in the [3D view](3D_view.md);
4.  Switch back to the Tasks panel;
5.  Select the feature in the 3D view; it will have been removed from the list.
6.  Repeat to remove other features.

###### v0.19 {#v0.19_1}

1.  Press **Remove feature** to remove a feature from the list.
2.  Switch to the Model tree;
3.  Select in the tree the feature to be removed.
4.  Repeat to remove other features.

## Opțiuni

![](images/Polarpattern_parameters.png )

### Axis

Atunci când se creează o caracteristică de model polar, dialogul \'Parametrii de tip polar\' oferă modalități diferite de a specifica axa de rotație a modelului.

#### Axa Normalăa schiței {#axa_normalăa_schiței}

O axă care este normală față de schiță și pornind de la originea schiței funcției utilizate este considerată ca axă pentru modelul polar.
Direcția modelului poate fi inversată prin bifarea \'Direcție inversă\'.

#### Axa orizontală a schiței {#axa_orizontală_a_schiței}

Uses the horizontal axis of the sketch for axis.

#### Axa verticală a schiței {#axa_verticală_a_schiței}

Uses the vertical axis of the sketch for axis.

#### Schiță Axă Personalizată {#schiță_axă_personalizată}

Dacă schița care definește funcția care urmează să fie modelată conține, de asemenea, o linie de construcție (sau linii), atunci lista derulantă/contextuală va conține o axă de schiță personalizată pentru fiecare linie de construcție. Prima linie de construcție va fi etichetă \"Axă de schiță 0\".

#### Baza (X/Y/Z) axa {#baza_xyz_axa}


<small>(v0.17)</small> 

Select one of the Body Origin\'s standard axis (X, Y or Z) as axis.

#### Selectare referințe\... {#selectare_referințe...}

Allows you to select either a DatumLine or an edge of an object or a line of a sketch to use for axis.

### Unghiuri și apariții {#unghiuri_și_apariții}

Specifică unghiul care trebuie acoperit de model și numărul total de forme (inclusiv caracteristica originală). De exemplu, patru apariții la un unghi de 180 de grade ar da o distanță de 60 de grade între modele. Există o excepție: dacă unghiul este de 360 ​​de grade, deoarece prima și ultima apariție sunt identice, cele patru apariții vor fi distanțate la 90 de grade. {{Clear}}

## Limite

-   Vedere [Repetiție Liniară](PartDesign_LinearPattern/ro#Limitări.md).








{{PartDesign Tools navi

}} 
