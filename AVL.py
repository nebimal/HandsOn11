def create_avl_tree():
    return {'root': None}

def create_avl_node(key):
    return {'key': key, 'left': None, 'right': None, 'height': 1, 'parent': None}

def get_height(node):
    if node is None:
        return 0
    return node['height']

def update_height(node):
    node['height'] = 1 + max(get_height(node['left']), get_height(node['right']))

def get_balance(node):
    if node is None:
        return 0
    return get_height(node['left']) - get_height(node['right'])

def AVL_Left_Rotate(x):
    y = x['right']
    T2 = y['left']
    
    y['left'] = x
    x['right'] = T2
    
    if T2 is not None:
        T2['parent'] = x
    y['parent'] = x['parent']
    x['parent'] = y
    
    update_height(x)
    update_height(y)
    return y

def AVL_Right_Rotate(y):
    x = y['left']
    T2 = x['right']
    
    x['right'] = y
    y['left'] = T2
    
    if T2 is not None:
        T2['parent'] = y
    x['parent'] = y['parent']
    y['parent'] = x
    
    update_height(y)
    update_height(x)
    return x

def AVL_Insert_Node(node, z):
    if node is None:
        return z
    if z['key'] < node['key']:
        node['left'] = AVL_Insert_Node(node['left'], z)
        node['left']['parent'] = node
    else:
        node['right'] = AVL_Insert_Node(node['right'], z)
        node['right']['parent'] = node

    update_height(node)
    balance = get_balance(node)

    if balance > 1 and z['key'] < node['left']['key']:
        return AVL_Right_Rotate(node)
    if balance < -1 and z['key'] > node['right']['key']:
        return AVL_Left_Rotate(node)
    if balance > 1 and z['key'] > node['left']['key']:
        node['left'] = AVL_Left_Rotate(node['left'])
        node['left']['parent'] = node
        return AVL_Right_Rotate(node)
    if balance < -1 and z['key'] < node['right']['key']:
        node['right'] = AVL_Right_Rotate(node['right'])
        node['right']['parent'] = node
        return AVL_Left_Rotate(node)
    
    return node

def AVL_Insert(T, z):
    T['root'] = AVL_Insert_Node(T['root'], z)
    if T['root'] is not None:
        T['root']['parent'] = None

def AVL_Search(node, k):
    if node is None or node['key'] == k:
        return node
    if k < node['key']:
        return AVL_Search(node['left'], k)
    else:
        return AVL_Search(node['right'], k)

def AVL_Minimum(node):
    current = node
    while current and current['left'] is not None:
        current = current['left']
    return current

def AVL_Successor(x):
    if x['right'] is not None:
        return AVL_Minimum(x['right'])
    y = x['parent']
    while y is not None and x == y['right']:
        x = y
        y = y['parent']
    return y

def AVL_Predecessor(x):
    if x['left'] is not None:
        current = x['left']
        while current['right'] is not None:
            current = current['right']
        return current
    y = x['parent']
    while y is not None and x == y['left']:
        x = y
        y = y['parent']
    return y

def AVL_Delete_Node(node, key):
    if node is None:
        return node
    if key < node['key']:
        node['left'] = AVL_Delete_Node(node['left'], key)
        if node['left'] is not None:
            node['left']['parent'] = node
    elif key > node['key']:
        node['right'] = AVL_Delete_Node(node['right'], key)
        if node['right'] is not None:
            node['right']['parent'] = node
    else:
        if node['left'] is None:
            temp = node['right']
            node = None
            return temp
        elif node['right'] is None:
            temp = node['left']
            node = None
            return temp
        temp = AVL_Minimum(node['right'])
        node['key'] = temp['key']
        node['right'] = AVL_Delete_Node(node['right'], temp['key'])
        if node['right'] is not None:
            node['right']['parent'] = node
    
    if node is None:
        return node

    update_height(node)
    balance = get_balance(node)

    if balance > 1 and get_balance(node['left']) >= 0:
        return AVL_Right_Rotate(node)
    if balance > 1 and get_balance(node['left']) < 0:
        node['left'] = AVL_Left_Rotate(node['left'])
        if node['left'] is not None:
            node['left']['parent'] = node
        return AVL_Right_Rotate(node)
    if balance < -1 and get_balance(node['right']) <= 0:
        return AVL_Left_Rotate(node)
    if balance < -1 and get_balance(node['right']) > 0:
        node['right'] = AVL_Right_Rotate(node['right'])
        if node['right'] is not None:
            node['right']['parent'] = node
        return AVL_Left_Rotate(node)

    return node

def AVL_Delete(T, key):
    T['root'] = AVL_Delete_Node(T['root'], key)
    if T['root'] is not None:
        T['root']['parent'] = None

def AVL_Inorder_Walk(node):
    if node is not None:
        AVL_Inorder_Walk(node['left'])
        print(node['key'], end=" ")
        AVL_Inorder_Walk(node['right'])

T = create_avl_tree()
keys = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
nodes = {}
for key in keys:
    node = create_avl_node(key)
    AVL_Insert(T, node)
    nodes[key] = node

print("Inorder traversal after insertion:")
AVL_Inorder_Walk(T['root'])
print("\n")

result = AVL_Search(T['root'], 13)
if result is not None:
    print("AVL_Search for 13: Found node with key", result['key'])
else:
    print("AVL_Search for 13: Not found")

result = AVL_Search(T['root'], 10)
if result is not None:
    print("AVL_Search for 10: Found node with key", result['key'])
else:
    print("AVL_Search for 10: Not found")

node_13 = nodes[13]
succ = AVL_Successor(node_13)
if succ is not None:
    print("AVL_Successor of 13:", succ['key'])
else:
    print("AVL_Successor of 13: None")

pred = AVL_Predecessor(node_13)
if pred is not None:
    print("AVL_Predecessor of 13:", pred['key'])
else:
    print("AVL_Predecessor of 13: None")

print("\nDeleting leaf node with key 2")
AVL_Delete(T, 2)
print("Inorder traversal after deleting 2:")
AVL_Inorder_Walk(T['root'])
print("\n")

print("Deleting leaf node with key 20")
AVL_Delete(T, 20)
print("Inorder traversal after deleting 20:")
AVL_Inorder_Walk(T['root'])
print("\n")

print("Deleting node with two children (key 6)")
AVL_Delete(T, 6)
print("Inorder traversal after deleting 6:")
AVL_Inorder_Walk(T['root'])
print()
