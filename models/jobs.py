from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from enum import Enum

class WorkType(str, Enum):
    WFH = "Work from Home"
    WFO = "Work from Office"
    Hybrid = "Hybrid"

class JobType(str, Enum):
    Job = "Full Time"
    Internship = "Internship"

class LevelType(str, Enum):
    junior = "Junior Level"
    mid = "Medium Level"
    senior = "Senior Level"

class Job(BaseModel):
    title: str
    company_id: str
    posted_on: datetime
    work_type: WorkType  # Work from Home, Work from Office, Hybrid
    description: str
    job_type: JobType  # Internship, Full time
    start_date: datetime
    duration: Optional[str] = None  # For internship duration
    salary_or_stipend: Optional[str] = None
    apply_by: datetime
    applicants_count: Optional[int] = None
    skills_required: List[str]
    openings: int
    perks: Optional[List[str]] = None
    conditions: Optional[str] = None