{
    "name": "Gestion des étudiants",
    "version": "0.1",
    "category": "Generic Modules/Others",
    "description": """Test création module gestion des étudiants Odoo v14""",
    "author": "Teilhaud",
    "depends": ["base"],
    "data": [
        "data/students_training_data.xml",
        "demo/students_student_data.xml",
        "demo/students_mark_data.xml",
        "views/students_views.xml",
        "views/trainings_views.xml",
        "views/notes_views.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "auto_install": False,
}
