# Gerekli kütüphaneler ile PSO ve GA sınıfları ekleniyor
from PSO import PSO
from TestFunc import TestFunc
import matplotlib.pyplot as plt

# DE Default parametreleri
pso = PSO(
    test_func=TestFunc().Sphere(),
    repeat=5,
    maxit=2500,
    npop=50,
    c1=1.4962,
    c2=1.4962,
    w=0.7298,
    wdamp=1.0
)

bestcost = pso.run()
#result = de.run()
#print(gbest['cost'])

# Optimum DE sonuç grafiği çizdiriliyor
plt.semilogy(bestcost)
plt.xlim(0, 2500)
plt.xlabel('İterasyonlar')
plt.ylabel('Maliyet Fonksiyonu')
plt.title('Particle Swarm Optimization (PSO)')
plt.grid(True)
plt.show()

# PSO için maliyet fonksiyonu GA olarak atanıyor
#PSO.CostFunction = gao
# GA parametre aralıkları tanımlanıyor. Sırasıyla:
# pc, gamma, mu, sigma, selectionType
# PSO parametreleri belirleniyor
# c1, c2 [0,5 - 2,5] w = [0,4 -0,9]

