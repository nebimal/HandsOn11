def create_rb_tree():
    NIL = {'key': None, 'left': None, 'right': None, 'parent': None, 'color': 'black'}
    T = {'root': NIL, 'NIL': NIL}
    return T

def create_rb_node(key, T):
    node = {'key': key, 'left': T['NIL'], 'right': T['NIL'], 'parent': T['NIL'], 'color': 'red'}
    return node

def RB_Search(x, k, T):
    while x != T['NIL'] and x['key'] is not None and k != x['key']:
        if k < x['key']:
            x = x['left']
        else:
            x = x['right']
    return x

def RB_Minimum(x, T):
    while x['left'] != T['NIL']:
        x = x['left']
    return x

def RB_Maximum(x, T):
    while x['right'] != T['NIL']:
        x = x['right']
    return x

def RB_Successor(x, T):
    if x['right'] != T['NIL']:
        return RB_Minimum(x['right'], T)
    y = x['parent']
    while y != T['NIL'] and x == y['right']:
        x = y
        y = y['parent']
    return y

def RB_Predecessor(x, T):
    if x['left'] != T['NIL']:
        return RB_Maximum(x['left'], T)
    y = x['parent']
    while y != T['NIL'] and x == y['left']:
        x = y
        y = y['parent']
    return y

def RB_Transplant(T, u, v):
    if u['parent'] == T['NIL']:
        T['root'] = v
    elif u == u['parent']['left']:
        u['parent']['left'] = v
    else:
        u['parent']['right'] = v
    v['parent'] = u['parent']

def RB_Left_Rotate(T, x):
    y = x['right']
    x['right'] = y['left']
    if y['left'] != T['NIL']:
        y['left']['parent'] = x
    y['parent'] = x['parent']
    if x['parent'] == T['NIL']:
        T['root'] = y
    elif x == x['parent']['left']:
        x['parent']['left'] = y
    else:
        x['parent']['right'] = y
    y['left'] = x
    x['parent'] = y

def RB_Right_Rotate(T, y):
    x = y['left']
    y['left'] = x['right']
    if x['right'] != T['NIL']:
        x['right']['parent'] = y
    x['parent'] = y['parent']
    if y['parent'] == T['NIL']:
        T['root'] = x
    elif y == y['parent']['right']:
        y['parent']['right'] = x
    else:
        y['parent']['left'] = x
    x['right'] = y
    y['parent'] = x

def RB_Insert(T, z):
    y = T['NIL']
    x = T['root']
    while x != T['NIL']:
        y = x
        if z['key'] < x['key']:
            x = x['left']
        else:
            x = x['right']
    z['parent'] = y
    if y == T['NIL']:
        T['root'] = z
    elif z['key'] < y['key']:
        y['left'] = z
    else:
        y['right'] = z
    RB_Insert_Fixup(T, z)

def RB_Insert_Fixup(T, z):
    while z['parent']['color'] == 'red':
        if z['parent'] == z['parent']['parent']['left']:
            y = z['parent']['parent']['right']
            if y['color'] == 'red':
                z['parent']['color'] = 'black'
                y['color'] = 'black'
                z['parent']['parent']['color'] = 'red'
                z = z['parent']['parent']
            else:
                if z == z['parent']['right']:
                    z = z['parent']
                    RB_Left_Rotate(T, z)
                z['parent']['color'] = 'black'
                z['parent']['parent']['color'] = 'red'
                RB_Right_Rotate(T, z['parent']['parent'])
        else:
            y = z['parent']['parent']['left']
            if y['color'] == 'red':
                z['parent']['color'] = 'black'
                y['color'] = 'black'
                z['parent']['parent']['color'] = 'red'
                z = z['parent']['parent']
            else:
                if z == z['parent']['left']:
                    z = z['parent']
                    RB_Right_Rotate(T, z)
                z['parent']['color'] = 'black'
                z['parent']['parent']['color'] = 'red'
                RB_Left_Rotate(T, z['parent']['parent'])
    T['root']['color'] = 'black'

def RB_Delete(T, z):
    y = z
    y_original_color = y['color']
    if z['left'] == T['NIL']:
        x = z['right']
        RB_Transplant(T, z, z['right'])
    elif z['right'] == T['NIL']:
        x = z['left']
        RB_Transplant(T, z, z['left'])
    else:
        y = RB_Minimum(z['right'], T)
        y_original_color = y['color']
        x = y['right']
        if y['parent'] != z:
            RB_Transplant(T, y, y['right'])
            y['right'] = z['right']
            y['right']['parent'] = y
        RB_Transplant(T, z, y)
        y['left'] = z['left']
        y['left']['parent'] = y
        y['color'] = z['color']
    if y_original_color == 'black':
        RB_Delete_Fixup(T, x)

def RB_Delete_Fixup(T, x):
    while x != T['root'] and x['color'] == 'black':
        if x == x['parent']['left']:
            w = x['parent']['right']
            if w['color'] == 'red':
                w['color'] = 'black'
                x['parent']['color'] = 'red'
                RB_Left_Rotate(T, x['parent'])
                w = x['parent']['right']
            if w['left']['color'] == 'black' and w['right']['color'] == 'black':
                w['color'] = 'red'
                x = x['parent']
            else:
                if w['right']['color'] == 'black':
                    w['left']['color'] = 'black'
                    w['color'] = 'red'
                    RB_Right_Rotate(T, w)
                    w = x['parent']['right']
                w['color'] = x['parent']['color']
                x['parent']['color'] = 'black'
                w['right']['color'] = 'black'
                RB_Left_Rotate(T, x['parent'])
                x = T['root']
        else:
            w = x['parent']['left']
            if w['color'] == 'red':
                w['color'] = 'black'
                x['parent']['color'] = 'red'
                RB_Right_Rotate(T, x['parent'])
                w = x['parent']['left']
            if w['right']['color'] == 'black' and w['left']['color'] == 'black':
                w['color'] = 'red'
                x = x['parent']
            else:
                if w['left']['color'] == 'black':
                    w['right']['color'] = 'black'
                    w['color'] = 'red'
                    RB_Left_Rotate(T, w)
                    w = x['parent']['left']
                w['color'] = x['parent']['color']
                x['parent']['color'] = 'black'
                w['left']['color'] = 'black'
                RB_Right_Rotate(T, x['parent'])
                x = T['root']
    x['color'] = 'black'

def RB_Inorder_Walk(x, T):
    if x != T['NIL']:
        RB_Inorder_Walk(x['left'], T)
        print(x['key'], end=" ")
        RB_Inorder_Walk(x['right'], T)


T = create_rb_tree()
keys = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
nodes = {}
for key in keys:
    node = create_rb_node(key, T)
    RB_Insert(T, node)
    nodes[key] = node

print("Inorder traversal after insertion:")
RB_Inorder_Walk(T['root'], T)
print("\n")

result = RB_Search(T['root'], 13, T)
if result != T['NIL'] and result['key'] is not None:
    print("RB_Search for 13: Found node with key", result['key'])
else:
    print("RB_Search for 13: Not found")
        
result = RB_Search(T['root'], 10, T)
if result != T['NIL'] and result['key'] is not None:
    print("RB_Search for 10: Found node with key", result['key'])
else:
    print("RB_Search for 10: Not found")
        
node_13 = nodes[13]
succ = RB_Successor(node_13, T)
if succ != T['NIL'] and succ['key'] is not None:
    print("RB_Successor of 13:", succ['key'])
else:
    print("RB_Successor of 13: None")
        
pred = RB_Predecessor(node_13, T)
if pred != T['NIL'] and pred['key'] is not None:
    print("RB_Predecessor of 13:", pred['key'])
else:
    print("RB_Predecessor of 13: None")

print("\nDeleting leaf node with key 2")
RB_Delete(T, nodes[2])
print("Inorder traversal after deleting 2:")
RB_Inorder_Walk(T['root'], T)
print("\n")
        
print("Deleting leaf node with key 20")
RB_Delete(T, nodes[20])
print("Inorder traversal after deleting 20:")
RB_Inorder_Walk(T['root'], T)
print("\n")
    
print("Deleting node with two children (key 6)")
RB_Delete(T, nodes[6])
print("Inorder traversal after deleting 6:")
RB_Inorder_Walk(T['root'], T)
print()
