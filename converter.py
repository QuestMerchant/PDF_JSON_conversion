import pymupdf
import json
import os

# Select document
doc_path = 'supplements/5ed - Book of Wondrous Magic V2.pdf'
doc = pymupdf.open(doc_path)
# Font family for italics
italic_font = "Bookmania-RegularItalic"
# Default font size
font_size = 12


span_list = []
# Loop full document
def span_loop():
    for page in doc:
        text = page.get_text("dict")

        for block in text.get("blocks",[]):
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    span_list.append(span)


# Loop a single page to identify font details (Identify font family for italics, and font size of paragraphs
def find_details(page_number):
    page = doc[page_number - 1]  # Allows actual page number and ignore zero indexing
    unique_font_family = set()
    unique_font_size = set()
    text = page.get_text("dict")
    for block in text.get("blocks", []):
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                font_family = span.get("font")
                font_size = span.get("size")
                if font_family not in unique_font_family or font_size not in unique_font_size:
                    content = span.get("text")
                    unique_font_family.add(font_family)
                    unique_font_size.add(font_size)
                    print(f"Text: {content}, Font Family: {font_family}, Font Size: {font_size}")



def magic_item_extraction():
    items = []
    current_item = {}
    italic_count = 0

    span_loop()

    for span in span_list:
        # Detect Heading
        if span.get("size") > font_size:
            # Only append if item is detected (has italic subheading)
            if current_item and italic_count > 0:
                items.append(current_item)
                italic_count = 0
            current_item = {"name": span.get("text").strip(), "type": "", "rarity": "", "description": ""}

        # Detect italics
        elif span.get("font") == italic_font:
            if "name" in current_item:
                if italic_count == 0:
                    type_rarity = span.get("text").strip()
                    split = type_rarity.split(", ")
                    current_item["type"] = split[0]
                    current_item["rarity"] = split[1]
                    italic_count += 1
                elif current_item["description"] == "":
                    current_item["rarity"] = split[1] + " " + span.get("text").strip()
                else:
                    current_item["description"] += span.get("text").strip() + " "

        # Detect paragraphs
        elif span.get("size") == font_size:
            if "name" in current_item:
                if italic_count > 0:
                    current_item["description"] += span.get("text").strip() + " "
                else:
                    current_item = {}
    print(items)

find_details(14)
