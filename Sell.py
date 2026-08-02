class Solutions:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit


prices = [4, 1, 5, 6, 7, 8]

obj = Solutions()
print(obj.maxProfit(prices))