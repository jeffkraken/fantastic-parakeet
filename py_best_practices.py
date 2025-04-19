from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", style="B", size=12)
        self.cell(0, 10, "Python Best Practices Cheat Sheet", new_x="LMARGIN", new_y="NEXT", align="C")

    def chapter_title(self, title):
        self.set_font("DejaVu", style="B", size=11)
        self.ln(5)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")

    def chapter_body(self, body):
        self.set_font("DejaVu", size=10)
        self.multi_cell(0, 5, body)
        self.ln()

# Initialize PDF
pdf = PDF()

# ✅ Add font before using it
font_path = os.path.join(os.path.dirname(__file__), "DejaVuSans.ttf")

# Optional: Check if font file exists
if not os.path.exists(font_path):
    raise FileNotFoundError(f"Font file not found: {font_path}")

pdf.add_font("DejaVu", "", font_path, uni=True)
pdf.add_font("DejaVu", "B", font_path, uni=True)

# Add first page after fonts are registered
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Content sections
sections = [
    ("1. Docstrings", 'Use triple quotes to explain what a function, class, or script does.\n\nExample:\n'
     'def scan_ports(ip):\n    """Scan all TCP ports on a given IP and return open ports."""'),
    
    ("2. Meaningful Names", 'Avoid vague names like x, y, data. Be descriptive.\n\nExample:\n'
     'def get_user_credentials():\n    ...'),

    ("3. Comments", 'Explain *why* something is done, not what is obviously being done.\n\n'
     '# Retry the request if it times out\nresponse = send_request(retry=True)'),

    ("4. Formatting", 'Follow PEP 8: 4 spaces for indent, under 79 characters per line.\nUse tools like Black or autopep8.'),

    ("5. Constants", 'Use ALL_CAPS for values that shouldn’t change.\n\nMAX_ATTEMPTS = 5'),

    ("6. Avoid Magic Numbers", 'Give important numbers a name so the code is readable.\n\nDEFAULT_TIMEOUT = 10'),

    ("7. List Comprehensions", 'Compact loops for list creation.\n\nports = [p for p in range(1024) if is_open(p)]'),

    ("8. Use `with` for File Access", 'Automatically closes the file.\n\nwith open("log.txt") as f:\n    data = f.read()'),

    ("9. Try/Except for Error Handling", 'Handle errors without crashing the script.\n\n'
     'try:\n    connect_to_db()\nexcept ConnectionError:\n    print("DB unreachable.")'),

    ("10. `if __name__ == '__main__'`", 'Keeps your script modular.\n\n'
     'def main():\n    run_scan()\n\nif __name__ == "__main__":\n    main()'),

    ("Security-Focused Examples", 
     'Avoid hardcoding sensitive info:\n'
     'API_KEY = "1234abcd"\nUse environment variables or config files.\n\n'
     'Validate input before using:\n'
     'def is_valid_ip(ip):\n    return re.match(r"^\\d{1,3}(\\.\\d{1,3}){3}$", ip)\n\n'
     'Use parameterized queries to avoid SQL injection:\n'
     'cursor.execute("SELECT * FROM users WHERE username = ?", (username,))\n\n'
     'Log errors, don’t print sensitive info:\n'
     'except Exception as e:\n    logging.error("Unexpected error", exc_info=True)'),

    ("Bonus Tips", 
     '- Keep functions short and focused\n'
     '- Avoid globals when possible\n'
     '- Test your code in small chunks\n'
     '- Use version control (Git) even for scripts\n')
]

# Add sections to PDF
for title, body in sections:
    pdf.chapter_title(title)
    pdf.chapter_body(body)

# Save PDF to same location as script
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
pdf_filename = os.path.splitext(os.path.basename(script_path))[0] + ".pdf"
pdf_path = os.path.join(script_dir, pdf_filename)
pdf.output(pdf_path)
