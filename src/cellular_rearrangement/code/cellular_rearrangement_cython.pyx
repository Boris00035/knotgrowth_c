cdef extern from "cellular_rearrangement.h":
    void cellular_rearrangement(float targetVolume)

def run(float targetVolume):
    cellular_rearrangement(targetVolume)