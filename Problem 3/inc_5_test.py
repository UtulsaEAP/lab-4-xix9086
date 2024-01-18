'''
Test cases for the inc_5 module.
'''
import inc_5 as inc_5
RANGE_ERRROR = "The range of integers should be inclusive."
DOMAIN_ERROR = "The second integer should be greater than the first."
class TestClass:
    def test_one(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["-15","10"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        inc_5.inc_5()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "-15 -10 -5 0 5 10" in all_outputs ,RANGE_ERRROR

    def test_two(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["20","5"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        inc_5.inc_5()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Second integer can't be less than the first." in all_outputs , DOMAIN_ERROR

    def test_three(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["10","15"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        inc_5.inc_5()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "10 15" in all_outputs ,RANGE_ERRROR

    def test_four(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["5","14"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        inc_5.inc_5()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "5 10" in all_outputs ,RANGE_ERRROR

    def test_five(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["4","4"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        inc_5.inc_5()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "4" in all_outputs ,RANGE_ERRROR
    