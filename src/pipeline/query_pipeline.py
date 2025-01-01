from src.components.data_ingestion import DataIngestion
from src.components.model import GeminiModel
from src.components.embed_model import GeminiEmbedings
from src.components.vector_storage import StorageVectorIndex


def get_query_engine(data):
    dt=DataIngestion()
    model=GeminiModel()
    embeddings=GeminiEmbedings()

    data=dt.load__data(data)
    llm_model=model.load_model()
    llm_embeddings=embeddings.load_embeddings()
    vsi=StorageVectorIndex(model=llm_model,embed_model=llm_embeddings,docs=data)
    index=vsi.get_vector_index()
    query_engine=index.as_query_engine(llm_model)

    return query_engine

    