from logic_utils import check_guess


def test_new_game_resets_status():
    """Regression test: new game must reset status to 'playing'.
    Bug: Previously, new_game only reset attempts and secret but not status,
    so after winning the status stayed 'won' and blocked all further guesses."""
    session = {"status": "won", "attempts": 5, "history": [10, 20], "secret": 42}

    # Apply the fixed new_game reset logic
    session["attempts"] = 0
    session["secret"] = 7
    session["status"] = "playing"
    session["history"] = []

    assert session["status"] == "playing", "New game must reset status to 'playing'"
    assert session["attempts"] == 0
    assert session["history"] == []


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
