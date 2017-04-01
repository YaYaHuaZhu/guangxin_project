/**
 * Created by YaYa HuaZhu on 2017/3/21.
 */

(function (doc) {
    var _news = doc.getElementsByClassName('news-link'),
        _newWrap = doc.getElementById('newWrap'),
        _close = doc.getElementById('close');
    for(var i = 0,item;item = _news[i++];) {
        item.onclick = function () {
            _newWrap.style.display = 'block';
            _newWrap.style.transition = '.5s';
            _newWrap.style.transform = 'scaleY(1)';
            _newWrap.style.msTransform = 'scaleY(1)';
            doc.body.scrollTop = 0;
            return false;
        };
    }
    _close.onclick = function () {
        _newWrap.style.transition = '.5s';
        _newWrap.style.transform = 'scaleY(0)';
        _newWrap.style.msTransform = 'scaleY(0)';
        _newWrap.style.display = 'none';
    };
})(document);