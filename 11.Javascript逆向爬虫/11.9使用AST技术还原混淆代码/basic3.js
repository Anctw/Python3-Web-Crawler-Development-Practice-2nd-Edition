import { parse } from "@babel/parser";
import generate from "@babel/generator";
import traverse from '@babel/traverse';
import * as types from "@babel/types";
import fs from "fs";

/*
* 1.表达式还原
*/
// const code = fs.readFileSync("code11.js", "utf-8");
// let ast = parse(code);
// traverse(ast, {
//     "UnaryExpression|BinaryExpression|ConditionalExpression|CallExpression": (
//         path
//     ) => {
//         const { confident, value } = path.evaluate();
//         if (value == Infinity || value == -Infinity) return;
//         confident && path.replaceWith(types.valueToNode(value));
//     },
// });
// const { code:output } = generate(ast);
// console.log(output);

/*
* 2.字符串还原
*/
// const code = fs.readFileSync("code2.js", "utf-8");
// let ast = parse(code);
// traverse(ast, {
//     StringLiteral({ node }) {
//         if (node.extra && /\\[ux]/gi.test(node.extra.raw)) {
//             node.extra.raw = node.extra.rawValue;
//         }
//     },
// });
// const { code:output } = generate(ast);
// console.log(output);

/*
* 3.无用代码删除
*/
// const code = fs.readFileSync("code3.js", "utf-8");
// let ast = parse(code);
// traverse(ast, {
//     IfStatement(path) {
//         let { consequent, alternate } = path.node;
//         let testPath = path.get("test");
//         const evaluateTest = testPath.evaluateTruthy();
//         if (evaluateTest === true) {
//             if(types.isBlockStatement(consequent)) {
//                 consequent = consequent.body;
//             }
//             path.replaceWithMultiple(consequent);
//         }else if (evaluateTest === false) {
//             if (alternate != null) {
//                 if(types.isBlockStatement(alternate)) {
//                     alternate = alternate.body;
//                 }
//                 path.replaceWithMultiple(alternate);
//             } else {
//                 path.remove();
//             }
//         }
//     }
// });
// const { code:output } = generate(ast);
// console.log(output);

/*
* 4.反控制流平坦化
*/
const code = fs.readFileSync("code4.js", "utf-8");
let ast = parse(code);
traverse(ast, {
    WhileStatement(path) {
        const { node, scope } = path;
        const { test, body } = node;
        let switchNode = body.body[0];
        let { discriminant, cases } = switchNode;
        let { object, property } = discriminant;
        let arrName = object.name;
        let binding = scope.getBinding(arrName);
        let { init } = binding.path.node;
        object = init.callee.object;
        property = init.callee.property
        let argument = init.arguments[0].value;
        let arrayFlow = object.value[property.name](argument);
        let resultBody = [];
        arrayFlow.forEach((index) => {
            let switchCase = cases.filter((c) => c.test.value == index)[0];
            let caseBody = switchCase.consequent;
            if (types.isContinueStatement(caseBody[caseBody.length - 1])){
                caseBody.pop();
            }
            resultBody = resultBody.concat(caseBody);
        });
        path.replaceWithMultiple(resultBody);
    },
});
const { code:output } = generate(ast);
console.log(output);