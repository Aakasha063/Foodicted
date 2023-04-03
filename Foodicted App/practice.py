import csv 
with open('food_data.csv') as fr:
            r = csv.reader(fr)
            foodId = 0
            for i in r:
                if len(i) > 0:
                    foodId = i[0]


# print(row['Food_ID'],row['Name'],row['Quantity'],row['Price'],row['Discount'],row['Stock'])

# rows=   [rows for row in reader if row['Food_ID'] == foodid, row[value] = new_value]
                
                    