#1.Пользователь вводит данные о количестве предприятий, 
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) и 
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

factories = {}
n = int(input( "Qunatity of factories: " ))

s_annual_profit = 0.00
for i in range(n):
    sfactory_name = input("Factory Name #"+str(i+1)+":")
    try :
        year_profit = str(input("Factory Name "+sfactory_name+", profits for each quarter per year divided by space: " ))  
        arr_quaters_profit = year_profit.split()
        f_average_profit = (float(arr_quaters_profit[0])+float(arr_quaters_profit[1])+float(arr_quaters_profit[2])+float(arr_quaters_profit[3]))/4
        print("Average quarter profit for factory", sfactory_name,": ",f_average_profit) 
        factories[sfactory_name] = f_average_profit 
        s_annual_profit += f_average_profit
        print("Average", s_annual_profit)  
    except OSError as e:             
        print('It should be four integer or float numbers for profits divided by spaces! Error:', e.strerror)
        break

avrg = float(s_annual_profit / n)
print("Average profit for all factories - ", avrg)

print( "\nFactories with profits above of average:")
for i in factories:
    if factories[i] > avrg:
        print(i)

print( "\nFactories with profits below of average:")
for i in factories:
    if factories[i] < avrg:
        print(i)