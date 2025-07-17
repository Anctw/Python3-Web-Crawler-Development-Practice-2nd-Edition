// ==UserScript==
// @name         HookBase64
// @namespace    https://login1.scrape.center/
// @version      0.1
// @description  Hook Base64 encode function
// @author       Hao
// @match        https://login1.scrape.center/
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function hook(object, attr){
        var func = object[attr]
        object[attr] = function(){
            console.log('hooked', object, attr)
            var ret = func.apply(object, arguments)
            debugger
            return ret
        }
    }
    hook(window, 'btoa')
})();