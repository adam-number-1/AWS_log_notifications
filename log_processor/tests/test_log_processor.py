import pytest

from log_processor import (
    error_generator
)

class TestModule:

    # python -m pytest --pdb tests\test_log_processor.py::TestModule::test_error_generator
    a_test_input_1 = {
        "args" : (
            "ERROR:a"
            ,
        ),
        "kwargs": {

        }
    }
    a_expected_output_1 = (
        [
            "ERROR:a"
        ]
    )

    a_test_input_2 = {
        "args" : (
            ""
            ,
        ),
        "kwargs": {

        }
    }
    a_expected_output_2 = (
        []
    )

    a_test_input_3 = {
        "args" : (
            "ERROR:a\nERROR:b\n"
            ,
        ),
        "kwargs": {

        }
    }
    a_expected_output_3 = (
        [
            "ERROR:a",
            "ERROR:b"
        ]
    )
    a_test_input_4 = {
        "args" : (
            "ERROR:a\nDEBUG:d\nERROR:b\n"
            ,
        ),
        "kwargs": {

        }
    }
    a_expected_output_4 = (
        [
            "ERROR:a",
            "ERROR:b"
        ]
    )
    a_test_input_5 = {
        "args" : (
            "ERROR:a\nsome_text\nERROR:b\n"
            ,
        ),
        "kwargs": {

        }
    }
    a_expected_output_5 = (
        [
            "ERROR:a\nsome_text",
            "ERROR:b"
        ]
    )

    @pytest.mark.parametrize(
        "test_input,expected_output",
        [
            (a_test_input_1, a_expected_output_1),
            (a_test_input_2, a_expected_output_2),
            (a_test_input_3, a_expected_output_3),
            (a_test_input_4, a_expected_output_4),
            (a_test_input_5, a_expected_output_5)
        ]
    )
    def test_error_generator(self, test_input, expected_output):
        result = list(
            error_generator(*test_input['args'], **test_input['kwargs'])
        )
        assert result == expected_output