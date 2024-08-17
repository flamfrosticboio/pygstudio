from loader import load_module

shared = load_module("shared")

def test_passes(monkeypatch):
    responses = ["Yes", "No", "Y", "N", "y", "n", "yiyi", "nononononononono"]
    for item in responses:
        monkeypatch.setattr('builtins.input', lambda _: item)
        response = shared.get_user_choice()
        assert response == item.lower().startswith("y")