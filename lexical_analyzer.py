import re

keywords = {
    "int", "float", "char", "double", "if", "else",
    "for", "while", "do", "return", "void", "break",
    "continue", "switch", "case", "default"
}

operators = {
    "+", "-", "*", "/", "%", "=",
    "==", "!=", ">", "<", ">=", "<=",
    "&&", "||", "!", "++", "--"
}

separators = {
    "(", ")", "{", "}", "[", "]", ";", ","
}

special_symbols = {
    "#", "@", "$", "?"
}

def lexical_analyzer(filename):

    keyword_count = 0
    identifier_count = 0
    operator_count = 0
    constant_count = 0
    string_count = 0
    separator_count = 0
    comment_count = 0
    special_symbol_count = 0

    with open(filename, "r") as file:
        code = file.read()

    # Remove and count comments
    comments = re.findall(r'//.*|/\*[\s\S]*?\*/', code)
    comment_count = len(comments)

    code = re.sub(r'//.*|/\*[\s\S]*?\*/', '', code)

    # Token pattern
    pattern = r'"[^"]*"|\'[^\']*\'|\d+\.\d+|\d+|[A-Za-z_][A-Za-z0-9_]*|==|!=|>=|<=|&&|\|\||\+\+|--|[+\-*/%=><!]|[(){}\[\];,]|[#@$?]'

    tokens = re.findall(pattern, code)

    print("\nTOKEN TYPE")
    print("----------------------------------------")

    for token in tokens:

        if token in keywords:
            print(token, "Keyword")
            keyword_count += 1

        elif token in operators:
            print(token, "Operator")
            operator_count += 1

        elif token in separators:
            print(token, "Separator")
            separator_count += 1

        elif token in special_symbols:
            print(token, "Special Symbol")
            special_symbol_count += 1

        elif token.startswith('"') or token.startswith("'"):
            print(token, "String Literal")
            string_count += 1

        elif re.fullmatch(r'\d+(\.\d+)?', token):
            print(token, "Constant")
            constant_count += 1

        elif re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', token):
            print(token, "Identifier")
            identifier_count += 1

    print("----------------------------------------")
    print("\nTOKEN COUNT")
    print("Keywords :", keyword_count)
    print("Identifiers :", identifier_count)
    print("Operators :", operator_count)
    print("Constants :", constant_count)
    print("String Literals :", string_count)
    print("Separators :", separator_count)
    print("Special Symbols :", special_symbol_count)
    print("Comments :", comment_count)


filename = input("Enter source code file name: ")
lexical_analyzer(filename)