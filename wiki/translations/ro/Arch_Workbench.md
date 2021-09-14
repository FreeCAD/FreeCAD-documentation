# Arch Workbench/ro




{{docnav/ro
|[Workbenches](Workbenches/ro.md)
|[Draft Module](Draft_Workbench/ro.md)
|IconL=Freecad.svg
|IconR=Workbench_Draft.svg
}}

<img alt="Arch workbench icon" src=images/Workbench_Arch.svg  style="width:128px;">


{{TOCright}}

## Introducere

Arch Workbench oferă un flux de lucru modern pentru [modeling information building](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM) pentru FreeCAD, cu suport pentru caracteristici precum entități arhitecturale complet parametrice, cum ar fi pereți, elemente structurale, acoperișuri, ferestre , scări, țevi și mobilier. Acesta susține datele \[IFC\] [industry foundation classes](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) și producerea de planuri de planuri 2D în combinație cu [ TechDraw](TechDraw_Workbench.md).

The <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch Workbench](Arch_Workbench.md) provides a modern [building information modelling](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM) workflow to FreeCAD, with support for features like fully parametric architectural entities such as walls, beams, roofs, windows, stairs, pipes, and furniture. It supports industry foundation classes ([IFC](Arch_IFC.md)) files, and production of 2D floor plans in combination with the <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md).

Atelierul Arch Workbench importă toate uneltele din [ Draft Workbench](Draft_Workbench.md), deoarece utilizează obiecte 2D pentru a-și construi obiectele arhitecturale. Cu toate acestea, Arch poate folosi și obiecte solide create pe alte Ateliere de lucru precum [ Part](Part_Workbench.md) și [ PartDesign](PartDesign_Workbench.md).

**Notă**: Funcția [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) a FreeCAD este acum împărțită treptat în acest Atelier Arhitectură, care conține toate instrumentele BIM de bază și [BIM Workbench addon](https://github.com/yorikvanhavre/BIM_Workbench), pe care îl puteți instala prin intermediul meniului Tools → Addon Manager, care adaugă un nou strat de interfață deasupra instrumentelor Arch, cu scopul de a face fluxul de lucru BIM în FreeCAD mai intuitiv și convivial.

The developers of Draft, Arch, and BIM also collaborate with the greater [OSArch community](https://osarch.org), with the ultimate goal of improving building design by using entirely free software.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">

## Instrumente

Acestea sunt instrumente pentru crearea obiectelor arhitecturale.

-   <img alt="" src=images/Arch_Wall.png  style="width:32px;"> [Wall](Arch_Wall.md): Creează un perete de la zero sau utilizând obiectul selectat ca bază
-   <img alt="" src=images/Arch_Structure.png  style="width:32px;"> [Structural element](Arch_Structure.md): Creează un element structural de la zero sau utilizând obiectul selectat ca bază

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Rebar tools](Arch_CompRebarStraight.md): Addon de armătură măresc Arch Workbench Structures.
    -   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> [Straight Rebar](Arch_Rebar_Straight.md): Creează o bară de armătură dreaptă în elementul structural selectat
    -   <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> [UShape Rebar](Arch_Rebar_UShape.md): Creează o bară de armătură în formă de U în elementul structural selectat
    -   <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> [LShape Rebar](Arch_Rebar_LShape.md): Creează o bară de armătură în formă de L în elementul structural selectat
    -   <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> [Bent Shape Rebar](Arch_Rebar_BentShape.md): Creează o bară de armătură în formă de Z în elementul structural selectat
    -   <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> [Stirrup Rebar](Arch_Rebar_Stirrup.md): Creează o bară de armătură în formă etrier în elementul structural selectat
    -   <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> [Helical Rebar](Arch_Rebar_Helical.md): Creează o bară de armătură în formă elicoidală în elementul structural selectat
    -   <img alt="" src=images/Arch_Rebar.png  style="width:32px;"> [Rebar](Arch_Rebar.md): Crează o bară de armătură în formă personalizată în elementul structural selectat utilizâd o schiță

-   <img alt="" src=images/Arch_Floor.png  style="width:32px;"> [Floor](Arch_Floor.md): Creează un etaj incluzând obiectele selectate
-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [Building Part](Arch_BuildingPart.md): Creează o parte de clădire incluzând obiectele selectate
-   <img alt="" src=images/Arch_Reference.png  style="width:32px;"> [Reference](Arch_Reference.md): Leagă obiecele din alt fișier FreeCAD în acest document
-   <img alt="" src=images/Arch_Building.png  style="width:32px;"> [Building](Arch_Building.md): Creează o clădire incluzând obiectele selectate.
-   <img alt="" src=images/Arch_Site.png  style="width:32px;"> [Site](Arch_Site.md): Creează un site incluzând obiectele selectate
-   <img alt="" src=images/Arch_Window.png  style="width:32px;"> [Window](Arch_Window.md): Creează o fereastră utilizând obiectul selectat ca bază
-   <img alt="" src=images/Arch_SectionPlane.png  style="width:32px;"> [Section Plane](Arch_SectionPlane.md): Adaugă un obiect plan de secțiune al documentului

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Axis tools](Arch_CompAxis.md): The Axis tool allows you to places a series of axes in the current document.
    -   <img alt="" src=images/Arch_Axis.png  style="width:32px;"> [Axis](Arch_Axis.md): Adaugă o matrice tip șir /1-direction array a axelor documentului
    -   <img alt="" src=images/Arch_AxisSystem.png  style="width:32px;"> [Axes system](Arch_AxisSystem.md): Adaugă un sitem de axe compus din câteva axe ale documetnului
    -   <img alt="" src=images/Arch_Grid.png  style="width:32px;"> [Grid](Arch_Grid.md): Adaugă un obiect tip grilă la document

-   <img alt="" src=images/Arch_Roof.png  style="width:32px;"> [Roof](Arch_Roof.md): Creează un acoperiș înclinat din fațeletel selectate
-   <img alt="" src=images/Arch_Space.png  style="width:32px;"> [Space](Arch_Space.md): Creează un obeict tip spațiu în document
-   <img alt="" src=images/Arch_Stairs.png  style="width:32px;"> [Stairs](Arch_Stairs.md): Creează o obiect tip scară în document

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Panel tools](Arch_CompPanel.md): Allows you to build all kinds of panel-like elements.
    -   <img alt="" src=images/Arch_Panel.png  style="width:32px;"> [Panel](Arch_Panel.md): Creează un obiect tip panou din obiectul 2D selectat
    -   <img alt="" src=images/Arch_Panel_Cut.png  style="width:32px;"> [Panel Cut](Arch_Panel_Cut.md): Creează o secțiune 2D cut view din panou <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Panel_Sheet.png  style="width:32px;"> [Panel Sheet](Arch_Panel_Sheet.md): Creează o 2D cut sheet incluzând panoul secțiune sau alt obeict 2D <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Nest.png  style="width:32px;"> [Nest](Arch_Nest.md): Permite încuibarea(așezarea economică) mai multor obiecte plane într-o formă tip container <small>(v0.17)</small> 

-   <img alt="" src=images/Arch_Frame.png  style="width:32px;"> [Frame](Arch_Frame.md): Creează un obiect tip cadru din straturile selecate
-   <img alt="" src=images/Arch_Equipment.png  style="width:32px;"> [Equipment](Arch_Equipment.md): Creează un obiect tip echipament sau mobilă

-   Instrumentele țeavă/Pipe tools \* <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Pipe tools](Arch_CompPipe.md) <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Pipe.png  style="width:32px;"> [Pipe](Arch_Pipe.md): Creează o țeavă <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_PipeConnector.png  style="width:32px;"> [Pipe Connector](Arch_PipeConnector.md): Creează un conector în colț sau în "T" între e sau 3 țevi selectate <small>(v0.17)</small> 

-   Instrumentele de Material <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Material tools](Arch_CompSetMaterial.md):Instrumentele Material permit adăugarea materialelor în documentul activ.
    -   <img alt="" src=images/Arch_SetMaterial.png  style="width:32px;"> [Material](Arch_SetMaterial.md): Creează un material și atribuiți-l obiectelor selectate, dacă există vreunul
    -   <img alt="" src=images/Arch_MultiMaterial.png  style="width:32px;"> [Multi-Material](Arch_MultiMaterial.md): Creează un multi-material și atribuiți-l obiectelor selectate, dacă există vreunul <small>(v0.17)</small> 
-   <img alt="" src=images/Arch_Schedule.png  style="width:32px;"> [Schedule](Arch_Schedule.md): Creează diferite tipuri de schedules

### Instrumente de Modificare 

Acestea sunt instrumente pentru modificarea obiectelor arhitecturale.

-   <img alt="" src=images/Arch_CutPlane.png  style="width:32px;"> [Cut with plane](Arch_CutPlane.md): Secționați un obiect după un plan.
-   <img alt="" src=images/Arch_Add.png  style="width:32px;"> [Add component](Arch_Add.md): Adăugați obiecte la componentă
-   <img alt="" src=images/Arch_Remove.png  style="width:32px;"> [Remove component](Arch_Remove.md): Extrageți sau șetgeți obeicte din tr-o componentă
-   <img alt="" src=images/Arch_Survey.png  style="width:32px;"> [Survey](Arch_Survey.md): Introduceți sau părăsiți modul surveying

### Utilități

Acestea sunt instrumente suplimentare care vă ajută în îndeplinirea unor sarcini specifice.

!!FUZZY!!\* ![ 32px](images/_Arch_Component.png ) [ Component](Arch_Component.md): Creează o componentă din Atelierul Arch non-parametrică

-   [ 32px](Imagine:_Arch_cloneComponent.png.md) [ Clone component](Arch_CloneComponent.md):
-   [ 32px](Imagine:_Arch_SplitMesh.png.md) [ Split Mesh](Arch_SplitMesh.md): Împărțiți o plasă selectată în componente separate
-   [ 32px](Imagine:_Arch_MeshToShape.png.md) [ Mesh to shape](Arch_MeshToShape.md): Conversia unui ochi de plasă într-o formă, îmbinând fațetele coplanare
-   ![ 32px](images/_Arch_SelectNonSolidMeshes.png ) [ Selectare ochiuri ne-solide](Arch_SelectNonSolidMeshes.md): Selecteaza toate ochiurile ne-solide din selecția curentă sau din document
-   ![ 32px](images/_Arch_RemoveShape.png ) [ Eliminați forma](Arch_RemoveShape.md): Se transformă obiectul Arch de tip cubic pe parametru complet
-   ![ 32px](images/_Arch_CloseHoles.png ) [ Close Holes](Arch_CloseHoles.md): Închide găurile într-un obiect selectat pe bază de forme
-   [ 32px](Imagine:_Arch_MergeWalls.png.md) [ Merge Walls](Arch_MergeWalls.md): Uniți doi sau mai mulți pereți
-   ![ 32px](images/_Arch_Check.png ) [ Check](Arch_Check.md): Verificați dacă obiectele selectate sunt solide și nu conțin defecte
-   ![ 32px](images/_Arch_IfcExplorer.png ) [ Ifc Explorer](Arch_IfcExplorer.md): Răsfoiți conținutul unui fișier tip [ IFC](Arch_IFC.md)
-   ![ 32px](images/_Arch_ToggleIfcBrepFlag.png ) [ Toggle flag IFC Brep](Arch_ToggleIfcBrepFlag.md): Forțează ca un obiect selectat să fie exportat ca un [/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final).
-   [ 32px](Imagine:_Arch_3Views.png.md) [ 3 Vizualizări de pe plasă](Arch_3Vizualizări.md): Creează vederi de sus, frontale și laterale dintr-o plasă [ mesh](Mesh_Workbench.md).
-   [ 32px](Imagine:_Arch_Schedule.png.md) [ Creare foaie de calcul IFC \...](Arch_MakeIfcSpreadsheet.md):
-   ![ 32px](images/_Arch_ToggleSubs.png ) [ Toggle Subcomponents](Arch_ToggleSubs.md): Afișează sau ascunde subcomponentele unui obiect Arch.

### Preferințe

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [Preferences](Arch_Preferences.md): preferințele pentru aspectul implicit al pereților, structurilor, barelor, ferestrelor, scărilor, panourilor, țevilor, grilelor și axelor.

### Formate de fișier 

-   [IFC](Arch_IFC.md) : Industry foundation Classes
-   [DAE](Arch_DAE.md) : Collada mesh format
-   [OBJ](Arch_OBJ.md) : Obj mesh format (export only)
-   [JSON](Arch_JSON.md) : JavaScript Object Notation format (export only)
-   [3DS](Arch_3DS.md) : 3DS format (import only)

## API

Modulul Arch poate fi folosit în scripturile [Python](Python.md) scripts și [macros](macros.md) utilizând funcții [Arch Python API](http://www.freecadweb.org/api/Arch.html) .

## Tutoriale

-   [Architecture workflow](http://yorik.uncreated.net/guestblog.php?tag=freecad): An example of how FreeCAD can begin to have its preliminary place in an architecture workflow.
-   [Arch tutorial](Arch_tutorial.md) (v. 0.14)
-   [Quick arch overview on Yorik\'s blog](http://yorik.uncreated.net/guestblog.php?2012=180) (v. 0.13)
-   [Video presentation of the Arch workbench](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Arch panel tutorial](Arch_panel_tutorial.md) (v. 0.15)
-   [BIM modeling chapter from the FreeCAD manual](Manual:BIM_modeling.md)
-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md)
-   [Export to STL or OBJ](Export_to_STL_or_OBJ.md)


{{docnav/ro
|[Workbenches/ro](Workbenches/ro.md)
|[Draft Module/ro](Draft_Workbench/ro.md)
|IconL=|IconR=Workbench_Draft.svg
}}


 

[Category:Workbenches](Category:Workbenches.md)
