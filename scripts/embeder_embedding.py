"""
使用嵌入模型更新节点嵌入属性
使用的环境: embed
"""

from neo4j import GraphDatabase
from llm.Embedder import Embed_v2
from tqdm import tqdm

# Neo4j数据库连接信息
URL = "bolt://59.77.5.106:7687"
USERNAME = 'neo4j'
PASSWORD = 'risk-trade-short-catalog-gram-4746'

# 初始化Neo4j驱动
driver = GraphDatabase.driver(URL, auth=(USERNAME, PASSWORD))
embedder = Embed_v2()

def update_embeddings(tx, nodes_batch):
    """更新节点的嵌入属性。

    Args:
        tx: Neo4j事务对象。
        nodes_batch: 节点记录的批次。
    """
    node_names = [record['name'] for record in nodes_batch]
    node_embeddings = embedder(node_names)

    for record, embedding in zip(nodes_batch, node_embeddings):
        node_id = record['nodeId']
        sentence_embedding = embedding.tolist()[0]

        update_query = (
            "MATCH (n) WHERE id(n) = $nodeId "
            "SET n.embedding = $embedding"
        )
        tx.run(update_query, nodeId=node_id, embedding=sentence_embedding)

def update_in_batches(batch_size):
    """分批更新节点嵌入。

    Args:
        batch_size: 每批处理的节点数量。
    """
    with driver.session() as session:
        # 获取所有需要更新嵌入的节点
        query = """
            MATCH (n) 
            WHERE n.embedding IS NULL 
            RETURN id(n) AS nodeId, n.name AS name
        """
        nodes = session.run(query).data()

        # 批量更新节点嵌入
        for i in range(0, len(nodes), batch_size):
            batch = nodes[i:i + batch_size]
            session.write_transaction(update_embeddings, nodes_batch=batch)

if __name__ == '__main__':
    update_in_batches(10)