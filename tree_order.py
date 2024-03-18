def preorder(root):
	if root is None:
		return
	print(root)
	preorder(root.left)
	preorder(root.right)
	
def inorder(root):
	if root is None:
		return
	inorder(root.left)
	print(root)
	inorder(root.right)
	
def postorder(root):
	if root is None:
		return
	postorder(root.left)
	postorder(root.right)
	print(root)