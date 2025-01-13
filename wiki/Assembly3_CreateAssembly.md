---
 GuiCommand:
   Name: Assembly3 CreateAssembly
   Icon: Assembly_New_Assembly.svg
   MenuLocation: Assembly3 , Create assembly
   Workbenches: Assembly3_Workbench
   Shortcut: **A** **N**
---

# Assembly3 CreateAssembly

## Description

The <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width:24px;"> **Assembly3 CreateAssembly** command adds a new **Assembly** branch object to the model tree.

Each branch object is an <img alt="" src=images/Assembly_Assembly_Tree.svg  style="width:24px;"> **Assembly** container and holds four group containers:

:   \- One for the <img alt="" src=images/Assembly_Assembly_Constraints_Tree.svg  style="width:24px;"> **Constraints** (which is hidden as long as it is empty)
:   \- One for the <img alt="" src=images/Assembly_Assembly_Element_Tree.svg  style="width:24px;"> 
**Elements**
:   \- One for the <img alt="" src=images/Assembly_Assembly_Part_Tree.svg  style="width:24px;"> 
**Parts**
:   \- One for the <img alt="" src=images/Assembly_Assembly_Relation_Tree.svg  style="width:24px;"> **Relations** (which is hidden by default and will be revealed when the <img alt="" src=images/Assembly_GotoRelation.svg  style="width:16px;"> [Go to relation](Assembly3_GoToRelation.md) command is used)

 The added **Assembly** object with all visible containers looks like this (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-07.png  style="width:190px;"> <img alt="" src=images/Assembly3_Example-Tree-08.png  style="width:190px;">

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Assembly_New_Assembly.svg‎‎" width=16px> [Create assembly](Assembly3_CreateAssembly.md)** button.
    -   Select the **Assembly3 → <img src="images/Assembly_New_Assembly.svg‎‎" width=16px> Create assembly** option from the menu.
    -   Use the keyboard shortcut **A** then **N**
2.  An Assembly container is created.



---
⏵ [documentation index](../README.md) > Assembly3 CreateAssembly
