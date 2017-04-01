/**
 * Created by YaYa HuaZhu on 2017/3/21.
 */

function Ajax(arg) {
    /*
     arg:{
     url: 请求的url
     method:默认为get,不区分大小写
     success:function(response,xhr){
     //成功钩子函数
     },
     fail:function(response,xhr){        //reponse就是返回的文本
     //xhr就是XMLHttpRequest对象
     //失败钩子函数
     }
     params:{//传递的参数
     key:value
     }
     }
     */
    this.arg = arg;
    var xhr = window.XMLHttpRequest ?
        new window.XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');

    var data = this.encodeParam(this.arg.params);
    if (/^get$/i.test(this.arg.method)) {
        this.arg.url += '?' + data + '&' + Math.random();//不缓存
    } else {
        this.arg.url += '?' + Math.random();
    }
    xhr.open(this.arg.method || 'get', this.arg.url);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            this.arg.success(xhr.responseText, xhr);
        }
        if (xhr.readyState == 4 && xhr.status != 200) {
            this.arg.fail(xhr.responseText, xhr);
        }
    }.bind(this);
    if (/^post$/i.test(this.arg.method)) {
        xhr.setRequestHeader('content-Type', 'application/x-www-form-urlencoded');
        xhr.send(data);
    } else {
        xhr.send();
    }
}

Ajax.prototype = {
    encodeParam: function () {//把传入的参数变成可传递的参数
        var ay = [];
        for (var i in this.arg.params) {
            var r = encodeURIComponent(i) + '=' + encodeURIComponent(this.arg.params[i]);
            ay.push(r);
        }
        return ay.join("&");
    }
};

(function (doc) {
    var _news = doc.getElementsByClassName('news-link'),
        _newWrap = doc.getElementById('newWrap'),
        _close = doc.getElementById('close');
    for (var i = 0, item; item = _news[i++];) {
        item.onclick = function () {
            console.log(this);
            var url = this.getAttribute('href');
            var ajax = new Ajax({
                url: url,
                method: 'get',
                success: function (res, xhr) {
                    res = JSON.parse(res);
                    doc.getElementsByClassName('new-title')[0].innerHTML = res.title;
                    doc.getElementsByClassName('new-content')[0].innerHTML = res.content;
                }
            });
            _newWrap.style.display = 'block';
            _newWrap.style.transition = '.5s';
            _newWrap.style.transform = 'scaleY(1)';
            _newWrap.style.msTransform = 'scaleY(1)';
            doc.body.scrollTop = 0;
            return false;
        };
    }
    if (_close) {
        _close.onclick = function () {
            _newWrap.style.transition = '.5s';
            _newWrap.style.transform = 'scaleY(0)';
            _newWrap.style.msTransform = 'scaleY(0)';
            setTimeout(function () {
                _newWrap.style.display = 'none';
            }, 500);
        };
    }
})(document);

