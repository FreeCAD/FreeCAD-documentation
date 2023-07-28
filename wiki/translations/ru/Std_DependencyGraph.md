---
- GuiCommand:/ru
   Name/ru:Граф зависимостей
   Name:Std DependencyGraph
   MenuLocation:Инструменты → Граф зависимостей...
   Workbenches:Все
---

# Std DependencyGraph/ru



## Описание

The **Std DependencyGraph** command displays the dependencies between objects in the active document in a \'dependency graph\'. As opposed to the [Tree view](Tree_view.md), objects are listed in reverse chronological order, with the first created object at the bottom.

It can be useful in analyzing a FreeCAD document and locating forks in a tree. The dependency graph layout will depend on which workbench was used to create the objects in the document. For example a model made exclusively in the [PartDesign](PartDesign_Workbench.md) workbench can display a linear dependency graph with a single vertical branch. A model made with [Part](Part_Workbench.md) operations will have many branches, but for a single part they will join up at the top after [Boolean](Part_Boolean.md) operations. If they don\'t, it means that they are separate objects.

The dependency graph is purely a visualization tool, therefore it cannot be edited. It automatically updates if changes are made to the model.

<img alt="" src=images/Std_DependencyGraph_example.svg  style="width:400px;"> 
*Example of a dependency graph with a PartDesign body on the left and an object created with Part operations on the right*



## Установка

To use the command a third-party software named [Graphviz](http://graphviz.org/) needs to be installed. If you do not have it pre-installed or it is installed in an unconventional location, FreeCAD will display the following dialog:

![](images/FreeCAD-0.17-missing-Graphviz-error-dialogue.png )

### Windows

Download the **graphviz-2.xx** installer from the [Graphviz Download page](https://graphviz.org/download/#windows) and launch it to install it. Some older versions seem to have issues displaying the graph; version 2.38 and newer are known to be reliable. You can find all graphviz releases on [Gitlab](https://gitlab.com/graphviz/graphviz/-/releases).

### macOS

You can install Graphviz using [Homebrew](https://brew.sh/) if you have macOS Big Sur (11) (or higher). While installing Homebrew, don\'t get nervous, if macOS asks you to install updates, e.g. for the Xcode commandline tools. These updates are performed later by the installation process.


{{Code|lang=text|code=
brew install graphviz
}}

This installs the Graphviz binaries under **/usr/local/bin** for macOS on Intel, or **/opt/homebrew** for macOS on Apple Silicon/ARM. FreeCAD should automatically find these locations. If the Graphviz program is not found you will be asked to specify a path. Unfortunately we can\'t navigate directly to the program in the file dialog that comes up from **Tools → Dependency graph...**. There are two options: You can use the key combination Cmd+Shift+. to show hidden items. Or you can use the key combination Cmd+Shift+G to get an input field for the path. Enter one of these paths in the [Terminal](https://en.wikipedia.org/wiki/Terminal_(macOS)):


{{Code|lang=text|code=
/usr/local/bin
}}

или:


{{Code|lang=text|code=
/opt/homebrew/bin
}}

and confirm the input field and the file selection dialog.

In case the Graphviz binaries are installed in a non-standard location try to find the program with the command:


{{Code|lang=text|code=
type dot
}}

It will output something like:


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}

And you can tell FreeCAD to look in that directory.

If you don\'t have macOS Big Sur (11) (or higher) Homebrew might not work, but you can use [MacPorts](https://www.macports.org/index.php) instead. Just download the [appropriate version for your OS](https://www.macports.org/install.php). Once the installation is complete, enter this command in the [Terminal](https://en.wikipedia.org/wiki/Terminal_(macOS)):


{{Code|lang=text|code=
sudo port install graphviz
}}

Enter your password and wait while the dependencies are downloaded and installed (it can take some time).

The Graphviz binaries may be under **/usr/local/bin** or **/opt/local/bin/dot**. FreeCAD may automatically find the Graphviz program with the file dialog that comes up from **Tools → Dependency graph...**, if not enter this command:


{{Code|lang=text|code=
type dot
}}

It will output something like:


{{Code|lang=text|code=
dot is /opt/local/bin/dot
}}

And you can tell FreeCAD to look in that directory as explained before.

It is also possible to make the opt directory visible with this command:


{{Code|lang=text|code=
defaults write com.apple.finder AppleShowAllFiles YES;
}}

then:


{{Code|lang=text|code=
killall Finder /System/Library/CoreServices/Finder.app;
}}

Therefore you can tell FreeCAD to follow this path. It has been successfully tested on macOS 10.13 (High Sierra).

### Linux

On most Linux distributions (Debian/Ubuntu, Fedora, OpenSUSE), you just need to install the Graphviz package from the repositories. However, similar to the macOS, in cases where the Graphviz binaries are installed in a non-standard location, try to find the program with the command:


{{Code|lang=text|code=
type dot
}}

It may output something like


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}

And therefore you can point FreeCAD to look in that directory.



## Применение

1.  Select the **Tools → <img src="images/Std_DependencyGraph.svg" width=16px> Dependency graph...** option from the menu.
2.  A new tab titled **Dependency graph** opens in the [Main view area](Main_view_area.md).
3.  Use the mouse scroll wheel to zoom in or out.
4.  Use the sliders at the bottom and at the right of the screen to pan the view. Alternatively hold down the left mouse button and move the mouse.

## Save

You can save a dependency graph:

1.  Make sure the Dependency graph tab is in the foreground.
2.  Select the **File → [Save](Std_Save.md)** or **File → [Save As](Std_SaveAs.md)** option from the menu.
3.  Enter a filename and select the file type (\*.png, \*.bmp, \*.gif, \*.jpg, \*.svg or \*.pdf).
4.  Press the **Save** button.

## General principles 

-   The graph shows objects in reverse chronological order.
-   The direction of arrows showing dependencies should always point down, from the child object to the parent object. An arrow pointing up indicates a cyclic dependency, an issue that needs to be resolved.
-   A sketch that contains links to [external geometry](Sketcher_External.md) will have a number with an \'x\' suffix besides the arrow linking it to its parent, showing the number of external geometries linked in the sketch.
-   Objects can have dependencies to multiple parents. For example, for a model built in [PartDesign](PartDesign_Workbench.md), a Pocket may be linked to its Sketch and to the Pad feature that came before it.
-   Disallowed dependencies (for example, between a [Draft](Draft_Workbench.md)/[Part](Part_Workbench.md) operation and an element inside a PartDesign Body) will show with a red arrow. This type of link usually shows a \'Links go out of allowed scope\' error in the [Report view](Report_view.md).
-   A [Part container](Std_Part.md) and [PartDesign Body](PartDesign_Body.md) enclose their content inside a frame with a randomly colored background. Their Origin also encloses its content (standard planes and axes) in a frame.
-   A [Groups](Std_Group.md) is displayed as a single element linked to its content.



## Ограничения

-   The dependency graph cannot help with the [topological naming problem](Topological_naming_problem.md). If a sketch switches faces of a feature after an edit, it is still linked to the feature. Even if some features are broken, the dependency graph will remain unchanged.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [3rd Party](Category_3rd Party.md) > Std DependencyGraph/ru
