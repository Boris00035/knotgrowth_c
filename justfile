run:
    uv run python -m main

build:
    uv build
    CFLAGS="-g3 -O0 -fno-omit-frame-pointer" CXXFLAGS="-g3 -O0 -fno-omit-frame-pointer" uv pip install -e . --no-build-isolation --force-reinstall

build_cythonize:
    uv build
    uv pip install -e .

init:
    uv sync

br: build run

matlab_vis:
    matlab -nodisplay -batch "addpath(genpath('src/visualization_matlab')); generate_result"
