# Images in HTML

These summary notes are based on the [Multimedia and Embedding](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding) module of MDN's [front-end web developer](https://developer.mozilla.org/en-US/docs/Learn/Front-end_web_developer) course.

## [Images in HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Images_in_HTML)

* To put a simple image on a webpage we use the `<img>` element. 
* This is an empty element (meaning that it has no text content or closing tag) that requires a `src` attribute containing a path pointing to the image.
*  The `alt` attribute is a textual description of the image, for use in situations where the image cannot be seen/displayed.
* The `width` and `height` attributes are used to specify the width and height of your image. 
  * **Note:** You shouldn't alter the size of your images using HTML attributes. If you do need to alter an image's size, you should use CSS instead.

### Annotating images with figures and figure captions

* The `<figure>` and `<figcaption>` provide a semantic container for figures, and to clearly link the figure to the caption. Alternatively, use a `<div>` wrapper.

```html
<figure>
  <img src="images/dinosaur.jpg"
       alt="The head and torso of a dinosaur skeleton;
            it has a large head with long sharp teeth"
       width="400"
       height="341">

  <figcaption>A T-Rex on display in the Manchester University Museum.</figcaption>
</figure>
```

* **In summary:** if an image has meaning, in terms of your content, you should use an HTML image. If an image is purely decoration, you should use CSS background images.

## [Video and audio content](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Video_and_audio_content)

### The `<video>` element

* The `<video>` element allows you to embed a video. Notable attributes are:
  * `src`: path to the video you want to embed.
  * `controls`: include the browser's own control interface.
  * `width` and `height`
  * `autoplay`: the audio or video start playing right away, while the rest of the page is loading.
  * `loop`: the video (or audio) starts playing again whenever it finishes.
  * `mute`: play with the sound turned off by default.
  * `poster`: the URL of an image which will be displayed before the video is played. It is intended to be used for a splash screen or advertising screen.
  * `preload`: Used for buffering large files; it can take one of three values:
    * `"none"` does not buffer the file
    * `"auto"` buffers the media file
    * `"metadata"` buffers only the metadata for the file

* The paragraph inside the `<video>` tags is called fallback content — this will be displayed if the browser accessing the page doesn't support the `<video>` element.
* `<source>` causes the browser to look through each file type and play the first one that is supported. The `type` attribute ([MIME type](https://developer.mozilla.org/en-US/docs/Glossary/MIME_type)) optimises this process.
* `<track>` points to a WebVTT file used for subtitles.

```html
<video controls width="400" height="400"
       autoplay loop muted preload="auto" 
       poster="poster.png">
  <source src="rabbit320.mp4" type="video/mp4">
  <source src="rabbit320.webm" type="video/webm">
  <track kind="subtitles" src="subtitles_en.vtt" srclang="en">
  <p>Your browser doesn't support HTML video. Here is a <a href="rabbit320.mp4">link to the video</a> instead.</p>
</video>
```

### The `<audio>` element

* The `<audio>` element works just like the `<video>` element, with a few small differences:
  * doesn't support the `width`/`height`   * attributes (no visual component)
  * doesn't support the `poster` attribute (no visual component).
* Other than this, `<audio>` supports all the same features as `<video>`.

## [From object to iframe — other embedding technologies](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Other_embedding_technologies)

TODO.