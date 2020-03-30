# -*- coding: utf-8 -*-
#
# SfePy documentation build configuration file, created by
# sphinx-quickstart on Wed Oct 14 00:02:22 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

## LS: Below walks parent directory and adds all non-excluded to sys.path
#def add_to_sys_path(arg, dirname, fnames):
#    excludes = ('.git',)
#    for exclude in excludes:
#        if exclude not in dirname:
#            sys.path.append(os.path.abspath(dirname))
#
#doc_dir,conf_file = os.path.split(__file__)
#sfepy_dir = os.path.abspath(os.path.join(doc_dir, os.path.pardir))
#os.path.walk(sfepy_dir, add_to_sys_path, None)
sys.path.append(os.path.abspath('sphinxext'))

# This is needed for gen_term_table.
sys.path.append(os.path.abspath('../script'))

import sfepy

numpydoc_path = sfepy.Config().numpydoc_path()

if numpydoc_path is not None:
    sys.path.append(os.path.abspath(numpydoc_path))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autosummary', 'sphinx.ext.autodoc',
              'sphinx.ext.doctest', 'sphinx.ext.imgmath',
              'sphinx.ext.viewcode', 'numpydoc',
              'gen_term_table', 'gen_solver_table',
              'IPython.sphinxext.ipython_console_highlighting',
              'IPython.sphinxext.ipython_directive']
#extensions = ['sphinx.ext.autodoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'SfePy'
copyright = u'2020, Robert Cimrman and SfePy developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

doc_version = sfepy.__version__
aux = doc_version.find('+git.')
if aux >= 0:
    doc_version_page = 'doc'
    doc_version = doc_version[:(aux + 13)]
    doc_version2 = doc_version[:(aux)]
    doc_version2 = 'latest release'
else:
    doc_version_page = 'doc-devel'
    doc_version2 = 'development'

# The short X.Y version.
version = 'version: ' + doc_version
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------
html_logo = './_static/sfepy_logo.png'

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_context = {
    # Enable the "Edit in GitHub link within the header of each page.
    'display_github': False,
    # Set the following variables to generate the resulting github URL for each page.
    # Format Template: https://{{ github_host|default("github.com") }}/{{ github_user }}/{{ github_repo }}/blob/{{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}
    'github_user': 'sfepy',
    'github_repo': 'sfepy',
    'github_version': 'master/doc/',
    'menu_links_name': 'Connections',
    'menu_links': [
        ('<i class="fa fa-newspaper-o fa-fw"></i> News', 'news.html'),
        ('<i class="fa fa-download fa-fw"></i> Downloads', 'downloads.html'),
        ('<i class="fa fa-github fa-fw"></i> Source Code', 'https://github.com/sfepy/sfepy'),
        ('<i class="fa fa-comment fa-fw"></i> Mailing list', 'https://mail.python.org/mailman3/lists/sfepy.python.org'),
        ('<i class="fa fa-bug fa-fw"></i> Bug/issue tracking', 'https://github.com/sfepy/sfepy/issues'),
        ('<i class="fa fa-file-text fa-fw"></i> The Paper', 'https://doi.org/10.1007/s10444-019-09666-0'),
        ('<i class="fa fa-info-circle fa-fw"></i> Docs: %s' % doc_version2, 'https://sfepy.org/%s' % doc_version_page),
    ],
}

html_theme_options = {
    'logo_only': True,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 2,
    'includehidden': True,
    'titles_only': False,
    'display_version': True,
}
# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_style = 'sfepy.css'

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

html_domain_indices = ["py-modindex"]

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'SfePy.tex', u'SfePy Documentation',
   u'Robert Cimrman and Contributors', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX customization.
#
#latex_engine = "xelatex"
latex_elements = {
    'preamble': r'''
\usepackage{bm}
\usepackage{amsfonts}
\def\dt{{\Delta t}}
\def\pdiff#1#2{\frac{\partial {#1}}{\partial {#2}}}
\def\pddiff#1#2{\frac{\partial^2 {#1}}{\partial {#2}^2}}
\def\tdiff#1#2{\frac{{\rm d} {#1}}{{\rm d} {#2}}}
\def\difd#1{\ {\rm d}#1}
\def\intl#1#2{\int \limits_{#1}^{#2}}
\def\eff{^{\rm eff}}
\def\sunm{^{(n-1)}}
\def\suz{^{(0)}}
\newcommand{\dvg}{\mathop{\rm div}}
\newcommand{\tr}{\mathop{\rm tr}}
\newcommand{\ul}[1]{\underline{#1}}
\newcommand{\uld}[1]{\dot{\underline{#1}}}
\newcommand{\ull}[1]{\underline{\underline{#1}}}
\newcommand{\dev}{\mathop{\rm dev}}
\newcommand{\skewop}{\mathop{\rm skew}}
\def\from{\leftarrow}
\def\Vcal{\mathcal{V}}
\def\Tcal{\mathcal{T}}
\def\Ical{\mathcal{I}}
\def\Hcal{\mathcal{H}}
\def\Fcal{\mathcal{F}}
\def\Gcal{\mathcal{G}}
\def\pd{\partial}
\def\ub{\bm{u}}
\def\vb{\bm{v}}
\def\Mb{\bm{M}}
\def\vphib{\bm{\varphi}}
''',
}
# LS: Are the following needed as well?
#\def\Vcal{\mathcal{V}}
#\def\Tcal{\mathcal{T}}
#\def\figDir{../doc/tex/figures}
#"""

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# Preamble for imgmath images
imgmath_latex_preamble = latex_elements['preamble']

# Better math vertical alignment (need LaTeX preview package)
imgmath_use_preview = True

# Turn off numpydoc autosummary tables
numpydoc_show_class_members = False

def process_terms(app, what_, name, obj, options, lines):
    """
    Prepend term call signature(s) into term docstrings.
    """
    if sys.version_info > (3,):
        type_type = type
    else:
        from types import TypeType as type_type

    from sfepy.terms import Term

    if isinstance(obj, type_type):
        if issubclass(obj, Term) and len(obj.name):
            arg_types = obj.arg_types
            if ((len(arg_types) > 1) and not isinstance(arg_types[0], str)):
                arg_types = [u', '.join(['%s' % arg for arg in arg_type])
                             for arg_type in arg_types]
                at_lines = [u'``(%s)``' % arg_type for arg_type in arg_types]

            else:
                arg_types = u', '.join(['%s' % arg for arg in arg_types])
                at_lines = [u'``(%s)``' % arg_types]

            for ii, line in enumerate(lines):
                if line.startswith(':Arguments'):
                    i0 = ii - 1
                    break

            else:
                i0 = 0

            len0 = len(obj.name) + 4
            lines.insert(i0+0, u'')
            lines.insert(i0+1, u':Call signature:')
            lines.insert(i0+2, u'')
            lines.insert(i0+3, (u'=' * len0) + u' ===')
            lines.insert(i0+4, u'**%s** %s' % (obj.name, at_lines[0]))
            for ii, line in enumerate(at_lines[1:]):
                lines.insert(i0+5+ii, u'..' + (' ' * (len0 - 1)) + line)
            lines.insert(i0+4+len(at_lines), (u'=' * len0) + u' ===')
            lines.insert(i0+5+len(at_lines), u'')

    # make sure there is a blank line at the end
    if lines and lines[-1]:
        lines.append(u'')


def setup(app):
    app.connect('autodoc-process-docstring', process_terms)

#
# -- Options for manual pages output ---------------------------------------------------
#
man_pages = [
    ('manpages',
    'sfepy-run',
    'Simple wrapper for main SfePy commands (scripts)',
    'Robert Cimrman and Contributors',
    1)
]
#
