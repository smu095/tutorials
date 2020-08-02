# [HTML Tables](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables)

These summary notes are based on the [HTML Tables](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables) module of MDN's [front-end web developer](https://developer.mozilla.org/en-US/docs/Learn/Front-end_web_developer) course.

## [HTML table basics](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics)

* The content of every table is enclosed by `<table></table>`.
* The smallest container inside a table is a table cell, which is created by a `<td>` element.
* Each row needs to be wrapped in a `<tr>` element, with each cell contained in a `<td>`.

```html
<tr>
  <td>Hi, I'm your first cell.</td>
  <td>I'm your second cell.</td>
  <td>I'm your third cell.</td>
  <td>I'm your fourth cell.</td>
</tr>
```

* To recognize the table headers as headers, both visually and semantically, you can use the `<th>` element.
* Table headers and cells have the `colspan` and `rowspan` attributes, which allow us to span cell contents across columns and rows.
* Tables can be styled using the `<colgroup>` wrapper, with `<col>` tags indicating the styling of one or more columns.

## [HTML table advanced features and accessibility](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Advanced)

* Tables can be given a caption by adding a `<caption>` element and nesting that inside the `<table>`.
* As tables get more complex in structure, it is useful to give them more structural definition using `<thead>`, `<tfoot>`, and `<tbody>` – acting as useful hooks for adding CSS to your table.
* The `scope` attribute can be used to provide screenreaders with additional information (see tutorial for more info).
