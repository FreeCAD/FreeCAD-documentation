# Download/pt-br
{{TOCright}}

## Versão estável atual 

A primeira versão 0.19.2 do FreeCAD (24291) foi publicada em 2021-04-22. Para saber o que há de novo, veja as [Notas de lançamento](Release_notes_0.19/pt-br.md).

Você encontrará a soma de verificação SHA256 para verificar a integridade de seu download na página [0.19.2 release](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19.2).

Versões anteriores podem ser baixadas da página [releases](https://github.com/FreeCAD/FreeCAD/releases).

+:----------------------------------------------------------------------------------------------------------------------------------------:+---+:------------------------------------------------------------------------------------------------------------------------------------------------------:+---+:-----------------------------------------------------------------------:+
| ![](images/Windows.png )                                                                                                           |   | ![](images/Mac.png )                                                                                                                                 |   | ![](images/AppImage-logo.png )                              |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| Install on Windows                                                                                                                       |   | Install on Mac                                                                                                                                         |   | Install on Linux                                                        |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| _ 64-bit |
+------------------------------------------------------------------------------------------------------------------------------------------+---+--------------------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------------+

### Notas para usuários do Windows 

-   O instalador de 32 bits (x86) suporta as seguintes versões do Windows: 7/8/10.
-   O instalador de 64 bits (x64) suporta as seguintes versões do Windows: 7/8/10.
-   Uma versão portátil ([64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD-0.19.2.7b5e18a-WIN-x64-portable1.7z)) que não precisa de instalação está na página de lançamento.
-   O pacote também pode ser instalado a partir do gerenciador [Chocolatey](https://chocolatey.org/packages/freecad).

### Notas para usuários de Mac OS X 

Mac OS X 10.12 *Sierra* é a versão mínima suportada.

### Notas para usuários GNU/Linux 

A maioria das distribuições traz o FreeCAD em seus repositórios oficiais, no entanto, se a distribuição não seguir um modelo de lançamento contínuo, a versão que eles fornecem pode estar desatualizada. Ao invés disso, você pode baixar o AppImage acima, marcá-lo como executável e iniciá-lo sem instalação.

Consulte a página [Instalando no Linux](Installing_on_Linux/pt-br.md) para mais opções de instalação, incluindo pacotes diários para Ubuntu e derivados.

Uma versão portátil que não precisa de instalação pode ser obtida iniciando o FreeCAD com estes comandos: <small>(v0.19)</small>  
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
```

Mais informações sobre as variáveis de ambiente do FreeCAD podem ser encontradas na [página de configuração](Start_up_and_Configuration/pt-br#Variáveis_de_ambiente.md).

## Versões de desenvolvimento 

= O desenvolvimento do FreeCAD está ativo.

-   Para usuários Linux, confira o desenvolvimento [AppImage](AppImage/pt-br.md).
-   Para compilações de desenvolvimento MacOS e Windows e código fonte de desenvolvimento, veja a página [compilações semanais](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds).
-   Para compilar o código-fonte mais recente, veja [compilação](Compiling/pt-br.md).

## Módulos e macros adicionais 

A comunidade FreeCAD fornece muitos módulos e macros adicionais. A partir de 0.17 eles podem ser facilmente instalados de dentro do FreeCAD usando o _.

---
[documentation index](../README.md) > Download/pt-br
