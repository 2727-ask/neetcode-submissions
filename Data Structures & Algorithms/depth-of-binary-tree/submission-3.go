/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func dfs(node *TreeNode, val int) int{
	if node == nil {
		return val
	}

	left := dfs(node.Left, val + 1)
	right := dfs(node.Right, val + 1)

	return max(left, right)
}

func maxDepth(root *TreeNode) int {
    return dfs(root, 0)
}
