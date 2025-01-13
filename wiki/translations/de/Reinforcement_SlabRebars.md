---
 GuiCommand:
   Name: Reinforcement SlabRebars
   Name/de: Reinforcement Plattenbewehrung
   MenuLocation: 3D/BIM , Bewehrungswerkzeuge , Slab Reinforcement
   Workbenches: Reinforcement_Workbench/de, BIM_Workbench/de
   SeeAlso: 
---

# Reinforcement SlabRebars/de



## Beschreibung

Das Werkzeug [Reinforcement Plattenbewehrung](Reinforcement_SlabRebars/de.md) ermöglicht dem Anwender Bewehrungsstäbe innerhalb eines [Arch Struktur](Arch_Structure/de.md)-Objekts Platte zu erstellen.

Dieses Werkzeug ist Teil des Arbeitsbereichs [Reinforcement](Reinforcement_Workbench/de.md); dieser ist ein [externer Arbeitsbereich](External_workbenches/de.md), der mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden kann.

<img alt="" src=images/Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:600px;"> 
*Beispiel einer Plattenbewehrung in einem [Arch Struktur](Arch_Structure/de.md)-Objekt Platte*

<img alt="" src=images/Right_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:600px;"> 
*Seitenansicht des Beispiels der Plattenbewehrung*

<img alt="" src=images/Front_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:600px;"> 
*Vorderansicht des Beispiels der Plattenbewehrung*



## Anwendung

1\. Wähle eine beliebige Fläche eines zuvor erstellten Slab-**<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)**-Objekts aus, wie im Bild unten gezeigt.

:   <img alt="" src=images/Selected_face_for_Slab_Arch_Structure.png  style="width:400px;">

:   
    
*Ausgewählte Fläche für Plattenbogenstruktur*
    

2\. Wähle dann **<img src="images/Reinforcement_SlabRebars.svg" width=16px> [Slab Reinforcement](Reinforcement_SlabRebars.md)** aus den Bewehrungswerkzeugen.

3\. Eine Dialog-Box wird sich öffnen, wie unten gezeigt.

:   <img alt="" src=images/Slab_Reinforcement_input_dialog_box.png  style="width:600px;">

:   
    
*Dialogfeld für die Plattenbewehrung*
    

4\. Wähle die gewünschte Abdeckungsart des Armierungsgewebes (oben oder unten).

5\. Wähle den gewünschten Bewehrungstyp und andere Eingabedaten für Bewehrungsstäbe in paralleler Richtung der ausgewählten Fläche, wie in der Abbildung unten gezeigt.

:   <img alt="" src=images/Bent_Shape_rebars_in_parallel_with_distribution_rebars_inputs_for_Slab_Reinforcement.png  style="width:600px;">

:   
    
*Dialogfeld für die Plattenbewehrung der Bewehrungsstäbe in paralleler Richtung zur ausgewählten Fläche*
    

6\. Klicke nun auf **Weiter** oder wähle „Querstäbe" in der Listenansicht aus.

7\. Wähle nun die gewünschten Daten als Eingabedaten für Rabars in Querrichtung der ausgewählten Fläche aus, wie im Bild unten gezeigt.

:   <img alt="" src=images/Bent_Shape_rebars_in_cross_direction_with_distribution_rebars.png  style="width:600px;">

:   
    
*Dialogfeld für die Plattenbewehrung der Bewehrungsstäbe in Querrichtung der ausgewählten Fläche*
    

8\. Klicke auf **OK** oder **Übernehmen** oder **Fertig**, um die Plattenbewehrung zu erzeugen.

9\. Klicke **Abbrechen**, um die Dialog-Box zu verlassen.


## Eigenschaften

**Eigenschaften für Bewehrungsstäbe in paralleler Richtung zur ausgewählten Fläche:**

-    **Mesh Cover Along**: Stellt die Ausrichtung des Bewehrungsnetzes entlang der Ober- oder Unterseite der Struktur dar. Kann zwei Werte haben: „Top" und „Bottom".

-    **Rebar Type**: Bewehrungstyp für parallele Bewehrungsstäbe zur Plattenbewehrung. Kann vier Werte haben: „StraightRebar", „LShapeRebar", „UShapeRebar", „BentShapeRebar".

-    **Front Cover**: Der Abstand zwischen parallelen Bewehrungsstäben und ausgewählter Fläche.

-    **Left Cover**: Der Abstand zwischen dem linken Ende der parallelen Bewehrung und der linken Fläche der Struktur.

-    **Right Cover**: Der Abstand zwischen dem rechten Ende der parallelen Bewehrung und der rechten Fläche der Struktur.

-    **Bottom Cover**: Der Abstand zwischen parallelen Bewehrungsstäben von der Unterseite der Struktur.

-    **Obere Abdeckung**: Der Abstand zwischen parallelen Bewehrungsstäben von der Oberseite der Struktur.

-    **Hintere Abdeckung**: Hintere Abdeckung für die Plattenbewehrung paralleler Bewehrungsstäbe.

-    **Ankerlänge**: Stellt die Armlänge von gebogenen parallelen Bewehrungsstäben dar, wenn der parallele Bewehrungsstabtyp BentShapeRebar ist.

-    **Biegewinkel**: Stellt den Winkel für gebogene parallele Bewehrungsstäbe dar, wenn der parallele Bewehrungsstabtyp BentShapeRebar ist.

-    **Rundung**: Ein Rundungswert, der auf die Ecken der Stäbe angewendet wird, ausgedrückt als Multiplikation mit dem Durchmesser paralleler Bewehrungsstäbe.

-    **Durchmesser**: Durchmesser paralleler Bewehrungsstäbe

-    **Menge**: Enthält die Anzahl paralleler Bewehrungsstäbe.

-    **Abstand**: Enthält den Abstand zwischen parallelen Bewehrungsstäben.

**Eigenschaften von Bewehrungsstäben für gebogene Bewehrungsstäbe in paralleler Richtung zur ausgewählten Fläche:**

-    **Amount**: Enthält die Anzahl der Verteilungsstäbe für gebogene Bewehrungsstäbe in paralleler Richtung.

-    **Spacing**: Enthält den Abstand zwischen Verteilungsstäben für gebogene Bewehrungsstäbe in paralleler Richtung. Bewehrungsstäbe in paralleler Richtung zur ausgewählten Fläche:\'\'\'

**Eigenschaften für Bewehrungsstäbe quer zur ausgewählten Fläche:**

\'\* **Rebar Type**: Bewehrungstyp für Querbewehrungsstäbe zur Plattenbewehrung. Kann vier Werte haben: \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **Front Cover**: Der Abstand zwischen Querbewehrungsstäben und ausgewählter Fläche.

-    **Left Cover**: Der Abstand zwischen dem linken Ende des Querbewehrungsstabs und der linken Fläche der Struktur.

-    **Right Cover**: Der Abstand zwischen dem rechten Ende des Querbewehrungsstabs und der rechten Fläche der Struktur.

-    **Bottom Cover**: Der Abstand zwischen Querbewehrungsstäben von der Unterseite der Struktur.

-    **Top Cover**: Der Abstand zwischen Querbewehrungsstäben von der Oberseite der Struktur.

-    **Rear Cover**: Hintere Abdeckung für Plattenbewehrung von Querbewehrungsstäben.

-    **Ankerlänge**: Stellt die Armlänge gebogener Querbewehrungsstäbe dar, wenn der Querbewehrungstyp „BentShapeRebar" ist.

-    **Biegewinkel**: Stellt den Winkel gebogener Querbewehrungsstäbe dar, wenn der Querbewehrungstyp „BentShapeRebar" ist.

-    **Rundung**: Ein Rundungswert, der auf die Ecken der Stäbe angewendet wird, ausgedrückt in multipliziert mit dem Durchmesser der Querbewehrungsstäbe.

-    **Durchmesser**: Durchmesser der Querbewehrungsstäbe

-    **Menge**: Enthält die Anzahl der Querbewehrungsstäbe.

-    **Abstand**: Enthält den Abstand zwischen den Querbewehrungsstäben.

**Eigenschaften von Verteilungsstäben für gebogene Formstäbe quer zur ausgewählten Fläche:**

-    **Amount**: Enthält die Anzahl der Verteilungsstäbe für gebogene Bewehrungsstäbe in Querrichtung.

-    **Spacing**: Enthält den Abstand zwischen den Verteilungsstäben für gebogene Bewehrungsstäbe in Querrichtung.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md),[Reinforcement-API](Reinforcement_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

-   Das Werkzeug „Reinforcement SlabRebars" kann über die [Python](Python/de.md)-Konsole mithilfe der folgenden Funktion verwendet werden:



### Plattenbewehrung erstellen 


```python
from SlabReinforcement.SlabReinforcement import makeSlabReinforcement
SlabReinforcementGroup = makeSlabReinforcement(
    parallel_rebar_type,
    parallel_front_cover,
    parallel_rear_cover,
    parallel_left_cover,
    parallel_right_cover,
    parallel_top_cover,
    parallel_bottom_cover,
    parallel_diameter,
    parallel_amount_spacing_check,
    parallel_amount_spacing_value,
    cross_rebar_type,
    cross_front_cover,
    cross_rear_cover,
    cross_left_cover,
    cross_right_cover,
    cross_top_cover,
    cross_bottom_cover,
    cross_diameter,
    cross_amount_spacing_check,
    cross_amount_spacing_value,
    cross_rounding = 2,
    cross_bent_bar_length = 50,
    cross_bent_bar_angle = 135,
    cross_l_shape_hook_orintation = "Alternate",
    cross_distribution_rebars_check = False,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 2,
    parallel_rounding = 2,
    parallel_bent_bar_length = 50,
    parallel_bent_bar_angle = 135,
    parallel_l_shape_hook_orintation = "Alternate",
    parallel_distribution_rebars_check = False,
    parallel_distribution_rebars_diameter = 8,
    parallel_distribution_rebars_amount_spacing_check = True,
    parallel_distribution_rebars_amount_spacing_value = 2,
    mesh_cover_along = "Bottom",
    structure = None,
    facename = None,
)
```

-   Erstellt ein `SlabReinforcementGroup`-Objekt aus der angegebenen `structure`, bei der es sich um eine Platten-[Bogenstruktur](Arch_Structure/de.md) handelt, und `facename`, bei der es sich um eine Fläche dieser Struktur handelt.
    -   Wenn weder `structure` noch `facename` angegeben sind, wird die vom Benutzer ausgewählte Fläche als Eingabe verwendet.

**Eigenschaften für Bewehrungsstäbe in paralleler Richtung zur ausgewählten Fläche:**

-    **parallel_rebar_type**: Bewehrungstyp für parallele Bewehrungsstäbe zur Plattenbewehrung. Kann vier Werte haben: „StraightRebar", „LShapeRebar", „UShapeRebar", „BentShapeRebar".

-    **parallel_front_cover**: Der Abstand zwischen parallelen Bewehrungsstäben und ausgewählter Fläche.

-    **parallel_rear_cover**: Hintere Abdeckung für Plattenbewehrung aus parallelen Bewehrungsstäben.

-    **parallel_left_cover**: Der Abstand zwischen dem linken Ende des parallelen Bewehrungsstabs und der linken Fläche der Struktur.

-    **parallel_right_cover**: Der Abstand zwischen dem rechten Ende des parallelen Bewehrungsstabs und der rechten Fläche der Struktur.

-    **parallel_top_cover**: Der Abstand zwischen parallelen Bewehrungsstäben von der Oberseite der Struktur.

-    **parallel_bottom_cover**: Der Abstand zwischen parallelen Bewehrungsstäben von der Unterseite der Struktur.

-    **parallel_diameter**: Durchmesser paralleler Bewehrungsstäbe.

-    **parallel_amount_spacing_check**: Wenn auf True gesetzt, wird der Wert von parallel_amount_spacing_value als Anzahl der Bewehrungsstäbe verwendet, andernfalls wird der Wert von parallel_amount_spacing_value als Abstand zwischen parallelen Bewehrungsstäben verwendet.

-    **parallel_amount_spacing_value**: Enthält die Anzahl der Bewehrungsstäbe oder den Abstand zwischen parallelen Bewehrungsstäben basierend auf dem Wert von amount_spacing_check.

-    **parallel_rounding**: Ein Rundungswert, der auf die Ecken der Stäbe angewendet wird, ausgedrückt in multipliziert mit dem parallel_diameter.

-    **parallel_bent_bar_length**: Stellt die Armlänge von parallel gebogenen Bewehrungsstäben dar, wenn parallel_rebar_type BentShapeRebar ist.

-    **parallel_bent_bar_angle**: Stellt den Winkel für parallel gebogene Bewehrungsstäbe dar, wenn parallel_rebar_type BentShapeRebar ist.

-    **parallel_l_shape_hook_orintation**: Stellt die Ausrichtung des Hakens paralleler L-förmiger Bewehrungsstäbe dar, wenn parallel_rebar_type LShapeRebar ist. Kann drei Werte haben: „Links", „Rechts", „Alternativ".

-    **parallel_distribution_rebars_check**: Wenn True, werden Verteilungsstäbe für parallel gebogene Bewehrungsstäbe hinzugefügt. Standard ist False.

-    **parallel_distribution_rebars_diameter**: Durchmesser der Verteilungsstäbe für parallel gebogene Bewehrungsstäbe.

-    **parallel_distribution_rebars_amount_spacing_check**: Wenn auf True gesetzt, wird der Wert von parallel_distribution_rebars_amount_spacing_value als Anzahl der Bewehrungsstäbe verwendet, andernfalls wird der Wert von parallel_distribution_rebars_amount_spacing_value als Abstand in parallel_distribution_rebars verwendet. Standard ist True.

-    **parallel_distribution_rebars_amount_spacing_value**: Enthält die Anzahl oder den Abstand zwischen den Verteilungsstäben für eine Seite parallel gebogener Bewehrungsstäbe basierend auf dem Wert von parallel_distribution_rebars_check. Standard ist 2.

**Eigenschaften für Bewehrungsstäbe quer zur ausgewählten Fläche:**

-    **cross_rebar_type**: Bewehrungstyp für Querbewehrungsstäbe zur Plattenbewehrung. Kann vier Werte haben: „StraightRebar", „LShapeRebar", „UShapeRebar", „BentShapeRebar".

-    **cross_front_cover**: Der Abstand zwischen Querbewehrungsstab und cross_face (Fläche senkrecht zur ausgewählten Fläche).

-    **cross_rear_cover**: Hintere Abdeckung für Plattenbewehrung von Querbewehrungsstäben.

-    **cross_left_cover**: Der Abstand zwischen dem linken Ende des Querbewehrungsstabs und der linken Fläche der Struktur.

-    **cross_right_cover**: Der Abstand zwischen dem rechten Ende des Bewehrungsstabs und der rechten Fläche der Struktur relativ zu cross_face.

-    **cross_top_cover**: Der Abstand zwischen den Querstäben von der Oberseite der Struktur.

-    **cross_bottom_cover**: Der Abstand zwischen den Querstäben von der Unterseite der Struktur.

-    **cross_diameter**: Durchmesser der Querstäbe.

-    **cross_amount_spacing_check**: Wenn auf True gesetzt, wird der Wert von cross_amount_spacing_value als Anzahl der Bewehrungsstäbe verwendet, andernfalls wird der Wert von cross_amount_spacing_value als Abstand zwischen den Bewehrungsstäben verwendet.

-    **cross_amount_spacing_value**: Enthält die Anzahl der Bewehrungsstäbe oder den Abstand zwischen den Bewehrungsstäben basierend auf dem Wert von cross_amount_spacing_check.

-    **cross_rounding**: Ein Rundungswert, der auf die Ecken der Stäbe angewendet wird, ausgedrückt als multipliziert mit dem cross_diameter.

-    **cross_bent_bar_length**: Stellt die Armlänge von gebogenem Querbewehrungsstahl dar, wenn cross_rebar_type BentShapeRebar ist.

-    **cross_bent_bar_angle**: Stellt den Winkel für gebogenen Querbewehrungsstahl dar, wenn cross_rebar_type BentShapeRebar ist.

-    **cross_l_shape_hook_orintation**: Stellt die Ausrichtung des Hakens von L-förmigem Querbewehrungsstahl dar, wenn cross_rebar_type LShapeRebar ist. Kann drei Werte haben: „Links", „Rechts", „Alternativ"

-    **cross_distribution_rebars_check**: Wenn True, werden Verteilungsstäbe für kreuzgebogene Bewehrungsstäbe hinzugefügt. Standard ist False.

-    **cross_distribution_rebars_diameter**: Durchmesser für Verteilungsstäbe für kreuzgebogene Bewehrungsstäbe.

-    **cross_distribution_rebars_amount_spacing_check**: Wenn auf True gesetzt, wird der Wert von cross_distribution_rebars_amount_spacing_value als Anzahl der Bewehrungsstäbe verwendet, andernfalls wird der Wert von cross_distribution_rebars_amount_spacing_value als Abstand in cross_distribution_rebars verwendet. Standard ist True.

-    **cross_distribution_rebars_amount_spacing_value**: Enthält die Anzahl oder den Abstand zwischen den Verteilungsbewehrungsstäben für eine Seite der kreuzgebogenen Bewehrungsstäbe basierend auf dem Wert von cross_distribution_rebars_check. Standard ist 2.

**Gemeinsame Eigenschaften für parallele und Querbewehrungsstäbe:**

-    **mesh_cover_along**: Kann zwei Werte haben: „Top" und „Bottom". Stellt die Ausrichtung des Bewehrungsgeflechts entlang der Ober- oder Unterseite der Struktur dar.

-    **structure**: Bogenstrukturobjekt. Standard ist Keine

-   ​​**facename**: ausgewählte Seite der Struktur. Standard ist Keine



### Ausgabe der Plattenbewehrung 

Die Eigenschaften der Plattenbewehrung kannst du mit der folgenden Funktion ändern:


```python
from SlabReinforcement.SlabReinforcement import editSlabReinforcement
slabReinforcementGroup = editSlabReinforcement(
    slabReinforcementGroup,
    parallel_rebar_type,
    parallel_front_cover,
    parallel_rear_cover,
    parallel_left_cover,
    parallel_right_cover,
    parallel_top_cover,
    parallel_bottom_cover,
    parallel_diameter,
    parallel_amount_spacing_check,
    parallel_amount_spacing_value,
    cross_rebar_type,
    cross_front_cover,
    cross_rear_cover,
    cross_left_cover,
    cross_right_cover,
    cross_top_cover,
    cross_bottom_cover,
    cross_diameter,
    cross_amount_spacing_check,
    cross_amount_spacing_value,
    cross_rounding = 2,
    cross_bent_bar_length = 50,
    cross_bent_bar_angle = 135,
    cross_l_shape_hook_orintation = "Alternate",
    cross_distribution_rebars_check = False,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 2,
    parallel_rounding = 2,
    parallel_bent_bar_length = 50,
    parallel_bent_bar_angle = 135,
    parallel_l_shape_hook_orintation = "Alternate",
    parallel_distribution_rebars_check = False,
    parallel_distribution_rebars_diameter = 8,
    parallel_distribution_rebars_amount_spacing_check = True,
    parallel_distribution_rebars_amount_spacing_value = 2,
    mesh_cover_along: str = "Bottom",
    structure = None,
    facename = None,
)
```

-    `slabReinforcementGroup`ist ein zuvor erstelltes `Slab Reinforcement`-Gruppenobjekt.

-   Die anderen Parameter sind dieselben, die von der Funktion `makeSlabReinforcement()` benötigt werden.



### Beispiele für Plattenbewehrung 

-   [Plattenspannung in zwei Richtungen](Example_Slab_Spanning_in_Two_Directions/de.md)

<img alt="" src=images/Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:800px;">

-   [Plattenspannung in eine Richtung](Example_Slab_Spanning_in_One_Direction/de.md)

<img alt="" src=images/Slab_spanning_in_one_Direction.png  style="width:800px;">

-   [Platte mit geradem Bewehrungsnetz](Example_Slab_Having_Mesh_Of_Straight_Rebars/de.md)

<img alt="" src=images/Slab_having_straight_rebars_in_both_direction.png  style="width:800px;">

-   [Platte mit U-förmigem Bewehrungsnetz](Example_Slab_Having_UShape_Rebars_Reinforcement_Mesh/de.md)

<img alt="" src=images/U-shape_rebars_isometric_view.png  style="width:800px;">

-   [Platte mit L-förmigem Bewehrungsnetz](Example_Slab_Having_LShape_Rebars_Reinforcement_Mesh/de.md)

<img alt="" src=images/L-Shape_Rebars_isometric_view.png  style="width:800px;">




{{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement SlabRebars/de
