from pyspark import SparkConf, SparkContext

word = 'this is letter for john, which described is'.split()
word1 = 'this is a time for the cate'.split()
int1 = [1, 2, 3, 4, 5, 6, 7]
int2 = [2, 3, 4, 56, 7, 8, 9]

sf = SparkConf().setMaster('spark://10.2.0.74:7077').setAppName("WordCount")
sc = SparkContext(conf=sf)

rdd = sc.parallelize(word)
rdd1 = sc.parallelize(word1)
rdd2 = sc.parallelize(int1)
rdd3 =sc.parallelize(int2)

# print(rdd.first())
# print(rdd2.reduce(lambda x,y: (x+y)))
# print(rdd.distinct().collect())
# def map1(x):
#     if x == 'is':
#         return None
#     return x
#
# for w in  rdd.map(map1).collect():
#     print(w)
# print(rdd.flatMap(lambda x: (x, len(x))).collect())
# print(rdd.map(lambda x: (x, len(x))).collect())
# print(rdd.filter(lambda x: (x != 'is')).collect())
# print(rdd.union(rdd2).collect())
# print(rdd.intersection(rdd1).collect())
# print(rdd.subtract(rdd1).collect())
# print(rdd.count())
# print(rdd.cartesian(rdd1).collect())
# print(rdd.countByValue())
# print(rdd.reduce(lambda x, y: (x + y)))



sc.stop()

