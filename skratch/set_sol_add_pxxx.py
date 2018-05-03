# coding=utf-8

def add_sol(p, ans=None):
    with open("euler_{}.py".format(p)) as f:
        lines = [l.strip('\n') for l in f.readlines()]
    sol_ind = [i for i in range(len(lines)) if lines[i] == '"""']
    if ans is None:
        lines.insert(sol_ind[1]+1, "__sol__ = None")
    else:
        lines.insert(sol_ind[1]+1, "__sol__ = {}".format(ans))
    with open("euler_{}.py".format(p), 'wb') as f:
        f.writelines("\n".join(lines))


def set_sol(p, ans):
    with open("./done/euler_{}.py".format(p)) as f:
        lines = [l.strip('\n') for l in f.readlines()]
    sol_ind = [i for i in range(len(lines)) if lines[i] == '"""']
    lines[sol_ind[1]+1] = "__sol__ = {}".format(ans)
    with open("euler_{}.py".format(p), 'wb') as f:
        f.writelines("\n".join(lines))


def add_pxxx(p):
    pxxx_lines = ['def p{}():'.format(p),
                  '    pass',
                  '',
                  'if __name__ == \'__main__\':',
                  '    ANSWER = p{}()'.format(p),
                  '    print(\"Answer: {}\".format(ANSWER))']
    with open("euler_{}.py".format(p), 'a') as f:
        f.write('\n'.join(pxxx_lines))
