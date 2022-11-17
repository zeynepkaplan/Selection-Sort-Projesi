# Soru:[22,27,16,2,18,6] -> Insertion Sort

# Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

# Big-O gösterimini yazınız.

# Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız

# 1.Average case: Aradığımız sayının ortada olması
# 2.Worst case: Aradığımız sayının sonda olması
# 3.Best case: Aradığımız sayının dizinin en başında olması.

# [22 , 27 , 16 , 2 , 18 , 6]
# [22 | 27 , 16 , 2 , 18 , 6]
# [22 , 27 | 16 , 2 , 18 ,6]
# [16 , 22 , 27 | 2 , 18, 6]
# [2 , 16 , 22 , 27 | 18, 6]
# [2 , 16 , 18 , 22, 27 | 6]
# [2 , 6 , 16 , 18 , 22 , 27 |]

# Dizideki eleman sayısına n dersek ilk aşamada n elemanı inceleyip en küçüğünü başa yazarız. İkinci aşamada kalan (n-1)
# elemanı inceler onlar arasındaki en küçüğü 2. sıraya yazarız , üçüncü aşamada (n-2) derken 1 elemana varana kadar bu
# şekilde ilerleriz.

# n + (n-1) + (n-2) + ... + 1 bu işlemi kısaca (n * (n + 1)) / 2 = (n^2 * n) / 2 şeklinde formüle edebiliriz.
# Big-O notasyonunda fonksiyonu domine eden kısmı alırız bu nedenle Big-O gösterimi O(n^2) şeklindedir.

# Dizi sırasına göre 18 sayısı 4. indekstedir bu nedenle Average Case'e girer.

[Patika.Dev](www.patika.dev)
