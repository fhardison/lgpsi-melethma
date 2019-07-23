MDFILES=$(wildcard *.md)
OUTPUT=$(MDFILES:.md=.html)

.SUFFIXES: .md .html

.md.html:
	pandoc $< -s --template ../lgpsi.html -o ../docs/$@ 



all: $(OUTPUT)


