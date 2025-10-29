import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Функция для расчёта коэффициента диффузии (упрощённая, с коррекцией для ногтя)
def calculate_diffusivity(MW, logP):
    # Базовый D как для кожи, но с коррекцией для ногтя (снижение на 2 порядка)
    D_base = 1e-8 * np.exp(-0.46 * np.sqrt(MW)) * np.exp(0.28 * logP)
    D_nail = D_base * 0.01  # Коррекция для плотной структуры ногтя
    return D_nail


# Функция для коэффициента распределения (K = 10^logP)
def calculate_partition(logP):
    K = 10 ** logP
    return K


# Модель проникновения (аналогично Францу для ногтей)
def nail_penetration_model(Q, t, P, A, V_d, C_d):
    dQdt = P * A * (C_d - Q / V_d)  # Учитываем уменьшение концентрации в доноре
    return dQdt


# Параметры для ногтей
A = 1.0  # Площадь, см²
h = 0.05  # Толщина ногтя, см (0.5 мм)
V_d = 1.0  # Объём донора, мл
C_d = 1.0  # Концентрация, мг/мл

# Вещества (те же свойства)
# (молекулярная масса MW, коэффициент распределения logP, растворимость Sol)
#  D = 10^-8 * exp(0.46*MW^0.5)*exp(0.28 *logP) - коэффициент диффузии
# P = D * K - где Р- проницаемость K - коэффициент распределения

substances = {
    'TPO': {'MW': 316, 'logP': 3.5, 'Sol': 0.1},
    # 'Ethyl Acetate': {'MW': 88, 'logP': 0.73, 'Sol': 1000},
    # 'Propyl Acetate': {'MW': 102, 'logP': 1.24, 'Sol': 500},
    # 'Isopropyl Alcohol': {'MW': 60, 'logP': 0.05, 'Sol': 1000}
}

# Время (часы)
t = np.linspace(0, 24, 25)

# Симуляция
plt.figure(figsize=(10, 6))
results = {}

for name, props in substances.items():
    MW = props['MW']
    logP = props['logP']
    Sol = props['Sol']

    # Расчёт D и P
    D = calculate_diffusivity(MW, logP)
    K = calculate_partition(logP)
    P = D * K / h

    # Коррекция на растворимость
    if Sol < 1:
        P *= Sol / 1.0

    # Решение (начальное Q0 = 1e-6, чтобы избежать log(0))
    Q0 = 1e-6
    Q = odeint(nail_penetration_model, Q0, t, args=(P, A, V_d, C_d))

    # Перевод в мкг/см²
    Q_mcg_cm2 = Q * 1000 / A

    results[name] = {'P': P, 'Q_final': Q_mcg_cm2[-1][0]}

    # График (semilogy для лог-шкалы)
    plt.semilogy(t, Q_mcg_cm2, label=f'{name} (P={P:.2e} cm/s)')

plt.xlabel('Время (часы)')
plt.ylabel('Накопленное количество (мкг/см², лог-шкала)')
plt.title('Модель проникновения через ногти (по Францу, с лог-шкалой)')
plt.legend()
plt.grid(True)

plt.show()

# Вывод результатов
for name, res in results.items():
    print(
        f'{name}: Коэффициент проницаемости P = {res["P"]:.2e} cm/s, Итоговое накопление = {res["Q_final"]:.2e} мкг/см²')

