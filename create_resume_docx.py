#!/usr/bin/env python3
"""
Script to create a professionally formatted DOCX resume
"""
import zipfile
import os

def create_resume_docx(filename):
    """Create a DOCX file with resume content"""

    # DOCX is a ZIP file containing XML documents
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as docx:

        # [Content_Types].xml
        content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
    <Default Extension="xml" ContentType="application/xml"/>
    <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
    <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>'''
        docx.writestr('[Content_Types].xml', content_types)

        # _rels/.rels
        rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''
        docx.writestr('_rels/.rels', rels)

        # word/_rels/document.xml.rels
        doc_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>'''
        docx.writestr('word/_rels/document.xml.rels', doc_rels)

        # word/styles.xml
        styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
    <w:docDefaults>
        <w:rPrDefault>
            <w:rPr>
                <w:rFonts w:ascii="Inter" w:hAnsi="Inter" w:cs="Inter"/>
                <w:sz w:val="22"/>
            </w:rPr>
        </w:rPrDefault>
    </w:docDefaults>
    <w:style w:type="paragraph" w:styleId="Normal">
        <w:name w:val="Normal"/>
        <w:rPr>
            <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
            <w:sz w:val="22"/>
        </w:rPr>
    </w:style>
    <w:style w:type="paragraph" w:styleId="Heading1">
        <w:name w:val="Heading 1"/>
        <w:rPr>
            <w:b/>
            <w:sz w:val="40"/>
            <w:color w:val="0F172A"/>
        </w:rPr>
    </w:style>
    <w:style w:type="paragraph" w:styleId="Heading2">
        <w:name w:val="Heading 2"/>
        <w:rPr>
            <w:b/>
            <w:sz w:val="28"/>
            <w:color w:val="6366F1"/>
        </w:rPr>
        <w:pPr>
            <w:spacing w:before="240" w:after="120"/>
        </w:pPr>
    </w:style>
    <w:style w:type="paragraph" w:styleId="Heading3">
        <w:name w:val="Heading 3"/>
        <w:rPr>
            <w:b/>
            <w:sz w:val="24"/>
            <w:color w:val="0F172A"/>
        </w:rPr>
    </w:style>
</w:styles>'''
        docx.writestr('word/styles.xml', styles)

        # word/document.xml - Main content
        document = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
    <w:body>
        <!-- Header / Name -->
        <w:p>
            <w:pPr><w:jc w:val="center"/><w:spacing w:after="120"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="48"/><w:color w:val="6366F1"/></w:rPr>
                <w:t>TOMASZ PLEWNIAK</w:t>
            </w:r>
        </w:p>

        <!-- Title -->
        <w:p>
            <w:pPr><w:jc w:val="center"/><w:spacing w:after="240"/></w:pPr>
            <w:r>
                <w:rPr><w:sz w:val="26"/><w:color w:val="475569"/></w:rPr>
                <w:t>Software Engineer</w:t>
            </w:r>
        </w:p>

        <!-- Contact Info -->
        <w:p>
            <w:pPr><w:jc w:val="center"/><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:sz w:val="20"/></w:rPr>
                <w:t>Bochnia, Poland  •  +48 726 286 367  •  t_plewniak@yahoo.com</w:t>
            </w:r>
        </w:p>

        <w:p>
            <w:pPr><w:jc w:val="center"/><w:spacing w:after="360"/></w:pPr>
            <w:r>
                <w:rPr><w:sz w:val="20"/></w:rPr>
                <w:t>LinkedIn: linkedin.com/in/tomasz-plewniak</w:t>
            </w:r>
        </w:p>

        <!-- Horizontal Line -->
        <w:p>
            <w:pPr>
                <w:pBdr>
                    <w:bottom w:val="single" w:sz="12" w:space="1" w:color="6366F1"/>
                </w:pBdr>
                <w:spacing w:after="240"/>
            </w:pPr>
        </w:p>

        <!-- Summary -->
        <w:p>
            <w:pPr><w:spacing w:after="180"/></w:pPr>
            <w:r>
                <w:rPr><w:sz w:val="22"/></w:rPr>
                <w:t>Dedicated Software Engineer with over 8 years of hands-on experience in designing, developing, and optimizing software solutions. Proven expertise in the full software development lifecycle, from conceptualization to deployment. Adept at leveraging the .NET ecosystem to create scalable and high-performance applications. Demonstrated leadership in collaborating with cross-functional teams to meet project goals. Passionate about staying abreast of industry trends and implementing best practices to drive continuous improvement. Known for problem-solving skills, innovation, and a commitment to delivering high-quality software solutions.</w:t>
            </w:r>
        </w:p>

        <!-- SKILLS Section -->
        <w:p>
            <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="32"/><w:color w:val="6366F1"/></w:rPr>
                <w:t>SKILLS</w:t>
            </w:r>
        </w:p>

        <!-- Core Technologies -->
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="22"/></w:rPr>
                <w:t>Core Technologies</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• .NET Framework &amp; .NET 6/7/8/9</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• C# Language Proficiency</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• Web API &amp; RESTful Services</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="120"/></w:pPr>
            <w:r><w:t>• Entity Framework Core</w:t></w:r>
        </w:p>

        <!-- Cloud & DevOps -->
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="22"/></w:rPr>
                <w:t>Cloud &amp; DevOps</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• Azure Cloud Platform</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• Docker &amp; Containerization</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• GitHub &amp; Azure DevOps</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="120"/></w:pPr>
            <w:r><w:t>• CI/CD Pipelines</w:t></w:r>
        </w:p>

        <!-- Databases -->
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="22"/></w:rPr>
                <w:t>Databases</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• MS SQL Server &amp; T-SQL</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• PostgreSQL</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• NoSQL Databases</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="120"/></w:pPr>
            <w:r><w:t>• Database Design &amp; Optimization</w:t></w:r>
        </w:p>

        <!-- Development Practices -->
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="22"/></w:rPr>
                <w:t>Development Practices &amp; Additional Skills</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• Unit, Integration &amp; Acceptance Testing (XUnit, NSubstitute, TestContainers)</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• Agile Methodologies</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• Code Reviews &amp; Mentoring</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• AI Tools (Cursor, Copilot)</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• Mass Transit &amp; Message Queuing</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="40"/></w:pPr>
            <w:r><w:t>• Third-party API Integration</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:ind w:left="360"/><w:spacing w:after="240"/></w:pPr>
            <w:r><w:t>• Leadership, Cross-functional Collaboration, Problem-solving</w:t></w:r>
        </w:p>

        <!-- PROFESSIONAL EXPERIENCE Section -->
        <w:p>
            <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="32"/><w:color w:val="6366F1"/></w:rPr>
                <w:t>PROFESSIONAL EXPERIENCE</w:t>
            </w:r>
        </w:p>

        <!-- Job 1: Beqom -->
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="24"/></w:rPr>
                <w:t>Senior Back-End Software Engineer</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:i/><w:color w:val="475569"/></w:rPr>
                <w:t>Beqom, Cracow, Poland (Remote) | April 2024 – Present</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="120"/></w:pPr>
            <w:r>
                <w:t>Developing and optimizing scalable back-end solutions for Beqom's compensation management platform. Collaborating with cross-functional teams to design robust APIs, enhance system performance, and ensure seamless integration with front-end services. Leading code reviews, mentoring junior developers, and driving the adoption of best practices in software development.</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="180"/></w:pPr>
            <w:r>
                <w:rPr><w:i/><w:sz w:val="18"/><w:color w:val="6366F1"/></w:rPr>
                <w:t>Tech: C#, .NET 6/8, Web API, Azure, PostgreSQL, NoSQL, EF Core, Mass Transit, Docker, XUnit, NSubstitute, TestContainers</w:t>
            </w:r>
        </w:p>

        <!-- Job 2: TDP -->
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="24"/></w:rPr>
                <w:t>Senior Software Engineer Consultant</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:i/><w:color w:val="475569"/></w:rPr>
                <w:t>TDP, Bochnia, Poland (Remote) | December 2022 – Present</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="120"/></w:pPr>
            <w:r>
                <w:t>Played a significant role in developing and designing innovative solutions for OrderYOYO, enhancing the functionality and performance of their online food ordering platform. Leveraged expertise in the .NET Stack to deliver scalable and efficient solutions.</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="180"/></w:pPr>
            <w:r>
                <w:rPr><w:i/><w:sz w:val="18"/><w:color w:val="6366F1"/></w:rPr>
                <w:t>Tech: C#, .NET 6/7/8/9, .NET Framework, Web API, Azure, MS SQL Server, NoSQL, EF Core, XUnit</w:t>
            </w:r>
        </w:p>

        <!-- Job 3: EPAM -->
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="24"/></w:rPr>
                <w:t>Senior / Lead Software Engineer</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:i/><w:color w:val="475569"/></w:rPr>
                <w:t>EPAM, Cracow, Poland (Hybrid) | October 2019 – November 2022</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="120"/></w:pPr>
            <w:r>
                <w:t>Contributed expertise to projects serving esteemed clients including Swiss Re and First American Corporation. Utilized C# to craft robust and efficient backend services, implemented RESTful APIs, and integrated various third-party APIs.</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="180"/></w:pPr>
            <w:r>
                <w:rPr><w:i/><w:sz w:val="18"/><w:color w:val="6366F1"/></w:rPr>
                <w:t>Tech: C#, .NET 3/5/6, .NET Framework, Web API, Azure, MS SQL Server, PostgreSQL, EF Core</w:t>
            </w:r>
        </w:p>

        <!-- Job 4: Elettric 80 -->
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="24"/></w:rPr>
                <w:t>Software Engineer</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:i/><w:color w:val="475569"/></w:rPr>
                <w:t>Elettric 80, Cracow, Poland | March 2018 – July 2019</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="120"/></w:pPr>
            <w:r>
                <w:t>Played a key role in developing and optimizing software solutions to enhance automation and efficiency within industrial systems. Responsible for delivering and running solutions at client factories including Algida factory in Italy and Dare Foods in Canada.</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="180"/></w:pPr>
            <w:r>
                <w:rPr><w:i/><w:sz w:val="18"/><w:color w:val="6366F1"/></w:rPr>
                <w:t>Tech: C#, .NET Framework, WPF, WCF, WinForms, MS SQL Server, T-SQL, SQLite</w:t>
            </w:r>
        </w:p>

        <!-- Job 5: Igloo -->
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="24"/></w:rPr>
                <w:t>C# Programmer</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:i/><w:color w:val="475569"/></w:rPr>
                <w:t>Igloo, Stary Wiśnicz, Poland | May 2017 – December 2017</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="180"/></w:pPr>
            <w:r>
                <w:t>Responsible for extending internal company systems to provide better support in production and adding new functionality to the company ERP system (MS Axapta).</w:t>
            </w:r>
        </w:p>

        <!-- Job 6: MAKRO -->
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="24"/></w:rPr>
                <w:t>IT &amp; E-commerce Specialist</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:i/><w:color w:val="475569"/></w:rPr>
                <w:t>MAKRO F.H.U, Bochnia, Poland | September 2016 – May 2017</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="240"/></w:pPr>
            <w:r>
                <w:t>Primarily responsible for implementation and support of the company e-shop using popular frameworks, preparation of sales reports and visit statistics via Google Analytics, and daily IT user support.</w:t>
            </w:r>
        </w:p>

        <!-- EDUCATION Section -->
        <w:p>
            <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="32"/><w:color w:val="6366F1"/></w:rPr>
                <w:t>EDUCATION</w:t>
            </w:r>
        </w:p>

        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="22"/></w:rPr>
                <w:t>Master of Engineering in Computer Science</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="120"/></w:pPr>
            <w:r>
                <w:rPr><w:i/></w:rPr>
                <w:t>Cracow University of Technology, Cracow, Poland | 2017</w:t>
            </w:r>
        </w:p>

        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="22"/></w:rPr>
                <w:t>Engineer's Degree in Computer Science</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:after="240"/></w:pPr>
            <w:r>
                <w:rPr><w:i/></w:rPr>
                <w:t>Higher Vocational School in Tarnow, Tarnow, Poland | 2014</w:t>
            </w:r>
        </w:p>

        <!-- LANGUAGES Section -->
        <w:p>
            <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="32"/><w:color w:val="6366F1"/></w:rPr>
                <w:t>LANGUAGES</w:t>
            </w:r>
        </w:p>

        <w:p>
            <w:pPr><w:spacing w:after="60"/></w:pPr>
            <w:r>
                <w:rPr><w:b/></w:rPr>
                <w:t>English</w:t>
            </w:r>
            <w:r>
                <w:t> – Professional working proficiency</w:t>
            </w:r>
        </w:p>

        <w:p>
            <w:pPr><w:spacing w:after="240"/></w:pPr>
            <w:r>
                <w:rPr><w:b/></w:rPr>
                <w:t>Polish</w:t>
            </w:r>
            <w:r>
                <w:t> – Native</w:t>
            </w:r>
        </w:p>

        <!-- CERTIFICATIONS Section -->
        <w:p>
            <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
            <w:r>
                <w:rPr><w:b/><w:sz w:val="32"/><w:color w:val="6366F1"/></w:rPr>
                <w:t>CERTIFICATIONS</w:t>
            </w:r>
        </w:p>

        <w:p>
            <w:pPr><w:spacing w:after="360"/></w:pPr>
            <w:r>
                <w:t>View professional certifications on LinkedIn: linkedin.com/in/tomasz-plewniak</w:t>
            </w:r>
        </w:p>

        <!-- GDPR Notice -->
        <w:p>
            <w:pPr>
                <w:pBdr>
                    <w:top w:val="single" w:sz="6" w:space="1" w:color="E2E8F0"/>
                </w:pBdr>
                <w:spacing w:before="240" w:after="60"/>
            </w:pPr>
            <w:r>
                <w:rPr><w:sz w:val="16"/><w:color w:val="94A3B8"/></w:rPr>
                <w:t>I hereby give consent for my personal data included in my application to be processed for the purposes of the recruitment process under the Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation).</w:t>
            </w:r>
        </w:p>

        <w:sectPr>
            <w:pgSz w:w="11906" w:h="16838"/>
            <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/>
        </w:sectPr>
    </w:body>
</w:document>'''
        docx.writestr('word/document.xml', document)

if __name__ == '__main__':
    output_file = 'Tomasz_Plewniak_Resume_Updated.docx'
    create_resume_docx(output_file)
    print(f'Successfully created {output_file}')
