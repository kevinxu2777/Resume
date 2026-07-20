from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUT = "Jiaqing_Xu_Resume.pdf"
ACCENT = colors.HexColor("#2F5D62")
TEXT = colors.HexColor("#111827")
MUTED = colors.HexColor("#555555")


def section(title):
    return [
        Spacer(1, 8),
        Paragraph(title.upper(), STYLES["section"]),
        Table([[""]], colWidths=[7.2 * inch], rowHeights=[1], style=TableStyle([
            ("LINEBELOW", (0, 0), (-1, -1), 0.8, ACCENT),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ])),
        Spacer(1, 4),
    ]


def role(left, right=None, subtitle=None):
    rows = []
    if right:
        rows.append([
            Paragraph(left, STYLES["role_left"]),
            Paragraph(right, STYLES["role_right"]),
        ])
    else:
        rows.append([Paragraph(left, STYLES["role_left"]), ""])
    if subtitle:
        rows.append([Paragraph(subtitle, STYLES["subtitle"]), ""])
    table = Table(rows, colWidths=[5.15 * inch, 2.05 * inch], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("SPAN", (0, 1), (1, 1)) if subtitle else ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    return table


def bullet(text):
    return Paragraph("- " + text, STYLES["bullet"])


def skill(label, text):
    return Paragraph(f"<b>{label}:</b> {text}", STYLES["body"])


STYLES = {
    "name": ParagraphStyle(
        "name",
        fontName="Times-Bold",
        fontSize=20,
        leading=22,
        alignment=1,
        textColor=colors.HexColor("#1f2f34"),
        spaceAfter=2,
    ),
    "contact": ParagraphStyle(
        "contact",
        fontName="Times-Roman",
        fontSize=10.2,
        leading=12,
        alignment=1,
        textColor=MUTED,
        spaceAfter=8,
    ),
    "summary": ParagraphStyle(
        "summary",
        fontName="Times-Roman",
        fontSize=10.3,
        leading=12.6,
        textColor=TEXT,
        spaceAfter=3,
    ),
    "section": ParagraphStyle(
        "section",
        fontName="Times-Bold",
        fontSize=11.5,
        leading=13,
        textColor=ACCENT,
        spaceAfter=0,
    ),
    "body": ParagraphStyle(
        "body",
        fontName="Times-Roman",
        fontSize=9.8,
        leading=12.2,
        textColor=TEXT,
        spaceAfter=1.4,
    ),
    "role_left": ParagraphStyle(
        "role_left",
        fontName="Times-Bold",
        fontSize=11.2,
        leading=12.8,
        textColor=TEXT,
    ),
    "role_right": ParagraphStyle(
        "role_right",
        fontName="Times-Roman",
        fontSize=10.2,
        leading=12.8,
        alignment=2,
        textColor=TEXT,
    ),
    "subtitle": ParagraphStyle(
        "subtitle",
        fontName="Times-Bold",
        fontSize=10.0,
        leading=11.8,
        textColor=MUTED,
    ),
    "bullet": ParagraphStyle(
        "bullet",
        fontName="Times-Roman",
        fontSize=9.8,
        leading=12.3,
        leftIndent=10,
        firstLineIndent=-7,
        textColor=TEXT,
        spaceAfter=1.1,
    ),
}


def build():
    doc = SimpleDocTemplate(
        OUT,
        pagesize=letter,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.48 * inch,
        bottomMargin=0.48 * inch,
        title="Jiaqing Xu Resume",
        author="Jiaqing Xu",
        subject="Resume",
        creator="ReportLab",
        pageCompression=0,
    )

    story = [
        Paragraph("Jiaqing Xu", STYLES["name"]),
        Paragraph(
            'Greater Boston, MA | kevinxu2777@gmail.com | '
            '<link href="https://github.com/kevinxu2777" color="#2F5D62">'
            "github.com/kevinxu2777</link>",
            STYLES["contact"],
        ),
        Paragraph(
            "Computer Science graduate and junior system administrator with hands-on experience supporting enterprise users, "
            "maintaining operational systems, and building Python automation tools with local dashboards, SQLite persistence, "
            "email alerting, and API integrations.",
            STYLES["summary"],
        ),
    ]

    story += section("Skills")
    story += [
        skill("Programming", "Python, JavaScript, Java, SQL, Go, HTML, CSS"),
        skill("Systems and IT", "Windows PowerShell, SecureCRT, VMware, Nutanix, network switch configuration, ticket triage"),
        skill("Automation and Data", "SQLite, REST APIs, HTML dashboards, SMTP email alerts, macOS LaunchAgents, spreadsheets"),
        skill("Languages", "English (fluent), Chinese (native)"),
    ]

    story += section("Experience")
    story.append(role("HiQ Computers - Onsite at Pfizer, Andover, MA", "Sep 2025 - Present", "Junior System Administrator"))
    story += [
        bullet("Resolve MCS support tickets for Pfizer end users, balancing daily troubleshooting with operational follow-through."),
        bullet("Maintain and support Non-GMP systems and workflows including ETOP, OMEGA, Unanet, and File Transfer."),
        bullet("Troubleshoot CLAN laptops, Nutanix-related requests, user-reported issues, and basic network/switch tasks."),
        bullet("Execute and validate SPEC-related activities according to documented procedures and support expectations."),
        bullet("Build and maintain operational spreadsheets for issue tracking, reporting, asset visibility, and support coordination."),
    ]

    story += section("Selected Projects")
    story.append(role("Market Watch Tool", "Python, SQLite, HTML, SMTP"))
    story += [
        bullet("Built a local market-monitoring system that tracks global news, macro events, equities, commodities, rates, and volatility signals."),
        bullet("Implemented event scoring, deduplication, SQLite history, email alert batching, and a live HTML dashboard with filtering and feedback controls."),
    ]
    story.append(Spacer(1, 3))
    story.append(role("Award Travel Copilot", "Python, CLI, SQLite, APIs"))
    story += [
        bullet("Built a travel-award monitoring workflow that uses seats.aero data to detect new award availability and create actionable email alerts."),
        bullet("Designed local profile logic for points balances, transfer-partner recommendations, credit tracking, and dashboard-based trip review."),
    ]

    story += section("Education")
    story.append(role("Boston University, Boston, MA", "May 2025", "Bachelor of Arts in Computer Science"))

    doc.build(story)


if __name__ == "__main__":
    build()
