# Macro Wiring And Hoses/en
{{Macro|Name=Macro Wiring And Hoses|Description=These macros support the creation and maintenance of Wires and Hoses.|Author=Piffpoof}}

**From [User:Piffpoof](User_Piffpoof.md) Note: some changes between v 0.14 and v 0.15 have effected this macro which will delay releasing it**

These macros support the creation and maintenance of Wires and Hoses.

![](images/Macro_Wiring_And_HosesCompletedHouse.jpg )

## Background

As part of our other FreeCAD projects we needed some way to document wiring and hoses. This set of macros was developed to meet that need. There is a lot this system doesn\'t do, but what it does do is provide visual representation of wiring and hoses, either as an isolated system or with the wiring and hoses in the context of a FreeCAD model. The record of all the wires and hoses is kept in a CSV format file outside of FreeCAD. So the file may be loaded into a spreadsheet program or used by other software.

## Description

As part of a documentation project we discovered we needed to document wires and hoses. We tried some different scenarios such as creating lines or cylinders as part of the existing model. Due to either problems using or maintaining it we decided to keep the information in a different format and outside of FreeCAD. That way they could be created on their own or created within an existing document. That decision allowed the user to work with the wiring and hoses in the way which suited them. As well they could work with it in different ways at different times as needs changed.

We initially weren\'t sure how to maintain a list of the hoses and wires and various different approaches were tried. The easiest way seemed to be to use the CSV file format which has been around for a long time. Also there were routines already written for managing CSV files from Python. Some of the advantages were:

-   human readable
-   can be loaded into any spreadsheet
-   can be maintained using a spreadsheet or simple text editor
-   a possible future enhancement would be to use it with the FreeCAD spreadsheet workbench

The next decisions were \"how\" to define such cables runs. As our purpose was primarily documentation, we chose to run line segments from point to point. Issues such as turn radius are not dealt with. Also cable diameter is not handled. A table of the cable runs is maintained through the CSV file but such things as proximity of cables (for electrical interference issues) and run length are not supported (although it might be possible to add a rudimentary cable run length quite easliy).

This set of macros is essentially a \"proof of concept\", it demonstrates some ideas and their feasibility. Our main goal was documentation, not physical plant management.We decided to maintain a data structure of points, which are the points through which the wires and hoses run. Secondly we set up a data structure which defines the cables and hoses in terms of the points they pass through. So a wire may only be routed where points for it have been defined.

For the 2 data structures we chose the following names:

-   Nexus - a point through which a cable or hose may pass (the plural is Nexi). Nexi are simply points in 3-space, for ease of visualisation the software places toroid rings around the location but this is only for ease of use. The toroid rings can be toggled off or on depending on user preference
-   Flows - generically these are routes comprised of Nexi. A code is associated with each type, the default codes being
    -   W - electrical wires
    -   C - conduits, intended primarily for wires but able to contain anything
    -   H - hoses to carry a variety of liquids
    -   G - gas lines
    -   K - a camera routing, this is really just reserved for future exploration as per [Tour camera animation](http://forum.freecadweb.org/viewtopic.php?f=24&t=8437)

Both Nexi and Flows have user assigned names, in addition Nexi have internally assigned IDs to facilitate management. Being points or locations in 3-space Nexi do not have colours but Flows can have one of 48 defined colours. The emphasis on colours ties back to the intended purpose being one of documentation.

The general workflow is

-   define and position Nexi
-   define Flow(s) in term of Nexi
-   for maintenance purposes edit both Nexi and Flows either visually using the FreeCAD GUI or using a tabular approach and the CSV definitions

As the data file which holds both the Nexi and Flow definition is text based it can be used in any text editor or by any other program wishing to access the data.

### Navigation Modes 

As a large part of the work with these macros depends on manipulating the display of the model to place and verify the placement of point in 3-space, it is essential to be comfortable with the Navigational Modes of FreeCAD which are documented on the page [Mouse navigation](Mouse_navigation.md). Being able to rotate the model in 3-space and then perform operations on a stationary model are essential.

## Installation

The code for Wiring And Hoses is in multiple macros and a library. So installation is comprised of copying the code to the appropriate Macro directory and invoking the Build Utility from the Macro menu, the Python console or a toolbar button (the preferred method).
-   see [How to install macros](How_to_install_macros.md) for information on how to install this macro code
-   see [Customize Toolbars](Customize_Toolbars.md) for information how to install as a button on a toolbar

## Usage

There are really two different approaches to working with these macros: the nexi and flows can be defined on their own using 3-space coordinates; or an existing FreeCAD document can be used and the nexi and flows can be defined in the context of that document. This is not an \'either/or\' decision but rather both approaches can be used when they are the most appropriate. As the definitions of the nexi and flows are kept in a CSV format file which is stored outside of FreeCAD, the presence or absence of a FreeCAD document does not affect working with the nexi and flow, it makes it easier by providing a visual context. For this description of usage the example will use a previously loaded FreeCAD document as a context as it is easier to place the

The usage of these macros really breaks down into 3 sections:

-   define nexi
-   define flows
-   edit the CSV format file to alter or add nexi and flows

There are alternative ways to perform some of the tasks outlined below and personal preference can decide. This example will apply electrical wiring and cold water plumbing to a house. Our empty house looks like this

![](images/Macro_Wiring_And_HosesEmptyHouse.jpg )

and is waiting for cold water and electricity to be installed. For convenience of explanation all the electrical items are in yellow and the water in blue (aside from the 2 sinks).

### Define Nexi 

The first step is one of creating points in 3-space (called \'nexi\' or \'nexus\" in the plural). These points will be used in the next step to define a flow. We create these points by clicking on (i.e. selecting) a surface and then supplying a name for the nexi. This description is of defining the nexi for the water flow.

1.  click on 
2.  the following dialog will appear:

 This is asking if you would like to open and load a FreeCAD document which has the model which you wish to add nexi and flows to. It is not necessary to load one but for this example we will load our empty house

1.  select a surface by clicking on it, it will be highlighted in the Tree window and have a colour indicating selected in the display.
2.  click on 
3.  the following dialog will appear asking for a name for the new nexi:



1.  the nexi will now be defined. It will be positioned in 3-space so that it is on the line from the selected face to the viewer, positioned just off the face so that it is not inside the object. Although the nexus might not be in the perfect position, leave it for the moment as it will be edited in a later step. A toroid (i.e. ring) will be displayed, it is centred on the point of the nexus. This ring is purely a visualisation tool so the location of the point can be identified. The visualisation rings can be toggled on/off at any time.
2.  define any more nexi in the same fashion, giving each a meaningful name
3.  click on 
4.  the following dialog will appear:



1.  answer Yes to save your new nexi

Note: at any point you can merge an existing project so as to have a visual context

### Define Flow 

Once nexi have been defined they can be used to define a flow. Our house now looks like this:

\< picture of house with nexi but not flows\>

It has nexi defined for the water flow but now flows as of yet.

1.  click on 

the following dialog will appear:



This is asking if you to select the nexi in the order you want them to create your flow.

1.  select the type of Flow: Wires, Conduits, Hoses, Gas Lines
2.  using the second popup, select the nexi in the order you want them



1.  supply a name for the flow
2.  select a colour for the flow
3.  click OK or Cancel. If you make an error in selecting the nexi (either order or including a wrong nexi) then click Cancel and restart this step.

\< picture of house with water flow\>

![](images/Macro_Wiring_And_HosesFlowsOnly.jpg )

### Editing Nexi and Flows 

There are 3 different ways to edit nexi. As the flows are defined in terms of nexi, altering nexi will affect any flow which includes them. For the descriptive flow attributes like colour and name, there is one way to make edits.

So far in this example we have generated the following table:







## User Interface 

The user interface is a combination of custom screens along with standard parts of the FreeCAD GUI.

\<snapshot 1 defining Nexi\>

\<snapshot 2 defining flow\>

\<snapshot 3 editing CSV file\>

\<snapshot 4 editing Position\>

## Options

At present there aren\'t really any options for Wiring and Hoses.

## Sample Files 

blah blah blah

## Remarks

blah blah blah

## Known Problems 

blah blah blah

## Future Possibilities 

blah blah blah

## Glossary

blah blah blah

## Links

blah blah blah

## Script

blah blah blah



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Wiring And Hoses/en
