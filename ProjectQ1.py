import random
import matplotlib.pyplot as plt

"""
Boyutları a × b × c olan bir bölge içerisinde toplam N tane cisim vardır (a, b, c ve N kullanıcı parametreleridir).
1.	(a) a, b, c ve N parametrelerini elde ediniz.
(b) N tane cismi bu bölge içerisinde rastgele olarak dağıtınız.
(c) Sistemin anlık görüntüsünü elde ediniz.
(d) Cisimler arasındaki ortalama mesafeyi elde ediniz.
(e) Cisimlerden birini rastgele seçiniz, bu cismin konumunu rastgele değiştiriniz (3D olacak şekilde). (Burada maksimum yer değiştirme miktarını tanımlayınız). Cisimlerden biri, bu bölgenin bir kenarından dışarı çıkması durumunda cismin diğer kenardan içeri giriyor olduğunu sağlayınız (bakınız ödev2).
(f) Bir önceki adımı T defa tekrarlayınız. Burada T simülasyon adım miktarı olup girdi parametresi olmasını sağlayınız.
(g) Cisimler arasındaki ortalama mesafenin zaman ile değişimini görüntüleyiniz.
(h) Sistemin dengeye gelip gelmediğini kontrol ediniz. Simülasyonun başından itibaren örneğin cisimler arasındaki mesafelerin ortalamasına bakınız, burada dalgalanmaların azaldığı anı dengeye ulaşma anı olarak tanımlayabilirsiniz.
(i) Denge durumları üzerinden cisimler arasındaki ortalama mesafeyi okuyunuz.
(j) Cisimler arasındaki mesafe için bir histogram yapınız.
(k) Sistemin anlık görüntüsünü elde ediniz.

Yukarıdaki simülasyonda konumu değiştirilen cisimin yeni konumuna herhangi bir kabul kriteri olmadan taşındığını not ediniz. Yani simülasyonda yeni konumların kabul edilme olasılığı %100'dür.
"""

def calculateDistance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2) ** 0.5

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
    return new_x, new_y, new_z

def calculateAvgDistance():
    total_distance = 0
    counter = 0
    for i in range(len(objects)):
        for j in range(i + 1, len(objects)):

            distance = calculateDistance(objects[i], objects[j])
            total_distance += distance
            counter += 1

    return total_distance / counter

def simulate():
    global objects, distances
    objects = generateObjects()
    distances = []

    for i in range(T):
        randomObject = random.choice(objects)
        objects.remove(randomObject)
        objects.append(moveObject(randomObject))
        distances.append(calculateAvgDistance())

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

def distanceGraghich():
    plt.plot(range(T), distances)
    plt.xlabel('Adım Sayısı')
    plt.ylabel('Ortalama Mesafe')
    plt.show()

def main():
    global a, b, c, N, maxDisplacement, T
    print("3 boyutlu evrenin büyüklük değerleri:")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    N = int(input("Kaç tane cisim olsun: "))
    maxDisplacement = float(input("Maksimum yer değiştirme miktarı: "))
    T = int(input("Simülasyon adım sayısı: "))
    simulate()
    threeD()
    distanceGraghich()



main()
