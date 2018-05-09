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

def remove_sol(p, ans=None):
    with open("../done/euler_{}.py".format(p)) as f:
        lines = [l.strip('\n') for l in f.readlines()]

    nosol = [l for l in lines if "__sol__" not in l]
    print(nosol)
    with open("../done/euler_{}.py".format(p), 'wb') as f:
        f.writelines("\n".join(nosol))



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

from os import listdir, getcwd

def extractsol(p, ans=None):
    with open("../done/euler_{}.py".format(p)) as f:
        lines = [l.strip('\n') for l in f.readlines() if '__sol__' in l]
    try:
        return(p, int(lines[0].split(' ')[-1]))
    except IndexError:
        pass

from codecs import getwriter
import json
# sols = {'001': 233168, '002': 4613732, '003': 6857, '004': 906609, '005': 232792560, '006': 25164150, '007': 104743, '008': 23514624000L, '009': 31875000, '010': 142913828922L, '011': 70600674, '012': 76576500, '013': 5537376230L, '014': 837799, '015': 137846528820L, '016': 1366, '017': 21124, '018': 1074, '019': 171, '020': 648, '021': 31626, '022': 871198282, '023': 4179871, '024': 2783915460L, '025': 4782, '026': 983, '027': -59231, '028': 669171001, '029': 9183, '030': 443839, '031': 73682, '032': 45228, '033': 100, '034': 40730, '035': 55, '036': 872187, '037': 748317, '038': 932718654, '039': 840, '040': 210, '041': 7652413, '042': 162, '043': 16695334890L, '044': 5482660, '045': 1533776805, '046': 5777, '047': 134043, '048': 9110846700L, '049': 296962999629L, '050': 997651, '052': 142857, '053': 4075, '054': 376, '055': 249, '056': 972, '057': 153, '058': 26241, '060': 26033, '062': 127035954683L, '063': 49, '067': 7273, '068': 6531031914842725L, '071': 428570, '072': 303963552391L, '073': 7295372, '075': 161667, '076': 190569291, '077': 71, '079': 73162890, '080': 40886, '081': 427337, '082': 260324, '083': 425185, '085': 2772, '087': 1097343, '089': 743, '092': 8581146, '094': 518408346, '097': 8739992577L, '099': 709, '102': 228, '107': 259679, '112': 1587000, '118': 44680, '119': 248155780267521L, '123': 21035, '124': 21417, '125': 2906969179L, '139': 10057761, '164': 378158756814587L, '173': 1572729, '174': 209566, '187': 17427258, '206': 1389019170, '347': 11109800204052L}
# with open('../txt_files/solutions.txt', 'wb') as f:
#     json.dump(sols, getwriter('utf-8')(f), ensure_ascii=True, indent=4, sort_keys=True)
# import json



DONE = [f[6:9] for f in listdir('../done/')  # find all files in the done dir
        if f.startswith('euler_')  # for which the file start with 'euler_'
        and f.endswith('.py')]  # and ends with '.py'

print(DONE)

for prob in DONE:
    remove_sol(prob)

sols = [ppp for ppp in [extractsol(p) for p in DONE ] if ppp != None]
print(sols)

solsd = {p[0]:p[1] for p in sols}
print(solsd)
