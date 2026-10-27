

func rob(nums []int) int {
	dp := make(map[int]int)
    return dfs(0, nums, dp)
}


func dfs(i int, nums [] int, dp map[int]int) int {
	val, exist := dp[i]
	
	if exist {
		return val
	}

	if (i >= len(nums)) {
		return 0
	}

	skip := dfs(i+1, nums, dp)
	rob := nums[i] + dfs(i+2, nums, dp)

	ans := max(skip, rob)

	dp[i] = ans
	return ans
}
