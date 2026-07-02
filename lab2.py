import curses

text = """Hello world!
This is a tiny text editor.
Edit me!"""

cursor = 0


def draw(screen):
    screen.clear()

    # ==========================================================
    # INITIALIZE THE DISPLAY
    #
    # Display the document with the cursor at the current
    # cursor position.
    #
    # Example
    #
    # text    = "Hello"
    # cursor  = 0
    #
    # display = "|Hello"
    #
    # ---------------- TODO ----------------

    display = text[:cursor] + "|" + text[cursor:]

    # ----------------------------------------

    for row, line in enumerate(display.split("\n")):
        screen.addstr(row, 0, line)

    screen.addstr(
        len(display.split("\n")) + 1,
        0,
        "← → Move   Type Insert   Backspace Delete   Enter New Line   Esc Quit",
    )

    screen.refresh()


def main(screen):
    global text, cursor
    screen.keypad(True)
    while True:
        draw(screen)
        key = screen.getch()
        print('hi')
        if key == 27:
            print('hi')
            break

        # ==========================================================
        # LEFT ARROW
        #
        # Move the cursor one position to the left.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hello"
        # cursor  = 2
        # display = "He|llo"
        #
        # ---------------- ANSWER ----------------


        elif key == curses.KEY_LEFT:
            if cursor > 0:
                cursor -= 1

            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------

        # ==========================================================
        # RIGHT ARROW
        #
        # Move the cursor one position to the right.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hello"
        # cursor  = 4
        # display = "Hell|o"
        #
        # ---------------- ANSWER ----------------

        elif key == curses.KEY_RIGHT:
            if cursor < len(text):
                cursor += 1

            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------

        # ==========================================================
        # BACKSPACE
        #
        # Delete the character immediately before the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Helo"
        # cursor  = 2
        # display = "He|lo"
        #
        # ---------------- ANSWER ----------------

        elif key in (8, 127, curses.KEY_BACKSPACE):
            if cursor > 0:
                text = text[:cursor - 1] + text[cursor:]
                cursor -= 1

            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------

        # ==========================================================
        # ENTER
        #
        # Insert a newline at the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hel\nlo"
        # cursor  = 4
        # display = "Hel\n|lo"
        #
        # ---------------- ANSWER ----------------

        elif key == 10:
            text = text[:cursor] + "\n" + text[cursor:]
            cursor += 1

            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------

        # ==========================================================
        # INSERT CHARACTER
        #
        # Insert the typed character at the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # Typing X
        #
        # After
        # text    = "HelXlo"
        # cursor  = 4
        # display = "HelX|lo"
        #
        # ---------------- ANSWER ----------------

        elif 32 <= key <= 126:
            text = text[:cursor] + chr(key) + text[cursor:]
            cursor += 1

            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------

        # BONUS: Can you figure out how to select one line up/down by yourself?

        elif key == curses.KEY_UP:
            text_lines = text.splitlines()
            cursor_dummy = cursor

            # get cursor line
            for i, line in enumerate(text_lines):
                if cursor_dummy <= len(line):
                    cursor_line = i
                    break
                else: 
                    cursor_dummy -= len(line) + 1  
            
            if cursor_line > 0:
                previous_line_len = len(text_lines[cursor_line - 1])
                current_col = cursor_dummy

                if current_col > previous_line_len:
                    cursor -= current_col + 1
                else:
                    cursor -= previous_line_len + 1

                cursor = max(cursor, 0)

            display = text[:cursor] + "|" + text[cursor:]

        elif key == curses.KEY_DOWN:
            text_lines = text.splitlines()
            cursor_dummy = cursor

            # get cursor line
            for i, line in enumerate(text_lines):
                if cursor_dummy <= len(line):
                    cursor_line = i
                    break
                else: 
                    cursor_dummy -= len(line) + 1  
            
            if cursor_line < len(text_lines) - 1:
                next_line_len = len(text_lines[cursor_line + 1])
                current_line_len_start = len(text_lines[cursor_line][:cursor])
                current_line_len_end = len(text_lines[cursor_line][cursor:])

                if current_line_len_end < next_line_len:
                    cursor += current_line_len_end + 1
                else:
                    cursor += len(text_lines[cursor_line]) + 1 + current_line_len_start 

                cursor = max(cursor, 0)

            display = text[:cursor] + "|" + text[cursor:]


curses.wrapper(main)