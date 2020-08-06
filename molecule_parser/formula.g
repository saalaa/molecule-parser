element: "A".."Z" "a".."z"*
index: "1".."9"+

term: (element | "(" formula ")" | "[" formula "]" | "{" formula "}") [index]

formula: term+

?start: formula
