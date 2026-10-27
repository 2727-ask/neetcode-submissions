




func rob(nums []int) int {

	if len(nums) == 1 {
		return nums[0]
	}

	dp := make(map[int]int)

	first := dfs(0, nums[:len(nums)-1], dp)

	dp = make(map[int]int)

	second := dfs(1, nums, dp)

    return max(first, second)
}


func dfs(i int, nums []int, dp map[int]int) int {

	val, exist := dp[i]
	if exist {
		return val
	}

	if i >= len(nums) {
		return 0
	}

	skip := dfs(i + 1, nums, dp)
	rob := nums[i] + dfs(i + 2, nums, dp)

	ans := max(skip, rob)

	dp[i] = ans

	return ans
}