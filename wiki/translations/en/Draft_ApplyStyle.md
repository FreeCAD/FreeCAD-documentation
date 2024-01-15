---
 GuiCommand:
   Name: Draft ApplyStyle
   MenuLocation: Utilities , Apply current style
   Workbenches: Draft_Workbench, Arch_Workbench
   SeeAlso: Draft_SetStyle
---

# Draft ApplyStyle/en

## Description

The <img alt="" src=images/Draft_ApplyStyle.svg  style="width:24px;"> **Draft ApplyStyle** command applies the current style settings to selected objects.


{{VersionMinus|0.21}}

: This command handles only five of the settings the [Draft SetStyle](Draft_SetStyle.md) command offers.


<small>(v0.21)</small> 

: This command changes the view properties of objects. It applies all settings the [Draft SetStyle](Draft_SetStyle.md) command offers. It also changes these additional properties:

-    **Decimals**(for dimensions): See [Draft Preferences](Draft_Preferences#Texts_and_dimensions.md).

-    **ShowLine**(for dimensions): Idem.

## Usage

1.  Optionally change the style settings with the [Draft SetStyle](Draft_SetStyle.md) command.
2.  Select one or more objects.
3.  Select the **Utilities → <img src="images/Draft_ApplyStyle.svg" width=16px> Apply current style** option from the menu.

## Notes

-   The [Draft SetStyle](Draft_SetStyle.md) command can also apply settings.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ApplyStyle/en
