def extension_to_language(ext:str):
    extension = ext.upper().strip()
    if extension in EXTENSION_TO_LANGUAGE:
        return EXTENSION_TO_LANGUAGE[extension]
    else:
        return extension


# All languages by their file type, grabbed and heavily modified from Wikipedia
# https://en.wikipedia.org/wiki/List_of_file_formats
EXTENSION_TO_LANGUAGE = {
    "1.ADA":"Ada",
    "2.ADA":"Ada",
    "602":"Text602",
    "ABW":"AbiWord",
    "ACL":"MS Word AutoCorrect List",
    "ADA":"Ada",
    "ADB":"Ada",
    "ADS":"Ada",
    "AFP":"IBc",
    "AHK":"AutoHotkey",
    "AMI":"Lostus Ami Pro",
    "ANS":"ANSI text",
    "APPLESCRIPT":"Applescript",
    "AS":"Adobe Flash ActionScript File",
    "ASC":"ASCII text",
    "ASM":"Assembly",
    "AU3":"AutoIt",
    "AWW":"Ability Write",
    "BAS":"BASIC",
    "BAT":"Batch file",
    "BB":"Blitz Basic",
    "BMX":"Blitz Basic",
    "C":"C / C++",
    "CBL":"COBOL source",
    "CBP":"C / C++",
    "CC":"C / C++",
    "CCF":"Color Chat 1.0",
    "CLJ":"Clojure source code",
    "CLJS":"ClojureScript",
    "CLS":"Visual Basic class",
    "CMD":"Batch file",
    "COB":"COBOL source",
    "Coffee":"CoffeeScript",
    "CPP":"C / C++",
    "CS":"C Sharp",
    "CSPROJ":"C Sharp",
    "CSS":"cascading style sheets",
    "CSV":"comma-separated values",
    "CWK":"ClarisWorks / AppleWorks document",
    "CXX":"C / C++",
    "D":"D",
    "DBA":"DarkBASIC source",
    "DBK":"DocBook XML sub-format",
    "DBPro123":"DarkBASIC Professional project",
    "DOC":"Word Document",
    "DOCM":"Word Document",
    "DOCX":"Word Document",
    "DOT":"Microsoft Word document template",
    "DOTX":"Office Open XML text document template",
    "E":"Eiffel",
    "ebuild":"Gentoo linux's portage package.",
    "EFS":"EGT Forever Source File",
    "EGG":"Chicken",
    "EGT":"EGT Universal Document",
    "EL":"Emacs Lisp source",
    "EPUB":"EPUB open standard for e-books",
    "ERB":"Ruby on Rails Script File",
    "F":"Fortran source",
    "F77":"Fortran source",
    "F90":"Fortran source",
    "FDX":"Final Draft",
    "FOR":"Fortran source",
    "FRM":"Visual Basic",
    "FRX":"Visual Basic",
    "FTH":"Forth",
    "FTM":"Fielded Text Meta",
    "FTN":"Fortran source",
    "FTX":"Fielded Text (Declared)",
    "GDOC":"Google Drive Document",
    "GED":"GameMaker Studio",
    "GM6":"GameMaker Studio",
    "GMD":"GameMaker Studio",
    "GMK":"GameMaker Studio",
    "GML":"GameMaker Studio",
    "GITIGNORE":"Git Ignore file",
    "GO":"Go",
    "H":"C / C++",
    "HPP":"C / C++",
    "HS":"Haskell",
    "HTA":"HTA",
    "HTM":"HyperText Markup Language",
    "HTML":"HyperText Markup Language",
    "HWP":"Haansoft (Hancom) Hangul Word Processor document",
    "HWPML":"Haansoft (Hancom) Hangul Word Processor document",
    "HXX":"C / C++",
    "I":"SWIG interface file",
    "IBI":"Icarus script",
    "ICI":"ICI",
    "IJS":"J",
    "INC":"Turbo Pascal included source",
    "INFO":"Texinfo",
    "INI":"configuration file",
    "IPYNB":"Python",
    "ITCL":"Itcl",
    "JAVA":"Java",
    "JS":"JavaScript",
    "JSFL":"JavaScript",
    "JSON":"Json",
    "L":"lex source",
    "LGT":"Logtalk source",
    "LISP":"Common Lisp source",
    "LOG":"Text log file",
    "LUA":"Lua",
    "LWP":"Lotus Word Pro",
    "M":"Objective-C",
    "M4":"M4",
    "MBP":"metadata for Mobipocket documents",
    "MCW":"Word Document",
    "MD":"Markdown document",
    "ML":"Standard ML / OCaml source",
    "Mobi":"Mobipocket documents",
    "MRC":"mIRC Script",
    "N":"Nemerle source",
    "NB":"Mathematica",
    "NBP":"Mathematica",
    "NCF":"NetWare Command File (scripting for Novell's NetWare OS)",
    "NEIS":"학교생활기록부 작성 프로그램(Student Record Writing Program) Document",
    "NUD":"C / C++",
    "NUT":"Squirrel",
    "ODM":"OpenDocument master document",
    "ODT":"OpenDocument text document",
    "OMM":"OmmWriter text document",
    "OTT":"OpenDocument text document template",
    "P":"Pascal",
    "PAGES":"Pages document",
    "PAP":"Papyrus word processor document",
    "PAS":"Pascal",
    "PDAX":"Portable Document Archive (PDA) document index file",
    "PDF":"Portable Document Format",
    "PHP":"PHP",
    "PHP1":"PHP",
    "PHP2":"PHP",
    "PHP3":"PHP",
    "PHP4":"PHP",
    "PHP5":"PHP",
    "PHP6":"PHP",
    "PHP7":"PHP",
    "PHP8":"PHP",
    "PIV":"Pivot stickfigure animator",
    "PL":"Perl",
    "POL":"Apcera Policy Language doclet",
    "PP":"Pascal",
    "PRO":"IDL",
    "PS1":"Windows PowerShell shell script",
    "PS1XML":"Windows PowerShell format and type definitions",
    "PSC1":"Windows PowerShell console file",
    "PSD1":"Windows PowerShell data file",
    "PSM1":"Windows PowerShell module file",
    "PY":"Python",
    "PYC":"Python",
    "PYO":"Python",
    "QUOX":"Question Object File Format for Quobject Designer or Quobject Explorer",
    "R":"R",
    "RB":"Ruby",
    "RC":".NET applications",
    "RC2":".NET applications",
    "RDP":"Remote Desktop Protocol",
    "RED":"Red",
    "REDS":"Red",
    "RESX":".NET applications",
    "RKT":"Racket",
    "RKTL":"Racket",
    "RPT":"Crystal Reports",
    "RTF":"Rich Text document",
    "S":"Assembly language source",
    "SCALA":"Scala",
    "SCE":"Scilab",
    "SCI":"Scilab",
    "SCM":"Scheme",
    "SCPT":"Applescript",
    "SCPTD":"See SCPT.",
    "SD7":"Seed7 source",
    "SDL":"State Description Language",
    "SDW":"StarWriter text document, used in earlier versions of StarOffice",
    "SE":"Shuttle Document",
    "SH":"Shell script",
    "SKB":"Sage Retrieve 4GL",
    "SKC":"Sage Retrieve 4GL",
    "SKD":"Sage Retrieve 4GL",
    "SKF":"Sage Retrieve 4GL",
    "SKG":"Sage Retrieve 4GL",
    "SKI":"Sage Retrieve 4GL",
    "SKK":"Sage Retrieve 4GL",
    "SKM":"Sage Retrieve 4GL",
    "SKO":"Sage Retrieve 4GL",
    "SKP":"Sage Retrieve 4GL",
    "SKQ":"Sage Retrieve 4GL",
    "SKS":"Sage Retrieve 4GL",
    "SKT":"Sage Retrieve 4GL",
    "SKZ":"Sage Retrieve 4GL",
    "SLN":"Visual Studio",
    "SPIN":"Spin",
    "STK":"Stickfigure file for Pivot stickfigure animator",
    "STW":"OpenOffice.org text document template",
    "SWG":"SWIG source code",
    "Sxw":"OpenOffice.org text document",
    "SYJS":"JavaScript",
    "SYPY":"Python",
    "TCL":"Tcl",
    "TeX":"TeX",
    "TSV":"tab-separated values",
    "TXT":"plaintext Text file",
    "UOF":"Uniform Office Format",
    "UOML":"Unique Object Markup Language",
    "VAP":"Visual Studio Analyzer project",
    "VB":"VB.NET",
    "VBG":"Visual Studio compatible project group",
    "VBP":"Visual Basic project",
    "VBPROJ":"Visual Basic .NET project",
    "VBS":"Visual Basic Script",
    "VCPROJ":"C / C++",
    "VDPROJ":"Visual Studio deployment project",
    "VIA":"Revoware VIA Document Project File",
    "VIP":"Visual Basic project",
    "WPD":"WordPerfect document",
    "WPS":"Microsoft Works document",
    "WPT":"Microsoft Works document",
    "WRD":"WordIt! document",
    "WRF":"ThinkFree Office",
    "WRI":"Microsoft Write document",
    "XHTML":"HyperText Markup Language",
    "XML":"eXtensible Markup Language",
    "XPL":"XProc script/pipeline",
    "XQ":"XQuery file",
    "XSL":"XSLT stylesheet",
    "Y":"yacc source",
    "YAML":"Yet Another Markup Language",
    "YML":"Yet Another Markup Language",
    # Some manual additions to fi some more common things
    "PNG":"Image",
    "JPEG":"Image",
    "JPG":"Image",
    "TIFF":"Image",
    "GIF":"Image",
}