# <ins>PDF to JSON converter</ins>

#### <ins>Description</ins>
I will use this code to automate the process of digitizing my D&D content. <br>
I changed my code to process one document at a time as each document has different styles that I need to input. <br>
Currently, I only have automation to detect the magic items and convert them into a JSON format for my personal project.

#### <ins>Guide</ins>
To use the code, you need to change the doc_path to the document's path, including the name and extension. <br>

#### <ins>Magic Items</ins>
To identify the items, you need to separate the headings and properties (Usually italicized, sometimes bold)<br>
I have a function `find_details(page)`. Select a page that has items for easy identification. <br>
This is not zero-indexed, so you can input the exact page, for example, find_details(11) to get results for page 11.<br>
This will print out lines on the page with their font family and size. It will only print lines with unique properties.<br>

<ins>EXAMPLE</ins>
```python
doc = pymupdf.open(doc_path)
find_details(11)
```
<ins>Result</ins><br>
>Font Family: Wingdings-Regular, Font Size: 14.039999961853027, Text:  <br>
Font Family: ModestoCondensed-Bold, Font Size: 14.039999961853027, Text:  <br>
Font Family: ModestoCondensed-Bold, Font Size: 18.0, Text: 15<br>
Font Family: Calibri, Font Size: 9.960000038146973, Text:  <br>
Font Family: ModestoCondensed-Light, Font Size: 21.959999084472656, Text: Baba Yaga’s Iron Kettle <br>
Font Family: Bookmania-RegularItalic, Font Size: 12.0, Text: Wondrous item, artifact (requires attunement)<br> 
Font Family: Bookmania-Regular, Font Size: 12.0, Text: Baba Yaga is an ancient sorceress of unknown origin, <br>
Font Family: Bookmania-BoldItalic, Font Size: 12.0, Text: Various properties.<br>
Font Family: ArialMT, Font Size: 12.0, Text:<br>

> [!Note]
> Changed the format to show text first.

In this example, the font would be set to 12 and the italicized font set to Bookmania-RegularItalic<br>
(The BoldItalic is within the description of the item and should not be separated)

With the font set, you can now run `magic_item_extraction()`.
This will save every item to a JSON file with the format: <br>
```
{
  "name": "Example Magic Item",
  "type": "Ring",
  "rarity": "Rare",
  "description": "This is a sample magic item.",
  "attunement": {
    "required": true,
    "conditions": {
      "classes": ["Wizard", "Sorcerer"]
    }
  }
}
```

#### <ins>Work In Progress</ins>
- Identifying weapons
- Extracting Spells
- Extracting Backgrounds
- Extracting Races
- Extracting Sub-Classes
