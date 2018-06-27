import ast
import inspect
from jinja2 import Environment, FileSystemLoader
from os import mkdir
from os.path import exists, join

our_modules = ['bib']


def create_markdown(problem_number: int):
    """
    Creates a markdown file where imported functions are expanded to show their source code
    if they are imported from bib.* and are explicit imports (no {@code import *}).
    :param problem_number: Problem number in done.py.*.
    :return: A String of markdown that would look good in GitHub.
    """
    file_name = f'done/py/euler_{str(problem_number).zfill(3)}.py'
    solution_code = open(file_name).read()
    tree = ast.parse(solution_code)
    our_imports = list(get_our_imports(tree))
    func_dict = {}
    for i in our_imports:
        for n in i.names:
            name = n.name
            print(name)
            ldict = locals()
            module = __import__(i.module, globals(), locals(), fromlist=[name])
            func = module.__dict__[name]
            func_dict[f'{i.module}.{name}'] = inspect.getsource(func)
    dependencies = func_dict_to_dependencies(func_dict)
    md_content = create_md_file(problem_number, solution_code, dependencies)
    out_dir = 'pretty_py'
    out_file_name = f'euler_{str(problem_number).zfill(3)}.md'
    if not exists(out_dir):
        mkdir(out_dir)
    with open(join(out_dir, out_file_name), 'w') as f:
        f.write(md_content)


def get_our_imports(tree: ast.AST):
    """Takes an ast tree and returns all imports we own"""
    imports = filter(lambda elem: isinstance(elem, ast.ImportFrom), tree.body)
    return filter(lambda i: i.module.split('.')[0] in our_modules, imports)


def func_dict_to_dependencies(func_dict: dict):
    """
    Takes the dictionary of func_name -> func_code and creates a list of dependencies where each dependency is
    a dictionary with keys name and code
    """
    dependencies = []
    for func_name, func_code in func_dict.items():
        dependencies.append({
            'name': func_name,
            'code': func_code
        })
    return dependencies


def create_md_file(problem_number: int, solution_code: str, dependencies: list):
    """
    Creates the MD file and returns the string to be written to file
    :param problem_number: Project Euler problem number
    :param solution_code: Code of the solution
    :param dependencies: Functions we imported from our own bib
    :return: string of MD file.
    """
    if dependencies is None:
        dependencies = []
    file_env = Environment(loader=FileSystemLoader('./templates'))
    template = file_env.get_template('pretty_py.md.j2')
    return template.render(problem_number=problem_number, solution_code=solution_code, dependencies=dependencies)


if __name__ == '__main__':
    create_markdown(26)
