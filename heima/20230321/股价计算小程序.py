name = "腾讯"
stock_price = 11.1
stock_code = "13123"
stock_price_daily_growth_factor = 1.2
growth_days = 30

print(f"公司：{name},  股票代码：{stock_code},当前股价：{stock_price},每日增长系数{stock_price_daily_growth_factor},经过{growth_days}增长,股票达到了{stock_price*stock_price_daily_growth_factor*growth_days}")