
def check_pdflatex_Arabic():
    from pylatex import Document, Package, Command, NoEscape

    # Create a document using the 'report' class with 11pt font on A4 paper.
    doc = Document(documentclass='report', document_options=['11pt', 'a4paper'])

    # Add necessary packages
    doc.packages.append(Package('inputenc', options='utf8'))
    doc.packages.append(Package('arabtex'))
    doc.packages.append(Package('babel', options='arabic'))

    # Set up the title and author in the preamble.
    doc.preamble.append(Command('title', NoEscape(r'\Huge\textsc{اللغة العربية}')))
    doc.preamble.append(Command('author', 'سالم البوزيدي'))

    # Start the document body.
    doc.append(NoEscape(r'\maketitle'))
    doc.append(NoEscape(r'\tableofcontents'))

    # Add a chapter and a section.
    doc.append(NoEscape(r'\chapter{علوم الحاسوب}'))
    doc.append(NoEscape(r'\section{تاريخ}'))

    # Begin the Arabic text environment.
    doc.append(NoEscape(r'\begin{otherlanguage}{arabic}'))

    # Define the Arabic text (with embedded \textLR commands for Latin words).
    arabic_text = r"""يعود تاريخ علوم الحاسوب إلى اختراع أول حاسوب رقمي حديث. فقبل العشرينات من القرن العشرين، كان مصطلح حاسوب \textLR{Computer} يشير إلى أي أداة بشرية تقوم بعملية الحسابات. ما هي القضايا أو الأشياء التي يمكن لآلة أن تحسبها باتباع قائمة من التعليمات مع ورقة وقلم، دون تحديد للزمن اللازم ودون أي مهارات أو بصيرة (ذكاء)؟ وكان أحد دوافع هذه الدراسات هو تطوير آلات حاسبة \textLR{computing machines} يمكنها إتمام الأعمال الروتينية والعرضة للخطأ البشري عند إجراء حسابات بشرية.
    خلال الأربعينات، مع تطوير آلات حاسبة أكثر قوة وقدرة حسابية، تتطور مصطلح حاسوب ليشير إلى الآلات بدلا من الأشخاص الذين يقومون بالحسابات. وأصبح من الواضح أن الحواسيب يمكنها أن تقوم بأكثر من مجرد عمليات حسابية وبالتالي انتقلوا لدراسة تحسيب أو التحسيب بشكل عام. بدأت المعلوماتية وعلوم الحاسب تأخذ استقلالها كفرع أكاديمي مستقل في الستينات، مع إيجاد أوائل أقسام علوم الحاسب في الجامعات وبدأت الجامعات تعطي إجازات في هذه العلوم [1]."""

    doc.append(NoEscape(arabic_text))

    # End the Arabic language environment.
    doc.append(NoEscape(r'\end{otherlanguage}'))

    # Generate the PDF (and keep the generated .tex file for inspection).
    doc.generate_pdf('arabic_document', clean_tex=False)


check_pdflatex_Arabic()


