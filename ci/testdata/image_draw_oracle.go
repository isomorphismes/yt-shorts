package main

import (
	"fmt"
	"image"
	"image/draw"
	"image/png"
	"os"
	"strconv"
)

func loadPNG(path string) (image.Image, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer f.Close()
	return png.Decode(f)
}

func main() {
	if len(os.Args) != 6 {
		fmt.Fprintln(os.Stderr, "usage: image_draw_oracle BASE SOURCE X Y OUTPUT")
		os.Exit(2)
	}

	base, err := loadPNG(os.Args[1])
	if err != nil {
		panic(err)
	}
	source, err := loadPNG(os.Args[2])
	if err != nil {
		panic(err)
	}
	x, err := strconv.Atoi(os.Args[3])
	if err != nil {
		panic(err)
	}
	y, err := strconv.Atoi(os.Args[4])
	if err != nil {
		panic(err)
	}

	out := image.NewRGBA(base.Bounds())
	draw.Draw(out, out.Bounds(), base, base.Bounds().Min, draw.Src)
	place := image.Rect(x, y, x+source.Bounds().Dx(), y+source.Bounds().Dy())
	draw.Draw(out, place, source, source.Bounds().Min, draw.Over)

	f, err := os.Create(os.Args[5])
	if err != nil {
		panic(err)
	}
	defer f.Close()
	if err := png.Encode(f, out); err != nil {
		panic(err)
	}
}
