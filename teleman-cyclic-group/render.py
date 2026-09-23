#!/usr/bin/env python3
from __future__ import annotations

import math
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / "build"
PAGE = BUILD / "page4.png"
OUT = BUILD / "teleman-cyclic-group-draft-silent.mp4"
W, H, FPS, DURATION = 720, 1280, 30, 30
FONT = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"

page = Image.open(PAGE).convert("RGB")
PW, PH = page.size

# λ^n = 1 on Teleman PDF p.4, measured from the 200-dpi page render.
TARGET = (417, 1558, 525, 1609)
TX = (TARGET[0] + TARGET[2]) / 2
TY = (TARGET[1] + TARGET[3]) / 2


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def smooth(u):
    u = clamp(u, 0.0, 1.0)
    return u * u * (3 - 2 * u)


def lerp(a, b, u):
    return a + (b - a) * u


def page_view(cx: float, cy: float, scale: float) -> Image.Image:
    src_w = W / scale
    src_h = H / scale
    cx = clamp(cx, src_w / 2, PW - src_w / 2)
    cy = clamp(cy, src_h / 2, PH - src_h / 2)
    box = (
        int(round(cx - src_w / 2)),
        int(round(cy - src_h / 2)),
        int(round(cx + src_w / 2)),
        int(round(cy + src_h / 2)),
    )
    crop = page.crop(box)
    return crop.resize((W, H), Image.Resampling.LANCZOS)


def target_box_in_frame(cx: float, cy: float, scale: float):
    src_w = W / scale
    src_h = H / scale
    cx = clamp(cx, src_w / 2, PW - src_w / 2)
    cy = clamp(cy, src_h / 2, PH - src_h / 2)
    left = cx - src_w / 2
    top = cy - src_h / 2
    x0 = (TARGET[0] - left) * scale
    y0 = (TARGET[1] - top) * scale
    x1 = (TARGET[2] - left) * scale
    y1 = (TARGET[3] - top) * scale
    return x0, y0, x1, y1


def mark_equation(img: Image.Image, cx: float, cy: float, scale: float, strength: float = 1.0):
    draw = ImageDraw.Draw(img, "RGBA")
    x0, y0, x1, y1 = target_box_in_frame(cx, cy, scale)
    pad_x = max(18, 20 * scale)
    pad_y = max(12, 10 * scale)
    alpha = int(235 * clamp(strength, 0, 1))
    width = max(4, int(5 * scale))
    draw.ellipse((x0 - pad_x, y0 - pad_y, x1 + pad_x, y1 + pad_y), outline=(30, 30, 30, alpha), width=width)


def make_plot(t: float) -> Image.Image:
    img = Image.new("RGB", (W, H), (248, 248, 245))
    d = ImageDraw.Draw(img)
    f_big = ImageFont.truetype(FONT, 62)
    f_small = ImageFont.truetype(FONT, 34)
    f_tiny = ImageFont.truetype(FONT, 26)

    title = "λ⁷ = 1"
    bbox = d.textbbox((0, 0), title, font=f_big)
    d.text(((W - (bbox[2]-bbox[0]))/2, 95), title, fill=(25, 25, 25), font=f_big)

    cx, cy, r = W // 2, 610, 250
    d.line((cx-r-35, cy, cx+r+35, cy), fill=(150,150,150), width=2)
    d.line((cx, cy-r-35, cx, cy+r+35), fill=(150,150,150), width=2)
    d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=(40,40,40), width=4)

    pts = []
    for k in range(7):
        a = -2 * math.pi * k / 7
        pts.append((cx + r*math.cos(a), cy + r*math.sin(a)))
    # polygon makes the cyclic structure visually explicit without replacing the unit circle.
    d.line(pts + [pts[0]], fill=(105,105,105), width=3)

    phase = int(max(0, t) / 0.55) % 7
    for k, (x, y) in enumerate(pts):
        rr = 15 if k == phase else 9
        fill = (20,20,20) if k == phase else (95,95,95)
        d.ellipse((x-rr, y-rr, x+rr, y+rr), fill=fill)
        powers = {2: "²", 3: "³", 4: "⁴", 5: "⁵", 6: "⁶"}
        label = "1" if k == 0 else ("ω" if k == 1 else "ω" + powers[k])
        tb = d.textbbox((0,0), label, font=f_tiny)
        dx = 23 if x >= cx else -23 - (tb[2]-tb[0])
        dy = -16 if y <= cy else 8
        d.text((x+dx, y+dy), label, fill=(50,50,50), font=f_tiny)

    cap = "seven roots • one cycle"
    cb = d.textbbox((0,0), cap, font=f_small)
    d.text(((W-(cb[2]-cb[0]))/2, 980), cap, fill=(45,45,45), font=f_small)
    return img


def paper_context() -> Image.Image:
    img = page_view(600, TY, 1.35)
    mark_equation(img, 600, TY, 1.35, 1.0)
    return img


def blend(a: Image.Image, b: Image.Image, u: float):
    return Image.blend(a, b, clamp(u,0,1))


def frame_at(t: float) -> Image.Image:
    # 0–10.8: slow scroll down the Teleman page until λ^n = 1 arrives near center.
    if t < 10.8:
        u = smooth(t / 10.8)
        scale = 0.90
        src_h = H / scale
        start_cy = src_h / 2
        cx = lerp(PW/2, 650, u)
        cy = lerp(start_cy, TY, u)
        img = page_view(cx, cy, scale)
        if t < 2.8:
            d = ImageDraw.Draw(img, "RGBA")
            f = ImageFont.truetype(FONT, 38)
            text = "What does this equation look like?"
            tb = d.textbbox((0,0), text, font=f)
            x0, y0 = 34, 48
            d.rounded_rectangle((x0-16, y0-10, x0+(tb[2]-tb[0])+16, y0+(tb[3]-tb[1])+20), radius=15, fill=(250,250,247,225))
            d.text((x0, y0), text, font=f, fill=(20,20,20,255))
        return img

    # 10.8–13.2: stop and circle the equation.
    if t < 13.2:
        img = page_view(650, TY, 0.90)
        strength = smooth((t - 10.8) / 0.65)
        mark_equation(img, 650, TY, 0.90, strength)
        return img

    # 13.2–15.7: dive into the equation.
    if t < 15.7:
        u = smooth((t - 13.2) / 2.5)
        scale = lerp(0.90, 4.3, u)
        cx = lerp(650, TX, u)
        cy = TY
        img = page_view(cx, cy, scale)
        mark_equation(img, cx, cy, scale, 1-u*0.75)
        return img

    # 15.7–17.4: equation becomes the roots-of-unity picture.
    if t < 17.4:
        u = smooth((t - 15.7) / 1.7)
        a = page_view(TX, TY, 4.3)
        mark_equation(a, TX, TY, 4.3, 0.25)
        b = make_plot(t-15.7)
        return blend(a, b, u)

    # 28.4–30: land on the roots picture with the conclusion.
    if t >= 28.4:
        img = make_plot(t-17.4)
        d = ImageDraw.Draw(img, "RGBA")
        f = ImageFont.truetype(FONT, 39)
        text = "Same group. Different pictures."
        tb = d.textbbox((0,0), text, font=f)
        x = (W-(tb[2]-tb[0]))/2
        y = 1110
        d.rounded_rectangle((x-18, y-12, x+(tb[2]-tb[0])+18, y+(tb[3]-tb[1])+18), radius=13, fill=(248,248,245,225))
        d.text((x,y), text, font=f, fill=(20,20,20,255))
        return img

    # 17.4–28.4: flip between the page and the plot, as if testing one against the other.
    period = 2.35
    local = (t - 17.4) % period
    on_plot = int((t - 17.4) / period) % 2 == 0
    base_a = make_plot(t-17.4) if on_plot else paper_context()
    base_b = paper_context() if on_plot else make_plot(t-17.4)
    # quick soft flip rather than a hard flash
    edge = 0.20
    if local > period - edge:
        return blend(base_a, base_b, smooth((local - (period-edge))/edge))
    img = base_a
    return img


def main():
    BUILD.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(OUT)
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    assert proc.stdin is not None
    for i in range(FPS * DURATION):
        frame = frame_at(i / FPS)
        proc.stdin.write(frame.tobytes())
    proc.stdin.close()
    rc = proc.wait()
    if rc:
        raise SystemExit(rc)
    print(OUT)

if __name__ == "__main__":
    main()
