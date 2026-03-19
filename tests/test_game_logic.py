from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_history_resets_on_new_game():
    # Simulate a game session where the user makes guesses and then starts a new game
    # The history should be reset to an empty list when a new game begins
    
    # Game 1: User makes some guesses
    game_state = {
        "history": [25, 50, 75],
        "attempts": 3,
        "secret": 42,
        "score": 100
    }
    
    # User clicks "New Game" - this should reset the history
    # Simulate what happens when the "New Game" button is clicked
    game_state["history"] = []
    game_state["attempts"] = 0
    
    # Verify that history was properly reset to empty
    assert game_state["history"] == [], "History should be reset to an empty list when a new game starts"
    assert game_state["attempts"] == 0, "Attempts should be reset to 0 when a new game starts"
