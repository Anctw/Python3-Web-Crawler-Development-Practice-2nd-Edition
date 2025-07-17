import { parse } from "@babel/parser";
import generate from "@babel/generator";
import traverse from '@babel/traverse';
import * as types from "@babel/types";
import fs from "fs";

/*
* 7.@babel/traverse 的使用
*/
// const code = fs.readFileSync("codes/code1.js", "utf-8");
// let ast = parse(code);
// traverse(ast, {
//     enter(path){
//         console.log(path)
//     },
// });

//使用AST修改代码（第一种方法）
// const code = fs.readFileSync("codes/code1.js", "utf-8");
// let ast = parse(code);
// traverse(ast, {
//     enter(path){
//         let node = path.node;
//         if (node.type === "NumericLiteral" && node.value === 3) {
//             node.value = 5;
//         }
//         if (node.type === "StringLiteral" && node.value === "hello") {
//             node.value = "hi"
//         }
//     },
// });

// const { code: output } = generate(ast, {
//     retainLines: true,
// });
// console.log(output)

//使用AST修改代码（第二种方法）
// const code = fs.readFileSync("codes/code1.js", "utf-8");
// let ast = parse(code);
// traverse(ast, {
//     NumericLiteral(path){
//         if (path.node.value === 3) {
//             path.node.value = 5;
//         }
//     },
//     StringLiteral(path){
//         if (path.node.value === "hello") {
//             path.node.value = "hi"
//         }
//     },
// });

// const { code: output } = generate(ast, {
//     retainLines: true,
// });
// console.log(output)

//使用AST删除代码
// const code = fs.readFileSync("codes/code1.js", "utf-8");
// let ast = parse(code);
// traverse(ast, {
//     CallExpression(path){
//         let node = path.node;
//         if (
//             node.callee.object.name === "console" &&
//             node.callee.property.name === "log"
//         ) {
//             path.remove()
//         }
//     },
// });

// const { code: output } = generate(ast, {
//     retainLines: true,
// });
// console.log(output)

/*
* 8.@babel/types 的使用
*/
const code = "const a = 1;";
let ast = parse(code);
traverse(ast, {
    VariableDeclaration(path){
        let init = types.binaryExpression(
            "+",
            types.identifier("a"),
            types.numericLiteral(1)
        );
        let declarator = types.variableDeclarator(types.identifier("b"), init);
        let declaration = types.variableDeclaration("const", [declarator]);
        path.insertAfter(declaration);
        path.stop();
    },
});
const output = generate(ast, {
    retainLines: true,
}).code;
console.log(output)