import logging
from chess_engine import game_state
from ai_engine import chess_ai

# Configure logging
logging.basicConfig(filename='chess_log.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def parse_move(move_str):
    col_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    try:
        start_col = col_map[move_str[0]]
        start_row = 8 - int(move_str[1])
        end_col = col_map[move_str[3]]
        end_row = 8 - int(move_str[4])
        return (start_row, start_col), (end_row, end_col)
    except (KeyError, IndexError, ValueError) as e:
        logger.error(f"Error parsing move {move_str}: {e}")
        return None, None


def get_human_move(game_s):
    while True:
        human_move = input("Enter your move (e.g., e2 e4): ")
        start, end = parse_move(human_move)
        if start and end and end in game_s.get_valid_moves(start):
            return start, end
        else:
            print("Invalid move. Try again.")
            logger.warning(f"Invalid move attempted: {human_move}")


def play_game():
    logger.info("Game started.")
    gameState = game_state()
    ai = chess_ai()
    hPlayer = "w"  # Assuming human is white
    aiPlayer = "b"

    while True:
        # Display board (textual representation can be implemented in GameState)
        # game_s.print_board()

        # Human move
        s, e = get_human_move(gameState)
        gameState.move_piece(s, e, False)
        logger.info(f"Player made this move: {s} -> {e}")

        # Check if game is over after human move
        game_over = gameState.checkmate_stalemate_checker()
        if game_over != 3:
            break

        # AI move
        ai_move = ai.minimax_black(gameState, 3, -100000, 100000, True, aiPlayer) if hPlayer == 'w' else ai.minimax_white(gameState, 3, -100000, 100000, True, aiPlayer)
        if ai_move:
            gameState.move_piece(ai_move[0], ai_move[1], True)
            logger.info(f"AI made this move: {ai_move[0]} -> {ai_move[1]}")

        # Check if game is over after AI move
        game_over = gameState.checkmate_stalemate_checker()
        if game_over != 3:
            break

    # Game over handling
    if game_over == 0:
        logger.info("Black wins!")
        print("Black wins!")
    elif game_over == 1:
        logger.info("White wins!")
        print("White wins!")
    elif game_over == 2:
        logger.info("Stalemate!")
        print("Stalemate!")


if __name__ == "__main__":
    play_game()