# Introduction to HTML

This tutorial is based on the [Introduction to HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML) module of MDN's [front-end web developer](https://developer.mozilla.org/en-US/docs/Learn/Front-end_web_developer) course.

To create a local web server, navigate to the folder containing content to show, and type

```python
python3 -m http.server
```

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

## What’s in the head? Metadata in HTML

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

## HTML text fundamentals

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

* The <em> (emphasis) element is used to *stress* certain words.
* The <strong> (strong importance) element is used to **emphasize** certain words.

## Creating hyperlinks

TODO.