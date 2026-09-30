from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor


TITLE_COLOR = RGBColor(15, 23, 42)
ACCENT_COLOR = RGBColor(22, 163, 74)
SECONDARY_COLOR = RGBColor(30, 58, 138)
HIGHLIGHT_COLOR = RGBColor(234, 88, 12)
TEXT_COLOR = RGBColor(51, 65, 81)
LIGHT_BG = RGBColor(248, 250, 252)
WHITE = RGBColor(255, 255, 255)


def set_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_title(slide, title, subtitle=None):
    title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.4), Inches(11.5), Inches(0.8))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.alignment = PP_ALIGN.LEFT
    run = p.runs[0]
    run.font.size = Pt(28)
    run.font.bold = True
    run.font.color.rgb = TITLE_COLOR

    if subtitle:
        subtitle_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.0), Inches(11.5), Inches(0.5))
        stf = subtitle_box.text_frame
        sp = stf.paragraphs[0]
        sp.text = subtitle
        sp.alignment = PP_ALIGN.LEFT
        run2 = sp.runs[0]
        run2.font.size = Pt(14)
        run2.font.color.rgb = RGBColor(71, 85, 105)


def add_bullets(slide, bullets, left=0.9, top=1.6, width=10.8, height=4.7, font_size=20):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    for i, b in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = b
        p.level = 0
        p.bullet = True
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(10)
        run = p.runs[0]
        run.font.size = Pt(font_size)
        run.font.color.rgb = TEXT_COLOR


def add_rounded_box(slide, x, y, w, h, fill_color, line_color=None, radius=0.15):
    # Since python-pptx doesn't support rounded rectangles directly, use a rectangle with a shadow effect
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = Pt(1)
    return shape


from pptx.enum.shapes import MSO_SHAPE


def add_icon_card(slide, title, text, x, y, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(2.2), Inches(1.4))
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.color.rgb = color
    tf = shape.textframe
    tf.text = title + "\n" + text
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf.paragraphs[0].runs[0].font.bold = True
    tf.paragraphs[0].runs[0].font.size = Pt(16)
    tf.paragraphs[0].runs[0].font.color.rgb = WHITE
    tf.paragraphs[1].alignment = PP_ALIGN.CENTER
    tf.paragraphs[1].runs[0].font.size = Pt(10)
    tf.paragraphs[1].runs[0].font.color.rgb = WHITE


def slide_1(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, LIGHT_BG)

    # header strip
    strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.35))
    strip.fill.solid()
    strip.fill.fore_color.rgb = SECONDARY_COLOR
    strip.line.fill.background()

    title_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.0), Inches(11.5), Inches(1.0))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "AI-Powered Automated Waste Classification System"
    p.alignment = PP_ALIGN.LEFT
    run = p.runs[0]
    run.font.size = Pt(28)
    run.font.bold = True
    run.font.color.rgb = TITLE_COLOR

    subtitle = slide.shapes.add_textbox(Inches(0.7), Inches(2.0), Inches(11.0), Inches(0.6))
    stf = subtitle.text_frame
    sp = stf.paragraphs[0]
    sp.text = "Field 5: Safety, Disaster Management & Infrastructure"
    sp.alignment = PP_ALIGN.LEFT
    run2 = sp.runs[0]
    run2.font.size = Pt(18)
    run2.font.color.rgb = TEXT_COLOR

    # small callout box
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.0), Inches(3.2), Inches(1.1))
    box.fill.solid()
    box.fill.fore_color.rgb = ACCENT_COLOR
    box.line.color.rgb = ACCENT_COLOR
    tf2 = box.text_frame
    p2 = tf2.paragraphs[0]
    p2.text = "Smart Waste Segregation"
    p2.alignment = PP_ALIGN.CENTER
    p2.runs[0].font.bold = True
    p2.runs[0].font.size = Pt(18)
    p2.runs[0].font.color.rgb = WHITE

    details = slide.shapes.add_textbox(Inches(0.7), Inches(4.5), Inches(5.0), Inches(1.8))
    dtf = details.text_frame
    for i, text in enumerate([
        "Institution: [Your College/University Name]",
        "Team: [Your Name(s)]",
        "Date: [Insert Date]",
    ]):
        p = dtf.paragraphs[0] if i == 0 else dtf.add_paragraph()
        p.text = text
        p.alignment = PP_ALIGN.LEFT
        p.runs[0].font.size = Pt(16)
        p.runs[0].font.color.rgb = TEXT_COLOR

    # simple illustrative waste icons using shapes
    for x, color, label in [
        (7.6, RGBColor(22, 163, 74), "Recyclable"),
        (9.0, RGBColor(59, 130, 246), "Organic"),
        (10.4, RGBColor(234, 88, 12), "Hazardous"),
    ]:
        card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(2.7), Inches(1.5), Inches(1.5))
        card.fill.solid()
        card.fill.fore_color.rgb = color
        card.line.color.rgb = color
        tf3 = card.text_frame
        p3 = tf3.paragraphs[0]
        p3.text = label
        p3.alignment = PP_ALIGN.CENTER
        p3.runs[0].font.bold = True
        p3.runs[0].font.size = Pt(12)
        p3.runs[0].font.color.rgb = WHITE


def slide_2(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, LIGHT_BG)
    add_title(slide, "Problem Statement", "Waste management challenges in modern cities")

    add_bullets(slide, [
        "Improper waste segregation lowers recycling efficiency and increases landfill usage.",
        "Mixed waste contaminates recyclable materials and reduces their economic value.",
        "Hazardous and electronic waste require specialized handling to protect communities.",
        "Manual sorting is time-consuming, inconsistent, and unsafe for workers.",
        "Rapid urbanization and increased consumption are intensifying waste generation."
    ], left=0.9, top=1.7, width=9.2, height=4.0, font_size=20)

    # side stats box
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.8), Inches(2.0), Inches(2.4), Inches(2.6))
    box.fill.solid()
    box.fill.fore_color.rgb = SECONDARY_COLOR
    box.line.color.rgb = SECONDARY_COLOR
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = 0.12
    tf.margin_right = 0.12
    for i, text in enumerate(["Waste Crisis", "Rising landfills", "Public health risk"]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = text
        p.alignment = PP_ALIGN.CENTER
        p.runs[0].font.bold = True if i == 0 else False
        p.runs[0].font.size = Pt(20 if i == 0 else 14)
        p.runs[0].font.color.rgb = WHITE


def slide_3(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, LIGHT_BG)
    add_title(slide, "Objectives", "Aims of the proposed waste classification system")
    add_bullets(slide, [
        "To develop an AI-based system for automatic waste identification and classification.",
        "To classify waste into recyclable, organic, electronic, hazardous, and general waste.",
        "To improve segregation efficiency, accuracy, and operational safety.",
        "To support sustainable urban infrastructure and smart city development.",
        "To minimize landfill dependency and promote recycling and responsible disposal."
    ], left=0.9, top=1.7, width=10.8, height=4.2, font_size=20)


def slide_4(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, LIGHT_BG)
    add_title(slide, "Proposed Solution", "Computer vision and machine learning for smart segregation")

    # diagram boxes
    boxes = [
        (0.8, 2.0, 2.0, 1.5, SECONDARY_COLOR, "Image Capture"),
        (3.1, 2.0, 2.0, 1.5, RGBColor(59, 130, 246), "Preprocessing"),
        (5.4, 2.0, 2.0, 1.5, RGBColor(22, 163, 74), "AI Model"),
        (7.7, 2.0, 2.0, 1.5, HIGHLIGHT_COLOR, "Classification"),
        (10.0, 2.0, 2.0, 1.5, RGBColor(124, 58, 237), "Sorting"),
    ]
    for x, y, w, h, col, label in boxes:
        sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
        sh.fill.solid()
        sh.fill.fore_color.rgb = col
        sh.line.color.rgb = col
        tf = sh.text_frame
        p = tf.paragraphs[0]
        p.text = label
        p.alignment = PP_ALIGN.CENTER
        p.runs[0].font.size = Pt(12)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = WHITE

    arrow = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(2.9), Inches(2.5), Inches(0.9), Inches(0.5))
    arrow.fill.solid(); arrow.fill.fore_color.rgb = RGBColor(148, 163, 184); arrow.line.color.rgb = RGBColor(148, 163, 184)
    a2 = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(5.2), Inches(2.5), Inches(0.9), Inches(0.5))
    a2.fill.solid(); a2.fill.fore_color.rgb = RGBColor(148, 163, 184); a2.line.color.rgb = RGBColor(148, 163, 184)
    a3 = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(8.5), Inches(2.5), Inches(0.9), Inches(0.5))
    a3.fill.solid(); a3.fill.fore_color.rgb = RGBColor(148, 163, 184); a3.line.color.rgb = RGBColor(148, 163, 184)

    add_bullets(slide, [
        "Waste images are captured using a camera-based system.",
        "The AI model identifies material type and category with confidence scoring.",
        "The system directs waste to the correct bin or disposal stream."
    ], left=1.0, top=4.0, width=10.8, height=2.0, font_size=18)


def slide_5(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, LIGHT_BG)
    add_title(slide, "Methodology", "Workflow for intelligent waste classification")

    add_bullets(slide, [
        "Collect and label waste images from multiple categories.",
        "Preprocess images for consistency in lighting, size, and quality.",
        "Train deep learning models such as CNNs for feature extraction and classification.",
        "Validate results using test data and confidence thresholds.",
        "Deploy the model for real-time prediction and automatic sorting guidance."
    ], left=0.9, top=1.8, width=10.8, height=4.2, font_size=20)


def slide_6(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, LIGHT_BG)
    add_title(slide, "Benefits and Impact", "Social, environmental, and operational advantages")

    cards = [
        (0.8, 2.0, 2.3, 1.4, SECONDARY_COLOR, "Recycling\nEfficiency"),
        (3.5, 2.0, 2.3, 1.4, RGBColor(59, 130, 246), "Cleaner\nCities"),
        (6.2, 2.0, 2.3, 1.4, RGBColor(22, 163, 74), "Hazard\nSafety"),
        (8.9, 2.0, 2.3, 1.4, HIGHLIGHT_COLOR, "Lower\nLandfill"),
    ]
    for x, y, w, h, col, label in cards:
        sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
        sh.fill.solid(); sh.fill.fore_color.rgb = col; sh.line.color.rgb = col
        tf = sh.text_frame
        p = tf.paragraphs[0]
        p.text = label
        p.alignment = PP_ALIGN.CENTER
        p.runs[0].font.size = Pt(16)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = WHITE

    add_bullets(slide, [
        "Improves recycling rates and reduces material contamination.",
        "Minimizes landfill waste and lowers environmental pollution.",
        "Enhances worker and public safety by detecting hazardous items early.",
        "Supports sustainable infrastructure and smart city development."
    ], left=0.9, top=4.0, width=11.0, height=1.8, font_size=18)


def slide_7(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, LIGHT_BG)
    add_title(slide, "Conclusion", "A practical, scalable step toward smarter waste management")
    add_bullets(slide, [
        "The proposed AI-powered waste classification system offers a practical and scalable solution.",
        "It improves segregation accuracy, reduces manual effort, and strengthens environmental safety.",
        "The system supports sustainable waste management and contributes to resilient infrastructure.",
        "By integrating AI with waste management systems, we move closer to a cleaner and safer future."
    ], left=0.9, top=1.8, width=10.8, height=4.2, font_size=20)


def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    slide_1(prs)
    slide_2(prs)
    slide_3(prs)
    slide_4(prs)
    slide_5(prs)
    slide_6(prs)
    slide_7(prs)

    prs.save("waste_classification_ppt.pptx")
    print("PowerPoint file created: waste_classification_ppt.pptx")


if __name__ == "__main__":
    main()
