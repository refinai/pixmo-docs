import subprocess
import tempfile
import os
from pylatex import Document, Command, NoEscape

os.environ['PATH'] += os.pathsep + '/usr/local/bin/latexmk'

print(os.environ['PATH'])
# def compile_latex(latex_file):
#     # Run pdflatex to compile the LaTeX document
#     result = subprocess.run(['pdflatex', latex_file], capture_output=True, text=True)
    
#     # Print the standard output and error messages
#     print(result.stdout)
#     print(result.stderr)

# # Call the function with your LaTeX file
# compile_latex('/var/folders/l1/hs11_20n30zdjlygtqqglg2r0000gn/T/tmpha065fw_/test_document.tex')

# os.environ['PATH'] += '/usr/local/texlive/2024/bin/universal-darwin'  # Change this path if necessary

def check_pdflatex():
    # Create temporary directory
    temp_dir = tempfile.mkdtemp()

    try:
        doc = Document("basic")
        doc.preamble.append(Command("title", "Awesome Title"))
        doc.append(NoEscape(r"\maketitle"))
        doc.append(r"This is a test document to check if pdflatex is available.")
        doc.generate_pdf(
            os.path.join(temp_dir, "test_document"), clean=True, clean_tex=False
        )
    except subprocess.CalledProcessError as e:
        print("Error output:", e.stderr)
        raise RuntimeError(
            f"Your system must have pdflatex installed to run this pipeline: {e}"
        )
    except Exception as e:
        raise RuntimeError(
            f"Your system must have pdflatex installed to run this pipeline: {e}"
        )

check_pdflatex()


