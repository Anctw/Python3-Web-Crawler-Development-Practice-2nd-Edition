// 原始代码
const code = `
let x = '1' + 1
console.log('x', x)
`

const options = {
    compact: false,
    controlFlowFlatterning:true
}

const obfuscator = require('javascript-obfuscator')
function obfuscate(code, options) {
return obfuscator.obfuscate(code, options).getObfuscatedCode()
}
console.log(obfuscate(code, options))



/*
* 4.JavaScript 混淆
* */
// 代码混淆
const _0x267594 = _0x38d9;
(function (_0x201976, _0x427b81) {
    const _0x50454b = _0x38d9, _0x57865d = _0x201976();
    while (!![]) {
        try {
            const _0x38cb93 = parseInt(_0x50454b(0x1f7)) / 0x1 * (-parseInt(_0x50454b(0x1f5)) / 0x2) + parseInt(_0x50454b(0x1fa)) / 0x3 + -parseInt(_0x50454b(0x1f8)) / 0x4 + parseInt(_0x50454b(0x1f6)) / 0x5 * (parseInt(_0x50454b(0x1f1)) / 0x6) + parseInt(_0x50454b(0x1f4)) / 0x7 * (parseInt(_0x50454b(0x1f9)) / 0x8) + -parseInt(_0x50454b(0x1fb)) / 0x9 + parseInt(_0x50454b(0x1f2)) / 0xa;
            if (_0x38cb93 === _0x427b81)
                break;
            else
                _0x57865d['push'](_0x57865d['shift']());
        } catch (_0x3cdfb8) {
            _0x57865d['push'](_0x57865d['shift']());
        }
    }
}(_0x28ef, 0x5cdbe));
function _0x38d9(_0x35d7c0, _0x517edb) {
    const _0x28ef31 = _0x28ef();
    return _0x38d9 = function (_0x38d91d, _0x3ad7a0) {
        _0x38d91d = _0x38d91d - 0x1f1;
        let _0x2d4689 = _0x28ef31[_0x38d91d];
        return _0x2d4689;
    }, _0x38d9(_0x35d7c0, _0x517edb);
}
let x = '1' + 0x1;
function _0x28ef() {
    const _0xcff446 = [
        '6FcUSYY',
        '8394080cPWbhd',
        'log',
        '752122GJiQsA',
        '22dhabmq',
        '2507815JURxqW',
        '68213jjesiM',
        '657072CEXXbi',
        '8FepDhX',
        '1622949KgnAeY',
        '6249951zJXSUb'
    ];
    _0x28ef = function () {
        return _0xcff446;
    };
    return _0x28ef();
}
console[_0x267594(0x1f3)]('x', x);


// 代码压缩
// 变量名混淆
// 字符串混淆
// 代码自我保护
// 控制流平坦化
// 无用代码注入
// 对象名替换
// 禁用控制台输出
// 调试保护
// 域名锁定
// 特殊编码

/*
5.WebAssembly
 */