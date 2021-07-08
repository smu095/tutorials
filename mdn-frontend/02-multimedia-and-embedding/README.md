# Images in HTML

These summary notes are based on the [Multimedia and Embedding](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding) module of MDN's [front-end web developer](https://developer.mozilla.org/en-US/docs/Learn/Front-end_web_developer) course.

## [Images in HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Images_in_HTML)

- To put a simple image on a webpage we use the `<img>` element.
- This is an empty element (meaning that it has no text content or closing tag) that requires a `src` attribute containing a path pointing to the image.
- The `alt` attribute is a textual description of the image, for use in situations where the image cannot be seen/displayed.
- The `width` and `height` attributes are used to specify the width and height of your image.
  - **Note:** You shouldn't alter the size of your images using HTML attributes. If you do need to alter an image's size, you should use CSS instead.

### Annotating images with figures and figure captions

- The `<figure>` and `<figcaption>` provide a semantic container for figures, and to clearly link the figure to the caption. Alternatively, use a `<div>` wrapper.

```html
<figure>
  <img
    src="images/dinosaur.jpg"
    alt="The head and torso of a dinosaur skeleton;
            it has a large head with long sharp teeth"
    width="400"
    height="341"
  />

  <figcaption>
    A T-Rex on display in the Manchester University Museum.
  </figcaption>
</figure>
```

- **In summary:** if an image has meaning, in terms of your content, you should use an HTML image. If an image is purely decoration, you should use CSS background images.

## [Video and audio content](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Video_and_audio_content)

### The `<video>` element

- The `<video>` element allows you to embed a video. Notable attributes are:

  - `src`: path to the video you want to embed.
  - `controls`: include the browser's own control interface.
  - `width` and `height`
  - `autoplay`: the audio or video start playing right away, while the rest of the page is loading.
  - `loop`: the video (or audio) starts playing again whenever it finishes.
  - `mute`: play with the sound turned off by default.
  - `poster`: the URL of an image which will be displayed before the video is played. It is intended to be used for a splash screen or advertising screen.
  - `preload`: Used for buffering large files; it can take one of three values:
    - `"none"` does not buffer the file
    - `"auto"` buffers the media file
    - `"metadata"` buffers only the metadata for the file

- The paragraph inside the `<video>` tags is called fallback content — this will be displayed if the browser accessing the page doesn't support the `<video>` element.
- `<source>` causes the browser to look through each file type and play the first one that is supported. The `type` attribute ([MIME type](https://developer.mozilla.org/en-US/docs/Glossary/MIME_type)) optimises this process.
- `<track>` points to a WebVTT file used for subtitles.

```html
<video
  controls
  width="400"
  height="400"
  autoplay
  loop
  muted
  preload="auto"
  poster="poster.png"
>
  <source src="rabbit320.mp4" type="video/mp4" />
  <source src="rabbit320.webm" type="video/webm" />
  <track kind="subtitles" src="subtitles_en.vtt" srclang="en" />
  <p>
    Your browser doesn't support HTML video. Here is a
    <a href="rabbit320.mp4">link to the video</a> instead.
  </p>
</video>
```

### The `<audio>` element

- The `<audio>` element works just like the `<video>` element, with a few small differences:
  - doesn't support the `width`/`height` \* attributes (no visual component)
  - doesn't support the `poster` attribute (no visual component).
- Other than this, `<audio>` supports all the same features as `<video>`.

## [From object to iframe — other embedding technologies](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Other_embedding_technologies)

- `<iframe>` elements are designed to allow you to embed other web documents into the current document.
- There are some security concerns to be aware of, [check the tutorial](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Other_embedding_technologies) for more info.

```html
<iframe
  src="https://developer.mozilla.org/en-US/docs/Glossary"
  width="100%"
  height="500"
  frameborder="0"
  allowfullscreen
  sandbox
>
  <p>
    <a href="https://developer.mozilla.org/en-US/docs/Glossary">
      Fallback link for browsers that don't support iframes
    </a>
  </p>
</iframe>
```

- Note the `sandbox` attribute, which requests heightened security settings.
- The `<embed>` and `<object>` elements are general purpose embedding tools for embedding multiple types of external content, but embedding methods are really a legacy technology.

## [Adding vector graphics to the Web](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Adding_vector_graphics_to_the_Web)

- **Raster images** are defined using a grid of pixels — a raster image file contains information showing exactly where each pixel is to be placed, and exactly what color it should be. Popular web raster formats include Bitmap (.bmp), PNG (.png), JPEG (.jpg), and GIF (.gif.)
- **Vector images** are defined using algorithms — a vector image file contains shape and path definitions that the computer can use to work out what the image should look like when rendered on the screen. The SVG format allows us to create powerful vector graphics for use on the Web.
- SVG is an XML-based language for describing vector images. It's basically markup, except that you've got many different elements for defining the shapes you want to appear in your image, and the effects you want to apply to those shapes.
- For creating SVG images, most people use a vector graphics editor like Inkscape or Illustrator.

## [Responsive images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)

- **Art direction:** The problem whereby you want to serve cropped images for different layouts — for example a landscape image showing a full scene for a desktop layout, and a portrait image showing the main subject zoomed in for a mobile layout.
- **Resolution switching:** The problem whereby you want to serve smaller image files to narrow screen devices, as they don't need huge images like desktop displays do — and also optionally that you want to serve different resolution images to high density/low density screens.

### Resolution switching: Different sizes

```html
<img
  srcset="elva-fairy-480w.jpg 480w, elva-fairy-800w.jpg 800w"
  sizes="(max-width: 600px) 480px,
            800px"
  src="elva-fairy-800w.jpg"
  alt="Elva dressed as a fairy"
/>
```

- `srcset` defines the set of images we will allow the browser to choose between, and what size each image is.
- Each set of image information is separated from the previous one by a comma. For each one, we write:
  - An image filename (`elva-fairy-480w.jpg`)
  - A space
  - The image's intrinsic width in pixels (`480w`) — note that this uses the `w` unit, not `px` as you might expect.
- `sizes` defines a set of media conditions (e.g. screen widths) and indicates what image size would be best to choose. In this case, before each comma we write:
  - A media condition (`(max-width:600px)`), describing a possible state that the screen can be in.
    A space.
    The width of the slot the image will fill when the media condition is true (`480px`).

### Resolution switching: Same size, different resolutions

- If you're supporting multiple display resolutions, but everyone sees your image at the same real-world size on the screen, you can allow the browser to choose an appropriate resolution image by using `srcset` with `x`-descriptors and without `sizes`.
- In this example, the following CSS is applied to the image so that it will have a width of 320 pixels on the screen (also called CSS pixels):

```css
img {
  width: 320px;
}
```

- In this case, `sizes` is not needed — the browser simply works out what resolution the display is that it is being shown on, and serves the most appropriate image referenced in the srcset.

```html
<img
  srcset="elva-fairy-320w.jpg, elva-fairy-480w.jpg 1.5x, elva-fairy-640w.jpg 2x"
  src="elva-fairy-640w.jpg"
  alt="Elva dressed as a fairy"
/>
```

### Art direction

- The `<picture>` element is a wrapper containing several `<source>` elements that provide different sources for the browser to choose from:

```html
<picture>
  <source media="(max-width: 799px)" srcset="elva-480w-close-portrait.jpg" />
  <source media="(min-width: 800px)" srcset="elva-800w.jpg" />
  <img src="elva-800w.jpg" alt="Chris standing up holding his daughter Elva" />
</picture>
```
