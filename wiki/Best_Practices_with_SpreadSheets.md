# Best Practices with SpreadSheets
# Introduction

This is a draft of what I imperfectly understand as best practices ( and tips, and gotchas ) for parametric modeling in FreeCad using SpreadSheets. On a wiki things may never be finished, but until I get comment I am pretty much finished with this. Plan to move out of sandbox soon.

## Why

For me the point of a parametric model is that measurements ( and sometimes other features ) can be changed by changing the value of an input variable or parameter. The parameters may be stored in many different locations in your model but I find that a spreadsheet is the most useful. You can just look at a table of values, their names, and perhaps some notes about them. The spreadsheet can also do some calculations like changing radii to diameters and vise versa.

## How

Use the spreadsheet workbench to add a spreadsheet. Then put you important dimensions in a cell. I find it most useful to give each cell a name or alias. If you do not do this the cells have non-informative names like B5. I normally also type the alias to the left of the column with the data, so when I look at the spreadsheet I can see both the name and the value ( some macros, see below, help you automate this process ). It is often useful to tile your workspace so you can see the spreadsheet and the model as you enter formula.

# Names in the SpreadSheet 

Like programming good names can really help you keep track of what you are doing. So be systematic in making up your names. Some bad names   *

-   part_size ( a radius, diameter\....? )
-   distance ( what direction, from what? )

Better names   *

-   bolt_diameter
-   bolt_length
-   shaft_dia

But note that you should try to be consistent   * try to use dia or diameter but not both.

Finally all names in a spreadsheet are referenced outside of it by using the spreadsheets name, so I usually rename it from the default \"Spreadsheet\" to the easier to type \"ss\".

# SpreadSheet values in the Model 

Most values/measurements in the model that can be entered as numbers can also be entered as formula, and the formula can use the names from the spreadsheet as values. Suppose for example your model has several shafts in different sketches which should all have the same radius, and also that you have holes in your model for the shafts to fit into. How do you change the radius of all the shafts and holes?

Here is an approach   *

-   In the spreadsheet have a cell shaft_radius, and another shaft_clearance, each with a numerical value. The clearance is the amount ( in radius ) that the hole needs to be larger than the shaft for the parts to fit.

-   In a sketch where you have a circle for the shaft apply the radius   * when the value box come up press the formula icon at its right hand side, or hit the = sign. Now you can enter the formula   *

ss.shaft_radius. Note that as you type FreeCad will try to help, if you type ss.s then FreeCad will suggest shaft_radius, and you can just click on it.

-   For a shaft hole try the radius ss.shaft_radius + ss.shaft_clearance

# Units

FreeCad can be fussy about units and not always intuitive. In one case I was getting errors in a sketch with measurements drawn from a spreadsheet. Getting rid of all the units seems to default FreeCad to mm, and when I cleared all the units in all the involved measurements the problem when away. Documentation on the spreadsheet seems to warn against problems with units but rather than getting rid of them recommends just consistent use everywhere. The safest units seem to be mm but others may work as well. Note that when adding ( 2 + 5 ) mm is not equal to 2mm +5mm, the units cannot be treated as a factor. Put the units on as soon as possible and as consistently as possible.

# Master Sketches 

Rather than use a spreadsheet I have seen some people use a \"master sketch\" The idea here is that all the important dimensions are drawn out in a sketch. This sketch is never padded, pocketed or drafted, but other sketches ( usually parallel to it ) use the connect to external geometry feature to synchronize the parameters. I have tried this and like the way it is more visual than a spreadsheet, but it also has limitations   * it is harder to do math in it, it is unclear what to do if you have three dimensions to parameterize, it is harder to annotate. Despite the limitations you may find it useful. When I use it now, and I still do, I link its parameters back to the spreadsheet and more or less get the best of both worlds.

# The Topological Naming Problem ( TNP ) 

This is a problem which causes a model to break \.... you do not get what you expect, and it usually includes elements in your model that report errors so they will not recompute. The problem seems to be particularly severe in highly parametric models which are fine until you change one of the parameters. I do not want to go too deeply into the problem here ( partly because I am not an expert ) but I think many of the best practices are developed for highly parametric models so they will not fail. I think the crux is that a model, like computer code, is held together by names and numbers. When you recompute an object, say even a cube, you get a new object and the names of its faces, edges\.... may change or be in different places. Other objects are attached to the names and now may not be where you want them or even in a place that makes sense. This can easily come up when you attach a sketch to the face of an object. So we will recommend practices that avoid this sort of attachment.

-   **[Why do my FreeCAD models break? - \"Topological Naming Problem\" - YouTube](https   *//www.youtube.com/watch?v=6p2vqEEmWq4)**

# Placement of Sketches 

You should place sketches on objects that will not move, or at least will not move in a way that changes it name. For example, solids in part design have faces with name and these internally generated names may change as the model is revised. Here are some safe ( safer ) ways.

## Planes Through Origin 

A sketch attached to any of the 3 planes passing through the origin is safe from the TNP as these are named invariant \"things\" If you can use these planes, if you are making holds all the way through an object you can start from the bottom as well as from the top.

## Move the Sketch Placement 

When the drawing of the sketch is \"closed\" there are still a lot of changes that can be made Data tab of the sketch in particular see   *

Base -\> Placement -\> Position ( x, y, z )

The directions x, y, and z are not the x, y, and z of the overall model but of the plane of the sketch. z is always out of plane and x and y in the plane so the whole thing is a right handed coordinate system. Move z to get the plane to move perpendicular to z. This amount can ( and should ) be entered from the spreadsheet. Here is an example of the idea.

Suppose you have a cube constructed from a sketch sitting on the xy plane and extending up in the z direction ( lets this be cube_z\_size in the spreadsheet ). You want to \"drill\" some cylindrical holds on the top face half way down through the cube. The simple thing to do is attach a second sketch sitting on the top face. Don\'t. It is very liable to break on resizing. Instead place you sketch on the xy plane then set the sketches z position to cube_z\_size. It now moves with the cube as if it were attached but is not subject to TNP. You set the depth of the holes ( in the pocket ) to cube_z\_size/2 and now one parameter in the spread sheet changes everything in the model that needs changing.

## Datums

A datum is another way of moving a sketch placement. A datum ( for planes ) is simply a plane that you can position anywhere in a model body at any angle ( all probably controlled by a spreadsheet ) and then you can attach sketches to the datums. I am not sure of what the trade offs are between \"placed\" sketches and datums so can not tell you when to use one or the other. It seems a bit more work to construct a datum, but then it is a bit more obvious how the sketch is being placed.

# Name the parts of the Model 

After I have constructed a model I am often a bit confused as to what is what in the model and how the pieces relate to each other. Because of this I often name parts of the model and think that this is a best practice for some parts of some models. Say you have bolt holes based on a sketch. You could name the sketch bolt_holes, then pocket them and name this bolt_holes\.... well not quite two things with the same name is one route to insanity. So I prefix them po\_ for pocket (pd- for pad ), s\_ for sketch. The names are then s_bolt_holes and po_bolt_holes. As usual with names try to pick a scheme and stick to it.

# In the Sketch 

-   I have heard that the sketch is easiest to work with, overall, if it is centered on the origin. May/may not be a useful guideline in absence of a reason to place differently.
-   Also heart that geometric properties like symmetry rather than numerical ones like dimension are to be preferred.

## Constraints Values and Name 

-   Constraints that have distances or angles\... may also be tied to the spreadsheet through expressions.
-   Constraint values can be given names like an alias and then used in other expressions. I generally refer directly to the spread sheet instead.

# Part Design 

Take a look at   * [Feature editing](Feature_editing.md)

# Order of Operations 

I have seen some stuff recommending you model in a certain order of operations. I do not understand this well enough to make recommendations.

# Models that Illustrate these Practices 

All these models may not be perfect, but attempt to show best pratices. The links may within this wiki or to external sites.

-   [Microscope Adapter Model](Microscope_Adapter_Model.md)

# Videos

## Some Briefly Reviewed Videos 

Reviews take a lot of time, these pretty much make sure the video is on topic, but not a whole lot more. Many of these videos are on channels that are listed at   * [FreeCAD on Video](FreeCAD_on_Video.md) There may be more you can check for updates on this page\'s history. Those listed here are in no particular order. The page search feature in your browser may help you find ones of interest.

-   **[Designing with spreadsheets in FreeCAD - YouTube](https   *//www.youtube.com/watch?v=_pITOzeqJ0Y)** \-- seems on topic
-   **[Designing a small cabinet using FreeCAD and spreadsheets - YouTube](https   *//www.youtube.com/watch?v=bdgQQFEpBN0)** \-\-- follow up to above, a real world example. Connecting to Excel.
-   **[FreeCAD - Using the Spreadsheet for Parametrized Sketch based Parts. - YouTube](https   *//www.youtube.com/watch?v=b07qbhYHZbU)** \-- seems on topic
-   **[FreeCAD 0.18 Link Spreadsheets to Part Design - YouTube](https   *//www.youtube.com/watch?v=xjL4-1S7Was)** \-- seems on topic
-   **[How to use Variables and Equations to Design in FreeCAD\|JOKO ENGINEERING\| - YouTube](https   *//www.youtube.com/watch?v=Jze6ftGc6BQ)** \-- nice basic intro.
-   **[FreeCAD - Basics - Spreadsheet Alias - YouTube](https   *//www.youtube.com/watch?v=06fn0tB01fE)** \-- nice basic intro.
-   **[FreeCAD Tutorial 2 \| Cylinder Parametric Model using Spreadsheet (Basics) - YouTube](https   *//www.youtube.com/watch?v=HcJAmhC1JfM)** \-- nice basic intro.
-   **[FreeCAD for Woodworkers 03 - Parametric Routing Template with Spreadsheets - YouTube](https   *//www.youtube.com/watch?v=kfyiFr8lCW4)** \-- basic intro + alias manager + draft application.
-   **[FreeCAD - Intro to Parametric Modelling - YouTube](https   *//www.youtube.com/watch?v=fXoRAYv1wHQ)** \-- nice intro, uses RealThunder version of FreeCad
-   **[Making a FreeCad File Parametrized from a Spreadsheet - YouTube](https   *//www.youtube.com/watch?v=camIgIfUjss)** \-- covers the basics
-   **[FreeCAD Tutorial \| Exercise 5   * Design of Parametric Model of Gear Pairs Using Spreadsheet Workbench - YouTube](https   *//www.youtube.com/watch?v=AwHZbCFXWf0)** \-- intro with gears
-   **[FreeCAD   * Make Your Own Part Library \|JOKO ENGINEERING\| - YouTube](https   *//www.youtube.com/watch?v=1qszeRDmpvg)** \-- nice
-   **[FreeCAD Tutorial - Framing BasicShed Window - Sketch Driven, Part Attachment and Spreadsheet Driven - YouTube](https   *//www.youtube.com/watch?v=qoutY6HQyBY)** \-- fairly complex with 2 spreadsheets
-   **[FreeCAD Excel CSV import 2019-05-13 - YouTube](https   *//www.youtube.com/watch?v=S_YHy_m1jwg)** \-- seems on topic, csv is nice addition
-   **[FreeCAD 0.18 Expressions - YouTube](https   *//www.youtube.com/watch?v=ilkG1cwt1Ic)** \-- expressions are important, this covers in detail
-   **[FreeCAD Beginner - #13 Spreadsheet for dimensions - Drawing tutorial not only for 3D print - YouTube](https   *//www.youtube.com/watch?v=3_p-hRKCKOA)** \-- basic intro
-   **[FreeCAD spreadsheet / parametric design - YouTube](https   *//www.youtube.com/watch?v=-HRDcCL73lM)** \-- some basics, no verbal narration
-   **[(59) FreeCAD \| Spreadsheet, Part Design, Part Workbench - YouTube](https   *//www.youtube.com/watch?v=xWG05uh2sxM)** \-- basics for spreadsheets with several workbenches.
-   **[FreeCAD Tutorial Part 3/3 \| Creation Parametric Assembly of Wind Turbine Using Spreadsheet - YouTube](https   *//www.youtube.com/watch?v=fjkxCXyHHnk)** \-- a lot of content about assembly, but includes use with spreadsheets.
-   **[FreeCAD Parametric Modelling - YouTube](https   *//www.youtube.com/watch?v=lf-up4UjG58&t=1346s)** \-- spreadsheets with sketches
-   **[FreeCAD Tutorial 27 - Spreadsheet Workbench - YouTube](https   *//www.youtube.com/watch?v=9DzpRqTvdU4)** \-- looks like a good intro -\> in German.
-   **[FreeCAD Spreadsheet Parametric Modeling Failure. - YouTube](https   *//www.youtube.com/watch?v=tZYR9AwQU1k)** Sometimes things go wrong.
-   **[FreeCAD For Beginners p.2 - Parametric Modelling - YouTube](https   *//www.youtube.com/watch?v=RNCsazKxviQ)**
-   **[FreeCAD Tutorial - Basics - NEMA Stepper Motor - YouTube](https   *//www.youtube.com/watch?v=HmxcNJQYt7o)**
-   **[FreeCAD - Parametric Design - YouTube](https   *//www.youtube.com/watch?v=NpFFPG9cwx8)** \-- from basics to a macro making setting the alias easier, use a \"2D\" approach in spreadsheet
-   **[BearingPeg 2.0 - FreeCAD Customization Example - YouTube](https   *//www.youtube.com/watch?v=GEhgrSl4hL0)** a second video to \"FreeCAD - Parametric Design - YouTube\" a realistic part being designed.
-   **[FreeCAD spreadsheet - parametric design - YouTube](https   *//www.youtube.com/watch?v=fQR-ef1FwJk)** a jewellery design application with 2 spreadsheets.
-   **[046 FreeCAD Part Design Draft and new Spreadsheet Alias Control - YouTube](https   *//www.youtube.com/watch?v=xoeQqf_wlN4)** \-- new alias control, a feature I missed ( v.19 )
-   **[How to create a ifcRoom from a Excel /CSV List with FreeCAD - YouTube](https   *//www.youtube.com/watch?v=TQYvez80Qhw)** \-- integration with Excel/CSV is not commonly covered. Also an interesting macro.
-   **[5# Tuto 3 Freecad l\'atelier tableau (Spreadsheet) - YouTube](https   *//www.youtube.com/watch?v=vBmDO7qq7Go)**
-   **[Crazy Simple 3D Printed Enclosure with FreeCAD 0.18 Parametric Design Part 1 - YouTube](https   *//www.youtube.com/watch?v=OLIUQtrMGBo)** \-- real world example, nice. First of a 6 part series. Lots of detail. English audio.
-   **[FreeCAD Tutorial - Parametrischer Möbelbau mit der PartDesign und Spreadsheet Workbench - YouTube](https   *//www.youtube.com/watch?v=63PfO0W5x-I)** seems to cover the basics, German audio.
-   **[FREECAD #122 - L BAR - SPREADSHEET - YouTube](https   *//www.youtube.com/watch?v=PdpeQgsh3LQ)** nice video, music I can stand with very clear mouse/key indications.
-   **[FreeCAD - Part variation with spreadsheets and Inventor Workbench - YouTube](https   *//www.youtube.com/watch?v=IjnB1zgYJm8)** Not best practice \.... but an interesting parametric add on, this is the only video at this time by this creator.
-   **[FreeCAD - Parameterized Lead Screw using Construction Geometries - YouTube](https   *//www.youtube.com/watch?v=BcKklSvVpM8)** Fairly complex design, heavy use of spreadsheet.
-   **[Tuto \|\| FreeCad 0.18    * apprendre à utiliser les tableurs - YouTube](https   *//www.youtube.com/watch?v=5HN6KuD87uE)** French ( I think ). A fairly complicated design with large spreadsheet.
-   **[Woodworking with FreeCAD - YouTube](https   *//www.youtube.com/watch?v=jfNBfdIpzDQ)** \-- goes beyond just basic dimensioning, plus a woodworking application is interesting. English audio.
-   **[FreeCAD Tutorial \| Exercise 7   * Design Parametric Model of PVC Pipe Fitting Tee in PartDesign - YouTube](https   *//www.youtube.com/watch?v=J1HZdkzgVlg)** fairly complex application. English audio.
-   **[BIM with FreeCAD - Expressions - YouTube](https   *//www.youtube.com/watch?v=Bc7ZtaMAx4g)** Mostly about expressions ( as in spreadsheet \"formulas\" ) this is one of a few videos I found with this focus.
-   **[Design and Print an Arduino Box with FreeCAD - YouTube](https   *//www.youtube.com/watch?v=y97EFZvmnAA)** does not focus on spreadsheet, but a very complete parametric model that uses it. **Links to source code for model!**

# Macros For Better SpreadSheet Use 

Just starting this section, a draft inside a draft. Macros may or may not help you keep to best pratices. Here are a few. Some little reviews here, just looking at defining and clearing macros.

## General

-   **[\"Spreadsheet tools\" site   *forum.freecadweb.org at DuckDuckGo](https   *//duckduckgo.com/?q=%22Spreadsheet+tools%22+site%3Aforum.freecadweb.org&ia=web)** DuckDuckGo search

-   **[tools for the spreadsheet - FreeCAD Forum](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=20508)** \-- one result from the search above.

## FreeCAD_AliasManager pgilfernandez 

-   **[Macro Alias Manager - FreeCAD Documentation](https   *//wiki.freecadweb.org/Macro_Alias_Manager)**
-   **[pgilfernandez/FreeCAD_AliasManager   * This macro helps managing aliases inside FreeCAD Spreadsheet workbench. It is able to create, delete, move aliases and create a \'part family\' group of files](https   *//github.com/pgilfernandez/FreeCAD_AliasManager)**

Review   * ( russ_hensel, dec 2020, Version   * 0.19.23141 (Git) )

-   Just want to create alias\'s from names in one column to another column.
-   Installed with Addon Manager, this went fine. +
-   Window Drops behind main window -
-   Has Help +
-   Use of \"from\" which seems to mean \"to\" was confusing to me. This may just be me. -
-   Hint   * names must be in column A
-   Alias were created +++++

## SheetProperties uribench 

-   **[uribench/SheetProperties   * FreeCAD Macro for manipulating properties of spreadsheet cells](https   *//github.com/uribench/SheetProperties)**

Review   * ( russ_hensel, dec 2020, Version   * 0.19.23141 (Git) )

-   Just want to create alias\'s from names in one column to another column.
-   Manual install, this went fine following directions at github but not sure about inclusion of \_\_init\_\_.py +
-   Window Drops resists dropping behind main window ?
-   Help no, but some error messages are useful ?
-   Hint.. if not working close and reopen seems more useful
-   Works\... a bit fussy but works, never figured out how custom or refresh were useful.

## Macro SpreadsheetTools 

-   **[Macro SpreadsheetTools - FreeCAD Documentation](https   *//wiki.freecadweb.org/Macro_SpreadsheetTools)**

Review   * ( russ_hensel, dec 2020, Version   * 0.19.23141 (Git) )

-   Just want to create alias\'s from names in one column to another column.
-   Installed with Addon Manager, this went fine. +
-   Window Drops behind main window -
-   No Help -
-   Does not work for me, throws many errors which seem to indicate it is written in Python 2.x

## Macros recipes 

-   **[Macros recipes - FreeCAD Documentation](https   *//wiki.freecadweb.org/Macros_recipes)**

# Links to Related Material 

-   Use category spreadsheet at foot of page

-   **[Spreadsheet Workbench - FreeCAD Documentation](https   *//wiki.freecadweb.org/Spreadsheet_Workbench)**
-   **[Manual   *Using spreadsheets - FreeCAD Documentation](https   *//wiki.freecadweb.org/Manual   *Using_spreadsheets)**
-   **[Customisable Parametric Design using Spreadsheets - FreeCAD Forum](https   *//forum.freecadweb.org/viewtopic.php?f=36&t=52196)**
-   **Forum Search and Specific Pages   * best pratices site   *forum.freecadweb.org at DuckDuckGo <https   *//duckduckgo.com/?q=best+pratices&sa=Search&sites=forum.freecadweb.org&ia=web>**
-   **[- Intro to Parametric Modelling - YouTube](https   *//www.youtube.com/watch?v=fXoRAYv1wHQ&feature=emb_logoFreeCAD)**
-   **[Feature editing - FreeCAD Documentation](https   *//wiki.freecadweb.org/Feature_editing/en)**

-   **[Best practice   * fuselage + wing - FreeCAD Forum](https   *//forum.freecadweb.org/viewtopic.php?f=36&t=33113)**
-   **[Some Tutorials on Methodology (v0.17) - Master Sketch, Skeleton Geometry, Spreadsheets - FreeCAD Forum](https   *//forum.freecadweb.org/viewtopic.php?f=36&t=43451)**

[Category   *Sandbox‏‎](Category   *Sandbox‏‎.md) [Category   *Spreadsheet‏‎](Category   *Spreadsheet‏‎.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sandbox‏‎]]  ](Category_Sandbox‏‎]]  .md) > Best Practices with SpreadSheets
