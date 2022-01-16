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
    

    document.getElementById("HandyEditor_editor").style.backgroundColor = eval(color2);
    document.getElementById("HandyEditor_menu").style.backgroundColor = eval(color1);
    
}
//方法集
function bold() {
    he.bold();
}

function italic() {
    he.italic();
}

function underline() {
    he.underline();
}

function fontsize() { //
    he.fontSize();
}

function fontname() { //
    he.fontname();
}

function color() { //
    he.color();
}

function backcolor() { //
    he.backcolor();
}

function center() {
    he.center();
}

function left() {
    he.left();
}

function right() {
    he.right();
}

function full() { //两端对齐
    he.full();
}

function indent() { //缩进
    he.indent();
}

function outdent() { //取消缩进
    he.outdent();
}

function link() { //
    he.link();
}

function unlink() {
    he.unlink();
}

function textblock() {
    he.textblock();
}

function code() {
    he.code();
}

function selectall() {
    he.selectall();
}

function removeformat() {
    he.removeformat();
}

function trash() {
    he.trash();
}

function image() { //
    he.image();
}

function orderedlist() {
    he.orderedlist();
}

function unorderedlist() {
    he.unorderedlist();
}

function undo() {
    he.undo();
}

function redo() {
    he.redo();
}