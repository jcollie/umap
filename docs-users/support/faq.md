# Frequently Asked Questions (FAQ)

## Which syntax is allowed in description fields? {: #text-formatting }

* `*single star for italic*` → *single star for italic*
* `**double star for bold**` → **double star for bold**
* `# one hash for main heading` ⤵ <h1>one hash for main heading</h1>
* `## two hashes for second heading` ⤵ <h2>two hashes for second heading</h2>
* `### three hashes for third heading` ⤵ <h3>three hashes for third heading</h3>
* `Simple link: [[http://example.com]]` → Simple link: [http://example.com](http://example.com)
* `Link with text: [[http://example.com|text of the link]]` → Link with text: [text of the link](http://example.com)
* `--- for a horizontal rule` ⤵ <hr>

## What are the available keyboard shortcuts? {: #keyboard-shortcuts}

With macOS, replace `Ctrl` by `Cmd`.

### Globals

* `Ctrl+F` → open search panel
* `Ctrl+E` → switch to edit mode
* `Escape` → close open panel or dialog
* `Shift+drag` on the map → zoom to this map extent
* `Shift+click` on the zoom buttons → zoom in/out by 3 levels

### In edit mode

* `Ctrl+E` → back to preview mode
* `Ctrl+S` → save map
* `Ctrl+Z` → undo all changes until last save
* `Ctrl+M` → add a new marker
* `Ctrl+P` → start a new polygon
* `Ctrl+L` → start a new line
* `Ctrl+I` → open importer panel
* `Ctrl+O` → open importer panel and file browser
* `Ctrl++` → zoom in
* `Ctrl+-` → zoom out
* `Shift+click` on a feature → edit this feature
* `Ctrl+Shift+click` on a feature → edit this feature layer

## Which syntax is allowed in conditional rules? {: #conditional-rules }

* `mycolumn=odd` → will match features whose column `mycolumn` equal `odd`
* `mycolumn!=odd` → will match features whose column `mycolumn` is missing or different from `odd`
* `mycolumn>12` → will match features whose column `mycolumn` is greater than `12` (as number)
* `mycolumn<12.34` → will match features whose column `mycolumn` is lower than `12.34` (as number)

When the condition match, the associated style will be applied to the corresponding feature.
