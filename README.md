# HDR Processor

## Required packages :

<table>
    <tr><th>package name in Linux</th></tr>
    <tr><td>dcraw</td></tr>
    <tr><td>libjpeg-turbo-progs</td></tr>
    <tr><td>libimage-exiftool-perl</td></tr>
    <tr><td>exiftran</td></tr>
    <tr><td>luminance-hdr</td></tr>
    <tr><td>imagemagick</td></tr>
    <tr><td>enfuse</td></tr>
    <tr><td>hugin-tools</td></tr>
</table>
<code>[sudo] apt-get install [package name]</code>

## Required python3 modules :

<ul>
    <li><code><a rel="muse" href="https://pypi.python.org/pypi/ExifRead">exifread</a></code></li> (or install with <code>[sudo] pip[3] install exifread</code>)</li>
    <li><code><a rel="muse" href="https://python-pillow.org/">pillow</a></code></li> (or install with <code>[sudo] pip[3] install Pillow</code>)</li>
</ul>

## For JPGs
 - Put all the images(at different exposures) in the current directory.
 - Run <code>python3 main_jpg.py</code>

## For RAW Images
 - Put all the raw images(at different exposures) in the current directory.
 - Run <code>python3 main_raw.py</code>