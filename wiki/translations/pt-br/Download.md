# Download/pt-br
## Versão estável atual 


<div class="mw-translate-fuzzy">

A versão 0.19.2 do FreeCAD (24291) foi publicada em 2021-04-22. Para saber o que há de novo, veja as [Notas de lançamento](Release_notes_0.19/pt-br.md).


</div>


<div class="mw-translate-fuzzy">

Você encontrará a soma de verificação SHA256 para verificar a integridade de seu download na página [0.19.2 release](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19.2).


</div>


<div class="mw-translate-fuzzy">

Versões anteriores podem ser baixadas a partir da página [releases](https://github.com/FreeCAD/FreeCAD/releases).


</div>

+::+::+::+
| ![](images/Windows.png )                                                                                                          | ![](images/Mac.png )                                                                                                            | ![](images/Linux_with_text.png )                                                                                  |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [Install instructions](Installing_on_Windows.md)                                                                                | [Install instructions](Installing_on_Mac.md)                                                                              | [Install instructions](Installing_on_Linux.md)                                                                          |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Windows-x86_64-installer-1.exe)       | [ARM (M-series) disk image](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-macOS-arm64-py311.dmg) | [x86_64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Linux-x86_64-py311.AppImage)   |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [64-bit portable version (.7z)](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Windows-x86_64-py311.7z) | [Intel disk image](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-macOS-x86_64-py311.dmg)         | [aarch64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Linux-aarch64-py311.AppImage) |
++++

### Notes for Windows users 


<div class="mw-translate-fuzzy">

### Notas para usuários do Windows 

-   Os instaladores de 32 bits (x86) e 64 bits (x64) são compatíveis com os Windows 7, 8 e 10.
-   Há uma versão portátil ([64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD-0.19.2.7b5e18a-WIN-x64-portable1.7z)), que não precisa de instalação. Baixe-a a partir da página de lançamento.
-   O pacote também pode ser instalado a partir do gerenciador [Chocolatey](https://chocolatey.org/packages/freecad).


</div>

### Notes for macOS users 


<div class="mw-translate-fuzzy">

### Notas para usuários de Mac OS X 

Mac OS X 10.12 *Sierra* é a versão mínima compatível.


</div>



### Notas para usuários GNU/Linux 

A maioria das distribuições traz o FreeCAD em seus repositórios oficiais. No entanto, se a distribuição não seguir um modelo de lançamento contínuo, a versão que eles fornecem pode estar desatualizada. Ao invés disso, você pode baixar o AppImage acima, marcá-lo como executável e iniciá-lo sem instalação.

Consulte a página [Instalando no Linux](Installing_on_Linux/pt-br.md) para mais opções de instalação, incluindo pacotes diários para Ubuntu e derivados.


<div class="mw-translate-fuzzy">

Uma versão portátil que não precisa de instalação pode ser obtida iniciando o FreeCAD com estes comandos: <small>(v0.19)</small>  
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
```


</div>


{{Code|lang=text|code=
cd path/to/directory_containing_AppImage/
chmod +x ./name_of_AppImage_file.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./name_of_AppImage_file.AppImage
}}

Mais informações sobre as variáveis de ambiente do FreeCAD podem ser encontradas na página [página de configuração](Start_up_and_Configuration/pt-br#Variáveis_de_ambiente.md).

## Development versions 


<div class="mw-translate-fuzzy">

## Versões de desenvolvimento 

=

O desenvolvimento do FreeCAD está ativo.

-   Para usuários Linux, confira o desenvolvimento [AppImage](AppImage/pt-br.md).
-   Para compilações de desenvolvimento MacOS e Windows e código fonte de desenvolvimento, veja a página [compilações semanais](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds).
-   Para compilar o código-fonte mais recente, veja [compilação](Compiling/pt-br.md).


</div>



## Módulos e macros adicionais 


<div class="mw-translate-fuzzy">

A comunidade FreeCAD fornece muitos módulos e macros adicionais. A partir da versão 0.17 é possível instalá-los por dentro do próprio FreeCAD, usando o [Gerenciador de Extensões](Std_AddonMgr/pt-br.md). [24px](Imagem:Std_AddonMgr.svg.md).


</div>



---
⏵ [documentation index](../README.md) > Download/pt-br
