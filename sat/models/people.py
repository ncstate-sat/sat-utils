from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, EmailStr, NaiveDatetime
from pydantic.dataclasses import dataclass

from sat.models.types import CAMPUS_ID


class Clearance(BaseModel):
    name: str
    object_id: int
    guid: str


class Credential(BaseModel):
    card_number: int
    patron_id: int


class StudentPlanInfo(BaseModel):
    academic_career: Optional[str] = ""
    program: Optional[str] = ""
    program_descr: Optional[str] = ""
    plan: Optional[str] = ""
    plan_descr: Optional[str] = ""
    sub_plan: Optional[str] = ""
    sub_plan_descr: Optional[str] = ""
    completion_term: Optional[int] = int()
    enrollment_term: Optional[int] = int()


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
    middle_name: Optional[str] = ""
    last_name: str


class NCSUPerson(Person):
    campus_id: CAMPUS_ID
    email: EmailStr
    active: bool


class NCSUStudent(NCSUPerson):
    plan: Optional[List[StudentPlanInfo]] = list()


class NCSUEmployee(NCSUPerson):
    supervisor_id: CAMPUS_ID
    department_id: int
    history: Optional[List[EmployeeHistory]] = list()


class NCSUAffiliate(Person):
    email: EmailStr
    active: bool
    sponsor_email: EmailStr
    type: AFFILIATE_TYPES


class CCUREPersonnel(BaseModel):
    campus_id: CAMPUS_ID
    object_id: int
    guid: str
    name: str
    active: bool
    last_modified: NaiveDatetime


class SATPerson(BaseModel):
    employee: Optional[NCSUEmployee] = dict()
    student: Optional[NCSUStudent] = dict()
    affiliate: Optional[NCSUAffiliate] = dict()
    acs: Optional[CCUREPersonnel] = dict()
    clearances: Optional[List[Clearance]] = list()
    credentials: Optional[List[Credential]] = list()