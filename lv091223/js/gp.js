/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
    return generate(n)
};

// var generate = (n) => {
//     if (n === 1) return ['()']
//     var result = []
//     var output = generate(n - 1)
//     output.forEach(o => {
//         result.push('(' + o + ')')

//         var post = '()' + o
//         if (!result.includes(post))
//             result.push(post);

//         var post = o + '()'
//         if (!result.includes(post))
//             result.push(post)
//     });
    
//     return result
// }

var generate = (n) => {
    stack = []
    res = []

    var openClosed = (open, closed) => {
        console.log({open, closed, res})
        if (open === closed && open === n) {
            stack.push(res.join(''))
        }
    
        if (open < n) {
            res.push('(')
            openClosed(open + 1, closed)
            res.pop()
        }
    
        if (closed < open) {
            res.push(')')
            openClosed(open, closed + 1)
            res.pop()
        }
    }
    
    openClosed(0, 0)
    return stack
}


var obtained = generateParenthesis(4)
var expected = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
console.log([...new Set(obtained)].length, obtained.length, expected.length)