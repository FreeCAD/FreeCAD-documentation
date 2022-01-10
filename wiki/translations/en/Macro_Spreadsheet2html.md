# Macro Spreadsheet2html/en
{{Macro
|Name=Spreadsheet2html
|Description=Exports a fc spreadsheet as html. Install through addon manager broken, please see macro wiki page for instruction.
|Author=heda
|Version=0.1
|Date=2021-08-09
|FCVersion=any with spreadsheet
}}

## Description

Exports the content of a FreeCAD SpreadSheet as styled html, can be used to import to LibreOffice Writer or Calc. Further info in the docstring of the macro.

## Usage

Select a SpreadSheet and run macro.

## Install

Visible in Addon manager, but install is broken. For now only option is to manually install, but you have to take the code from \"view source\" from this wiki. The full code is there, but it does not render on the wiki.

## Link

Forum: No dedicated thread at time of writing.

## Code

**Macro\_Spreadsheet2html.FCMacro**

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    # ***************************************************************************
    # *   Copyright (c) 2021 heda <@fc-forum>                                   *
    # *                                                                         *
    # *   This file is part of the FreeCAD CAx development system.              *
    # *                                                                         *
    # *   This program is free software; you can redistribute it and/or modify  *
    # *   it under the terms of the GNU Lesser General Public License (LGPL)    *
    # *   as published by the Free Software Foundation; either version 2 of     *
    # *   the License, or (at your option) any later version.                   *
    # *   for detail see the LICENCE text file.                                 *
    # *                                                                         *
    # *   This program is distributed in the hope that it will be useful,       *
    # *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
    # *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
    # *   GNU Library General Public License for more details.                  *
    # *                                                                         *
    # *   You should have received a copy of the GNU Library General Public     *
    # *   License along with this program; if not, write to the Free Software   *
    # *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
    # *   USA                                                                   *
    # *                                                                         *
    # ***************************************************************************


    __Name__ = 'Spreadsheet2html'
    __Comment__ = 'Exports a fc spreadsheet as html. NOTE: wiki caps code so follow instruction on wiki for install.'
    __Author__ = 'heda @ fc-forum'
    __Version__ = '0.1'
    __Date__ = '2021-08-09'
    __License__ = 'LGPL-2.0-or-later'
    __Web__ = ''
    __Wiki__ = 'Associated wiki page'
    __Icon__ = ''
    __Help__ = 'Select a spreadsheet and launch macro.'
    __Status__ = 'Stable'
    __Requires__ = 'tested on FreeCAD v0.19'
    __Communication__ = 'forum'
    __Files__ = ''



    __doc__ = """
    Exports a selected spreadsheet as html, can be opened directly in LO-Writer.
    File is saved in user Documents with similar name as the fc-file.
    All cells with content are included in the exported range.

    To use with LO-Writer:
      - open the html-file directly with LO-Writer

    To use with LO-Calc:
      - create new LO-Calc doc
      - menu: "Sheet/Link to External Data" and select the generated html file

    There are 5 options for the generated html:
      - values without any formatting or comments
      - values with formatting & comments (default)
      - formulas with formatting & comments
      - extra table for comments, i.e. units, formulas & alias (default without)
      - with/without table borders (default with)
      
    The options are set in the macrofile, not via gui.

    Imports to Calc does not respect column width & row heigth,
    html in browser and Writer does...
    Same goes for merged cells.
    Neither Writer nor Calc parses the comments, hence the option for extra table.

    Alias:
      The extra table helps in recreating alias in Calc, to redefine the
      name within Calc (look in LO-Calc docs if you want to know how).

      Obviously the use of alias is only working for an alias that
      has references that Calc understands, so "=A1+B2" works,
      while "=Box.Length" does not.
      
      For the cases where the evaluation should work, one still has to
      select the cell with the formula and click the "equal sign" in
      the formula bar of Calc user interface.

    Comments contains the following as per availability:
      - unit strings when defined on cells in fc
      - name of alias when defined on cells in fc
      - formulas if the option to evaluate expressions to values is True (default)
      - evaluated value if the option to keep formulas is True

    For the option "paste values" it is just the evaluated values of the cells.
    The option does not pass along comments.
    """

    filelocation = 'Documents'
    options = dict(PasteSpecial_values=False,
                   PasteSpecial_values_and_format=True,
                   PasteSpecial_formulas_and_format=False,
                   CommentTable=False,
                   TableBorder=True)

    ColumnWidthFactor = 100/85 # FC has 100 as std width, 85 is reasonable for LO
    RowHeightFactor = 30/17

    import FreeCADGui as Gui

    import re
    import html as htmllib
    import xml.etree.ElementTree as ET
    from string import ascii_uppercase
    from itertools import product
    from pathlib import Path
    from datetime import datetime as dt


    #spreadsheet = App.ActiveDocument.Spreadsheet

    spreadsheet, = Gui.Selection.getSelection()
    sp_name = spreadsheet.FullName.replace('#', '-')
    sp_content = spreadsheet.cells.Content
    root = ET.fromstring(sp_content)

    cells = dict()
    for el in root:
        if not 'Cell' in el.tag: continue
        address = el.attrib.pop('address')
        cells[address] = el.attrib

    #import pprint
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(cells)

    ### find range of sheet
    ##  (would be nice with a simple sp.getRange())
    char = re.compile(r'\d+')
    num = re.compile(r'\D+')

    def split_address(address):
        C, _, _, R = char.split(address) + num.split(address)
        return C, int(R)

    tmp = dict(split_address(address) for address in cells)
    Rmax = max(tmp.values())
    ## need to separate one and two chars comparison
    if any(map(lambda s: len(s) == 2, tmp)):
        Cmax = max(filter(lambda s: len(s) == 2, tmp))
    else:
        Cmax = max(tmp)

    ### prepare column and row iterable for actual range
    column_iter = list(ascii_uppercase)
    column_extension = 10 # assume that col-span on last col is limited to 9...
    cart = product(ascii_uppercase, repeat=2)
    if Cmax in column_iter:
        cut_idx = column_iter.index(Cmax) + 1
        length = range(column_extension)
        column_iter += [''.join(c) for _, c in zip(length, cart)]

        column_extension = column_iter[cut_idx:cut_idx + column_extension]
        column_iter = column_iter[:cut_idx]
    else:
        a, b = (ord(c)-65 for c in Cmax)
        length = range(a * len(ascii_uppercase) + b + 1 + column_extension)
        column_iter += [''.join(c) for _, c in zip(length, cart)]
                    
        column_extension = column_iter[-column_extension:]
        column_iter = column_iter[:-len(column_extension)]

    ## extend range where needed
    hitcells = (cell for cell in cells if str(Rmax) in cell)
    extend = max(cells.get(address).get('rowSpan', '1') for cell in hitcells)
    Rmax += int(extend) - 1

    extend = 1
    for address in (cell for cell in cells if str(Cmax) in cell):
        v = int(cells.get(address).get('colSpan', 1))
        extend = v if v > extend else extend
    column_iter += column_extension[:int(extend) - 1]
    column_iter = tuple(column_iter)
    Cmax = column_iter[-1]


    ### generating html
    # doctype workaround, tripping parser if there
    doctype = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"/>'

    template = """
    <html>
    <head>
        
        <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
        <title>FreeCAD</title>
        <meta name="template" content="LibreOffice (Calc) 6.4"/>
        <meta name="generator" content="FreeCAD macro - SpreadSheet2LibreOffice"/>
        <meta name="created" content=""/>
        
        <style type="text/css">
            a.comment-indicator:hover + comment { background:#ffd; position:absolute; display:block; border:1px solid black; padding:0.5em;  } 
            a.comment-indicator { background:red; display:inline-block; border:1px solid black; width:0.5em; height:0.5em;  } 
            comment { display:none;  } 
        </style>
        
    </head>

    <body>
    <table cellspacing="0" cellpadding="3" border="1">
    </table>
    </body>

    </html>
    """

    doc = ET.fromstring(template)

    title = doc.find('./head/title')
    title.text += ' ' + sp_name
    created = doc.find("./head/meta[@name='created']")
    created.set('content', dt.now().strftime('%Y-%m-%d %H:%M:%S'))

    table = doc.find('./body/table')
    table.set('border', str(int(options.get('TableBorder'))))
        
    for width in (spreadsheet.getColumnWidth(c) for c in column_iter):
        ET.SubElement(table, 'colgroup',
                      dict(width='{:.0f}'.format(width/ColumnWidthFactor)))

    align_table = dict(left=('align', 'left'), center=('align', 'center'),
                       right=('align', 'right'),
                       top=('valign', 'top'), vcenter=('valign', 'middle'),
                       bottom=('valign', 'bottom'))
    style_table = dict(bold='b', italic='i', underline='u')

    skip_list = list()
    for r in range(1, Rmax+1):
        rowheight = spreadsheet.getRowHeight(str(r)) / RowHeightFactor
        tr = ET.Element('tr', dict(height='{:.0f}'.format(rowheight)))
        for c in column_iter:
            address = f'{c}{r}'
            cell = cells.get(address, dict())
            new_attrib = dict()
            td = ET.Element('td')
            td.text = cell.get('content')
            # avoid overflow, implies look ahead
            colspan = int(cell.get('colSpan', 0))
            rowspan = int(cell.get('rowSpan', 0))
            if colspan > 0:
                idx = column_iter.index(c) + 1
                gen = (f'{ci}{r}' for ci in column_iter[idx:idx + colspan - 1])
                skip_list.extend(gen)
                new_attrib.update(dict(colspan=str(colspan)))
            if rowspan > 0:
                gen = (f'{c}{ri}' for ri in range(r + 1, r + rowspan))
                skip_list.extend(gen)
                new_attrib.update(dict(rowspan=str(rowspan)))
                
            if address in skip_list:
                continue
            
            tr.append(td)
            
            # styling and attributes
            subel, comment = list(), list()
            for k in sorted(cell):
                v = cell.get(k)
                if k == 'alias':
                    comment.append('alias: {}'.format(v))
                elif k == 'alignment':
                    for which in v.split('|'):
                        kva = align_table.get(which)
                        if kva:
                            new_attrib.update(dict((kva,)))
                elif k == 'backgroundColor':
                    new_attrib.update(dict(bgcolor=v[:-2]))
                elif k == 'displayUnit':
                    comment.append('unit: {}'.format(v))
                elif k == 'foregroundColor': # will always be first
                    font = ET.Element('font', dict(color=v[:-2]))
                    subel.append(font)
                elif k == 'style':
                    for which in v.split(chr(124)):
                        sty = ET.Element(style_table.get(which))
                        subel.insert(0, sty)
            
            # formula options
            if isinstance(td.text, str) and td.text.startswith('='):
                if options.get('PasteSpecial_values'):
                    td.text = str(spreadsheet.get(address)) # returns casted type
                elif options.get('PasteSpecial_values_and_format'):
                    formula = td.text
                    td.text = str(spreadsheet.get(address))
                    comment.append('formula: {}'.format(formula))
                elif options.get('PasteSpecial_formulas_and_format'):
                    value = spreadsheet.get(address)
                    comment.append('value: {}'.format(value))

            if options.get('PasteSpecial_values'):
                subel, comment = list(), list()
                for k in tuple(new_attrib):
                    if not 'span' in k:
                        _ = new_attrib.pop(k)

            # sanitize for html
            if td.text:
                td.text = htmllib.escape(td.text)

            if comment:
                ET.SubElement(td, 'a', {'class': 'comment-indicator'})
                popup = ET.Element('comment')
                popup.text = '  |  '.join((htmllib.escape(cm) for cm in comment))
                td.append(popup)
                            
            td.attrib = new_attrib

            if subel:
                parent = td
                for child in subel:
                    child.text = parent.text
                    parent.text = None
                    parent.append(child)
                    parent = child

        table.append(tr)

    ### extra table
    if options.get('CommentTable'):

        template_extra = """
        <table cellspacing="0" cellpadding="3" border="1">
        <tr>
            <td><b>adress</b></td>
            <td><b>trace</b></td>
            <td><b>evaluated</b></td>
            <td><b>unit</b></td>
            <td><b>formula</b></td>
            <td><b>alias</b></td>
        </tr>
        </table>
        """
        table_extra = ET.fromstring(template_extra)
        
        table_extra.set('border', str(int(options.get('TableBorder'))))
        
        body = doc.find('./body')
        body.extend((ET.Element('p'), table_extra))
        
        for address, attrib in cells.items():
            row = [address, f'={address}', None,
                   attrib.get('displayUnit'), None, attrib.get('alias')]

            content = attrib.get('content')
            if not content:
                continue

            row[2] = content
            if content.startswith('='):
                value = spreadsheet.get(address)
                row[2] = value
                row[4] = chr(39) + content
        
            tr = ET.Element('tr')
            for r in row:
                td = ET.Element('td')
                td.text = r
                tr.append(td)

            table_extra.append(tr)


    ### save file on disk
    filehandle = Path.home() / filelocation / '{}.html'.format(sp_name)
    htmldoc = ET.ElementTree(doc)
    htmldoc.write(filehandle, encoding='utf-8',
                  xml_declaration=True, method='html')

    filehandle.write_text('\n'.join((doctype, filehandle.read_text())))

    print('Exported spreadsheet as html.')

    # end

## Version

v0.1 2021-08-09 : first release

---
[documentation index](../README.md) > Macro Spreadsheet2html/en
