import pytest
from pydantic import ValidationError
from sat.models.people import (
    AFFILIATE_TYPES,
    CCUREPersonnel,
    Clearance,
    Credential,
    EmployeeHistory,
    NCSUAffiliate,
    NCSUEmployee,
    NCSUStudent,
    SATPerson,
    StudentPlanInfo,
)


@pytest.fixture
def clearance():
    def _clearance(multiple: int = None):
        clearance = {
            "name": "John Doe",
            "object_id": 1234,
            "guid": "12345678-1234-1234-1234-123456789012",
        }
        if multiple:
            return [Clearance(**clearance) for _ in range(multiple)]
        else:
            return Clearance(**clearance)

    return _clearance


@pytest.fixture
def credential():
    def _credential(multiple: int = None):
        credential = {
            "card_number": 1234567890,
            "patron_id": 1234567890,
        }
        if multiple:
            return [Credential(**credential) for _ in range(multiple)]
        else:
            return Credential(**credential)

    return _credential


@pytest.fixture
def student_plan_info():
    def _student_plan_info(multiple: int = None):
        st_plan = {
            "academic_career": "UG",
            "program": "CSC",
            "program_descr": "Computer Science",
            "plan": "BS",
            "plan_descr": "Bachelor of Science",
            "sub_plan": "CSC",
            "sub_plan_descr": "Computer Science",
            "completion_term": 202305,
            "enrollment_term": 202108,
        }
        if multiple:
            return [StudentPlanInfo(**st_plan) for _ in range(multiple)]
        else:
            return StudentPlanInfo(**st_plan)

    return _student_plan_info


@pytest.fixture
def employee_history():
    def _employee_history(multiple: int = None):
        emp_history = {
            "empl_status": "A",
            "supervisor_id": "123456789",
            "effective_date": "2021-08-01",
            "classification": "EHRA",
            "department_name": "Information Technology",
            "ouc": 1234,
        }
        if multiple:
            return [EmployeeHistory(**emp_history) for _ in range(multiple)]
        else:
            return EmployeeHistory(**emp_history)

    return _employee_history


@pytest.fixture
def student():
    def _ncsu_student(multiple: int = None):
        student = {
            "first_name": "John",
            "middle_name": "Q",
            "last_name": "Public",
            "campus_id": "123456789",
            "email": "jqpublic@example.com",
            "active": True,
        }
        if multiple:
            return [NCSUStudent(**student) for _ in range(multiple)]
        else:
            return NCSUStudent(**student)

    return _ncsu_student


@pytest.fixture
def employee():
    def _ncsu_employee(multiple: int = None):
        employee = {
            "first_name": "Jane",
            "last_name": "Doe",
            "campus_id": "987654321",
            "email": "jdoe@example.com",
            "supervisor_id": "123456789",
            "active": True,
            "department_id": "1234",
        }
        if multiple:
            return [NCSUEmployee(**employee) for _ in range(multiple)]
        else:
            return NCSUEmployee(**employee)

    return _ncsu_employee


@pytest.fixture
def affiliate():
    def _ncsu_affiliate(multiple: int = None):
        affiliate = {
            "first_name": "Jack",
            "last_name": "Smith",
            "campus_id": "123456789",
            "email": "jdoe@example.com",
            "sponsor_email": "jdoe@example.com",
            "type": AFFILIATE_TYPES.Visitor,
            "active": True,
        }
        if multiple:
            return [NCSUAffiliate(**affiliate) for _ in range(multiple)]
        else:
            return NCSUAffiliate(**affiliate)

    return _ncsu_affiliate


@pytest.fixture
def ccure_personnel():
    def _ccure_personnel(multiple: int = None):
        ccure_personnel = {
            "campus_id": "123456789",
            "object_id": 1234,
            "guid": "12345678-1234-1234-1234-123456789012",
            "name": "John Doe",
            "active": True,
            "last_modified": "2021-08-01T12:00:00",
        }
        if multiple:
            return [CCUREPersonnel(**ccure_personnel) for _ in range(multiple)]
        else:
            return CCUREPersonnel(**ccure_personnel)

    return _ccure_personnel


def test_sat_person():
    expected = {
        "employee": {},
        "student": {},
        "affiliate": {},
        "acs": {},
        "clearances": [],
        "credentials": [],
    }
    sat_person = SATPerson()
    assert sat_person.model_dump() == expected


def test_sat_person_employee(employee):
    employee = employee()
    expected = {
        "employee": employee.model_dump(),
        "student": {},
        "affiliate": {},
        "acs": {},
        "clearances": [],
        "credentials": [],
    }
    sat_person = SATPerson(employee=employee)
    assert sat_person.model_dump() == expected


def test_sat_person_student(student):
    student = student()
    expected = {
        "employee": {},
        "student": student.model_dump(),
        "affiliate": {},
        "acs": {},
        "clearances": [],
        "credentials": [],
    }
    sat_person = SATPerson(student=student)
    assert sat_person.model_dump() == expected


def test_sat_person_affiliate(affiliate):
    affiliate = affiliate()
    expected = {
        "employee": {},
        "student": {},
        "affiliate": affiliate.model_dump(),
        "acs": {},
        "clearances": [],
        "credentials": [],
    }
    sat_person = SATPerson(affiliate=affiliate)
    assert sat_person.model_dump() == expected


def test_sat_person_acs(ccure_personnel):
    ccure_personnel = ccure_personnel()
    expected = {
        "employee": {},
        "student": {},
        "affiliate": {},
        "acs": ccure_personnel.model_dump(),
        "clearances": [],
        "credentials": [],
    }
    sat_person = SATPerson(acs=ccure_personnel)
    assert sat_person.model_dump() == expected


def test_sat_person_acs_no_campus_id(ccure_personnel):
    ccure_personnel = ccure_personnel().model_dump()
    del ccure_personnel["campus_id"]
    new_personnel = CCUREPersonnel(**ccure_personnel)
    expected = {
        "employee": {},
        "student": {},
        "affiliate": {},
        "acs": new_personnel.model_dump(),
        "clearances": [],
        "credentials": [],
    }
    sat_person = SATPerson(acs=new_personnel)
    assert sat_person.model_dump() == expected


def test_sat_person_clearances(clearance):
    clearances = clearance()
    expected = {
        "employee": {},
        "student": {},
        "affiliate": {},
        "acs": {},
        "clearances": [clearances.model_dump()],
        "credentials": [],
    }
    sat_person = SATPerson(clearances=[clearances])
    assert sat_person.model_dump() == expected


def test_sat_person_multiple_clearances(clearance):
    clearances = clearance(multiple=3)
    expected = {
        "employee": {},
        "student": {},
        "affiliate": {},
        "acs": {},
        "clearances": [c.model_dump() for c in clearances],
        "credentials": [],
    }
    sat_person = SATPerson(clearances=clearances)
    assert sat_person.model_dump() == expected


def test_sat_person_credentials(credential):
    credentials = credential()
    expected = {
        "employee": {},
        "student": {},
        "affiliate": {},
        "acs": {},
        "clearances": [],
        "credentials": [credentials.model_dump()],
    }
    sat_person = SATPerson(credentials=[credentials])
    assert sat_person.model_dump() == expected


def test_sat_person_multiple_credentials(credential):
    credentials = credential(multiple=3)
    expected = {
        "employee": {},
        "student": {},
        "affiliate": {},
        "acs": {},
        "clearances": [],
        "credentials": [c.model_dump() for c in credentials],
    }
    sat_person = SATPerson(credentials=credentials)
    assert sat_person.model_dump() == expected


def test_sat_person_add_clearance(clearance):
    clearance1 = clearance()
    clearance2 = clearance()
    sat_person = SATPerson(clearances=[clearance1])
    sat_person.add_clearance(clearance2)
    assert len(sat_person.clearances) == 2


def test_sat_person_add_credential(credential):
    credential1 = credential()
    credential2 = credential()
    sat_person = SATPerson(credentials=[credential1])
    sat_person.add_credential(credential2)
    assert len(sat_person.credentials) == 2


def test_sat_person_invalid():
    with pytest.raises(ValidationError):
        SATPerson(employee=[1, 2, 3])


def test_campus_id_validation_not_int():
    with pytest.raises(ValidationError, match="Campus ID must be a parsable number"):
        NCSUStudent(
            first_name="John",
            last_name="Public",
            campus_id="12345678a",
            email="jp@example.com",
            active=True,
        )


def test_campus_id_validation_greater_9_chars():
    with pytest.raises(ValidationError, match="Campus ID must be 9 characters long"):
        NCSUStudent(
            first_name="John",
            last_name="Public",
            campus_id="12345678746",
            email="jp@example.com",
            active=True,
        )


def test_campus_id_validation_less_than_9_chars():
    with pytest.raises(ValidationError, match="Campus ID must be 9 characters long"):
        NCSUStudent(
            first_name="John",
            last_name="Public",
            campus_id="123456",
            email="jp@example.com",
            active=True,
        )
