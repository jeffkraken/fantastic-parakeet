import os
import subprocess
from jinja2 import Environment, FileSystemLoader
from datetime import date

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.tex')

# Define content sections
sections = [
    {
        "title": "1. Docstrings",
        "body": r'''
Use triple quotes to explain what a function, class, or script does.

\begin{verbatim}
def scan_ports(ip):
    """Scan all TCP ports on a given IP and return open ports."""
\end{verbatim}
'''
    },
    {
        "title": "2. Meaningful Names",
        "body": r'''
Avoid vague names like x, y, data. Be descriptive.

\begin{verbatim}
def get_user_credentials():
    ...
\end{verbatim}
'''
    },
    {
        "title": "3. Comments",
        "body": r'''
Explain why something is done, not what is obviously being done.

\begin{verbatim}
# Retry the request if it times out
response = send_request(retry=True)
\end{verbatim}
'''
    },
    {
        "title": "4. Formatting",
        "body": r'''
Follow PEP 8: 4 spaces per indent, and keep lines under 79 characters.

Use auto-formatting tools like Black or autopep8.
'''
    },
    {
        "title": "5. Constants",
        "body": r'''
Use ALL_CAPS for values that shouldn't change.

\begin{verbatim}
MAX_ATTEMPTS = 5
\end{verbatim}
'''
    },
    {
        "title": "6. Avoid Magic Numbers",
        "body": r'''
Give important numbers a name so the code is readable.

\begin{verbatim}
DEFAULT_TIMEOUT = 10
\end{verbatim}
'''
    },
    {
        "title": "7. List Comprehensions",
        "body": r'''
Use list comprehensions for concise loops.

\begin{verbatim}
ports = [p for p in range(1024) if is_open(p)]
\end{verbatim}
'''
    },
    {
        "title": "8. Use `with` for File Access",
        "body": r'''
Using `with` ensures the file is closed automatically.

\begin{verbatim}
with open("log.txt") as f:
    data = f.read()
\end{verbatim}
'''
    },
    {
        "title": "9. Try/Except for Error Handling",
        "body": r'''
Handle errors without crashing your script.

\begin{verbatim}
try:
    connect_to_db()
except ConnectionError:
    print("DB unreachable.")
\end{verbatim}
'''
    },
    {
        "title": "10. `if __name__ == '__main__'`",
        "body": r'''
Keeps your script modular and reusable.

\begin{verbatim}
def main():
    run_scan()

if __name__ == "__main__":
    main()
\end{verbatim}
'''
    }
]

# Template context
context = {
    "title": "Python Best Practices Cheat Sheet",
    "author": "Jeff Krakenberg",
    "date": date.today().strftime("%B %d, %Y"),
    "sections": sections
}

# Render LaTeX content
rendered_tex = template.render(context)

# Write the LaTeX to a file
with open("output.tex", "w", encoding="utf-8") as f:
    f.write(rendered_tex)

# Compile LaTeX to PDF
subprocess.run(["pdflatex", "-interaction=nonstopmode", "output.tex"],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Open the generated PDF
if os.path.exists("output.pdf"):
    os.startfile("output.pdf")
else:
    print("PDF generation failed.")
