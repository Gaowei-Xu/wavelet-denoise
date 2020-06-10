#!/usr/bin/python3
# -*- coding: utf-8 -*-
from audio import Audio
import numpy as np
import wave
from wtop import WaveletOperator


class AudioStream(object):
    def __init__(self, stream_full_path):
        """
        constructor function
        :param stream_full_path: full path of input audio stream
        """
        self._stream_full_path = stream_full_path
        self._audio = None
        self._wavelet_op = WaveletOperator()

    def load(self):
        """
        load audio from local disk

        :return:
        """
        rf = wave.open(self._stream_full_path, 'rb')

        # 声道数, 量化位数（byte), 采样频率, 采样点数, 压缩类型, 压缩类型的描述
        (channels, sampling_with, sampling_freq, sampling_points, comp_type, comp_desc) = rf.getparams()

        # TODO: here we assume that sampling width is 2 bytes and audio channels equals to 1
        assert sampling_with == 2
        assert channels == 1
        assert sampling_freq == 16000

        audio_seq_str = rf.readframes(sampling_points)
        audio_seq = np.frombuffer(audio_seq_str, dtype=np.short)

        # assign loaded .wav object
        self._audio = Audio(
            channels=channels,
            sampling_with=sampling_with,
            sampling_freq=sampling_freq,
            sampling_points=sampling_points,
            comp_type=comp_type,
            comp_desc=comp_desc,
            audio_seq=audio_seq     # numerical representation of input audio sequence
        )
        rf.close()

    def denoise(self):
        """
        de-noising phase of input audio sequence

        :return: audio object after de-nosing
        """
        denoised_audio_seq = self._wavelet_op.run(input_audio=self._audio)
        self._audio.audio_seq = denoised_audio_seq
        self._audio.sampling_points = denoised_audio_seq.tostring()

    def dump(self, dump_full_path):
        """
        dump the audio wave file after de-nosing into local disk

        :param dump_full_path: dump full path of input audio file after de-noising
        :return:
        """
        wf = wave.open(dump_full_path, 'wb')

        # set wav parameters
        wf.setnchannels(self._audio.channels)
        wf.setsampwidth(self._audio.sampling_with)
        wf.setframerate(self._audio.sampling_freq)

        # dump audio sequence after de-noising
        self._audio.audio_seq = self._audio.audio_seq.astype(np.short)
        wf.writeframes(self._audio.audio_seq.tostring())
        wf.close()


if __name__ == '__main__':
    processor = AudioStream(stream_full_path='../data/对话场景_过滤前.wav')
    processor.load()
    processor.denoise()
    processor.dump(dump_full_path='../data/对话场景_小波过滤后.wav')



