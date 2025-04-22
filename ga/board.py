from PIL import Image, ImageDraw

def draw_chessboard(board, square_size=80, queen_path="assets/queen.png"):
    n = len(board)
    board_img = Image.new("RGB", (n * square_size, n * square_size), color="white")
    draw = ImageDraw.Draw(board_img)

    light = "#f0d9b5"
    dark = "#b58863"
    queen = Image.open(queen_path).convert("RGBA").resize((square_size, square_size))

    for row in range(n):
        for col in range(n):
            x0, y0 = col * square_size, row * square_size
            x1, y1 = x0 + square_size, y0 + square_size
            draw.rectangle([x0, y0, x1, y1], fill=light if (row + col) % 2 == 0 else dark)
            if board[col] == row:
                board_img.paste(queen, (x0, y0), queen)

    return board_img