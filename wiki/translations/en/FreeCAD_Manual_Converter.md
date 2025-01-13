# FreeCAD Manual Converter/en
{{Macro
|Name=FreeCAD Manual Converter
|Description=Python script that automatically generates PDF and EPUB versions of the FreeCAD manual.
|Version = 0.1
|Author=Adrianos
|Date=2024-12-16
|FCVersion=All
}}

## Introduction

The FreeCAD Manual Converter is a Python script that automatically generates PDF and EPUB versions of the FreeCAD manual from the FreeCAD Wiki. It creates a complete, properly formatted offline manual that includes all chapters, images, and formatting from the online manual.

### Background

The [FreeCAD Manual](Manual_Introduction.md) is a living document that continuously evolves thanks to the contributions of community members. While this makes it an excellent up-to-date resource, there are times when users need offline access to the manual or prefer to read it on e-readers and tablets. This script bridges that gap by allowing users to:

-   Generate an up-to-date offline copy of the manual at any time
-   Create both PDF and EPUB formats for different reading preferences
-   Include all the latest community contributions and updates
-   Maintain proper formatting and image quality
-   Have a complete reference even without internet access

## Dependencies

### Windows

1.  Install Python 3.x.
2.  Install GTK3 runtime
3.  Open Command Prompt and install Python packages:


{{MacroCode|code=
pip install requests weasyprint beautifulsoup4 PyPDF2 Pillow cairosvg ebooklib
}}

### Linux (Ubuntu/Debian) 

Install all necessary dependencies as:


```python
sudo apt-get update
sudo apt-get install -y python3-pip python3-dev python3-cairo python3-gi-cairo
sudo apt-get install -y libcairo2-dev libpango1.0-dev libgdk-pixbuf2.0-dev libffi-dev shared-mime-info
```

and


```python
pip3 install requests weasyprint beautifulsoup4 PyPDF2 Pillow cairosvg ebooklib
```

## Usage

To use the script just download it and run it. The script will create two files in your current directory:

-   **FreeCAD_User_Manual.pdf**: Complete PDF version of the manual
-   **FreeCAD_User_Manual.epub**: EPUB version suitable for e-readers

## Script


{{MacroCode|code=
import requests
from weasyprint import HTML
import os
from bs4 import BeautifulSoup
import re
from PyPDF2 import PdfMerger
from PIL import Image
from io import BytesIO
import base64
import cairosvg
import ebooklib
from ebooklib import epub
import uuid
from datetime import datetime


class FreeCADManualConverter:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.toc_entries = []  # Store chapter titles, subchapters, and hierarchy
        self.chapters_html = []  # Store HTML content for EPUB creation
        self.image_cache = {}  # Cache for deduplicating images

    def optimize_image(self, img_url, max_width=800):
        """Download and optimize a raster image."""
        try:
            response = self.session.get(img_url, stream=True)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            if img.width > max_width:
                img = img.resize((max_width, int(img.height * max_width / img.width)), Image.Resampling.LANCZOS)
            buffer = BytesIO()
            img.save(buffer, format="PNG", optimize=True)
            buffer.seek(0)
            return buffer.read()
        except Exception as e:
            print(f"Error optimizing image {img_url}: {e}")
            return None

    def svg_to_png(self, svg_url):
        """Convert SVG to PNG."""
        try:
            response = self.session.get(svg_url)
            response.raise_for_status()
            return cairosvg.svg2png(bytestring=response.content, output_width=16, output_height=16)
        except Exception as e:
            print(f"Error converting SVG {svg_url} to PNG: {e}")
            return None
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.toc_entries = []  # Store chapter titles, subchapters, and hierarchy
        self.chapters_html = []  # Store HTML content for EPUB creation

    def extract_manual_links(self, base_url="https://wiki.freecad.org/Manual"):
        """Extract all manual links and subchapters from the main Manual page."""
        print(f"Fetching manual links from {base_url}...")
        html_content = self.fetch_page(base_url)
        if not html_content:
            return []

        soup = BeautifulSoup(html_content, 'html.parser')
        links = {}
        seen = set()

        # Define unwanted languages
        excluded_languages = ['fr', 'de', 'es', 'hr', 'it', 'ko', 'pl', 'pt', 'ro', 'ru', 'zh']

        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if any(f"/{lang}" in href for lang in excluded_languages):
                continue

            if href.startswith('/Manual:'):
                full_url = f"https://wiki.freecad.org{href}"
                base_chapter = full_url.split('#')[0]
                subchapter = full_url.split('#')[1] if '#' in full_url else None

                if base_chapter not in seen:
                    links[base_chapter] = []
                    seen.add(base_chapter)

                if subchapter:
                    links[base_chapter].append(subchapter)

        print(f"Found {len(links)} unique manual links with subchapters.")
        return links

    def fetch_page(self, url):
        """Fetch the HTML content of a given URL."""
        if url.startswith('/'):
            url = f"https://wiki.freecad.org{url}"

        try:
            response = self.session.get(url)
            if response.status_code != 200:
                print(f"Failed to fetch {url}. HTTP status code: {response.status_code}")
                return None
            return response.text
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def extract_main_content(self, html_content, base_url, chapter_title, chapter_id, subchapters):
        """Extract content within the 'mw-parser-output' div, fix links, and process image paths."""
        soup = BeautifulSoup(html_content, 'html.parser')

        # Remove unwanted elements
        for class_name in ['mw-pt-languages noprint', 'docnav', 'NavFrame', 'manualtoc']:
            for element in soup.find_all(class_=class_name):
                element.decompose()

        main_content = soup.find('div', class_='mw-parser-output')
        if not main_content:
            print("Main content ('mw-parser-output') not found.")
            return None

        # Add chapter title as heading at the top if not present
        if not main_content.find('h1', id=chapter_id):
            heading_tag = soup.new_tag('h1', id=chapter_id)
            heading_tag.string = chapter_title
            main_content.insert(0, heading_tag)

        # Process images and store them for EPUB
        for img in main_content.find_all('img'):
            src = img.get('src')
            if src and src.startswith('/'):
                img_url = f"{base_url}{src}"
                img_filename = os.path.basename(src)

                if src.endswith('.svg'):
                    # Convert SVG to PNG
                    png_data = self.svg_to_png(img_url)
                    if png_data:
                        img_data = png_data
                        img_filename = f"{img_filename[:-4]}.png"
                else:
                    # Optimize raster image
                    img_data = self.optimize_image(img_url)

                if img_data:
                    # For PDF
                    img['src'] = f"data:image/png;base64,{base64.b64encode(img_data).decode('utf-8')}"
                    # For EPUB - store reference
                    img['epub_src'] = img_filename
                    img['epub_data'] = img_data

        # Fix links
        for link in main_content.find_all('a'):
            href = link.get('href')
            if href and href.startswith('/'):
                link['href'] = f"{base_url}{href}"

        # Store the HTML content for EPUB creation
        self.chapters_html.append({
            'title': chapter_title,
            'id': chapter_id,
            'content': main_content,
            'number': len(self.chapters_html) + 1
        })

        return str(main_content)

    def convert_to_pdf(self, url, chapter_number, chapter_id, subchapters, output_dir='pdfs'):
        print(f"Processing {url}...")
        os.makedirs(output_dir, exist_ok=True)

        html_content = self.fetch_page(url)
        if not html_content:
            return None

        soup = BeautifulSoup(html_content, 'html.parser')
        chapter_title = soup.title.string.split(" - ")[0] if soup.title else "Chapter"
        chapter_title = chapter_title.replace("Manual:", "").strip()

        base_url = "https://wiki.freecad.org"
        main_content = self.extract_main_content(html_content, base_url, chapter_title, chapter_id, subchapters)
        if not main_content:
            return None

 
        output_file = os.path.join(output_dir, f"{chapter_id}.pdf")

        self.toc_entries.append((chapter_number, chapter_title, chapter_id, subchapters))

        styled_content = f"""
        <html>
        <head>
        <style>
        body {{
            margin: 20px;
            font-family: Arial, sans-serif;
        }}

       h1 {{
           text-align: center;
           font-size: 24px;
           margin-bottom: 10px;
       }}
       h2 {{
           font-size: 18px;
           margin-top: 10px;
       }}
       img {{
           max-width: 100%;
           height: auto;
       }}
       code, pre {{
           font-family: Consolas, "Courier New", monospace;
           font-size: 14px;
           background-color: #f4f4f4;
           padding: 10px;
           display: block;
           white-space: pre-wrap;
           word-wrap: break-word;
           overflow-x: auto;
           border: 1px solid #ddd;
           border-radius: 5px;
       }}
       .mw-highlight {{
           padding: 10px;
           margin: 10px 0;
           border: 1px solid #ddd;
           background-color: #f9f9f9;
           border-radius: 5px;
       }}
       .wikitable {{
           width: 100%;
           border-collapse: collapse;
           margin: 20px 0;
           font-size: 14px;
           text-align: left;
           page-break-inside: avoid;
       }}
       .wikitable th, .wikitable td {{
           border: 1px solid #ddd;
           padding: 10px;
           page-break-inside: avoid;
       }}
       .wikitable tr {{
           page-break-inside: avoid;
       }}
       .wikitable tr:nth-child(even) {{
           background-color: #f9f9f9;
       }}
       .wikitable tr:hover {{
           background-color: #f1f1f1;
       }}
       .wikitable th {{
           background-color: #f2f2f2;
           text-align: center;
           font-weight: bold;
       }}
       


</style>


</head>


<body>

       {main_content}
       


</body>


</html>

       """

       try:
           HTML(string=styled_content).write_pdf(output_file)
           print(f"Created {output_file}")
           return output_file
       except Exception as e:
           print(f"Error creating PDF for {url}: {e}")
           return None

   def generate_toc(self, output_file='pdfs/Table_of_Contents.pdf'):
       """Generate a Table of Contents PDF with indented subchapters."""
       print("Generating Table of Contents...")
       toc_html = """
       


<html>


<head>


<style>

       body {{
           margin: 20px;
           font-family: Arial, sans-serif;
       }}
       h1 {{
           text-align: center;
           font-size: 28px;
       }}
       ul {{
           list-style: none;
           padding: 0;
       }}
       li {{
           margin: 5px 0;
       }}
       .chapter {{
           font-weight: bold;
           font-size: 16px;
       }}
       .subchapter {{
           font-size: 14px;
           margin-left: 20px;
       }}
       a {{
           color: blue;
           text-decoration: none;
       }}
       


</style>


</head>


<body>


<h1>

Table of Contents


</h1>


\"\"\"

       for chapter_number, title, chapter_id, subchapters in self.toc_entries:
           toc_html += f'


<li class="chapter">

{chapter_number}. {title}


</li>

\'

           for i, sub in enumerate(subchapters, start=1):
               toc_html += f'


<li class="subchapter">

{chapter_number}.{i} {sub.replace(\"\_\", \" \").capitalize()}


</li>

\'

       toc_html += "


</ul>


</body>


</html>

\"

       try:
           HTML(string=toc_html).write_pdf(output_file)
           print(f"Created {output_file}")
       except Exception as e:
           print(f"Error creating Table of Contents PDF: {e}")

   def merge_pdfs(self, pdf_files, output_file):
       print(f"Merging PDFs into {output_file}...")
       merger = PdfMerger()
       for pdf in pdf_files:
           merger.append(pdf)
       merger.write(output_file)
       merger.close()
       print(f"Successfully created {output_file}")

   def create_epub(self, output_file='FreeCAD_User_Manual.epub'):
       """Create an EPUB version of the manual."""
       print(f"Creating EPUB: {output_file}")

       # Initialize EPUB book
       book = epub.EpubBook()

       # Set metadata
       book.set_identifier(str(uuid.uuid4()))
       book.set_title('FreeCAD User Manual')
       book.set_language('en')
       book.add_author('FreeCAD Community')
       book.set_cover("cover.jpg", self.generate_cover())

       # Add CSS
       style = '''
           body { margin: 20px; font-family: Arial, sans-serif; }
           h1 { text-align: center; font-size: 2em; margin-bottom: 1em; }
           h2 { font-size: 1.5em; margin-top: 1em; }
           img { max-width: 100%; height: auto; }
           code, pre {
               font-family: monospace;
               background-color: #f4f4f4;
               padding: 0.5em;
               display: block;
               white-space: pre-wrap;
               border: 1px solid #ddd;
               border-radius: 5px;
           }
           table {
               width: 100%;
               border-collapse: collapse;
               margin: 1em 0;
           }
           th, td {
               border: 1px solid #ddd;
               padding: 0.5em;
           }
       '''
       nav_css = epub.EpubItem(
           uid="style_nav",
           file_name="style/nav.css",
           media_type="text/css",
           content=style
       )
       book.add_item(nav_css)

       # Create chapters
       chapters = []
       for chapter_data in self.chapters_html:
           # Create chapter
           chapter = epub.EpubHtml(
               title=chapter_data['title'],
               file_name=f'chapter_{chapter_data["number"]}.xhtml',
               lang='en'
           )

           # Process content for EPUB
           content = chapter_data['content']

           # Handle images
           for img in content.find_all('img'):
               if 'epub_data' in img.attrs and 'epub_src' in img.attrs:
                   # Generate a content hash for the image data
                   import hashlib
                   img_hash = hashlib.md5(img['epub_data']).hexdigest()

                   # Check if we've seen this image before
                   if img_hash not in self.image_cache:
                       # This is a new image
                       image_filename = f'{img_hash}_{img["epub_src"]}'
                       self.image_cache[img_hash] = image_filename

                       # Add image to EPUB
                       image_item = epub.EpubItem(
                           uid=f'image_{img_hash}',
                           file_name=f'images/{image_filename}',
                           media_type='image/png',
                           content=img['epub_data']
                       )
                       book.add_item(image_item)

                   # Update image source to use cached filename
                   img['src'] = f'images/{self.image_cache[img_hash]}'
                   # Remove EPUB-specific attributes
                   del img['epub_data']
                   del img['epub_src']

           # Set chapter content
           chapter.content = str(content)
           chapter.add_item(nav_css)

           # Add chapter
           book.add_item(chapter)
           chapters.append(chapter)

       # Create table of contents
       book.toc = [(epub.Section('Table of Contents'), chapters)]

       # Add navigation files
       book.add_item(epub.EpubNcx())
       book.add_item(epub.EpubNav())

       # Define reading order
       book.spine = ['nav'] + chapters

       # Write EPUB file
       epub.write_epub(output_file, book, {})
       print(f"Successfully created {output_file}")

   def generate_cover(self):
       """Generate a simple cover image for the EPUB."""
       from PIL import Image, ImageDraw, ImageFont

       # Create a new image with a white background
       cover = Image.new('RGB', (1600, 2400), 'white')
       draw = ImageDraw.Draw(cover)

       # Add title text
       try:
           font = ImageFont.truetype("Arial", 120)
       except:
           font = ImageFont.load_default()

       title = "FreeCAD\nUser Manual"
       draw.text((800, 1000), title, font=font, fill='black', anchor="mm", align="center")

       # Add date
       date_str = datetime.now().strftime("%Y-%m-%d")
       draw.text((800, 1300), date_str, font=font, fill='gray', anchor="mm")

       # Convert to bytes
       img_byte_arr = BytesIO()
       cover.save(img_byte_arr, format='JPEG')
       img_byte_arr.seek(0)

       return img_byte_arr.getvalue()

   def batch_convert(self, links, output_dir='pdfs', merged_pdf='FreeCAD_User_Manual.pdf', create_epub=True):
       """Convert manual to both PDF and EPUB formats."""
       # First create PDF as before
       pdf_files = []
       for chapter_number, (chapter_url, subchapters) in enumerate(links.items(), start=1):
           chapter_id = re.sub(r'[<>:"/\\?*]', '_', chapter_url.split('/')[-1])
           pdf_file = self.convert_to_pdf(chapter_url, chapter_number, chapter_id, subchapters, output_dir)
           if pdf_file:
               pdf_files.append(pdf_file)

       # Generate and merge Table of Contents
       toc_file = os.path.join(output_dir, "Table_of_Contents.pdf")
       self.generate_toc(toc_file)
       pdf_files.insert(0, toc_file)

       if pdf_files:
           self.merge_pdfs(pdf_files, merged_pdf)

       # Create EPUB version if requested
       if create_epub:
           self.create_epub('FreeCAD_User_Manual.epub')

def main():

   converter = FreeCADManualConverter()
   manual_links = converter.extract_manual_links()
   converter.batch_convert(manual_links, output_dir='pdfs',
                         merged_pdf='FreeCAD_User_Manual.pdf',
                         create_epub=True)

if \_\_name\_\_ == \"\_\_main\_\_\":

   main()

}}



---
⏵ [documentation index](../README.md) > FreeCAD Manual Converter/en
