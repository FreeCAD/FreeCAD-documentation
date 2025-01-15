---
 GuiCommand:
   Name: Std Expressions
   Workbenches: All
---

# Std Expressions

## Description

The **Std Expressions** command copies expression data to and from the Clipboard. The data references the names of objects and documents and can only be used in that context.

 {{Code|lang=text|code=
##@@ Height Unnamed#Cylinder.ExpressionEngine (Cylinder)
##@@
Box.Width

##@@ Radius Unnamed#Cylinder.ExpressionEngine (Cylinder)
##@@
Box.Length
}} 
*Example Clipboard data*

## Usage

### Copy selected 

1.  Select one or more objects.
2.  Select the **Expression actions → Copy selected** option from the [Tree view](Tree_view.md) context menu.
3.  Expression data from the objects is copied to the Clipboard.

### Copy active document 

1.  Select the **Expression actions → Copy active document** option from the Tree view context menu.
2.  Expression data from all objects in the active document is copied to the Clipboard.

### Copy all documents 

1.  Select the **Expression actions → Copy all documents** option from the Tree view context menu.
2.  Expression data from all objects in all opened documents is copied to the Clipboard.

### Paste

1.  Make sure appropriate Clipboard data is available by using one of the previous options first.
2.  Select the **Expression actions → Paste** option from the Tree view context menu.
3.  Expression data from the Clipboard is pasted.
4.  The data is removed from the Clipboard.



---
⏵ [documentation index](../README.md) > Std Expressions
