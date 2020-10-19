$(document).ready(function() {
    var code = $('.code')[0];
    var mode = $('.language').val();
    var editor = CodeMirror.fromTextArea(code, {
        lineNumbers: true,
        mode: mode,
        theme: "cobalt",
        autoCloseTags: true,
        autoCloseBrackets: true,
        comment:true,
        autoRefresh:true,
    });
})