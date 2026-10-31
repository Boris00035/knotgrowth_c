cdef extern from "cellular_rearrangement.h":
    void cellular_rearrangement()

def run():
    cellular_rearrangement()