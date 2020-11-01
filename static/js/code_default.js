$(document).ready(function() {
    var code = $('.code')[0];
    var mode = $('.language').val();
    var mixedMode = {
        name: "htmlmixed",
        scriptTypes: [{matches: /\/x-handlebars-template|\/x-mustache/i,
                       mode: null},
                      {matches: /(text|application)\/(x-)?vb(a|script)/i,
                       mode: "vbscript"}]
      };
    if (mode == "htmlmixed") {
        mode = mixedMode
    }
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