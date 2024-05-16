Works of pointer array like Brain Fuck.

`>` and `<` move left and right.

`+` and `-` decrement and increment current value at pointer adress.

`*` and `/` multiply and divide the current value at pointer adress and the current value at pointer adress + 1 and set the current value at pointer adress to the result.

`?n` and `?c` print current value at pointer adress as a number and a unicode characer respectively.
`??` prints the text that follows, ended by a | . You can use \n for a new line \\ for \ and \| for |. e.g. `??Hellow World!|`

`,uc` takes user input as a string and sets the current value and onwards as the unicode of each character.
`,un` or `,uf` takes user input as an integar of float respectively, specify `#`, `+`, `-`, `*` or `/` to do that operation to the current value at pointer adress (# = set). e.g. `,un*`
`,` + `c`, `#`, `+`, `-`, `*` or `\` takes the text that follows, ended by a | , and sets/runs an operation to the current value at pointer adress. e.g. `,#100|`

`[` and `]` start and end a loop, and repeats it the amount of times as the text that follows, ended by a | . e.g. `[32|+>]`

`@` followed by a number ended by a `|` , runs a different line of the code like a function, with a seperate pointer array. e.g. `@12|`

`¬` followed by a function name ended by a `|` and parameters seperated by a `|` and ended with `||` calls a function from one of the modules. e.g. `slp|10||`


Current Modules:

Time:

`slp` + n: Sleeps for n seconds.

If:

`>` + a + b + code: Checks if a > b and if so, then it runs code.

`<` + a + b + code: Checks if a < b and if so, then it runs code.

`=` + a + b + code: Checks if a == b and if so, then it runs code.
