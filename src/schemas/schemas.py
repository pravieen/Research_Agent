from typing import Optional, List, TypeVar

from pydantic import BaseModel, Field

T = TypeVar('T')

class AppError(BaseModel):
    """ Used when to throw the error in the api response"""
    code: str = Field(description="Error Code")
    message: T = Field(description="Error Message")

class AppFault(BaseModel):
    """ Used when to construct in the api response."""
    label: str = 'RESEARCH-AGENT'
    field: str = 'RESEARCH-AGENT'
    validator: str = 'Simple'
    errors: Optional[list[AppError]] = []

class ResearchRequest(BaseModel):
    query: str
    max_results: Optional[int]

class PaperResponse(BaseModel):
    title: str
    summary: str
    url: str
    pdf_url: Optional[str]
    published: str
    authors: List[str]

class ResearchResponse(BaseModel):
    papers: List[PaperResponse]
    summaries: List[str]
    synthesis: str