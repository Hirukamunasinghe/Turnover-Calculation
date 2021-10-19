b_inventory = int(input("How much is the begenning inventory? "))
e_inventory = int(input("How mcuh is the ending inventory? "))
cost_of_goods_sold = int(input("How much is the cost of goods sold? "))
avg_inventory = (b_inventory + e_inventory) / 2
turnover = cost_of_goods_sold / avg_inventory
print(f"The turnover value is {turnover}" )
