# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520706028.1967714
_enable_loop = True
_template_filename = 'themes/custom/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        helper = _mako_get_namespace(context, 'helper')
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        pagination = _mako_get_namespace(context, 'pagination')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        math = _mako_get_namespace(context, 'math')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        helper = _mako_get_namespace(context, 'helper')
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        pagination = _mako_get_namespace(context, 'pagination')
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        def content_header():
            return render_content_header(context)
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        __M_writer('\n<!-- <div class="col-md-3">\n    <div class="card mb-3" style="margin-bottom: 1rem;">\n      <sidebar class="card-header" style="margin-top: 0;text-align:  center;">Random Dots</sidebar>\n      <div class="card-body align-items-center">\n        <h5 class="card-subtitle text-muted" style="color: #9b9596;">I have committed sins, I want to clean myself & work towards becoming a स्थितप्रज्ञस्य"</h5>\n    </div>\n    <img style="max-width: 100%; display: block;" src="/images/shiva.jpg" alt="Card image">\n    <div class="card-footer text-muted">\n        Last Update: ')
        __M_writer(filters.html_escape(str(posts[0].formatted_date(date_format))))
        __M_writer('\n    </div>\n</div> -->\n\n<!-- <ul class="list-group">\n  <li class="list-group-item d-flex justify-content-between align-items-center"><a>\n    Learning Theory</a>\n    <span class="badge badge-primary badge-pill">2</span>\n  </li>\n  <li class="list-group-item d-flex justify-content-between align-items-center">\n    <a>Mathematics</a>\n    <span class="badge badge-primary badge-pill">2</span>\n  </li>\n  <li class="list-group-item d-flex justify-content-between align-items-center">\n    <a>Programming</a>\n    <span class="badge badge-primary badge-pill">1</span>\n  </li>')
        __M_writer('  <li class="list-group-item d-flex justify-content-between align-items-center">\n    <a>Running@2.5km</a>\n    <span class="badge badge-primary badge-pill">10.01min</span>\n  </li>\n</ul> -->\n\n<!-- <div class="card border-primary mb-3">\n  <div class="card-header" style="font-weight: 600;"><sidebar>Quotes</sidebar></div>\n  <div class="card-body">\n    <p class="card-text" style="font-style:  italic;"><h5>The first principle is you must not fool yourself - and your are the most easiest person to fool by yourself<span class="badge badge-secondary badge-pill">Feynman</span></h5></p>\n    <p class="card-text" style="font-style:  italic;"><h5>I\'ve set myself to become the King of Pirates. And if i die trying, at least I tried <span class="badge badge-secondary badge-pill">Luffy</span></h5></p>\n    <p class="card-text" style="font-style:  italic;"><h5>No fear. No distractions. The ability to let that which does not matter truly slide <span class="badge badge-secondary badge-pill">Tyler Durden</span></h5></p>\n  </div>\n</div>\n\n<div class="card border-primary mb-3">\n  <div class="card-header" style="font-weight: 600;"><sidebar>All is one, One is All</sidebar></div>\n  <div class="card-body">\n<!--   \t<p class="card-text" style="font-weight: 400;"><a style="font-size: 0.9em;">In case if you want to know more about me...</a></p>\n -->    <!-- <p class="card-text" style="font-style:  italic;"><h5>I always struggle in aligning thoughts to get the better complete view which will answer everything. So I was trying to figure out the kind of life I want to lead and principles which I should stick to, Surprisingly everything was converging to single point and I was only able to align to one kind of lifestyle. I could clearly see everytime I admire some character I try to see my reflection in them and which makes me even more clear about my life. Such great convergence I could see in the <a>Shiva, Hanuman, Karna, Luffy</a> all have the same core values.</h5></p>  -->\n    \n    <!-- <p class="card-text" style="font-weight: 600;"><a>Shiva, Hanuman, Karna, Luffy</a></p> -->\n   <!--  <p class="card-text" style="font-style:  italic;"><a> Hanuman </a></p>\n    <p class="card-text" style="font-style:  italic;"><a> Karna </a></p>\n    <p class="card-text" style="font-style:  italic;"><a> Monkey D Luffy </a></p> -->\n    <!-- <p class="card-text"><h4>\n    \t<span class="badge badge-secondary badge-pill">Self Control</span>\n    \t<span class="badge badge-secondary badge-pill">Kindness</span>\n    \t<span class="badge badge-secondary badge-pill">Dedication towards their duties(Dharma)</span>\n    \t<span class="badge badge-secondary badge-pill">Selflessness</span>\n    \t<span class="badge badge-secondary badge-pill">Sticking to Promise</span>\n    \t<span class="badge badge-secondary badge-pill">Skill</span>\n    \t<span class="badge badge-secondary badge-pill">Purity</span>\n    \t<span class="badge badge-secondary badge-pill">Stand up for ones who believe in me</span>\n    \t<span class="badge badge-secondary badge-pill"></span></h4></p>\n    <p class="card-text" style="font-style:  italic;"><h5>These core values are all the same for them. I want to lead a life which will make me stick to these core values.</h5></p>\n  </div>\n</div> -->\n\n\n<!-- <div class="card border-success mb-3">\n  <div class="card-header" style="font-weight: 600;"><a>Monkey D Luffy</a></div>\n  <div class="card-body">\n    \n  </div>\n</div>\n\n<div class="card border-secondary mb-3">\n  <div class="card-header" style="font-weight: 600;"><a>Tylor Durden</a></div>\n  <div class="card-body">\n    \n  </div>\n</div> -->\n<!-- </div> -->\n\n\n\n<!-- <div class="col-md-9"> -->\n<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n        <div class="metadata">\n            <!-- <p class="byline author vcard"><span class="byline-name fn" itemprop="author">\n')
            if author_pages_generated:
                __M_writer('                <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('            </span></p> -->\n            <p class="dateline"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time></a></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n    </header>\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('    </div>\n    </article>\n')
        __M_writer('</div>\n<!-- </div> -->\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def content_header():
            return render_content_header(context)
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.translation_link()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "35": 6, "41": 0, "75": 2, "76": 3, "77": 4, "78": 5, "79": 6, "80": 7, "85": 15, "90": 145, "96": 9, "109": 9, "110": 10, "111": 10, "112": 11, "113": 12, "114": 12, "115": 12, "116": 14, "117": 14, "118": 14, "124": 17, "152": 17, "157": 20, "158": 21, "159": 22, "160": 22, "161": 22, "162": 24, "163": 25, "164": 25, "165": 25, "166": 27, "167": 36, "168": 36, "169": 53, "170": 112, "171": 113, "172": 113, "173": 113, "174": 115, "175": 115, "176": 115, "177": 115, "178": 118, "179": 119, "180": 119, "181": 119, "182": 119, "183": 119, "184": 120, "185": 121, "186": 121, "187": 121, "188": 123, "189": 124, "190": 124, "191": 124, "192": 124, "193": 124, "194": 124, "195": 124, "196": 124, "197": 125, "198": 126, "199": 126, "200": 126, "201": 128, "202": 130, "203": 131, "204": 132, "205": 132, "206": 133, "207": 134, "208": 135, "209": 135, "210": 137, "211": 140, "212": 142, "213": 142, "214": 143, "215": 143, "216": 144, "217": 144, "223": 18, "232": 18, "233": 19, "234": 19, "240": 234}}
__M_END_METADATA
"""
