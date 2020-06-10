#!/usr/bin/python3
# -*- coding: utf-8 -*-
from audio import Audio
import numpy as np
from scipy.signal import butter, sosfilt
import pywt
import matplotlib.pyplot as plt


class WaveletOperator(object):
    def __init__(self):
        pass

    @staticmethod
    def run(input_audio, wavelet_name='db4'):
        """
        de-noising main phase

        :param input_audio: input audio with
        :param wavelet_name: default wavelet
        :return:
        """
        sequence = input_audio.audio_seq
        mu = np.mean(sequence)
        sigma = np.std(sequence)

        sequence = (sequence - mu) / sigma

        w = pywt.Wavelet(wavelet_name)
        maxlev = pywt.dwt_max_level(len(sequence), w.dec_len)
        coeffs = pywt.wavedec(sequence, wavelet_name, level=maxlev)  # 将信号进行小波分解

        for i in range(1, len(coeffs)):
            bottom_thresh = 0.02
            coeffs[i] = pywt.threshold(
                data=coeffs[i],
                value=bottom_thresh * np.max(coeffs[i]),
                mode='soft',
                substitute=0.0
            )

            upper_thresh = 0.6
            coeffs[i] = pywt.threshold(
                data=coeffs[i],
                value=upper_thresh * np.max(coeffs[i]),
                mode='less',
                substitute=0.6 * np.max(coeffs[i])
            )

        rec_sequence = pywt.waverec(coeffs, wavelet_name)

        rec_sequence = rec_sequence * sigma + mu

        plt.figure(figsize=(12, 8))
        plt.subplot(211)
        plt.plot(input_audio.audio_seq, 'b')
        plt.title('Original input audio sequence')
        plt.subplot(212)
        plt.plot(rec_sequence, 'r')
        plt.title('De-noised audio sequence')
        plt.savefig('./wave_comp.png', dpi=300)

        return rec_sequence
