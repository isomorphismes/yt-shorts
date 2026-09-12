#!/usr/bin/env python3
from __future__ import annotations

import ctypes as C
import math
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEGERT_COLOR_CORE = (
    ROOT / "third_party" / "wegert" / "app" / "src" / "main" / "assets" / "wegert_color.glsl"
)
OUT = Path(__file__).resolve().parent / "wegert-k-loop.mp4"
W = H = 720
FPS = 30
HOLD_SECONDS = 6
ZOOM_SECONDS = 8
SECONDS = HOLD_SECONDS + ZOOM_SECONDS
FRAMES = FPS * SECONDS
K_PERIOD_SECONDS = 7
START_HALF_HEIGHT = 1.35
END_HALF_HEIGHT = 6.0

# Wegert owns the domain-coloring map. This renderer owns only the mathematical
# function being evaluated. In particular, it does not represent Teleman's
# branch points as Wegert's interactive zero/pole state and it does not patch
# Wegert's palette implementation.
color_core = WEGERT_COLOR_CORE.read_text()

VERTEX = r"""#version 330 core
layout(location = 0) in vec2 a_position;
out vec2 v_ndc;
void main() {
    v_ndc = a_position;
    gl_Position = vec4(a_position, 0.0, 1.0);
}
"""

FRAGMENT = (
    r"""#version 330 core
in vec2 v_ndc;
out vec4 frag_color;
uniform vec2 u_center;
uniform float u_half_height;
uniform float u_aspect;
uniform vec2 u_resolution;
uniform float u_theta;

"""
    + color_core
    + r"""

vec2 complex_mul(vec2 left, vec2 right) {
    return vec2(
        left.x * right.x - left.y * right.y,
        left.x * right.y + left.y * right.x
    );
}

vec2 principal_sqrt(vec2 value) {
    float magnitude = sqrt(length(value));
    float half_phase = 0.5 * atan(value.y, value.x);
    return magnitude * vec2(cos(half_phase), sin(half_phase));
}

vec2 teleman_value(vec2 z, float theta) {
    // w(z;k) = sqrt((z^2 - 1)(z^2 - k^2)), with k moving once around |k|=1.
    vec2 one = vec2(1.0, 0.0);
    vec2 k = vec2(cos(theta), sin(theta));
    vec2 z_squared = complex_mul(z, z);
    vec2 k_squared = complex_mul(k, k);
    vec2 product = complex_mul(z_squared - one, z_squared - k_squared);
    return principal_sqrt(product);
}

void main() {
    vec2 z = u_center + vec2(
        v_ndc.x * u_half_height * u_aspect,
        v_ndc.y * u_half_height
    );
    vec2 value = teleman_value(z, u_theta);
    vec3 color = wegert_color_complex(value);

    // Parameter guide only: one visible k moves around |k|=1. This is not
    // Wegert's zero/pole UI and does not alter the function evaluation above.
    // Keep the guide about one screen pixel wide as the camera zooms out.
    float world_per_pixel = (2.0 * u_half_height) / max(u_resolution.y, 1.0);
    float unit_circle_pixels = abs(length(z) - 1.0) / world_per_pixel;
    float guide_mix = 0.78 * (1.0 - smoothstep(0.55, 1.35, unit_circle_pixels));
    color = mix(color, vec3(1.0), guide_mix);

    // A small plain white point with a dark rim. No bullseye or zero marker.
    vec2 k = vec2(cos(u_theta), sin(u_theta));
    float k_radius_pixels = length(z - k) / world_per_pixel;
    if (k_radius_pixels < 5.2) {
        color = k_radius_pixels < 3.6 ? vec3(1.0) : vec3(0.06);
    }

    frag_color = vec4(color, 1.0);
}
"""
)

EGL_DEFAULT_DISPLAY = C.c_void_p(0)
EGL_NO_SURFACE = C.c_void_p(0)
EGL_NO_CONTEXT = C.c_void_p(0)
EGL_NONE = 0x3038
EGL_SURFACE_TYPE = 0x3033
EGL_PBUFFER_BIT = 0x0001
EGL_RENDERABLE_TYPE = 0x3040
EGL_OPENGL_BIT = 0x0008
EGL_RED_SIZE = 0x3024
EGL_GREEN_SIZE = 0x3023
EGL_BLUE_SIZE = 0x3022
EGL_ALPHA_SIZE = 0x3021
EGL_WIDTH = 0x3057
EGL_HEIGHT = 0x3056
EGL_OPENGL_API = 0x30A2

GL_VERTEX_SHADER = 0x8B31
GL_FRAGMENT_SHADER = 0x8B30
GL_COMPILE_STATUS = 0x8B81
GL_LINK_STATUS = 0x8B82
GL_INFO_LOG_LENGTH = 0x8B84
GL_ARRAY_BUFFER = 0x8892
GL_STATIC_DRAW = 0x88E4
GL_FLOAT = 0x1406
GL_FALSE = 0
GL_TRIANGLE_STRIP = 0x0005
GL_RGBA = 0x1908
GL_UNSIGNED_BYTE = 0x1401

os.environ.setdefault("EGL_PLATFORM", "surfaceless")
egl = C.CDLL("libEGL.so.1")
gl = C.CDLL("libGL.so.1")


def proto(lib, name, restype, *args):
    function = getattr(lib, name)
    function.restype = restype
    function.argtypes = list(args)
    return function


eglGetDisplay = proto(egl, "eglGetDisplay", C.c_void_p, C.c_void_p)
eglInitialize = proto(egl, "eglInitialize", C.c_uint, C.c_void_p, C.POINTER(C.c_int), C.POINTER(C.c_int))
eglChooseConfig = proto(egl, "eglChooseConfig", C.c_uint, C.c_void_p, C.POINTER(C.c_int), C.POINTER(C.c_void_p), C.c_int, C.POINTER(C.c_int))
eglCreatePbufferSurface = proto(egl, "eglCreatePbufferSurface", C.c_void_p, C.c_void_p, C.c_void_p, C.POINTER(C.c_int))
eglBindAPI = proto(egl, "eglBindAPI", C.c_uint, C.c_uint)
eglCreateContext = proto(egl, "eglCreateContext", C.c_void_p, C.c_void_p, C.c_void_p, C.c_void_p, C.POINTER(C.c_int))
eglMakeCurrent = proto(egl, "eglMakeCurrent", C.c_uint, C.c_void_p, C.c_void_p, C.c_void_p, C.c_void_p)
eglDestroySurface = proto(egl, "eglDestroySurface", C.c_uint, C.c_void_p, C.c_void_p)
eglDestroyContext = proto(egl, "eglDestroyContext", C.c_uint, C.c_void_p, C.c_void_p)
eglTerminate = proto(egl, "eglTerminate", C.c_uint, C.c_void_p)

glCreateShader = proto(gl, "glCreateShader", C.c_uint, C.c_uint)
glShaderSource = proto(gl, "glShaderSource", None, C.c_uint, C.c_int, C.POINTER(C.c_char_p), C.POINTER(C.c_int))
glCompileShader = proto(gl, "glCompileShader", None, C.c_uint)
glGetShaderiv = proto(gl, "glGetShaderiv", None, C.c_uint, C.c_uint, C.POINTER(C.c_int))
glGetShaderInfoLog = proto(gl, "glGetShaderInfoLog", None, C.c_uint, C.c_int, C.POINTER(C.c_int), C.c_char_p)
glCreateProgram = proto(gl, "glCreateProgram", C.c_uint)
glAttachShader = proto(gl, "glAttachShader", None, C.c_uint, C.c_uint)
glLinkProgram = proto(gl, "glLinkProgram", None, C.c_uint)
glGetProgramiv = proto(gl, "glGetProgramiv", None, C.c_uint, C.c_uint, C.POINTER(C.c_int))
glGetProgramInfoLog = proto(gl, "glGetProgramInfoLog", None, C.c_uint, C.c_int, C.POINTER(C.c_int), C.c_char_p)
glUseProgram = proto(gl, "glUseProgram", None, C.c_uint)
glGenVertexArrays = proto(gl, "glGenVertexArrays", None, C.c_int, C.POINTER(C.c_uint))
glBindVertexArray = proto(gl, "glBindVertexArray", None, C.c_uint)
glGenBuffers = proto(gl, "glGenBuffers", None, C.c_int, C.POINTER(C.c_uint))
glBindBuffer = proto(gl, "glBindBuffer", None, C.c_uint, C.c_uint)
glBufferData = proto(gl, "glBufferData", None, C.c_uint, C.c_ssize_t, C.c_void_p, C.c_uint)
glEnableVertexAttribArray = proto(gl, "glEnableVertexAttribArray", None, C.c_uint)
glVertexAttribPointer = proto(gl, "glVertexAttribPointer", None, C.c_uint, C.c_int, C.c_uint, C.c_uint, C.c_int, C.c_void_p)
glGetUniformLocation = proto(gl, "glGetUniformLocation", C.c_int, C.c_uint, C.c_char_p)
glUniform2f = proto(gl, "glUniform2f", None, C.c_int, C.c_float, C.c_float)
glUniform1f = proto(gl, "glUniform1f", None, C.c_int, C.c_float)
glViewport = proto(gl, "glViewport", None, C.c_int, C.c_int, C.c_int, C.c_int)
glDrawArrays = proto(gl, "glDrawArrays", None, C.c_uint, C.c_int, C.c_int)
glReadPixels = proto(gl, "glReadPixels", None, C.c_int, C.c_int, C.c_int, C.c_int, C.c_uint, C.c_uint, C.c_void_p)
glFinish = proto(gl, "glFinish", None)


def compile_shader(kind, text):
    shader = glCreateShader(kind)
    encoded = text.encode()
    pointer = C.c_char_p(encoded)
    glShaderSource(shader, 1, C.byref(pointer), None)
    glCompileShader(shader)
    ok = C.c_int()
    glGetShaderiv(shader, GL_COMPILE_STATUS, C.byref(ok))
    if not ok.value:
        length = C.c_int()
        glGetShaderiv(shader, GL_INFO_LOG_LENGTH, C.byref(length))
        message = C.create_string_buffer(max(length.value, 1))
        glGetShaderInfoLog(shader, len(message), None, message)
        raise RuntimeError(message.value.decode(errors="replace"))
    return shader


def smoothstep01(value: float) -> float:
    value = min(max(value, 0.0), 1.0)
    return value * value * (3.0 - 2.0 * value)


def camera_half_height(frame: int) -> float:
    elapsed = frame / FPS
    if elapsed <= HOLD_SECONDS:
        return START_HALF_HEIGHT

    zoom_fraction = smoothstep01((elapsed - HOLD_SECONDS) / ZOOM_SECONDS)
    # Interpolate logarithmically so the apparent zoom speed is smooth rather
    # than spending most of the shot at the wide end.
    return math.exp(
        math.log(START_HALF_HEIGHT)
        + zoom_fraction * (math.log(END_HALF_HEIGHT) - math.log(START_HALF_HEIGHT))
    )


display = eglGetDisplay(EGL_DEFAULT_DISPLAY)
major = C.c_int()
minor = C.c_int()
if not display or not eglInitialize(display, C.byref(major), C.byref(minor)):
    raise SystemExit("EGL initialization failed")

attributes = (C.c_int * 15)(
    EGL_SURFACE_TYPE, EGL_PBUFFER_BIT,
    EGL_RENDERABLE_TYPE, EGL_OPENGL_BIT,
    EGL_RED_SIZE, 8,
    EGL_GREEN_SIZE, 8,
    EGL_BLUE_SIZE, 8,
    EGL_ALPHA_SIZE, 8,
    EGL_NONE, 0, 0,
)
config = C.c_void_p()
config_count = C.c_int()
if not eglChooseConfig(display, attributes, C.byref(config), 1, C.byref(config_count)) or config_count.value < 1:
    raise SystemExit("No OpenGL pbuffer configuration")

pbuffer_attributes = (C.c_int * 5)(EGL_WIDTH, W, EGL_HEIGHT, H, EGL_NONE)
surface = eglCreatePbufferSurface(display, config, pbuffer_attributes)
if not surface:
    raise SystemExit("Pbuffer creation failed")
if not eglBindAPI(EGL_OPENGL_API):
    raise SystemExit("eglBindAPI failed")
context_attributes = (C.c_int * 1)(EGL_NONE)
context = eglCreateContext(display, config, EGL_NO_CONTEXT, context_attributes)
if not context:
    raise SystemExit("OpenGL context creation failed")
if not eglMakeCurrent(display, surface, surface, context):
    raise SystemExit("eglMakeCurrent failed")

vertex_shader = compile_shader(GL_VERTEX_SHADER, VERTEX)
fragment_shader = compile_shader(GL_FRAGMENT_SHADER, FRAGMENT)
program = glCreateProgram()
glAttachShader(program, vertex_shader)
glAttachShader(program, fragment_shader)
glLinkProgram(program)
ok = C.c_int()
glGetProgramiv(program, GL_LINK_STATUS, C.byref(ok))
if not ok.value:
    length = C.c_int()
    glGetProgramiv(program, GL_INFO_LOG_LENGTH, C.byref(length))
    message = C.create_string_buffer(max(length.value, 1))
    glGetProgramInfoLog(program, len(message), None, message)
    raise RuntimeError(message.value.decode(errors="replace"))
glUseProgram(program)

vertices = (C.c_float * 8)(-1, -1, 1, -1, -1, 1, 1, 1)
vao = C.c_uint()
vbo = C.c_uint()
glGenVertexArrays(1, C.byref(vao))
glBindVertexArray(vao)
glGenBuffers(1, C.byref(vbo))
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, C.sizeof(vertices), C.cast(vertices, C.c_void_p), GL_STATIC_DRAW)
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)


def uniform(name):
    location = glGetUniformLocation(program, name.encode())
    if location < 0:
        raise RuntimeError(f"missing shader uniform: {name}")
    return location


locations = {name: uniform(name) for name in (
    "u_center", "u_half_height", "u_aspect", "u_resolution", "u_theta",
)}
glUniform2f(locations["u_center"], 0.0, 0.0)
glUniform1f(locations["u_aspect"], 1.0)
glUniform2f(locations["u_resolution"], W, H)
glViewport(0, 0, W, H)

ffmpeg = subprocess.Popen([
    "ffmpeg", "-y", "-loglevel", "error",
    "-f", "rawvideo", "-pixel_format", "rgba",
    "-video_size", f"{W}x{H}", "-framerate", str(FPS), "-i", "-",
    "-vf", "vflip", "-an", "-c:v", "libx264", "-preset", "veryfast",
    "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(OUT),
], stdin=subprocess.PIPE)

pixels = (C.c_ubyte * (W * H * 4))()
for frame in range(FRAMES):
    elapsed = frame / FPS
    theta = 2.0 * math.pi * elapsed / K_PERIOD_SECONDS
    glUniform1f(locations["u_theta"], theta)
    glUniform1f(locations["u_half_height"], camera_half_height(frame))
    glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)
    glFinish()
    glReadPixels(0, 0, W, H, GL_RGBA, GL_UNSIGNED_BYTE, pixels)
    ffmpeg.stdin.write(bytes(pixels))

ffmpeg.stdin.close()
if ffmpeg.wait():
    raise SystemExit("ffmpeg failed")

eglMakeCurrent(display, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT)
eglDestroySurface(display, surface)
eglDestroyContext(display, context)
eglTerminate(display)
print(OUT)
