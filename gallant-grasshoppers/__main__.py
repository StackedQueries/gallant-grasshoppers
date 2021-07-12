import render as r
# from render.component import Component
import signal
import time

term = r.terminal()

boxer_logo = [".----------------.  .----------------.  .----------------.  .----------------.  .----------------.",
              "| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |",
              "| |   ______     | || |     ____     | || |  ____  ____  | || |  _________   | || |  _______     | |",
              "| |  |_   _ \\    | || |   .'    `.   | || | |_  _||_  _| | || | |_   ___  |  | || | |_   __ \\    | |",
              "| |    | |_) |   | || |  /  .--.  \\  | || |   \\ \\  / /   | || |   | |_  \\_|  | || |   | |__) |   | |",
              "| |    |  __'.   | || |  | |    | |  | || |    > `' <    | || |   |  _|  _   | || |   |  __ /    | |",
              "| |   _| |__) |  | || |  \\  `--'  /  | || |  _/ /'`\\ \\_  | || |  _| |___/ |  | || |  _| |  \\ \\_  | |",
              "| |  |_______/   | || |   `.____.'   | || | |____||____| | || | |_________|  | || | |____| |___| | |",
              "| |              | || |              | || |              | || |              | || |              | |",
              "| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |",
              "'----------------'  '----------------'  '----------------'  '----------------'  '----------------'"]

# def main() -> None:
#    """Starts up main function"""
#    while True:
#        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
#            print(term.home + term.clear + term.move_y(term.height // 2))
#            print(term.black_on_darkkhaki(term.center("hello world")))
#            c = Component(None, 20, 10, 5, 5)
#            c.set_data("Box boys: 15" + str(Component(c, 12, 6, 2, 3, "Buy More?"))
#                       + str(Component(c, 3, 3, 3, 5, ">")))
#            c.draw_component()
#            term.inkey()


def main():  # type () -> None
    """Starts up main function"""
    while True:
        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
            r.start_page.print_start_page()
            signal.signal(signal.SIGWINCH, r.start_page.print_start_page)
            key_press = term.inkey()
        if key_press == " ":
            break


if __name__ == '__main__':
    main()
