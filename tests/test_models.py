import pytest
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
    def _clearance(multiple: list[dict] = None):
        if multiple:
            return [Clearance(**item) for item in multiple]
        else:
            return Clearance(
                name="John Doe",
                object_id=1234,
                guid="12345678-1234-1234-1234-123456789012",
            )

    return _clearance


@pytest.fixture
def credential():
    def _credential(multiple: list[dict] = None):
        if multiple:
            return [Credential(**item) for item in multiple]
        else:
            return Credential(
                card_number=1234567890,
                patron_id=1234567890,
            )

    return _credential


@pytest.fixture
def student_plan_info():
    def _student_plan_info(multiple: list[dict] = None):
        if multiple:
            return [StudentPlanInfo(**item) for item in multiple]
        else:
            return StudentPlanInfo(
                academic_career="UG",
                program="CSC",
                program_descr="Computer Science",
                plan="BS",
                plan_descr="Bachelor of Science",
                sub_plan="CSC",
                sub_plan_descr="Computer Science",
                completion_term=202305,
                enrollment_term=202108,
            )

    return _student_plan_info


@pytest.fixture
def employee_history():
    def _employee_history(multiple: list[dict] = None):
        if multiple:
            return [EmployeeHistory(**item) for item in multiple]
        else:
            return EmployeeHistory(
                empl_status="A",
                supervisor_id="123456789",
                effective_date="2021-08-01",
                classification="EHRA",
                department_name="Information Technology",
                ouc=1234,
            )

    return _employee_history


@pytest.fixture
def student():
    def _ncsu_student(multiple: list[dict] = None):
        if multiple:
            return [NCSUStudent(**item) for item in multiple]
        else:
            return NCSUStudent(
                first_name="John",
                middle_name="Q",
                last_name="Public",
                campus_id="123456789",
                email="jqpublic@example.com",
                active=True,
            )

    return _ncsu_student


@pytest.fixture
def employee():
    def _ncsu_employee(multiple: list[dict] = None):
        if multiple:
            return [NCSUEmployee(**item) for item in multiple]
        else:
            return NCSUEmployee(
                first_name="Jane",
                last_name="Doe",
                campus_id="987654321",
                email="jdoe@example.com",
                supervisor_id="123456789",
                active=True,
                department_id=1234,
            )

    return _ncsu_employee


@pytest.fixture
def affiliate():
    def _ncsu_affiliate(multiple: list[dict] = None):
        if multiple:
            return [NCSUAffiliate(**item) for item in multiple]
        else:
            return NCSUAffiliate(
                first_name="Jack",
                last_name="Smith",
                campus_id="123456789",
                email="jsmith@example.com",
                sponsor_email="jdoe@example.com",
                type=AFFILIATE_TYPES.Visitor,
                active=True,
            )

    return _ncsu_affiliate


@pytest.fixture
def ccure_personnel():
    def _ccure_personnel(multiple: list[dict] = None):
        if multiple:
            return [CCUREPersonnel(**item) for item in multiple]
        else:
            return CCUREPersonnel(
                campus_id="123456789",
                object_id=1234,
                guid="12345678-1234-1234-1234-123456789012",
                name="John Doe",
                active=True,
                last_modified="2021-08-01T12:00:00",
            )

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
