/*
 * @lc app=leetcode id=121 lang=golang
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
func maxProfit(prices []int) int {

	var (
		buy        int = prices[0]
		mostProfit int = 0
	)

	for _, price := range prices[1:] {
		potentialProfit := price - buy
		mostProfit = max(potentialProfit, mostProfit)
		buy = min(price, buy)
	}

	return mostProfit
}

// @lc code=end

