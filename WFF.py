from WFFParser import parser

variables = {}


def eval_expression(tree):
    print(tree)
    if tree[0] == 'num':
        return tree[1]
    elif tree[0] == 'string':
        return tree[1]
    elif tree[0] == 'id':
        return tree[1]
    elif tree[0] == 'wff':
        return eval_expression(tree[1])
    elif tree[0] == 'list':
        return eval_expression(tree[1])
    elif tree[0] == 'array':
        return [eval_expression(i) for i in tree[1]]
    elif tree[0] == 'variable':
        if tree[1] in variables:
            variables[tree[1]] = variables.get(tree[1])+1
        else:
            variables[tree[1]] = 1

def read_input():
    data = input('WFF: ').strip()
    return data


def main():
    while True:
        data = read_input()
        if data == 'exit':
            break
        try:
            variables.clear()
            tree = parser.parse(data)
        except Exception as inst:
            print(inst.args[0])
            continue
        try:
            answer = eval_expression(tree)
            freeVars = [v for v in variables.keys() if variables[v]==1]
            print("Free Variables: " + str(freeVars))
            if(type(answer) == list):
                print([eval_expression(i) for i in answer])
            else:
                print(answer)
        except Exception as inst:
            print(inst.args[0])


main()