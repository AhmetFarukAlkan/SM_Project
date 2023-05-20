import random
import matplotlib.pyplot as plt
import math

"""
Boyutları a × b × c olan bir bölge içerisinde toplam N tane cisim vardır (a, b, c ve N kullanıcı parametreleridir).
2.  Yukarıdaki simülasyonu yeniden değerlendirelim. 1. soruda seçilen cisme rastgele yer değiştirme yaptırmak istediğimizde, geçmek istediği konum yakınında dlim kadar ötede başka bir cismin olup olmadığını kontrol edelim.
 Burada dlim bir parametredir. Eğer bu uzaklık içerisinde herhangi bir başka cisim yoksa geçiş tamamlanır. Eğer bu uzaklık içerisinde başka bir cisim varsa geçiş %50 olasılıkla tamamlanır. Bunu gerçekleştirmek için, geçilmek istenen konumdaki en yakın diğer cismin uzaklığı hesaplanır.
 Örneğin dx olsun ve eğer e^(-dx) ≥ R ise geçiş sağlanır. Aksi halde sağlanmaz. Burada R, [0, 1] aralığında rastgele bir sayıdır.
(a) Sistemin dengeye gelip gelmediğini kontrol ediniz.
(b) Cisimler arasındaki ortalama mesafenin zaman ile değişimine bakınız.
(c) Denge durumları üzerinden cisimler arasındaki ortalama mesafeyi bulunuz.
(d) Sistemin denge durumuna ait anlık görüntüler elde ediniz.
(e) Yeni durumlara geçiş oranını elde ediniz ve görüntüleyiniz. Geçiş oranını yaklaşık %65 civarında olması için neler yapabileceğinizi değerlendiriniz, yani çok küçük veya çok yüksek değerler olmaması için.

"""
# Aynı
def calculateDistance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2) ** 0.5

# Aynı
def generateObjects():
    objects = []
    for i in range(N):
        x = random.uniform(0, a)
        y = random.uniform(0, b)
        z = random.uniform(0, c)
        objects.append((x, y, z))
    return objects


def moveObject(obj):
    x, y, z = obj
    new_x = random.uniform(max(x - maxDisplacement, 0), min(x + maxDisplacement, a))
    new_y = random.uniform(max(y - maxDisplacement, 0), min(y + maxDisplacement, b))
    new_z = random.uniform(max(z - maxDisplacement, 0), min(z + maxDisplacement, c))

    #
    for other_obj in objects:
        if other_obj != obj:
            distance = calculateDistance((new_x, new_y, new_z), other_obj)
            if distance <= dLim:
                if random.uniform(0, 1) < 0.5:
                    dx = distance
                    prob = math.exp(-dx)
                    if prob >= R:
                        return new_x, new_y, new_z
                    else:
                        return x, y, z
    #

    return new_x, new_y, new_z

# Aynı
def calculateAvgDistance():
    total_distance = 0
    counter = 0
    for i in range(len(objects)):
        for j in range(i + 1, len(objects)):
            distance = calculateDistance(objects[i], objects[j])
            total_distance += distance
            counter += 1

    return total_distance / counter

# Geçiş oranı hesapla
def calculateTranRate():
    transitions = 0
    for obj in objects:
        new_x, new_y, new_z = moveObject(obj)
        if (new_x, new_y, new_z) != obj:
            transitions += 1
    transitionRate = transitions / N
    transitionRates.append(transitionRate)
#

def simulate():
    global objects, distances, transitionRates
    objects = generateObjects()
    distances = []
    transitionRates = []

    for i in range(T):
        randomObject = random.choice(objects)
        objects.remove(randomObject)
        objects.append(moveObject(randomObject))
        distances.append(calculateAvgDistance())
        # Geçiş Oranı
        calculateTranRate()
        #

# Aynı
def threeD():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xs = [obj[0] for obj in objects]
    ys = [obj[1] for obj in objects]
    zs = [obj[2] for obj in objects]

    ax.scatter(xs, ys, zs)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Aynı
def distanceGraghich():
    plt.plot(range(T), distances)
    plt.xlabel('Adım Sayısı')
    plt.ylabel('Ortalama Mesafe')
    plt.show()

# Geçiş grafik
def tranGraphich():
    plt.plot(range(T), transitionRates)
    plt.xlabel('Adım Sayısı')
    plt.ylabel('Geçiş Oranı')
    plt.ylim(0, 1)
    plt.show()
#

def main():
    global a, b, c, N, maxDisplacement, T, dLim, R
    print("3 boyutlu evrenin büyüklük değerleri:")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    N = int(input("Kaç tane cisim olsun: "))
    maxDisplacement = float(input("Maksimum yer değiştirme miktarı: "))
    T = int(input("Simülasyon adım sayısı: "))

    #
    dLim = float(input("Geçiş kontrol uzaklığı (dlim): "))
    R = random.uniform(0, 1)
    #

    simulate()

    #
    # Sistemin dengeye gelip gelmediği
    fluctuationThreshold = 0.01 #Kabul edilen dalgalanma miktarı
    isStable = abs(distances[-1] - distances[0]) < fluctuationThreshold
    print("Dengeye Geliş:" + str(isStable))
    #

    #

    # # Denge durumları üzerinden cisimler arasındaki ortalama mesafesi
    # averageDistanceInEquilibrium = sum(distances[-100:]) / 100
    # print("Denge durumları üzerinden cisimler arasındaki ortalama mesafesi: " + str(averageDistanceInEquilibrium))
    # #

    threeD()
    distanceGraghich()
    tranGraphich()

    # Geçiş oranının yaklaşık %65 civarında olması için dLim değeri
    desiredTransitionRate = 0.65
    RThreshold = math.log(desiredTransitionRate)
    dLim = -1 * math.log(abs(RThreshold))  # Yeni dLim değeri
    print("Yeni dLim değeri:" + str(dLim))


main()
