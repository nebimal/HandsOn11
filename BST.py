def create_node(key):
    return {'key': key, 'left': None, 'right': None, 'parent': None}

def BST_Search(x, k):
    if x is None or x['key'] == k:
        return x
    if k < x['key']:
        return BST_Search(x['left'], k)
    else:
        return BST_Search(x['right'], k)

def BST_Insert(T, z):
    y = None
    x = T['root']
    while x is not None:
        y = x
        if z['key'] < x['key']:
            x = x['left']
        else:
            x = x['right']
    z['parent'] = y
    if y is None:
        T['root'] = z 
    elif z['key'] < y['key']:
        y['left'] = z
    else:
        y['right'] = z

def BST_Minimum(x):
    while x['left'] is not None:
        x = x['left']
    return x

def BST_Maximum(x):
    while x['right'] is not None:
        x = x['right']
    return x

def BST_Transplant(T, u, v):
    if u['parent'] is None:
        T['root'] = v
    elif u == u['parent']['left']:
        u['parent']['left'] = v
    else:
        u['parent']['right'] = v
    if v is not None:
        v['parent'] = u['parent']

def BST_Delete(T, z):
    if z['left'] is None:
        BST_Transplant(T, z, z['right'])
    elif z['right'] is None:
        BST_Transplant(T, z, z['left'])
    else:
        y = BST_Minimum(z['right'])
        if y['parent'] != z:
            BST_Transplant(T, y, y['right'])
            y['right'] = z['right']
            if y['right'] is not None:
                y['right']['parent'] = y
        BST_Transplant(T, z, y)
        y['left'] = z['left']
        if y['left'] is not None:
            y['left']['parent'] = y

def BST_Successor(x):
    if x['right'] is not None:
        return BST_Minimum(x['right'])
    y = x['parent']
    while y is not None and x == y['right']:
        x = y
        y = y['parent']
    return y

def BST_Predecessor(x):
    if x['left'] is not None:
        return BST_Maximum(x['left'])
    y = x['parent']
    while y is not None and x == y['left']:
        x = y
        y = y['parent']
    return y

def BST_Inorder_Walk(x):
    if x is not None:
        BST_Inorder_Walk(x['left'])
        print(x['key'], end=" ")
        BST_Inorder_Walk(x['right'])


T = {'root': None}
keys = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
   
nodes = {}
for key in keys:
        node = create_node(key)
        BST_Insert(T, node)
        nodes[key] = node

print("Inorder traversal after insertion:")
BST_Inorder_Walk(T['root'])
print("\n")

result = BST_Search(T['root'], 13)
if result is not None:
    print("BST_Search for 13: Found node with key", result['key'])
else:
    print("BST_Search for 13: Not found")
    
result = BST_Search(T['root'], 10)
if result is not None:
    print("BST_Search for 10: Found node with key", result['key'])
else:
    print("BST_Search for 10: Not found")
    
node_13 = nodes[13]
succ = BST_Successor(node_13)
if succ:
    print("BST_Successor of 13:", succ['key'])
else:
    print("BST_Successor of 13: None")
    
pred = BST_Predecessor(node_13)
if pred:
    print("BST_Predecessor of 13:", pred['key'])
else:
    print("BST_Predecessor of 13: None")
    
print("\nDeleting leaf node with key 2")
BST_Delete(T, nodes[2])
print("Inorder traversal after deleting 2:")
BST_Inorder_Walk(T['root'])
print("\n")
    
print("Deleting leaf node with key 20")
BST_Delete(T, nodes[20])
print("Inorder traversal after deleting 20:")
BST_Inorder_Walk(T['root'])
print("\n")

print("Deleting node with two children (key 6)")
BST_Delete(T, nodes[6])
print("Inorder traversal after deleting 6:")
BST_Inorder_Walk(T['root'])
print()