import statsmodels.api as sm

# Группа A
total_A = 21  # Общее количество участников в группе A
converted_A = 7  # Количество участников, купивших продукт в группе A

# Группа B
total_B = 79  # Общее количество участников в группе B
converted_B = 13  # Количество участников, купивших продукт в группе B

# Расчет пропорций
prop_A = converted_A / total_A
prop_B = converted_B / total_B

# Расчет статистической значимости разницы пропорций
zscore, pvalue = sm.stats.proportions_ztest([converted_A, converted_B], [total_A, total_B])

# Вывод результатов
print(f"Группа A: {converted_A}/{total_A} ({prop_A:.2%})")
print(f"Группа B: {converted_B}/{total_B} ({prop_B:.2%})")
print(f"p-значение: {pvalue:.4f}")
if pvalue < 0.05:
    print("Статистически значимая разница между группами A и B")
else:
    print("Нет статистически значимой разницы между группами A и B")
