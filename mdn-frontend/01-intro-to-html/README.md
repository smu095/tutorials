# Introduction to HTML

These summary notes are based on the [Introduction to HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML) module of MDN's [front-end web developer](https://developer.mozilla.org/en-US/docs/Learn/Front-end_web_developer) course.

To create a local web server (requires Python 3.6+), navigate to the folder containing content to show, and type

```python
python3 -m http.server
```

or, if you are using [Visual Studio Code](https://code.visualstudio.com/), install the [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension.

## [Getting started with HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started)

* HTML (HyperText Markup Language) is a markup language that tells the web browser how to structure the web pages you visit.
* HTML consists of a series of elements used to enclose, wrap or markup content to make it appear or act in a certain way.

![HTML element inforgraphic](https://mdn.mozillademos.org/files/9347/grumpy-cat-small.png)

* Element can be nested.

### Block vs. inline elements

* **Block-level elements** usually represent structural elements on the page (`<p>`, `<li>`, etc.).
* A block-level element starts on a new line following the element that precedes it.
* Any content following a block-level element also starts on a new line.
* **Inline elements** are contained within block-level elements, and are typically used on text (e.g. `<a>`, `<em>`, etc.).
* Inline elements *will not* cause a new line to appear in the document.

### Empty elements

* Some HTML elements do not require a closing tag, such as `<img>`.

### Attributes

* Elements can have **attributes**, which contain extra information about the element which *is not visible to the user*.
* Attributes should be wrapped in quotation marks and hyphenated (if more than one word).
* Multiple attributes are space-separated.

![Attribute infographic](https://mdn.mozillademos.org/files/9345/grumpy-cat-attribute-small.png)

### Boolean attributes

* Some attributes are written without values. These are called **boolean** attributes.

```html
<!-- using the disabled attribute prevents the end user from entering text into the input box -->
<input type="text" disabled>

<!-- text input is allowed, as it doesn't contain the disabled attribute -->
<input type="text">  
```

### Anatomy of an HTML document

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
</html>
```

1. `<DOCTYPE html>`: The doctype. Doctype is a historical artifact that needs to be included for everything else to work right. <!DOCTYPE html> is the shortest string of characters that counts as a valid doctype. That is all you need to know!
2. `<html></html>`: This element wraps all the content on the page. It is sometimes known as the **root element**.
3. `<head></head>`: This element acts as a container for everything you want to include on the HTML page, that isn't the content the page will show to viewers. This includes keywords and a page description that would appear in search results, CSS to style content, character set declarations, and more.
3. `<meta charset="utf-8">`: This element specifies the character set for your document to UTF-8. The page can now handle any textual content it might contain.
4. `<title></title>`: This sets the title of the page, which is the title that appears in the browser tab the page is loaded in. The page title is also used to describe the page when it is bookmarked.
5. `<body></body>`: This contains all the content that displays on the page, including text, images, videos, games, playable audio tracks, or whatever else.

### Entity references: Including special characters in HTML

* In HTML, the characters `<`, `>`,`"`, `'` and `&` are special characters.
* Character reference equivalents: `&lt;`, `&gt;`, `&quot;`, `&apos;` and `&amp;`.
* [List of XML and HTML character entity references](https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references) (Wikipedia).

### HTML comments

* To write an HTML comment, wrap it in the special markers `<!--` and `-->`.

## [What’s in the head? Metadata in HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML)

* The HTML head is the contents of the `<head>` element. The head's job is to contain metadata about the document.
* The `<title>` element is metadata that represents the title of the overall HTML document (not the document's content.)
* HTML has an "official" way of adding metadata to a document — the `<meta>` element, e.g. `<meta charset="utf-8">`.
* Many `<meta>` elements include `name` and `content` attributes.
  * `name` specifies the type of meta element it is; what type of information it contains.
  * `content` specifies the actual meta content.
  * Open Graph Data is a metadata protocol that Facebook invented to provide richer metadata for websites. One effect of this is that when you link to a site on facebook, the link appears along with an image and description.
  * Twitter also has its own similar proprietary metadata called Twitter Cards, which has a similar effect when the site's URL is displayed on twitter.com.

### Adding custom icons to your site

* You can add references to custom icons in your metadata, and these will be displayed in certain contexts. 
* The most commonly used of these is the **favicon** (short for "favorites icon", referring to its use in the "favorites" or "bookmarks" lists in browsers).
* A favicon can be added to your page by:
  1. Saving it in the same directory as the site's index page, saved in .ico format.
  2. Adding the following line into your HTML's `<head>` block to reference it:

  ```html
  <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
  ```

### Applying CSS and JavaScript to HTML

* Just about all websites employ **CSS** to make them look cool, and **JavaScript** to power interactive functionality
* These are most commonly applied to a web page using the `<link>` element and the `<script>` element, respectively.
* The `<link>` element should always go inside the head of your document. This takes two attributes, `rel="stylesheet"`, which indicates that it is the document's stylesheet, and `href`, which contains the path to the stylesheet file.
* The `<script>` element should also go into the head, and should include 
  * a `src` attribute containing the path to the JavaScript you want to load, and
  * `defer`, which basically instructs the browser to load the JavaScript at the same time as the page's HTML, so that you don't get errors resulting from JavaScript trying to access an HTML element that doesn't exist on the page yet.

### Setting the primary language of the document

* You can (and really should) set the language of your page. This can be done by adding the `lang` attribute to the opening HTML tag, e.g. `<html lang="en-US">`.

## [HTML text fundamentals](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals)

### The basics: Headings and Paragraphs

* In HTML, each paragraph has to be wrapped in a `<p>` element.
* Each heading has to be wrapped in a heading element. There are six heading elements — `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, and `<h6>`.
* **Best practice:** Preferably you should just use a single `<h1>` per page.
* **Best practice:** Of the six heading levels available, you should aim to use no more than three per page.

### Lists

* **Unordered lists** (`<ul>`) are used to mark up lists of items for which the order of the items doesn't matter.

```html
<ul>
  <li>milk</li>
  <li>eggs</li>
  <li>bread</li>
  <li>hummus</li>
</ul>
```

* **Ordered lists** (`<ol>`) are lists in which the order of the items does matter.

```html
<ol>
  <li>Drive to the end of the road</li>
  <li>Turn right</li>
  <li>Go straight across the first two roundabouts</li>
  <li>Turn left at the third roundabout</li>
  <li>The school is on your right, 300 meters up the road</li>
</ol>
```

* In both cases, each list item must be wrapped in a `<li>` (list item) element.
* Lists can also be **nested**.

### Emphasis and importance

* The `<em>` (emphasis) element is used to *stress* certain words.
* The `<strong>` (strong importance) element is used to **emphasize** certain words.

## [Creating hyperlinks](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks)

* Links are created using the `<a>` element with a `href` attribute (Hypertext Reference) containing the web address.
* The `title` attribute is intended to contain supplementary useful information about the link.
* Block level elements can be turned into links using `<a></a>` tags.
* The `id` attribute makes it possible to link to a specific part of an HTML document (known as a document fragment), e.g.:

```html
<h2 id="Mailing_address">Mailing address</h2>
<p>Want to write us a letter? Use our <a href="#Mailing_address">mailing address</a>.</p>
```

* **Absolute URLs** point to a location defined by its absolute location on the web, including protocol and domain name.
* **Relative URLs** point to a location that is relative to the file you are linking from.

### Link best practices

* Include keywords in your link text to effectively describe what is being linked to.
* Don't repeat the URL as part of the link text.
* Don't say "link" or "links to" in the link text.
* Keep your link label as short as possible.
* Minimize instances where multiple copies of the same text are linked to different places.
* Use relative links wherever possible.
* Leave clear signposts when linking to non-HTML resources.
* Use the download attribute when linking to a download.

### E-mails

* E-mails can be linked to using the `mailto:` URL scheme inside `href`.
* Any standard mail header fields can be added to the `mailto:` URL you provide, e.g.:

```html
<a href="mailto:example@mail.com?cc=other@mail.com&subject=The%20subject%20of%20the%20email&body=The%20body%20of%20the%20email">
  Send mail with cc, subject and body
</a>
```

* Note the use of the question mark (`?`) to separate the main URL from the field values, and ampersands (`&`) to separate each field in the `mailto:` URL.

## [Advanced text formatting](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Advanced_text_formatting)

### Descriptions lists

* **Description lists** mark up a set of items and their associated descriptions.
* Description lists use the `<dl>` wrapper. Each term is wrapped in a `<dt>` (description term) element, and each description is wrapped in a `<dd>` (description definition) element.

```html
<dl>
  <dt>soliloquy</dt>
  <dd>In drama, where a character speaks to themselves, representing their inner thoughts or feelings and in the process relaying them to the audience (but not to other characters.)</dd>
  <dt>monologue</dt>
  <dd>In drama, where a character speaks their thoughts out loud to share them with the audience and any other characters present.</dd>
  <dt>aside</dt>
  <dd>In drama, where a character shares a comment only with the audience for humorous or dramatic effect. This is usually a feeling, thought, or piece of additional background information.</dd>
</dl>
```

### Quotations

* If a section of **block level content** (be it a paragraph, multiple paragraphs, a list, etc.) is quoted from somewhere else, you should wrap it inside a `<blockquote>` element. Include a URL pointing to the source inside a `cite` attribute:

```html
<p>Here below is a blockquote...</p>
<blockquote cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
  <p>The <strong>HTML <code>&lt;blockquote&gt;</code> Element</strong> (or <em>HTML Block
  Quotation Element</em>) indicates that the enclosed text is an extended quotation.</p>
</blockquote>
```

* **Inline quotations** work in exactly the same way, except that they use the <q> element:

```html
<p>The quote element — <code>&lt;q&gt;</code> — is <q cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q">intended
for short quotations that don't require paragraph breaks.</q></p>
```

* The content of the `cite` attribute is not used by browsers and screenreaders. The `<cite>` element (styled in italic by default) can be used to explicitly reference the source.

### Abbreviations

* `<abbr>` is used to wrap an abbreviation or acronym, and provide a full expansion of the term inside a `title` attribute.

```html
<p>We use <abbr title="Hypertext Markup Language">HTML</abbr> to structure our web documents.</p>
```

### Marking up contact details

* `<address>` wraps around your contact details, e.g.:

```html
<address>
  <p>Chris Mills, Manchester, The Grim North, UK</p>
</address>
```

### Superscript and subscript

*  The `<sup>` and `<sub>` elements handle superscript and subscript, respectively.

### Representing computer code

* There are a number of elements available for marking up computer code using HTML:
  * `<code>`: For marking up generic pieces of computer code.
  * `<pre>`: For retaining whitespace (generally code blocks).
  * `<var>`: For specifically marking up variable names.
  * `<kbd>`: For marking up keyboard (and other types of) input entered into the computer.
  * `<samp>`: For marking up the output of a computer program.

* See [Represenintg computer code](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Advanced_text_formatting#Representing_computer_code) for examples.

### Marking up times and dates

* The `<time>` element is used for marking up times and dates in a machine-readable format, provided by the `datetime` attribute, e.g.:

```html
<time datetime="2016-01-20">20 January 2016</time>
```

## [Document and website structure](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure)

### Basic sections of a document

* HTML has block level elements used to define areas of your website:
  * **header** (`<head>`): Usually a big strip across the top with a big heading, logo, and perhaps a   tagline. This usually stays the same from one webpage to another.
  * **navigation bar** (`<nav>`): Links to the site's main sections, usually remains consistent from   one webpage to another.
  * **main content** (`<main>`): A big area in the center that contains most of the unique content of   a given webpage. Typically contains various content subsections represented by `<article>`,   `<section>`, and `<div>` elements.
  * **sidebar** (`<aside>`): Some peripheral info, links, quotes, ads, etc.
  * **footer** (`<footer>`): A strip across the bottom of the page that generally contains fine print,   copyright notices, or contact info.

### HTML layout elements in more detail

**Resource:** https://developer.mozilla.org/en-US/docs/Web/HTML/Element

* `<main>` is for content unique to this page. Use `<main>` only once per page, and put it directly inside `<body>`. Ideally this shouldn't be nested within other elements.
* `<article>` encloses a block of related content that makes sense on its own without the rest of the page (e.g., a single blog post).
* `<section>` is similar to `<article>`, but it is more for grouping together a single part of the page that constitutes one single piece of functionality (e.g., a mini map, or a set of article headlines and summaries). It's considered best practice to begin each section with a heading; also note that you can break `<article>`s up into different `<section>`s, or `<section>`s up into different `<article>`s, depending on the context.
* `<aside>` contains content that is not directly related to the main content but can provide additional information indirectly related to it (glossary entries, author biography, related links, etc.).
* `<header>` represents a group of introductory content. If it is a child of `<body>` it defines the global header of a webpage, but if it's a child of an `<article>` or `<section>` it defines a specific header for that section (try not to confuse this with titles and headings).
* `<nav>` contains the main navigation functionality for the page. Secondary links, etc., would not go in the navigation.
* `<footer>` represents a group of end content for a page.

### Non-semantic wrappers

* Sometimes you might want to just group a set of elements together to affect them all as a single entity with some CSS or JavaScript. 
* For cases like these, HTML provides the `<div>` (short for *division*) and `<span>` elements with a suitable `class` attribute, to provide some kind of label for them so they can be easily targeted.
* `<span>` is an **inline non-semantic element**, which you should only use if you can't think of a better semantic text element to wrap your content, or don't want to add any specific meaning.
* `<div>` is a **block level non-semantic element**, which you should only use if you can't think of a better semantic block element to use, or don't want to add any specific meaning.

> **Warning:** Divs are so convenient to use that it's easy to use them too much. As they carry no semantic value, they just clutter your HTML code. Take care to use them only when there is no better semantic solution and try to reduce their usage to the minimum otherwise you'll have a hard time updating and maintaining your documents.

### Line breaks and horizontal rules

* `<br>` creates a line break in a paragraph.
* `<hr>` elements create a horizontal rule in the document that denotes a thematic change in the text.

## [Debugging HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Debugging_HTML)

See [the official docs](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Debugging_HTML) for more info (using developer tools to debug, etc.).