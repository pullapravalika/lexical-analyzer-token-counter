# Lexical Analyzer & Token Counter

## 1. Title

**Lexical Analyzer & Token Counter**

## 2. Objective

The objective of this project is to develop a lexical analyzer that reads a source-code file and identifies different types of tokens. The program also counts the number of tokens belonging to each category.

The token types identified by the program are:

* Keywords
* Identifiers
* Operators
* Constants/Literals
* String Literals
* Separators/Delimiters
* Special Symbols
* Comments

## 3. Problem Statement

Develop a program that reads a source-code file and performs lexical analysis by identifying and counting different types of tokens.

The program accepts a source-code file as input and analyzes the contents of the file. Each token is classified according to its type, and the total number of tokens in each category is displayed.

## 4. Algorithm

1. Start the program.
2. Ask the user to enter the source-code file name.
3. Open and read the source-code file.
4. Identify and count comments.
5. Remove comments from the source code for token processing.
6. Identify keywords.
7. Identify identifiers.
8. Identify operators.
9. Identify constants/numeric literals.
10. Identify string literals.
11. Identify separators/delimiters.
12. Identify special symbols.
13. Display each token along with its token type.
14. Display the total count of each token category.
15. Stop the program.

## 5. Source Code

The project is implemented using Python.

The main source-code file is:

`lexical_analyzer.py`

The program reads the input source-code file and uses regular expressions to identify different types of tokens.

## 6. Sample Input

The following C source code is used as sample input:

```c
int sum = a + b;
float average = sum / 2.0;

// Calculate average

if (average > 50)
    printf("Pass");
```

The input is stored in the file:

`input.c`

## 7. Sample Output

```text
TOKEN TYPE
----------------------------------------
int Keyword
sum Identifier
= Operator
a Identifier
+ Operator
b Identifier
; Separator
float Keyword
average Identifier
= Operator
sum Identifier
/ Operator
2.0 Constant
; Separator
if Keyword
( Separator
average Identifier
> Operator
50 Constant
) Separator
printf Identifier
( Separator
"Pass" String Literal
) Separator
; Separator
----------------------------------------

TOKEN COUNT
Keywords : 3
Identifiers : 7
Operators : 5
Constants : 2
String Literals : 1
Separators : 7
Special Symbols : 0
Comments : 1
```

## 8. Token Classification

| Token                  | Type           |
| ---------------------- | -------------- |
| `int`                  | Keyword        |
| `sum`                  | Identifier     |
| `=`                    | Operator       |
| `a`                    | Identifier     |
| `+`                    | Operator       |
| `b`                    | Identifier     |
| `;`                    | Separator      |
| `float`                | Keyword        |
| `average`              | Identifier     |
| `/`                    | Operator       |
| `2.0`                  | Constant       |
| `if`                   | Keyword        |
| `(`                    | Separator      |
| `>`                    | Operator       |
| `50`                   | Constant       |
| `)`                    | Separator      |
| `printf`               | Identifier     |
| `"Pass"`               | String Literal |
| `// Calculate average` | Comment        |

## 9. Test Cases

### Test Case 1: Basic C Program

**Input:**

```c
int a = 10;
int b = 20;
int sum = a + b;
```

**Expected Result:**

The program identifies:

* `int` as a Keyword
* `a`, `b`, and `sum` as Identifiers
* `=`, `+` as Operators
* `10`, `20` as Constants
* `;` as Separators

### Test Case 2: Conditional Statement

**Input:**

```c
if (a > 10)
    printf("Greater");
```

**Expected Result:**

The program identifies:

* `if` as a Keyword
* `a` and `printf` as Identifiers
* `>` as an Operator
* `10` as a Constant
* `"Greater"` as a String Literal
* `(`, `)` as Separators

### Test Case 3: Comment

**Input:**

```c
// This is a comment
int number = 100;
```

**Expected Result:**

The program identifies the comment and counts it separately. It also identifies `int` as a Keyword, `number` as an Identifier, `100` as a Constant, and `=` and `;` according to their respective token types.

## 10. Conclusion

The Lexical Analyzer & Token Counter successfully reads a source-code file and performs lexical analysis. It identifies different types of tokens such as keywords, identifiers, operators, constants, string literals, separators, special symbols, and comments. The program also displays the total number of tokens in each category.

This project demonstrates the basic working principle of a lexical analyzer used in compiler design.
