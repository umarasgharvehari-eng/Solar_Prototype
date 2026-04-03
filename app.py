from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_quotation_pdf(profile, appliances, results):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 40

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(40, y, "Pakistan Solar Panel Quotation")
    y -= 30

    pdf.setFont("Helvetica", 11)
    pdf.drawString(40, y, f"Customer: {profile.get('name', 'N/A')}")
    y -= 18
    pdf.drawString(40, y, f"Mobile: {profile.get('mobile', 'N/A')}")
    y -= 18
    pdf.drawString(40, y, f"City: {profile.get('city', 'N/A')}")
    y -= 18
    pdf.drawString(40, y, f"Utility: {profile.get('utility', 'N/A')}")
    y -= 18
    pdf.drawString(40, y, f"System Type: {profile.get('system_type', 'N/A')}")
    y -= 28

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(40, y, "Recommended System")
    y -= 20

    pdf.setFont("Helvetica", 11)
    lines = [
        f"Solar Size: {results.get('solar_size_kw', 0):.2f} kW",
        f"Inverter Size: {results.get('inverter_kw', 0)} kW",
        f"Battery Size: {results.get('battery_kwh', 0):.2f} kWh",
        f"Panel Wattage: {results.get('panel_watt', 0)} W",
        f"Number of Panels: {results.get('panel_count', 0)}",
        f"Monthly Generation: {results.get('monthly_generation', 0):.0f} kWh",
        f"Monthly Savings: PKR {results.get('monthly_savings', 0):,.0f}",
        f"Payback: {results.get('payback_years', 0):.1f} years",
    ]

    for line in lines:
        pdf.drawString(40, y, line)
        y -= 18

    y -= 10
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(40, y, "Cost Breakdown")
    y -= 20

    pdf.setFont("Helvetica", 11)
    cost_lines = [
        f"Solar Panels Cost: PKR {results.get('panel_cost', 0):,.0f}",
        f"Battery Cost: PKR {results.get('battery_cost', 0):,.0f}",
        f"Inverter Cost: PKR {results.get('inverter_cost', 0):,.0f}",
        f"Installation Cost: PKR {results.get('installation_cost', 0):,.0f}",
        f"Structure Cost: PKR {results.get('structure_cost', 0):,.0f}",
        f"BOS / Wiring Cost: PKR {results.get('bos_cost', 0):,.0f}",
        f"Transport Cost: PKR {results.get('transport_cost', 0):,.0f}",
        f"Total Project Cost: PKR {results.get('total_cost', 0):,.0f}",
    ]

    for line in cost_lines:
        pdf.drawString(40, y, line)
        y -= 18

    y -= 10
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(40, y, "Selected Appliances")
    y -= 20

    pdf.setFont("Helvetica", 10)
    for a in appliances[:18]:
        appliance_line = f"{a.get('name')} | {a.get('qty')} x {a.get('watts')}W | {a.get('hours')}h/day"
        pdf.drawString(40, y, appliance_line)
        y -= 15
        if y < 60:
            pdf.showPage()
            y = height - 40
            pdf.setFont("Helvetica", 10)

    pdf.save()
    buffer.seek(0)
    return buffer
