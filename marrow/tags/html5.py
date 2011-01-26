# encoding: utf-8

from marrow.tags import filters
from marrow.tags.base import Tag, Flush, Text


__all__ = ['comment', 'html', 'flush', 'Text']


_doctype = '<!DOCTYPE HTML>\n'
_tags = ['a', 'abbr', 'address', 'area', 'article', 'aside', 'audio', 'b', 'base', 'bdo', 'blockquote', 'body', 'br', 'button', 'canvas', 'caption', 'cite', 'code', 'col', 'colgroup', 'command', 'datalist', 'dd', 'del', 'details', 'dfn', 'div', 'dl', 'dt', 'em', 'embed', 'eventsource', 'fieldset', 'figcaption', 'figure', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hgroup', 'hr', 'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'keygen', 'label', 'legend', 'li', 'link', 'mark', 'map', 'menu', 'meta', 'meter', 'nav', 'noscript', 'object', 'ol', 'optgroup', 'option', 'output', 'p', 'param', 'pre', 'progress', 'q', 'ruby', 'rp', 'rt', 'samp', 'script', 'section', 'select', 'small', 'source', 'span', 'strong', 'style', 'sub', 'summary', 'sup', 'table', 'tbody', 'td', 'textarea', 'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'ul', 'var', 'video', 'wbr']
_partial = ['area', 'base', 'br', 'embed', 'eventsource', 'hr', 'img', 'input', 'link', 'meta', 'param', 'wbr', 'source']
_nowrap = ['title', 'textarea', 'pre', 'label', 'option', 'a', 'legend', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'th', 'td']
_comment = (u'<!--', u'-->')

_attributes = ['accesskey', 'class', 'contenteditable', 'contextmenu', 'dir', 'draggable', 'hidden', 'id', 'lang', 'spellcheck', 'style', 'tabindex', 'title']
_events = ['onabort', 'onblur', 'oncanplay', 'oncanplaythrough', 'onchange', 'onclick', 'oncontextmenu', 'ondblclick', 'ondrag', 'ondragend', 'ondragenter', 'ondragleave', 'ondragover', 'ondragstart', 'ondrop', 'ondurationchange', 'onemptied', 'onended', 'onerror', 'onfocus', 'onformchange', 'onforminput', 'oninput', 'oninvalid', 'onkeydown', 'onkeypress', 'onkeyup', 'onload', 'onloadeddata', 'onloadedmetadata', 'onloadstart', 'onmousedown', 'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel', 'onpause', 'onplay', 'onplaying', 'onprogress', 'onratechange', 'onreadystatechange', 'onscroll', 'onseeked', 'onseeking', 'onselect', 'onshow', 'onstalled', 'onsubmit', 'onsuspend', 'ontimeupdate', 'onvolumechange', 'onwaiting']


flush = Flush()


class comment(Tag):
    def enter(self):
        yield _comment[0]

    def exit(self):
        yield _comment[1]

comment = comment()


html = Tag('html', prefix=_doctype)


_locals = locals()

for t in _tags:
    if t not in _locals:
        _locals[t] = Tag(t, simple=t in _partial, indent=not t in _nowrap)
        __all__.append(t)

for f in filters.__all__:
    _locals[f] = getattr(filters, f)
    __all__.append(f)

del _locals
