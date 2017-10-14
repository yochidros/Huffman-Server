import subprocess
import upload


def assign_code(nodes, label, result, prefix=""):
    childs = nodes[label]
    tree = {}
    if len(childs) == 2:
        tree["0"] = assign_code(nodes, childs[0], result, prefix+"0")
        tree["1"] = assign_code(nodes, childs[1], result, prefix+"1")
        return tree
    else:
        result[label] = prefix
        return label


def Huffman_code(_vals):
    vals = _vals.copy()
    nodes = {}
    for n in vals.keys():  # leafs initialization
        nodes[n] = []
    print(nodes)
    while len(vals) > 1:  # binary tree creation
        s_vals = sorted(vals.items(), key=lambda x: x[1])
        a1 = s_vals[0][0]
        a2 = s_vals[1][0]
        vals[a1+a2] = vals.pop(a1) + vals.pop(a2)
        nodes[a1+a2] = [a1, a2]
    """  
    if len(vals) == 1:
        tree = {}
        print(tree)
        for k in vals.keys():
            tree["0"] = k
        return tree
    """ 
    code = {}
    root = a1+a2
    tree = {}
    # assignment of the code for the given binary tree
    tree = assign_code(nodes, root, code)
    return tree


def draw_tree(tree, prefix=''):
    if isinstance(tree, str):
        descr = 'N%s [label="%s\n%s", fontcolor=blue, fontsize=16, width=2, shape=box];\n' % (prefix, tree, prefix)
    else:  # Node description
        descr = 'N%s [label="%s"];\n' % (prefix, prefix)
        for child in tree.keys():
            descr += draw_tree(tree[child], prefix=prefix+child)
            descr += "N%s -> N%s;\n" % (prefix, prefix+child)
    return descr


def generate_image(data={}):
    tree = Huffman_code(data)
    print(tree)
    with open("graph.dot", "w") as f:
        f.write("digraph G {\n")
        f.write(draw_tree(tree))
        f.write("}")
    result = subprocess.call('dot -Tpng graph.dot -o graph.png', shell=True)
    if result == 0:
        upload.upload()
