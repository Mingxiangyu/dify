import logging
import time

from core.rag.datasource.retrieval_service import RetrievalService
from core.rag.models.document import Document
from core.rag.retrieval.retrival_methods import RetrievalMethod
from extensions.ext_database import db
from models.account import Account
from models.dataset import Dataset, DatasetQuery, DocumentSegment

default_retrieval_model = {
    'search_method': RetrievalMethod.SEMANTIC_SEARCH.value,
    'reranking_enable': False,
    'reranking_model': {
        'reranking_provider_name': '',
        'reranking_model_name': ''
    },
    'top_k': 2,
    'score_threshold_enabled': False
}


class HitTestingService:
    @classmethod
    def retrieve(cls, dataset: Dataset, query: str, account: Account, retrieval_model: dict, limit: int = 10) -> dict:
        if dataset.available_document_count == 0 or dataset.available_segment_count == 0:
            return {
                "query": {
                    "content": query,
                    "tsne_position": {'x': 0, 'y': 0},
                },
                "records": []
            }

        start = time.perf_counter()

        # get retrieval model , if the model is not setting , using default
        # 获取 检索 模型(如果模型未设置)，使用 默认设置
        if not retrieval_model:
            retrieval_model = dataset.retrieval_model if dataset.retrieval_model else default_retrieval_model

        all_documents = RetrievalService.retrieve(retrival_method=retrieval_model.get('search_method', 'semantic_search'),# 从retrieval_model字典中获取的search_method键对应的值（默认为semantic_search）作为参数
                                                  dataset_id=dataset.id,
                                                  query=cls.escape_query_for_search(query),
                                                  top_k=retrieval_model.get('top_k', 2),
                                                  score_threshold=retrieval_model.get('score_threshold', .0)
                                                  if retrieval_model['score_threshold_enabled'] else None,
                                                  reranking_model=retrieval_model.get('reranking_model', None)
                                                  if retrieval_model['reranking_enable'] else None,
                                                  reranking_mode=retrieval_model.get('reranking_mode')
                                                  if retrieval_model.get('reranking_mode') else 'reranking_model',
                                                  weights=retrieval_model.get('weights', None),
                                                  )

        end = time.perf_counter()
        logging.debug(f"Hit testing retrieve in {end - start:0.4f} seconds")

        dataset_query = DatasetQuery(
            dataset_id=dataset.id,
            content=query,
            source='hit_testing',
            created_by_role='account',
            created_by=account.id
        )

        db.session.add(dataset_query)
        db.session.commit()

        return cls.compact_retrieve_response(dataset, query, all_documents)

    @classmethod
    def compact_retrieve_response(cls, dataset: Dataset, query: str, documents: list[Document]):
        i = 0
        records = []
        for document in documents:
            index_node_id = document.metadata['doc_id']

            segment = db.session.query(DocumentSegment).filter(
                DocumentSegment.dataset_id == dataset.id,
                DocumentSegment.enabled == True,
                DocumentSegment.status == 'completed',
                DocumentSegment.index_node_id == index_node_id
            ).first()

            if not segment:
                i += 1
                continue

            record = {
                "segment": segment,
                "score": document.metadata.get('score', None),
            }

            records.append(record)

            i += 1

        return {
            "query": {
                "content": query,
            },
            "records": records
        }

    @classmethod
    def hit_testing_args_check(cls, args):
        query = args['query']

        if not query or len(query) > 250:
            raise ValueError('Query is required and cannot exceed 250 characters')

    @staticmethod
    def escape_query_for_search(query: str) -> str:
        return query.replace('"', '\\"')
