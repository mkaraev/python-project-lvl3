simple_html = """<!DOCTYPE html>
<html>
</html>
    """

html_with_resources = """<!DOCTYPE html>
<html>
  <head>
    <title>My webpage!</title>
    <link rel="stylesheet" href="/styles/styles.css" />
    <script async src="/javascript/index.js"></script>
  </head>
  <body>
    <h1>Hello, World!</h1>
    <h4 id='date'></h4>

    <div class="image-section">
      <div class="section-style">
        <img src="/images/image1.img" alt="" />
        <p>A random image courtesy of unsplash.com.</p>
      </div>

      <div class="section-style">
        <img src="/images/image2.img" alt="" />
        <p>A random image courtesy of unsplash.com.</p>
      </div>
    </div>

    <div class="image-section">
      <div class="section-style">
        <img src="/images/image3.img" alt="" />
        <p>A random image courtesy of unsplash.com.</p>
      </div>

    </div>
  </body>
</html>
    """
