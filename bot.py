
from datetime import date
from pathlib import Path

GAME_NAME = "Tic Tac Toe PRO"

PLAY_STORE_LINK = (
    "https://play.google.com/store/apps/details"
    "?id=com.gnanaswaroop.tictactoepro"
)

posts = [
    """Can you become the Tic Tac Toe PRO champion? 🏆

Challenge your friends or play against the computer!
Try different board sizes and test your strategy.

Play now:
""",
    """Bored? Let's play Tic Tac Toe! 🎮

Enjoy Player vs Player, Player vs Computer
and exciting Ultimate Tic Tac Toe.

Download here:
""",
    """Think you are unbeatable at Tic Tac Toe? 😎

Challenge yourself with different difficulty levels
and discover new themes!

Play Tic Tac Toe PRO:
""",
    """Challenge a friend today! ⚔️

Play Tic Tac Toe PRO with multiple game modes,
fun themes and exciting rewards.

Get the game:
""",
    """Classic Tic Tac Toe, with more challenges! 🔥

Try different boards, unlock themes
and improve your strategy.

Download now:
""",
    """Are you ready for the Ultimate Tic Tac Toe challenge? 🧠

Play against friends or the computer.
Your next challenge is waiting!

Play here:
""",
    """One game. Endless challenges! 🎯

Explore Tic Tac Toe PRO with different modes,
themes and strategic gameplay.

Get started:
"""
]

def generate_post():
    today = date.today()
    post_index = today.toordinal() % len(posts)

    content = posts[post_index]
    final_post = (
        f"{GAME_NAME}\n\n"
        f"{content}\n"
        f"{PLAY_STORE_LINK}\n\n"
        "#TicTacToe #MobileGaming #AndroidGames #PuzzleGame"
    )

    Path("daily_post.txt").write_text(
        final_post,
        encoding="utf-8"
    )

    print("Daily promotion post generated!")
    print(final_post)


if __name__ == "__main__":
    generate_post()
