from django.template import RequestContext
from django.template.loader import get_template
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
from paste.tools import cache_exists, cache_fetch, cache_store


def render_pygments(request, paste, data):
    """Renders Pygments template."""
    key = paste.slug+'_pygments.cache'
    if cache_exists(key):
        highlighted_content = cache_fetch(key)
    else:
        lexer = get_lexer_by_name(paste.language.slug)
        formatter = get_formatter_by_name('html')
        highlighted_content = highlight(paste.content, lexer, formatter)
        cache_store(key, highlighted_content)
    data['paste'] = paste
    data['highlighted'] = highlighted_content
    context = RequestContext(request, data)
    return get_template('paste/show-pygments.html').render(context)


def render_form(request, paste, data):
    """Renders Form template."""
    data['paste'] = paste
    context = RequestContext(request, data)
    return get_template('paste/show-form.html').render(context)


def render_raw(request, paste, data):
    """Renders RAW content."""
    data['paste'] = paste
    context = RequestContext(request, data)
    return get_template('paste/show-raw.html').render(context)
