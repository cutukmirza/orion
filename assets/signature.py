import ast


signature = """"""

def convert_html_to_dash(html_code, dash_modules=None):
    """Convert standard html (as string) to Dash components.

    Looks into the list of dash_modules to find the right component (default to [html, dcc, dbc])."""
    from xml.etree import ElementTree

    if dash_modules is None:
        import dash_html_components as html
        import dash_core_components as dcc

        dash_modules = [html, dcc]
        try:
            import dash_bootstrap_components as dbc

            dash_modules.append(dbc)
        except ImportError:
            pass

    def find_component(name):
        for module in dash_modules:
            try:
                return getattr(module, name)
            except AttributeError:
                pass
        raise AttributeError(f"Could not find a dash widget for '{name}'")

    def parse_css(css):
        """Convert a style in ccs format to dictionary accepted by Dash"""
        return {k: v for style in css.strip(";").split(";") for k, v in [style.split(":")]}

    def parse_value(v):
        try:
            return ast.literal_eval(v)
        except (SyntaxError, ValueError):
            return v

    parsers = {"style": parse_css, "id": lambda x: x}

    def _convert(elem):
        comp = find_component(elem.tag.capitalize())
        children = [_convert(child) for child in elem]
        if not children:
            children = elem.text
        attribs = elem.attrib.copy()
        if "class" in attribs:
            attribs["className"] = attribs.pop("class")
        attribs = {k: parsers.get(k, parse_value)(v) for k, v in attribs.items()}

        return comp(children=children, **attribs)

    et = ElementTree.fromstring(html_code)

    return _convert(et)

print(convert_html_to_dash(signature))