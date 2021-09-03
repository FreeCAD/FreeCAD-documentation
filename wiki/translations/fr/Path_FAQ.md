

## FAQ Atelier Path {#faq_atelier_path}


<div class="mw-translate-fuzzy">

### Combien d\'axes l\'atelier Path peut-il traiter ? {#combien_daxes_latelier_path_peut_il_traiter}


</div>

Pour le moment, en version 0.18, l\'atelier Path peut gérer jusqu\'à 3 axes. Actuellement, les capacités du 4ème axe sont en cours de développement pour la prochaine version officielle, avec certaines opérations de l\'atelier Path déjà mises à niveau vers le statut de base du 4ème axe.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Pourquoi, dans certaines instances, l\'atelier Path propose-t-il plus d\'un moyen pour spécifier une Opération ? {#pourquoi_dans_certaines_instances_latelier_path_propose_t_il_plus_dun_moyen_pour_spécifier_une_opération}


</div>

L\'atelier Path fournit des outils permettant de réaliser de nombreuses opérations de fraisage, d\'autres étant en élaboration et comme FreeCAD est à code ouvert, rien n\'empêche les utilisateurs de créer leurs propres fonctionnalités.

Dans le dessin 3D, il existe souvent plusieurs méthodes disponibles qui peuvent être avantageuses à utiliser pour des opérations Job différents. Dans certains cas, des combinaisons d\'opérations sont utilisées pour fournir un fraisage complet du Stock.

Un exemple habituel est que l\'opération Contour peut être générée depuis Edges ou Faces. Dans certains cas, il peut y avoir un avantage à utiliser l\'une ou l\'autre des méthodes.

[top](#top.md)

## Why does Dressing up an Operation change the position in the Job Workflow shown in the Operations list? {#why_does_dressing_up_an_operation_change_the_position_in_the_job_workflow_shown_in_the_operations_list}

All additions to the Job\--including modifications, and Operation copies\--are appended at the end of the Job Workflow. If that disrupts the correct Job sequence, it must be reordered in the Job editor-\>Workflow tab.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Quelle est la différence entre Clearance Height et Safe Height? {#quelle_est_la_différence_entre_clearance_height_et_safe_height}


</div>

Des informations plus détaillées sont disponible sur [ Depths and Heights](Template:Depths/Heights.md).

[top](#top.md)


<div class="mw-translate-fuzzy">

### Quelle est l\'utilisation habituelle de SetupSheet? {#quelle_est_lutilisation_habituelle_de_setupsheet}


</div>

Le SetupSheet est un masque de saisie dédié, contenu dans un Job, modifié dans la vue Property, seulement accessible depuis Path workbench. Il fournit une méthode pour configurer les éléments d\'un Job en utilisant les Values et les Expressions du SetupSheet aux utilisateurs experts.

Les entrées courantes pour Depths, Heights, et Tool Controllers comprennent:

1.  Final Depth Expression \-- OpFinalDepth
2.  Start Depth Expression \-- OpStartDepth
3.  Step Down Expression \-- Defaults to OpToolDiameter. Cette expression est utilisée à chaque Operation pour calculer les valeurs par défaut de descente (Step down) en fonction du diamètre de l\'outil (Tool) défini dans le gestionnaire d\'outils (Tool controller) associé.
4.  Clearance Height Expression \-- StartDepth+SetupSheet.ClearanceHeightOffset
5.  Clearance Height Offset Value \-- Contient la valeur utilisée dans Expressions
6.  Safe Height Expression \-- StartDepth+SetupSheet.SafeHeightOffset
7.  Safe Height Offset Value \-- Contient la valeur utilisée dans Expressions
8.  Horizontal Rapid Value \-- Fournit la valeur par défaut utilisée pour renseigner le taux d\'avance horizontale rapide (Horizontal Rapid Feed) pour tous les gestionnaires d\'outils.
9.  Vertical Rapid Value \-- Fournit la valeur par défaut utilisée pour renseigner le taux d\'avance verticale rapide (Vertical Rapid Feed) pour tous les gestionnaires d\'outils.

Cela permet d\'avoir de la flexibilité. Par exemple, les expressions par défaut sont fournies mais peuvent être modifiées par l\'utilisateur. La modification peut même réduire l\'équation par défaut à une Value si cela convient à l\'utilisateur.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Quelle est l\'utilisation habituelle de Job Templates?? {#quelle_est_lutilisation_habituelle_de_job_templates}


</div>

Job templates permet de sauvegarder les définitions de Job les plus communes et de les réutiliser pour les Jobs avec une configuration similaire.

[top](#top.md)

## How many Base objects does Path workbench support? {#how_many_base_objects_does_path_workbench_support}

Support exists only for a single Base object. To create paths for multiple solids in a single Job you can make a Compound out of them and use that as the base object for the Job.

[top](#top.md)

## Why does an Operation not produce usable output? {#why_does_an_operation_not_produce_usable_output}

A variety of reasons exist that may cause an individual Operation to generate no output.

One common reason is that the Tool geometry defined in the Tool controller selected for the Operation is too large to fit within the geometry selected on the 3D model for the Operation.

Be aware that this will typically exhibit as a Rapids movement to where the Operation beginning, completed by a Rapid Z movement to the geometry selected to define the Operation, and then a return to Rapid transit height.

Another common misunderstanding is that a Contour Operation is not outputting paths, when the Contour editor Operation-\>Cut Side is \"Inside\", the default, and toggling the 3D Model viability allows them to be seen.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Path Workbench peut-il effectuer des fraisages de surface en 3D? {#path_workbench_peut_il_effectuer_des_fraisages_de_surface_en_3d}


</div>

Oui, Path fournit des Operations de fraisage de surfaces 3D. Cela necessite l\'installation d\'OpenCamLibrary, un module Open Source d\'un fournisseur extérieur, dans le répertoire des fichiers de Macros.

OpenCamLibrary n\'est pas intégrée à FreeCAD pour s\'assurer qu\'aucune violation de licence ne se produise.

[top](#top.md)


<div class="mw-translate-fuzzy">

### Quoi faire si les stratégies d\'Operation par défaut ne correspondent pas à mes besoins? {#quoi_faire_si_les_stratégies_doperation_par_défaut_ne_correspondent_pas_à_mes_besoins}


</div>

Pour les Pocket Operations, le point de départ (Start Point) par défaut est en XYZ = 000 et est toujours validé mais il peut aussi être configuré dans la fenêtre Property. Les Operations Pocket et Facing sont pré-selectionnées en Climb plutôt qu\'en Cut Mode conventionnel dans l\'onglet Operation.

For Contour style Operations, the Operation tab has a \"Direction\" input that may be configured as CW, or CCW, which defines the cut direction. For reference:

1.  Cut Side = Outside, Cut Direction = CCW, Climb Cut
2.  Cut Side = Outside, Cut Direction = CW, Conventional Cut
3.  Cut Side = Inside, Cut Direction = CW, Conventional Cut

Cut Side = Inside, Cut Direction = CCW, Climb Cut

Start Points can be enabled\--and configured in the Property view window.

In FaceMill Operations Material Allowance can be specified, allowing overcutting for positive values, and undercutting for negative values.

In Contour and Pocket Operations, the Extra Offset serves the same purpose.

These inputs are valuable, allowing functionality including:

1.  Defining Roughing Passes, in conjunction with the Depths input fields.
2.  Specifying overcut for Facing operations
3.  Features smaller than the Tool diameter, that must be faced, can benefit from specifying an Outside Contour cut with a negative Extra Offset value.

Judicious care should be exercised when specifying Material Allowances and Offsets, at the risk of undesired cuts into the Stock.

[top](#top.md)

## What do I do if an Operation generates more Vertical movements than my Job can tolerate? {#what_do_i_do_if_an_operation_generates_more_vertical_movements_than_my_job_can_tolerate}

Operations such as 3D\_Pocket, Pocket\_Shape, and FaceMill, but not Contour Operations have a configuration option to keep the tool down, in the Data tab of the Property View.

[top](#top.md)

## How can I leave tabs to clamp my milled work? {#how_can_i_leave_tabs_to_clamp_my_milled_work}

Path workbench provides a Tag dressup for just this purpose.

[top](#top.md)

## What is a Postprocessor? {#what_is_a_postprocessor}

The Postprocessor is used to tailor output code to target CNC controllers for various machines, in their G-Code dialect.

[top](#top.md)

## Can I modify an existing, or make my own Postprocessor? {#can_i_modify_an_existing_or_make_my_own_postprocessor}

Postprocessors are Python scripts, and are saved in the Macro file path. They are intended to be modified, or used as a template for further Postprocessor development.

[top](#top.md)

## I only want to use one Postprocessor\--can I make it the default, or hide other options? {#i_only_want_to_use_one_postprocessor__can_i_make_it_the_default_or_hide_other_options}

Yes, The path preferences has a section for post processors where you can select which post processors to display and select a default post.

[top](#top.md)

## How I can set metric/imperial units for my path object? {#how_i_can_set_metricimperial_units_for_my_path_object}

The 3D model units are defined in the Edit-\>Preferences\...\>General-\>Units tab\'s User System drop menu.

The Units setting configuring how the the target mill interprets the Job G-Code is set in the output Postprocessor, which inserts a G20, or a G21 G-Code command to indicate inches or millimeters, respectively.

The Postprocessor also is configured for Units/Second, or Units/Minute. If set for Units/Minute, the Path workbench internal G-Code dialect Feed rate is multiplied by 60.

Mismatches between the 3D model and Postprocessor settings are likely culprits for factor of 60 errors in Feed rate, and factors of 25.4 in distance.

[top](#top.md)

## How I can simulate my milling strategies? {#how_i_can_simulate_my_milling_strategies}

A volumetric simulator is provided to view the result of cutting the tool geometries included in the Job Operations against the Stock.

If the path lines obscure the simulation result, their visibility should be toggled off before simulation.

[top](#top.md)

## What is the significance of the path line colors? {#what_is_the_significance_of_the_path_line_colors}

Path line colors are defined in the Edit-\>Preference\...-\>Path-\>Path colors tab. Default colors include:

1.  Green for normal paths.
2.  Red for rapid paths.
3.  Yellow for Probed paths.

[top](#top.md)

## How do I Enable/Disable visibility of path lines? {#how_do_i_enabledisable_visibility_of_path_lines}

Path workbench allows control of the display of path lines by toggling the visibility of the Job by selecting it in the Combo View. The visibility of individual or groups of Operations are then toggled from the Combo View.

[top](#top.md)

## How do I check that my G-Code sequence is correct? {#how_do_i_check_that_my_g_code_sequence_is_correct}

By default, the Postprocessor output is displayed in a window before saving. This\--along with the Path CAM simulator provide a means to examine the Job before processing it on a CNC machine. The G-Code inspection tool allows you to inspect the internal Path G-Code for each Operation, providing a means to trace whether the output of the Postprocessor reflects what is defined in the Operation.

The Operations list in the Combo View panel displays the sequence that the operations will be processed in the Job. If the Operations are correct, but not in the desired sequence, that can be adjusted by double clicking the Operations list and dragging the Operations to their proper location, or by double clicking the Job editor and selecting the Workflow tab, then using the Up/Down arrows on selected Operations to sort them.

[top](#top.md)

## Why am I not getting correct G-Code output from my Postprocessor for Operations inserted using the Partial Command-\>Custom command? {#why_am_i_not_getting_correct_g_code_output_from_my_postprocessor_for_operations_inserted_using_the_partial_command_custom_command}

Commonly, the Custom G-Code command because the format is always in Units/second, it can cause factor of 60 errors for CNC machine targets that operate in Units/minute.

[top](#top.md)

## Why do changes to Placement values in the Property View not seem to work correctly in Path workbench? {#why_do_changes_to_placement_values_in_the_property_view_not_seem_to_work_correctly_in_path_workbench}

\"The Path feature also holds a Placement property. Changing the value of that placement will change the position of the Feature in the 3D view, although the Path information itself won\'t be modified. The transformation is purely visual. This allows you, for example, to create a Path around a face that has a particular orientation on your model, that is not the same orientation as your cutting material will have on the CNC machine.

However, Path Compounds can make use of the Placement of their children (see below).\"

[https://www.freecadweb.org/wiki/Path\_scripting Path scripting](https://www.freecadweb.org/wiki/Path_scripting_Path_scripting.md)

[top](#top.md)

## Why does Path workbench on my computer seem to miss functionality that I see in other users forum posts? {#why_does_path_workbench_on_my_computer_seem_to_miss_functionality_that_i_see_in_other_users_forum_posts}

By default, Experimental functionality is hidden in Path workbench.

[top](#top.md)

## Why do Youtube videos posted by Path workbench developers appear out of synch with the Path workbench? {#why_do_youtube_videos_posted_by_path_workbench_developers_appear_out_of_synch_with_the_path_workbench}

Path workbench shifted dramatically from FreeCAD v0.16 to v0.17, and any videos posted prior to January 1st, 2018, are very likely to contain information that is no longer in synch with v0.17 of FreeCAD Path workbench.

[top](#top.md)

## Why are arcs not round, but are made of a set of straight lines? {#why_are_arcs_not_round_but_are_made_of_a_set_of_straight_lines}

This is only a matter of displaying the path. You can change this in the preferences: Load Path workbench.

1.  open Preferences-\>Path-\>Job Preferences
2.  set the values for *Default Geometry Tolerance* and *Default Curve Accuracy* to small values but not to 0, e.g. to 0.01mm.
3.  confirm the change
4.  Restart FreeCAD.

[top](#top.md)





{{Path_Tools_navi

}} 
