from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Digital Payments 2025 - UPI Report", ln=True, align="C")
        self.ln(10)

    def add_section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

    def add_image(self, img_path, w=170):
        if os.path.exists(img_path):
            self.image(img_path, w=w)
            self.ln(10)

def create_pdf_report(image_paths, output_pdf='reports/Digital_Payments_Report.pdf'):
    pdf = PDF()
    pdf.set_auto_page_break(auto=False)  # Turn off auto-break for manual control
    pdf.add_page()

    count = 0  # Track number of charts per page

    for title, path in image_paths.items():
        if count == 2:
            pdf.add_page()  # Add new page after every 2 plots
            count = 0

        pdf.add_section_title(title)
        pdf.add_image(path)
        count += 1  # Increment plot count on current page

    pdf.output(output_pdf)
