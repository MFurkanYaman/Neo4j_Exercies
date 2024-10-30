from neo4j import GraphDatabase
import nltk

# Gramer Tanımı
grammar_1 = nltk.CFG.fromstring("""
  S -> NP VP
  NP -> Det N
  VP -> V NP
  Det -> 'the' | 'a'
  N -> 'cat' | 'dog'
  V -> 'chased' | 'saw'
""")

# Neo4j veritabanına bağlanma

def connect_Neo4j():
    global driver

    uri = "bolt://localhost:7687"  # URI for the Neo4j database
    user = "neo4j"  # Username
    password = "12345678"  # Password

    driver = GraphDatabase.driver(uri, auth=(user, password))

# Cypher sorgusu çalıştırma fonksiyonu
def run_query(query, parameters=None):
    with driver.session() as session:
        session.run(query, parameters)


def add_grammar_to_neo4j(grammar_1):
    for production in grammar_1.productions():
        # Sol taraf (örneğin: S -> NP VP)
        lhs = str(production.lhs())
          
        # Sağ taraf (örneğin: NP VP)
        rhs = [str(sym) for sym in production.rhs()]
        # Sol taraf için düğüm ekleme
        run_query(
            "MERGE (n:NonTerminal {name: $name})",
            {"name": lhs}
        )

        # Sağ taraf için düğümler ve ilişkiler ekleme
        for symbol in rhs:
            # Her sembol için düğüm ekle
            run_query(
                "MERGE (n:Symbol {name: $name})",
                {"name": symbol}
            )
            
            # Sol taraftan sağ tarafa ilişki ekle
            run_query(
                """
                MATCH (a:NonTerminal {name: $lhs}), (b:Symbol {name: $rhs})
                MERGE (a)-[:PRODUCES]->(b)
                """,
                {"lhs": lhs, "rhs": symbol}
            )



def main():
        # Bağlantıyı kapatma
        driver.close()

        # add_grammar_to_neo4j(grammar_1)
