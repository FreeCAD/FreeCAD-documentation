# Interface Customization/pt-br
{{TOCright}}

## Introdução

A interface do FreeCAD é baseada no moderno kit de ferramentas [Qt](http   *//en.wikipedia.org/wiki/Qt_(toolkit)) e tem uma organização de última geração. Alguns aspectos da interface podem ser personalizados. Você pode, por exemplo, adicionar barras de ferramentas personalizadas, com ferramentas de várias bancadas de trabalho (workbenches) ou ferramentas definidas em macros, e você pode criar seus próprios atalhos de teclado. Mas os menus e barras de ferramentas padrão que vêm com o FreeCAD e suas bancadas de trabalho não podem ser alterados.

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*The Customize dialog box*

## Utilização

1.  Os comandos disponíveis na caixa de diálogo \"Customize\" (Personalizar) dependem das bancadas de trabalho que foram carregadas na sessão atual do FreeCAD. Portanto, você deve primeiro carregar todas as bancadas de trabalho cujos comandos deseja ter acesso.
2.  Existem várias maneiras de invocar o comando <img alt="" src=images/Std_DlgCustomize.svg  style="width   *16px;"> [Std DlgCustomize](Std_DlgCustomize.md)   *
    -   Selecionar a opção **Tools → <img src="images/Std_DlgCustomize.svg" width=16px> Customize...** do menu.
    -   Clicar com o botão direito na área da barra de ferramentas e escolher **<img src="images/Std_DlgCustomize.svg" width=16px> Customize...** nos menus de contexto.
3.  A caixa de diálogo Personalizar é aberta. Para obter mais informações, consulte [Options](#Options.md).
4.  O botão **Help** não funciona neste momento.
5.  Pressione o botão **Close** para fechar a caixa de diálogo.

## Opções

Na caixa de diálogo \"Customize\" (Personalizar), as seguintes guias estão disponíveis   *

### \"Commands\" (Comandos) 

![](images/Std_DlgCustomize_tab_Commands.png ) 
*A guia "Commands" (Comandos)*

Nesta guia você pode navegar pelos comandos disponíveis.

#### Comandos de navegação 

1.  Selecione uma categoria de comando no painel **\"Category\"** (Categoria) à esquerda. Algumas categorias correspondem às entradas do menu.
2.  As ferramentas disponíveis na categoria selecionada são mostradas no painel à direita.
3.  Passe o mouse sobre um comando   * sua dica de ferramenta é exibida.
4.  Selecione um comando   * o texto da barra de status é exibido abaixo dos dois painéis.


{{Top}}

### \"Keyboard\" (Teclado) 

![](images/Std_DlgCustomize_tab_Keyboard.png ) 
*A guia "Keyboard" (Teclado)*

Nesta guia, atalhos de teclado personalizados podem ser definidos. Os atalhos para comandos de macro podem ser definidos na guia [Macros](#Macros.md).

#### Adicionar um atalho personalizado 

1.  Selecione uma categoria de comando na lista suspensa **\"Category\" (Categoria)**.
2.  Selecione um comando do painel **\"Commands\" (Comandos)**.
3.  A caixa **\"Current shortcut\" (Atalho atual)** exibe o atalho atual, se disponível.
4.  Insira um novo atalho na caixa de entrada **\"Press new shortcut\" (Digite um novo atalho)**. Os atalhos podem ter até 4 entradas. Cada entrada é um único caractere, uma combinação de uma ou mais teclas especiais ou uma combinação de uma ou mais teclas especiais e um caractere. Use **Backspace** para corrigir erros.
5.  Se o atalho já estiver em uso, uma caixa de diálogo perguntará se você deseja substituí-lo e o comando ao qual o atalho está atribuído aparecerá no painel **\"Currently assigned to\" (Atualmente atribuído a)**.
6.  Pressione o botão **Assign** para atribuir o novo atalho.
7.  Pressione o botão **Clear** para remover o atalho inserido. Isso também removerá o conteúdo da caixa **\"Current shortcut\" (Atalho atual)**. Observe que os atalhos padrão não são removidos permanentemente. Eles serão restaurados ao reiniciar o FreeCAD.

#### Remover um atalho personalizado 

1.  Selecione uma categoria de comando na lista suspensa **\"Category\" (Categoria)**.
2.  Selecione um comando do painel **\"Commands\" (Comandos)**.
3.  Pressione o botão **Reset**.

#### Remover todos os atalhos personalizados 

1.  Pressione o botão **Reset All**.

#### Notas (Keyboard) 

-   Os atalhos só funcionam se seus comandos aparecerem no menu padrão ou no menu de uma bancada que foi carregada na sessão atual do FreeCAD, ou se seus comandos aparecerem em uma barra de ferramentas *visível*.

-   Na V0.19, há um problema com alguns comandos da bancada de trabalho \"Draft\" (Rascunho). Seus atalhos padrão não funcionam e/ou atalhos personalizados não podem ser atribuídos a eles.
-   Para reatribuir um atalho padrão, um novo atalho deve ser atribuído ao seu comando original primeiro.


{{Top}}

### \"Workbenches\" (Bancadas de trabalho) 

![](images/Std_DlgCustomize_tab_Workbenches.png ) 
*A guia "Workbenches" (Bancadas de trabalho)*

On this tab the [Workbench selector](Std_Workbench.md) list can be changed. The **Enabled workbenches** list shows the workbenches as they will appear in the Workbench selector.

#### Disable a workbench 

1.  Select a workbench in the **Enabled workbenches** list.
2.  Press the **<img src="images/Button_left.svg" width=16px>** button.
3.  The workbench will be moved to the **Disabled workbenches** list

#### Re-enable a workbench 

1.  Select a workbench in the **Disabled workbenches** list.
2.  Press the **<img src="images/Button_right.svg" width=16px>** button.
3.  The workbench will be moved to the **Enabled workbenches** list

#### Re-enable all workbenches 

1.  Press the **<img src="images/Button_add_all.svg" width=16px>** button.

#### Change a workbench position 

1.  Select a workbench in the **Enabled workbenches** list.
2.  Press the **<img src="images/Button_up.svg" width=16px>** button or the **<img src="images/Button_down.svg" width=16px>** button.
3.  Optionally repeat this until the workbench is in the correct position.

#### Sort workbenches alphabetically 

1.  Press the **<img src="images/Button_sort.svg" width=16px>** button.


{{Top}}

### Toolbars

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*The Toolbars tab*

On this tab custom toolbars can be created and modified.

#### Select the workbench 

1.  In the dropdown list on the right select the workbench whose custom toolbars you want to modify. The {{Value|Global}} option is there for custom toolbars that should be available in all workbenches.

#### Create a toolbar 

1.  Press the **New...** button.
2.  Enter a name in the dialog box that opens.
3.  Press the **OK** button.
4.  The new toolbar will appear in the panel on the right.

#### Rename a toolbar 

1.  Select a toolbar in the panel on the right.
2.  Press the **Rename...** button.
3.  Enter a new name in the dialog box that opens.
4.  Press the **OK** button.

#### Delete a toolbar 

1.  Select a toolbar in the panel on the right.
2.  Press the **Delete** button.

#### Disable a toolbar 

1.  Uncheck the checkbox in front of the toolbar name in the panel on the right.
2.  A disabled toolbar will be invisible in the FreeCAD interface.

#### Add a command 

1.  At least one custom toolbar is required. See [Create a toolbar](#Create_a_toolbar.md).
2.  Select the correct toolbar in the panel on the right. If no toolbar is selected, the command will be added to the first toolbar in the list.
3.  Select a category from the dropdown list on the left. Macro commands that have been set up on the [Macros](#Macros.md) tab appear in the \'Macros\' category.
4.  Select a command from the panel on the left.
5.  Or select \'\' to add a separator (a line between two toolbar buttons).
6.  Press **<img src="images/Button_right.svg" width=16px>** button.

#### Remove a command 

1.  If required, expand the toolbar in the panel on the right.
2.  Select a command.
3.  Press **<img src="images/Button_left.svg" width=16px>** button.

#### Change a command position 

1.  If required, expand the toolbar in the panel on the right.
2.  Select a command.
3.  Press the **<img src="images/Button_up.svg" width=16px>** button or the **<img src="images/Button_down.svg" width=16px>** button.
4.  Optionally repeat this until the command is in the correct position.

#### Notes (Toolbars) 

-   Toolbars belonging to the current workbench are updated immediately, but after disabling/re-enabling a toolbar a workbench change is required (switch to a different workbench and then switch back).
-   To update global toolbars a workbench change (if commands have been added or removed) or a restart (if the order of a toolbar has changed or a toolbar was renamed) is required.

-   In V0.19 there is an issue with some Draft commands. After adding them to a custom toolbar and exiting the FreeCAD application the **user.cfg** file must be manually edited for these commands. Search for the name of the custom toolbar and in that section change the content of the `FCText` items that start with `gui_` to `DraftTools`.


{{Top}}

### Macros

![](images/Std_DlgCustomize_tab_Macros.png ) 
*The Macros tab*

On this tab user macro commands can be set up. Once set up, they can be added to custom toolbars. FreeCAD uses a dedicated folder for user macros and only macros in that folder can be set up. Use the <img alt="" src=images/Std_DlgMacroExecute.svg  style="width   *16px;"> [Std DlgMacroExecute](Std_DlgMacroExecute.md) command to find this folder on your system.

If you download a macro with the <img alt="" src=images/Std_AddonMgr.svg  style="width   *16px;"> [Addon Manager](Std_AddonMgr.md) then make sure that you also download its icon image file. Most macros have an image link on the information page that appears in the Addon Manager. You can for example put this image file in the user macros folder.

If you want to use a macro downloaded from a different source you will have to install it manually. See [How to install macros](How_to_install_macros.md) for more information.

#### Add a macro command 

1.  In the **Macro** dropdown list select a macro.
2.  Enter a **Menu text**. This will be the name used to identify the macro command and will also appear in the toolbar if there is no icon.
3.  Optionally enter a **Tool tip**. This text will appear near the location of the mouse when you hover the toolbar icon.
4.  Optionally enter a **Status text**. This text will appear in the [status bar](Status_bar.md) when you hover the toolbar icon.
5.  Optionally enter the wiki page for the macro, if available, in the **What\'s this** input box. Enter the page name, not the full URL.
6.  Optionally enter a shortcut in the **Accelerator** input box. See [Keyboard](#Keyboard.md) for more information.
7.  To add an icon   *
    1.  Press the **Pixmap** **...** button.
    2.  The Choose Icon dialog box opens.
    3.  If required press the **Icon folders...** button to add an icon folder.
    4.  Select an icon from the panel. The Choose Icon dialog box closes automatically.
8.  Press the **Add** button.
9.  The macro command appears in the panel on the left.
10. The macro command can now be selected on the [Toolbars](#Toolbars.md) tab.

#### Remove a macro command 

1.  Select the macro command in the panel on the left.
2.  Press the **Remove** button.

#### Change a macro command 

1.  Double-click the macro command in the panel on the left.
2.  Make the required changes. Note that you cannot remove the icon, you can only replace it.
3.  Press the **Replace** button.


{{Top}}

### Spaceball Motion 

This tab is blank if no Spaceball is detected. See   * [3Dconnexion input devices](3Dconnexion_input_devices.md). {{Top}}

### Spaceball Buttons 

This is tab is blank if no Spaceball is detected. See   * [3Dconnexion input devices](3Dconnexion_input_devices.md). {{Top}}

## Themes

FreeCAD supports complete theming of the interface, via .qss stylesheets. The [qss format](https   *//doc.qt.io/qt-5/stylesheet-syntax.html) is very similar to the [css format](https   *//en.wikipedia.org/wiki/CSS) used in web pages, it basically adds methods to reference the different widgets and elements of the Qt interface. You can change the default theme (which simply takes the style defined by your desktop system) by selecting a **style sheet** in the [FreeCAD preferences](Preferences_Editor#General.md).

You can also create your own theme if you are not satisfied with the themes that are bundled with FreeCAD, for example by editing an [existing style sheet](https   *//github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets). Your new style must be placed in a specific folder for it to be found by FreeCAD   *

-    **%APPDATA%/FreeCAD/Gui/Stylesheets**(on Windows). The **%APPDATA%** folder can be retrieved by entering {{Incode|App.getUserAppDataDir()}} in the [Python console](Python_console.md).

-    **$HOME/.FreeCAD/Gui/Stylesheets**(on Linux).

-    **$HOME/Library/Preferences/FreeCAD/Gui/Stylesheets**(on MacOS).


{{Top}}

## Addons

Addons offer yet another way to customize the use interface. Below are some addons created by users in the FreeCAD community. They can be downloaded through the <img alt="" src=images/Std_AddonMgr.svg  style="width   *16px;"> [Addon Manager](Std_AddonMgr.md) (note   * they are listed on the Workbenches tab).

### CubeMenu

-   Github repository   * <https   *//github.com/triplus/CubeMenu>

### Glass

-   Github repository   * <https   *//github.com/triplus/Glass>.

### IconThemes

-   Github repository   * <https   *//github.com/triplus/IconThemes>

### Launcher

-   Github repository   * <https   *//github.com/triplus/Launcher>

### PieMenu

-   Github repository   * <https   *//github.com/triplus/PieMenu>

### RemBench

-   Github repository   * <https   *//github.com/triplus/RemBench>

### ShortCut

-   Github repository   * <https   *//github.com/triplus/ShortCuts>


{{Top}}





{{Std Base navi

}} {{Interface navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Interface Customization/pt-br
