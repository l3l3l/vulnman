import os
from vulnman.settings import BASE_DIR


LATEX_INTERPRETER = 'latexmk -pdf'

# for some reasons only works with os.path.join and not with pathlib
LATEX_GRAPHICSPATH = [
    os.path.join(BASE_DIR, "apps/reporting/templates/report/assets"),
    os.path.join(BASE_DIR, "uploads/proofs"),
    os.path.join(BASE_DIR, "templates/custom/report/assets")
]

SEVERITY_COLORS = {
    'Critical': {'hex': '9c1720', 'chart_border': 'rgba(156, 23, 32, 1)', 'chart': 'rgba(156, 23, 32, 0.2)'},
    'High': {'hex': 'd13c0f', 'chart_border': 'rgba(209, 60, 15, 1)', 'chart': 'rgba(209, 60, 15, 0.2)'},
    'Medium': {'hex': 'e8971e', 'chart_border': 'rgba(232, 151, 30, 1)', 'chart': 'rgba(232, 151, 30, 0.2)'},
    'Low': {'hex': '2075f5', 'chart_border': 'rgba(32, 117, 245, 1)', 'chart': 'rgba(32, 117, 245, 0.2)'},
    'None': {'hex': '059D1D', 'chart_border': 'rgba(5, 157, 29, 1)', 'chart': 'rgba(5, 157, 29, 0.2)'},
    'Information': {'hex': '059D1D', 'chart_border': 'rgba(5, 157, 29, 1)', 'chart': 'rgba(5, 157, 29, 0.2)'},
}

VULNMAN_CSS_THEME = "vulnman-dark"

HOST_OS_ICONS = {
    "linux": {
        "icon": "fa fa-linux", "matches": ["Ubuntu", "Fedora", "Arch-Linux", "Debian", "Linux"]
    }
}

TAGGIT_CASE_INSENSITIVE = True

CUSTOM_EXTERNAL_TOOLS = {}

REPORT_SECTION_DEFAULTS_DIR = os.path.join(BASE_DIR, "apps/reporting/templates/report/html_default/defaults")

REPORT_SECTIONS = {
    "assessment_overview": os.path.join(REPORT_SECTION_DEFAULTS_DIR, "02_assessment_overview.md"),
    "methodology": os.path.join(REPORT_SECTION_DEFAULTS_DIR, "03_methodology.md")
}
CUSTOM_REPORT_SECTIONS = {}

# API Settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning'
    # 'DEFAULT_RENDERER_CLASSES': [
    #    'rest_framework.renderers.JSONRenderer'
    # ]
}

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

