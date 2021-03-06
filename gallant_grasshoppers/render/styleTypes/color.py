from ..utils.terminal import Terminal


def color(component: object, param: any = None) -> str:
    """Changes colors in component"""
    if not param:
        return ""

    term = Terminal()

    return term.color_rgb(param[0], param[1], param[2])
