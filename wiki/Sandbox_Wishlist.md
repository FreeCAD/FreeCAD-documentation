# Sandbox:Wishlist
## Introduction

This page is a wishlist of items that can improve the FreeCAD experience.

Anyone is free to add / remove / modify items here, i.e. help in recording new ideas and keeping it decently up to date. The purpose of the wishlist is not to replace forum posts, bug reports or feature requests, but rather serve as an incomplete overview of identified improvement areas.

The page is a complement to the [Workarounds](Workarounds.md) page, and less well maintained [Roadmap Category](   *Category_Roadmap.md) on this Wiki.

The page has 4 benefits   *

-   people can scan the page to see if an idea of theirs is already noted down
-   minimal effort to capture an idea that is then possible to find back
-   works for people that are not present at gh
-   avoids ideas to fade to a less discoverable spot in the forum


<div class="mw-collapsible mw-collapsed toccolours">

## Application wide 


<div class="mw-collapsible-content">

++++++++
| **Ver.** | **Item**                       | **Type** | **Current**                                                                                       | **Wish**                                                                                                                                                                                                                                                                                                        | **Additional**                                                                                                                                                                      | **Fixed in** |
++++++++
| 0.20     | Selection methods              | Modify   | There are multiple paradigms for how to select objects/entities for use with a command.           | More streamlined through the application. In order for that to happen, someone needs to make a detailed overview of how it works today for all corners of FreeCAD. That overview, to date, does not exist. So do not expect anything to happen on this topic unless it is kicked off with creating an overview. | [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=59384)                                                                                                              |              |
++++++++
| 0.20     | Control of spin widget ticks   | New      | Different spin widgets have different tick-steps, some in preference, some hardcoded?             | Add functionality to alter tick-size on the fly. Think font size up/down but for decimal point location. Should be part of std toolbar and affect relevant widgets.                                                                                                                                             | [forum thread](https   *//forum.freecadweb.org/viewtopic.php?p=543849#p543849)                                                                                                         |              |
++++++++
| 0.20     | Standardized performance tests | New      | Not present                                                                                       | Create some scripts to test & record performance of different aspects over time.                                                                                                                                                                                                                                | [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=70550) [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=73306&sid=ba36fcfc368afe5c111cbeddbc78626c) |              |
++++++++
| 0.20     | Editor preference              | Modify   | Current is tabs                                                                                   | Change default to 4 spaces.                                                                                                                                                                                                                                                                                     | [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=70620)                                                                                                             |              |
++++++++
| 0.20     | Selection                      | Modify   | Improve selection behaviour                                                                       | a\) do not deselect when ctrl is down                                                                                                                                                                                                                                                                           | [forum thread](https   *//forum.freecadweb.org/viewtopic.php?p=638582#p638582)                                                                                                         | a\) 0.21     |
|          |                                |          |                                                                                                   |                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                     |              |
|          |                                |          |                                                                                                   |   b) instead of require “to be spot on” (within picking radius), i.e. preselection is active, one could select anything that is in closest proximity to the mouse click. Librecad does it this way, and it is very convenient.                                                                                |                                                                                                                                                                                     |              |
++++++++
| 0.20     | Box Selection                  | Modify   | No preview highlight when using box selection.                                                    | Add preview highlight for box selection.                                                                                                                                                                                                                                                                        |                                                                                                                                                                                     |              |
++++++++
| 0.20     | Macro dialogue                 | Modify   | No icons on the buttons.                                                                          | Add icons for the buttons                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                     |              |
++++++++
| 0.20     | Macro dialogue                 | Modify   | There is a button to edit macro path, but no button to open "location" with native file explorer. | Add button to open macro location in native file explorer.                                                                                                                                                                                                                                                      |                                                                                                                                                                                     |              |
++++++++
| 0.20     | Macro dialogue                 | Modify   | Button "Download" opens AddOnMgr                                                                  | Why not just have "AddOnManager" as button text?                                                                                                                                                                                                                                                                |                                                                                                                                                                                     |              |
++++++++


</div>


</div>


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

## Std / Base / AddonMgr 


<div class="mw-collapsible-content">

        
  **Ver.**   **Item**                                   **Type**       **Current**                                                                                                                                                                                                               **Wish**                                                                                                                                                                                                                                                                                                                                                                                                                                                             **Additional**                                                                                                                                                                                                                                      **Fixed in**
  0.20       Py imports                                 Modify         New users used to python often struggle with imports in current fc.                                                                                                                                                       Make imports behave more like vanilla python. Could also be beneficial to start a breaking journey to make addons pip/conda installable, while at the same time impose full namespacing for py code.                                                                                                                                                                                                                                                                 [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=29584&start=40) [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=67498&p=583438#p583438) [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=43280)   
  0.20       Macro folder missing from sys.path         Modify         Appears to be inconsistent behavior of adding the macro folder to sys.path.                                                                                                                                               No matter location (including non-std user settings) importing from macro folder should work out of the box. (is this currently handled by packaging?)                                                                                                                                                                                                                                                                                                               [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=72293)                                                                                                                                                                             
  0.20       Cmd args                                   Modify         Running headless with arguments is a bit of an headache (think running a sphinx build)                                                                                                                                    Make shell-runs behave more like vanilla python & a decent scheme for env-vars.                                                                                                                                                                                                                                                                                                                                                                                      [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=67780)                                                                                                                                                                             
  0.20       Restart command                            New            No file menu option to restart.                                                                                                                                                                                           A file menu option to restart.                                                                                                                                                                                                                                                                                                                                                                                                                                       [forum thread](https   *//wiki.freecadweb.org/Code_snippets#Close_and_restart_FreeCAD)                                                                                                                                                                 
  0.20       Measurement tool                           Modify / new   Several different tools, part wb measure is the most comprehensive built in option. Addon options include FCInfo, Asm4 Measure, QuickMeasure, etc.                                                                        A new application wide info tool located in inspection wb. Inspection wb should as well be able to compute area / volume of selected items (with its own icons)                                                                                                                                                                                                                                                                                                      [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=68243) [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=72643)                                                                                                      
  0.20       Category views                             Modify         Addon manager shows a flat (long) view of macros / wb's.                                                                                                                                                                  Simplest is probably just an additional preset filter with category. Both macros and wb's have a categorization already available, that should be possible to use in the addonmgr.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
  0.20       Internal rounding                          New            One symptom is for example that placement all of a sudden is -0.00                                                                                                                                                        That there was a possibility to apply round to geometries in an easy way. Should work application wide, i.e. any new geometry is created with rounded values (no more 1.23456e-7 instead of 0) with user setting. Think this implies a sort of inspection round when geometry comes back from occ. Should also be possible to take for example a polyline and round those coordinates to a given decimal number, analogue for a shell/solid/mesh and its vertexes.                                                                                                                                                                                                                                                       
  0.20       3d-view coordsys                           Modify         Cuts the right most letter (when in default) lower right location.                                                                                                                                                        Move zero of that coordsys slightly to left.                                                                                                                                                                                                                                                                                                                                                                                                                         [forum thread](https   *//forum.freecadweb.org/viewtopic.php?p=463243#p463243) [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=63527)                                                                                                 
  0.20       Set edge colors                            New            There is a dialogue for setting face colors.                                                                                                                                                                              Expand that dialogue, or a new one, for edge & vertex colors.                                                                                                                                                                                                                                                                                                                                                                                                        [forum thread](https   *//wiki.freecadweb.org/Macro_Colorize)                                                                                                                                                                                          
  0.20       Identifying versions when opening files.   New            Users are not informed when opening files created with earlier versions. Once the file is opened the earlier file is lost forever.                                                                                        Ask user if they want to save a back-up of the file before it is altered.                                                                                                                                                                                                                                                                                                                                                                                            [forum thread](https   *//forum.freecadweb.org/viewtopic.php?p=496590#p496590)                                                                                                                                                                         
  0.20       Pip install through gui                    New            Pip install is currently only by shell.                                                                                                                                                                                   Create a gui for correct installation of additional libs. Could be pip, conda, apt, etc based on existing install. If not actually running the command, at least it could produce a string to copy into shell, with info from which directory to run it from. Should be possible to do even for appimages.                                                                                                                                                           [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=57023)                                                                                                                                                                             
  0.20       Arrow for direction                        New            There is no visual indication of where a placement/attachment edit goes.                                                                                                                                                  Show an arrow indicating positive direction when user enters edit mode of such property, i.e when clicking for example z, an arrow will appear showing the positive direction an altered value will move the entity. Does not do much when everything is aligned to global xyz, but helps when coord sys are nested and individually rotated.                                                                                                                                                                                                                                                                                                                                                                            
  0.20       Creation / edit coordinates                New            When creating / editing draft objects the coordinate inputs are always tracking 3d-view mouse movements. This is unpractical if one just wants to enter coordinates, and happen to move the mouse in the 3d view.         a\) a reset button, so that all goes to zero b) checkbox for switching off tracking of 3d-view coordinates in input widgets. (implementation proposal in link)                                                                                                                                                                                                                                                                                                       [forum thread](https   *//forum.freecadweb.org/viewtopic.php?p=503914#p503914)                                                                                                                                                                         
  0.20       Font for shapestring                       Modify         Font must be given for something to render, user is not informed if font is missing. Meaning on a fresh install shapestring will most likely render nothing without notifying user.                                       a\) attempt to find font on os default locations, qt has current used font-family b) raise meaningful user info if nothing is rendered                                                                                                                                                                                                                                                                                                                               [forum thread](https   *//forum.freecadweb.org/viewtopic.php?p=509970#p509970)                                                                                                                                                                         
  0.20       Improved coordinate api                    Modify         For example Vector is an iterable, whereas Vertex is not.                                                                                                                                                                 a\) all should be iterables out of the box b) vertex should have same py.\_\_repr\_\_ as vector c) vector could have a round method d) there could be a application wide setting for number of decimals to show in \_\_repr\_\_                                                                                                                                                                                                                                      [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=63751)                                                                                                                                                                             
  0.20       Macro folders                              Modify         Today one and only one folder must be used for macros.                                                                                                                                                                    a\) allow for recursive folders in "user/Macro" b) allow to configure multiple folders c) new document object type that holds a path to a macro that runs if doc.obj is double-clicked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
  0.20       Transform widget origin                    Modify         Always show in placement coord.                                                                                                                                                                                           Make configurable to also show in for example shape cog.                                                                                                                                                                                                                                                                                                                                                                                                             [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=67159) [forum thread](https   *//github.com/FreeCAD/FreeCAD/issues/6588)                                                                                                               
  0.20       Dxf import                                 New            Dxf import is a constant and reoccurring source of forum posts showcasing different issues.                                                                                                                               Use ezdxf as base for dxf import, seems like parts of ezdxf can optionally be compiled for speed. In any case a pure python importer based on ezdxf appears to have ability to outpace current c-importer, so a pure python implementation to begin with focusing on coverage should be good enough.                                                                                                                                                                 [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=68444)                                                                                                                                                                              
  0.20       Group                                      New            The count of children in a group is only available through scripting.                                                                                                                                                     Show children count of a selected group in "status bar". Could be valid for any other container object as well. Or the count could be part of the tool-tip when hoovering in the tree-view.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
  0.20       Selection view                             Modify         No gui indication of total amount of selected objects.                                                                                                                                                                    Add label at bottom of "selection view" with total amount of selected entities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
  0.20       Macro execution                            New            No meaningful way to stop execution of a macro other than killing the whole application.                                                                                                                                  Introduce a way to break a running macro, corresponding to "ctrl-c" in a vanilla python session. Could be a short-cut of a gui-button.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
  0.20       Macro namespace                            New            Macro variables not available in python console after execution. Actually they can be made to be, they just are not with default settings.                                                                                a\) change default to \"run in global\". b) introduce a \"macro\" namespace that could be imported, would avoid possible conflicts with fc main namespace.                                                                                                                                                                                                                                                                                                           [macro settings](https   *//wiki.freecadweb.org/Preferences_Editor#Macro)                                                                                                                                                                              
  0.20       Shape.BoundBox                             Modify         In python, Shape.BoundBox appears to be a static snap-shot, i.e. it is not a reference to current data. A recompute does not reflect updated values, the Shape.BoundBox has to be reassigned to pick up current values.   Modify the python version of Shape.BoundBox to reflect current values after a recompute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
  0.20       Macro toolbar \"execute\"                  Modify         Only runs macro when macro is the active tab in document/3d-view.                                                                                                                                                         If no macro open/shown in 3d-view, run the first macro in the "recent macro" list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        


</div>


</div>


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

## Arch


<div class="mw-collapsible-content">

        
  **Ver.**   **Item**    **Type**   **Current**                                                          **Wish**                                         **Additional**                                                                **Fixed in**
  0.20       Cut-plane   Bug        Transparency and color of cut-plane is transferred to final solid.   Object appearance should be unaffected by cut.   [forum thread](https   *//forum.freecadweb.org/viewtopic.php?p=628242#p628242)   
        


</div>


</div>


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

## Draft


<div class="mw-collapsible-content">

        
  **Ver.**   **Item**                        **Type**   **Current**                                                                                                                                                                                                                                                                                                                                            **Wish**                                                                                                                                                                                                                                                                                **Additional**                                                                    **Fixed in**
  0.20       Move                            Modify     If wanting to make for example 10 lines as transformed copies, when using draft/move and enabling "continue & copy" the dialogue still automatically closes when 2nd point is defined.                                                                                                                                                                 Keep dialogue open for a new move. Additionally when in copy/continue mode, the 1st point can be skipped, it should be the 2nd point of the last move (with relative setting that is zero, but it would save one button press if there was no need to re-enter that)                                                                                                      
  0.20       Chain select                    New        Path wb has chain select, but it bugs out on for example a set of draft/lines.                                                                                                                                                                                                                                                                         A chain select command in base wb's (std/draft/part?) with option to a) chain connected b) chain tangent. Should also not break out of command when hitting a branch of edges, it should simply stay in selection mode and allow for selection of branch and thus continue the chain.                                                                                     
  0.20       Dimension                       Modify     When adding a dimension, the actual dimension is often way too small.                                                                                                                                                                                                                                                                                  First fontsize should be a portion of document bounding box. Rather than the application default, there should be a document default value, and once that is set, it stays -- so no change in property as such, just how the first value is set in a document.                                                                                                            
  0.20       Scale                           Modify     Input widget for scale factor is not user friendly. a) try and enter a scale factor of 1.23 with a fresh install b) does not take expressions.                                                                                                                                                                                                         Better handling of decimal entries and allow expressions in input widget.                                                                                                                                                                                                                                                                                                 
  0.20       Edit dialogue for wire/spline              Hard to discover how to add/remove points to wires & splines. If one edits wires in current versions, there is more clicks now than earlier, which matters a lot if you are cleaning files that have a large amount of points (read thousands\...)                                                                                                     a\) bring back the buttons from v0.18 into the edit dialogue b) make a label widget explaining the procedure to add/remove points.                                                                                                                                                      [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=57630&start=30)   
  0.20       Scale                           Modify     An arc cannot be scaled in draft without making a clone.                                                                                                                                                                                                                                                                                               Make it possible to scale arcs naively, should not be technically impossible, even with non-uniform scaling parameters (although it will change the type of entity irreversibly).                                                                                                                                                                                         
  0.20       Transform                       New        Part/transform widget does not work on draft objects.                                                                                                                                                                                                                                                                                                  Adapt transform widget to work also for draft objects.                                                                                                                                                                                                                                                                                                                    
  0.20       Split taskpanel                 Modify     Esc does not exit task-panel.                                                                                                                                                                                                                                                                                                                          Make esc exit task panel in draft, it does on some draft taskpanels but not all. There are more than split, for example shapestring.                                                                                                                                                                                                                                      
  0.20       Split / downgrade etc           Modify     When using a dividing function in draft, split, downgrade, etc. If the object is in a group the new objects end up in root.                                                                                                                                                                                                                            Dividing operations should respect the original object location (group/layer) and be created in that location.                                                                                                                                                                                                                                                            
  0.20       Points removal from wires       New        Currently 3 clicks (and 2 hands) are required to remove a point from a wire. Alt needs to be pressed, the point needs to clicked, rmb needs to be clicked and "delete point" needs to be clicked in the context menu.                                                                                                                                  Allow for box selection in the wire edit mode and have a button for deletion of points, or possibly context menu entry.                                                                                                                                                                                                                                                   
  0.20       Svg export                      Modify     A draft line, etc with a dash-dot decoration, exported to svg, imports as a solid line into inkscape.                                                                                                                                                                                                                                                  Respect line decorations in exports to svg.                                                                                                                                                                                                                                                                                                                               
  0.20       ShapeString                     Modify     ShapeString does not allow for alternative aligning.                                                                                                                                                                                                                                                                                                   Make aligning properties such as "right-align", "center", etc. the full capability would be NSEW or any combination of those with the additional centre option.                                                                                                                                                                                                           
  0.20       Draft linestyle                 Modify     To reproduce   * change linestyles to "dashed", the gap is dynamic based on object size and zoom (assuming this, but that is how it appears to work on screen). Now if one object is about half in size, it will appear as solid line on screen although dashed is set, this is valid when zoomed out, if one zooms in it appears dashed on the screen.   Modify gap algo to care for all objects in such way that dashed is dashed on the screen (btw, dashdot behaves different...)                                                                                                                                                                                                                                               
        


</div>


</div>


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

## Sketcher


<div class="mw-collapsible-content">

        
  **Ver.**   **Item**                                **Type**   **Current**                                                                                                                  **Wish**                                                                                                                                                                                                                                                                                                                                                                                                                 **Additional**                                                           **Fixed in**
  0.20       Optional "missing coincidences check"   New        Not being able to extrude/pad due to missing coincidences in sketches is a constant and reoccurring source of forum posts.   Auto check for missing coincidences when closing a sketch. Should be a preference to switch behaviour on/off. Should be on as default since the target audience is new users. That there are usecases for open vertexes should not affect this, deliberate open vertexes have little to do with missing coincidences. Could be made fancy and only raise the info dialogue if found and be silent if nothing is found.   [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=66091)   
  0.20       Angle constraint                        New        Support common angles, steps of 15.                                                                                          See forum thread                                                                                                                                                                                                                                                                                                                                                                                                         [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=70424)   
        


</div>


</div>


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

## Part


<div class="mw-collapsible-content">

++++++++
| **Ver.** | **Item**                       | **Type** | **Current**                                              | **Wish**                                                                                                  | **Additional**                                                          | **Fixed in** |
++++++++
| 0.20     | Loft                           | Modify   | Selection widget only allows to add profiles one by one. | a\) multi-select with ctrl-key down                                                                       |                                                                         |              |
|          |                                |          |                                                          |                                                                                                           |                                                                         |              |
|          |                                |          |                                                          |   b) new buttons to “add all” / “remove all”                                                            |                                                                         |              |
++++++++
| 0.20     | Undesired reset of colors      | Bug      | Color of shape resets to default without asking for it.  | To be fixed, description in forum post.                                                                   | [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=68411) |              |
++++++++
| 0.20     | Rework check geometry dialogue | Modify   | See forum thread.                                        |                                                                                                           | [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=34&t=70809) |              |
++++++++
| 0.20     | Segfault sweep                 | Bug      | Example file in forum post.                              |                                                                                                           | [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=70770)  |              |
++++++++
| 0.20     | Fuse behaviour on larger sets  | Modify   | Example in forum post.                                   | For operations where a list is passed, it appears that chunking the operation makes a noticable speed-up. | [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=73306) |              |
++++++++


</div>


</div>


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

## Part Design 


<div class="mw-collapsible-content">

        
  **Ver.**   **Item**               **Type**       **Current**                                                                                                      **Wish**                                                                                                                                                                                           **Additional**                                                           **Fixed in**
  0.20       Out of body message.   Modify / new   Cryptic error for new comers when trying to do operations on entities outside of the body.                       a\) open a dialogue for selecting objects to move into the body. b) error message with suggestions for actions, rather than just stating what is wrong.                                            [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=55575)   
  0.20       Hole                   Modify         Direction of hole is always same, occasionally leading to a hole initially not being made, this confuses users   Add heuristics to apply a direction of the hole that is actually producing a cavity. Heuristics is only for best guess during creation. The "reverse" property should stay as a static property.                                                                            
        


</div>


</div>


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

## Mesh


<div class="mw-collapsible-content">

        
  **Ver.**   **Item**             **Type**   **Current**                                                                          **Wish**                                                                                                                                                                                   **Additional**                                                                             **Fixed in**
  0.20       Merge close points   New        No built in way to merge close points on a mesh.                                     Repair option to merge close points, with dialogue to set distance (in mm) for what qualifies as a close point. Returns a new mesh with valid topology.                                                                                                                               
  0.20       Show / hide facets   New        Can show/hide complete meshes.                                                       Allow for selection of faces, and a graphical way to hide them along with a reset button. The hiding should be persistent, so that one can use other operations while hidden.                                                                                                         
  0.20       Split facet          New        No obvious way to split facets.                                                      Select a facet, it is then split in 2 with the longest edge split at midpoint.                                                                                                                                                                                                        
  0.20       Move facet point     New        No gui for redefining a single facet point.                                          Select a point in a mesh, snap to another existing point on another facet, not necessarily on same mesh, but always a mesh-object.                                                                                                                                                    
  0.20       Mesh boolean icons   Modify     Think they are not disabled although fc cannot find a valid OpenSCad installation.   Commands should be disabled if there is no valid OpenSCad installation on the machine. Maybe update the preference page with a button to check if there is a valid installation as well.                                                                                              
  0.20       Add triangle         Modify     Pop-up menu today is "Add triangle / Flip normal / Clear"                            Suggest pop-up menu wording should be "Add triangle +N / Add triangle -N / Clear" or "Add +Normal / Add -Normal / Clear"                                                                                                                                                              
  0.20       Extract facet        New        Multiple steps to be able to extract a couple of facets to faces.                    Command that allows selection of individual facets and upon "ok/apply" it creates part.faces from the selected facets.                                                                     [forum thread](https   *//forum.freecadweb.org/viewtopic.php?p=510737#p510737)                
  0.20       Quad meshes          New        Handles exclusively trimeshes as of today                                            Add support for pure quad meshes and mixed tri/quad meshes.                                                                                                                                                                                                                           
  0.20       Scaling              Modify     Gui only allows for uniform scale.                                                   Allow non-uniform scaling via gui.                                                                                                                                                         [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=70713&p=614405#p614405)   
  0.20       Py-api               Modify     Mesh.show does not return document object.                                           Return the new document object when showing.                                                                                                                                               [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=70713&p=614405#p614405)   
        


</div>


</div>


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

## Points


<div class="mw-collapsible-content">

        
  **Ver.**   **Item**   **Type**   **Current**                                   **Wish**                                                                        **Additional**                                                           **Fixed in**
  0.20       Scaling    New        No native scaling command for point clouds.   Add scaling command to points wb, and a method for scaling in the points obj.   [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=66091)   
        


</div>


</div>


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

## FEM


<div class="mw-collapsible-content">

        
  **Ver.**   **Item**        **Type**   **Current**                                                        **Wish**                                 **Additional**                                                                **Fixed in**
  0.20       Torque load     New        No built in way to correctly apply a torque load.                  Make a torque constraint object & gui.   [forum thread](https   *//forum.freecadweb.org/viewtopic.php?p=420008#p420008)   
  0.20       Use multicore   Modify     Appears that preference setting for multi-core is not effective.   Fix in link\...                          [forum thread](https   *//forum.freecadweb.org/viewtopic.php?p=519494#p519494)   
        


</div>


</div>


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

## Image


<div class="mw-collapsible-content">

        
  **Ver.**   **Item**     **Type**   **Current**    **Wish**                                                                                               **Additional**                                                            **Fixed in**
  0.20       Python api   New        Non existing   Add py-api with image object. Creation of object either with path to image on disk or data as bytes.   [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=70504)   
        


</div>


</div>


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

## Wiki


<div class="mw-collapsible-content">

        
  **Ver.**   **Item**                 **Type**   **Current**                                                                                                                                                                                     **Wish**                                        **Additional**   **Fixed in**
  \-         Versioning / archiving   New        a\) No agreed means to lock a version of the wiki. The crawler used to create the qt helpfiles is not a complete snap, it is a partial crawl. b) could use an "archived v.xyz" scheme as well   A robuster way to secure legacy info on wiki.                    
        


</div>


</div>


{{Top}}


<div class="mw-collapsible mw-collapsed toccolours">

## Fixed


<div class="mw-collapsible-content">

        
  **Workbench**   **Item**             **Type**   **Current**                                                      **Wish**   **Additional**                                                                                                                                                                          **Fixed in**
  Draft           Spline 2 arc / dxf   Bug        See forum thread. An easy fix for someone working with git\...              [forum thread](https   *//forum.freecadweb.org/viewtopic.php?p=600132#p600132) [gh source](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Draft/draftgeoutils/arcs.py#L135-L147)   0.21 [gh pull](https   *//github.com/FreeCAD/FreeCAD/pull/7821)
                                                                                                                                                                                                                                                                                                                      
        


</div>


</div>


{{Top}}

[Category   *Roadmap](Category_Roadmap.md) [Category   *Sandbox](Category_Sandbox.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Roadmap]] ](Category_Roadmap]] .md) > Sandbox:Wishlist
