#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Audio(object):
    """
    A simple class of audio object
    """
    def __init__(self, channels, sampling_with, sampling_freq, sampling_points, comp_type, comp_desc, audio_seq):
        self._channels = channels
        self._sampling_with = sampling_with
        self._sampling_freq = sampling_freq
        self._sampling_points = sampling_points
        self._comp_type = comp_type
        self._comp_desc = comp_desc
        self._audio_seq = audio_seq

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, value):
        self._channels = value

    @property
    def sampling_with(self):
        return self._sampling_with

    @sampling_with.setter
    def sampling_with(self, value):
        self._sampling_with = value

    @property
    def sampling_freq(self):
        return self._sampling_freq

    @sampling_freq.setter
    def sampling_freq(self, value):
        self._sampling_freq = value

    @property
    def sampling_points(self):
        return self._sampling_points

    @sampling_points.setter
    def sampling_points(self, value):
        self._sampling_points = value

    @property
    def comp_type(self):
        return self._comp_type

    @comp_type.setter
    def comp_type(self, value):
        self._comp_type = value

    @property
    def comp_desc(self):
        return self._comp_desc

    @comp_desc.setter
    def comp_desc(self, value):
        self._comp_desc = value

    @property
    def audio_seq(self):
        return self._audio_seq

    @audio_seq.setter
    def audio_seq(self, value):
        self._audio_seq = value
