# Sandbox:TestWikiPage/de
### Überblick

= Diese Seite kann verwendet werden, um die Wiki Markierung vor der Bearbeitung einer echten Seite auszuprobieren. Fühle dich frei, hier zu tun, was immer du willst!

## **FreeCAD Kurzreferenz Karten** 

### Dateimenü - Alt+F 

  Command                           Icon                                               Shortcut      Command                                Icon                                               Shortcut          Command                                     Icon                                                                     Shortcut
  --------------------------------- -------------------------------------------------- ---------- -- -------------------------------------- -------------------------------------------------- -------------- -- ------------------------------------------- ------------------------------------------------------------------------ ----------
  [New](Std_New.md)         <img alt="" src=images/Std_New.svg  style="width:32px;">         Ctrl+N        [Open](Std_Open.md)            <img alt="" src=images/Std_Open.svg  style="width:32px;">       Ctrl+O            [Close](Std_CloseActiveWindow.md)   <img alt="" src=images/Std_CloseActiveWindow.svg  style="width:32px;">   Ctrl+F4
  [Save](Std_Save.md)       <img alt="" src=images/Std_Save.svg  style="width:32px;">       Ctrl+S        [Save as\...](Std_SaveAs.md)   <img alt="" src=images/Std_SaveAs.svg  style="width:32px;">   Ctrl+Shift+S      [Import](Std_Import.md)             <img alt="" src=images/Std_Import.svg  style="width:32px;">                         Ctrl+I
  [Export](Std_Export.md)   <img alt="" src=images/Std_Export.svg  style="width:32px;">   Ctrl+E        [Print](Std_Print.md)          <img alt="" src=images/Std_Print.svg  style="width:32px;">     Ctrl+P            [Exit](Std_Exit.md)                 <img alt="" src=images/Std_Quit.svg  style="width:32px;">                             Alt+F4

### Bearbeitungsmenü - Alt+E 

  Command                                        Icon                                                           Shortcut      Command                                        Icon                                                               Shortcut                                   Command                                    Icon                                                     Shortcut
  ---------------------------------------------- -------------------------------------------------------------- ---------- -- ---------------------------------------------- ------------------------------------------------------------------ --------------------------------------- -- ------------------------------------------ -------------------------------------------------------- --------------
  [Undo](Std_Undo.md)                    <img alt="" src=images/Std_Undo.svg  style="width:32px;">                   Ctrl+Z        [Redo](Std_Redo.md)                    <img alt="" src=images/Std_Redo.svg  style="width:32px;">                       Ctrl+Shift+Z (Linux) Ctrl+Y (Windows)      [Cut](Std_Cut.md)                  <img alt="" src=images/Std_Cut.svg  style="width:32px;">               Ctrl+X
  [Copy](Std_Copy.md)                    <img alt="" src=images/Std_Copy.svg  style="width:32px;">                   Ctrl+C        [Paste](Std_Paste.md)                  <img alt="" src=images/Std_Paste.svg  style="width:32px;">                     Ctrl+V                                     [Refresh](Std_Refresh.md)          <img alt="" src=images/Std_Refresh.svg  style="width:32px;">       Ctrl+R or F5
  [Box Selection](Std_BoxSelection.md)   <img alt="" src=images/Std_BoxSelection.svg  style="width:32px;">   Ctrl+B        [Select All](Std_SelectAll.md)         <img alt="" src=images/Std_SelectAll.svg  style="width:32px;">                                                        [Delete](Std_Delete.md)            <img alt="" src=images/Std_Delete.svg  style="width:32px;">         Del
  [Toggle Edit Mode](Std_Edit.md)        <img alt="" src=images/Std_Edit.svg  style="width:32px;">                                 [Preferences](Std_DlgPreferences.md)   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;">                                              [What\'s This](Std_WhatsThis.md)   <img alt="" src=images/Std_WhatsThis.svg  style="width:32px;">   Shift+F4

### Ansichtsmenü - Alt+V 

  Command                                                  Icon                                                       Shortcut   Sub      Command                                                Icon                                                           Shortcut   Sub      Command                                                Icon   Shortcut   Sub
  -------------------------------------------------------- ---------------------------------------------------------- ---------- ----- -- ------------------------------------------------------ -------------------------------------------------------------- ---------- ----- -- ------------------------------------------------------ ------ ---------- -------------------------------------------
  [Orthographic view](Std_OrthographicCamera.md)   <img alt="" src=images/View-isometric.svg  style="width:32px;">   O                   [Perspective view](Std_PerspectiveCamera.md)   <img alt="" src=images/View-perspective.svg  style="width:32px;">   P                   Standard views                                         icon              [Sub](#View_->_Standard_Views.md)
  [Stereo](Std_ViewIvStereo.md)                    Icon                                                       Alt+S                                                                                                                                                         [Toggle visibility](Std_ToggleVisibility.md)   Icon   Space      
  Toggle navigation/edit mode                              Icon                                                       Esc                 [Appearance\...](Std_SetAppearance.md)         Icon                                                           Ctrl+D              Toolbars                                               Icon   Alt+B      
  [Views](Std_Views.md)                            Icon                                                       Alt+W                                                                                                                                                                                                                                  

#### Ansicht -\> Standard Ansichten 

  Command     Icon                                                              Shortcut      Command   Icon                                                        Shortcut      Command   Icon                                                         Shortcut      Command   Icon                                                      Shortcut
  ----------- ----------------------------------------------------------------- ---------- -- --------- ----------------------------------------------------------- ---------- -- --------- ------------------------------------------------------------ ---------- -- --------- --------------------------------------------------------- ----------
  Axometric   [32px\|text-top=isometric](Image:View-isometric.svg.md)   0             Front     [32px\|text-top=front](Image:View-front.svg.md)     1             Top       [32px\|text-top=top](Image:View-top.svg.md)          2             Right     [32px\|text-top=right](Image:View-right.svg.md)   3
  Rear        [32px\|text-top=rear](Image:View-rear.svg.md)             4             Bottom    [32px\|text-top=bottom](Image:View-bottom.svg.md)   5             Left      [32px\|text-top=View-left](Image:View-left.svg.md)   6                                                                                 

#### View -\> Freeze display 

  Command       Icon   Shortcut
  ------------- ------ ----------
  Freeze View          Shift+F

#### View -\> Zoom 

  Command   Icon                                                                Shortcut      Command    Icon                                                              Shortcut      Command                                  Icon                                                                     Shortcut
  --------- ------------------------------------------------------------------- ---------- -- ---------- ----------------------------------------------------------------- ---------- -- ---------------------------------------- ------------------------------------------------------------------------ ----------
  Zoom In   [32px\|text-top=View-zoom-in](File:Std_ViewZoomIn.svg.md)   Ctrl++        Zoom Out   [32px\|text-top=zoom-out](Image:Std_ViewZoomOut.svg.md)   Ctrl+-        [Box zoom](Std_ViewBoxZoom.md)   [32px\|text-top=View-zoom-border](File:Std_ViewBoxZoom.svg.md)   Ctrl+B

#### View -\> Document window 

  Command                                             Icon   Shortcut      Command                                               Icon   Shortcut
  --------------------------------------------------- ------ ---------- -- ----------------------------------------------------- ------ ----------
  [Docked](Std_ViewDockUndockFullscreen.md)   icon   D             [Undocked](Std_ViewDockUndockFullscreen.md)   icon   U

### Macro Menu - Alt+M 

  Command                                            Icon                                                                 Shortcut      Command                                                  Icon                                                                 Shortcut      Command                                           Icon                                                                 Shortcut
  -------------------------------------------------- -------------------------------------------------------------------- ---------- -- -------------------------------------------------------- -------------------------------------------------------------------- ---------- -- ------------------------------------------------- -------------------------------------------------------------------- ----------
  [Macro recording](Std_DlgMacroRecord.md)   <img alt="" src=images/Std_DlgMacroRecord.svg  style="width:32px;">                   [Stop macro recording](Std_MacroStopRecord.md)   <img alt="" src=images/Std_MacroStopRecord.svg  style="width:32px;">                 [Execute macro](Std_DlgMacroExecute.md)   <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:32px;">   Ctrl+F6
  [Debug macro](Std_MacroStartDebug.md)      <img alt="" src=images/Std_MacroStartDebug.svg  style="width:32px;">   F6            [Stop debugging](Std_MacroStopDebug.md)          <img alt="" src=images/Std_MacroStopDebug.svg  style="width:32px;">     Shift+F6      [Step over](Std_MacroStepOver.md)                                                                              F10
  [Step into](Std_MacroStepInto.md)                                                                               F11           [Toggle breakpoint](Std_ToggleBreakpoint.md)                                                                          F9                                                                                                                                   

### Windows Menu - Alt+W 

  Command         Icon                                                       Shortcut      Command    Icon                                                       Shortcut      Command   Icon                                                             Shortcut      Command   Icon                                                             Shortcut
  --------------- ---------------------------------------------------------- ---------- -- ---------- ---------------------------------------------------------- ---------- -- --------- ---------------------------------------------------------------- ---------- -- --------- ---------------------------------------------------------------- ----------
  Next            <img alt="" src=images/Std_WindowNext.svg  style="width:32px;">   Alt+X         Previous   <img alt="" src=images/Std_WindowPrev.svg  style="width:32px;">   Alt+V         Tile      <img alt="" src=images/Std_WindowTileVer.svg  style="width:32px;">   Alt+T         Cascade   <img alt="" src=images/Std_WindowCascade.svg  style="width:32px;">   Alt+C
  Arrange Icons                                                              Alt+I         Windows                                                               Alt+W                                                                                                                                                                             

### Arch Menu - Alt+A 

  Command                                Icon                                                     Shortcut      Command                                         Icon                                                             Shortcut      Command                            Icon                                                 Shortcut      Command                            Icon                                                 Shortcut
  -------------------------------------- -------------------------------------------------------- ---------- -- ----------------------------------------------- ---------------------------------------------------------------- ---------- -- ---------------------------------- ---------------------------------------------------- ---------- -- ---------------------------------- ---------------------------------------------------- ----------
  [Wall](Arch_Wall.md)           <img alt="" src=images/Arch_Wall.svg  style="width:32px;">           W+A           [Structure](Arch_Structure.md)          <img alt="" src=images/Arch_Structure.svg  style="width:32px;">         S+T           [Rebar](Arch_Rebar.md)     <img alt="" src=images/Arch_Rebar.svg  style="width:32px;">     R+B           [Floor](Arch_Floor.md)     <img alt="" src=images/Arch_Floor.svg  style="width:32px;">     F+L
  [Building](Arch_Building.md)   <img alt="" src=images/Arch_Building.svg  style="width:32px;">   B+U           [Site](Arch_Site.md)                    <img alt="" src=images/Arch_Site.svg  style="width:32px;">                   S+I           [Window](Arch_Window.md)   <img alt="" src=images/Arch_Window.svg  style="width:32px;">   W+N           [Roof](Arch_Roof.md)       <img alt="" src=images/Arch_Roof.svg  style="width:32px;">       R+F
  [Axis](Arch_Axis.md)           <img alt="" src=images/Arch_Axis.svg  style="width:32px;">           A+X           [Section Plane](Arch_SectionPlane.md)   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;">   S+E           [Space](Arch_Space.md)     <img alt="" src=images/Arch_Space.svg  style="width:32px;">     S+P           [Stairs](Arch_Stairs.md)   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;">   S+R
  [Panel](Arch_Panel.md)         <img alt="" src=images/Arch_Panel.svg  style="width:32px;">         P+A           [Equipment](Arch_Equipment.md)          <img alt="" src=images/Arch_Equipment.svg  style="width:32px;">         E+Q           [Frame](Arch_Frame.md)     <img alt="" src=images/Arch_Frame.svg  style="width:32px;">     F+R           Set material                                                                            M+T
                                                                                                                                                                                                                                                                                                                                                                                                                                             



[Category:Documentation](Category:Documentation.md) [Category:Wiki](Category:Wiki.md) [Category:Sandbox](Category:Sandbox.md)

---
[documentation index](../README.md) > Sandbox:TestWikiPage/de
