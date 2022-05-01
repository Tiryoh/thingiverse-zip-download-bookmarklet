(
    function () {
        url = document.location.href;
        if (url.indexOf('thingiverse.com') != -1) {
            const [all, id] = url.match(/https?:\/\/www\.thingiverse\.com\/thing:([0-9]*)\/?(.*)/);
            const archive = 'https://thingiverse.com/thing:' + id + '/zip';
            console.log('Opening ' + archive + ' Bookmarklet Version 0.0.1');
            document.location.href = archive;
        }
        else {
            alert('Try this on thingiverse.com. Bookmarklet Version 0.0.1\n' + url);
        }
    }
)();