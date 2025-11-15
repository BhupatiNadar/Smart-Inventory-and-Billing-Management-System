from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

def generate_simple_invoice(invoice_id, customer_name, items, subtotal, tax, grand_total):
    file_name = f"invoice_{invoice_id}.pdf"
    c = canvas.Canvas(file_name, pagesize=A4)

    # Page width for centering
    PAGE_WIDTH = A4[0]

    # Starting Y position (more padding)
    y = 260 * mm  

    # Centered title
    c.setFont("Helvetica-Bold", 20)
    title = "Smart Inventory Store"
    c.drawCentredString(PAGE_WIDTH / 2, y, title)

    y -= 12
    c.setFont("Helvetica", 12)
    c.drawCentredString(PAGE_WIDTH / 2, y, "-" * 40)

    # Customer section (center aligned)
    y -= 20
    c.setFont("Helvetica", 14)
    c.drawCentredString(PAGE_WIDTH / 2, y, f"Customer: {customer_name}")

    import datetime
    today = datetime.date.today().strftime("%d-%m-%Y")

    y -= 18
    c.drawCentredString(PAGE_WIDTH / 2, y, f"Date: {today}")

    # Items Header
    y -= 30
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(PAGE_WIDTH / 2, y, "Items")

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(PAGE_WIDTH / 2, y, "Name        Qty      Price      Total")

    # Items List (centered by adjusting X offset)
    y -= 15
    c.setFont("Helvetica", 12)
    for item in items:
        line = f"{item['name']:<12}   {item['qty']:<5}    {item['price']:<7}    {item['total']}"
        c.drawCentredString(PAGE_WIDTH / 2, y, line)
        y -= 15

    # Separator
    y -= 10
    c.drawCentredString(PAGE_WIDTH / 2, y, "-" * 40)

    # Totals
    y -= 18
    c.drawCentredString(PAGE_WIDTH / 2, y, f"Sub Total:                       {subtotal}")

    y -= 15
    c.drawCentredString(PAGE_WIDTH / 2, y, f"Tax (5%):                         {tax}")

    y -= 15
    c.drawCentredString(PAGE_WIDTH / 2, y, "-" * 40)

    y -= 18
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(PAGE_WIDTH / 2, y, f"Grand Total:                    {grand_total}")

    y -= 18
    c.setFont("Helvetica", 12)
    c.drawCentredString(PAGE_WIDTH / 2, y, "-" * 40)

    # Thank You message
    y -= 30
    c.setFont("Helvetica-Oblique", 14)
    c.drawCentredString(PAGE_WIDTH / 2, y, "Thank you for shopping!")

    c.save()
    return file_name
