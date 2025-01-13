---
 GuiCommand:
   Name: Assembly CreateAssembly
   MenuLocation: Assembly , Create Assembly
   Workbenches: Assembly_Workbench
   Shortcut: **A**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateAssembly

## Description

The <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Assembly CreateAssembly](Assembly_CreateAssembly.md) tool creates a root assembly (Assembly object) in the current document, or a sub-assembly in a pre-existing active assembly. A document can only hold one root assembly.

Each Assembly object is created with an [Origin](App_OriginGroupExtension.md) object and an empty Joints container by default.

## Usage

1.  If the document already contains one or more assemblies: Activate an assembly.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Assembly_CreateAssembly.svg" width=16px> [Create Assembly](Assembly_CreateAssembly.md)** button.
    -   Select the **Assembly → <img src="images/Assembly_CreateAssembly.svg" width=16px> Create Assembly** option from the menu.
    -   Use the keyboard shortcut: **A**.
3.  A new Assembly object is created, either in the document or in the activated assembly.

## Properties

See also: [Property editor](Property_editor.md).

An **Assembly** object, or formally an {{Incode|Assembly::AssemblyObject}}, has the following properties:

### Data


{{TitleProperty|Base}}

-    **Type|String**:

-    **Material|Link**:

-    **Meta|Map|Hidden**:

-    **Id|String**:

-    **Uid|UUID|Hidden**:

-    **License|String**:

-    **License URL|String**:

-    **Color|Color**:

-    **Placement|Placement**:

-    **Label|String**:

-    **Label2|String|Hidden**:

-    **Expression Engine|ExpressionEngine|Hidden**:

-    **Visibility|Bool|Hidden**:

-    **Origin|Link|Hidden**:

-    **Group|LinkList**:

-    **_ Group Touched|Bool|Hidden**:

### View


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: {{value|Group}} (the only option yet).

-    **Show In Tree|Bool**: {{value|true}} by default.

-    **Visibility|Bool**: {{value|true}} by default.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**:

-    **Selection Style|Enumeration**:




 {{Assembly_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateAssembly
