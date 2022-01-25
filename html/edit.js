//导入HandyEditor.min.js
var he = HE.getEditor('editor');
//隐藏id为editor的textarea




function getQueryString(name) {
    //正则表达式，获取地址中的参数
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    //匹配目标参数
    var r = window.location.search.substr(1).match(reg);
    //返回参数值
    if (r != null) return unescape(r[2]);
    return null;

}

function getHtml() {
    return he.getHtml();

}

function getText() {
    return he.getText();
}


/*给变量he一个值*/
function setText(html) {
    //将html中的所有\n替换成<br>
    html = html.replace(/\\n/g, "<br>");
    return he.set(html);
}

var text = getQueryString("text");
setText(text)


function setBackgroundColor(color1, color2) {
    
    //设置背景颜色
    document.getElementById("HandyEditor_editor").style.backgroundColor = "#63d8d8";
    document.getElementById("HandyEditor_menu").style.backgroundColor = "#63d8d8";
    
    
}
//方法集
function color() { //
    he.color();
}

