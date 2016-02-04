
from typing import Any, Dict, Optional, Sequence, Tuple, Union
# At present, I don't understand how to tell mypy about ast.Node
# import ast
# Node = ast.Node
Node = Any
class AstArgFormatter(AstFormatter):
    def do_BoolOp(self, node: Node) -> str: ...
    def do_Bytes(self, node: Node) -> str: ...
    def do_Name(self, node: Node) -> Any: ...
        # return str if Node.id in Tuple[str,str] else Node.id
    def do_Num(self, node: Node) -> str: ...
    def do_Str(self, node: Node) -> str: ...
class AstFormatter:
    def do_Assert(self, node: Node) -> str: ...
    def do_Assign(self, node: Node) -> str: ...
    def do_Attribute(self, node: Node) -> str: ...
    def do_AugAssign(self, node: Node) -> str: ...
    def do_AugLoad(self, node: Node) -> str: ...
    def do_BinOp(self, node: Node) -> str: ...
    def do_BoolOp(self, node: Node) -> str: ...
    def do_Break(self, node: Node) -> str: ...
    def do_Bytes(self, node: Node) -> str: ...
    def do_Call(self, node: Node) -> str: ...
    def do_ClassDef(self, node: Node) -> str: ...
    def do_Compare(self, node: Node) -> str: ...
    def do_Continue(self, node: Node) -> str: ...
    def do_Del(self, node: Node) -> str: ...
    def do_Delete(self, node: Node) -> str: ...
    def do_Dict(self, node: Node) -> str: ...
    def do_Ellipsis(self, node: Node) -> str: ...
    def do_ExceptHandler(self, node: Node) -> str: ...
    def do_Exec(self, node: Node) -> str: ...
    def do_Expr(self, node: Node) -> str: ...
    def do_Expression(self, node: Node) -> str: ...
    def do_ExtSlice(self, node: Node) -> str: ...
    def do_For(self, node: Node) -> str: ...
    def do_FunctionDef(self, node: Node) -> str: ...
    def do_GeneratorExp(self, node: Node) -> str: ...
    def do_Global(self, node: Node) -> str: ...
    def do_If(self, node: Node) -> str: ...
    def do_IfExp(self, node: Node) -> str: ...
    def do_Import(self, node: Node) -> str: ...
    def do_ImportFrom(self, node: Node) -> str: ...
    def do_Index(self, node: Node) -> str: ...
    def do_Interactive(self, node: Node) -> None: ...
    def do_Lambda(self, node: Node) -> str: ...
    def do_List(self, node: Node) -> str: ...
    def do_ListComp(self, node: Node) -> str: ...
    def do_Load(self, node: Node) -> str: ...
    def do_Module(self, node: Node) -> str: ...
    def do_Name(self, node: Node) -> str: ...
    def do_Num(self, node: Node) -> str: ...
    def do_Param(self, node: Node) -> str: ...
    def do_Pass(self, node: Node) -> str: ...
    def do_Print(self, node: Node) -> str: ...
    def do_Raise(self, node: Node) -> str: ...
    def do_Repr(self, node: Node) -> str: ...
    def do_Return(self, node: Node) -> str: ...
    def do_Slice(self, node: Node) -> str: ...
    def do_Store(self, node: Node) -> str: ...
    def do_Str(self, node: Node) -> str: ...
    def do_Subscript(self, node: Node) -> str: ...
    def do_TryExcept(self, node: Node) -> str: ...
    def do_TryFinally(self, node: Node) -> str: ...
    def do_Tuple(self, node: Node) -> str: ...
    def do_UnaryOp(self, node: Node) -> str: ...
    def do_While(self, node: Node) -> str: ...
    def do_With(self, node: Node) -> str: ...
    def do_Yield(self, node: Node) -> str: ...
    def do_arg(self, node: Node) -> str: ...
    def do_arguments(self, node: Node) -> str: ...
    def do_comprehension(self, node: Node) -> str: ...
    def do_keyword(self, node: Node) -> str: ...
    def format(self, node: Node) -> bool: ...
    def get_import_names(self, node: Node) -> Any: ...
        # return result
    def indent(self, s: str) -> str: ...
    def kind(self, node: Node) -> Any: ...
        # return Node.__class__.__name__
    def op_name(self, node: Node, strict: bool=True) -> str: ...
    def visit(self, node: Node) -> str: ...
class LeoGlobals:
    def _callerName(self, n: int=1, files=False) -> str: ...
    def callers(self, n: int=4, count=0, excludeCaller=True, files=False) -> Any: ...
        # return sep.join(result)
    def cls(self) -> None: ...
    def pdb(self) -> None: ...
    def shortFileName(self, fileName, n: int=None) -> Any: ...
        # return os.path.basename(fileName)
        # return str
    def trace(self, *args, **keys) -> None: ...
class Pattern(object):
    def __eq__(self, obj) -> Any: ...
        # return NotImplemented
        # return bool
    def __hash__(self) -> int: ...
    def __init__(self, find_s: str, repl_s: str='', trace: bool=False) -> None: ...
    def __ne__(self, obj) -> Any: ...
        # return not self.__eq__(obj)
    def __repr__(self) -> str: ...
    def all_matches(self, s: str, trace: bool=False) -> Any: ...
        # return List
        # return list(self.regex.finditer(str))
    def full_balanced_match(self, s: str, i: int, trace: bool=False) -> Any: ...
        # return int if str else None
    def is_balanced(self) -> bool: ...
    def match(self, s: str, trace: bool=False) -> Tuple[bool,str]: ...
    def match_balanced(self, delim, s: str, i: int, trace: bool=False) -> int: ...
    def match_entire_string(self, s: str, trace: bool=False) -> Any: ...
        # return bool
        # return int is not None
    def replace(self, m, s: str, trace: bool=False) -> str: ...
class StandAloneMakeStubFile:
    def __init__(self) -> None: ...
    def create_parser(self) -> Any: ...
        # return optparse.OptionParser
    def finalize(self, fn: str) -> str: ...
    def get_config_string(self) -> str: ...
    def init_parser(self, s: str) -> None: ...
    def is_section_name(self, s: str) -> bool: ...
    def make_stub_file(self, fn: str) -> None: ...
    def run(self) -> None: ...
    def run_all_unit_tests(self) -> None: ...
    def scan_command_line(self) -> None: ...
    def scan_options(self) -> None: ...
    def scan_patterns(self, section_name) -> List: ...
class Stub(object):
    def __eq__(self, obj) -> Any: ...
        # return NotImplemented
        # return self.name==obj.name
    def __ge__(self, other) -> bool: ...
    def __gt__(self, obj) -> Any: ...
        # return NotImplemented
        # return self.name>obj.name
    def __hash__(self) -> Any: ...
        # return int
        # return self.parent.hash()+int
    def __init__(self, kind, name: str, parent) -> None: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, obj) -> Any: ...
        # return not self.__eq__(obj)
    def __repr__(self) -> str: ...
    def full_name(self) -> Any: ...
        # return self.name
        # return str
class StubFormatter(AstFormatter):
    def __init__(self, general_patterns: List[Pattern]) -> None: ...
    def do_BoolOp(self, node: Node) -> str: ...
    def do_Bytes(self, node: Node) -> str: ...
    def do_Name(self, node: Node) -> str: ...
    def do_Num(self, node: Node) -> str: ...
    def do_Return(self, node: Node) -> str: ...
    def do_Str(self, node: Node) -> str: ...
    def match(self, patterns: List, s: str) -> str: ...
    def visit(self, node: Node) -> str: ...
class StubTraverser(ast.NodeVisitor):
    def __init__(self, controller: StandAloneMakeStubFile) -> None: ...
    def format_arguments(self, node: Node) -> str: ...
    def format_return_expressions(self, aList1, aList: List, kind) -> str: ...
    def format_returns(self, node: Node) -> Any: ...
        # return self.format_return_expressions(r1,r,kind)
        # return str
    def get_def_name(self, node: Node) -> str: ...
    def indent(self, s: str) -> str: ...
    def is_known_type(self, s: str) -> Any: ...
        # return bool
        # return self.is_known_type(str)
    def munge_arg(self, s: str) -> str: ...
    def out(self, s: str) -> None: ...
    def output_stubs(self, stub, sort_flag) -> None: ...
    def run(self, node: Node) -> None: ...
    def visit_ClassDef(self, node: Node) -> None: ...
    def visit_FunctionDef(self, node: Node) -> None: ...
    def visit_Return(self, node: Node) -> None: ...
class TestClass:
    def parse_group(group: str) -> Tuple[int,str]: ...
    def return_all(self) -> bool: ...
    def return_array() -> Any: ...
        # return f(str)
    def return_list(self, a: str) -> List[str]: ...
def main() -> None: ...
def pdb() -> None: ...
