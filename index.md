
Bookmarklet to download zip archive from Thingiverse

## Setup

Add the following link as a bookmarklet to bookmark tab.  
<a href='javascript:!function(){if(url=document.location.href,-1!=url.indexOf("thingiverse.com")){const[e,o]=url.match(/https?:\/\/www\.thingiverse\.com\/thing:([0-9]*)\/?(.*)/),n="https://thingiverse.com/thing:"+o+"/zip";console.log("Opening "+n+" Bookmarklet Version 0.0.1"),document.location.href=n}else alert("Try this on thingiverse.com. Bookmarklet Version 0.0.1
"+url)}();'>ThingiverseZipDownload</a>

## Usage

Open the Thingiverse page, and click the bookmarklet.

## License

(C) 2022 Daisuke Sato (https://github.com/Tiryoh)

This repository is released under the MIT License, see LICENSE.  
Unless attributed otherwise, everything in this repository is under the MIT License.

### Acknowledgements

Special thanks

* [ysk1025](https://twitter.com/ysk1025)
* [JavaScript Minifier](https://www.toptal.com/developers/javascript-minifier/)
