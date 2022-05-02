# Flamingo Workbench/pl
**Środowisko pracy Flamingo (Python2/Qt4) zostało zastąpione przez środowisko pracy Dodo (Python3/Qt5). Ta strona wiki przedstawia różnice między tymi dwoma środowiskami. Obecnie [środowisko pracy Dodo](Dodo_Workbench/pl.md) odnosi się do tej strony.**

## Wprowadzenie

Jest to zestaw dostosowanych poleceń i obiektów programu FreeCAD, które pomagają przyspieszyć rysowanie ram i rurociągów.



:   \"**Flamingo** jest przeznaczony dla wersji używających środowiska Python \> 2.7 i zestawu narzędzi Qt4.





:   \"**Dodo** jest przeznaczony dla wersji używających środowiska Python \> 3.6 i zestawu narzędzi Qt5.



Dla wygody narzędzia Flamingo / Dodo są pogrupowane w trzy paski narzędziowe/menu + jeden zestaw narzędzi.

![](images/flamingoBlob.png )

![](images/dodoBlob.png )

-   **Narzędzia ram**: służą do rozmieszczania ram, kratownic i podobnych elementów w programie FreeCAD przy użyciu obiektów Konstrukcji modułu Arch. \.../flamingo/tutorial/tutorialFrame.pdf
-   **Narzędzia rur**: to logiczna kontynuacja narzędzia ram, ponieważ zajmuje się tworzeniem rurociągów i konstrukcji rurowych. Posiada również własne klasy Python do tworzenia obiektów rurociągów, takich jak rury, kolanka, kołnierze itp. \.../flamingo/tutorials/tutorialPype2.pdf
-   **Narzędzia Eagle**: to w zasadzie dodatek i skrót do bardzo profesjonalnego programu [FreeCAD-PCB](https://github.com/marmni/FreeCAD-PCB) *(dostępnego także w repozytorium dodatków programu FreeCAD)* do importowania pozycji obiektów z pliku .brd programu Eagle na płytce drukowanej narysowanej w programie FreeCAD za pomocą programu a.m., odnoszący się tylko do ich nazw. Jest to także początek, a właściwie nazwa całego środowiska pracy. \.../flamingo/tutorial/tutorialEagle.pdf

:\* Pasek narzędzi **Przybory** umożliwia wyszukiwanie obiektów w modelu i ich odległości, przesuwanie / obracanie płaszczyzny roboczej oraz mały hack okna dialogowego [Linia łamana](Draft_Wire/pl.md) środowiska Rysunek Roboczy, który pozwala na zmianę położenia płaszczyzny roboczej w locie.

## Bibliografia

-   Autor: oddtopus
-   Kod źródłowy na platformie GitHub:

<https://github.com/oddtopus/flamingo>

<https://github.com/oddtopus/dodo>

## Instalacja

To środowisko pracy może być zainstalowane z <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md). Aby zainstalować je samodzielnie zobacz stronę [Instalacja zewnętrznych środowisk pracy](Installing_more_workbenches/pl.md).

## Narzędzia do ram 


<div class="center" style="width: auto; margin-left: auto; margin-right: auto;">

![](images/Flamingos_frame2.jpg )


</div>


:   1\) Umieść jedną belkę na jednej krawędzi *(klasa frameIt)*

W przypadku obiektu belki i krawędzi w modelu narzędzie to nakłada belkę na krawędź, zaznaczając je kolejno aż do naciśnięcia klawisza **ESC**.

:   2\) Wypełnij ramę *(klasa fillFrame)*

Okno dialogowe służące do tworzenia na wielu krawędziach zaznaczonych w rzucie belek o typie wybranym wcześniej, spośród tych występujących w modelu.

Za pomocą przycisku **Wybierz** można zmienić typ belki.


**Dodo: ta funkcja została zastąpiona w oknie dialogowym "Wstaw rozgałęzienie ramy" przyciskiem **Dodaj pojedynczy**.**


:   3\) Wstaw ścieżkę *(klasa insertPath)*.

Narzędzie do tworzenia ciągłego obrysu na ścieżce zdefiniowanej przez krawędzie zaznaczone w rzutni, nawet jeśli nie stykają się one ze sobą, przecinają się w środku lub należą do różnych obiektów. Jedynym ograniczeniem jest istnienie przecięcia dwóch kolejnych krawędzi w kolejności, w jakiej zostały one wybrane. Również linia środkowa otrzymuje właściwości widoku linii środkowej, tj. pomarańczowy kolor i kreskowanie.

:   4\) Wstaw przekrój *(klasa insertSection)*.

Okno dialogowe do tworzenia zestawu profili, które będą używane w modelu dla obiektu FrameLine.

-   Lista **Przekroje**: zawiera wszystkie przekroje zdefiniowane w pliku .csv odpowiadającym wybranemu typowi przekroju.
-   Lista **Typy przekrojów**: typy przekrojów zdefiniowane za pomocą plików .csv znajdujących się w folderze /tables
-   Przycisk **Wstaw**: tworzy grupę \"Profile\_zestaw\", jeśli jeszcze nie istnieje, i dodaje do niej obiekt wybranego profilu.

Inne tabele profili można tworzyć poprzez dodanie odpowiedniego pliku .csv w folderze /tables. Zasady tworzenia i dostosowywania takich tabel są podobne do tych, które obowiązują w przypadku linii rurowych.

Inne profile można szkicować w modelu i przeciągać do grupy \"Profile\_zestaw\".

Orientacja dwuteowników może mieć wpływ na odwzorowanie belek.


**Dodo: zmieniono zakres działania tej funkcji.
W dodo otwiera okno dialogowe, w którym można utworzyć 10 kształtów przekroju belki o niestandardowych wymiarach:
* kwadrat wydrążony i pełny,
* okrąg wydrążony i pełny,
* T, I, C, L, Z,
* Ω ''(omega)''.
Możliwa jest także zmiana położenia środka lub edycja istniejącego przekroju..**


:   5\) Menedżer linii ram *(klasa FrameLineManager)*.

Podobnie jak w przypadku obiektów \"linii rur\", jest to okno dialogowe do tworzenia i zmiany właściwości obiektów \"linii ram\".

Podobnie jak powyżej, linie ramy są obiektami, które gromadzą właściwości wspólne dla zestawu belek *(mianowicie przekrój belki)*, które są włączone do wspólnej grupy w drzewie modelu. Posiadają one również opcjonalną właściwość `.Base`, domyślnie ustawioną na wartość `None`, która jest linią środkową belek ramy. Po zdefiniowaniu ścieżki o aliasie .Base *(DWire lub Szkic)* można dodawać inne belki do linii ramy, ale zostaną one usunięte po wywołaniu polecenia **Przerysuj**. W oknie dialogowym dostępne są następujące funkcje:

-   lista profili belek włączonych wcześniej do modelu przez okno dialogowe \"Wstaw przekroje standardowe\" *(czytaj dalej)*,
-   pole wyboru, aby wybrać aktywną linię ramy spośród już utworzonych lub wartość `nowa`, aby utworzyć nową,
-   pole tekstowe, w którym należy wpisać nazwę tworzonej linii szkieletowej. Jeśli nie zostanie wpisana żadna nazwa lub zostanie wpisane słowo `name`, linia szkieletowa zostanie nazwana domyślnie `Telaio00n`,
-   przycisk **Wstaw**: tworzy nowy obiekt FrameLine lub dodaje nowe elementy do tego, który został wybrany w polu wyboru, jeśli w aktywnej rzutni zaznaczone są krawędzie,
-   przycisk **Przerysuj**: tworzy nowe belki i umieszcza je nad wybraną ścieżką. Nowe belki zostaną zebrane wewnątrz grupy FrameLine. Opcja nie tworzy ani nie aktualizuje belek dodanych do linii FrameLine poza zdefiniowaną ścieżką,
-   przycisk **Wyczyść**: usuwa wszystkie belki w grupie FrameLine. Dotyczy to również belek dodanych do linii FrameLine poza jej zdefiniowaną ścieżką,
-   przycisk **Pobierz ścieżkę**: przypisuje wybrany dwuteownik do atrybutu Ścieżka obiektu FrameLine,
-   przycisk **Pobierz profil**: zmienia atrybut Profil obiektu FrameLine na taki, jaki posiada belka wybrana w rzutni lub wybrany z listy,
-   pole wyboru {{CheckBox|TRUE|Kopiuj profil}}: zaznaczenie tego pola powoduje wygenerowanie nowego obiektu profilu dla każdej belki, aby uniknąć wielokrotnych odniesień w modelu,
-   pole wyboru {{CheckBox|Przesuń do początku}}: jeśli jest zaznaczone, przesuwa środek masy profilu do początku układu współrzędnych: dzięki temu linia środkowa belki pokrywa się z punktem środkowym profilu.

Jeśli nazwa obiektu FrameLine zostanie zmieniona, automatycznie zmieni się także nazwa odpowiedniej grupy, ale nie odwrotnie.

:   6\) FrameBranch manager

Similar to the analogous feature in the Pype menu, this is a container for beams structured on a .Base. The base can be a DWire, a Sketch or also the edges of a solid shape. When the underlying base is changed, also the position and length of the beams is modified accordingly. It\'s possible to trim/extend to any geometry the beams and rotate the sections aroud the center-line through the commands provided in the dialog: in this way the modification is not lost when the document is recomputed.

-   **OK** creates one framebranch over the pre-selected geometry
-   **Cancel** closes the dialog
-   the **** text box allow to insert a custom name to the feature
-   the **combo box** allow to select the type of section that will be displayed in the **list box**. (see ../Mod/flamingo/shapes or ../Mod/dodo/shapez to customize)
-   **AddBeams** adds one member to a frame to the currently selected edge. The edge must belong to an existing framebranch
-   **RemoveBeams** removes the selected beam from the corresponding edge
-   **ChangeProfile** change the profiles to the framebranch. To select the framebranch just select in the view area one of its members.
-   **Get targets** selects geometry from the view area to trim/extend to the beams. Targets can also not belong to any framebranch.
-   **Trim/Extend** changes the lenght of selected members to the targets
-   **Add single** creates one beam, of the specified ****, not linked to the base on any edge or surface selected.
-   **Redraw** recreates the frame, deleting all the offsets and rotations

When one beam belonging to a framebranch is selected in the view area, the TAIL is visually highlighted. That allows to change manually the offsets of tail and head, beside the rotation of the section, using the commands provided in the dialog.

:   7\) Spin beams by 45 deg. (class spinSect)

Tool to spin one object around the \"Z\" axis of its shape by 45 degrees.

:   8\) Reverse orientation (class reverseBeam)

Tool to spin one object around the \"X\" axis of its shape by 180 degrees. Notes: if one edge of the object is selected, that is used as the pivot of rotation.

:   9\) Shift the beam (class shiftBeam)

Okno dialogowe do przesuwania i kopiowania obiektów.

**X**, **Y** and **Z** textboxes for direct input the amount of translation in each direction.

**Multiple** textbox is the multiple coefficient of the translation amount.

**Steps** textbox is the denominator of the translation amount. It\'s used when the amount of translation is to be covered in some steps.

**Get displacement** button to take the amount and direction of translation from the distance of selected entities (points, edges, faces) or even from a single edge. In the latter case, a green arrow is displayed to show the direction.

**OK** to perform the action and **Cancel** to close the dialog.

:   13\) Rotate + mate the edges (class rotJoin)

Tool to translate and rotate the beams to mate two edges. Same as above but it also makes the edges co-linear.

:   10\) pivotTheBeam (class pivotBeam)

Dialog to rotate one beam or other object around one of its edges.

**Angle** textbox to insert the degree of rotation.

**Reverse** button to rotate in the opposite direction, if necessary.

**OK** to perform the action and **Cancel** to close the dialog.

:   11\) Flush the surfaces (class levelBeam)

Tool to flush the parallel faces of two objects. Actually the command takes to the same level, respect the position and orientation of the first face selected, the center-of-mass of all faces selected. Thus it translates the objects even if the faces are not parallel.

:   12\) Mate the Edges (class alignEdge)

Tool to mate two parallel edges. Actually the command moves the objects along the minimum distance of their selected edge to the first one. Thus it translates the object even if edges are not parallel and it\'s a good way to place objects in desired position. It is also possible to select two edges of the same objects. With this method is possible to move quickly one object by steps defined on its own geometry.

:   14\) alignFlange (class alignFlange)

Dialog to rotate beams so that their surfaces are parallel to one reference plane.

It\'s possible to preselect the reference face before invoking the command.

The three **XY**, **XZ** and **YZ** buttons allow to choose directly the orientation of principal planes as the reference.

Finally it\'s possible to enter directly the new orientation of faces by the three coordinates of the normal and the button **Set normal**.

:   15\) Stretch the beam (class stretchBeam)

Dialog to change the length of beams.

In the textbox write the new length that will be applied to selected beams or pipes. Otherwise **Get Length** button takes the new length from the selected geometry (either the length of a beam or edge or the distance between geometric entities).

With the slider it\'s possible to change the length wirtten in the text-box from -100% to +100%.

Radio buttons **Head** and **Tail** allow to choose the side of the beam that will be changed.

:   16\) Extend the beam (class extend)

Dialog to extend one beam to one selected target.

If entities are preselected before calling this command, the first entity is automatically taken as target and the object attached to it is removed from the selection set. In any case it\'s possible to change the target object with the push-button **Select**.

:   17\) Adjust frames\' angle (class adjustFrameAngle)

Tool to adjust the beams at square angles of frames. To understand at best how it works, refer to the previous tutorial.

## Narzędzia do rur 


<div class="center" style="width: auto; margin-left: auto; margin-right: auto;">

![](images/Flamingos_pype2.jpg )


</div>


:   1\) Wstaw rurę.

Opens a dialog to insert tubes.

The top-right combo is a common feature for all \"Insert \...\" dialogs: it lists the pype-line objects defined in the current document: with this it\'s possible to select to which pype-line to assign the newly created pipes. You can also leave it to  so that the object is created on the root line of the part model. In the top-left corner is printed the currently selected pipe rating, taken from the listbox in the right column. Pipes dimensions for each pipe-rating are defined in .csv files, which is possible to add or modify, with few simple naming rules, according needs. Curves, reductions etc. have the same rules for definition of their tables of dimensions: see files in ../Mod/flamingo/Tables. Read also \"tutorialPype.pdf\" to know how to customize or create them.

To define position and orientation of pipes, following selections are possible:

-   one or more straight edges
-   one or more curved edges
-   one or more vertexes
-   nothing; in this case the tube will be placed at origin.

If no length is specified, the default is 200 units (just a convenient length, in mm).

**Reverse** button allow to rotate by 180° the last tube created or those currently selected.

**Apply** button allow to apply a different lenght or Nominal diameter to the tubes currently selected.


**Dodo: added a pie-menu (keyboard shortcut: "Z") to create "pype" objects: this is intended to insert faster refinements to the drawing**


:   2\) Insert a curve

Opens a dialog to insert one elbow.

Beside the common widgets with other \"Insert\...\" dialogs, the **Trim/Extend** button allow to adjust the length of selected pipes to the selected edge of the curve. To define position and orientation following selections are possible:

-   one vertex,
-   one circular edge
-   one pipe at one of its ends; in this case the curve\'s diameter and thickness will automatically fit those of the selected pipe
-   a pair of edges or pipes or beams, also not contiguous but intersecting; in this case curve\'s properties will automatically fit to connect the two selected objects; also selected pipes will be automatically trimmed or extended to the curve\'s edges
-   nothing; in this case the curve will be placed at origin.

If no angle is specified the default is 90 degrees.

:   3\) Insert a reduction

Opens a dialog to insert concentric reductions.

To define position and orientation following selections are possible: two pipes parallel (possibly co-linear)

-   one pipe at one of its ends
-   one pipe
-   one circular edge
-   one straight edge
-   one vertex
-   nothing (created at origin)

In case one pipe is selected, its properties are applied to the reduction.

In case two pipes are selected, the tool will try automatically to connect them with the right major and minor diameter.

:   4\) Insert a cap

Opens dialog to insert caps.

To define position and orientation following selections are possible: one or more curved edges (axis and origin across the center) one or more vertexes nothing If a pipe edge is selected the caps\' properties will automatically fit to those of the pipe.

:   5\) Insert a valve

Create a \"placeholder\" of a valve from a .csv table like above. Beside the offset dimension, it\'s important because it defines also the Kv coefficient that will be used to calculate pressure losses with the relevant tool in \"Utils\" menu. Note that the symbol of the placeholder changes according the type of the valve, if in its name is found one keyword among \"ball\", \"butterfly\" or \"globe\".

:   6\) Insert a flange

Opens dialog to insert flanges. To define position and orientation following selections are possible:

-   one or more circular edges,
-   one or more vertexes,
-   nothing.

In case one pipe is selected, its properties are applied to the flange.

:   7\) Insert a U-bolt

Opens dialog to insert U-bolts.

To define position and orientation following selections are possible:

-   one or more circular edges
-   one or more pipes
-   nothing.

In case one pipe is selected, its properties are aplied to the U-bolt. Moreover it\'s possible to choose to place the U-bolt at the **Head** or **Tail** ends or in the **Middle** of the pipes by checking the relevant box.

With **Ref. face** button it\'s possible to select the face of the support to which to orient the U-bolt axis.



*Only in **dodo**: the above piping components can be inserted also wfrom the dedicated pie-menu.*



:   8\) PypeLine Manager

Before talking about the dialog it\'s worth to recall what the pype-line object is in the context of Flamingo workbench.

This object represent a collection of objects \"PType\" that are updated with the methods defined in the Python class itself. At present time it creates, with the method \"obj.Proxy.update(obj,\[edges\])\", pipes and curves over the given edges and collect them in a group named according the object\'s obj.Label. A standard bending radius \"3D\" (i.e. 1.5xO.D.) is applied for curves. The Bend Radius is a common property of object pype-line, thus it can be changed and then redrawn. When the Label of the object pype-line is renamed, the name of its group is changed accordingly.

The class PypeLine2 has also the optional attribute \".Base\", which namely represent the centerline of the piping:

-   If Base is None, PypeLine2 behaves like a bare container of objects, with possibility to group them automatically, assign one color and extract the part-list.
-   .Base can be a Wire or a Sketch or any object which has edges in its Shape.
-   Running \"obj.Proxy.update(obj)\", without any \[edges\], the class attempts to render the pypeline (Pipe and Elbow objects) on the \"obj.Base\" edges: for well defined geometries this usually leads to the desired result. If \[edges\] are given, pipes and curves will be drawn along them.
-   Running \"obj.Proxy.purge(obj)\" deletes from the model all Pipes and Elbows that belongs to the pype-line.
-   Remember that the object created outside the .Base won\'t be updated when the .Base is changed and the pypeline is redrawn and (except pipe and curves) won\'t be deleted if the pype-line is purged.

This understood, the command opens the dialog to create or modify one pype-line.

The dialog is very similar to those for insert other objects seen before.

The pipe ratings tables, where the O.D. and thickness are defined, are the same of those for tubes (e.g. Pipe\_SCH-STD.csv).

When  is in the combo and **Insert** is pressed, a new pype-line object is created in the document with the relevant group.

It is possible to create one pypeline in three ways, according to the objects selected in the viewport when Insert is pushed:

-   nothing is selected. One pype-line is created with property .Base = None and included in its group with the specified name and color (or default values). The piping objects to populate it can be created one-by-one with the commands seen above or alternatively a centerline can be selected afterwards with **Get Profile** and **Redraw** buttons.
-   one DWire object is selected. It is automatically taken as Base and converted in a Path (orange, dash-dotted) and pipes and curves are drawn along it.
-   a set of edges are selected (even not contiguous but anyway having intersections extending their ends). One Path is created connecting all the edges (see the Path tool in the Frame toolbar) and assigned as .Base to the newly created pype-line. Then pipes and curves are drawn on it as above.

After that it\'s still possible to add other objects (such as Flange, Reduct\...) using the relevant insertion commands described above. When objects are created within a pype-line they are automatically included in the relevant group of the model and the common properties (i.e. O.D., thickness, color, bending radius etc.) are applied.

If at least one pype-line is already in the model, that can be selected from the combo-box: in this case, pushing Insert creates the pipes and curves like described above but, instead of creating a new pype-line object, it adds them to the selected existing pype-line. Beware that the piping created in this way will be deleted at next **Redraw**.

**Get Path**, Get Profile and Color allow to change the .Base property, the nominal size and color of the object respectively.

**Redraw** re-create tubes and curves along the .Base (if defined) after any modification to the path or the properties of the pype-line.

**Part list** generates a .csv file with the bill of material of the piping object included in the pype-line selected in the combo.

:   9\) Insert a PypeBranch

This pype object behave like a PypeLine except it automatically updates whenever the Base (a DWire or a SketchObject) is modified: that includes changing the placement, stretching, moving, adding or deleting edges. It is mainly intended to represent the secondary branches of the PypeLine (see the dedicated tutorial) but it can also act as a stand-alone object. This is an important task that allow to change quickly the layout of pipes but, as a drawback, its geometry is more rigidly defined. In other words, pipes can not be splitted or resized independently because they will be eventually redrawn on the Base. Changin the OD, thk or BendRadius of the PypeBranch, instead, will apply on all tubes and curves of it.

:   10\) Insert a tank

[See tutorial Part 4 (1/2)](#Links.md)

:   11\) Insert a piperoute

[See tutorial Part 4 (2/2)](#Links.md)

:   12\) Break the pipe

Opens a dialog to break one pipe at a defined point, optionally making a gap between the ends of the two parts. Multiple selection is possible.

Insert in the **Point** text-box the length where the pipe or pipes are going to break: this can be an absolute value or just a percentage of the length (a numeral followed by %). In some case it\'s quicker to use the slide-bar at the bottom to change this value.

The **Length** button allow to measure the length of the selected pipe and use that as the reference of the slide-bar scale.

If it\'s needed just to break pipes in two, leave the **Gap** text-box to 0; otherwise define the length of the gap. If a reference length is choosen, also the gap can be defined as a percentage. As seen in the [tutorial](https://github.com/oddtopus/flamingo/blob/master/tutorials), it\'s possible to measure the gap from geometries in the model with the **Get gap** button: that\'s the distance between any geometric entity or even the length of a single edge.

Pushing on **Break** performs the action.

The Pypeline combo, as usual, allow to choose the group to which to assign the new objects created.

:   13\) Mate pipes edges.

When two circular edges belonging to different objects are selected, pressing this button will make the second object move to make the edges concentric and coplanar.

This works not only with pipes.

:   14\) Join the pypes

Joins the Ports of different objects in a graphical way. It works only among pype-objects, also from different workbenches, where the Ports\[\] property is defined congruently.

:   15\) Fit one elbow

Select 2 intersecting pipes + 1 elbow: executing this command, they will be joined. It works only among pype-objects, also from different workbenches.

:   16\) Extend pipes to intersection

By selecting two pipes, this command extend them both to their intersection point, if exists.

:   17\) Extend pipe to intersection

By selecting two pipes, this command extend the first to the intersection with the other, if exists.

:   18\) Lay-down the pipes

By selecting one face and multiple pipes, this command translates the pipe along the normal of the face in order to make them lie on its plane.

:   19\) Raise-up the support

Similar to the tool above but in this case is the support that is raised or lowered, so that the face is tangent to the pipe.

:   20\) Attach to tube

Attaches a pype object (2, 3, 4, 5 or 6) rigidly to the nearest end of a pipe (1). To detach, click on the button while the attached object is selected alone.

:   21\) Create pipes point-to-point

Opens a dialog similar to \"Draw a DWire\" together with the dialog of \"Insert a pipe\": this allows to draw a sequence of pipes, connected by curves, just selecting one point after the other. It is also allowed to change properties of the pipe and/or the pype-line on the fly.

:   22\) Insert Any Shape

This is a tool to create a \"pype\" object from a .STEP or .IGES or .BREP file. It loads the imported file into the Shape property of a FeaturePython.

## Utilities


<div class="center" style="width: auto; margin-left: auto; margin-right: auto;">

![](images/Flamingos_utils.jpg )


</div>


:   1\) Make a polygon

The first two tools of utils are part of a separate project which aims to create an automatic scanner of rooms with a stepper motor and an ultrasonic distance meter. This tool creates one regular polygon inside a sketch.

:   2\) Polygon from file

Tool to create any polygon inside a sketch taking vertexes from a .csv file, where they are stored in polar coordinates.

:   3\) Query the model

Tool to get various informations according to the object or objects selected. Beside length or distances, it is specifically suited to give informations related to beams and pipes (length, section, angle-between).

:   4\) Align workplane

Tool to set the position and rotation of working plane according to the selected existing geometry.

The normal of working plane is defined scanning the elements in the following order:

1.  the normal of a face
2.  the normal of the plane of a curve
3.  the normal of the plane containing two segments

The origin of working plane is defined (in order) by

1.  one vertex
2.  the center of curvature of a line
3.  the intersection of two lines
4.  the center of an edge

:   5\) Offset workplane

Shifts the working plane along its normal vector. To show the direction of offset, a temporary green arrow is displayed on the screen. Clearly also negative values are allowed.

:   6\) Rotate workplane

Rotates the working plane around one of its axis. Also in this case a green arrow is displayed in the viewport to identify the present orientation of the WP: the arrow is pointed in the Z direction and the long base of the arrow is layed over the X direction.

:   7\) Draw a DWire

This tool works exactly like the corresponding tool of Draft workbench but with few additional options at the end of the dialog. As default, the origin of working plane is redefined at each point added because this makes simpler to draw segments of known length and orientation using the snap-to-grid option. Then two push-buttons, invoked also with the short-key Ctrl+Shift+(), allow to rotate and offset the working plane as seen above without breaking the DWire object. The last three buttons allow to quickly change the rotation of working plane to be parallel to the principal planes.

:   8\) Quick move objects

To move quickly any part, to access the underlying objects for instance, this tool provides a graphic handle (green arrow) by clicking on which it\'s possible to displace and rotate the selected objects.

:   9\) Pressure loss calculator

Opens one dialog to calculate the pressure losses across the pype-parts selected in the viewport or across one PypeBranch. The friction coefficient is calculated for each straight tube and elbow. For other objects the concentrated pressure loss is calculated through the flow factor, provided that the attribute Kv is available and set to a positive value.

## Odnośniki internetowe 

-   Forum: [New workbench for metal structures](http://forum.freecadweb.org/viewtopic.php?f=8&t=17035) (announcement)
-   Forum: [Flamingo & Dodo workbench(s) discussion thread](https://forum.freecadweb.org/viewtopic.php?t=22711)
-   Tutorials: [flamingo/tutorials](https://github.com/oddtopus/flamingo/tree/master/tutorials)

-   Video tutorials:
    -   [Simple video tutorial for frame creation with pipes](https://www.youtube.com/watch?v=_Or91gdBLMU)
    -   [Part 1: how to created pipe lines](https://www.youtube.com/watch?v=cBj0umlvzAk)
    -   [Part 2: frames, supports, flanges, and imported components](https://www.youtube.com/watch?v=e81PpWY5L00)
    -   [Part 3: drawing one building with four sketches (and a bunch of other features)](https://www.youtube.com/watch?v=IqEccmsg5dU)
    -   [Part 4 (1/2): Pump room layout and piping plan](https://www.youtube.com/watch?v=aPF8SS_1Aqo)
    -   [Part 4 (2/2): Pump room import in building and pipe-route](https://www.youtube.com/watch?v=iGnW88x9bKQ)
-   Reporting bugs:
    -   [Flamingo GitHub issue queue](https://github.com/oddtopus/flamingo/issues)
    -   [Dodo GitHub issue queue](https://github.com/oddtopus/dodo/issues)

## Other useful links 

-   [External workbenches](External_workbenches.md)
-   [Macros recipes](Macros_recipes.md)
-   [OSE-Piping-Workbench: to create extra pipe fittings](https://wiki.opensourceecology.org/wiki/OSE_Piping_Workbench)

## Zewnętrzne środowiska pracy 

Środowiska pracy FreeCAD są łatwe do zaprogramowania w środowisku [Python](Python/pl.md). Dlatego też, wiele osób opracowuje dodatkowe \"przestrzenie robocze\" wykraczające poza główny obszar rozwoju programu FreeCAD.

Strona [Zewnętrzne środowiska pracy](External_workbenches/pl.md) zawiera informacje i poradniki na temat niektórych z nich, a projekt [Dodatki FreeCAD](https://github.com/FreeCAD/FreeCAD-addons) ma na celu zebranie ich i uczynienie łatwymi do zainstalowania z poziomu programu FreeCAD.

Nowe środowiska pracy są w czasie tworzenia, bądź cierpliwy!



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Flamingo Workbench/pl
