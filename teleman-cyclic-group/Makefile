PYTHON ?= python3
BUILD := build
PDF := $(BUILD)/RepThry.pdf
PAGE := $(BUILD)/page4.png
SOURCE := https://math.berkeley.edu/~teleman/math/RepThry.pdf

.PHONY: draft silent clean

draft: $(BUILD)/teleman-cyclic-group-draft.mp4

silent: $(BUILD)/teleman-cyclic-group-draft-silent.mp4

$(PDF):
	mkdir -p $(BUILD)
	curl -L --fail --silent --show-error '$(SOURCE)' -o '$@'

$(PAGE): $(PDF)
	pdftoppm -f 4 -singlefile -png -r 200 '$(PDF)' '$(BUILD)/page4'

$(BUILD)/teleman-cyclic-group-draft-silent.mp4: $(PAGE) render.py
	$(PYTHON) render.py

$(BUILD)/voiceover.wav: voiceover.txt
	mkdir -p $(BUILD)
	espeak -s 165 -p 45 -a 145 -w '$@' -f '$<'

$(BUILD)/teleman-cyclic-group-draft.mp4: $(BUILD)/teleman-cyclic-group-draft-silent.mp4 $(BUILD)/voiceover.wav
	ffmpeg -y -loglevel error -i '$<' -i '$(BUILD)/voiceover.wav' -c:v copy -c:a aac -b:a 128k -t 30 -movflags +faststart '$@'

clean:
	rm -rf $(BUILD)
