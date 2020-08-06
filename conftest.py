import json
import pytest

with open("chemicals.json") as file:
    CHEMICALS = json.load(file)


def pytest_generate_tests(metafunc):
    if "chemical" in metafunc.fixturenames:
        metafunc.parametrize(
            "chemical", [chemical["input"] for chemical in CHEMICALS], indirect=True,
        )


@pytest.fixture
def chemical(request):
    for chemical in CHEMICALS:
        if chemical["input"] == request.param:
            return chemical
