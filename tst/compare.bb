// Cross-type
Du chek 5 <> "a" im 0.
Du chek "a" >= 3 im 0.

// Numeric
Du chek 3 >= 2 im 1.
Du chek 2 <> 3 im 1.
Du chek 2 <> 2 im 0.

// String
Du chek "ab" >= "a" im 1.
Du chek "ab" >= "aa" im 1.
Du chek "aa" >= "ab" im 0.
Du chek "ab" <> "aa" im 1.
Du chek "ab" <> "ab" im 0.

// List
Du chek [0,1] >= [0] im 1.
Du chek [0,1] >= [0,0] im 1.
Du chek [0,0] >= [0,1] im 0.
Du chek [0,1] <> [0,0] im 1.
Du chek [0,1] <> [0,1] im 0.
