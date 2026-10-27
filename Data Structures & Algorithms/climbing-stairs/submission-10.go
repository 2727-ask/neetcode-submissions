func climbStairs(n int) int {

	if n <= 2 {
		return n
	}

	first := 1
	second := 2

	jump := 0
	for i:=2; i<n; i++ {
		jump = first + second
		first = second
		second = jump
	}
	return jump
}
