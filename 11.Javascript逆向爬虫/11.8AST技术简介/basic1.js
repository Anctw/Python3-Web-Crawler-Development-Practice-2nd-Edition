import { parse } from "@babel/parser";
import generate from "@babel/generator";
import fs from "fs";

/*
* 5.@babel/parser的使用
*/
// const code = fs.readFileSync("codes/code1.js", "utf-8");
// let ast = parse(code);
// console.log(ast);
// console.log(ast.program.body);

/*
* 6.@babel/generate 的使用
*/
const code = fs.readFileSync("codes/code1.js", "utf-8");
let ast = parse(code);
const { code: output } = generate(ast, {
    retainLines: true,
});
console.log(output)


/*
* 8.@babel/types 的使用
*/