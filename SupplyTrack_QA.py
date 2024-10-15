from neo4j import GraphDatabase

uri = "neo4j://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "12345678")) 
session = driver.session()

# 1) Tüm markaları listele.
"""
result=(session.run("MATCH (b:Brand) RETURN b.name AS brand_name"))
for record in result:
    print(record["brand_name"])
"""

# 2) Bir marka hangi üretim yerinde üretiliyor ?
"""
result=session.run("MATCH (b:Brand)-[:MADEIN]->(m:ManufacturingLocation) RETURN b.name, m.name ")
for record in result:
    print(f"Brand: {record['b.name']} -> Manufacturing Location: {record['m.name']}")
"""

# 3) Üretim yeri 'Montana' olan tüm markaları listele.
"""
result=session.run("MATCH (b:Brand)-[:MADEIN]->(m:ManufacturingLocation {name: 'Montana'}) Return b.name")
for record in result:
    print(f"Montana's Brand: {record['b.name']} ")
"""


# 4) Fiyatı 6000’den fazla olan ürünleri listele.
"""
result=session.run("MATCH (p:Product) WHERE p.price > 6000 RETURN p.name,p.price ")
for record in result:
    print(f"{record['p.name']}'s price {record['p.price']} ")
"""

# 5)  New York City satış yerinde hangi markalar satış yapıyor?

"""
result=session.run("MATCH (b:Brand)-[:BRAND_SALES_LOCATIONS]->(s:SalesLocation) WHERE s.name='New York City' RETURN b.name")
for record in result:
    print(f" New York City's sale brands: {record['b.name']} ")
"""
# 6) Massachusetts'de  üretilen tüm ürünler nelerdir?
"""
result = session.run("MATCH (b:Brand)-[:MADEIN]->(m:ManufacturingLocation) WHERE m.name='Massachusetts' RETURN b.name, m.name") 
for record in result:
    print(f"Brand: {record['b.name']}, Manufacturing Location: {record['m.name']}") ??????
"""

# 7) Her markanın kaç farklı satış yerinde bulunduğunu sorgula.
"""
result = session.run(" MATCH (b:Brand)-[:BRAND_SALES_LOCATIONS]->(s:SalesLocation) RETURN b.name AS brand_name, COUNT(s) AS sales_location_count")

for record in result:
    print(f"Brand: {record['brand_name']}, Sales Locations Count: {record['sales_location_count']}")
"""

# 8) En çok ürün hangi marka tarafından üretiliyor?

"""
result = session.run("
    MATCH (p:Product)-[:MANUFACTURING]->(b:Brand)
    RETURN b.name AS brand_name, COUNT(p) AS product_count
    ORDER BY product_count DESC
    LIMIT 1
")

for record in result:
    print(f"En çok ürün üreten marka: {record['brand_name']}, Ürün sayısı: {record['product_count']}")
"""

#9) Bir ürünü kaç farklı firma üretiyor?
"""
result = session.run( "MATCH (p:Product)-[:MANUFACTURING]->(b:Brand) RETURN p.name AS product_name, COUNT(DISTINCT b) AS brand_count ORDER BY brand_count DESC ")
for record in result:
    print(f" Product: {record['product_name']}, Brand Count: {record['brand_count']}")
"""

# 10) Her satış noktasında satılan toplam ürün sayısı nedir?
"""
result=session.run("MATCH (p:Product)-[:PRODUCT_SALES_LOCATION]->(s:SalesLocation) RETURN s.name AS location, SUM(p.quantity)  as product_count ORDER BY product_count")
for record in result:
    print(f" Sales Location: {record['location']}, Product Count: {record['product_count']}")

# 10) Bir markanın ürünleri aracılığıyla dolaylı olarak bağlı olduğu satış yerlerini bul.
"""


# 11) Markası Steuber LLC  ve üretim  yeri 'Wisconsin' olan ürünleri bul.
"""
result = session.run("
    MATCH (p:Product)-[:MANUFACTURING]->(b:Brand),
    (b)-[:MADEIN]->(m:ManufacturingLocation)
    WHERE m.name = 'Wisconsin' AND b.name = 'Steuber LLC'
    RETURN p.name AS p_name
")

for record in result:
    print(f"Ürün: {record['p_name']}")
"""

# 13) Aynı satış yerinde bulunan diğer markaları öner.
"""
result = session.run("
    MATCH (p:Product)-[:PRODUCT_SALES_LOCATION]->(s:SalesLocation)
    WITH s.name AS sales_location, COLLECT(DISTINCT p.name) AS products
    RETURN sales_location, products
")

for record in result:
    print(f"Sales Location: {record['sales_location']} - Products: {', '.join(record['products'])}")
"""

# 14) Bir markanın satış yaptığı bir yeri güncelle 
""""
result = session.run("
    MATCH (b:Brand {name: 'Zulauf and Sons'})-[r:BRAND_SALES_LOCATIONS]->(s:SalesLocation {name: 'North Las Vegas'})
    DELETE r
    WITH b
    MERGE (new_location:SalesLocation {name: 'Ankara'})  
    MERGE (b)-[:BRAND_SALES_LOCATIONS]->(new_location)
")

# Ankara'da satılan markaları kontrol etme
kontrol = session.run("MATCH (b:Brand)-[:BRAND_SALES_LOCATIONS]->(s:SalesLocation) WHERE s.name='Ankara' RETURN b.name")

# Sonuçları yazdırma
for record in kontrol:
    print(f"The brand selling products in Ankara: {record['b.name']}")
"""

# 15) Belirli bir markaya yeni bir satış noktası ekle ve bunu sorgula.
"""
result=session.run("MERGE (b:Brand {name: $brand_name})"
                   "MERGE (s:SalesLocation {name: $sales_location})"
                   "MERGE (b)-[:BRAND_SALES_LOCATIONS]->(s)",
                   brand_name="Zulauf and Sons",sales_location="Bursa")

"""

