def preorder(arr, i):
    if i >= len(arr):
        return
    val = arr[i]
    print(val)
    preorder(arr, 2 * i +1)
    preorder(arr, 2 * i + 2)
    return 

def inorder(arr, i):
    if i >= len(arr):
        return
    val = arr[i]
    inorder(arr, 2 * i +1)
    print(val)
    inorder(arr, 2 * i + 2)
    return

def postorder(arr, i):
    if i >= len(arr):
        return
    val = arr[i]
    postorder(arr, 2 * i +1)
    postorder(arr, 2 * i + 2)
    print(val)
    return
