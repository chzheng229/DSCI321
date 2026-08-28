from student_code import robot_navigation

def test_path_validity():
    assert robot_navigation(["a","b","c","h","z"]) == (10, "z")

def test_input_validity():
    assert robot_navigation(["a","t","f"]) == -1

def test_target_reaching():
    assert robot_navigation(["a", "b", "c", "e"]) == (0, "e")

def test_cyclical():
    assert robot_navigation(["a","d","f","e","d"]) == -2




