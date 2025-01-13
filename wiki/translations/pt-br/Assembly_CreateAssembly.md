---
 GuiCommand:
   Name: Assembly CreateAssembly
   MenuLocation: Assembly , Create Assembly
   Workbenches: Assembly_Workbench
   Shortcut: **A**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateAssembly/pt-br


</div>



## Descrição


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Assembly CreateAssembly](Assembly_CreateAssembly.md) tool creates a root assembly (Assembly object) in the current document, or a sub-assembly in a pre-existing active assembly. A document can only hold one root assembly.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Each Assembly object is created with an [Origin](App_OriginGroupExtension.md) object and an empty Joints container by default.


</div>



## Utilização


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  If the document already contains one or more assemblies: Activate an assembly.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Assembly_CreateAssembly.svg" width=16px> [Create Assembly](Assembly_CreateAssembly.md)** button.
    -   Select the **Assembly → <img src="images/Assembly_CreateAssembly.svg" width=16px> Create Assembly** option from the menu.
    -   Use the keyboard shortcut: **A**.
3.  A new Assembly object is created, either in the document or in the activated assembly.


</div>



## Propriedades


<div lang="en" dir="ltr" class="mw-content-ltr">

See also: [Property editor](Property_editor.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

An **Assembly** object, or formally an {{Incode|Assembly::AssemblyObject}}, has the following properties:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Data


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">


{{TitleProperty|Base}}


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

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


</div>



### Vista


<div lang="en" dir="ltr" class="mw-content-ltr">


{{TitleProperty|Display Options}}


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-    **Display Mode|Enumeration**: {{value|Group}} (the only option yet).

-    **Show In Tree|Bool**: {{value|true}} by default.

-    **Visibility|Bool**: {{value|true}} by default.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">


{{TitleProperty|Selection}}


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-    **On Top When Selected|Enumeration**:

-    **Selection Style|Enumeration**:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateAssembly/pt-br
