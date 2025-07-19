import os

apps = [
    "accounts", "students", "teachers", "attendance", "assignments",
    "clubs", "resources", "notifications", "forums", "admin_panel", "core"
]

for app in apps:
    print(f"Creating app: {app}")
    os.system(f"python manage.py startapp {app}")
