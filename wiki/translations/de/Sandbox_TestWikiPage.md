# Sandbox:TestWikiPage/de
### Überblick

= Diese Seite kann verwendet werden, um die Wiki Markierung vor der Bearbeitung einer echten Seite auszuprobieren. Fühle dich frei, hier zu tun, was immer du willst!

## **FreeCAD Kurzreferenz Karten** 

### Dateimenü - Alt+F 

  Command                           Icon                                               Shortcut      Command                                Icon                                               Shortcut          Command                                     Icon                                                                     Shortcut
  --------------------------------- -------------------------------------------------- ---------- -- -------------------------------------- -------------------------------------------------- -------------- -- ------------------------------------------- ------------------------------------------------------------------------ ----------
  _            <img alt="" src=images/Std_Open.svg  style="width:32px;">       Ctrl+O            [Close](Std_CloseActiveWindow.md)   <img alt="" src=images/Std_CloseActiveWindow.svg  style="width:32px;">   Ctrl+F4
  _   <img alt="" src=images/Std_SaveAs.svg  style="width:32px;">   Ctrl+Shift+S      [Import](Std_Import.md)             <img alt="" src=images/Std_Import.svg  style="width:32px;">                         Ctrl+I
  _          <img alt="" src=images/Std_Print.svg  style="width:32px;">     Ctrl+P            [Exit](Std_Exit.md)                 <img alt="" src=images/Std_Quit.svg  style="width:32px;">                             Alt+F4

### Bearbeitungsmenü - Alt+E 

  Command                                        Icon                                                           Shortcut      Command                                        Icon                                                               Shortcut                                   Command                                    Icon                                                     Shortcut
  ---------------------------------------------- -------------------------------------------------------------- ---------- -- ---------------------------------------------- ------------------------------------------------------------------ --------------------------------------- -- ------------------------------------------ -------------------------------------------------------- --------------
  _                    <img alt="" src=images/Std_Redo.svg  style="width:32px;">                       Ctrl+Shift+Z (Linux) Ctrl+Y (Windows)      [Cut](Std_Cut.md)                  <img alt="" src=images/Std_Cut.svg  style="width:32px;">               Ctrl+X
  _                  <img alt="" src=images/Std_Paste.svg  style="width:32px;">                     Ctrl+V                                     [Refresh](Std_Refresh.md)          <img alt="" src=images/Std_Refresh.svg  style="width:32px;">       Ctrl+R or F5
  _         <img alt="" src=images/Std_SelectAll.svg  style="width:32px;">                                                        [Delete](Std_Delete.md)            <img alt="" src=images/Std_Delete.svg  style="width:32px;">         Del
  _   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;">                                              [What\'s This](Std_WhatsThis.md)   <img alt="" src=images/Std_WhatsThis.svg  style="width:32px;">   Shift+F4

### Ansichtsmenü - Alt+V 

  Command                                                  Icon                                                       Shortcut   Sub      Command                                                Icon                                                           Shortcut   Sub      Command                                                Icon   Shortcut   Sub
  -------------------------------------------------------- ---------------------------------------------------------- ---------- ----- -- ------------------------------------------------------ -------------------------------------------------------------- ---------- ----- -- ------------------------------------------------------ ------ ---------- -------------------------------------------
  _   <img alt="" src=images/View-perspective.svg  style="width:32px;">   P                   Standard views                                         icon              [Sub](#View_->_Standard_Views.md)
  [Stereo](Std_ViewIvStereo.md)                    Icon                                                       Alt+S                                                                                                                                                         [Toggle visibility](Std_ToggleVisibility.md)   Icon   Space      
  Toggle navigation/edit mode                              Icon                                                       Esc                 [Appearance\...](Std_SetAppearance.md)         Icon                                                           Ctrl+D              Toolbars                                               Icon   Alt+B      
  [Views](Std_Views.md)                            Icon                                                       Alt+W                                                                                                                                                                                                                                  

#### Ansicht -\> Standard Ansichten 

  Command     Icon                                                              Shortcut      Command   Icon                                                        Shortcut      Command   Icon                                                         Shortcut      Command   Icon                                                      Shortcut
  ----------- ----------------------------------------------------------------- ---------- -- --------- ----------------------------------------------------------- ---------- -- --------- ------------------------------------------------------------ ---------- -- --------- --------------------------------------------------------- ----------
  Axometric   _   0             Front     _     1             Top       _          2             Right     _   3
  Rear        _             4             Bottom    _   5             Left      _   6                                                                                 

#### View -\> Freeze display 

  Command       Icon   Shortcut
  ------------- ------ ----------
  Freeze View          Shift+F

#### View -\> Zoom 

  Command   Icon                                                                Shortcut      Command    Icon                                                              Shortcut      Command                                  Icon                                                                     Shortcut
  --------- ------------------------------------------------------------------- ---------- -- ---------- ----------------------------------------------------------------- ---------- -- ---------------------------------------- ------------------------------------------------------------------------ ----------
  Zoom In   _   Ctrl++        Zoom Out   _   Ctrl+-        _   Ctrl+B

#### View -\> Document window 

  Command                                             Icon   Shortcut      Command                                               Icon   Shortcut
  --------------------------------------------------- ------ ---------- -- ----------------------------------------------------- ------ ----------
  [Docked](Std_ViewDockUndockFullscreen.md)   icon   D             [Undocked](Std_ViewDockUndockFullscreen.md)   icon   U

### Macro Menu - Alt+M 

  Command                                            Icon                                                                 Shortcut      Command                                                  Icon                                                                 Shortcut      Command                                           Icon                                                                 Shortcut
  -------------------------------------------------- -------------------------------------------------------------------- ---------- -- -------------------------------------------------------- -------------------------------------------------------------------- ---------- -- ------------------------------------------------- -------------------------------------------------------------------- ----------
  _   <img alt="" src=images/Std_MacroStopRecord.svg  style="width:32px;">                 [Execute macro](Std_DlgMacroExecute.md)   <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:32px;">   Ctrl+F6
  _          <img alt="" src=images/Std_MacroStopDebug.svg  style="width:32px;">     Shift+F6      [Step over](Std_MacroStepOver.md)                                                                              F10
  [Step into](Std_MacroStepInto.md)                                                                               F11           [Toggle breakpoint](Std_ToggleBreakpoint.md)                                                                          F9                                                                                                                                   

### Windows Menu - Alt+W 

  Command         Icon                                                       Shortcut      Command    Icon                                                       Shortcut      Command   Icon                                                             Shortcut      Command   Icon                                                             Shortcut
  --------------- ---------------------------------------------------------- ---------- -- ---------- ---------------------------------------------------------- ---------- -- --------- ---------------------------------------------------------------- ---------- -- --------- ---------------------------------------------------------------- ----------
  Next            <img alt="" src=images/Std_WindowNext.svg  style="width:32px;">   Alt+X         Previous   <img alt="" src=images/Std_WindowPrev.svg  style="width:32px;">   Alt+V         Tile      <img alt="" src=images/Std_WindowTileVer.svg  style="width:32px;">   Alt+T         Cascade   <img alt="" src=images/Std_WindowCascade.svg  style="width:32px;">   Alt+C
  Arrange Icons                                                              Alt+I         Windows                                                               Alt+W                                                                                                                                                                             

### Arch Menu - Alt+A 

  Command                                Icon                                                     Shortcut      Command                                         Icon                                                             Shortcut      Command                            Icon                                                 Shortcut      Command                            Icon                                                 Shortcut
  -------------------------------------- -------------------------------------------------------- ---------- -- ----------------------------------------------- ---------------------------------------------------------------- ---------- -- ---------------------------------- ---------------------------------------------------- ---------- -- ---------------------------------- ---------------------------------------------------- ----------
  _          <img alt="" src=images/Arch_Structure.svg  style="width:32px;">         S+T           _     <img alt="" src=images/Arch_Floor.svg  style="width:32px;">     F+L
  _                    <img alt="" src=images/Arch_Site.svg  style="width:32px;">                   S+I           _       <img alt="" src=images/Arch_Roof.svg  style="width:32px;">       R+F
  _   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;">   S+E           _   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;">   S+R
  _          <img alt="" src=images/Arch_Equipment.svg  style="width:32px;">         E+Q           [Frame](Arch_Frame.md)     <img alt="" src=images/Arch_Frame.svg  style="width:32px;">     F+R           Set material                                                                            M+T
                                                                                                                                                                                                                                                                                                                                                                                                                                             



_ _ _

---
[documentation index](../README.md) > Sandbox:TestWikiPage/de
