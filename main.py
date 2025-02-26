import numpy as np
import scipy.stats as stats

# Данные о росте спортсменов в разных группах
football_players = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey_players = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

# Проверка на нормальность распределения (Тест Шапиро-Уилка)
shapiro_football = stats.shapiro(football_players)
shapiro_hockey = stats.shapiro(hockey_players)
shapiro_weightlifters = stats.shapiro(weightlifters)

# Проверка гомогенности дисперсий (Тест Левена)
levene_test = stats.levene(football_players, hockey_players, weightlifters)

# Проведение однофакторного дисперсионного анализа ANOVA
anova_test = stats.f_oneway(football_players, hockey_players, weightlifters)

# Вывод результатов
print(f"Тест Шапиро-Уилка (футболисты): p-value = {shapiro_football.pvalue:.4f}")
print(f"Тест Шапиро-Уилка (хоккеисты): p-value = {shapiro_hockey.pvalue:.4f}")
print(f"Тест Шапиро-Уилка (штангисты): p-value = {shapiro_weightlifters.pvalue:.4f}")
print(f"Тест Левена (гомогенность дисперсий): p-value = {levene_test.pvalue:.4f}")
print(f"ANOVA: F-статистика = {anova_test.statistic:.4f}, p-value = {anova_test.pvalue:.4f}")

# Определение наличия статистически значимых различий
alpha = 0.05
if anova_test.pvalue < alpha:
    print("Есть статистически значимые различия в среднем росте между группами.")
else:
    print("Нет статистически значимых различий в среднем росте между группами.")
