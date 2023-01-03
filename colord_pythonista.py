import sys
from typing import Union


ANSI_COLOR_EXT = [
    (0, 0, 0),
    (0, 0, 128),
    (0, 128, 0),
    (0, 128, 128),
    (128, 0, 0),
    (128, 0, 128),
    (128, 128, 0),
    (192, 192, 192),
    (128, 128, 128),
    (0, 0, 255),
    (0, 255, 0),
    (0, 255, 255),
    (255, 0, 0),
    (255, 0, 255),
    (255, 255, 0),
    (255, 255, 255),
    (0, 0, 0),
    (95, 0, 0),
    (135, 0, 0),
    (175, 0, 0),
    (215, 0, 0),
    (255, 0, 0),
    (0, 95, 0),
    (95, 95, 0),
    (135, 95, 0),
    (175, 95, 0),
    (215, 95, 0),
    (255, 95, 0),
    (0, 135, 0),
    (95, 135, 0),
    (135, 135, 0),
    (175, 135, 0),
    (215, 135, 0),
    (255, 135, 0),
    (0, 175, 0),
    (95, 175, 0),
    (135, 175, 0),
    (175, 175, 0),
    (215, 175, 0),
    (255, 175, 0),
    (0, 215, 0),
    (95, 215, 0),
    (135, 215, 0),
    (175, 215, 0),
    (215, 215, 0),
    (255, 215, 0),
    (0, 255, 0),
    (95, 255, 0),
    (135, 255, 0),
    (175, 255, 0),
    (215, 255, 0),
    (255, 255, 0),
    (0, 0, 95),
    (95, 0, 95),
    (135, 0, 95),
    (175, 0, 95),
    (215, 0, 95),
    (255, 0, 95),
    (0, 95, 95),
    (95, 95, 95),
    (135, 95, 95),
    (175, 95, 95),
    (215, 95, 95),
    (255, 95, 95),
    (0, 135, 95),
    (95, 135, 95),
    (135, 135, 95),
    (175, 135, 95),
    (215, 135, 95),
    (255, 135, 95),
    (0, 175, 95),
    (95, 175, 95),
    (135, 175, 95),
    (175, 175, 95),
    (215, 175, 95),
    (255, 175, 95),
    (0, 215, 95),
    (95, 215, 95),
    (135, 215, 95),
    (175, 215, 95),
    (215, 215, 95),
    (255, 215, 95),
    (0, 255, 95),
    (95, 255, 95),
    (135, 255, 95),
    (175, 255, 95),
    (215, 255, 95),
    (255, 255, 95),
    (0, 0, 135),
    (95, 0, 135),
    (135, 0, 135),
    (175, 0, 135),
    (215, 0, 135),
    (255, 0, 135),
    (0, 95, 135),
    (95, 95, 135),
    (135, 95, 135),
    (175, 95, 135),
    (215, 95, 135),
    (255, 95, 135),
    (0, 135, 135),
    (95, 135, 135),
    (135, 135, 135),
    (175, 135, 135),
    (215, 135, 135),
    (255, 135, 135),
    (0, 175, 135),
    (95, 175, 135),
    (135, 175, 135),
    (175, 175, 135),
    (215, 175, 135),
    (255, 175, 135),
    (0, 215, 135),
    (95, 215, 135),
    (135, 215, 135),
    (175, 215, 135),
    (215, 215, 135),
    (255, 215, 135),
    (0, 255, 135),
    (95, 255, 135),
    (135, 255, 135),
    (175, 255, 135),
    (215, 255, 135),
    (255, 255, 135),
    (0, 0, 175),
    (95, 0, 175),
    (135, 0, 175),
    (175, 0, 175),
    (215, 0, 175),
    (255, 0, 175),
    (0, 95, 175),
    (95, 95, 175),
    (135, 95, 175),
    (175, 95, 175),
    (215, 95, 175),
    (255, 95, 175),
    (0, 135, 175),
    (95, 135, 175),
    (135, 135, 175),
    (175, 135, 175),
    (215, 135, 175),
    (255, 135, 175),
    (0, 175, 175),
    (95, 175, 175),
    (135, 175, 175),
    (175, 175, 175),
    (215, 175, 175),
    (255, 175, 175),
    (0, 215, 175),
    (95, 215, 175),
    (135, 215, 175),
    (175, 215, 175),
    (215, 215, 175),
    (255, 215, 175),
    (0, 255, 175),
    (95, 255, 175),
    (135, 255, 175),
    (175, 255, 175),
    (215, 255, 175),
    (255, 255, 175),
    (0, 0, 215),
    (95, 0, 215),
    (135, 0, 215),
    (175, 0, 215),
    (215, 0, 215),
    (255, 0, 215),
    (0, 95, 215),
    (95, 95, 215),
    (135, 95, 215),
    (175, 95, 215),
    (215, 95, 215),
    (255, 95, 215),
    (0, 135, 215),
    (95, 135, 215),
    (135, 135, 215),
    (175, 135, 215),
    (215, 135, 215),
    (255, 135, 215),
    (0, 175, 223),
    (95, 175, 223),
    (135, 175, 223),
    (175, 175, 223),
    (223, 175, 223),
    (255, 175, 223),
    (0, 223, 223),
    (95, 223, 223),
    (135, 223, 223),
    (175, 223, 223),
    (223, 223, 223),
    (255, 223, 223),
    (0, 255, 223),
    (95, 255, 223),
    (135, 255, 223),
    (175, 255, 223),
    (223, 255, 223),
    (255, 255, 223),
    (0, 0, 255),
    (95, 0, 255),
    (135, 0, 255),
    (175, 0, 255),
    (223, 0, 255),
    (255, 0, 255),
    (0, 95, 255),
    (95, 95, 255),
    (135, 95, 255),
    (175, 95, 255),
    (223, 95, 255),
    (255, 95, 255),
    (0, 135, 255),
    (95, 135, 255),
    (135, 135, 255),
    (175, 135, 255),
    (223, 135, 255),
    (255, 135, 255),
    (0, 175, 255),
    (95, 175, 255),
    (135, 175, 255),
    (175, 175, 255),
    (223, 175, 255),
    (255, 175, 255),
    (0, 223, 255),
    (95, 223, 255),
    (135, 223, 255),
    (175, 223, 255),
    (223, 223, 255),
    (255, 223, 255),
    (0, 255, 255),
    (95, 255, 255),
    (135, 255, 255),
    (175, 255, 255),
    (223, 255, 255),
    (255, 255, 255),
    (8, 8, 8),
    (18, 18, 18),
    (28, 28, 28),
    (38, 38, 38),
    (48, 48, 48),
    (58, 58, 58),
    (68, 68, 68),
    (78, 78, 78),
    (88, 88, 88),
    (98, 98, 98),
    (108, 108, 108),
    (118, 118, 118),
    (128, 128, 128),
    (138, 138, 138),
    (148, 148, 148),
    (158, 158, 158),
    (168, 168, 168),
    (178, 178, 178),
    (188, 188, 188),
    (198, 198, 198),
    (208, 208, 208),
    (218, 218, 218),
    (228, 228, 228),
    (238, 238, 238),
]

ANSI_COLOR = {
    0: (),
    30: (0.1, 0.1, 0.1),
    31: (0., 0., 0.),
    32: (0., 0., 0.),
    33: (0., 0., 0.),
    34: (0., 0., 0.),
    35: (0., 0., 0.),
    36: (0., 0., 0.),
    37: (0., 0., 0.),
}


def setup():
    try:
        import console
        import builtins
        # bltinprt = builtins.print

        def replace_ansi_escape_and_stdout_write(text: str):
            try:
                index = text.index('\033')
                sys.stdout.write(str(text[:index]))
                index += 1
                num = ''
                for c in text[index:]:
                    index += 1
                    if c == 'm':
                        break
                    num += c
                
                try:
                    num = int(num)
                    console.set_color(*ANSI_COLOR[num])
                except ValueError:
                    args = num.split(';')  # type: ignore
                    if len(args) == 3:
                        console.set_color(*list(map(lambda x: x / 255, ANSI_COLOR_EXT[int(args[2])])))
                    else:
                        console.set_color(int(args[2]) / 255,
                                          int(args[3]) / 255,
                                          int(args[4]) / 255)

                replace_ansi_escape_and_stdout_write(text[index:])
            except ValueError:
                sys.stdout.write(str(text))

        def print2(*values: object, sep: Union[str, None] = None, end: Union[str, None] = None,
                   file=None, flush=True):
            for v in values:
                sys.stdout.write(str(v))
                if file is not None:
                    file.write(str(v))
                if sep is not None:
                    sys.stdout.write(sep)
                    if file is not None:
                        file.write(sep)
            if end is None:
                sys.stdout.write('\n')
                if file is not None:
                    file.write('\n')
            else:
                sys.stdout.write(end)
                if file is not None:
                    file.write(end)
            if flush:
                sys.stdout.flush()
        
        builtins.print = print2
    except ModuleNotFoundError:
        pass

if __name__ == "__main__":
    setup()