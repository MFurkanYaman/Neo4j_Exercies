import pandas as pd
from neo4j import GraphDatabase

def generate_graph(tx,row):

    #Marka -> Üretim Yeri İlişkisi
    tx.run("MERGE (b: Brand {name: $brand_name})"
           "MERGE (m: ManufacturingLocation {name: $manufacturing_location})"
           "MERGE (b)-[:MADEIN]->(m)",
            brand_name=row['brand_name'], manufacturing_location=row['manufacturing_location'] 
    )
    
    #Marka -> Satış Yeri İlişkisi
    tx.run("MERGE (b:Brand {name: $brand_name})"
           "MERGE (s:SalesLocation {name: $sales_location})"
           "MERGE (b)-[:BRAND_SALES_LOCATIONS]->(s)",
           brand_name=row["brand_name"],sales_location=row["sales_location"])
   

    #Ürün -> Marka İlişkisi
    tx.run("MERGE (p:Product {name: $product})"
           "MERGE (b:Brand {name: $brand_name})"
           "MERGE (p)-[:MANUFACTURING]->(b)",
           brand_name=row["brand_name"],product=row["product"])
           
    
    #Ürün -> Satış Yeri İlişkisi
    tx.run("MERGE (p:Product {name: $product})"
           "MERGE (s:SalesLocation {name: $sales_location})"
           "MERGE (p)-[:PRODUCT_SALES_LOCATION]->(s)",
           product=row["product"],sales_location=row["sales_location"])
    
    #Ürün Bilgilerini Düğüm Özellikleri Olarak Ekleme
    tx.run("MATCH (p:Product {name: $product})"
           "SET p.price=$price, p.quantity=$quantity, p.production_year=$production_year",
           product=row['product'], price=row['price'], quantity=row['quantity'], production_year=row['production_year'])

    

def main():
    data=pd.read_csv("product_data.csv")
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "12345678"))  

    with driver.session() as session:
        for index, row in data.iterrows():
            session.execute_write(generate_graph, row) # csv_to_db'ye row değişkenini argüman olarak geçirir
    
main()

