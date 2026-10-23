/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func dfs(node *TreeNode) {
	if node == nil {
		return
	}

	temp := node.Left
	node.Left = node.Right
	node.Right = temp

	dfs(node.Left)
	dfs(node.Right)
}


func invertTree(root *TreeNode) *TreeNode {
    dfs(root)
	return root
}
