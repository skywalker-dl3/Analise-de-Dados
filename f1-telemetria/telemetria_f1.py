import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt

# Estilo visual
plotting.setup_mpl()

print("Buscando dados da F1... Pode demorar um pouco na primeira vez!")

# GP do Bahrein 2023 - Qualificação
session = fastf1.get_session(2023, 'Bahrain', 'Q')
session.load()

# Comparando Verstappen e Leclerc
v_lap = session.laps.pick_driver('VER').pick_fastest()
l_lap = session.laps.pick_driver('LEC').pick_fastest()

v_tel = v_lap.get_car_data().add_distance()
l_tel = l_lap.get_car_data().add_distance()

plt.figure(figsize=(10, 5))
plt.plot(v_tel['Distance'], v_tel['Speed'], color='blue', label='Verstappen')
plt.plot(l_tel['Distance'], l_tel['Speed'], color='red', label='Leclerc')

plt.title('Duelo de Velocidade: Red Bull vs Ferrari')
plt.xlabel('Distância (m)')
plt.ylabel('Velocidade (km/h)')
plt.legend()
plt.grid(True)

print("Abrindo o gráfico...")
plt.show()
