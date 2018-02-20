# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519143822.115591
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
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content_header():
            return render_content_header(context._locals(__M_locals))
        pagination = _mako_get_namespace(context, 'pagination')
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        def content():
            return render_content(context._locals(__M_locals))
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
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
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
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
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content_header():
            return render_content_header(context)
        pagination = _mako_get_namespace(context, 'pagination')
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
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
        __M_writer('\n<div class="col-md-3">\n    <div class="card mb-3" style="margin-bottom: 1rem;">\n      <h3 class="card-header" style="margin-top: 0;text-align:  center;">Random Dots</h3>\n      <div class="card-body">\n        <h6 class="card-subtitle text-muted"> "Life\'s simple when you keep it simple"</h6>\n    </div>\n    <img style="max-width: 100%; display: block;" src="/images/7.jpg" alt="Card image">\n    <div class="card-footer text-muted">\n        Last Update: ')
        __M_writer(filters.html_escape(str(posts[0].formatted_date(date_format))))
        __M_writer('\n    </div>\n</div>\n<ul class="list-group">\n  <li class="list-group-item d-flex justify-content-between align-items-center">\n    Learning Theory\n    <span class="badge badge-primary badge-pill">2</span>\n  </li>\n  <li class="list-group-item d-flex justify-content-between align-items-center">\n    Mathematics\n    <span class="badge badge-primary badge-pill">2</span>\n  </li>\n  <li class="list-group-item d-flex justify-content-between align-items-center">\n    Programming\n    <span class="badge badge-primary badge-pill">1</span>\n  </li>\n</ul>\n\n<div class="card text-white bg-primary mb-3">\n  <div class="card-header" style="font-weight: 600;">Richard Feynman</div>\n  <div class="card-body">\n    <p class="card-text" style="font-style:  italic;">The first principle is you must not fool yourself - and your are the most easiest person to fool by yourself</p>\n  </div>\n</div>\n\n<div class="card text-white bg-success mb-3">\n  <div class="card-header" style="font-weight: 600;">Monkey D Luffy</div>\n  <div class="card-body">\n    <p class="card-text" style="font-style:  italic;">I\'ve set myself to become the King of Pirates. And if i die trying, at least I tried.</p>\n  </div>\n</div>\n\n<div class="card text-white bg-secondary mb-3">\n  <div class="card-header" style="font-weight: 600;">Tylor Durden</div>\n  <div class="card-body">\n    <p class="card-text" style="font-style:  italic;">No fear. No distractions. The ability to let that which does not matter truly slide</p>\n  </div>\n</div>\n\n<div class="card border-primary">\n  <div class="card-header"><h4>Inspiring Blogs</h4></div>\n  <div class="text-primary">\n    <a href="https://danieltakeshi.github.io/" class="list-group-item list-group-item-action"> Daniel Seita\'s Blog\n     </a>\n      <a href="https://terrytao.wordpress.com/" class="list-group-item list-group-item-action">\n        Terry Tao\'s Blog\n      </a>\n      <a href="https://gowers.wordpress.com/2007/09/" class="list-group-item list-group-item-action">Gower\'s Blog\n      </a>\n      <a href="https://www.scottaaronson.com/blog/?m=200510" class="list-group-item list-group-item-action">Scott Aronson\'s Blog\n      </a>\n      <a href="http://www.math.ucr.edu/home/baez/README.html" class="list-group-item list-group-item-action">John Bae\'s Stuff\n      </a>\n      <a href="https://jeremykun.com/primers/" class="list-group-item list-group-item-action">Jeremy Kun\'s Blog\n      </a>\n      <a href="http://nuit-blanche.blogspot.in/2016/10/input-convex-neural-networks.html" class="list-group-item list-group-item-action">Nuite Blanche\'s Blog\n      </a>\n      <a href="https://www.revolvy.com/main/index.php?s=List%20of%20theorems&uid=1575" class="list-group-item list-group-item-action">Mathematical Theorem\'s Ocean\n      </a>\n    </div>\n    </div>   \n</div>\n\n<div class="col-md-9">\n<div class="postindex">\n')
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
        __M_writer('</div>\n</div>\n')
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
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.translation_link()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "35": 6, "41": 0, "75": 2, "76": 3, "77": 4, "78": 5, "79": 6, "80": 7, "85": 15, "90": 134, "96": 9, "109": 9, "110": 10, "111": 10, "112": 11, "113": 12, "114": 12, "115": 12, "116": 14, "117": 14, "118": 14, "124": 17, "152": 17, "157": 20, "158": 21, "159": 22, "160": 22, "161": 22, "162": 24, "163": 25, "164": 25, "165": 25, "166": 27, "167": 36, "168": 36, "169": 101, "170": 102, "171": 102, "172": 102, "173": 104, "174": 104, "175": 104, "176": 104, "177": 107, "178": 108, "179": 108, "180": 108, "181": 108, "182": 108, "183": 109, "184": 110, "185": 110, "186": 110, "187": 112, "188": 113, "189": 113, "190": 113, "191": 113, "192": 113, "193": 113, "194": 113, "195": 113, "196": 114, "197": 115, "198": 115, "199": 115, "200": 117, "201": 119, "202": 120, "203": 121, "204": 121, "205": 122, "206": 123, "207": 124, "208": 124, "209": 126, "210": 129, "211": 131, "212": 131, "213": 132, "214": 132, "215": 133, "216": 133, "222": 18, "231": 18, "232": 19, "233": 19, "239": 233}}
__M_END_METADATA
"""
