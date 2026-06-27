from docx.shared import Pt, RGBColor, Inches
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
MID='002855'; BLUE='005EB8'; TEXT='333333'
def rgb(h): return RGBColor(int(h[0:2],16),int(h[2:4],16),int(h[4:6],16))
def setup(doc):
    sec=doc.sections[0]; sec.page_width=Inches(8.5); sec.page_height=Inches(11); sec.top_margin=Inches(.7); sec.bottom_margin=Inches(.7); sec.left_margin=Inches(.75); sec.right_margin=Inches(.75); sec.header_distance=Inches(.3); sec.footer_distance=Inches(.3)
    styles=doc.styles
    for name,size,color,bold in [('Title',30,MID,True),('Subtitle',18,BLUE,True),('Heading 1',21,MID,True),('Heading 2',16,BLUE,True),('Heading 3',12.5,MID,True),('Caption',9,'555555',False),('Normal',10.5,TEXT,False)]:
        st=styles[name]; st.font.name='Aptos Display' if name in ('Title','Subtitle') else 'Aptos'; st.font.size=Pt(size); st.font.color.rgb=rgb(color); st.font.bold=bold
        if hasattr(st,'paragraph_format'):
            st.paragraph_format.space_after=Pt(6); st.paragraph_format.line_spacing=1.1
            if name.startswith('Heading'): st.paragraph_format.keep_with_next=True
