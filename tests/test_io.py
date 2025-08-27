import io, runpy, sys, yaml, pathlib

STUDENT = "student.py"
SUITE = pathlib.Path("suite.yaml")

def run_student(stdin_text: str) -> list[str]:
    old_in, old_out = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = io.StringIO(stdin_text), io.StringIO()
    try:
        runpy.run_path(STUDENT, run_name="__main__")
        return sys.stdout.getvalue().rstrip("\n").splitlines()
    finally:
        sys.stdin, sys.stdout = old_in, old_out

def test_suite():
    data = yaml.safe_load(SUITE.read_text(encoding="utf-8"))
    cases = data.get("cases", data)
    assert isinstance(cases, list) and cases, "suite.yaml sem casos válidos"

    for i, case in enumerate(cases, 1):
        name = case.get("name", f"case{i}")
        stdin_text = case["stdin"]
        expected = case["expected_stdout"].rstrip("\n").splitlines()
        out = run_student(stdin_text)
        assert out == expected, (
            f"\n{name} falhou.\n--- ESPERADO ---\n" +
            "\n".join(expected) +
            "\n--- OBTIDO -----\n" +
            "\n".join(out) + "\n"
        )
