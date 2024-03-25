from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, EmailStr, NaiveDatetime
from pydantic.dataclasses import dataclass

from sat.models.types import CAMPUS_ID


@dataclass
class Clearance:
    name: str
    object_id: int
    guid: str


@dataclass
class Credential:
    card_number: int
    patron_id: int


@dataclass
class StudentPlanInfo:
    academic_career: Optional[str]
    program: Optional[str]
    program_descr: Optional[str]
    plan: Optional[str]
    plan_descr: Optional[str]
    sub_plan: Optional[str]
    sub_plan_descr: Optional[str]
    completion_term: Optional[int]
    enrollment_term: Optional[int]


@dataclass
class EmployeeHistory:
    empl_status: str
    supervisor_id: str
    effective_date: Optional[str]
    classification: Optional[str]
    department_name: Optional[str]
    ouc: Optional[int]


AFFILIATE_TYPES = Enum("AFFILIATE_TYPES", ["Visitor", "Self Pay" "Contractor", "Corp Partner"])


class Person(BaseModel):
    first_name: str
    middle_name: Optional[str]
    last_name: str


class NCSUStudent(Person):
    campus_id: CAMPUS_ID
    email: EmailStr
    active: bool
    plan: Optional[List[StudentPlanInfo]]


class NCSUEmployee(Person):
    campus_id: CAMPUS_ID
    email: EmailStr
    active: bool
    supervisor_id: CAMPUS_ID
    department_id: int
    history: Optional[List[EmployeeHistory]]


class NCSUAffiliate(Person):
    campus_id: CAMPUS_ID
    email: EmailStr
    active: bool
    sponsor_id: CAMPUS_ID
    type: AFFILIATE_TYPES


class CCUREPersonnel(BaseModel):
    campus_id: CAMPUS_ID
    object_id: int
    guid: str
    name: str
    active: bool
    last_modified: NaiveDatetime


class SATPerson(BaseModel):
    employee: Optional[NCSUEmployee]
    student: Optional[NCSUStudent]
    affiliate: Optional[NCSUAffiliate]
    acs: Optional[CCUREPersonnel]
    clearances: Optional[List[Clearance]]
    credentials: Optional[List[Credential]]
