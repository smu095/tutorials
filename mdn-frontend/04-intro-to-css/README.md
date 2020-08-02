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

TODO.
