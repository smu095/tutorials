# [Learn to style HTML using CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)

These summary notes are based on the [Learn to style HTML using CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS) module of MDN's [front-end web developer](https://developer.mozilla.org/en-US/docs/Learn/Front-end_web_developer) course.

## [What is CSS?](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS)

- CSS is a language for specifying how documents are presented to users — how they are styled, laid out, etc.
- CSS is a rule-based language — you define rules specifying groups of styles that should be applied to particular elements or groups of elements on your web page.
- As there are so many things that you could style using CSS, the language is broken down into _modules_.
- On each property page on MDN you can see the status of the property you are interested in, so you can tell if you will be able to use it on a website.

### CSS syntax

```css
h1 {
  color: red;
  font-size: 5em;
}
```

- The rule opens with a selector . This selects the HTML element that we are going to style. In this case we are styling level one headings (`<h1>`).
- The curly braces `{ }` contain one or more declarations, which take the form of property and value pairs.

### General CSS syntax

```css
style-rule ::=
    selectors-list {
      properties-list
    }
```

where

```css
selectors-list ::=
    selector[:pseudo-class] [::pseudo-element]
    [, selectors-list]

properties-list ::=
    [property : value] [; properties-list]
```

## [Getting started with CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/Getting_started#Adding_CSS_to_our_document)

### Adding CSS to our document

- The most usual and useful way applying a CSS file to an HTML document is by linking CSS from the head of your document:

```html
<link rel="stylesheet" href="styles.css" />
```

- The `<link>` element tells the browser that we have a stylesheet, using the `rel` attribute, and the location of that stylesheet as the value of the `href` attribute.

### Styling HTML elements

- An _element selector_ is a selector that directly matches an HTML element name. You can target multiple selectors at once, by separating the selectors with a comma.

- The default behavior of elements can be changed by simply choosing the HTML element that you want to change, and using a CSS rule to change the way it looks, e.g.:

```css
li {
  list-style-type: square;
}
```

### Adding a class

- So far we have styled elements based on their HTML element names. This works as long as you want all of the elements of that type in your document to look the same.
- Most of the time that isn't the case and so you will need to find a way to select a subset of the elements without changing the others.
- The most common way to do this is to add a `class` attribute to your HTML element and target that class.
- In your CSS you can target the class by creating a selector for the class name that starts with a full stop character, e.g.:

```html
<ul>
  <li>Item one</li>
  <li class="special">Item two</li>
  <li>Item <em>three</em></li>
</ul>
```

```css
.special {
  color: orange;
  font-weight: bold;
}
```

- In this example, you can apply the class of `special` to any element on your page that you want to have the same look as this list item.

- Sometimes you will see rules with a selector that lists the HTML element selector along with the class:

```css
li.special {
  color: orange;
  font-weight: bold;
}
```

- This syntax means "target any `li` element that has a class of `special`".

### Styling things based on their location in a document

- The **descendant combinator** takes the form of a space between two other selectors, e.g. to select only an `<em>` that is nested inside an `<li>` element:

```css
li em {
  color: rebeccapurple;
}
```

- The **adjacent sibling combinator** (using the `+` between the selectors) styles an element when it comes directly after another element at the same hierarchy level in the HTML, e.g.:

```css
h1 + p {
  font-size: 200%;
}
```

- This example will style a paragraph when it comes directly after a heading at the same hierarchy level in the HTML.

### Styling things based on state

- CSS can target different states of an element, e.g.:

```css
a:link {
  color: pink;
}

a:visited {
  color: green;
}
```

### Combining selectors and combinators

- You can combine multiple selectors and combinators together, e.g.:

```css
/* selects any <span> that is inside a <p>, which is inside an <article>  */
article p span {
  ...;
}

/* selects any <p> that comes directly after a <ul>, which comes directly after an <h1>  */
h1 + ul + p {
  ...;
}
```

- You can combine multiple types, e.g.:

```css
body h1 + p .special {
  color: yellow;
  background-color: black;
  padding: 5px;
}
```

- This example will style any element with a class of `special`, which is inside a `<p>`, which comes just after an `<h1>`, which is inside a `<body>`.

## [How CSS is structured](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_is_structured)

### Applying CSS to HTML

There are three ways to apply CSS to an HTML document:

1. **External stylesheets:** An external stylesheet contains CSS in a separate file with a `.css` extension. This is the most common and useful method of bringing CSS to a document.

```html
<!-- Inside a subdirectory called styles inside the current directory -->
<link rel="stylesheet" href="styles/style.css" />

<!-- Inside a subdirectory called general, which is in a subdirectory called styles, inside the current directory -->
<link rel="stylesheet" href="styles/general/style.css" />

<!-- Go up one directory level, then inside a subdirectory called styles -->
<link rel="stylesheet" href="../styles/style.css" />
```

2. **Internal stylesheet:** Resides within an HTML document. To create an internal stylesheet, you place CSS inside a `<style>` element contained inside the HTML `<head>`.

```html
<head>
  <meta charset="utf-8" />
  <title>My CSS experiment</title>
  <style>
    h1 {
      color: blue;
      background-color: yellow;
      border: 1px solid black;
    }

    p {
      color: red;
    }
  </style>
</head>
```

3. **Inline styles (not recommended):** Inline styles are CSS declarations that affect a single HTML element, contained within a `style` attribute.

```html
<h1 style="color: blue;background-color: yellow;border: 1px solid black;">
  Hello World!
</h1>
```

### Selectors

- A selector targets HTML to apply styles to content.
- Each CSS rule starts with a selector—or a list of selectors—in order to tell the browser which element or elements the rules should apply to.

### Specificity

- The CSS language has rules to control which selector is stronger in the event of a conflict. These rules are called **cascade** and **specificity**.
- **The cascade rule:** Later styles replace conflicting styles that appear earlier in the stylesheet.

```css
p {
  color: red;
}

/* The following rule prevails. */
p {
  color: blue;
}
```

- **The specificity rule:** When there is a conflict between the class selector and the element selector, the class prevails.

```css
.special {
  color: red;
}

p {
  color: blue;
}
```

```html
<!-- This will be red. -->
<p class="special">What color am I?</p>
```

### Properties and values

- CSS consists of two components:

  1.**Properties:** These are human-readable identifiers that indicate which stylistic features you want to modify. For example, `font-size`, `width`, `background-color`.

  2. **Values:** Each property is assigned a value. This value indicates how to style the property.

- When a property is paired with a value, this pairing is called a **CSS declaration**.
- CSS declarations are found within **CSS declaration blocks**.
- CSS declaration blocks are paired with selectors to produce **CSS rulesets**.

### Functions

- Some values which take the form of a function (like `calc` in the example below). A function consists of the function name, and brackets to enclose the values for the function.

```html
<div class="outer"><div class="box">The inner box is 90% - 30px.</div></div>
```

```css
.outer {
  border: 5px solid black;
}

.box {
  padding: 10px;
  width: calc(90% - 30px);
  background-color: rebeccapurple;
  color: white;
}
```

### @rules

- CSS `@rules` (pronounced "at-rules") provide instruction for what CSS should perform or how it should behave.

- Some `@rules` are simple with just a keyword and a value.

- One common `@rule` is `@media`, which is used to create media queries. Media queries use conditional logic for applying CSS styling.

### Shorthands

- Some properties like `font`, `background`, `padding`, `border`, and `margin` are called **shorthand properties**. This is because shorthand properties set several values in a single line.

```css
/* In 4-value shorthands like padding and margin, the values are applied
   in the order top, right, bottom, left (clockwise from the top). There are also other 
   shorthand types, for example 2-value shorthands, which set padding/margin
   for top/bottom, then left/right */
padding: 10px 15px 15px 5px;
```

## [How CSS works](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_works)

![How CSS works](https://mdn.mozillademos.org/files/11781/rendering.svg)

### About the DOM

- The browser loads the HTML (e.g. receives it from the network) and converts it into a DOM (_Document Object Model_).
- The DOM represents the document in the computer's memory.
- A DOM has a tree-like structure. Each element, attribute, and piece of text in the markup language becomes a DOM node in the tree structure.
- The nodes are defined by their relationship to other DOM nodes. Some elements are parents of child nodes, and child nodes have siblings.
- The browser parses the fetched CSS, and sorts the different rules by their selector types into different "buckets", e.g. element, class, ID, and so on.
- Based on the selectors it finds, it works out which rules should be applied to which nodes in the DOM, and attaches style to them as required (this intermediate step is called a render tree).

```html
<p>
  Let's use:
  <span>Cascading</span>
  <span>Style</span>
  <span>Sheets</span>
</p>
```

gets converted into the following DOM structure:

```
P
├─ "Let's use:"
├─ SPAN
|  └─ "Cascading"
├─ SPAN
|  └─ "Style"
└─ SPAN
   └─ "Sheets"
```

### What happens if a browser encounters CSS it doesn't understand?

- If a browser is parsing your rules, and encounters a property or value that it doesn't understand, it ignores it and moves on to the next declaration.
- It will do this if you have made an error and misspelled a property or value, or if the property or value is just too new and the browser doesn't yet support it.
- This behavior means that you can use new CSS as an enhancement, knowing that no error will occur if it is not understood.
