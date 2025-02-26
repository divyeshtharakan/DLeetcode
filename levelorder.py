class tree:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

def levelorder(root):
	if root==None:
		return
	q=[]
	q.append(root) #address
	while(q): 
		curr=q.pop(0)
		print(curr.data,end=" ")
		if curr.left:
			q.append(curr.left)
		if curr.right:
			q.append(curr.right)

if __name__=='__main__':
	t=tree(5)
	t.left=10
	t.right=20
	t.left.left=30
	t.left.right=40
	levelorder(t)


		
