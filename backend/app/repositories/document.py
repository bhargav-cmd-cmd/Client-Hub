from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentBase
from app.repositories.base import BaseRepository

class DocumentRepository(BaseRepository[Document, DocumentCreate, DocumentBase]):
    pass

document_repo = DocumentRepository(Document)
